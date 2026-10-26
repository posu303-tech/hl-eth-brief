# ETH perp (Hyperliquid) - 2026-10-26 17:44 UTC+05:30 (12:14 UTC)
spot 2,331.35 | mark 2,331.40 | oracle 2,332.40 | OI 1,105,990.51 ETH (-0.136% vs last run, 24h n/a until the store has a day)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $683.0m

## 1) HTF bias - BEARISH (-5 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,343.04 / 2,391.97) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 31% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,355.00 | POC 2,400.50 | VAH 2,460.00 (width 105.00 = 4.50% of spot, 240 bars)
- developing session (51% elapsed): VAL 2,310.00 | POC 2,329.50 | VAH 2,335.00
- session VWAP 2,318.13 (+1s 2,328.99 / -1s 2,307.28) | prior session VWAP 2,338.57
- prior day: PDH 2,370.50 | PDL 2,310.30 | PDC 2,328.80 (PDH intact, PDL swept)
- floor pivots: S3 2,242.37 | S2 2,276.33 | S1 2,302.57 | P 2,336.53 | R1 2,362.77 | R2 2,396.73 | R3 2,422.97
- 1H ATR(14) 16.80 = 0.72% of spot | ATR vs 30d median x1.16
- distance to POC -4.12 ATR | VAH -7.66 ATR | VAL -1.41 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp +0.00088%/hr, BybitPerp +0.00035%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.4 ATR below VAL 2,355.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,355.00 | stop 2,301.90 | T1 2,400.50 | T2 2,460.00
- R:R 0.86 at T1, 1.98 at T2 | risk 53.10
- invalid: 5m close below 2,301.90: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.86R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.4 ATR below VAL 2,355.00; short the retest that fails at it
- entry 2,355.00 | stop 2,367.60 | T1 2,310.30 | T2 2,302.57
- R:R 3.55 at T1, 4.16 at T2 | risk 12.60
- invalid: 1H close back inside value (above 2,355.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.55R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,318.13 or pivot resistance near 2,336.53; sell the rejection, not the touch
- entry 2,336.53 | stop 2,346.61 | T1 2,310.30 | T2 2,302.94
- R:R 2.60 at T1, 3.33 at T2 | risk 10.08
- invalid: 5m close above 2,346.61: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.60R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$10.08-$12.60); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
