# ETH perp (Hyperliquid) - 2026-11-03 20:28 UTC+05:30 (14:58 UTC)
spot 2,284.75 | mark 2,284.70 | oracle 2,285.27 | OI 997,062.85 ETH (+3.669% vs last run, +1.89% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $863.6m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,266.48 / 2,292.66) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 21% of prior range | -1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +1.9% with price -0.2%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,254.00 | POC 2,326.50 | VAH 2,369.00 (width 115.00 = 5.03% of spot, 240 bars)
- developing session (62% elapsed): VAL 2,243.00 | POC 2,258.50 | VAH 2,284.00
- session VWAP 2,271.39 (+1s 2,288.59 / -1s 2,254.19) | prior session VWAP 2,272.93
- prior day: PDH 2,315.20 | PDL 2,236.10 | PDC 2,252.50 (PDH intact, PDL intact)
- floor pivots: S3 2,141.57 | S2 2,188.83 | S1 2,220.67 | P 2,267.93 | R1 2,299.77 | R2 2,347.03 | R3 2,378.87
- 1H ATR(14) 15.09 = 0.66% of spot | ATR vs 30d median x1.09
- distance to POC -2.77 ATR | VAH -5.58 ATR | VAL +2.04 ATR | closes outside value (last 20): 40%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00102%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,254.00; enter on the reclaim
- entry 2,254.00 | stop 2,246.45 | T1 2,326.50 | T2 2,369.00
- R:R 9.61 at T1, 15.24 at T2 | risk 7.55
- invalid: 5m close below 2,246.45: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 9.61R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,369.00 while still inside value; buy the confirmation, not the poke
- entry 2,370.51 | stop 2,361.45 | T1 2,378.87 | T2 2,485.51
- R:R 0.92 at T1, 12.70 at T2 | risk 9.05
- invalid: 1H close back below 2,369.00: the expansion failed, mirror the short at VAL
- verdict: STAND ASIDE - T1 pays 0.92R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,271.39 or pivot support near 2,271.39; buy the hold, not the touch
- entry 2,271.39 | stop 2,262.33 | T1 2,288.59 | T2 2,299.77
- R:R 1.90 at T1, 3.13 at T2 | risk 9.05
- invalid: 5m close below 2,262.33: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.90R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.55-$9.05); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
