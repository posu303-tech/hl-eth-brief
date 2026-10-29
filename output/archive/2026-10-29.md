# ETH perp (Hyperliquid) - 2026-10-30 01:40 UTC+05:30 (20:10 UTC)
spot 2,306.85 | mark 2,306.80 | oracle 2,308.02 | OI 1,084,103.50 ETH (-4.196% vs last run, -2.80% 24h)
funding -0.00002%/hr (~-0.20%/yr, 11th pct of last 500h) | 24h notional $1,042.2m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,337.01 / 2,360.92) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 52% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 11th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -2.8%, price -2.5%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,306.00 | POC 2,400.50 | VAH 2,417.00 (width 111.00 = 4.81% of spot, 240 bars)
- developing session (84% elapsed): VAL 2,303.00 | POC 2,307.50 | VAH 2,344.00
- session VWAP 2,328.91 (+1s 2,348.96 / -1s 2,308.86) | prior session VWAP 2,355.95
- prior day: PDH 2,391.00 | PDL 2,322.70 | PDC 2,358.40 (PDH intact, PDL swept)
- floor pivots: S3 2,255.43 | S2 2,289.07 | S1 2,323.73 | P 2,357.37 | R1 2,392.03 | R2 2,425.67 | R3 2,460.33
- 1H ATR(14) 17.95 = 0.78% of spot | ATR vs 30d median x1.08
- distance to POC -5.22 ATR | VAH -6.14 ATR | VAL +0.05 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00106%/hr, BybitPerp +0.00067%/hr, HlPerp +0.00010%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,306.00; enter on the reclaim
- entry 2,306.00 | stop 2,297.03 | T1 2,400.50 | T2 2,417.00
- R:R 10.53 at T1, 12.37 at T2 | risk 8.97
- invalid: 5m close below 2,297.03: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.53R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,417.00 while still inside value; buy the confirmation, not the poke
- entry 2,418.79 | stop 2,408.03 | T1 2,460.33 | T2 2,529.79
- R:R 3.86 at T1, 10.31 at T2 | risk 10.77
- invalid: 1H close back below 2,417.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 3.86R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,328.91 or pivot resistance near 2,328.91; sell the rejection, not the touch
- entry 2,328.91 | stop 2,339.68 | T1 2,308.86 | T2 2,293.01
- R:R 1.86 at T1, 3.33 at T2 | risk 10.77
- invalid: 5m close above 2,339.68: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.86R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$8.97-$10.77); funding runs -0.0006%/day ($-0.00/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
