# ETH perp (Hyperliquid) - 2026-11-18 18:24 UTC+05:30 (12:54 UTC)
spot 1,794.35 | mark 1,794.40 | oracle 1,795.50 | OI 609,734.46 ETH (+0.294% vs last run, +0.71% 24h)
funding +0.00004%/hr (~+0.32%/yr, 9th pct of last 500h) | 24h notional $818.1m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,813.70 / 1,915.17) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 9th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +0.7%, price -1.5%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.75 | VAH 2,049.50 (width 339.00 = 18.89% of spot, 240 bars)
- developing session (54% elapsed): VAL 1,798.50 | POC 1,811.25 | VAH 1,815.50
- session VWAP 1,806.20 (+1s 1,813.91 / -1s 1,798.48) | prior session VWAP 1,800.56
- prior day: PDH 1,842.80 | PDL 1,750.10 | PDC 1,824.30 (PDH intact, PDL intact)
- floor pivots: S3 1,675.97 | S2 1,713.03 | S1 1,768.67 | P 1,805.73 | R1 1,861.37 | R2 1,898.43 | R3 1,954.07
- 1H ATR(14) 15.86 = 0.88% of spot | ATR vs 30d median x0.85
- distance to POC -1.41 ATR | VAH -16.09 ATR | VAL +5.29 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00024%/hr, BybitPerp -0.00010%/hr, HlPerp +0.00006%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,702.57 | T1 1,816.75 | T2 2,049.50
- R:R 13.40 at T1, 42.75 at T2 | risk 7.93
- invalid: 5m close below 1,702.57: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 13.40R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,049.50 while still inside value; buy the confirmation, not the poke
- entry 2,051.09 | stop 2,041.57 | T1 2,390.09 | T2 2,079.64
- R:R 35.62 at T1, 3.00 at T2 | risk 9.52
- invalid: 1H close back below 2,049.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 35.62R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,806.20 or pivot support near 1,768.67; buy the hold, not the touch
- entry 1,768.67 | stop 1,759.15 | T1 1,800.39 | T2 1,813.91
- R:R 3.33 at T1, 4.75 at T2 | risk 9.52
- invalid: 5m close below 1,759.15: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.93-$9.52); funding runs +0.0009%/day ($+0.00/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
