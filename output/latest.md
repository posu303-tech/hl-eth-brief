# ETH perp (Hyperliquid) - 2026-11-04 02:22 UTC+05:30 (20:52 UTC)
spot 2,290.45 | mark 2,290.50 | oracle 2,291.10 | OI 1,008,221.06 ETH (+1.119% vs last run, +5.16% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $624.9m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,272.16 / 2,292.70) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 21% of prior range | -1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +5.2% with price +1.9%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,254.00 | POC 2,326.50 | VAH 2,369.00 (width 115.00 = 5.02% of spot, 240 bars)
- developing session (87% elapsed): VAL 2,265.00 | POC 2,290.50 | VAH 2,309.00
- session VWAP 2,278.94 (+1s 2,295.78 / -1s 2,262.10) | prior session VWAP 2,272.93
- prior day: PDH 2,315.20 | PDL 2,236.10 | PDC 2,252.50 (PDH intact, PDL intact)
- floor pivots: S3 2,141.57 | S2 2,188.83 | S1 2,220.67 | P 2,267.93 | R1 2,299.77 | R2 2,347.03 | R3 2,378.87
- 1H ATR(14) 14.41 = 0.63% of spot | ATR vs 30d median x0.99
- distance to POC -2.50 ATR | VAH -5.45 ATR | VAL +2.53 ATR | closes outside value (last 20): 20%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00070%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,254.00; enter on the reclaim
- entry 2,254.00 | stop 2,246.79 | T1 2,326.50 | T2 2,369.00
- R:R 10.06 at T1, 15.96 at T2 | risk 7.21
- invalid: 5m close below 2,246.79: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.06R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,369.00 while still inside value; buy the confirmation, not the poke
- entry 2,370.44 | stop 2,361.79 | T1 2,378.87 | T2 2,485.44
- R:R 0.97 at T1, 13.30 at T2 | risk 8.65
- invalid: 1H close back below 2,369.00: the expansion failed, mirror the short at VAL
- verdict: STAND ASIDE - T1 pays 0.97R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,278.94 or pivot support near 2,278.94; buy the hold, not the touch
- entry 2,278.94 | stop 2,270.29 | T1 2,295.78 | T2 2,307.76
- R:R 1.95 at T1, 3.33 at T2 | risk 8.65
- invalid: 5m close below 2,270.29: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.95R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.21-$8.65); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
