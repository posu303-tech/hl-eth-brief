# ETH perp (Hyperliquid) - 2026-11-11 16:09 UTC+05:30 (10:39 UTC)
spot 2,063.45 | mark 2,063.50 | oracle 2,064.10 | OI 773,866.08 ETH (+1.588% vs last run, -3.29% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,327.3m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,093.02 / 2,192.21) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 37% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -3.3%, price -1.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,004.00 | POC 2,124.50 | VAH 2,282.00 (width 278.00 = 13.47% of spot, 240 bars)
- developing session (44% elapsed): VAL 2,052.00 | POC 2,067.50 | VAH 2,069.00
- session VWAP 2,058.01 (+1s 2,065.07 / -1s 2,050.96) | prior session VWAP 2,060.93
- prior day: PDH 2,135.80 | PDL 2,003.70 | PDC 2,052.50 (PDH intact, PDL intact)
- floor pivots: S3 1,860.10 | S2 1,931.90 | S1 1,992.20 | P 2,064.00 | R1 2,124.30 | R2 2,196.10 | R3 2,256.40
- 1H ATR(14) 18.68 = 0.91% of spot | ATR vs 30d median x0.92
- distance to POC -3.27 ATR | VAH -11.70 ATR | VAL +3.18 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00055%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,004.00; enter on the reclaim
- entry 2,004.00 | stop 1,994.66 | T1 2,124.50 | T2 2,282.00
- R:R 12.90 at T1, 29.76 at T2 | risk 9.34
- invalid: 5m close below 1,994.66: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.90R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,282.00 while still inside value; buy the confirmation, not the poke
- entry 2,283.87 | stop 2,272.66 | T1 2,561.87 | T2 2,317.50
- R:R 24.80 at T1, 3.00 at T2 | risk 11.21
- invalid: 1H close back below 2,282.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 24.80R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,058.01 or pivot support near 2,058.01; buy the hold, not the touch
- entry 2,058.01 | stop 2,046.80 | T1 2,095.38 | T2 2,124.30
- R:R 3.33 at T1, 5.91 at T2 | risk 11.21
- invalid: 5m close below 2,046.80: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.34-$11.21); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
