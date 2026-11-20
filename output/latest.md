# ETH perp (Hyperliquid) - 2026-11-20 16:45 UTC+05:30 (11:15 UTC)
spot 1,749.45 | mark 1,749.50 | oracle 1,750.22 | OI 613,763.31 ETH (+1.112% vs last run, +2.41% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $967.2m

## 1) HTF bias - BEARISH (-5 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,772.74 / 1,860.89) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 26% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +2.4% with price -3.0%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.25 | VAH 1,976.00 (width 265.50 = 15.18% of spot, 240 bars)
- developing session (47% elapsed): VAL 1,730.00 | POC 1,747.75 | VAH 1,757.00
- session VWAP 1,743.14 (+1s 1,754.60 / -1s 1,731.69) | prior session VWAP 1,778.27
- prior day: PDH 1,816.40 | PDL 1,735.30 | PDC 1,756.60 (PDH intact, PDL swept)
- floor pivots: S3 1,641.37 | S2 1,688.33 | S1 1,722.47 | P 1,769.43 | R1 1,803.57 | R2 1,850.53 | R3 1,884.67
- 1H ATR(14) 19.66 = 1.12% of spot | ATR vs 30d median x1.00
- distance to POC -3.40 ATR | VAH -11.52 ATR | VAL +1.98 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00076%/hr, BybitPerp +0.00066%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,700.67 | T1 1,816.25 | T2 1,976.00
- R:R 10.76 at T1, 27.01 at T2 | risk 9.83
- invalid: 5m close below 1,700.67: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.76R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,710.50 while still inside value; sell the confirmation, not the poke
- entry 1,708.53 | stop 1,720.33 | T1 1,688.33 | T2 1,641.37
- R:R 1.71 at T1, 5.69 at T2 | risk 11.79
- invalid: 1H close back above 1,710.50: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 1.71R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,743.14 or pivot resistance near 1,769.43; sell the rejection, not the touch
- entry 1,769.43 | stop 1,781.23 | T1 1,735.30 | T2 1,722.47
- R:R 2.89 at T1, 3.98 at T2 | risk 11.79
- invalid: 5m close above 1,781.23: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.89R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.83-$11.79); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
