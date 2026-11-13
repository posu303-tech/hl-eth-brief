# ETH perp (Hyperliquid) - 2026-11-13 05:34 UTC+05:30 (00:04 UTC)
spot 2,018.85 | mark 2,019.00 | oracle 2,019.80 | OI 732,827.09 ETH (-3.584% vs last run, -4.63% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,223.6m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,047.92 / 2,144.74) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 44% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -4.6%, price -1.8%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,983.00 | POC 2,124.50 | VAH 2,257.00 (width 274.00 = 13.57% of spot, 240 bars)
- session VWAP 2,019.10 (+1s 2,019.10 / -1s 2,019.10) | prior session VWAP 2,016.72
- prior day: PDH 2,065.60 | PDL 1,982.70 | PDC 2,018.80 (PDH intact, PDL intact)
- floor pivots: S3 1,896.23 | S2 1,939.47 | S1 1,979.13 | P 2,022.37 | R1 2,062.03 | R2 2,105.27 | R3 2,144.93
- 1H ATR(14) 15.99 = 0.79% of spot | ATR vs 30d median x0.94
- distance to POC -6.61 ATR | VAH -14.89 ATR | VAL +2.24 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00121%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,983.00; enter on the reclaim
- entry 1,983.00 | stop 1,975.01 | T1 2,124.50 | T2 2,257.00
- R:R 17.70 at T1, 34.27 at T2 | risk 7.99
- invalid: 5m close below 1,975.01: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 17.70R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,983.00 while still inside value; sell the confirmation, not the poke
- entry 1,981.40 | stop 1,990.99 | T1 1,939.47 | T2 1,896.23
- R:R 4.37 at T1, 8.88 at T2 | risk 9.59
- invalid: 1H close back above 1,983.00: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 4.37R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,019.10 or pivot resistance near 2,022.37; sell the rejection, not the touch
- entry 2,022.37 | stop 2,031.96 | T1 1,990.39 | T2 1,983.00
- R:R 3.33 at T1, 4.10 at T2 | risk 9.59
- invalid: 5m close above 2,031.96: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.99-$9.59); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
