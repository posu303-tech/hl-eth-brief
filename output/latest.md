# ETH perp (Hyperliquid) - 2026-11-26 03:51 UTC+05:30 (22:21 UTC)
spot 1,682.35 | mark 1,682.40 | oracle 1,683.23 | OI 640,835.11 ETH (+4.452% vs last run, +4.45% 24h)
funding +0.00119%/hr (~+10.41%/yr, 48th pct of last 500h) | 24h notional $1,037.1m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,676.29 / 1,732.21) | 0 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 28% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 48th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +4.5% with price -0.1%: new shorts | -1 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,682.50 | POC 1,816.25 | VAH 1,833.50 (width 151.00 = 8.98% of spot, 240 bars)
- developing session (93% elapsed): VAL 1,628.50 | POC 1,644.75 | VAH 1,665.50
- session VWAP 1,651.43 (+1s 1,669.58 / -1s 1,633.28) | prior session VWAP 1,688.91
- prior day: PDH 1,720.90 | PDL 1,663.20 | PDC 1,679.30 (PDH intact, PDL swept)
- floor pivots: S3 1,597.00 | S2 1,630.10 | S1 1,654.70 | P 1,687.80 | R1 1,712.40 | R2 1,745.50 | R3 1,770.10
- 1H ATR(14) 20.94 = 1.24% of spot | ATR vs 30d median x1.21
- distance to POC -6.39 ATR | VAH -7.22 ATR | VAL -0.01 ATR | closes outside value (last 20): 85%
- cross-venue funding: BinPerp +0.00059%/hr, BybitPerp +0.00121%/hr, HlPerp +0.00123%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.0 ATR below VAL 1,682.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,682.50 | stop 1,652.73 | T1 1,816.25 | T2 1,833.50
- R:R 4.49 at T1, 5.07 at T2 | risk 29.77
- invalid: 5m close below 1,652.73: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 4.49R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.0 ATR below VAL 1,682.50; short the retest that fails at it
- entry 1,682.50 | stop 1,698.21 | T1 1,663.20 | T2 1,654.70
- R:R 1.23 at T1, 1.77 at T2 | risk 15.71
- invalid: 1H close back inside value (above 1,682.50) voids the acceptance
- verdict: STAND ASIDE - T1 pays 1.23R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,651.43 or pivot resistance near 1,687.80; sell the rejection, not the touch
- entry 1,687.80 | stop 1,700.36 | T1 1,663.20 | T2 1,654.70
- R:R 1.96 at T1, 2.63 at T2 | risk 12.56
- invalid: 5m close above 1,700.36: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.96R)

## 4) Risk note
Stops sit 0.60-1.42x the 1H ATR (~$12.56-$29.77); funding runs +0.0285%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
