"""Cross-language parity: the browser state machine must agree with watch.py.

The page recomputes setup states in JavaScript so it can feel live without a
backend. That is one rule set implemented twice, which is exactly the kind of
thing that silently drifts - so both sides run the same bar sequences here and
the test fails on any disagreement.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from parse import Candle

import levels as lv

BAR = 300_000
T0 = 1_793_000_000_000


def bar(offset: int, o: float, h: float, l: float, c: float) -> Candle:
    start = T0 + offset * BAR
    return Candle(t=start, T=T0 + offset * BAR + BAR - 1, o=o, h=h, l=l, c=c, v=10.0, n=5)


def long_plan(**overrides) -> dict:
    plan = {
        "index": 0,
        "name": "parity long",
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
        name="parity short",
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


CASES = [
    ("never touches the level", long_plan(), [
        bar(1, 96.5, 97.5, 96.0, 96.8),
        bar(2, 105.0, 106.0, 104.0, 105.5),
    ]),
    ("touch arms but does not confirm", long_plan(), [
        bar(1, 99.0, 101.0, 98.5, 99.4),
    ]),
    ("arm then confirm", long_plan(), [
        bar(1, 99.0, 101.0, 98.5, 99.4),
        bar(2, 99.6, 101.2, 99.4, 100.8),
    ]),
    ("same-bar reclaim", long_plan(), [
        bar(1, 98.0, 101.0, 97.5, 100.9),
    ]),
    ("void on a close through the stop", long_plan(), [
        bar(1, 96.0, 96.5, 94.0, 94.5),
    ]),
    ("void beats a later reclaim", long_plan(), [
        bar(1, 96.0, 96.5, 94.0, 94.5),
        bar(2, 94.0, 101.0, 94.0, 100.5),
    ]),
    ("short arm then confirm", short_plan(), [
        bar(1, 110.5, 111.0, 109.8, 110.2),
        bar(2, 110.0, 110.2, 109.0, 109.4),
    ]),
    ("short rejects a close the wrong way", short_plan(), [
        bar(1, 110.5, 111.0, 109.8, 110.2),
        bar(2, 110.0, 111.5, 109.9, 111.2),
    ]),
    ("short voids above the stop", short_plan(), [
        bar(1, 114.0, 116.0, 113.5, 115.5),
    ]),
    ("gap through a wide band still arms and fires", long_plan(touch_band=5.0), [
        bar(1, 94.0, 96.0, 93.0, 95.5),
        bar(2, 96.0, 106.0, 95.8, 105.0),
    ]),
]


def serialise(candle: Candle) -> dict:
    return {
        "t": candle.t,
        "T": candle.T,
        "o": candle.o,
        "h": candle.h,
        "l": candle.l,
        "c": candle.c,
        "v": candle.v,
    }


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class JavaScriptParityTests(unittest.TestCase):
    def test_js_state_machine_matches_python(self):
        payload = []
        expected = []
        for name, plan, bars in CASES:
            state, event = lv.evaluate_setup(plan, bars, None)
            payload.append(
                {"name": name, "plan": plan, "bars": [serialise(candle) for candle in bars]}
            )
            expected.append({"status": state["status"], "event": bool(event)})

        with tempfile.TemporaryDirectory() as tmp:
            case_file = Path(tmp) / "cases.json"
            case_file.write_text(json.dumps(payload), encoding="utf-8")
            result = subprocess.run(
                [shutil.which("node"), "tests/parity_runner.js", str(case_file)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=60,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        got = json.loads(result.stdout)
        self.assertEqual(len(got), len(expected))
        for (name, _, _), js, py in zip(CASES, got, expected):
            self.assertEqual(js, py, f"JS and Python disagree on: {name}")

    def test_js_syntax_is_valid(self):
        for name in ("live.js", "app.js"):
            path = ROOT / "web" / name
            result = subprocess.run(
                [shutil.which("node"), "--check", str(path)],
                capture_output=True,
                text=True,
                timeout=60,
            )
            self.assertEqual(result.returncode, 0, f"{name}: {result.stderr}")


if __name__ == "__main__":
    unittest.main()
