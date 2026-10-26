#!/usr/bin/env python3
"""5-minute trigger watch.

Reads the plan published by the hourly brief, fetches the newest 5m candles, and
alerts when a setup arms, fires or dies. It never rewrites the plan.

Exit codes: 0 ok (with or without events), 2 no plan, 3 fetch failure, 4 stale plan.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import hl_api
import levels as lv
import notify
import parse as hl_parse

ROOT = Path(__file__).resolve().parent
HOUR_MS = 3_600_000


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_state(path: Path, plan_id: str) -> dict:
    if not path.exists():
        return {"plan_id": plan_id, "updated_at": None, "setups": {}}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"plan_id": plan_id, "updated_at": None, "setups": {}}
    if state.get("plan_id") != plan_id:
        return {"plan_id": plan_id, "updated_at": None, "setups": {}}
    state.setdefault("setups", {})
    return state


def write_state(path: Path, state: dict) -> bool:
    text = json.dumps(state, indent=2, sort_keys=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def format_event(levels: dict, event: dict) -> str:
    stamp = datetime.fromtimestamp(event["bar_t"] / 1000, tz=timezone.utc).strftime("%H:%M UTC")
    head = (
        f"{event['status']} | {levels['symbol']} | "
        f"S{event['index'] + 1} {event['name']} [{event['side']}]"
    )
    lines = [head, f"{event['message']} ({stamp})"]
    if event["status"] == lv.FIRED:
        lines.append(
            f"stop {event['stop']:,.2f} | T1 {event['t1']:,.2f} | T2 {event['t2']:,.2f} "
            f"| {event['rr1']:.2f}R / {event['rr2']:.2f}R"
        )
        lines.append(
            "plan says: STAND ASIDE (T1 under the R:R floor)"
            if not event["tradable"]
            else "plan says: valid - trigger confirmed"
        )
    else:
        lines.append("no further alerts for this setup today")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="5-minute trigger watch for the published plan.")
    parser.add_argument("--levels", default=str(ROOT / "output" / "latest.json"))
    parser.add_argument("--state", default=str(ROOT / "data" / "watch_state.json"))
    parser.add_argument("--max-age-min", type=int, default=360, help="refuse to trade a plan older than this")
    parser.add_argument("--lookback-hours", type=int, default=6)
    parser.add_argument("--no-telegram", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="evaluate and print, do not write state")
    args = parser.parse_args(argv)

    levels_path = Path(args.levels)
    if not levels_path.exists():
        print(f"NO PLAN: {levels_path} not found", file=sys.stderr)
        return 2
    levels = read_json(levels_path)

    now = int(time.time() * 1000)
    age_min = (now - int(levels["as_of"])) / 60_000
    if age_min > args.max_age_min:
        print(
            f"STALE PLAN: generated {age_min:.0f} min ago (limit {args.max_age_min}); "
            f"waiting for the hourly brief to refresh it",
            file=sys.stderr,
        )
        return 4

    state_path = Path(args.state)
    state = read_state(state_path, levels["plan_id"])

    start = max(int(levels["as_of"]) - args.lookback_hours * HOUR_MS, now - 12 * HOUR_MS)
    try:
        payload = hl_api.fetch_candles(levels["symbol"], "5m", start, now)
        bars = hl_parse.parse_candles(payload, path="candles_5m", interval="5m", coin=levels["symbol"])
    except (hl_api.HyperliquidError, hl_parse.MissingFieldError) as exc:
        print(f"FETCH FAILURE: {exc}", file=sys.stderr)
        return 3

    new_states, events = lv.evaluate_all(
        levels,
        eligible := lv.eligible_bars(levels, bars, now_ms=now),
        state.get("setups"),
    )

    statuses = ", ".join(f"S{int(key) + 1}={value['status']}" for key, value in sorted(new_states.items()))
    print(f"plan {levels['plan_id']} age {age_min:.0f}m | {len(eligible)} new 5m bars | {statuses}")

    for event in events:
        text = format_event(levels, event)
        print(text)
        print("")
        if not args.no_telegram and not args.dry_run:
            result = notify.send(text)
            if not result["ok"]:
                print(f"  telegram: not sent ({result.get('skipped') or result.get('detail')})")

    changed = state.get("setups") != new_states
    state["setups"] = new_states
    if changed:
        state["updated_at"] = now
        if not args.dry_run:
            write_state(state_path, state)
    print(f"state changed: {changed}" + (" (dry run, not written)" if args.dry_run and changed else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
