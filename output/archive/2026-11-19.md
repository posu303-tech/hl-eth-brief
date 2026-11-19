# ETH perp (Hyperliquid) - 2026-11-20 02:50 UTC+05:30 (21:20 UTC)
spot 1,742.75 | mark 1,743.00 | oracle 1,743.90 | OI 611,332.90 ETH (+2.007% vs last run, +0.03% 24h)
funding +0.00074%/hr (~+6.50%/yr, 23th pct of last 500h) | 24h notional $793.1m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,791.76 / 1,877.94) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 47% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 23th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +0.0%, price -1.0%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.75 | VAH 2,018.00 (width 307.50 = 17.64% of spot, 240 bars)
- developing session (89% elapsed): VAL 1,751.00 | POC 1,777.75 | VAH 1,794.50
- session VWAP 1,781.98 (+1s 1,798.20 / -1s 1,765.77) | prior session VWAP 1,778.32
- prior day: PDH 1,825.80 | PDL 1,732.60 | PDC 1,776.50 (PDH intact, PDL intact)
- floor pivots: S3 1,637.60 | S2 1,685.10 | S1 1,730.80 | P 1,778.30 | R1 1,824.00 | R2 1,871.50 | R3 1,917.20
- 1H ATR(14) 19.67 = 1.13% of spot | ATR vs 30d median x1.05
- distance to POC -3.76 ATR | VAH -13.99 ATR | VAL +1.64 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00037%/hr, BybitPerp +0.00085%/hr, HlPerp +0.00079%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,700.67 | T1 1,816.75 | T2 2,018.00
- R:R 10.80 at T1, 31.27 at T2 | risk 9.83
- invalid: 5m close below 1,700.67: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.80R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,018.00 while still inside value; buy the confirmation, not the poke
- entry 2,019.97 | stop 2,008.17 | T1 2,327.47 | T2 2,055.37
- R:R 26.06 at T1, 3.00 at T2 | risk 11.80
- invalid: 1H close back below 2,018.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 26.06R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,781.98 or pivot support near 1,730.80; buy the hold, not the touch
- entry 1,730.80 | stop 1,719.00 | T1 1,770.14 | T2 1,798.20
- R:R 3.33 at T1, 5.71 at T2 | risk 11.80
- invalid: 5m close below 1,719.00: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.83-$11.80); funding runs +0.0178%/day ($+0.07/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
