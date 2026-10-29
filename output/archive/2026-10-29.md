# ETH perp (Hyperliquid) - 2026-10-29 12:26 UTC+05:30 (06:56 UTC)
spot 2,311.85 | mark 2,311.90 | oracle 2,313.00 | OI 1,096,238.27 ETH (-1.351% vs last run, -1.93% 24h)
funding +0.00023%/hr (~+2.03%/yr, 17th pct of last 500h) | 24h notional $920.3m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,340.42 / 2,365.38) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 52% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 17th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.9%, price -1.7%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,306.00 | POC 2,400.50 | VAH 2,417.00 (width 111.00 = 4.80% of spot, 240 bars)
- developing session (29% elapsed): VAL 2,299.00 | POC 2,307.50 | VAH 2,322.00
- session VWAP 2,314.39 (+1s 2,327.49 / -1s 2,301.30) | prior session VWAP 2,355.95
- prior day: PDH 2,391.00 | PDL 2,322.70 | PDC 2,358.40 (PDH intact, PDL swept)
- floor pivots: S3 2,255.43 | S2 2,289.07 | S1 2,323.73 | P 2,357.37 | R1 2,392.03 | R2 2,425.67 | R3 2,460.33
- 1H ATR(14) 17.47 = 0.76% of spot | ATR vs 30d median x1.22
- distance to POC -5.08 ATR | VAH -6.02 ATR | VAL +0.33 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00047%/hr, BybitPerp +0.00072%/hr, HlPerp +0.00023%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,306.00; enter on the reclaim
- entry 2,306.00 | stop 2,297.27 | T1 2,400.50 | T2 2,417.00
- R:R 10.82 at T1, 12.71 at T2 | risk 8.73
- invalid: 5m close below 2,297.27: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.82R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,417.00 while still inside value; buy the confirmation, not the poke
- entry 2,418.75 | stop 2,408.27 | T1 2,460.33 | T2 2,529.75
- R:R 3.97 at T1, 10.59 at T2 | risk 10.48
- invalid: 1H close back below 2,417.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 3.97R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,314.39 or pivot resistance near 2,357.37; sell the rejection, not the touch
- entry 2,357.37 | stop 2,367.85 | T1 2,323.73 | T2 2,306.00
- R:R 3.21 at T1, 4.90 at T2 | risk 10.48
- invalid: 5m close above 2,367.85: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.21R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$8.73-$10.48); funding runs +0.0056%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
