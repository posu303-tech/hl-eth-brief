# ETH perp (Hyperliquid) - 2026-10-26 15:44 UTC+05:30 (10:14 UTC)
spot 2,331.05 | mark 2,331.00 | oracle 2,332.15 | OI 1,107,580.39 ETH (-0.004% vs last run, 24h n/a until the store has a day)
funding +0.00054%/hr (~+4.76%/yr, 20th pct of last 500h) | 24h notional $707.6m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,344.10 / 2,393.22) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 31% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 20th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,355.00 | POC 2,400.50 | VAH 2,460.00 (width 105.00 = 4.50% of spot, 240 bars)
- developing session (43% elapsed): VAL 2,309.00 | POC 2,331.50 | VAH 2,335.00
- session VWAP 2,317.23 (+1s 2,327.98 / -1s 2,306.47) | prior session VWAP 2,338.57
- prior day: PDH 2,370.50 | PDL 2,310.30 | PDC 2,328.80 (PDH intact, PDL swept)
- floor pivots: S3 2,242.37 | S2 2,276.33 | S1 2,302.57 | P 2,336.53 | R1 2,362.77 | R2 2,396.73 | R3 2,422.97
- 1H ATR(14) 17.73 = 0.76% of spot | ATR vs 30d median x1.23
- distance to POC -3.92 ATR | VAH -7.27 ATR | VAL -1.35 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp +0.00074%/hr, BybitPerp +0.00028%/hr, HlPerp +0.00054%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.4 ATR below VAL 2,355.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,355.00 | stop 2,301.43 | T1 2,400.50 | T2 2,460.00
- R:R 0.85 at T1, 1.96 at T2 | risk 53.57
- invalid: 5m close below 2,301.43: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.85R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.4 ATR below VAL 2,355.00; short the retest that fails at it
- entry 2,355.00 | stop 2,368.30 | T1 2,310.30 | T2 2,302.57
- R:R 3.36 at T1, 3.94 at T2 | risk 13.30
- invalid: 1H close back inside value (above 2,355.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.36R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,317.23 or pivot resistance near 2,336.53; sell the rejection, not the touch
- entry 2,336.53 | stop 2,347.17 | T1 2,310.30 | T2 2,302.57
- R:R 2.47 at T1, 3.19 at T2 | risk 10.64
- invalid: 5m close above 2,347.17: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.47R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$10.64-$13.30); funding runs +0.0130%/day ($+0.05/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
