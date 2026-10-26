#!/usr/bin/env python3
"""Intraday brief for Hyperliquid perps, built only from the keyless /info API.

Sections are fixed: HTF bias, intraday regime/value, three conditional setups,
one risk line. No predictions. A parse failure prints the raw JSON and exits 2.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import analytics
import brief as brief_mod
import hl_api
import levels as lv
import notify
import parse as hl_parse
from parse import MissingFieldError

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output"
DATA_DIR = ROOT / "data"
OI_STORE = DATA_DIR / "oi_snapshots.jsonl"

HOUR_MS = 3_600_000
DAY_MS = 86_400_000
PAYLOAD_KEYS = (
    "candles_1h",
    "candles_5m",
    "meta_and_asset_ctxs",
    "funding_history",
    "predicted_fundings",
)


# ---------------------------------------------------------------------- input
def parse_as_of(value: str | None) -> int:
    if not value:
        return int(time.time() * 1000)
    text = value.strip().replace("Z", "+00:00")
    stamp = datetime.fromisoformat(text)
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return int(stamp.timestamp() * 1000)


def parse_offset(value: str | None) -> int:
    """'+05:30' -> 330. A fixed offset avoids needing the tzdata package on Windows."""
    if not value:
        return 0
    text = value.strip().upper().replace("UTC", "").replace("GMT", "")
    if text in ("", "Z", "+0", "-0"):
        return 0
    sign = -1 if text.startswith("-") else 1
    text = text.lstrip("+-")
    hours, _, minutes = text.partition(":")
    try:
        return sign * (int(hours) * 60 + int(minutes or 0))
    except ValueError:
        raise SystemExit(f"bad --display-offset {value!r}; try +05:30 or -08:00") from None


def collect(symbol: str, as_of: int, offline: str | None) -> tuple[dict, hl_api.RawVault]:
    vault = hl_api.RawVault()
    if offline:
        base = Path(offline)
        payloads = {}
        for key in PAYLOAD_KEYS:
            path = base / f"{key}.json"
            if not path.exists():
                raise FileNotFoundError(f"offline fixture missing: {path}")
            payloads[key] = json.loads(path.read_text(encoding="utf-8"))
            vault.put(key, {"offline": str(path)}, payloads[key])
        return payloads, vault

    payloads = {
        "candles_1h": hl_api.fetch_candles(
            symbol, "1h", as_of - 35 * DAY_MS, as_of, vault=vault, key="candles_1h"
        ),
        "candles_5m": hl_api.fetch_candles(
            symbol, "5m", as_of - 3 * DAY_MS, as_of, vault=vault, key="candles_5m"
        ),
        "meta_and_asset_ctxs": hl_api.fetch_asset_ctxs(vault=vault, key="meta_and_asset_ctxs"),
        "funding_history": hl_api.fetch_funding_history(
            symbol, as_of - 30 * DAY_MS, vault=vault, key="funding_history"
        ),
        "predicted_fundings": hl_api.fetch_predicted_fundings(vault=vault, key="predicted_fundings"),
    }
    return payloads, vault


# ------------------------------------------------------------- open interest
def read_oi_store(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if (
            isinstance(row, dict)
            and isinstance(row.get("ts"), (int, float))
            and isinstance(row.get("oi"), (int, float))
        ):
            rows.append(row)
    return rows


def oi_changes(rows: list[dict], symbol: str, as_of: int, current_oi: float) -> tuple[float | None, float | None]:
    """(delta vs last stored run, delta vs ~24h ago). None when no baseline exists."""
    series = sorted(
        (row for row in rows if str(row.get("symbol", "")).upper() == symbol.upper()),
        key=lambda row: row["ts"],
    )
    previous_pct = None
    if series and series[-1]["oi"]:
        previous_pct = (current_oi / series[-1]["oi"] - 1.0) * 100.0

    target = as_of - DAY_MS
    best = None
    for row in series:
        if row["ts"] > as_of - DAY_MS / 2:  # must be at least 12h old to count as a day baseline
            continue
        if best is None or abs(row["ts"] - target) < abs(best["ts"] - target):
            best = row
    day_pct = None
    if best is not None and abs(best["ts"] - target) <= 6 * HOUR_MS and best["oi"]:
        day_pct = (current_oi / best["oi"] - 1.0) * 100.0
    return previous_pct, day_pct


def append_oi(path: Path, symbol: str, as_of: int, open_interest: float, mark: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"ts": as_of, "symbol": symbol, "oi": open_interest, "mark": mark}) + "\n")


# ---------------------------------------------------------------------- build
def build_book(payloads: dict, symbol: str, as_of: int, args: argparse.Namespace) -> analytics.LevelBook:
    candles_1h = hl_parse.parse_candles(
        payloads["candles_1h"], path="candles_1h", interval="1h", coin=symbol
    )
    candles_5m = hl_parse.parse_candles(
        payloads["candles_5m"], path="candles_5m", interval="5m", coin=symbol
    )
    ctx = hl_parse.parse_asset_ctx(payloads["meta_and_asset_ctxs"], symbol)
    funding = hl_parse.parse_funding_history(payloads["funding_history"])
    venues = hl_parse.parse_predicted_fundings(payloads["predicted_fundings"], symbol)

    warnings = hl_parse.candle_gap_warnings(candles_1h, HOUR_MS)
    warnings += hl_parse.candle_gap_warnings(candles_5m, 5 * 60_000)

    rows = read_oi_store(OI_STORE)
    previous_pct, day_pct = oi_changes(rows, symbol, as_of, ctx.open_interest)

    return analytics.compute(
        symbol=symbol,
        as_of=as_of,
        candles_1h=candles_1h,
        candles_5m=candles_5m,
        ctx=ctx,
        funding_history=funding,
        funding_venues=venues,
        session_start_hour=args.session_start_hour,
        va_days=args.va_days,
        va_percent=args.va_percent,
        bucket=args.bucket,
        oi_prev_pct=previous_pct,
        oi_24h_pct=day_pct,
        warnings=warnings,
        min_rr=args.min_rr,
    )


def book_to_dict(book: analytics.LevelBook) -> dict:
    data = dataclasses.asdict(book)
    data["setups"] = [
        {
            **dataclasses.asdict(setup),
            "risk": setup.risk,
            "rr1": setup.rr1,
            "rr2": setup.rr2,
            "stand_aside": setup.stand_aside,
        }
        for setup in book.setups
    ]
    return data


def save(book: analytics.LevelBook, text: str, levels: dict) -> tuple[Path, Path, Path]:
    """Write the published plan: latest.md/latest.json plus a per-day archive copy."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "archive").mkdir(exist_ok=True)
    md_path = OUTPUT_DIR / "latest.md"
    json_path = OUTPUT_DIR / "latest.json"
    md_path.write_text(text + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(levels, indent=2), encoding="utf-8")
    archive_path = OUTPUT_DIR / "archive" / f"{levels['day']}.md"
    archive_path.write_text(text + "\n", encoding="utf-8")
    return md_path, json_path, archive_path


def dump_payloads(directory: str, payloads: dict, symbol: str, as_of: int) -> Path:
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    for key, payload in payloads.items():
        (path / f"{key}.json").write_text(json.dumps(payload), encoding="utf-8")
    (path / "meta.json").write_text(json.dumps({"symbol": symbol, "as_of": as_of}), encoding="utf-8")
    return path


def write_raw_dump(vault: hl_api.RawVault) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(tz=timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = OUTPUT_DIR / f"raw_{stamp}.json"
    path.write_text(
        json.dumps({key: vault.get(key) for key in vault.keys()}, indent=2, default=str),
        encoding="utf-8",
    )
    return path


# ----------------------------------------------------------------- selfcheck
def selfcheck(symbol: str) -> int:
    as_of = int(time.time() * 1000)
    try:
        payloads, vault = collect(symbol, as_of, None)
        candles_1h = hl_parse.parse_candles(
            payloads["candles_1h"], path="candles_1h", interval="1h", coin=symbol
        )
        candles_5m = hl_parse.parse_candles(
            payloads["candles_5m"], path="candles_5m", interval="5m", coin=symbol
        )
        ctx = hl_parse.parse_asset_ctx(payloads["meta_and_asset_ctxs"], symbol)
        funding = hl_parse.parse_funding_history(payloads["funding_history"])
        venues = hl_parse.parse_predicted_fundings(payloads["predicted_fundings"], symbol)
    except MissingFieldError as exc:
        print(str(exc), file=sys.stderr)
        print(f"raw payload written to {write_raw_dump(vault)}", file=sys.stderr)
        return 2
    except hl_api.HyperliquidError as exc:
        print(f"FETCH FAILURE: {exc}", file=sys.stderr)
        return 3

    print("SELFCHECK OK")
    print(f"  candles 1h        : {len(candles_1h)} bars, last {datetime.fromtimestamp(candles_1h[-1].t / 1000, tz=timezone.utc):%Y-%m-%d %H:%M} UTC close {candles_1h[-1].c:,.2f}")
    print(f"  candles 5m        : {len(candles_5m)} bars, last close {candles_5m[-1].c:,.2f}")
    print(f"  mark / oracle     : {ctx.mark_px:,.2f} / {ctx.oracle_px:,.2f}")
    print(f"  funding (hourly)  : {ctx.funding * 100:+.5f}%  ->  {ctx.funding * 24 * 365 * 100:+.2f}%/yr")
    print(f"  open interest     : {ctx.open_interest:,.2f} {symbol}")
    print(f"  funding history   : {len(funding)} hourly points")
    print(f"  venues            : {', '.join(sorted(venues)) if venues else 'n/a'}")
    return 0


# ---------------------------------------------------------------------- main
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Hyperliquid perp intraday brief (keyless).")
    parser.add_argument("--symbol", default="ETH", help="perp coin as listed on Hyperliquid (default ETH)")
    parser.add_argument("--va-days", type=int, default=10, help="completed sessions in the value area")
    parser.add_argument("--va-percent", type=float, default=0.70, help="value area coverage (default 0.70)")
    parser.add_argument("--bucket", type=float, default=None, help="volume-profile bucket in quote units")
    parser.add_argument("--session-start-hour", type=int, default=0, help="UTC hour a session starts (default 0)")
    parser.add_argument("--min-rr", type=float, default=1.5, help="R:R floor before a setup is 'stand aside'")
    parser.add_argument(
        "--display-offset",
        default="+05:30",
        help="local offset for timestamps; sessions stay UTC. '0' for UTC (default +05:30)",
    )
    parser.add_argument("--as-of", default=None, help="ISO timestamp for a reproducible snapshot")
    parser.add_argument("--offline", default=None, help="directory of saved JSON payloads")
    parser.add_argument("--dump-payloads", default=None, help="save the raw payloads to a directory")
    parser.add_argument("--json", action="store_true", help="print the published plan JSON (levels.json)")
    parser.add_argument("--book-json", action="store_true", help="print the full computed book instead")
    parser.add_argument("--telegram-plan", action="store_true", help="push the compact plan to Telegram")
    parser.add_argument("--no-save", action="store_true", help="do not write output files or OI history")
    parser.add_argument("--selfcheck", action="store_true", help="fetch, validate every field, exit")
    return parser


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args(argv)

    if args.selfcheck:
        return selfcheck(args.symbol)

    as_of = parse_as_of(args.as_of)
    offset = parse_offset(args.display_offset)
    vault = hl_api.RawVault()
    try:
        payloads, vault = collect(args.symbol, as_of, args.offline)
        if args.dump_payloads:
            dump_payloads(args.dump_payloads, payloads, args.symbol, as_of)
        book = build_book(payloads, args.symbol, as_of, args)
    except MissingFieldError as exc:
        dump = write_raw_dump(vault)
        print(str(exc), file=sys.stderr)
        print(f"raw payload written to {dump}", file=sys.stderr)
        return 2
    except hl_api.HyperliquidError as exc:
        print(f"FETCH FAILURE: {exc}", file=sys.stderr)
        return 3

    text = brief_mod.render(book, display_offset_minutes=offset)
    plan = lv.build_levels(book, display_offset_minutes=offset)

    if args.book_json:
        print(json.dumps(book_to_dict(book), indent=2))
    elif args.json:
        print(json.dumps(plan, indent=2))
    else:
        print(text)

    if not args.no_save:
        md_path, json_path, archive_path = save(book, text, plan)
        append_oi(OI_STORE, args.symbol, as_of, book.oi, book.mark)
        print(f"\n[saved] {md_path}")
        print(f"[saved] {json_path}")
        print(f"[saved] {archive_path}")

    if args.telegram_plan:
        result = notify.send(brief_mod.render_plan_message(book, display_offset_minutes=offset))
        print(f"[telegram] {'sent' if result['ok'] else result.get('skipped') or result.get('detail')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
