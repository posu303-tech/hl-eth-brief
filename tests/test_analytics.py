"""Maths tests against hand-computed answers, plus one end-to-end compute."""

from __future__ import annotations

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from analytics import (
    InsufficientData,
    ValueArea,
    atr_series,
    auto_bucket,
    bias_report,
    build_setups,
    classify_regime,
    compute,
    ema,
    floor_pivots,
    group_sessions,
    session_start,
    session_vwap,
    structure_read,
    true_ranges,
    value_area,
    value_area_from_hist,
    volume_profile,
    VWAP,
    wilder_atr,
)
from brief import render
from parse import AssetCtx, Candle, FundingPoint
from support import (
    DAY_MS,
    HOUR_MS,
    make_candles,
    make_ctx_payload,
    make_funding_points,
)

AS_OF = int(datetime(2026, 10, 26, 12, 0, tzinfo=timezone.utc).timestamp() * 1000)


def candle(t, o, h, l, c, v=10.0) -> Candle:
    return Candle(t=t, T=t + HOUR_MS - 1, o=o, h=h, l=l, c=c, v=v, n=10)


class SessionTests(unittest.TestCase):
    def test_session_start_floors_to_utc_midnight(self):
        ts = AS_OF  # 2026-10-26 12:00 UTC
        self.assertEqual(session_start(ts), ts - 12 * HOUR_MS)

    def test_session_start_honours_shift(self):
        ts = AS_OF
        shifted = session_start(ts, start_hour=6)
        self.assertEqual(shifted % DAY_MS, 6 * HOUR_MS)
        self.assertLessEqual(shifted, ts)
        self.assertGreater(shifted + DAY_MS, ts)

    def test_group_sessions_splits_on_boundary(self):
        midnight = session_start(AS_OF)
        bars = [candle(midnight - HOUR_MS, 1, 2, 0.5, 1.5), candle(midnight, 1, 2, 0.5, 1.8)]
        sessions = group_sessions(bars)
        self.assertEqual(len(sessions), 2)


class VolumeProfileTests(unittest.TestCase):
    def test_bar_volume_fans_across_its_range(self):
        hist = volume_profile([candle(0, 1, 2, 0, 1, v=100.0)], bucket=1.0)
        self.assertAlmostEqual(hist[0], 50.0)
        self.assertAlmostEqual(hist[1], 50.0)
        self.assertEqual(len(hist), 2)

    def test_value_area_expands_toward_heavier_side(self):
        va = value_area_from_hist({0: 20.0, 1: 30.0, 2: 50.0}, bucket=1.0, percent=0.70, bars=3)
        self.assertAlmostEqual(va.poc, 2.5)
        self.assertAlmostEqual(va.val, 1.0)
        self.assertAlmostEqual(va.vah, 3.0)
        self.assertGreaterEqual(va.captured_pct, 0.70)

    def test_poc_alone_can_cover_target(self):
        va = value_area_from_hist({0: 10.0, 1: 80.0, 2: 10.0}, bucket=1.0, percent=0.70)
        self.assertAlmostEqual(va.poc, 1.5)
        self.assertAlmostEqual(va.val, 1.0)
        self.assertAlmostEqual(va.vah, 2.0)

    def test_tie_prefers_lower_bucket_for_poc(self):
        va = value_area_from_hist({0: 30.0, 1: 30.0}, bucket=1.0, percent=0.70)
        self.assertAlmostEqual(va.poc, 0.5)

    def test_empty_profile_raises(self):
        with self.assertRaises(InsufficientData):
            value_area_from_hist({}, bucket=1.0)

    def test_value_area_from_candles_is_ordered(self):
        bars = make_candles(96, AS_OF - 96 * HOUR_MS, HOUR_MS, 2000.0, drift=0.0001, amplitude=0.7)
        va = value_area(bars, bucket=1.0)
        self.assertLess(va.val, va.poc)
        self.assertLess(va.poc, va.vah)
        self.assertGreater(va.total_volume, 0)

    def test_auto_bucket_is_a_round_number(self):
        self.assertEqual(auto_bucket(2315.0), 1.0)
        self.assertEqual(auto_bucket(100_000.0), 50.0)
        self.assertEqual(auto_bucket(0.5), 0.0002)


class VWAPTests(unittest.TestCase):
    def test_hand_computed_two_bars(self):
        bars = [candle(0, 9, 10, 8, 9), candle(0, 11, 12, 10, 11)]
        vwap = session_vwap(bars)
        self.assertAlmostEqual(vwap.vwap, 10.0)
        self.assertAlmostEqual(vwap.sigma, 1.0)
        self.assertAlmostEqual(vwap.volume, 20.0)

    def test_zero_volume_raises(self):
        with self.assertRaises(InsufficientData):
            session_vwap([candle(0, 1, 2, 0.5, 1.5, v=0.0)])


class PivotTests(unittest.TestCase):
    def test_floor_pivots_hand_computed(self):
        pivots = floor_pivots(high=110.0, low=90.0, close=100.0)
        self.assertAlmostEqual(pivots.p, 100.0)
        self.assertAlmostEqual(pivots.r1, 110.0)
        self.assertAlmostEqual(pivots.r2, 120.0)
        self.assertAlmostEqual(pivots.r3, 130.0)
        self.assertAlmostEqual(pivots.s1, 90.0)
        self.assertAlmostEqual(pivots.s2, 80.0)
        self.assertAlmostEqual(pivots.s3, 70.0)


class ATRTests(unittest.TestCase):
    def test_true_range_uses_prior_close(self):
        bars = [candle(0, 9, 10, 8, 9), candle(0, 11, 12, 9, 11)]
        self.assertEqual(true_ranges(bars), [2.0, 3.0])

    def test_wilder_atr_hand_computed(self):
        bars = [
            candle(0, 9, 10, 8, 9),
            candle(0, 10, 12, 9, 11),
            candle(0, 11, 13, 11, 12),
        ]
        self.assertAlmostEqual(wilder_atr(bars, period=2), 2.25)

    def test_atr_needs_enough_bars(self):
        with self.assertRaises(InsufficientData):
            wilder_atr([candle(0, 1, 2, 0.5, 1.5)], period=14)

    def test_atr_series_length(self):
        bars = make_candles(30, 0, HOUR_MS, 2000.0, amplitude=0.5)
        self.assertEqual(len(atr_series(bars, period=14)), 30 - 14 + 1)


class EMATests(unittest.TestCase):
    def test_hand_computed_ema(self):
        self.assertEqual([round(value, 6) for value in ema([1, 2, 3, 4, 5], 3)], [2.0, 3.0, 4.0])

    def test_insufficient_values(self):
        with self.assertRaises(InsufficientData):
            ema([1, 2], 5)


class StructureTests(unittest.TestCase):
    def test_higher_highs_and_lows(self):
        bars = make_candles(20, 0, HOUR_MS, 2000.0, drift=0.002)
        self.assertEqual(structure_read(bars, 20, 10), "higher")

    def test_lower_highs_and_lows(self):
        bars = make_candles(20, 0, HOUR_MS, 2000.0, drift=-0.002)
        self.assertEqual(structure_read(bars, 20, 10), "lower")

    def test_insufficient_history(self):
        self.assertEqual(structure_read(make_candles(5, 0, HOUR_MS, 2000.0), 20, 10), "insufficient")


class BiasTests(unittest.TestCase):
    def test_all_components_bullish(self):
        report = bias_report(
            spot=100.0, ema_fast=90.0, ema_slow=80.0, value_label="above",
            prior_range_position=0.9, structure="higher", funding_percentile=10.0,
            oi_24h_pct=5.0, price_24h_pct=2.0,
        )
        self.assertEqual(report.score, 6)
        self.assertEqual(report.label, "Bullish")

    def test_all_components_bearish(self):
        report = bias_report(
            spot=100.0, ema_fast=110.0, ema_slow=120.0, value_label="below",
            prior_range_position=0.1, structure="lower", funding_percentile=95.0,
            oi_24h_pct=5.0, price_24h_pct=-2.0,
        )
        self.assertEqual(report.score, -6)
        self.assertEqual(report.label, "Bearish")

    def test_neutral_needs_three(self):
        report = bias_report(
            spot=100.0, ema_fast=90.0, ema_slow=80.0, value_label="above",
            prior_range_position=0.5, structure="mixed", funding_percentile=50.0,
            oi_24h_pct=None, price_24h_pct=None,
        )
        self.assertEqual(report.score, 2)
        self.assertEqual(report.label, "Balanced")

    def test_threshold_is_three(self):
        report = bias_report(
            spot=100.0, ema_fast=90.0, ema_slow=80.0, value_label="above",
            prior_range_position=0.9, structure="mixed", funding_percentile=50.0,
            oi_24h_pct=None, price_24h_pct=None,
        )
        self.assertEqual(report.score, 3)
        self.assertEqual(report.label, "Bullish")

    def test_missing_oi_is_neutral_not_guessed(self):
        report = bias_report(
            spot=100.0, ema_fast=100.0, ema_slow=100.0, value_label="inside",
            prior_range_position=None, structure="mixed", funding_percentile=None,
            oi_24h_pct=None, price_24h_pct=None,
        )
        self.assertEqual(report.score, 0)
        self.assertIn("n/a", report.components[-1].read)


class RegimeTests(unittest.TestCase):
    def setUp(self):
        self.va = ValueArea(poc=100.0, val=90.0, vah=110.0, total_volume=1000.0,
                            captured_volume=700.0, bucket=1.0, bars=240)

    def test_trend_up(self):
        report = classify_regime(closes=[120.0] * 20, va=self.va, spot=120.0, atr=5.0,
                                 slope_atr=1.2, vol_ratio=1.1)
        self.assertEqual(report.label, "trend-up")
        self.assertEqual(report.value_label, "above")

    def test_trend_down(self):
        report = classify_regime(closes=[80.0] * 20, va=self.va, spot=80.0, atr=5.0,
                                 slope_atr=-1.2, vol_ratio=1.1)
        self.assertEqual(report.label, "trend-down")

    def test_rotational_inside(self):
        report = classify_regime(closes=[100.0, 101.0, 99.0] * 7, va=self.va, spot=100.0,
                                 atr=5.0, slope_atr=0.0, vol_ratio=1.0)
        self.assertEqual(report.label, "rotational-balance")
        self.assertEqual(report.value_label, "inside")

    def test_failed_auction(self):
        closes = [120.0, 121.0, 119.0, 105.0, 104.0, 102.0]
        report = classify_regime(closes=closes, va=self.va, spot=102.0, atr=5.0,
                                 slope_atr=0.0, vol_ratio=1.0)
        self.assertEqual(report.label, "failed-auction")

    def test_breakout_attempt_without_slope(self):
        report = classify_regime(closes=[120.0] * 20, va=self.va, spot=120.0, atr=5.0,
                                 slope_atr=0.1, vol_ratio=1.0)
        self.assertEqual(report.label, "breakout-attempt")

    def test_distances_are_in_atr_units(self):
        report = classify_regime(closes=[120.0] * 20, va=self.va, spot=120.0, atr=5.0,
                                 slope_atr=1.2, vol_ratio=1.0)
        self.assertAlmostEqual(report.distance_vah_atr, 2.0)
        self.assertAlmostEqual(report.distance_poc_atr, 4.0)


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.va = ValueArea(poc=100.0, val=90.0, vah=110.0, total_volume=1000.0,
                            captured_volume=700.0, bucket=1.0, bars=240)
        self.vwap = VWAP(vwap=101.0, sigma=2.0, volume=1000.0, bars=144)
        self.pivots = floor_pivots(110.0, 90.0, 100.0)

    def build(self, spot, bias_label="Balanced"):
        return build_setups(spot=spot, atr=5.0, va=self.va, vwap=self.vwap,
                            pivots=self.pivots, pdh=112.0, pdl=88.0, bias_label=bias_label)

    def test_always_three_setups(self):
        for spot in (85.0, 100.0, 95.0, 105.0, 115.0):
            setups = self.build(spot)
            self.assertEqual(len(setups), 3)
            for setup in setups:
                self.assertGreater(setup.risk, 0)
                self.assertGreater(setup.rr1, 0)
                self.assertIn(setup.side, {"LONG", "SHORT"})

    def test_long_stop_is_below_entry_short_above(self):
        for setup in self.build(115.0):
            if setup.side == "LONG":
                self.assertLess(setup.stop, setup.entry)
                self.assertGreater(setup.t1, setup.entry)
            else:
                self.assertGreater(setup.stop, setup.entry)
                self.assertLess(setup.t1, setup.entry)

    def test_rr_math(self):
        from analytics import Setup
        setup = Setup(name="x", side="LONG", trigger="t", entry=100.0, stop=95.0,
                      t1=110.0, t2=120.0, invalidation="i")
        self.assertAlmostEqual(setup.risk, 5.0)
        self.assertAlmostEqual(setup.rr1, 2.0)
        self.assertAlmostEqual(setup.rr2, 4.0)
        self.assertFalse(setup.stand_aside)

    def test_thin_rr_flags_stand_aside(self):
        from analytics import Setup
        setup = Setup(name="x", side="LONG", trigger="t", entry=100.0, stop=95.0,
                      t1=105.0, t2=120.0, invalidation="i")
        self.assertAlmostEqual(setup.rr1, 1.0)
        self.assertTrue(setup.stand_aside)

    def test_inside_value_fades_toward_poc(self):
        setups = self.build(95.0)  # lower half of value
        self.assertEqual(setups[0].side, "LONG")
        self.assertAlmostEqual(setups[0].entry, 90.0)
        self.assertAlmostEqual(setups[0].t1, 100.0)


class ComputeEndToEndTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start = AS_OF - 600 * HOUR_MS
        cls.bars_1h = make_candles(600, start, HOUR_MS, 2000.0, drift=0.0001, amplitude=0.8)
        last_price = cls.bars_1h[-1].c
        cls.bars_5m = make_candles(200, AS_OF - 200 * 5 * 60_000, 5 * 60_000, last_price, amplitude=1.5)
        cls.spot = cls.bars_5m[-1].c
        cls.ctx = AssetCtx(
            coin="ETH", funding=0.0000021, open_interest=1_104_331.97,
            prev_day_px=cls.bars_1h[-25].c, oracle_px=cls.spot * 1.0005,
            mark_px=cls.spot, day_ntl_vlm=732_131_271.0, day_base_vlm=314_261.0,
            mid_px=cls.spot * 1.0002, premium=-0.00017,
        )
        cls.funding = make_funding_points("ETH", count=720, end_ms=AS_OF)
        cls.book = compute(
            symbol="ETH", as_of=AS_OF, candles_1h=cls.bars_1h, candles_5m=cls.bars_5m,
            ctx=cls.ctx, funding_history=cls.funding,
            funding_venues={"HlPerp": (0.0000021, 1), "BinPerp": (0.00001, 8)},
            oi_24h_pct=2.5,
        )

    def test_value_area_is_ordered_and_covers_target(self):
        va = self.book.va
        self.assertLess(va.val, va.poc)
        self.assertLess(va.poc, va.vah)
        self.assertGreaterEqual(va.captured_pct, 0.69)
        self.assertEqual(va.bars, len([c for c in self.bars_1h if c.T <= AS_OF][-240:]))

    def test_prior_day_levels_come_from_a_completed_session(self):
        self.assertGreater(self.book.pdh, self.book.pdl)
        self.assertGreaterEqual(self.book.pdc, self.book.pdl)
        self.assertLessEqual(self.book.pdc, self.book.pdh)

    def test_atr_and_vwap_are_finite(self):
        self.assertGreater(self.book.atr, 0)
        self.assertGreater(self.book.vwap.volume, 0)
        self.assertTrue(0 <= self.book.session_progress <= 1)

    def test_three_setups_all_have_positive_risk(self):
        self.assertEqual(len(self.book.setups), 3)
        for setup in self.book.setups:
            self.assertGreater(setup.risk, 0)

    def test_bias_has_six_components(self):
        self.assertEqual(len(self.book.bias.components), 6)
        self.assertEqual(self.book.bias.score, sum(c.score for c in self.book.bias.components))

    def test_render_has_exactly_four_sections(self):
        text = render(self.book)
        for header in ("## 1) HTF bias", "## 2) Intraday regime", "## 3) Setups", "## 4) Risk note"):
            self.assertIn(header, text)
        self.assertEqual(text.count("## "), 4)

    def test_render_states_value_position_and_no_forecast(self):
        text = render(self.book)
        self.assertIn("value", text)
        self.assertTrue("above value" in text or "inside value" in text or "below value" in text)
        self.assertIn("no price forecast", text)

    def test_render_is_ascii(self):
        render(self.book).encode("ascii")


if __name__ == "__main__":
    unittest.main()
