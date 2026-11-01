# ETH perp (Hyperliquid) - 2026-11-01 20:26 UTC+05:30 (14:56 UTC)
spot 2,270.05 | mark 2,270.00 | oracle 2,270.86 | OI 983,323.98 ETH (-0.121% vs last run, +0.61% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $267.5m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,261.27 / 2,306.97) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 64% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +0.6%, price +1.1%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,262.00 | POC 2,326.50 | VAH 2,413.00 (width 151.00 = 6.65% of spot, 240 bars)
- developing session (62% elapsed): VAL 2,264.00 | POC 2,268.50 | VAH 2,272.00
- session VWAP 2,267.57 (+1s 2,271.60 / -1s 2,263.55) | prior session VWAP 2,247.80
- prior day: PDH 2,266.10 | PDL 2,235.00 | PDC 2,254.80 (PDH swept, PDL intact)
- floor pivots: S3 2,206.73 | S2 2,220.87 | S1 2,237.83 | P 2,251.97 | R1 2,268.93 | R2 2,283.07 | R3 2,300.03
- 1H ATR(14) 8.47 = 0.37% of spot | ATR vs 30d median x0.89
- distance to POC -6.66 ATR | VAH -16.87 ATR | VAL +0.95 ATR | closes outside value (last 20): 40%
- cross-venue funding: BinPerp -0.00009%/hr, BybitPerp +0.00015%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,262.00; enter on the reclaim
- entry 2,262.00 | stop 2,257.76 | T1 2,326.50 | T2 2,413.00
- R:R 15.22 at T1, 35.64 at T2 | risk 4.24
- invalid: 5m close below 2,257.76: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 15.22R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,413.00 while still inside value; buy the confirmation, not the poke
- entry 2,413.85 | stop 2,408.76 | T1 2,564.85 | T2 2,429.10
- R:R 29.70 at T1, 3.00 at T2 | risk 5.08
- invalid: 1H close back below 2,413.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 29.70R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,267.57 or pivot support near 2,267.57; buy the hold, not the touch
- entry 2,267.57 | stop 2,262.49 | T1 2,271.60 | T2 2,284.52
- R:R 0.79 at T1, 3.33 at T2 | risk 5.08
- invalid: 5m close below 2,262.49: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.79R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$4.24-$5.08); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
