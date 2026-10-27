# ETH perp (Hyperliquid) - 2026-10-27 15:51 UTC+05:30 (10:21 UTC)
spot 2,301.05 | mark 2,301.00 | oracle 2,302.30 | OI 1,134,166.54 ETH (+1.458% vs last run, +2.41% 24h)
funding +0.00022%/hr (~+1.97%/yr, 15th pct of last 500h) | 24h notional $763.5m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,326.81 / 2,376.92) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 15th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +2.4% with price -1.2%: new shorts | -1 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,336.00 | POC 2,400.50 | VAH 2,459.00 (width 123.00 = 5.35% of spot, 240 bars)
- developing session (43% elapsed): VAL 2,309.00 | POC 2,327.50 | VAH 2,330.00
- session VWAP 2,316.28 (+1s 2,325.38 / -1s 2,307.18) | prior session VWAP 2,318.19
- prior day: PDH 2,344.40 | PDL 2,292.60 | PDC 2,323.40 (PDH intact, PDL intact)
- floor pivots: S3 2,244.07 | S2 2,268.33 | S1 2,295.87 | P 2,320.13 | R1 2,347.67 | R2 2,371.93 | R3 2,399.47
- 1H ATR(14) 14.62 = 0.64% of spot | ATR vs 30d median x0.86
- distance to POC -6.80 ATR | VAH -10.80 ATR | VAL -2.39 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00043%/hr, BybitPerp +0.00018%/hr, HlPerp +0.00024%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.4 ATR below VAL 2,336.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,336.00 | stop 2,285.29 | T1 2,400.50 | T2 2,459.00
- R:R 1.27 at T1, 2.43 at T2 | risk 50.71
- invalid: 5m close below 2,285.29: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 1.27R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.4 ATR below VAL 2,336.00; short the retest that fails at it
- entry 2,336.00 | stop 2,346.97 | T1 2,295.87 | T2 2,268.33
- R:R 3.66 at T1, 6.17 at T2 | risk 10.97
- invalid: 1H close back inside value (above 2,336.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.66R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,316.28 or pivot support near 2,295.87; buy the hold, not the touch
- entry 2,295.87 | stop 2,287.09 | T1 2,325.11 | T2 2,344.40
- R:R 3.33 at T1, 5.53 at T2 | risk 8.77
- invalid: 5m close below 2,287.09: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$8.77-$10.97); funding runs +0.0054%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
