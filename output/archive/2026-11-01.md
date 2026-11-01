# ETH perp (Hyperliquid) - 2026-11-01 12:50 UTC+05:30 (07:20 UTC)
spot 2,264.35 | mark 2,264.39 | oracle 2,265.03 | OI 984,511.78 ETH (+0.387% vs last run, -0.27% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $264.9m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,258.90 / 2,309.74) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 64% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -0.3%, price +0.9%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,262.00 | POC 2,326.50 | VAH 2,413.00 (width 151.00 = 6.67% of spot, 240 bars)
- developing session (31% elapsed): VAL 2,266.00 | POC 2,267.50 | VAH 2,272.00
- session VWAP 2,267.57 (+1s 2,270.76 / -1s 2,264.39) | prior session VWAP 2,247.80
- prior day: PDH 2,266.10 | PDL 2,235.00 | PDC 2,254.80 (PDH swept, PDL intact)
- floor pivots: S3 2,206.73 | S2 2,220.87 | S1 2,237.83 | P 2,251.97 | R1 2,268.93 | R2 2,283.07 | R3 2,300.03
- 1H ATR(14) 8.64 = 0.38% of spot | ATR vs 30d median x0.77
- distance to POC -7.19 ATR | VAH -17.20 ATR | VAL +0.27 ATR | closes outside value (last 20): 70%
- cross-venue funding: BinPerp +0.00027%/hr, BybitPerp +0.00000%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,262.00; enter on the reclaim
- entry 2,262.00 | stop 2,257.68 | T1 2,326.50 | T2 2,413.00
- R:R 14.92 at T1, 34.94 at T2 | risk 4.32
- invalid: 5m close below 2,257.68: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 14.92R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,413.00 while still inside value; buy the confirmation, not the poke
- entry 2,413.86 | stop 2,408.68 | T1 2,564.86 | T2 2,429.42
- R:R 29.12 at T1, 3.00 at T2 | risk 5.19
- invalid: 1H close back below 2,413.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 29.12R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,267.57 or pivot support near 2,251.97; buy the hold, not the touch
- entry 2,251.97 | stop 2,246.78 | T1 2,266.10 | T2 2,270.76
- R:R 2.73 at T1, 3.62 at T2 | risk 5.19
- invalid: 5m close below 2,246.78: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.73R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$4.32-$5.19); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
