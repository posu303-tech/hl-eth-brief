"""Parsing tests: coercion, ordering, and the raw-JSON-on-missing-field contract."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from parse import (
    DataQualityError,
    MissingFieldError,
    candle_gap_warnings,
    parse_asset_ctx,
    parse_candles,
    parse_funding_history,
    parse_predicted_fundings,
)
from support import make_ctx_payload, make_funding_payload, make_predicted_payload

CANDLE = {"t": 1_791_957_600_000, "T": 1_791_961_199_999, "s": "ETH", "i": "1h",
          "o": "2502.2", "c": "2504.1", "h": "2509.1", "l": "2498.7", "v": "4899.0864", "n": 2166}


def payload(*candles: dict) -> list:
    return list(candles)


class CandleParsingTests(unittest.TestCase):
    def test_string_prices_become_floats(self):
        candles = parse_candles(payload(CANDLE), interval="1h", coin="ETH")
        self.assertEqual(len(candles), 1)
        candle = candles[0]
        self.assertIsInstance(candle.c, float)
        self.assertAlmostEqual(candle.o, 2502.2)
        self.assertAlmostEqual(candle.v, 4899.0864)
        self.assertEqual(candle.n, 2166)
        self.assertAlmostEqual(candle.typical, (2509.1 + 2498.7 + 2504.1) / 3)

    def test_sorts_by_open_time_and_dedupes(self):
        later = dict(CANDLE, t=CANDLE["t"] + 3_600_000, T=CANDLE["T"] + 3_600_000, c="2510.0", h="2511.0")
        duplicate = dict(CANDLE, c="2505.0")
        candles = parse_candles(payload(later, CANDLE, duplicate), interval="1h", coin="ETH")
        self.assertEqual([c.t for c in candles], [CANDLE["t"], CANDLE["t"] + 3_600_000])
        self.assertAlmostEqual(candles[0].c, 2505.0)  # last record wins on a duplicate

    def test_missing_volume_prints_raw_json(self):
        broken = dict(CANDLE)
        del broken["v"]
        with self.assertRaises(MissingFieldError) as caught:
            parse_candles(payload(broken), interval="1h", coin="ETH")
        error = caught.exception
        self.assertEqual(error.field, "v")
        self.assertEqual(error.raw, payload(broken))
        message = str(error)
        self.assertIn("'v' missing", message)
        self.assertIn('"o": "2502.2"', message)  # the offending record is in the dump
        self.assertIn("--- raw JSON ---", message)

    def test_null_field_counts_as_missing(self):
        broken = dict(CANDLE, h=None)
        with self.assertRaises(MissingFieldError) as caught:
            parse_candles(payload(broken), interval="1h", coin="ETH")
        self.assertIn("null/empty", str(caught.exception))

    def test_non_numeric_field_rejected(self):
        broken = dict(CANDLE, c="not-a-number")
        with self.assertRaises(MissingFieldError) as caught:
            parse_candles(payload(broken), interval="1h", coin="ETH")
        self.assertIn("not numeric", str(caught.exception))

    def test_empty_payload_rejected(self):
        with self.assertRaises(MissingFieldError):
            parse_candles([], interval="1h", coin="ETH")

    def test_high_below_low_rejected(self):
        broken = dict(CANDLE, h="2400.0", o="2450.0", c="2460.0")
        with self.assertRaises(DataQualityError):
            parse_candles(payload(broken), interval="1h", coin="ETH")

    def test_interval_mismatch_rejected(self):
        with self.assertRaises(DataQualityError):
            parse_candles(payload(CANDLE), interval="5m", coin="ETH")

    def test_trade_count_is_optional(self):
        lean = {key: value for key, value in CANDLE.items() if key != "n"}
        candles = parse_candles(payload(lean), interval="1h", coin="ETH")
        self.assertEqual(candles[0].n, 0)

    def test_gap_warning_flags_missing_bars(self):
        first = dict(CANDLE)
        third = dict(CANDLE, t=CANDLE["t"] + 3 * 3_600_000, T=CANDLE["T"] + 3 * 3_600_000)
        candles = parse_candles(payload(first, third), interval="1h", coin="ETH")
        warnings = candle_gap_warnings(candles, 3_600_000)
        self.assertEqual(len(warnings), 1)
        self.assertIn("bars missing", warnings[0])

    def test_no_gap_warning_on_contiguous_bars(self):
        second = dict(CANDLE, t=CANDLE["t"] + 3_600_000, T=CANDLE["T"] + 3_600_000)
        candles = parse_candles(payload(CANDLE, second), interval="1h", coin="ETH")
        self.assertEqual(candle_gap_warnings(candles, 3_600_000), [])


class AssetCtxTests(unittest.TestCase):
    def test_uses_universe_index_not_position_zero(self):
        ctx = parse_asset_ctx(make_ctx_payload("ETH", mark=2314.98), "ETH")
        self.assertEqual(ctx.coin, "ETH")
        self.assertAlmostEqual(ctx.mark_px, 2314.98)
        self.assertAlmostEqual(ctx.funding, 0.0000020)
        self.assertAlmostEqual(ctx.open_interest, 1_000_000.0)
        self.assertAlmostEqual(ctx.mid_px, 2314.98 * 1.0002, places=4)

    def test_missing_open_interest_dumps_raw(self):
        data = make_ctx_payload("ETH")
        del data[1][1]["openInterest"]
        with self.assertRaises(MissingFieldError) as caught:
            parse_asset_ctx(data, "ETH")
        error = caught.exception
        self.assertEqual(error.field, "openInterest")
        self.assertEqual(error.raw, data)
        self.assertIn('"markPx"', str(error))

    def test_unknown_coin_rejected(self):
        with self.assertRaises(MissingFieldError) as caught:
            parse_asset_ctx(make_ctx_payload("ETH"), "SOL")
        self.assertIn("coin not listed", str(caught.exception))

    def test_malformed_envelope_rejected(self):
        with self.assertRaises(MissingFieldError):
            parse_asset_ctx({"universe": []}, "ETH")


class FundingTests(unittest.TestCase):
    def test_history_sorted_ascending(self):
        points = parse_funding_history(make_funding_payload("ETH", count=5))
        self.assertEqual(len(points), 5)
        self.assertEqual([p.time for p in points], sorted(p.time for p in points))

    def test_history_missing_rate_dumps_raw(self):
        data = make_funding_payload("ETH", count=2)
        data[1].pop("fundingRate")
        with self.assertRaises(MissingFieldError) as caught:
            parse_funding_history(data)
        self.assertIn("fundingRate", str(caught.exception))

    def test_predicted_fundings_keyed_by_venue(self):
        venues = parse_predicted_fundings(make_predicted_payload("ETH", rate=0.00001), "ETH")
        self.assertEqual(set(venues), {"HlPerp", "BinPerp"})
        self.assertAlmostEqual(venues["HlPerp"][0], 0.00001)
        self.assertEqual(venues["HlPerp"][1], 1)
        self.assertEqual(venues["BinPerp"][1], 8)

    def test_predicted_fundings_absent_coin_returns_empty(self):
        self.assertEqual(parse_predicted_fundings(make_predicted_payload("ETH"), "SOL"), {})


if __name__ == "__main__":
    unittest.main()
