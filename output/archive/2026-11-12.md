# ETH perp (Hyperliquid) - 2026-11-12 23:36 UTC+05:30 (18:06 UTC)
spot 2,017.25 | mark 2,017.14 | oracle 2,017.88 | OI 760,066.71 ETH (-0.326% vs last run, -1.20% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,201.3m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,056.52 / 2,152.69) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 30% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.2%, price -3.4%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,004.00 | POC 2,124.50 | VAH 2,279.00 (width 275.00 = 13.63% of spot, 240 bars)
- developing session (75% elapsed): VAL 1,989.00 | POC 2,012.50 | VAH 2,024.00
- session VWAP 2,016.52 (+1s 2,035.54 / -1s 1,997.50) | prior session VWAP 2,066.33
- prior day: PDH 2,103.00 | PDL 2,034.70 | PDC 2,055.50 (PDH intact, PDL swept)
- floor pivots: S3 1,957.50 | S2 1,996.10 | S1 2,025.80 | P 2,064.40 | R1 2,094.10 | R2 2,132.70 | R3 2,162.40
- 1H ATR(14) 18.75 = 0.93% of spot | ATR vs 30d median x1.10
- distance to POC -5.72 ATR | VAH -13.96 ATR | VAL +0.71 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00091%/hr, BybitPerp +0.00103%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,004.00; enter on the reclaim
- entry 2,004.00 | stop 1,994.62 | T1 2,124.50 | T2 2,279.00
- R:R 12.85 at T1, 29.33 at T2 | risk 9.38
- invalid: 5m close below 1,994.62: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.85R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 2,004.00 while still inside value; sell the confirmation, not the poke
- entry 2,002.12 | stop 2,013.38 | T1 1,957.50 | T2 1,727.12
- R:R 3.97 at T1, 24.44 at T2 | risk 11.25
- invalid: 1H close back above 2,004.00: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 3.97R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,016.52 or pivot resistance near 2,064.40; sell the rejection, not the touch
- entry 2,064.40 | stop 2,075.65 | T1 2,034.70 | T2 2,026.89
- R:R 2.64 at T1, 3.33 at T2 | risk 11.25
- invalid: 5m close above 2,075.65: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.64R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.38-$11.25); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
