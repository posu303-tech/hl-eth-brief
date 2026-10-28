# ETH perp (Hyperliquid) - 2026-10-28 13:45 UTC+05:30 (08:15 UTC)
spot 2,364.35 | mark 2,364.50 | oracle 2,365.50 | OI 1,117,797.24 ETH (-1.015% vs last run, -1.44% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $665.4m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,338.66 / 2,370.64) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 79% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.4%, price +2.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,314.00 | POC 2,400.50 | VAH 2,429.00 (width 115.00 = 4.86% of spot, 240 bars)
- developing session (34% elapsed): VAL 2,351.00 | POC 2,352.50 | VAH 2,366.00
- session VWAP 2,354.70 (+1s 2,361.33 / -1s 2,348.08) | prior session VWAP 2,329.40
- prior day: PDH 2,364.10 | PDL 2,296.20 | PDC 2,349.70 (PDH swept, PDL intact)
- floor pivots: S3 2,241.33 | S2 2,268.77 | S1 2,309.23 | P 2,336.67 | R1 2,377.13 | R2 2,404.57 | R3 2,445.03
- 1H ATR(14) 12.61 = 0.53% of spot | ATR vs 30d median x0.83
- distance to POC -2.87 ATR | VAH -5.13 ATR | VAL +3.99 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00089%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,314.00; enter on the reclaim
- entry 2,314.00 | stop 2,307.69 | T1 2,400.50 | T2 2,429.00
- R:R 13.72 at T1, 18.23 at T2 | risk 6.31
- invalid: 5m close below 2,307.69: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 13.72R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,429.00 while still inside value; buy the confirmation, not the poke
- entry 2,430.26 | stop 2,422.69 | T1 2,445.03 | T2 2,545.26
- R:R 1.95 at T1, 15.20 at T2 | risk 7.57
- invalid: 1H close back below 2,429.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 1.95R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,354.70 or pivot support near 2,354.70; buy the hold, not the touch
- entry 2,354.70 | stop 2,347.14 | T1 2,361.33 | T2 2,377.13
- R:R 0.88 at T1, 2.96 at T2 | risk 7.57
- invalid: 5m close below 2,347.14: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.88R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$6.31-$7.57); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
