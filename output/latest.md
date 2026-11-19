# ETH perp (Hyperliquid) - 2026-11-19 08:38 UTC+05:30 (03:08 UTC)
spot 1,766.25 | mark 1,766.15 | oracle 1,766.90 | OI 600,366.31 ETH (-1.765% vs last run, -1.25% 24h)
funding +0.00100%/hr (~+8.75%/yr, 29th pct of last 500h) | 24h notional $615.3m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,793.85 / 1,894.94) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 47% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 29th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -1.2%, price -2.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.75 | VAH 2,018.00 (width 307.50 = 17.41% of spot, 240 bars)
- developing session (13% elapsed): VAL 1,767.50 | POC 1,770.25 | VAH 1,782.00
- session VWAP 1,777.16 (+1s 1,783.28 / -1s 1,771.03) | prior session VWAP 1,778.32
- prior day: PDH 1,825.80 | PDL 1,732.60 | PDC 1,776.50 (PDH intact, PDL intact)
- floor pivots: S3 1,637.60 | S2 1,685.10 | S1 1,730.80 | P 1,778.30 | R1 1,824.00 | R2 1,871.50 | R3 1,917.20
- 1H ATR(14) 18.77 = 1.06% of spot | ATR vs 30d median x0.99
- distance to POC -2.69 ATR | VAH -13.41 ATR | VAL +2.97 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00091%/hr, BybitPerp +0.00062%/hr, HlPerp +0.00099%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,701.11 | T1 1,816.75 | T2 2,018.00
- R:R 11.32 at T1, 32.76 at T2 | risk 9.39
- invalid: 5m close below 1,701.11: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.32R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,018.00 while still inside value; buy the confirmation, not the poke
- entry 2,019.88 | stop 2,008.61 | T1 2,327.38 | T2 2,053.67
- R:R 27.30 at T1, 3.00 at T2 | risk 11.26
- invalid: 1H close back below 2,018.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 27.30R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,777.16 or pivot support near 1,730.80; buy the hold, not the touch
- entry 1,730.80 | stop 1,719.54 | T1 1,768.34 | T2 1,783.28
- R:R 3.33 at T1, 4.66 at T2 | risk 11.26
- invalid: 5m close below 1,719.54: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.39-$11.26); funding runs +0.0240%/day ($+0.10/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
