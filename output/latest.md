# ETH perp (Hyperliquid) - 2026-11-08 12:38 UTC+05:30 (07:08 UTC)
spot 2,233.85 | mark 2,233.80 | oracle 2,234.80 | OI 976,784.99 ETH (-0.079% vs last run, +0.04% 24h)
funding +0.00105%/hr (~+9.21%/yr, 49th pct of last 500h) | 24h notional $195.8m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,247.60 / 2,281.48) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 49th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +0.0%, price -0.5%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,314.00 (width 98.00 = 4.39% of spot, 240 bars)
- developing session (30% elapsed): VAL 2,233.00 | POC 2,233.50 | VAH 2,238.00
- session VWAP 2,234.63 (+1s 2,236.76 / -1s 2,232.49) | prior session VWAP 2,237.95
- prior day: PDH 2,251.00 | PDL 2,223.00 | PDC 2,239.50 (PDH intact, PDL intact)
- floor pivots: S3 2,196.67 | S2 2,209.83 | S1 2,224.67 | P 2,237.83 | R1 2,252.67 | R2 2,265.83 | R3 2,280.67
- 1H ATR(14) 6.97 = 0.31% of spot | ATR vs 30d median x0.71
- distance to POC -2.10 ATR | VAH -11.49 ATR | VAL +2.56 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00098%/hr, HlPerp +0.00104%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,212.51 | T1 2,248.50 | T2 2,314.00
- R:R 9.32 at T1, 28.11 at T2 | risk 3.49
- invalid: 5m close below 2,212.51: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 9.32R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,314.00 while still inside value; buy the confirmation, not the poke
- entry 2,314.70 | stop 2,310.51 | T1 2,412.70 | T2 2,327.25
- R:R 23.42 at T1, 3.00 at T2 | risk 4.18
- invalid: 1H close back below 2,314.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 23.42R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,234.63 or pivot support near 2,224.67; buy the hold, not the touch
- entry 2,224.67 | stop 2,220.48 | T1 2,236.76 | T2 2,248.50
- R:R 2.89 at T1, 5.70 at T2 | risk 4.18
- invalid: 5m close below 2,220.48: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.89R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$3.49-$4.18); funding runs +0.0252%/day ($+0.11/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
