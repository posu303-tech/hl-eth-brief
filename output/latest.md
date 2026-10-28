# ETH perp (Hyperliquid) - 2026-10-29 02:26 UTC+05:30 (20:56 UTC)
spot 2,356.65 | mark 2,356.70 | oracle 2,357.72 | OI 1,115,329.01 ETH (-1.872% vs last run, -1.59% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $779.3m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,343.27 / 2,368.45) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 79% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.6%, price +0.6%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,314.00 | POC 2,400.50 | VAH 2,429.00 (width 115.00 = 4.88% of spot, 240 bars)
- developing session (87% elapsed): VAL 2,338.00 | POC 2,352.50 | VAH 2,372.00
- session VWAP 2,355.35 (+1s 2,369.65 / -1s 2,341.06) | prior session VWAP 2,329.40
- prior day: PDH 2,364.10 | PDL 2,296.20 | PDC 2,349.70 (PDH swept, PDL intact)
- floor pivots: S3 2,241.33 | S2 2,268.77 | S1 2,309.23 | P 2,336.67 | R1 2,377.13 | R2 2,404.57 | R3 2,445.03
- 1H ATR(14) 15.51 = 0.66% of spot | ATR vs 30d median x1.08
- distance to POC -2.83 ATR | VAH -4.67 ATR | VAL +2.75 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00096%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,314.00; enter on the reclaim
- entry 2,314.00 | stop 2,306.25 | T1 2,400.50 | T2 2,429.00
- R:R 11.16 at T1, 14.83 at T2 | risk 7.75
- invalid: 5m close below 2,306.25: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.16R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,429.00 while still inside value; buy the confirmation, not the poke
- entry 2,430.55 | stop 2,421.25 | T1 2,445.03 | T2 2,545.55
- R:R 1.56 at T1, 12.36 at T2 | risk 9.30
- invalid: 1H close back below 2,429.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 1.56R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,355.35 or pivot support near 2,336.67; buy the hold, not the touch
- entry 2,336.67 | stop 2,327.36 | T1 2,364.10 | T2 2,377.13
- R:R 2.95 at T1, 4.35 at T2 | risk 9.30
- invalid: 5m close below 2,327.36: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.95R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.75-$9.30); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
