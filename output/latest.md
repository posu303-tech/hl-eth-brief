# ETH perp (Hyperliquid) - 2026-11-01 02:52 UTC+05:30 (21:22 UTC)
spot 2,252.25 | mark 2,252.39 | oracle 2,253.28 | OI 978,663.26 ETH (+0.137% vs last run, -1.67% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $229.8m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,256.67 / 2,314.66) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.7%, price +0.5%: no edge | 0 |

## 2) Intraday regime - failed-auction, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,251.00 | POC 2,326.50 | VAH 2,413.00 (width 162.00 = 7.19% of spot, 240 bars)
- developing session (89% elapsed): VAL 2,242.00 | POC 2,244.50 | VAH 2,253.00
- session VWAP 2,246.10 (+1s 2,250.79 / -1s 2,241.41) | prior session VWAP 2,225.15
- prior day: PDH 2,261.00 | PDL 2,173.10 | PDC 2,243.50 (PDH intact, PDL intact)
- floor pivots: S3 2,102.83 | S2 2,137.97 | S1 2,190.73 | P 2,225.87 | R1 2,278.63 | R2 2,313.77 | R3 2,366.53
- 1H ATR(14) 9.74 = 0.43% of spot | ATR vs 30d median x0.62
- distance to POC -7.62 ATR | VAH -16.50 ATR | VAL +0.13 ATR | closes outside value (last 20): 75%
- cross-venue funding: BinPerp -0.00128%/hr, BybitPerp -0.00010%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,251.00; enter on the reclaim
- entry 2,251.00 | stop 2,246.13 | T1 2,326.50 | T2 2,413.00
- R:R 15.50 at T1, 33.25 at T2 | risk 4.87
- invalid: 5m close below 2,246.13: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 15.50R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,413.00 while still inside value; buy the confirmation, not the poke
- entry 2,413.97 | stop 2,408.13 | T1 2,575.97 | T2 2,431.51
- R:R 27.71 at T1, 3.00 at T2 | risk 5.85
- invalid: 1H close back below 2,413.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 27.71R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,246.10 or pivot support near 2,246.10; buy the hold, not the touch
- entry 2,246.10 | stop 2,240.25 | T1 2,250.79 | T2 2,261.00
- R:R 0.80 at T1, 2.55 at T2 | risk 5.85
- invalid: 5m close below 2,240.25: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.80R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$4.87-$5.85); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
