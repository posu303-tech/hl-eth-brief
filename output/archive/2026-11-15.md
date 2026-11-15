# ETH perp (Hyperliquid) - 2026-11-16 03:07 UTC+05:30 (21:37 UTC)
spot 1,816.05 | mark 1,815.80 | oracle 1,816.70 | OI 587,658.40 ETH (-0.051% vs last run, -11.66% 24h)
funding +0.00026%/hr (~+2.28%/yr, 14th pct of last 500h) | 24h notional $1,573.2m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,849.95 / 2,005.00) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 19% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 14th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -11.7%, price +1.7%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,829.50 | POC 2,124.25 | VAH 2,166.00 (width 336.50 = 18.53% of spot, 240 bars)
- developing session (90% elapsed): VAL 1,778.00 | POC 1,822.25 | VAH 1,837.50
- session VWAP 1,794.11 (+1s 1,828.16 / -1s 1,760.05) | prior session VWAP 1,830.31
- prior day: PDH 1,936.00 | PDL 1,727.80 | PDC 1,768.00 (PDH intact, PDL swept)
- floor pivots: S3 1,477.00 | S2 1,602.40 | S1 1,685.20 | P 1,810.60 | R1 1,893.40 | R2 2,018.80 | R3 2,101.60
- 1H ATR(14) 23.90 = 1.32% of spot | ATR vs 30d median x0.84
- distance to POC -12.89 ATR | VAH -14.64 ATR | VAL -0.56 ATR | closes outside value (last 20): 85%
- cross-venue funding: BinPerp -0.00000%/hr, BybitPerp +0.00017%/hr, HlPerp +0.00024%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.6 ATR below VAL 1,829.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,829.50 | stop 1,715.85 | T1 2,124.25 | T2 2,166.00
- R:R 2.59 at T1, 2.96 at T2 | risk 113.65
- invalid: 5m close below 1,715.85: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.59R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.6 ATR below VAL 1,829.50; short the retest that fails at it
- entry 1,829.50 | stop 1,847.43 | T1 1,727.80 | T2 1,685.20
- R:R 5.67 at T1, 8.05 at T2 | risk 17.93
- invalid: 1H close back inside value (above 1,829.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 5.67R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,794.11 or pivot support near 1,810.60; buy the hold, not the touch
- entry 1,810.60 | stop 1,796.26 | T1 1,828.16 | T2 1,858.40
- R:R 1.22 at T1, 3.33 at T2 | risk 14.34
- invalid: 5m close below 1,796.26: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.22R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-4.76x the 1H ATR (~$17.93-$113.65); funding runs +0.0062%/day ($+0.03/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
