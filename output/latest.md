# ETH perp (Hyperliquid) - 2026-11-13 21:36 UTC+05:30 (16:06 UTC)
spot 1,925.45 | mark 1,925.50 | oracle 1,926.41 | OI 726,184.16 ETH (-1.940% vs last run, -4.46% 24h)
funding +0.00018%/hr (~+1.53%/yr, 15th pct of last 500h) | 24h notional $1,511.4m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,002.15 / 2,116.29) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 44% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 15th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -4.5%, price -4.4%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,982.50 | POC 2,124.25 | VAH 2,256.50 (width 274.00 = 14.23% of spot, 240 bars)
- developing session (67% elapsed): VAL 1,912.50 | POC 1,934.25 | VAH 1,970.00
- session VWAP 1,950.22 (+1s 1,978.37 / -1s 1,922.07) | prior session VWAP 2,016.72
- prior day: PDH 2,065.60 | PDL 1,982.70 | PDC 2,018.80 (PDH intact, PDL swept)
- floor pivots: S3 1,896.23 | S2 1,939.47 | S1 1,979.13 | P 2,022.37 | R1 2,062.03 | R2 2,105.27 | R3 2,144.93
- 1H ATR(14) 22.63 = 1.18% of spot | ATR vs 30d median x1.21
- distance to POC -8.78 ATR | VAH -14.63 ATR | VAL -2.52 ATR | closes outside value (last 20): 65%
- cross-venue funding: BinPerp +0.00056%/hr, BybitPerp +0.00094%/hr, HlPerp +0.00018%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.5 ATR below VAL 1,982.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,982.50 | stop 1,914.13 | T1 2,124.25 | T2 2,256.50
- R:R 2.07 at T1, 4.01 at T2 | risk 68.37
- invalid: 5m close below 1,914.13: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.07R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.5 ATR below VAL 1,982.50; short the retest that fails at it
- entry 1,982.50 | stop 1,999.47 | T1 1,939.47 | T2 1,896.23
- R:R 2.54 at T1, 5.08 at T2 | risk 16.97
- invalid: 1H close back inside value (above 1,982.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 2.54R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,950.22 or pivot resistance near 1,950.22; sell the rejection, not the touch
- entry 1,950.22 | stop 1,963.80 | T1 1,922.07 | T2 1,904.96
- R:R 2.07 at T1, 3.33 at T2 | risk 13.58
- invalid: 5m close above 1,963.80: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.07R)

## 4) Risk note
Stops sit 0.60-3.02x the 1H ATR (~$13.58-$68.37); funding runs +0.0042%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
