# ETH perp (Hyperliquid) - 2026-11-15 14:38 UTC+05:30 (09:08 UTC)
spot 1,830.45 | mark 1,830.30 | oracle 1,831.20 | OI 605,749.77 ETH (-5.723% vs last run, -13.40% 24h)
funding +0.00111%/hr (~+9.68%/yr, 38th pct of last 500h) | 24h notional $2,309.7m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,868.33 / 2,028.54) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 19% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 38th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -13.4%, price -3.8%: no edge | 0 |

## 2) Intraday regime - trend-down, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,829.50 | POC 2,124.25 | VAH 2,166.00 (width 336.50 = 18.38% of spot, 240 bars)
- developing session (38% elapsed): VAL 1,758.50 | POC 1,790.25 | VAH 1,831.50
- session VWAP 1,779.68 (+1s 1,812.80 / -1s 1,746.55) | prior session VWAP 1,830.31
- prior day: PDH 1,936.00 | PDL 1,727.80 | PDC 1,768.00 (PDH intact, PDL swept)
- floor pivots: S3 1,477.00 | S2 1,602.40 | S1 1,685.20 | P 1,810.60 | R1 1,893.40 | R2 2,018.80 | R3 2,101.60
- 1H ATR(14) 30.09 = 1.64% of spot | ATR vs 30d median x1.28
- distance to POC -9.76 ATR | VAH -11.15 ATR | VAL +0.03 ATR | closes outside value (last 20): 75%
- cross-venue funding: BinPerp +0.00029%/hr, BybitPerp -0.00067%/hr, HlPerp +0.00117%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,829.50; enter on the reclaim
- entry 1,829.50 | stop 1,814.45 | T1 2,124.25 | T2 2,166.00
- R:R 19.59 at T1, 22.37 at T2 | risk 15.05
- invalid: 5m close below 1,814.45: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 19.59R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,829.50 while still inside value; sell the confirmation, not the poke
- entry 1,826.49 | stop 1,844.55 | T1 1,727.80 | T2 1,685.20
- R:R 5.47 at T1, 7.83 at T2 | risk 18.05
- invalid: 1H close back above 1,829.50: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 5.47R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,779.68 or pivot resistance near 1,893.40; sell the rejection, not the touch
- entry 1,893.40 | stop 1,911.45 | T1 1,833.22 | T2 1,746.55
- R:R 3.33 at T1, 8.13 at T2 | risk 18.05
- invalid: 5m close above 1,911.45: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$15.05-$18.05); funding runs +0.0265%/day ($+0.11/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
