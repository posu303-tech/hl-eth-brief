"""State machine tests: arming, confirmation, invalidation, idempotency, staleness.

These pin the rules that decide whether your phone buzzes, so they are tested
against exact bar sequences rather than approximate ones.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from parse import Candle

import levels as lv
from fixtures_helper import available, build_book_from_fixtures

T0 = 1_793_000_000_000  # arbitrary but fixed
BAR = 300_000


def bar(offset: int, o: float, h: float, l: float, c: float) -> Candle:
    start = T0 + offset * BAR
    return Candle(t=start, T=start + BAR - 1, o=o, h=h, l=l, c=c, v=10.0, n=5)


def long_plan(**overrides) -> dict:
    plan = {
        "index": 0,
        "name": "test long",
        "side": "LONG",
        "entry": 100.0,
        "stop": 95.0,
        "t1": 110.0,
        "t2": 120.0,
        "arm_level": 100.0,
        "arm_direction": 1,
        "invalid_level": 95.0,
        "touch_band": 1.0,
        "rr1": 2.0,
        "rr2": 4.0,
        "stand_aside": False,
    }
    plan.update(overrides)
    return plan


def short_plan(**overrides) -> dict:
    plan = long_plan(
        index=1,
        name="test short",
        side="SHORT",
        entry=110.0,
        stop=115.0,
        arm_level=110.0,
        arm_direction=-1,
        invalid_level=115.0,
        t1=100.0,
        t2=90.0,
    )
    plan.update(overrides)
    return plan


class ArmAndFireTests(unittest.TestCase):
    def test_touch_arms_without_firing(self):
        bars = [bar(1, 99.0, 101.0, 98.5, 99.4)]
        state, event = lv.evaluate_setup(long_plan(), bars, None)
        self.assertIsNone(event)
        self.assertEqual(state["status"], lv.ARMED)
        self.assertEqual(state["armed_at"], bars[0].t)

    def test_armed_then_close_beyond_entry_fires(self):
        bars = [
            bar(1, 99.0, 101.0, 98.5, 99.4),   # touch -> armed
            bar(2, 99.6, 101.2, 99.4, 100.8),  # close above entry -> fired
        ]
        state, event = lv.evaluate_setup(long_plan(), bars, None)
        self.assertEqual(state["status"], lv.FIRED)
        self.assertIsNotNone(event)
        self.assertEqual(event["status"], lv.FIRED)
        self.assertAlmostEqual(event["price"], 100.8)
        self.assertAlmostEqual(event["level"], 100.0)

    def test_same_bar_touch_and_reclaim_fires(self):
        bars = [bar(1, 98.0, 101.0, 97.5, 100.9)]
        state, event = lv.evaluate_setup(long_plan(), bars, None)
        self.assertEqual(state["status"], lv.FIRED)
        self.assertIsNotNone(event)

    def test_no_fire_without_a_touch(self):
        bars = [
            bar(1, 96.5, 97.5, 96.0, 96.8),      # above the stop, well below the band
            bar(2, 105.0, 106.0, 104.0, 105.5),  # beyond entry, but it never traded at it
        ]
        state, event = lv.evaluate_setup(long_plan(), bars, None)
        self.assertIsNone(event)
        self.assertEqual(state["status"], lv.WAITING)

    def test_short_fires_on_close_below_entry(self):
        bars = [
            bar(1, 110.5, 111.0, 109.8, 110.2),  # touch -> armed
            bar(2, 110.0, 110.2, 109.0, 109.4),  # close below -> fired
        ]
        state, event = lv.evaluate_setup(short_plan(), bars, None)
        self.assertEqual(state["status"], lv.FIRED)
        self.assertAlmostEqual(event["price"], 109.4)

    def test_short_does_not_fire_on_close_above_entry(self):
        bars = [
            bar(1, 110.5, 111.0, 109.8, 110.2),
            bar(2, 110.0, 111.5, 109.9, 111.2),
        ]
        state, event = lv.evaluate_setup(short_plan(), bars, None)
        self.assertIsNone(event)
        self.assertEqual(state["status"], lv.ARMED)


class InvalidationTests(unittest.TestCase):
    def test_close_beyond_stop_voids(self):
        bars = [bar(1, 96.0, 96.5, 94.0, 94.5)]
        state, event = lv.evaluate_setup(long_plan(), bars, None)
        self.assertEqual(state["status"], lv.VOID)
        self.assertEqual(event["status"], lv.VOID)
        self.assertIn("plan dead", event["message"])

    def test_short_voids_on_close_above_stop(self):
        bars = [bar(1, 114.0, 116.0, 113.5, 115.5)]
        state, event = lv.evaluate_setup(short_plan(), bars, None)
        self.assertEqual(state["status"], lv.VOID)

    def test_void_is_terminal(self):
        bars = [bar(1, 96.0, 96.5, 94.0, 94.5)]
        state, event = lv.evaluate_setup(long_plan(), bars, None)
        self.assertEqual(state["status"], lv.VOID)
        later, second = lv.evaluate_setup(long_plan(), [bar(2, 95.0, 101.0, 95.0, 100.5)], state)
        self.assertIsNone(second)
        self.assertEqual(later["status"], lv.VOID)

    def test_fired_is_terminal(self):
        bars = [bar(1, 99.0, 101.0, 98.5, 100.9)]
        state, _ = lv.evaluate_setup(long_plan(), bars, None)
        self.assertEqual(state["status"], lv.FIRED)
        later, second = lv.evaluate_setup(long_plan(), [bar(2, 96.0, 96.5, 94.0, 94.5)], state)
        self.assertIsNone(second)
        self.assertEqual(later["status"], lv.FIRED)


class StalenessTests(unittest.TestCase):
    def test_repeat_bars_do_not_double_fire(self):
        bars = [bar(1, 99.0, 101.0, 98.5, 100.9)]
        state, first = lv.evaluate_setup(long_plan(), bars, None)
        self.assertIsNotNone(first)
        _, second = lv.evaluate_setup(long_plan(), bars, state)
        self.assertIsNone(second)

    def test_second_run_only_sees_new_bars(self):
        first_batch = [bar(1, 99.0, 101.0, 98.5, 99.4)]
        state, event = lv.evaluate_setup(long_plan(), first_batch, None)
        self.assertIsNone(event)
        self.assertEqual(state["status"], lv.ARMED)

        second_batch = first_batch + [bar(2, 99.6, 101.2, 99.4, 100.8)]
        state2, event2 = lv.evaluate_setup(long_plan(), second_batch, state)
        self.assertEqual(state2["status"], lv.FIRED)
        self.assertIsNotNone(event2)
        self.assertEqual(event2["bar_t"], second_batch[-1].t)


class EligibilityTests(unittest.TestCase):
    def test_excludes_bars_that_closed_before_the_plan(self):
        levels = {"as_of": T0 + 2 * BAR, "setups": []}
        bars = [bar(0, 100, 101, 99, 100.5), bar(1, 100, 101, 99, 100.5), bar(2, 100, 101, 99, 100.5)]
        now = T0 + 10 * BAR
        kept = lv.eligible_bars(levels, bars, now_ms=now)
        self.assertEqual([b.t for b in kept], [T0 + 2 * BAR])

    def test_excludes_the_still_forming_bar(self):
        levels = {"as_of": T0}
        bars = [bar(1, 100, 101, 99, 100.5), bar(2, 100, 101, 99, 100.5)]
        now = bars[1].t + 1000  # second bar has not closed yet
        kept = lv.eligible_bars(levels, bars, now_ms=now)
        self.assertEqual([b.t for b in kept], [bars[0].t])


class EvaluateAllTests(unittest.TestCase):
    def test_each_setup_is_independent(self):
        levels = {
            "as_of": T0,
            "setups": [
                long_plan(index=0),
                short_plan(index=1),
                long_plan(index=2, name="third", entry=80.0, arm_level=80.0, stop=75.0, invalid_level=75.0),
            ],
        }
        bars = [
            bar(1, 99.0, 101.0, 98.5, 100.9),   # fires S1 only
            bar(2, 110.5, 111.0, 109.8, 109.4),  # fires S2 only
        ]
        states, events = lv.evaluate_all(levels, bars, None)
        self.assertEqual({event["index"] for event in events}, {0, 1})
        self.assertEqual(states["0"]["status"], lv.FIRED)
        self.assertEqual(states["1"]["status"], lv.FIRED)
        self.assertEqual(states["2"]["status"], lv.WAITING)


@unittest.skipUnless(available(), "no recorded fixtures in tests/fixtures")
class BuildLevelsTests(unittest.TestCase):
    def test_plan_contains_machine_levels(self):
        book = build_book_from_fixtures()
        plan = lv.build_levels(book, display_offset_minutes=330)
        self.assertEqual(len(plan["setups"]), 3)
        for setup in plan["setups"]:
            self.assertIn(setup["arm_direction"], (1, -1))
            self.assertGreater(setup["touch_band"], 0)
            self.assertAlmostEqual(setup["invalid_level"], setup["stop"])
            self.assertEqual(setup["arm_direction"], 1 if setup["side"] == "LONG" else -1)
        json.dumps(plan)  # must be serialisable
        self.assertEqual(plan["day"], lv.plan_day(book.as_of))
        self.assertEqual(plan["display_offset_minutes"], 330)

    def test_plan_day_rolls_at_utc_midnight(self):
        from analytics import DAY_MS, session_start

        midnight = session_start(T0) + DAY_MS  # next UTC midnight after T0
        self.assertNotEqual(lv.plan_day(midnight - 1), lv.plan_day(midnight))


class EventFormattingTests(unittest.TestCase):
    LEVELS = {"symbol": "ETH"}

    def _event(self, **overrides):
        event = {
            "index": 1,
            "name": "Acceptance and retest (short VAL)",
            "side": "SHORT",
            "status": lv.FIRED,
            "bar_t": T0,
            "price": 2353.2,
            "level": 2355.0,
            "stop": 2368.01,
            "t1": 2310.3,
            "t2": 2302.57,
            "rr1": 3.44,
            "rr2": 4.03,
            "tradable": True,
            "message": "5m close 2,353.20 below entry 2,355.00",
        }
        event.update(overrides)
        return event

    def test_fired_message_carries_the_whole_trade(self):
        from watch import format_event

        text = format_event(self.LEVELS, self._event())
        self.assertIn("FIRED | ETH | S2", text)
        self.assertIn("2,355.00", text)
        self.assertIn("3.44R / 4.03R", text)
        self.assertIn("valid - trigger confirmed", text)

    def test_stand_aside_is_called_out(self):
        from watch import format_event

        text = format_event(self.LEVELS, self._event(tradable=False))
        self.assertIn("STAND ASIDE", text)

    def test_void_message_says_plan_dead(self):
        from watch import format_event

        event = self._event(status=lv.VOID, message="5m close 2,300.10 below the invalidation 2,301.62 - plan dead")
        text = format_event(self.LEVELS, event)
        self.assertIn("VOID | ETH", text)
        self.assertIn("plan dead", text)
        self.assertNotIn("3.44R", text)


class NotifyTests(unittest.TestCase):
    def test_unconfigured_send_is_a_noop(self):
        import os
        from unittest.mock import patch

        import notify

        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": "", "TELEGRAM_CHAT_ID": ""}):
            result = notify.send("hello")
        self.assertFalse(result["ok"])
        self.assertIn("not set", result["skipped"])

    def test_split_message_respects_the_limit(self):
        import notify

        text = "\n\n".join("x" * 900 for _ in range(6))
        chunks = notify.split_message(text, limit=2000)
        self.assertGreaterEqual(len(chunks), 3)
        self.assertTrue(all(len(chunk) <= 2000 for chunk in chunks))


class ChangeAlertTests(unittest.TestCase):
    PREVIOUS = {
        "bias": {"label": "Bearish", "score": -4},
        "regime": {"label": "trend-down"},
        "spot": 2318.0,
        "value_area": {"val": 2355.0, "poc": 2400.5, "vah": 2460.0},
        "atr": {"value": 17.4},
    }

    def test_first_run_is_silent(self):
        self.assertEqual(lv.describe_changes(None, self.PREVIOUS), [])

    def test_bias_flip_is_reported(self):
        current = dict(self.PREVIOUS, bias={"label": "Balanced", "score": -1})
        changes = lv.describe_changes(self.PREVIOUS, current)
        self.assertEqual(changes, ["bias Bearish (-4) -> Balanced (-1)"])

    def test_regime_flip_is_reported(self):
        current = dict(self.PREVIOUS, regime={"label": "rotational-balance"})
        changes = lv.describe_changes(self.PREVIOUS, current)
        self.assertEqual(changes, ["regime trend-down -> rotational-balance"])

    def test_both_flips_in_one_alert(self):
        current = dict(
            self.PREVIOUS,
            bias={"label": "Bullish", "score": 3},
            regime={"label": "trend-up"},
        )
        self.assertEqual(len(lv.describe_changes(self.PREVIOUS, current)), 2)

    def test_unchanged_plan_is_silent(self):
        self.assertEqual(lv.describe_changes(self.PREVIOUS, dict(self.PREVIOUS)), [])

    def test_message_carries_the_levels(self):
        message = lv.format_change_message(self.PREVIOUS, ["regime trend-down -> trend-up"])
        self.assertIn("REGIME CHANGE", message)
        self.assertIn("2,355", message)
        self.assertIn("1H ATR", message)


if __name__ == "__main__":
    unittest.main()
