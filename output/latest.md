# ETH perp (Hyperliquid) - 2026-11-11 08:10 UTC+05:30 (02:40 UTC)
spot 2,058.65 | mark 2,058.60 | oracle 2,059.50 | OI 761,766.79 ETH (-1.322% vs last run, -3.50% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,381.6m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,104.87 / 2,203.09) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 37% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -3.5%, price -2.8%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,004.00 | POC 2,124.50 | VAH 2,282.00 (width 278.00 = 13.50% of spot, 240 bars)
- developing session (11% elapsed): VAL 2,044.00 | POC 2,049.50 | VAH 2,058.00
- session VWAP 2,053.21 (+1s 2,059.31 / -1s 2,047.11) | prior session VWAP 2,060.93
- prior day: PDH 2,135.80 | PDL 2,003.70 | PDC 2,052.50 (PDH intact, PDL intact)
- floor pivots: S3 1,860.10 | S2 1,931.90 | S1 1,992.20 | P 2,064.00 | R1 2,124.30 | R2 2,196.10 | R3 2,256.40
- 1H ATR(14) 21.59 = 1.05% of spot | ATR vs 30d median x1.08
- distance to POC -3.05 ATR | VAH -10.34 ATR | VAL +2.53 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00036%/hr, BybitPerp +0.00022%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,004.00; enter on the reclaim
- entry 2,004.00 | stop 1,993.20 | T1 2,124.50 | T2 2,282.00
- R:R 11.16 at T1, 25.75 at T2 | risk 10.80
- invalid: 5m close below 1,993.20: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.16R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,282.00 while still inside value; buy the confirmation, not the poke
- entry 2,284.16 | stop 2,271.20 | T1 2,562.16 | T2 2,323.03
- R:R 21.46 at T1, 3.00 at T2 | risk 12.96
- invalid: 1H close back below 2,282.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 21.46R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,053.21 or pivot support near 2,053.21; buy the hold, not the touch
- entry 2,053.21 | stop 2,040.26 | T1 2,096.40 | T2 2,124.30
- R:R 3.33 at T1, 5.49 at T2 | risk 12.96
- invalid: 5m close below 2,040.26: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$10.80-$12.96); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
