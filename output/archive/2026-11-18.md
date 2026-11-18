# ETH perp (Hyperliquid) - 2026-11-18 09:04 UTC+05:30 (03:34 UTC)
spot 1,806.65 | mark 1,806.70 | oracle 1,807.54 | OI 607,949.61 ETH (-2.928% vs last run, +0.71% 24h)
funding +0.00101%/hr (~+8.89%/yr, 27th pct of last 500h) | 24h notional $915.5m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,816.00 / 1,925.23) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 27th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +0.7%, price -1.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.75 | VAH 2,049.50 (width 339.00 = 18.76% of spot, 240 bars)
- developing session (15% elapsed): VAL 1,796.00 | POC 1,803.75 | VAH 1,811.00
- session VWAP 1,807.96 (+1s 1,815.71 / -1s 1,800.21) | prior session VWAP 1,800.56
- prior day: PDH 1,842.80 | PDL 1,750.10 | PDC 1,824.30 (PDH intact, PDL intact)
- floor pivots: S3 1,675.97 | S2 1,713.03 | S1 1,768.67 | P 1,805.73 | R1 1,861.37 | R2 1,898.43 | R3 1,954.07
- 1H ATR(14) 19.89 = 1.10% of spot | ATR vs 30d median x1.03
- distance to POC -0.51 ATR | VAH -12.21 ATR | VAL +4.83 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00074%/hr, BybitPerp +0.00064%/hr, HlPerp +0.00103%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,700.56 | T1 1,816.75 | T2 2,049.50
- R:R 10.69 at T1, 34.09 at T2 | risk 9.94
- invalid: 5m close below 1,700.56: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.69R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,049.50 while still inside value; buy the confirmation, not the poke
- entry 2,051.49 | stop 2,039.56 | T1 2,390.49 | T2 2,087.29
- R:R 28.41 at T1, 3.00 at T2 | risk 11.93
- invalid: 1H close back below 2,049.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 28.41R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,807.96 or pivot support near 1,768.67; buy the hold, not the touch
- entry 1,768.67 | stop 1,756.73 | T1 1,808.44 | T2 1,816.75
- R:R 3.33 at T1, 4.03 at T2 | risk 11.93
- invalid: 5m close below 1,756.73: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.94-$11.93); funding runs +0.0243%/day ($+0.10/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
