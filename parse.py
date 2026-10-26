"""Parsing and validation for Hyperliquid /info payloads.

Every accessor goes through ``require``/``num`` so a renamed, null or
non-numeric field fails loudly with the raw payload attached, instead of
silently producing a wrong number.

Hyperliquid is inconsistent about numeric types: candle prices arrive as
strings, ``metaAndAssetCtxs`` prices arrive as strings, and some endpoints
return floats. ``num`` accepts both.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

_MISSING = object()


class MissingFieldError(KeyError):
    """A required field was absent, null, empty or non-numeric."""

    def __init__(
        self,
        field: str,
        path: str,
        record: Any = None,
        raw: Any = None,
        reason: str = "missing",
    ) -> None:
        self.field = field
        self.path = path
        self.record = record
        self.raw = raw
        self.reason = reason
        super().__init__(f"{field!r} {reason} at {path}")

    def raw_json(self, indent: int = 2) -> str:
        payload = self.raw if self.raw is not None else self.record
        return json.dumps(payload, indent=indent, default=str, sort_keys=False)

    def __str__(self) -> str:  # printed straight to stderr by the CLI
        lines = [
            f"PARSE FAILURE: field {self.field!r} {self.reason} at {self.path}",
            "--- raw JSON ---",
            self.raw_json(),
            "--- end raw JSON ---",
        ]
        return "\n".join(lines)


class DataQualityError(RuntimeError):
    """The payload parsed, but the numbers are not usable (bad OHLC, gaps...)."""


# ------------------------------------------------------------------ primitives
def require(record: Mapping[str, Any], field: str, path: str, raw: Any = None) -> Any:
    value = record.get(field, _MISSING) if isinstance(record, Mapping) else _MISSING
    if value is _MISSING:
        raise MissingFieldError(field, path, record, raw, reason="missing")
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise MissingFieldError(field, path, record, raw, reason="null/empty")
    return value


def num(record: Mapping[str, Any], field: str, path: str, raw: Any = None) -> float:
    value = require(record, field, path, raw)
    if isinstance(value, bool):
        raise MissingFieldError(field, path, record, raw, reason="boolean, not numeric")
    try:
        out = float(value)
    except (TypeError, ValueError):
        raise MissingFieldError(
            field, path, record, raw, reason=f"not numeric ({type(value).__name__})"
        ) from None
    if not math.isfinite(out):
        raise MissingFieldError(field, path, record, raw, reason="non-finite")
    return out


def num_opt(record: Mapping[str, Any], field: str, path: str, default: float | None = None) -> float | None:
    value = record.get(field) if isinstance(record, Mapping) else None
    if value is None or (isinstance(value, str) and value.strip() == ""):
        return default
    return num(record, field, path)


# ---------------------------------------------------------------------- candles
@dataclass(frozen=True)
class Candle:
    t: int  # open time, ms
    T: int  # close time, ms
    o: float
    h: float
    l: float
    c: float
    v: float  # base volume (ETH for the ETH perp)
    n: int  # trade count

    @property
    def typical(self) -> float:
        return (self.h + self.l + self.c) / 3.0

    @property
    def is_up(self) -> bool:
        return self.c >= self.o


def parse_candles(
    payload: Any,
    *,
    path: str = "candleSnapshot",
    interval: str | None = None,
    coin: str | None = None,
) -> list[Candle]:
    """Validate a candleSnapshot array, sort by open time and drop duplicates."""
    if not isinstance(payload, Sequence) or isinstance(payload, (str, bytes)) or len(payload) == 0:
        raise MissingFieldError("candles[]", path, None, payload, reason="empty or not a list")

    candles: list[Candle] = []
    for index, record in enumerate(payload):
        where = f"{path}[{index}]"
        if not isinstance(record, Mapping):
            raise MissingFieldError("record", where, None, payload, reason="not an object")
        if coin is not None and "s" in record and record["s"] != coin:
            raise DataQualityError(f"{where}.s = {record['s']!r}, expected {coin!r}")
        if interval is not None and "i" in record and record["i"] != interval:
            raise DataQualityError(f"{where}.i = {record['i']!r}, expected {interval!r}")

        candle = Candle(
            t=int(num(record, "t", where, payload)),
            T=int(num(record, "T", where, payload)),
            o=num(record, "o", where, payload),
            h=num(record, "h", where, payload),
            l=num(record, "l", where, payload),
            c=num(record, "c", where, payload),
            v=num(record, "v", where, payload),
            n=int(num_opt(record, "n", where, 0.0) or 0),
        )
        if candle.h < candle.l:
            raise DataQualityError(f"{where}: high {candle.h} < low {candle.l}")
        if not (candle.l - 1e-9 <= candle.o <= candle.h + 1e-9):
            raise DataQualityError(f"{where}: open {candle.o} outside [{candle.l}, {candle.h}]")
        if not (candle.l - 1e-9 <= candle.c <= candle.h + 1e-9):
            raise DataQualityError(f"{where}: close {candle.c} outside [{candle.l}, {candle.h}]")
        if candle.T < candle.t:
            raise DataQualityError(f"{where}: close time before open time")
        candles.append(candle)

    candles.sort(key=lambda item: item.t)
    deduped: list[Candle] = []
    for candle in candles:
        if deduped and deduped[-1].t == candle.t:
            deduped[-1] = candle  # keep the later record for a duplicate open time
        else:
            deduped.append(candle)
    return deduped


def candle_gap_warnings(
    candles: Sequence[Candle], interval_ms: int, *, max_gaps: int = 3
) -> list[str]:
    """Report missing bars rather than crashing: exchanges drop candles around outages."""
    gaps = []
    for previous, current in zip(candles, candles[1:]):
        delta = current.t - previous.t
        if delta > interval_ms * 2:
            gaps.append((previous.t, delta))
    if not gaps:
        return []
    head = "; ".join(f"{gap / interval_ms:.0f} bars missing at t={t}" for t, gap in gaps[:max_gaps])
    extra = "" if len(gaps) <= max_gaps else f" (+{len(gaps) - max_gaps} more)"
    return [f"candle gaps: {head}{extra}"]


# ------------------------------------------------------------------- asset ctx
@dataclass(frozen=True)
class AssetCtx:
    coin: str
    funding: float  # HOURLY funding rate as a fraction, e.g. 0.0000020526
    open_interest: float  # coins
    prev_day_px: float
    oracle_px: float
    mark_px: float
    day_ntl_vlm: float
    day_base_vlm: float
    mid_px: float | None = None
    premium: float | None = None


def parse_asset_ctx(payload: Any, coin: str, *, path: str = "metaAndAssetCtxs") -> AssetCtx:
    """metaAndAssetCtxs returns [meta, ctxs]; ctxs is positional, aligned to universe."""
    if not isinstance(payload, Sequence) or isinstance(payload, (str, bytes)) or len(payload) != 2:
        raise MissingFieldError("metaAndAssetCtxs[2]", path, None, payload, reason="expected [meta, ctxs]")

    meta, ctxs = payload
    if not isinstance(meta, Mapping):
        raise MissingFieldError("meta", f"{path}[0]", None, payload, reason="not an object")
    universe = require(meta, "universe", f"{path}[0]", payload)
    if not isinstance(universe, Sequence) or not universe:
        raise MissingFieldError("universe[]", f"{path}[0]", meta, payload, reason="empty")

    index = None
    for position, asset in enumerate(universe):
        if isinstance(asset, Mapping) and asset.get("name") == coin:
            index = position
            break
    if index is None:
        raise MissingFieldError(f"universe[{coin}]", f"{path}[0]", meta, payload, reason="coin not listed")
    if not isinstance(ctxs, Sequence) or index >= len(ctxs):
        raise MissingFieldError(
            f"ctxs[{index}]", f"{path}[1]", ctxs, payload, reason="index beyond ctxs length"
        )

    ctx = ctxs[index]
    where = f"{path}[1][{index}]"
    return AssetCtx(
        coin=coin,
        funding=num(ctx, "funding", where, payload),
        open_interest=num(ctx, "openInterest", where, payload),
        prev_day_px=num(ctx, "prevDayPx", where, payload),
        oracle_px=num(ctx, "oraclePx", where, payload),
        mark_px=num(ctx, "markPx", where, payload),
        day_ntl_vlm=num(ctx, "dayNtlVlm", where, payload),
        day_base_vlm=num(ctx, "dayBaseVlm", where, payload),
        mid_px=num_opt(ctx, "midPx", where),
        premium=num_opt(ctx, "premium", where),
    )


# --------------------------------------------------------------------- funding
@dataclass(frozen=True)
class FundingPoint:
    coin: str
    rate: float
    time: int


def parse_funding_history(payload: Any, *, path: str = "fundingHistory") -> list[FundingPoint]:
    if not isinstance(payload, Sequence) or isinstance(payload, (str, bytes)):
        raise MissingFieldError("fundingHistory[]", path, None, payload, reason="not a list")
    points: list[FundingPoint] = []
    for index, record in enumerate(payload):
        where = f"{path}[{index}]"
        points.append(
            FundingPoint(
                coin=str(require(record, "coin", where, payload)),
                rate=num(record, "fundingRate", where, payload),
                time=int(num(record, "time", where, payload)),
            )
        )
    points.sort(key=lambda point: point.time)
    return points


def parse_predicted_fundings(
    payload: Any, coin: str, *, path: str = "predictedFundings"
) -> dict[str, tuple[float, int]]:
    """Cross-venue funding: {venue: (rate, interval_hours)} for one coin."""
    if not isinstance(payload, Sequence) or isinstance(payload, (str, bytes)):
        raise MissingFieldError("predictedFundings[]", path, None, payload, reason="not a list")
    for index, row in enumerate(payload):
        if not isinstance(row, Sequence) or len(row) != 2 or row[0] != coin:
            continue
        venues: dict[str, tuple[float, int]] = {}
        for venue_index, entry in enumerate(row[1]):
            where = f"{path}[{index}][1][{venue_index}]"
            if not isinstance(entry, Sequence) or len(entry) != 2:
                raise MissingFieldError("venue", where, None, payload, reason="expected [name, ctx]")
            name, ctx = entry
            venues[str(name)] = (
                num(ctx, "fundingRate", where, payload),
                int(num(ctx, "fundingIntervalHours", where, payload)),
            )
        return venues
    return {}
