"""The published plan (levels.json) and the trigger state machine.

The 5-minute watch evaluates the *published* plan rather than recomputing one.
Recomputing every few minutes would let stops drift mid-trade and make "armed"
flicker; instead the daily levels (VA, pivots, PDH/PDL) and hourly ATR are frozen
into levels.json by the brief, and the watch only asks: has price reached a level,
and has a 5m close confirmed it?

State machine, per setup:

    WAITING --touch entry+-band--> ARMED --5m close beyond entry--> FIRED
       |                             |
       +--- 5m close beyond stop -----+--> VOID

`FIRED` and `VOID` are terminal for that plan day. Arming matters because a setup
must be *reached* before its confirmation counts: if price is already beyond the
entry when the plan is published (normal for a retest setup), the first close
beyond it must not fire.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Mapping, Sequence

from analytics import LevelBook, session_start
from parse import Candle

WAITING = "WAITING"
ARMED = "ARMED"
FIRED = "FIRED"
VOID = "VOID"
TERMINAL = (FIRED, VOID)

BAR_MS_5M = 300_000


def plan_day(as_of_ms: int) -> str:
    return datetime.fromtimestamp(session_start(as_of_ms) / 1000, tz=timezone.utc).date().isoformat()


def build_setup_plans(book: LevelBook) -> list[dict]:
    """Freeze each setup into machine-checkable levels."""
    band = 0.35 * book.atr
    plans = []
    for index, setup in enumerate(book.setups):
        plans.append(
            {
                "index": index,
                "name": setup.name,
                "side": setup.side,
                "entry": round(setup.entry, 4),
                "stop": round(setup.stop, 4),
                "t1": round(setup.t1, 4),
                "t2": round(setup.t2, 4),
                "arm_level": round(setup.entry, 4),
                "arm_direction": 1 if setup.side == "LONG" else -1,
                "invalid_level": round(setup.stop, 4),
                "touch_band": round(band, 4),
                "risk": round(setup.risk, 4),
                "rr1": round(setup.rr1, 4),
                "rr2": round(setup.rr2, 4),
                "stand_aside": setup.stand_aside,
                "trigger": setup.trigger,
                "invalidation": setup.invalidation,
            }
        )
    return plans


def build_levels(book: LevelBook, *, display_offset_minutes: int = 0) -> dict:
    """The machine-readable contract shared by the watch, the site and the alert."""
    day = plan_day(book.as_of)
    return {
        "symbol": book.symbol,
        "plan_id": f"{book.symbol}:{day}",
        "day": day,
        "as_of": book.as_of,
        "display_offset_minutes": display_offset_minutes,
        "spot": round(book.spot, 4),
        "mark": round(book.mark, 4),
        "oracle": round(book.oracle, 4),
        "funding_hourly": book.funding_hourly,
        "funding_apr": book.funding_apr,
        "open_interest": book.oi,
        "oi_24h_pct": book.oi_24h_pct,
        "value_area": {
            "val": round(book.va.val, 4),
            "poc": round(book.va.poc, 4),
            "vah": round(book.va.vah, 4),
            "width": round(book.va.width, 4),
            "bucket": book.va.bucket,
            "bars": book.va.bars,
            "sessions": book.va_days,
        },
        "developing_value_area": None
        if book.dev_va is None
        else {
            "val": round(book.dev_va.val, 4),
            "poc": round(book.dev_va.poc, 4),
            "vah": round(book.dev_va.vah, 4),
            "session_progress": round(book.session_progress, 4),
        },
        "vwap": {"value": round(book.vwap.vwap, 4), "sigma": round(book.vwap.sigma, 4)},
        "prior_day": {
            "high": round(book.pdh, 4),
            "low": round(book.pdl, 4),
            "close": round(book.pdc, 4),
            "open": round(book.pdo, 4),
            "high_swept": book.pdh_swept,
            "low_swept": book.pdl_swept,
        },
        "pivots": {
            "p": round(book.pivots.p, 4),
            "r1": round(book.pivots.r1, 4),
            "r2": round(book.pivots.r2, 4),
            "r3": round(book.pivots.r3, 4),
            "s1": round(book.pivots.s1, 4),
            "s2": round(book.pivots.s2, 4),
            "s3": round(book.pivots.s3, 4),
        },
        "atr": {
            "value": round(book.atr, 4),
            "pct": round(book.atr_pct, 4),
            "median_30": round(book.atr_median_30, 4),
            "ratio": round(book.vol_ratio, 4),
        },
        "bias": {"label": book.bias.label, "score": book.bias.score, "max_score": book.bias.max_score},
        "regime": {
            "label": book.regime.label,
            "value_label": book.regime.value_label,
            "pct_closes_outside": round(book.regime.pct_closes_outside, 4),
        },
        "setups": build_setup_plans(book),
        "warnings": list(book.warnings),
    }


def fresh_state() -> dict:
    return {"status": WAITING, "armed_at": None, "last_bar_t": 0, "event_at": None, "detail": ""}


def eligible_bars(levels: Mapping, bars: Sequence[Candle], *, now_ms: int) -> list[Candle]:
    """Only bars that closed after the plan was published, and are already closed.

    Without the lower bound the watch would grade a fresh plan against history that
    predates it (a stop can look 'broken' by a move that happened before the level
    existed). Without the upper bound it would act on a half-formed candle.
    """
    as_of = int(levels["as_of"])
    return [bar for bar in bars if as_of < bar.T <= now_ms]


def evaluate_setup(
    plan: Mapping,
    bars: Sequence[Candle],
    state: Mapping | None,
) -> tuple[dict, dict | None]:
    """Walk new bars in order and return (new_state, event or None).

    Idempotent: bars at or before ``state['last_bar_t']`` are ignored, so running
    the watch twice within one 5-minute candle cannot double-fire.
    """
    current = dict(state or fresh_state())
    if current.get("status") in TERMINAL:
        if bars:
            current["last_bar_t"] = max(int(current.get("last_bar_t") or 0), bars[-1].t)
        return current, None

    status = current.get("status", WAITING)
    armed_at = current.get("armed_at")
    last_bar_t = int(current.get("last_bar_t") or 0)

    direction = int(plan["arm_direction"])
    arm = float(plan["arm_level"])
    band = float(plan["touch_band"])
    invalid = float(plan["invalid_level"])

    event: dict | None = None
    for bar in bars:
        if bar.t <= last_bar_t:
            continue
        last_bar_t = bar.t

        # A close beyond the stop kills the plan regardless of arming.
        if (direction > 0 and bar.c < invalid) or (direction < 0 and bar.c > invalid):
            status = VOID
            event = _event(plan, VOID, bar, level=invalid)
            break

        if bar.l <= arm + band and bar.h >= arm - band:
            status = ARMED
            armed_at = bar.t

        confirmed = bar.c > arm if direction > 0 else bar.c < arm
        if status == ARMED and confirmed:
            status = FIRED
            event = _event(plan, FIRED, bar, level=arm)
            break

    current.update(status=status, armed_at=armed_at, last_bar_t=last_bar_t)
    if event:
        current["event_at"] = event["bar_t"]
        current["detail"] = event["message"]
    return current, event


def _event(plan: Mapping, status: str, bar: Candle, *, level: float) -> dict:
    return {
        "index": plan["index"],
        "name": plan["name"],
        "side": plan["side"],
        "status": status,
        "bar_t": bar.t,
        "price": round(bar.c, 4),
        "level": round(level, 4),
        "stop": plan["stop"],
        "t1": plan["t1"],
        "t2": plan["t2"],
        "rr1": plan["rr1"],
        "rr2": plan["rr2"],
        "tradable": not plan.get("stand_aside", False),
        "message": _message(plan, status, bar, level),
    }


def _message(plan: Mapping, status: str, bar: Candle, level: float) -> str:
    if status == VOID:
        side = "below" if plan["arm_direction"] > 0 else "above"
        return f"5m close {bar.c:,.2f} {side} the invalidation {level:,.2f} - plan dead"
    verb = "above" if plan["arm_direction"] > 0 else "below"
    return f"5m close {bar.c:,.2f} {verb} entry {level:,.2f}"


def evaluate_all(
    levels: Mapping,
    bars: Sequence[Candle],
    states: Mapping[str, Mapping] | None,
) -> tuple[dict, list[dict]]:
    """Evaluate every setup in the plan; returns ({index: state}, [events])."""
    states = states or {}
    out: dict[str, dict] = {}
    events: list[dict] = []
    for plan in levels["setups"]:
        key = str(plan["index"])
        new_state, event = evaluate_setup(plan, bars, states.get(key))
        out[key] = new_state
        if event:
            events.append(event)
    return out, events
