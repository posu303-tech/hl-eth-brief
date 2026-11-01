# ETH perp (Hyperliquid) - 2026-11-01 06:25 UTC+05:30 (00:55 UTC)
spot 2,261.25 | mark 2,261.30 | oracle 2,262.40 | OI 980,719.77 ETH (+0.210% vs last run, -0.83% 24h)
funding +0.00098%/hr (~+8.55%/yr, 37th pct of last 500h) | 24h notional $220.3m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,256.38 / 2,312.87) | 0 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 64% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 37th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -0.8%, price +0.6%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,262.00 | POC 2,326.50 | VAH 2,413.00 (width 151.00 = 6.68% of spot, 240 bars)
- developing session (4% elapsed): VAL 2,253.00 | POC 2,254.50 | VAH 2,258.00
- session VWAP 2,256.34 (+1s 2,258.59 / -1s 2,254.09) | prior session VWAP 2,247.80
- prior day: PDH 2,266.10 | PDL 2,235.00 | PDC 2,254.80 (PDH intact, PDL intact)
- floor pivots: S3 2,206.73 | S2 2,220.87 | S1 2,237.83 | P 2,251.97 | R1 2,268.93 | R2 2,283.07 | R3 2,300.03
- 1H ATR(14) 9.33 = 0.41% of spot | ATR vs 30d median x0.67
- distance to POC -6.99 ATR | VAH -16.26 ATR | VAL -0.08 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00013%/hr, BybitPerp -0.00088%/hr, HlPerp +0.00098%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.1 ATR below VAL 2,262.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,262.00 | stop 2,230.33 | T1 2,326.50 | T2 2,413.00
- R:R 2.04 at T1, 4.77 at T2 | risk 31.67
- invalid: 5m close below 2,230.33: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.04R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.1 ATR below VAL 2,262.00; short the retest that fails at it
- entry 2,262.00 | stop 2,269.00 | T1 2,237.83 | T2 2,220.87
- R:R 3.45 at T1, 5.88 at T2 | risk 7.00
- invalid: 1H close back inside value (above 2,262.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.45R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,256.34 or pivot support near 2,256.34; buy the hold, not the touch
- entry 2,256.34 | stop 2,250.74 | T1 2,266.10 | T2 2,275.00
- R:R 1.74 at T1, 3.33 at T2 | risk 5.60
- invalid: 5m close below 2,250.74: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.74R)

## 4) Risk note
Stops sit 0.60-3.39x the 1H ATR (~$5.60-$31.67); funding runs +0.0234%/day ($+0.10/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
