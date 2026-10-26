"""Replays a recorded Hyperliquid payload and asserts the brief still renders.

This is the regression guard against an API shape change: if Hyperliquid renames
a field, this test fails with the raw JSON attached before the live brief does.
Fixtures are produced with: python eth_brief.py --dump-payloads tests/fixtures --no-save
"""

from __future__ import annotations

import argparse
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import eth_brief
from brief import render

FIXTURES = Path(__file__).resolve().parent / "fixtures"


@unittest.skipUnless((FIXTURES / "meta.json").exists(), "no recorded fixtures in tests/fixtures")
class FixtureReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        meta = json.loads((FIXTURES / "meta.json").read_text(encoding="utf-8"))
        cls.meta = meta
        cls.payloads = {
            key: json.loads((FIXTURES / f"{key}.json").read_text(encoding="utf-8"))
            for key in eth_brief.PAYLOAD_KEYS
        }
        args = argparse.Namespace(
            session_start_hour=0, va_days=10, va_percent=0.70, bucket=None, min_rr=1.5
        )
        cls.book = eth_brief.build_book(cls.payloads, meta["symbol"], meta["as_of"], args)
        cls.text = render(cls.book)

    def test_all_five_payloads_parse(self):
        for key in eth_brief.PAYLOAD_KEYS:
            self.assertIn(key, self.payloads)

    def test_value_area_is_ordered(self):
        va = self.book.va
        self.assertLess(va.val, va.poc)
        self.assertLess(va.poc, va.vah)
        self.assertGreaterEqual(va.captured_pct, 0.69)

    def test_levels_are_plausible(self):
        self.assertGreater(self.book.atr, 0)
        self.assertLess(self.book.atr_pct, 10.0)
        self.assertGreater(self.book.pdh, self.book.pdl)
        self.assertGreater(self.book.oi, 0)
        self.assertNotEqual(self.book.vwap.vwap, 0.0)

    def test_three_setups_with_positive_risk(self):
        self.assertEqual(len(self.book.setups), 3)
        for setup in self.book.setups:
            self.assertGreater(setup.risk, 0)
            self.assertGreater(setup.rr1, 0)

    def test_render_has_four_sections(self):
        for header in ("## 1) HTF bias", "## 2) Intraday regime", "## 3) Setups", "## 4) Risk note"):
            self.assertIn(header, self.text)
        self.assertEqual(self.text.count("## "), 4)

    def test_structured_output_is_json_serialisable(self):
        payload = json.dumps(eth_brief.book_to_dict(self.book))
        self.assertIn('"setups"', payload)
        self.assertIn('"rr1"', payload)


if __name__ == "__main__":
    unittest.main()
