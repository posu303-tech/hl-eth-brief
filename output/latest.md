# ETH perp (Hyperliquid) - 2026-10-28 21:24 UTC+05:30 (15:54 UTC)
spot 2,331.45 | mark 2,331.60 | oracle 2,332.70 | OI 1,136,607.25 ETH (+1.683% vs last run, +1.54% 24h)
funding +0.00122%/hr (~+10.71%/yr, 38th pct of last 500h) | 24h notional $501.9m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,342.15 / 2,369.51) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 79% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 38th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +1.5% with price -0.6%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,314.00 | POC 2,400.50 | VAH 2,429.00 (width 115.00 = 4.93% of spot, 240 bars)
- developing session (66% elapsed): VAL 2,340.00 | POC 2,352.50 | VAH 2,380.00
- session VWAP 2,352.32 (+1s 2,367.76 / -1s 2,336.88) | prior session VWAP 2,329.40
- prior day: PDH 2,364.10 | PDL 2,296.20 | PDC 2,349.70 (PDH swept, PDL intact)
- floor pivots: S3 2,241.33 | S2 2,268.77 | S1 2,309.23 | P 2,336.67 | R1 2,377.13 | R2 2,404.57 | R3 2,445.03
- 1H ATR(14) 14.26 = 0.61% of spot | ATR vs 30d median x0.98
- distance to POC -4.84 ATR | VAH -6.84 ATR | VAL +1.22 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00114%/hr, BybitPerp +0.00096%/hr, HlPerp +0.00122%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,314.00; enter on the reclaim
- entry 2,314.00 | stop 2,306.87 | T1 2,400.50 | T2 2,429.00
- R:R 12.14 at T1, 16.13 at T2 | risk 7.13
- invalid: 5m close below 2,306.87: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.14R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,429.00 while still inside value; buy the confirmation, not the poke
- entry 2,430.43 | stop 2,421.87 | T1 2,445.03 | T2 2,545.43
- R:R 1.71 at T1, 13.44 at T2 | risk 8.55
- invalid: 1H close back below 2,429.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 1.71R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,352.32 or pivot support near 2,309.23; buy the hold, not the touch
- entry 2,309.23 | stop 2,300.68 | T1 2,337.75 | T2 2,364.10
- R:R 3.33 at T1, 6.41 at T2 | risk 8.55
- invalid: 5m close below 2,300.68: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.13-$8.55); funding runs +0.0294%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
