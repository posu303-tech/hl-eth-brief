# ETH perp (Hyperliquid) - 2026-10-27 21:53 UTC+05:30 (16:23 UTC)
spot 2,345.15 | mark 2,345.10 | oracle 2,346.09 | OI 1,119,334.56 ETH (-1.308% vs last run, -0.11% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $811.3m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,327.13 / 2,374.06) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -0.1%, price +1.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,336.00 | POC 2,400.50 | VAH 2,459.00 (width 123.00 = 5.24% of spot, 240 bars)
- developing session (68% elapsed): VAL 2,311.00 | POC 2,327.50 | VAH 2,335.00
- session VWAP 2,323.94 (+1s 2,335.59 / -1s 2,312.28) | prior session VWAP 2,318.19
- prior day: PDH 2,344.40 | PDL 2,292.60 | PDC 2,323.40 (PDH swept, PDL intact)
- floor pivots: S3 2,244.07 | S2 2,268.33 | S1 2,295.87 | P 2,320.13 | R1 2,347.67 | R2 2,371.93 | R3 2,399.47
- 1H ATR(14) 17.30 = 0.74% of spot | ATR vs 30d median x1.04
- distance to POC -3.20 ATR | VAH -6.58 ATR | VAL +0.53 ATR | closes outside value (last 20): 95%
- cross-venue funding: BinPerp +0.00103%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,336.00; enter on the reclaim
- entry 2,336.00 | stop 2,327.35 | T1 2,400.50 | T2 2,459.00
- R:R 7.46 at T1, 14.22 at T2 | risk 8.65
- invalid: 5m close below 2,327.35: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 7.46R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,459.00 while still inside value; buy the confirmation, not the poke
- entry 2,460.73 | stop 2,450.35 | T1 2,583.73 | T2 2,491.87
- R:R 11.85 at T1, 3.00 at T2 | risk 10.38
- invalid: 1H close back below 2,459.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 11.85R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,323.94 or pivot support near 2,323.94; buy the hold, not the touch
- entry 2,323.94 | stop 2,313.56 | T1 2,335.59 | T2 2,344.40
- R:R 1.12 at T1, 1.97 at T2 | risk 10.38
- invalid: 5m close below 2,313.56: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.12R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$8.65-$10.38); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
