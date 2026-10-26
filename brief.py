"""Renders the brief. Four fixed sections, ASCII only, no forecasts.

Section order is fixed on purpose: bias, then regime/value, then the three
conditional setups, then one risk line. If a setup's first target does not pay
at least 1.5R it is still printed, but flagged STAND ASIDE rather than dressed up.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from analytics import LevelBook, Setup


def offset_label(minutes: int) -> str:
    if not minutes:
        return "UTC"
    sign = "+" if minutes > 0 else "-"
    total = abs(minutes)
    return f"UTC{sign}{total // 60:02d}:{total % 60:02d}"


def _stamp(ms: int, offset_minutes: int = 0) -> str:
    utc = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
    if not offset_minutes:
        return utc.strftime("%Y-%m-%d %H:%M UTC")
    local = utc + timedelta(minutes=offset_minutes)
    return f"{local:%Y-%m-%d %H:%M} {offset_label(offset_minutes)} ({utc:%H:%M} UTC)"


def _p(value: float | None, fallback: str = "n/a") -> str:
    return fallback if value is None else f"{value:,.2f}"


def _signed(value: float | None, digits: int = 2, suffix: str = "", fallback: str = "n/a") -> str:
    return fallback if value is None else f"{value:+.{digits}f}{suffix}"


def _score(value: int) -> str:
    return f"{value:+d}" if value else "0"


def _setup_block(index: int, setup: Setup) -> list[str]:
    lines = [
        f"**S{index} - {setup.name}** [{setup.side}]",
        f"- trigger: {setup.trigger}",
        f"- entry {_p(setup.entry)} | stop {_p(setup.stop)} | T1 {_p(setup.t1)} | T2 {_p(setup.t2)}",
        f"- R:R {setup.rr1:.2f} at T1, {setup.rr2:.2f} at T2 | risk {setup.risk:,.2f}",
        f"- invalid: {setup.invalidation}",
    ]
    if setup.stand_aside:
        lines.append(
            f"- verdict: STAND ASIDE - T1 pays {setup.rr1:.2f}R, below the {setup.min_rr:.1f}R floor"
        )
    else:
        lines.append(f"- verdict: valid only if the trigger prints (T1 {setup.rr1:.2f}R)")
    return lines


def render(book: LevelBook, *, display_offset_minutes: int = 0) -> str:
    va = book.va
    regime = book.regime
    pct_of_spot = va.width / book.spot * 100 if book.spot else 0.0

    lines: list[str] = []
    oi_parts = []
    if book.oi_prev_pct is not None:
        oi_parts.append(f"{book.oi_prev_pct:+.3f}% vs last run")
    oi_parts.append(
        f"{book.oi_24h_pct:+.2f}% 24h" if book.oi_24h_pct is not None else "24h n/a until the store has a day"
    )
    lines.append(f"# {book.symbol} perp (Hyperliquid) - {_stamp(book.as_of, display_offset_minutes)}")
    lines.append(
        f"spot {_p(book.spot)} | mark {_p(book.mark)} | oracle {_p(book.oracle)} | "
        f"OI {book.oi:,.2f} {book.symbol} ({', '.join(oi_parts)})"
    )
    lines.append(
        f"funding {_signed(book.funding_hourly * 100, 5, '%/hr')} "
        f"(~{_signed(book.funding_apr * 100, 2, '%/yr')}"
        + (
            f", {book.funding_percentile:.0f}th pct of last {book.funding_window_hours}h"
            if book.funding_percentile is not None
            else ""
        )
        + f") | 24h notional ${book.day_ntl_vlm / 1e6:,.1f}m"
    )
    lines.append("")

    # ---------------------------------------------------------------- 1) bias
    lines.append(f"## 1) HTF bias - {book.bias.label.upper()} ({book.bias.score:+d} of +-{book.bias.max_score})")
    lines.append("")
    lines.append("| component | read | score |")
    lines.append("|---|---|---|")
    for component in book.bias.components:
        lines.append(f"| {component.name} | {component.read} | {_score(component.score)} |")
    lines.append("")

    # --------------------------------------------------- 2) regime and value
    lines.append(f"## 2) Intraday regime - {regime.label}, price {regime.value_label.upper()} value")
    lines.append("")
    lines.append(
        f"- value area ({book.va_days} UTC sessions, {book.va_percent:.0%}): "
        f"VAL {_p(va.val)} | POC {_p(va.poc)} | VAH {_p(va.vah)} "
        f"(width {va.width:,.2f} = {pct_of_spot:.2f}% of spot, {va.bars} bars)"
    )
    if book.dev_va is not None:
        lines.append(
            f"- developing session ({book.session_progress:.0%} elapsed): "
            f"VAL {_p(book.dev_va.val)} | POC {_p(book.dev_va.poc)} | VAH {_p(book.dev_va.vah)}"
        )
    bands = (
        f"- session VWAP {_p(book.vwap.vwap)} (+1s {_p(book.vwap.vwap + book.vwap.sigma)} / "
        f"-1s {_p(book.vwap.vwap - book.vwap.sigma)})"
    )
    if book.prev_vwap is not None:
        bands += f" | prior session VWAP {_p(book.prev_vwap.vwap)}"
    lines.append(bands)
    lines.append(
        f"- prior day: PDH {_p(book.pdh)} | PDL {_p(book.pdl)} | PDC {_p(book.pdc)} "
        f"(PDH {'swept' if book.pdh_swept else 'intact'}, PDL {'swept' if book.pdl_swept else 'intact'})"
    )
    lines.append(
        f"- floor pivots: S3 {_p(book.pivots.s3)} | S2 {_p(book.pivots.s2)} | S1 {_p(book.pivots.s1)} | "
        f"P {_p(book.pivots.p)} | R1 {_p(book.pivots.r1)} | R2 {_p(book.pivots.r2)} | R3 {_p(book.pivots.r3)}"
    )
    lines.append(
        f"- 1H ATR(14) {book.atr:,.2f} = {book.atr_pct:.2f}% of spot "
        f"| ATR vs 30d median x{book.vol_ratio:.2f}"
    )
    lines.append(
        f"- distance to POC {regime.distance_poc_atr:+.2f} ATR | VAH {regime.distance_vah_atr:+.2f} ATR "
        f"| VAL {regime.distance_val_atr:+.2f} ATR | closes outside value (last 20): {regime.pct_closes_outside:.0%}"
    )
    if book.funding_venues:
        venue_bits = []
        for name, (rate, interval) in sorted(book.funding_venues.items()):
            per_hour = rate / interval if interval else rate
            venue_bits.append(f"{name} {per_hour * 100:+.5f}%/hr")
        lines.append(f"- cross-venue funding: {', '.join(venue_bits)}")
    lines.append("")

    # -------------------------------------------------------------- 3) setups
    lines.append("## 3) Setups (conditional - trigger first, then act)")
    lines.append("")
    for index, setup in enumerate(book.setups, start=1):
        lines.extend(_setup_block(index, setup))
        lines.append("")

    # ---------------------------------------------------------------- 4) risk
    tradable = [setup for setup in book.setups if not setup.stand_aside]
    pool = tradable or book.setups
    risks = sorted(setup.risk for setup in pool if setup.risk > 0)
    if risks:
        stop_text = (
            f"{risks[0] / book.atr:.2f}-{risks[-1] / book.atr:.2f}x the 1H ATR "
            f"(~${risks[0]:,.2f}-${risks[-1]:,.2f})"
        )
    else:
        stop_text = "ATR-sized stops"
    qualifier = "" if tradable else " (no setup cleared the R:R floor, so these are reference stops)"
    lines.append(
        f"## 4) Risk note\n"
        f"Stops sit {stop_text}{qualifier}; funding runs {book.funding_hourly * 24 * 100:+.4f}%/day "
        f"(${book.funding_hourly * 10_000:+.2f}/hr per $10k notional), so size so one ATR of adverse "
        f"excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms."
    )
    lines.append("")

    if book.warnings:
        lines.append("_data notes: " + "; ".join(book.warnings) + "_")
    lines.append("_Levels are conditional triggers derived from observed candles; no price forecast is implied._")
    return "\n".join(lines)


def render_plan_message(book: LevelBook, *, display_offset_minutes: int = 0) -> str:
    """Compact plan for a Telegram push: the levels, not the essay."""
    va = book.va
    lines = [
        f"{book.symbol} plan - {_stamp(book.as_of, display_offset_minutes)}",
        f"spot {_p(book.spot)} | bias {book.bias.label.upper()} ({book.bias.score:+d}) "
        f"| {book.regime.label}, {book.regime.value_label} value",
        f"VA10  VAL {_p(va.val)} | POC {_p(va.poc)} | VAH {_p(va.vah)}",
        f"PDH {_p(book.pdh)} | PDL {_p(book.pdl)} | 1H ATR {book.atr:,.2f} ({book.atr_pct:.2f}%)",
        "setups:",
    ]
    for index, setup in enumerate(book.setups, start=1):
        flag = " (stand aside)" if setup.stand_aside else ""
        lines.append(
            f"S{index} {setup.side} {_p(setup.entry)} | stop {_p(setup.stop)} | "
            f"T1 {_p(setup.t1)} | T2 {_p(setup.t2)} | {setup.rr1:.1f}R{flag}"
        )
    return "\n".join(lines)
