"""Deterministic level maths for the Hyperliquid ETH brief.

Every number here is a function of observed candles and context. Nothing is
forecast. The bias and regime scores are written as explicit rules so the
output can be audited rather than trusted, and so the unit tests can pin them.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Iterable, Sequence

from parse import AssetCtx, Candle, FundingPoint

DAY_MS = 86_400_000
HOUR_MS = 3_600_000


class InsufficientData(RuntimeError):
    """Not enough bars to compute a requested statistic."""


# -------------------------------------------------------------------- sessions
def session_start(ts_ms: int, start_hour: int = 0) -> int:
    """UTC session open containing ``ts_ms``; ``start_hour`` shifts the boundary."""
    shift = start_hour * HOUR_MS
    return ((ts_ms - shift) // DAY_MS) * DAY_MS + shift


def group_sessions(candles: Iterable[Candle], start_hour: int = 0) -> dict[int, list[Candle]]:
    sessions: dict[int, list[Candle]] = {}
    for candle in candles:
        sessions.setdefault(session_start(candle.t, start_hour), []).append(candle)
    return dict(sorted(sessions.items()))


# ------------------------------------------------------------------ value area
@dataclass(frozen=True)
class ValueArea:
    poc: float
    val: float
    vah: float
    total_volume: float
    captured_volume: float
    bucket: float
    bars: int

    @property
    def width(self) -> float:
        return self.vah - self.val

    @property
    def captured_pct(self) -> float:
        return self.captured_volume / self.total_volume if self.total_volume else 0.0


def auto_bucket(price: float, fraction: float = 0.0005) -> float:
    """A 'nice' bucket ~0.05% of price: 1.0 for ETH near $2.3k, 50 for BTC near $100k."""
    target = max(price * fraction, 1e-9)
    exponent = math.floor(math.log10(target))
    base = 10.0**exponent
    for multiple in (10, 5, 2, 1):
        if target >= base * multiple:
            return base * multiple
    return base


def volume_profile(candles: Sequence[Candle], bucket: float) -> dict[int, float]:
    """Distribute each bar's volume uniformly over its high-low range.

    A bar is a range, not a point: assigning all of its volume to the typical
    price over-weights the middle and hollows out the extremes.
    """
    if bucket <= 0:
        raise ValueError("bucket must be positive")

    hist: dict[int, float] = {}
    for candle in candles:
        if candle.v <= 0 or candle.h < candle.l:
            continue
        if candle.h == candle.l:
            index = math.floor(candle.l / bucket)
            hist[index] = hist.get(index, 0.0) + candle.v
            continue

        span = candle.h - candle.l
        first = math.floor(candle.l / bucket)
        last = math.floor(candle.h / bucket)
        if last - first > 2000:
            raise InsufficientData(f"one bar spans {last - first + 1} buckets; bucket {bucket} is too fine")
        for index in range(first, last + 1):
            lower = index * bucket
            overlap = min(candle.h, lower + bucket) - max(candle.l, lower)
            if overlap > 0:
                hist[index] = hist.get(index, 0.0) + candle.v * (overlap / span)
    return hist


def value_area_from_hist(
    hist: dict[int, float], bucket: float, percent: float = 0.70, bars: int = 0
) -> ValueArea:
    """Expand from the POC toward the heavier neighbouring bucket until ``percent``.

    Ties go to the upper bucket so the result is deterministic.
    """
    if not hist:
        raise InsufficientData("empty volume profile")
    total = sum(hist.values())
    if total <= 0:
        raise InsufficientData("zero total volume")

    low_key, high_key = min(hist), max(hist)
    poc_index = max(hist.items(), key=lambda item: (item[1], -item[0]))[0]

    low_index = high_index = poc_index
    captured = hist[poc_index]
    target = total * percent

    while captured < target and (low_index > low_key or high_index < high_key):
        above = hist.get(high_index + 1) if high_index < high_key else None
        below = hist.get(low_index - 1) if low_index > low_key else None
        # -1 is a sentinel: an exhausted side never wins the comparison.
        up = above if above is not None else -1.0
        down = below if below is not None else -1.0
        if up >= down:
            high_index += 1
            captured += up
        else:
            low_index -= 1
            captured += down

    return ValueArea(
        poc=(poc_index + 0.5) * bucket,
        val=low_index * bucket,
        vah=(high_index + 1) * bucket,
        total_volume=total,
        captured_volume=captured,
        bucket=bucket,
        bars=bars,
    )


def value_area(candles: Sequence[Candle], bucket: float, percent: float = 0.70) -> ValueArea:
    return value_area_from_hist(volume_profile(candles, bucket), bucket, percent, bars=len(candles))


# ------------------------------------------------------------------------ VWAP
@dataclass(frozen=True)
class VWAP:
    vwap: float
    sigma: float
    volume: float
    bars: int


def session_vwap(candles: Sequence[Candle]) -> VWAP:
    volume = sum(candle.v for candle in candles)
    if volume <= 0:
        raise InsufficientData("zero volume for VWAP")
    vwap = sum(candle.typical * candle.v for candle in candles) / volume
    variance = sum(candle.v * (candle.typical - vwap) ** 2 for candle in candles) / volume
    return VWAP(vwap=vwap, sigma=math.sqrt(max(variance, 0.0)), volume=volume, bars=len(candles))


# --------------------------------------------------------------------- pivots
@dataclass(frozen=True)
class FloorPivots:
    p: float
    r1: float
    r2: float
    r3: float
    s1: float
    s2: float
    s3: float


def floor_pivots(high: float, low: float, close: float) -> FloorPivots:
    """Classic floor-trader pivots on the prior session's H/L/C."""
    if high < low:
        raise ValueError(f"high {high} < low {low}")
    p = (high + low + close) / 3.0
    return FloorPivots(
        p=p,
        r1=2 * p - low,
        r2=p + (high - low),
        r3=high + 2 * (p - low),
        s1=2 * p - high,
        s2=p - (high - low),
        s3=low - 2 * (high - p),
    )


# ------------------------------------------------------------------------ ATR
def true_ranges(candles: Sequence[Candle]) -> list[float]:
    ranges: list[float] = []
    previous_close: float | None = None
    for candle in candles:
        if previous_close is None:
            ranges.append(candle.h - candle.l)
        else:
            ranges.append(
                max(candle.h - candle.l, abs(candle.h - previous_close), abs(candle.l - previous_close))
            )
        previous_close = candle.c
    return ranges


def wilder_atr(candles: Sequence[Candle], period: int = 14) -> float:
    """Wilder's ATR: seed with the SMA of the first ``period`` true ranges."""
    ranges = true_ranges(candles)
    if len(ranges) < period:
        raise InsufficientData(f"need {period} bars for ATR({period}), got {len(ranges)}")
    atr = sum(ranges[:period]) / period
    for value in ranges[period:]:
        atr = (atr * (period - 1) + value) / period
    return atr


def atr_series(candles: Sequence[Candle], period: int = 14) -> list[float]:
    ranges = true_ranges(candles)
    if len(ranges) < period:
        return []
    atr = sum(ranges[:period]) / period
    series = [atr]
    for value in ranges[period:]:
        atr = (atr * (period - 1) + value) / period
        series.append(atr)
    return series


def ema(values: Sequence[float], period: int) -> list[float]:
    """EMA seeded with the SMA of the first ``period`` values."""
    if period <= 0:
        raise ValueError("period must be positive")
    if len(values) < period:
        raise InsufficientData(f"need {period} values for EMA({period}), got {len(values)}")
    multiplier = 2 / (period + 1)
    out = [sum(values[:period]) / period]
    for value in values[period:]:
        out.append(out[-1] + multiplier * (value - out[-1]))
    return out


# ----------------------------------------------------------------------- reads
def structure_read(candles: Sequence[Candle], lookback: int = 20, half: int = 10) -> str:
    """Compare swing extremes of the recent half against the older half."""
    if len(candles) < lookback:
        return "insufficient"
    older, recent = candles[-lookback:-half], candles[-half:]
    higher_high = max(c.h for c in recent) > max(c.h for c in older)
    higher_low = min(c.l for c in recent) > min(c.l for c in older)
    lower_high = max(c.h for c in recent) < max(c.h for c in older)
    lower_low = min(c.l for c in recent) < min(c.l for c in older)
    if higher_high and higher_low:
        return "higher"
    if lower_high and lower_low:
        return "lower"
    return "mixed"


@dataclass(frozen=True)
class BiasComponent:
    name: str
    read: str
    score: int


@dataclass(frozen=True)
class BiasReport:
    label: str
    score: int
    max_score: int
    components: list[BiasComponent]


def bias_report(
    *,
    spot: float,
    ema_fast: float,
    ema_slow: float,
    value_label: str,
    prior_range_position: float | None,
    structure: str,
    funding_percentile: float | None,
    oi_24h_pct: float | None,
    price_24h_pct: float | None,
) -> BiasReport:
    """Six auditable reads. The label needs |score| >= 3 to leave 'Balanced'.

    Funding is scored contrarian: crowded longs (top quintile) are a headwind,
    not a confirmation. OI is scored against the 24h price move, because OI
    alone says nothing about direction.
    """
    components: list[BiasComponent] = []

    if spot > ema_fast > ema_slow:
        components.append(BiasComponent("EMA stack", f"price > EMA50 > EMA200 ({ema_fast:,.2f} / {ema_slow:,.2f})", 1))
    elif spot < ema_fast < ema_slow:
        components.append(BiasComponent("EMA stack", f"price < EMA50 < EMA200 ({ema_fast:,.2f} / {ema_slow:,.2f})", -1))
    else:
        components.append(BiasComponent("EMA stack", f"mixed ({ema_fast:,.2f} / {ema_slow:,.2f})", 0))

    value_scores = {"above": 1, "inside": 0, "below": -1}
    components.append(
        BiasComponent("10-session value", f"price {value_label} the value area", value_scores.get(value_label, 0))
    )

    if prior_range_position is None:
        components.append(BiasComponent("Prior day close", "n/a", 0))
    else:
        score = 1 if prior_range_position >= 0.65 else -1 if prior_range_position <= 0.35 else 0
        components.append(
            BiasComponent("Prior day close", f"closed at {prior_range_position:.0%} of prior range", score)
        )

    structure_scores = {"higher": 1, "lower": -1}
    components.append(
        BiasComponent("20-bar structure", f"1H swings {structure}", structure_scores.get(structure, 0))
    )

    if funding_percentile is None:
        components.append(BiasComponent("Funding percentile", "n/a", 0))
    else:
        score = -1 if funding_percentile >= 80 else 1 if funding_percentile <= 20 else 0
        components.append(
            BiasComponent(
                "Funding percentile",
                f"{funding_percentile:.0f}th pct of trailing history (crowded longs = headwind)",
                score,
            )
        )

    if oi_24h_pct is None or price_24h_pct is None:
        components.append(BiasComponent("OI 24h", "n/a (needs a stored baseline)", 0))
    elif oi_24h_pct > 1.0 and price_24h_pct > 0:
        components.append(BiasComponent("OI 24h", f"OI {oi_24h_pct:+.1f}% with price {price_24h_pct:+.1f}%: new longs", 1))
    elif oi_24h_pct > 1.0 and price_24h_pct < 0:
        components.append(BiasComponent("OI 24h", f"OI {oi_24h_pct:+.1f}% with price {price_24h_pct:+.1f}%: new shorts", -1))
    else:
        components.append(BiasComponent("OI 24h", f"OI {oi_24h_pct:+.1f}%, price {price_24h_pct:+.1f}%: no edge", 0))

    total = sum(component.score for component in components)
    label = "Bullish" if total >= 3 else "Bearish" if total <= -3 else "Balanced"
    return BiasReport(label=label, score=total, max_score=len(components), components=components)


@dataclass(frozen=True)
class RegimeReport:
    label: str
    value_label: str
    pct_closes_outside: float
    slope_atr: float
    vol_ratio: float
    distance_vah_atr: float
    distance_val_atr: float
    distance_poc_atr: float


def classify_regime(
    *,
    closes: Sequence[float],
    va: ValueArea,
    spot: float,
    atr: float,
    slope_atr: float,
    vol_ratio: float,
) -> RegimeReport:
    """Ordered rules; the first match wins. No smoothing, no discretion."""
    if not closes:
        raise InsufficientData("no closes for regime classification")
    outside = sum(1 for close in closes if close > va.vah or close < va.val) / len(closes)
    value_label = "above" if spot > va.vah else "below" if spot < va.val else "inside"

    recent = closes[-6:]
    poked_out = any(close > va.vah or close < va.val for close in recent)
    back_inside = all(va.val <= close <= va.vah for close in closes[-3:])

    if value_label == "inside" and poked_out and back_inside:
        label = "failed-auction"
    elif outside >= 0.55 and abs(slope_atr) >= 0.5:
        label = "trend-up" if slope_atr > 0 else "trend-down"
    elif value_label != "inside" and outside >= 0.50:
        label = "breakout-attempt"
    else:
        label = "rotational-balance"

    def atr_distance(level: float) -> float:
        return (spot - level) / atr if atr else 0.0

    return RegimeReport(
        label=label,
        value_label=value_label,
        pct_closes_outside=outside,
        slope_atr=slope_atr,
        vol_ratio=vol_ratio,
        distance_vah_atr=atr_distance(va.vah),
        distance_val_atr=atr_distance(va.val),
        distance_poc_atr=atr_distance(va.poc),
    )


# --------------------------------------------------------------------- setups
@dataclass(frozen=True)
class Setup:
    name: str
    side: str
    trigger: str
    entry: float
    stop: float
    t1: float
    t2: float
    invalidation: str
    min_rr: float = 1.5

    @property
    def risk(self) -> float:
        return abs(self.entry - self.stop)

    @property
    def rr1(self) -> float:
        return abs(self.t1 - self.entry) / self.risk if self.risk > 0 else float("inf")

    @property
    def rr2(self) -> float:
        return abs(self.t2 - self.entry) / self.risk if self.risk > 0 else float("inf")

    @property
    def stand_aside(self) -> bool:
        return self.risk <= 0 or self.rr1 < self.min_rr


def _targets(entry: float, levels: Iterable[float], atr: float, direction: int) -> tuple[float, float]:
    """First and second structural level beyond ``entry``; ATR fallback if thin."""
    gap = 0.4 * atr
    unique = sorted({round(level, 6) for level in levels if level is not None and math.isfinite(level)})
    if direction > 0:
        candidates = [level for level in unique if level >= entry + gap]
        t1 = candidates[0] if candidates else entry + 1.0 * atr
        t2 = next((level for level in candidates[1:] if level >= t1 + gap), entry + 1.8 * atr)
    else:
        candidates = [level for level in reversed(unique) if level <= entry - gap]
        t1 = candidates[0] if candidates else entry - 1.0 * atr
        t2 = next((level for level in candidates[1:] if level <= t1 - gap), entry - 1.8 * atr)
    return t1, t2


def build_setups(
    *,
    spot: float,
    atr: float,
    va: ValueArea,
    vwap: VWAP,
    pivots: FloorPivots,
    pdh: float,
    pdl: float,
    bias_label: str,
    min_rr: float = 1.5,
) -> list[Setup]:
    """Three conditional templates anchored on live levels.

    Triggers are written first and entries are limit-style, so these are plans,
    not predictions. A setup whose first target is under ``min_rr`` is still
    reported but flagged 'stand aside'.
    """
    val, vah, poc = va.val, va.vah, va.poc
    inside = val <= spot <= vah
    bullish = bias_label != "Bearish"
    setups: list[Setup] = []

    # 1) value rejection ----------------------------------------------------
    if inside:
        if spot <= poc:
            setups.append(
                Setup(
                    name="Value rejection (long from VAL)",
                    side="LONG",
                    trigger=f"5m close back inside value after tagging VAL {val:,.2f}; enter on the reclaim",
                    entry=val,
                    stop=val - 0.5 * atr,
                    t1=poc,
                    t2=vah,
                    invalidation=f"5m close below {val - 0.5 * atr:,.2f}: value rejected lower, stand down",
                    min_rr=min_rr,
                )
            )
        else:
            setups.append(
                Setup(
                    name="Value rejection (short from VAH)",
                    side="SHORT",
                    trigger=f"5m close back inside value after tagging VAH {vah:,.2f}; enter on the loss of the edge",
                    entry=vah,
                    stop=vah + 0.5 * atr,
                    t1=poc,
                    t2=val,
                    invalidation=f"5m close above {vah + 0.5 * atr:,.2f}: acceptance higher, stand down",
                    min_rr=min_rr,
                )
            )
    elif spot > vah:
        setups.append(
            Setup(
                name="Failed auction (short back into value)",
                side="SHORT",
                trigger=(
                    f"price is {(spot - vah) / atr:.1f} ATR above VAH {vah:,.2f}; arm only on a 5m close "
                    f"back below it, which is what confirms the failure"
                ),
                entry=vah,
                stop=max(spot, pdh) + 0.5 * atr,
                t1=poc,
                t2=val,
                invalidation=f"5m close above {max(spot, pdh) + 0.5 * atr:,.2f}: the sweep was acceptance",
                min_rr=min_rr,
            )
        )
    else:
        setups.append(
            Setup(
                name="Failed auction (long back into value)",
                side="LONG",
                trigger=(
                    f"price is {(val - spot) / atr:.1f} ATR below VAL {val:,.2f}; arm only on a 5m close "
                    f"back above it, which is what confirms the failure"
                ),
                entry=val,
                stop=min(spot, pdl) - 0.5 * atr,
                t1=poc,
                t2=vah,
                invalidation=f"5m close below {min(spot, pdl) - 0.5 * atr:,.2f}: the sweep was acceptance",
                min_rr=min_rr,
            )
        )

    # 2) acceptance and retest ---------------------------------------------
    if not inside:
        if spot > vah:
            entry = vah
            stop = vah - 0.75 * atr
            t1, t2 = _targets(entry, [pdh, pivots.r1, pivots.r2, pivots.r3, entry + va.width], atr, +1)
            setups.append(
                Setup(
                    name="Acceptance and retest (long VAH)",
                    side="LONG",
                    trigger=(
                        f"price has been accepted {(spot - vah) / atr:.1f} ATR above VAH {vah:,.2f}; "
                        f"long the retest that holds above it"
                    ),
                    entry=entry,
                    stop=stop,
                    t1=t1,
                    t2=t2,
                    invalidation=f"1H close back inside value (below {vah:,.2f}) voids the acceptance",
                    min_rr=min_rr,
                )
            )
        else:
            entry = val
            stop = val + 0.75 * atr
            t1, t2 = _targets(entry, [pdl, pivots.s1, pivots.s2, pivots.s3, entry - va.width], atr, -1)
            setups.append(
                Setup(
                    name="Acceptance and retest (short VAL)",
                    side="SHORT",
                    trigger=(
                        f"price has been accepted {(val - spot) / atr:.1f} ATR below VAL {val:,.2f}; "
                        f"short the retest that fails at it"
                    ),
                    entry=entry,
                    stop=stop,
                    t1=t1,
                    t2=t2,
                    invalidation=f"1H close back inside value (above {val:,.2f}) voids the acceptance",
                    min_rr=min_rr,
                )
            )
    else:
        direction = 1 if bullish else -1
        if direction > 0:
            entry = vah + 0.1 * atr
            stop = vah - 0.5 * atr
            t1, t2 = _targets(entry, [pdh, pivots.r1, pivots.r2, pivots.r3, entry + va.width], atr, +1)
            setups.append(
                Setup(
                    name="Range expansion (long above VAH)",
                    side="LONG",
                    trigger=f"1H close above VAH {vah:,.2f} while still inside value; buy the confirmation, not the poke",
                    entry=entry,
                    stop=stop,
                    t1=t1,
                    t2=t2,
                    invalidation=f"1H close back below {vah:,.2f}: the expansion failed, mirror the short at VAL",
                    min_rr=min_rr,
                )
            )
        else:
            entry = val - 0.1 * atr
            stop = val + 0.5 * atr
            t1, t2 = _targets(entry, [pdl, pivots.s1, pivots.s2, pivots.s3, entry - va.width], atr, -1)
            setups.append(
                Setup(
                    name="Range expansion (short below VAL)",
                    side="SHORT",
                    trigger=f"1H close below VAL {val:,.2f} while still inside value; sell the confirmation, not the poke",
                    entry=entry,
                    stop=stop,
                    t1=t1,
                    t2=t2,
                    invalidation=f"1H close back above {val:,.2f}: the expansion failed, mirror the long at VAH",
                    min_rr=min_rr,
                )
            )

    # 3) VWAP and pivot confluence -----------------------------------------
    long_zone = max((level for level in (vwap.vwap, pivots.s1, pivots.p) if level <= spot - 0.2 * atr), default=None)
    short_zone = min((level for level in (vwap.vwap, pivots.r1, pivots.p) if level >= spot + 0.2 * atr), default=None)

    zone = long_zone if bullish else short_zone
    direction = 1 if bullish else -1
    if zone is None:
        zone = short_zone if bullish else long_zone
        direction = -direction if zone is not None else direction
    if zone is None:
        zone = vwap.vwap
        direction = 1 if bullish else -1

    if direction > 0:
        entry = zone
        stop = zone - 0.6 * atr
        t1, t2 = _targets(entry, [vwap.vwap + vwap.sigma, poc, vah, pivots.r1, pdh, entry + 2.0 * atr], atr, +1)
        setups.append(
            Setup(
                name="VWAP / pivot confluence (long)",
                side="LONG",
                trigger=f"session VWAP {vwap.vwap:,.2f} or pivot support near {zone:,.2f}; buy the hold, not the touch",
                entry=entry,
                stop=stop,
                t1=t1,
                t2=t2,
                invalidation=f"5m close below {stop:,.2f}: the confluence level is lost",
                min_rr=min_rr,
            )
        )
    else:
        entry = zone
        stop = zone + 0.6 * atr
        t1, t2 = _targets(entry, [vwap.vwap - vwap.sigma, poc, val, pivots.s1, pdl, entry - 2.0 * atr], atr, -1)
        setups.append(
            Setup(
                name="VWAP / pivot confluence (short)",
                side="SHORT",
                trigger=f"session VWAP {vwap.vwap:,.2f} or pivot resistance near {zone:,.2f}; sell the rejection, not the touch",
                entry=entry,
                stop=stop,
                t1=t1,
                t2=t2,
                invalidation=f"5m close above {stop:,.2f}: the confluence level is lost",
                min_rr=min_rr,
            )
        )

    return setups


# -------------------------------------------------------------------- assembly
@dataclass
class LevelBook:
    symbol: str
    as_of: int
    spot: float
    mark: float
    oracle: float
    prev_day_px: float
    funding_hourly: float
    funding_apr: float
    funding_percentile: float | None
    funding_window_hours: int
    funding_venues: dict[str, tuple[float, int]]
    oi: float
    oi_prev_pct: float | None
    oi_24h_pct: float | None
    day_ntl_vlm: float
    va: ValueArea
    va_days: int
    va_percent: float
    dev_va: ValueArea | None
    session_progress: float
    vwap: VWAP
    prev_vwap: VWAP | None
    pdh: float
    pdl: float
    pdc: float
    pdo: float
    pdh_swept: bool
    pdl_swept: bool
    pivots: FloorPivots
    atr: float
    atr_pct: float
    atr_median_30: float
    vol_ratio: float
    bias: BiasReport
    regime: RegimeReport
    setups: list[Setup]
    warnings: list[str] = field(default_factory=list)


def compute(
    *,
    symbol: str,
    as_of: int,
    candles_1h: Sequence[Candle],
    candles_5m: Sequence[Candle],
    ctx: AssetCtx,
    funding_history: Sequence[FundingPoint],
    funding_venues: dict[str, tuple[float, int]] | None = None,
    session_start_hour: int = 0,
    va_days: int = 10,
    va_percent: float = 0.70,
    bucket: float | None = None,
    oi_prev_pct: float | None = None,
    oi_24h_pct: float | None = None,
    warnings: Sequence[str] | None = None,
    min_rr: float = 1.5,
) -> LevelBook:
    notes = list(warnings or [])
    spot = ctx.mid_px if ctx.mid_px else ctx.mark_px

    completed = [candle for candle in candles_1h if candle.T <= as_of]
    if len(completed) < 60:
        raise InsufficientData(f"need >=60 completed 1H bars, got {len(completed)}")

    sessions = group_sessions(completed, session_start_hour)
    closed = {key: bars for key, bars in sessions.items() if key + DAY_MS <= as_of}
    if len(closed) < va_days:
        notes.append(f"only {len(closed)} completed sessions available, wanted {va_days}")
    va_keys = list(closed)[-va_days:]
    va_candles = [candle for key in va_keys for candle in closed[key]]
    bucket = bucket or auto_bucket(completed[-1].c)
    va = value_area(va_candles, bucket, va_percent)

    current_key = session_start(as_of, session_start_hour)
    intraday = [candle for candle in candles_5m if current_key <= candle.t <= as_of]
    dev_va: ValueArea | None = None
    if len(intraday) >= 4:
        dev_va = value_area(intraday, bucket, va_percent)
        vwap = session_vwap(intraday)
    else:
        intraday = [candle for candle in candles_1h if current_key <= candle.t <= as_of]
        if not intraday:
            raise InsufficientData("no bars in the current session")
        vwap = session_vwap(intraday)
    session_progress = min(max((as_of - current_key) / DAY_MS, 0.0), 1.0)

    prev_bars = closed[max(closed)] if closed else []
    if not prev_bars:
        raise InsufficientData("no completed prior session for H/L/C and pivots")
    pdh = max(candle.h for candle in prev_bars)
    pdl = min(candle.l for candle in prev_bars)
    pdc = prev_bars[-1].c
    pdo = prev_bars[0].o
    prev_vwap = session_vwap(prev_bars)
    session_high = max(candle.h for candle in intraday)
    session_low = min(candle.l for candle in intraday)

    pivots = floor_pivots(pdh, pdl, pdc)
    atr = wilder_atr(completed, 14)
    series = atr_series(completed, 14)
    atr_median_30 = statistics.median(series[-30:]) if len(series) >= 30 else atr
    vol_ratio = atr / atr_median_30 if atr_median_30 else 1.0

    closes = [candle.c for candle in completed]
    ema50_series = ema(closes, 50)
    ema_fast = ema50_series[-1]
    try:
        ema_slow = ema(closes, 200)[-1]
    except InsufficientData:
        ema_slow = ema_fast
        notes.append("EMA200 unavailable (fewer than 200 bars); bias component neutralised by degenerate stack")

    rates = [point.rate for point in funding_history]
    funding_percentile = (
        100.0 * sum(1 for rate in rates if rate <= ctx.funding) / len(rates) if rates else None
    )

    value_label = "above" if spot > va.vah else "below" if spot < va.val else "inside"
    prior_range_position = (pdc - pdl) / (pdh - pdl) if pdh > pdl else None
    structure = structure_read(completed, 20, 10)
    price_24h_pct = (spot / ctx.prev_day_px - 1.0) * 100 if ctx.prev_day_px else None

    bias = bias_report(
        spot=spot,
        ema_fast=ema_fast,
        ema_slow=ema_slow,
        value_label=value_label,
        prior_range_position=prior_range_position,
        structure=structure,
        funding_percentile=funding_percentile,
        oi_24h_pct=oi_24h_pct,
        price_24h_pct=price_24h_pct,
    )

    slope_atr = (ema50_series[-1] - ema50_series[-11]) / atr if len(ema50_series) >= 11 and atr else 0.0
    regime = classify_regime(
        closes=closes[-20:], va=va, spot=spot, atr=atr, slope_atr=slope_atr, vol_ratio=vol_ratio
    )

    setups = build_setups(
        spot=spot,
        atr=atr,
        va=va,
        vwap=vwap,
        pivots=pivots,
        pdh=pdh,
        pdl=pdl,
        bias_label=bias.label,
        min_rr=min_rr,
    )

    return LevelBook(
        symbol=symbol,
        as_of=as_of,
        spot=spot,
        mark=ctx.mark_px,
        oracle=ctx.oracle_px,
        prev_day_px=ctx.prev_day_px,
        funding_hourly=ctx.funding,
        funding_apr=ctx.funding * 24 * 365,
        funding_percentile=funding_percentile,
        funding_window_hours=len(rates),
        funding_venues=dict(funding_venues or {}),
        oi=ctx.open_interest,
        oi_prev_pct=oi_prev_pct,
        oi_24h_pct=oi_24h_pct,
        day_ntl_vlm=ctx.day_ntl_vlm,
        va=va,
        va_days=va_days,
        va_percent=va_percent,
        dev_va=dev_va,
        session_progress=session_progress,
        vwap=vwap,
        prev_vwap=prev_vwap,
        pdh=pdh,
        pdl=pdl,
        pdc=pdc,
        pdo=pdo,
        pdh_swept=session_high > pdh,
        pdl_swept=session_low < pdl,
        pivots=pivots,
        atr=atr,
        atr_pct=atr / spot * 100 if spot else 0.0,
        atr_median_30=atr_median_30,
        vol_ratio=vol_ratio,
        bias=bias,
        regime=regime,
        setups=setups,
        warnings=notes,
    )
