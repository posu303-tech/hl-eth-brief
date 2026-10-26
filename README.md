# HL-ETH-Brief

A keyless, on-demand intraday brief for Hyperliquid perps (ETH by default), with an
hourly GitHub Action, a 5-minute trigger watch and a mobile-friendly static site.

Everything is derived from public `POST https://api.hyperliquid.xyz/info` calls:
no API key, no wallet, no account state, no signed requests.

The brief has exactly four sections: HTF bias, intraday regime and value position,
three conditional setups, one risk line. **No price predictions.**

## Quick start

```powershell
python eth_brief.py                 # live brief -> output/latest.md + latest.json
python eth_brief.py --selfcheck     # fetch + validate every field, then exit
python eth_brief.py --json          # the published plan (levels.json contract)
python eth_brief.py --book-json     # the full computed book instead
python eth_brief.py --symbol SOL    # any listed perp works
python eth_brief.py --as-of 2026-10-26T12:00:00Z   # reproducible snapshot
python eth_brief.py --offline tests\fixtures --no-save   # replay recorded payloads
python watch.py --dry-run           # evaluate triggers, write nothing
python make_site.py                 # build site/ from output/
```

`output/latest.md` is the brief, `output/latest.json` is the plan the watch reads,
`output/archive/YYYYMMDD.md` keeps one snapshot per UTC day.

## What gets computed

| Quantity | Method |
|---|---|
| 10-session value area | 1H bars from the last 10 **completed** UTC sessions; each bar's volume spread uniformly across its high-low into $1 buckets (0.05% of price, rounded to 1/2/5); POC = heaviest bucket; VA expands from the POC toward the heavier neighbour until 70% of volume is captured |
| Developing value | same profile over the current session's 5m bars, reported separately |
| Session VWAP | current UTC session, `sum(typical*volume)/sum(volume)`, with volume-weighted +-1 sigma bands |
| Prior day H/L/C | last completed UTC session; flags whether today already swept PDH or PDL |
| Floor pivots | classic floor-trader on prior H/L/C: `P=(H+L+C)/3`, `R1=2P-L`, `S1=2P-H`, `R2=P+(H-L)`, `S2=P-(H-L)`, `R3=H+2(P-L)`, `S3=L-2(H-P)` |
| 1H ATR | Wilder ATR(14) on completed bars, seeded with the SMA of the first 14 true ranges |
| HTF bias | six auditable +/-1 reads: EMA50/200 stack, value position, prior-day close location, 20-bar swing structure, funding percentile (contrarian), OI 24h vs price 24h. Label needs abs(score) >= 3 |
| Regime | ordered rules: failed-auction, then trend (>=55% of last 20 closes outside value and EMA50 slope >= 0.5 ATR), then breakout-attempt, else rotational-balance |
| Setups | value rejection, acceptance-and-retest, VWAP/pivot confluence. Every entry, stop, T1 and T2 is a real level; a setup whose T1 pays under 1.5R prints **STAND ASIDE** |

## Deployment (GitHub Actions + Pages)

Two workflows, deliberately split:

| | `brief.yml` | `watch.yml` |
|---|---|---|
| cron | `5 * * * *` (hourly) | `*/5 * * * *` |
| reads | all payloads | the published plan + new 5m closes |
| writes | `output/`, `data/oi_snapshots.jsonl`, Pages | `data/watch_state.json`, only on a transition |

The split matters: the brief commits hourly, the watch commits only when a setup
changes state. Without it you get 288 commits a day.

One-time setup:

1. Push this folder to a **public** repo.
2. Settings -> Pages -> Source: **GitHub Actions**.
3. Optional: Settings -> Secrets -> `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
   Without them everything still runs; alerts are just skipped.
4. Run the *hourly brief* workflow once manually to publish and seed `output/latest.json`.

Then `https://<user>.github.io/<repo>/` is the brief, `/archive.html` is the history,
`/levels.json` is the machine-readable plan.

### Alert semantics

- **FIRED** - a 5m close crossed a setup entry *after* the level was actually reached
- **VOID** - a 5m close crossed the invalidation; the plan is dead for the day
- one message per transition; both are terminal until the UTC day rolls over
- the watch ignores bars that closed before the plan was published, so a fresh plan
  is never graded against history that predates it
- a plan older than 6h is refused rather than traded

### Cadence reality

Public repo: Actions minutes and Pages are free (~7k min/month at this cadence).
GitHub's scheduler is best effort - a 5-minute cron typically lands 1-10 minutes late
and is occasionally dropped under load. If that proves too slow for entries, the next
step is a Cloudflare Worker cron, not a bigger backend.

### Day boundary

Sessions are UTC (VA, PDH/PDL, pivots). Timestamps render in `--display-offset`
(default `+05:30`). 00:00 UTC = 05:30 IST, so the "prior day" flips mid-morning IST
while the levels themselves stay on exchange-standard UTC sessions.

## Files

```
hl_api.py     POST /info with retry/backoff + RawVault (payload retention)
parse.py      dataclasses, numeric coercion, MissingFieldError with raw JSON
analytics.py  value area, VWAP, pivots, ATR, bias, regime, setups, compute()
brief.py      the four-section renderer + compact Telegram plan message
levels.py     levels.json contract + trigger state machine
watch.py      5-minute evaluator (fetch, evaluate, alert, persist state)
make_site.py  static site builder
mdmini.py     minimal Markdown -> HTML for this project's own output
notify.py     Telegram sender (silent no-op when unconfigured)
eth_brief.py  CLI, OI snapshot store, selfcheck
tests/        unittest suite + recorded payload fixtures
```

## Failure behaviour

A missing, null or non-numeric field raises `MissingFieldError`, which prints the
offending record plus the full raw JSON to stderr, writes `output/raw_<ts>.json`, and
exits 2. Nothing is silently defaulted to zero.

`watch.py` exit codes: `0` ok, `2` no plan, `3` fetch failure, `4` plan too old.
The workflow treats 2 and 4 as "wait for the next brief", not as failures.

## API quirks worth remembering

- Candles must be `{"type":"candleSnapshot","req":{...}}`. The flat
  `{"type":"candles",...}` body returns HTTP 422.
- Prices arrive as **strings** on `metaAndAssetCtxs` and in candles; `num()` handles both.
- Hyperliquid perp funding is **hourly**, not 8-hourly. Annualising as x3x365
  overstates it 8x.
- `fundingHistory` returns at most 500 hourly points (~21 days).
- There is **no historical OI endpoint**. The 24h OI delta reads `n/a` until
  `data/oi_snapshots.jsonl` holds a snapshot at least 12h old.
- `access-control-allow-origin: *` on `/info`, so a browser can call it directly
  (that is what makes a backend unnecessary).

## Tests

```powershell
python -m unittest discover -s tests -v
```

99 tests: coercion, sort/dedupe, missing-field raw dump, hand-computed value area /
VWAP / pivots / Wilder ATR / EMA, bias thresholds, all four regime branches, R:R maths,
the trigger state machine (arming, confirmation, invalidation, idempotency, pre-plan
bars, still-forming bars), the mini renderer, and an end-to-end replay of a recorded
live payload through to the built site.

## Non-goals

No forecasting, no order placement, no position sizing against your balance (the risk
note is expressed in ATR units and funding cost per $10k notional).
