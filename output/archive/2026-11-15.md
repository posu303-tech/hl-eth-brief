# ETH perp (Hyperliquid) - 2026-11-15 22:26 UTC+05:30 (16:56 UTC)
spot 1,808.05 | mark 1,807.80 | oracle 1,808.80 | OI 587,958.21 ETH (-2.937% vs last run, -14.51% 24h)
funding -0.00075%/hr (~-6.58%/yr, 4th pct of last 500h) | 24h notional $1,999.1m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,856.94 / 2,014.58) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 19% of prior range | -1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 4th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -14.5%, price -0.9%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,829.50 | POC 2,124.25 | VAH 2,166.00 (width 336.50 = 18.61% of spot, 240 bars)
- developing session (71% elapsed): VAL 1,773.00 | POC 1,806.25 | VAH 1,837.50
- session VWAP 1,791.43 (+1s 1,826.15 / -1s 1,756.71) | prior session VWAP 1,830.31
- prior day: PDH 1,936.00 | PDL 1,727.80 | PDC 1,768.00 (PDH intact, PDL swept)
- floor pivots: S3 1,477.00 | S2 1,602.40 | S1 1,685.20 | P 1,810.60 | R1 1,893.40 | R2 2,018.80 | R3 2,101.60
- 1H ATR(14) 27.11 = 1.50% of spot | ATR vs 30d median x0.96
- distance to POC -11.66 ATR | VAH -13.20 ATR | VAL -0.79 ATR | closes outside value (last 20): 85%
- cross-venue funding: BinPerp -0.00060%/hr, BybitPerp -0.00043%/hr, HlPerp -0.00075%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.8 ATR below VAL 1,829.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,829.50 | stop 1,714.24 | T1 2,124.25 | T2 2,166.00
- R:R 2.56 at T1, 2.92 at T2 | risk 115.26
- invalid: 5m close below 1,714.24: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.56R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.8 ATR below VAL 1,829.50; short the retest that fails at it
- entry 1,829.50 | stop 1,849.84 | T1 1,727.80 | T2 1,685.20
- R:R 5.00 at T1, 7.10 at T2 | risk 20.34
- invalid: 1H close back inside value (above 1,829.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 5.00R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,791.43 or pivot support near 1,791.43; buy the hold, not the touch
- entry 1,791.43 | stop 1,775.16 | T1 1,826.15 | T2 1,845.66
- R:R 2.13 at T1, 3.33 at T2 | risk 16.27
- invalid: 5m close below 1,775.16: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.13R)

## 4) Risk note
Stops sit 0.60-4.25x the 1H ATR (~$16.27-$115.26); funding runs -0.0180%/day ($-0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
