# ETH perp (Hyperliquid) - 2026-11-13 13:16 UTC+05:30 (07:46 UTC)
spot 1,941.75 | mark 1,941.70 | oracle 1,942.78 | OI 740,552.34 ETH (+1.054% vs last run, -2.89% 24h)
funding +0.00006%/hr (~+0.53%/yr, 12th pct of last 500h) | 24h notional $1,909.3m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,025.74 / 2,132.20) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 44% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 12th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -2.9%, price -5.1%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,982.50 | POC 2,124.25 | VAH 2,256.50 (width 274.00 = 14.11% of spot, 240 bars)
- developing session (32% elapsed): VAL 1,901.00 | POC 1,934.25 | VAH 1,972.00
- session VWAP 1,950.20 (+1s 1,981.98 / -1s 1,918.43) | prior session VWAP 2,016.72
- prior day: PDH 2,065.60 | PDL 1,982.70 | PDC 2,018.80 (PDH intact, PDL swept)
- floor pivots: S3 1,896.23 | S2 1,939.47 | S1 1,979.13 | P 2,022.37 | R1 2,062.03 | R2 2,105.27 | R3 2,144.93
- 1H ATR(14) 24.00 = 1.24% of spot | ATR vs 30d median x1.41
- distance to POC -7.60 ATR | VAH -13.11 ATR | VAL -1.70 ATR | closes outside value (last 20): 20%
- cross-venue funding: BinPerp +0.00025%/hr, BybitPerp +0.00027%/hr, HlPerp +0.00007%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.7 ATR below VAL 1,982.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,982.50 | stop 1,929.75 | T1 2,124.25 | T2 2,256.50
- R:R 2.69 at T1, 5.19 at T2 | risk 52.75
- invalid: 5m close below 1,929.75: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.69R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.7 ATR below VAL 1,982.50; short the retest that fails at it
- entry 1,982.50 | stop 2,000.50 | T1 1,939.47 | T2 1,896.23
- R:R 2.39 at T1, 4.79 at T2 | risk 18.00
- invalid: 1H close back inside value (above 1,982.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 2.39R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,950.20 or pivot resistance near 1,950.20; sell the rejection, not the touch
- entry 1,950.20 | stop 1,964.60 | T1 1,918.43 | T2 1,902.20
- R:R 2.21 at T1, 3.33 at T2 | risk 14.40
- invalid: 5m close above 1,964.60: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.21R)

## 4) Risk note
Stops sit 0.60-2.20x the 1H ATR (~$14.40-$52.75); funding runs +0.0014%/day ($+0.01/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
