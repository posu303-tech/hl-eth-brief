# ETH perp (Hyperliquid) - 2026-10-28 02:42 UTC+05:30 (21:12 UTC)
spot 2,344.35 | mark 2,344.20 | oracle 2,345.03 | OI 1,133,394.24 ETH (+1.256% vs last run, +1.15% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $706.5m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,330.56 / 2,372.69) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +1.1% with price +1.7%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,336.00 | POC 2,400.50 | VAH 2,459.00 (width 123.00 = 5.25% of spot, 240 bars)
- developing session (88% elapsed): VAL 2,304.00 | POC 2,327.50 | VAH 2,336.00
- session VWAP 2,327.06 (+1s 2,340.59 / -1s 2,313.53) | prior session VWAP 2,318.19
- prior day: PDH 2,344.40 | PDL 2,292.60 | PDC 2,323.40 (PDH swept, PDL intact)
- floor pivots: S3 2,244.07 | S2 2,268.33 | S1 2,295.87 | P 2,320.13 | R1 2,347.67 | R2 2,371.93 | R3 2,399.47
- 1H ATR(14) 15.01 = 0.64% of spot | ATR vs 30d median x0.92
- distance to POC -3.74 ATR | VAH -7.64 ATR | VAL +0.56 ATR | closes outside value (last 20): 70%
- cross-venue funding: BinPerp +0.00107%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,336.00; enter on the reclaim
- entry 2,336.00 | stop 2,328.49 | T1 2,400.50 | T2 2,459.00
- R:R 8.59 at T1, 16.39 at T2 | risk 7.51
- invalid: 5m close below 2,328.49: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 8.59R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,459.00 while still inside value; buy the confirmation, not the poke
- entry 2,460.50 | stop 2,451.49 | T1 2,583.50 | T2 2,487.52
- R:R 13.66 at T1, 3.00 at T2 | risk 9.01
- invalid: 1H close back below 2,459.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 13.66R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,327.06 or pivot support near 2,327.06; buy the hold, not the touch
- entry 2,327.06 | stop 2,318.05 | T1 2,340.59 | T2 2,347.67
- R:R 1.50 at T1, 2.29 at T2 | risk 9.01
- invalid: 5m close below 2,318.05: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.50R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.51-$9.01); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
