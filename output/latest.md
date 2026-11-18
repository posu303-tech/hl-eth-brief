# ETH perp (Hyperliquid) - 2026-11-19 02:47 UTC+05:30 (21:17 UTC)
spot 1,756.65 | mark 1,756.69 | oracle 1,757.65 | OI 611,153.66 ETH (+0.233% vs last run, -2.42% 24h)
funding -0.00001%/hr (~-0.09%/yr, 9th pct of last 500h) | 24h notional $670.2m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,799.83 / 1,902.57) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 9th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -2.4%, price -2.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.75 | VAH 2,049.50 (width 339.00 = 19.30% of spot, 240 bars)
- developing session (89% elapsed): VAL 1,732.50 | POC 1,756.75 | VAH 1,797.50
- session VWAP 1,778.78 (+1s 1,801.82 / -1s 1,755.74) | prior session VWAP 1,800.56
- prior day: PDH 1,842.80 | PDL 1,750.10 | PDC 1,824.30 (PDH intact, PDL swept)
- floor pivots: S3 1,675.97 | S2 1,713.03 | S1 1,768.67 | P 1,805.73 | R1 1,861.37 | R2 1,898.43 | R3 1,954.07
- 1H ATR(14) 18.96 = 1.08% of spot | ATR vs 30d median x0.98
- distance to POC -3.17 ATR | VAH -15.44 ATR | VAL +2.43 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00101%/hr, BybitPerp +0.00069%/hr, HlPerp -0.00003%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,701.02 | T1 1,816.75 | T2 2,049.50
- R:R 11.21 at T1, 35.75 at T2 | risk 9.48
- invalid: 5m close below 1,701.02: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.21R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,049.50 while still inside value; buy the confirmation, not the poke
- entry 2,051.40 | stop 2,040.02 | T1 2,390.40 | T2 2,085.53
- R:R 29.79 at T1, 3.00 at T2 | risk 11.38
- invalid: 1H close back below 2,049.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 29.79R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,778.78 or pivot resistance near 1,778.78; sell the rejection, not the touch
- entry 1,778.78 | stop 1,790.16 | T1 1,768.67 | T2 1,755.74
- R:R 0.89 at T1, 2.03 at T2 | risk 11.38
- invalid: 5m close above 1,790.16: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.89R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.48-$11.38); funding runs -0.0003%/day ($-0.00/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
