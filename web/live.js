/* Pure logic for the live layer. No DOM, no fetch - so node can test it.
 *
 * This mirrors levels.py on purpose: the page must agree with the Telegram watch.
 * tests/test_parity.py feeds the same bar sequences to both and fails if they drift.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.LiveMath = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  const WAITING = "WAITING";
  const ARMED = "ARMED";
  const FIRED = "FIRED";
  const VOID = "VOID";

  function parseBars(raw) {
    return (raw || [])
      .map(function (c) {
        return {
          t: Number(c.t),
          T: Number(c.T),
          o: Number(c.o),
          h: Number(c.h),
          l: Number(c.l),
          c: Number(c.c),
          v: Number(c.v),
        };
      })
      .filter(function (b) {
        return isFinite(b.t) && isFinite(b.c) && isFinite(b.h) && isFinite(b.l);
      })
      .sort(function (a, b) {
        return a.t - b.t;
      });
  }

  // Same rule as levels.eligible_bars: only bars that closed after the plan was
  // published, and that are already closed.
  function eligibleBars(levels, bars, now) {
    const asOf = Number(levels.as_of) || 0;
    const stamp = now || Date.now();
    return (bars || []).filter(function (b) {
      return b.T > asOf && b.T <= stamp;
    });
  }

  function sessionVwap(bars) {
    let volume = 0;
    let weighted = 0;
    for (let i = 0; i < bars.length; i++) {
      const typical = (bars[i].h + bars[i].l + bars[i].c) / 3;
      volume += bars[i].v;
      weighted += typical * bars[i].v;
    }
    if (!volume) return null;
    const vwap = weighted / volume;
    let variance = 0;
    for (let i = 0; i < bars.length; i++) {
      const typical = (bars[i].h + bars[i].l + bars[i].c) / 3;
      variance += bars[i].v * Math.pow(typical - vwap, 2);
    }
    return { vwap: vwap, sigma: Math.sqrt(Math.max(variance / volume, 0)), volume: volume, bars: bars.length };
  }

  // Mirrors levels.evaluate_setup exactly: void on a close beyond the stop,
  // arm on a touch of entry +- band, fire on a close beyond entry once armed.
  function evaluateSetup(plan, bars) {
    const direction = Number(plan.arm_direction);
    const arm = Number(plan.arm_level);
    const band = Number(plan.touch_band);
    const invalid = Number(plan.invalid_level);

    let status = WAITING;
    let armedAt = null;
    let lastBarT = 0;
    let event = null;

    const list = bars || [];
    for (let i = 0; i < list.length; i++) {
      const bar = list[i];
      if (bar.t <= lastBarT) continue;
      lastBarT = bar.t;

      if ((direction > 0 && bar.c < invalid) || (direction < 0 && bar.c > invalid)) {
        status = VOID;
        event = { status: VOID, bar_t: bar.t, price: bar.c, level: invalid };
        break;
      }

      if (bar.l <= arm + band && bar.h >= arm - band) {
        status = ARMED;
        armedAt = bar.t;
      }

      const confirmed = direction > 0 ? bar.c > arm : bar.c < arm;
      if (status === ARMED && confirmed) {
        status = FIRED;
        event = { status: FIRED, bar_t: bar.t, price: bar.c, level: arm };
        break;
      }
    }

    return { status: status, armedAt: armedAt, lastBarT: lastBarT, event: event };
  }

  function snapshot(levels, bars, mid, now) {
    const stamp = now || Date.now();
    const eligible = eligibleBars(levels, bars, stamp);
    const vwap = bars && bars.length ? sessionVwap(bars) : null;
    const atr = Number((levels.atr && levels.atr.value) || 0);
    const lastBar = bars && bars.length ? bars[bars.length - 1].c : Number(levels.spot);
    const spot = isFinite(mid) ? mid : lastBar;
    const va = levels.value_area || {};

    function distance(level) {
      const value = Number(level);
      if (!atr || !isFinite(value)) return null;
      return (spot - value) / atr;
    }

    const setups = (levels.setups || []).map(function (plan) {
      const result = evaluateSetup(plan, eligible);
      return {
        index: plan.index,
        side: plan.side,
        entry: plan.entry,
        standAside: !!plan.stand_aside,
        state: result.status,
      };
    });

    return {
      spot: spot,
      vwap: vwap,
      atr: atr,
      setups: setups,
      distVah: distance(va.vah),
      distPoc: distance(va.poc),
      distVal: distance(va.val),
      bars: bars ? bars.length : 0,
      eligible: eligible.length,
      lastBarAt: eligible.length ? eligible[eligible.length - 1].t : null,
      now: stamp,
    };
  }

  return {
    WAITING: WAITING,
    ARMED: ARMED,
    FIRED: FIRED,
    VOID: VOID,
    parseBars: parseBars,
    eligibleBars: eligibleBars,
    sessionVwap: sessionVwap,
    evaluateSetup: evaluateSetup,
    snapshot: snapshot,
  };
});
