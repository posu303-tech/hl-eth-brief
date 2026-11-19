# ETH perp (Hyperliquid) - 2026-11-19 18:16 UTC+05:30 (12:46 UTC)
spot 1,798.55 | mark 1,798.20 | oracle 1,799.05 | OI 599,302.36 ETH (-0.177% vs last run, -1.71% 24h)
funding +0.00038%/hr (~+3.33%/yr, 16th pct of last 500h) | 24h notional $645.3m

## 1) HTF bias - BALANCED (+2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,796.46 / 1,886.97) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 47% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 16th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.7%, price +0.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.75 | VAH 2,018.00 (width 307.50 = 17.10% of spot, 240 bars)
- developing session (53% elapsed): VAL 1,782.50 | POC 1,804.75 | VAH 1,811.50
- session VWAP 1,792.16 (+1s 1,804.74 / -1s 1,779.58) | prior session VWAP 1,778.32
- prior day: PDH 1,825.80 | PDL 1,732.60 | PDC 1,776.50 (PDH intact, PDL intact)
- floor pivots: S3 1,637.60 | S2 1,685.10 | S1 1,730.80 | P 1,778.30 | R1 1,824.00 | R2 1,871.50 | R3 1,917.20
- 1H ATR(14) 15.39 = 0.86% of spot | ATR vs 30d median x0.87
- distance to POC -1.18 ATR | VAH -14.26 ATR | VAL +5.72 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00103%/hr, BybitPerp +0.00044%/hr, HlPerp +0.00037%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,702.80 | T1 1,816.75 | T2 2,018.00
- R:R 13.81 at T1, 39.96 at T2 | risk 7.70
- invalid: 5m close below 1,702.80: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 13.81R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,018.00 while still inside value; buy the confirmation, not the poke
- entry 2,019.54 | stop 2,010.30 | T1 2,327.04 | T2 2,047.24
- R:R 33.30 at T1, 3.00 at T2 | risk 9.23
- invalid: 1H close back below 2,018.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 33.30R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,792.16 or pivot support near 1,792.16; buy the hold, not the touch
- entry 1,792.16 | stop 1,782.92 | T1 1,804.74 | T2 1,816.75
- R:R 1.36 at T1, 2.66 at T2 | risk 9.23
- invalid: 5m close below 1,782.92: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.36R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.70-$9.23); funding runs +0.0091%/day ($+0.04/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
