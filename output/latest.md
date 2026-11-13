# ETH perp (Hyperliquid) - 2026-11-14 03:58 UTC+05:30 (22:28 UTC)
spot 1,927.85 | mark 1,927.90 | oracle 1,928.86 | OI 716,808.24 ETH (-1.291% vs last run, -2.19% 24h)
funding -0.00040%/hr (~-3.54%/yr, 6th pct of last 500h) | 24h notional $1,386.5m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,988.78 / 2,105.99) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 44% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 6th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -2.2%, price -4.3%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,982.50 | POC 2,124.25 | VAH 2,256.50 (width 274.00 = 14.21% of spot, 240 bars)
- developing session (94% elapsed): VAL 1,913.00 | POC 1,934.25 | VAH 1,964.00
- session VWAP 1,948.13 (+1s 1,975.07 / -1s 1,921.19) | prior session VWAP 2,016.72
- prior day: PDH 2,065.60 | PDL 1,982.70 | PDC 2,018.80 (PDH intact, PDL swept)
- floor pivots: S3 1,896.23 | S2 1,939.47 | S1 1,979.13 | P 2,022.37 | R1 2,062.03 | R2 2,105.27 | R3 2,144.93
- 1H ATR(14) 21.06 = 1.09% of spot | ATR vs 30d median x1.00
- distance to POC -9.33 ATR | VAH -15.61 ATR | VAL -2.60 ATR | closes outside value (last 20): 95%
- cross-venue funding: BinPerp +0.00024%/hr, BybitPerp +0.00055%/hr, HlPerp -0.00043%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.6 ATR below VAL 1,982.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,982.50 | stop 1,917.32 | T1 2,124.25 | T2 2,256.50
- R:R 2.17 at T1, 4.20 at T2 | risk 65.18
- invalid: 5m close below 1,917.32: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.17R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.6 ATR below VAL 1,982.50; short the retest that fails at it
- entry 1,982.50 | stop 1,998.29 | T1 1,939.47 | T2 1,896.23
- R:R 2.72 at T1, 5.46 at T2 | risk 15.79
- invalid: 1H close back inside value (above 1,982.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 2.72R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,948.13 or pivot resistance near 1,948.13; sell the rejection, not the touch
- entry 1,948.13 | stop 1,960.77 | T1 1,921.19 | T2 1,906.02
- R:R 2.13 at T1, 3.33 at T2 | risk 12.63
- invalid: 5m close above 1,960.77: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.13R)

## 4) Risk note
Stops sit 0.60-3.10x the 1H ATR (~$12.63-$65.18); funding runs -0.0097%/day ($-0.04/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
