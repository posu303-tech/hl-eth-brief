/* Live strip: polls Hyperliquid straight from the browser (CORS is open on /info),
 * recomputes session VWAP and each setup's state, and repaints. No backend, no secrets.
 * If a fetch fails it keeps the last numbers and says so rather than showing a lie.
 */
(function () {
  "use strict";

  const POLL_MS = 20000;
  const STALE_MS = 90000;

  function money(value) {
    const n = Number(value);
    if (!isFinite(n)) return "--";
    return n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function atrText(value) {
    if (value === null || value === undefined || !isFinite(value)) return "--";
    return (value >= 0 ? "+" : "") + value.toFixed(2) + " ATR";
  }

  function clock(ms) {
    if (!ms) return "--";
    return new Date(ms).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
  }

  function setText(id, text) {
    const el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  async function post(body) {
    const response = await fetch("https://api.hyperliquid.xyz/info", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    if (!response.ok) throw new Error("hyperliquid HTTP " + response.status);
    return response.json();
  }

  function midOf(book) {
    try {
      const bid = Number(book.levels[0][0].px);
      const ask = Number(book.levels[1][0].px);
      if (isFinite(bid) && isFinite(ask)) return (bid + ask) / 2;
    } catch (error) {
      /* fall through to the candle close */
    }
    return undefined;
  }

  function renderChips(levels, snapshot) {
    const host = document.getElementById("live-chips");
    if (!host) return;
    const byIndex = {};
    (snapshot ? snapshot.setups : []).forEach(function (setup) {
      byIndex[String(setup.index)] = setup;
    });

    host.innerHTML = "";
    (levels.setups || []).forEach(function (plan) {
      const live = byIndex[String(plan.index)];
      const chip = document.createElement("span");
      const state = live ? live.state : "WAITING";
      chip.className = "chip s-" + state.toLowerCase();
      const label = state === "WAITING" ? "WAITING" : state;
      chip.textContent = "S" + (plan.index + 1) + " " + plan.side + " \u00b7 " + label;
      chip.title = plan.name + " \u2014 entry " + money(plan.entry);
      host.appendChild(chip);
    });
  }

  function render(levels, snapshot, mode) {
    const dot = document.getElementById("live-dot");
    if (dot) dot.className = "dot " + mode;

    if (!snapshot) {
      setText("live-meta", mode === "off" ? "offline \u2014 retrying" : "connecting\u2026");
      renderChips(levels, null);
      return;
    }

    setText("live-spot", money(snapshot.spot));
    setText("live-vwap", snapshot.vwap ? money(snapshot.vwap.vwap) : "--");
    setText("live-vah", atrText(snapshot.distVah));
    setText("live-poc", atrText(snapshot.distPoc));
    setText("live-val", atrText(snapshot.distVal));
    setText(
      "live-meta",
      (mode === "off" ? "offline \u2014 last " : "updated ") +
        clock(snapshot.now) +
        " \u00b7 " +
        snapshot.eligible +
        " bars"
    );
    renderChips(levels, snapshot);
  }

  async function tick(context) {
    const symbol = context.levels.symbol;
    const now = Date.now();
    try {
      const [book, raw] = await Promise.all([
        post({ type: "l2Book", coin: symbol }),
        post({
          type: "candleSnapshot",
          req: { coin: symbol, interval: "5m", startTime: context.sessionStart, endTime: now },
        }),
      ]);
      const bars = window.LiveMath.parseBars(raw);
      const snapshot = window.LiveMath.snapshot(context.levels, bars, midOf(book), now);
      context.last = snapshot;
      render(context.levels, snapshot, "live");
    } catch (error) {
      render(context.levels, context.last, "off");
    }
  }

  async function boot() {
    const host = document.getElementById("live");
    if (!host || !window.LiveMath) return;

    let levels;
    try {
      const response = await fetch("./levels.json", { cache: "no-store" });
      levels = await response.json();
    } catch (error) {
      render({ setups: [] }, null, "off");
      return;
    }

    const context = {
      levels: levels,
      sessionStart: Date.parse(levels.day + "T00:00:00Z"),
      last: null,
    };

    render(levels, null, "wait");
    tick(context);
    setInterval(function () {
      if (!document.hidden) tick(context);
    }, POLL_MS);
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden) tick(context);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
