# ETH perp (Hyperliquid) - 2026-11-20 08:27 UTC+05:30 (02:57 UTC)
spot 1,744.25 | mark 1,744.50 | oracle 1,745.42 | OI 607,014.66 ETH (-0.706% vs last run, +1.11% 24h)
funding -0.00005%/hr (~-0.47%/yr, 9th pct of last 500h) | 24h notional $914.4m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,784.09 / 1,871.68) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 26% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 9th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +1.1% with price -1.4%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.25 | VAH 1,976.00 (width 265.50 = 15.22% of spot, 240 bars)
- developing session (12% elapsed): VAL 1,725.50 | POC 1,734.25 | VAH 1,755.00
- session VWAP 1,744.46 (+1s 1,755.93 / -1s 1,732.98) | prior session VWAP 1,778.27
- prior day: PDH 1,816.40 | PDL 1,735.30 | PDC 1,756.60 (PDH intact, PDL swept)
- floor pivots: S3 1,641.37 | S2 1,688.33 | S1 1,722.47 | P 1,769.43 | R1 1,803.57 | R2 1,850.53 | R3 1,884.67
- 1H ATR(14) 21.60 = 1.24% of spot | ATR vs 30d median x1.14
- distance to POC -3.33 ATR | VAH -10.73 ATR | VAL +1.56 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00044%/hr, BybitPerp +0.00012%/hr, HlPerp -0.00005%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,699.70 | T1 1,816.25 | T2 1,976.00
- R:R 9.79 at T1, 24.58 at T2 | risk 10.80
- invalid: 5m close below 1,699.70: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 9.79R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,710.50 while still inside value; sell the confirmation, not the poke
- entry 1,708.34 | stop 1,721.30 | T1 1,688.33 | T2 1,641.37
- R:R 1.54 at T1, 5.17 at T2 | risk 12.96
- invalid: 1H close back above 1,710.50: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 1.54R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,744.46 or pivot resistance near 1,769.43; sell the rejection, not the touch
- entry 1,769.43 | stop 1,782.39 | T1 1,735.30 | T2 1,726.23
- R:R 2.63 at T1, 3.33 at T2 | risk 12.96
- invalid: 5m close above 1,782.39: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.63R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$10.80-$12.96); funding runs -0.0013%/day ($-0.01/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
