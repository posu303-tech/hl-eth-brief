# ETH perp (Hyperliquid) - 2026-11-02 04:58 UTC+05:30 (23:28 UTC)
spot 2,266.45 | mark 2,266.80 | oracle 2,267.70 | OI 970,921.80 ETH (-0.683% vs last run, -1.00% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $315.9m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,261.97 / 2,303.25) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 64% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.0%, price +0.5%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,262.00 | POC 2,326.50 | VAH 2,413.00 (width 151.00 = 6.66% of spot, 240 bars)
- developing session (98% elapsed): VAL 2,261.00 | POC 2,268.50 | VAH 2,272.00
- session VWAP 2,265.64 (+1s 2,270.70 / -1s 2,260.57) | prior session VWAP 2,247.80
- prior day: PDH 2,266.10 | PDL 2,235.00 | PDC 2,254.80 (PDH swept, PDL intact)
- floor pivots: S3 2,206.73 | S2 2,220.87 | S1 2,237.83 | P 2,251.97 | R1 2,268.93 | R2 2,283.07 | R3 2,300.03
- 1H ATR(14) 8.46 = 0.37% of spot | ATR vs 30d median x0.98
- distance to POC -7.10 ATR | VAH -17.32 ATR | VAL +0.53 ATR | closes outside value (last 20): 15%
- cross-venue funding: BinPerp +0.00018%/hr, BybitPerp +0.00000%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,262.00; enter on the reclaim
- entry 2,262.00 | stop 2,257.77 | T1 2,326.50 | T2 2,413.00
- R:R 15.24 at T1, 35.69 at T2 | risk 4.23
- invalid: 5m close below 2,257.77: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 15.24R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,413.00 while still inside value; buy the confirmation, not the poke
- entry 2,413.85 | stop 2,408.77 | T1 2,564.85 | T2 2,429.08
- R:R 29.74 at T1, 3.00 at T2 | risk 5.08
- invalid: 1H close back below 2,413.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 29.74R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,265.64 or pivot support near 2,251.97; buy the hold, not the touch
- entry 2,251.97 | stop 2,246.89 | T1 2,266.10 | T2 2,270.70
- R:R 2.78 at T1, 3.69 at T2 | risk 5.08
- invalid: 5m close below 2,246.89: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.78R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$4.23-$5.08); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
