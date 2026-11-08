# ETH perp (Hyperliquid) - 2026-11-08 20:28 UTC+05:30 (14:58 UTC)
spot 2,240.65 | mark 2,240.60 | oracle 2,241.19 | OI 989,567.32 ETH (+1.309% vs last run, +2.27% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $219.0m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,245.21 / 2,278.52) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +2.3% with price -0.2%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,314.00 (width 98.00 = 4.37% of spot, 240 bars)
- developing session (62% elapsed): VAL 2,233.00 | POC 2,239.50 | VAH 2,240.00
- session VWAP 2,237.27 (+1s 2,240.43 / -1s 2,234.11) | prior session VWAP 2,237.95
- prior day: PDH 2,251.00 | PDL 2,223.00 | PDC 2,239.50 (PDH intact, PDL intact)
- floor pivots: S3 2,196.67 | S2 2,209.83 | S1 2,224.67 | P 2,237.83 | R1 2,252.67 | R2 2,265.83 | R3 2,280.67
- 1H ATR(14) 6.64 = 0.30% of spot | ATR vs 30d median x0.77
- distance to POC -1.18 ATR | VAH -11.05 ATR | VAL +3.71 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00067%/hr, BybitPerp +0.00085%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,212.68 | T1 2,248.50 | T2 2,314.00
- R:R 9.79 at T1, 29.52 at T2 | risk 3.32
- invalid: 5m close below 2,212.68: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 9.79R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,314.00 while still inside value; buy the confirmation, not the poke
- entry 2,314.66 | stop 2,310.68 | T1 2,412.66 | T2 2,326.62
- R:R 24.60 at T1, 3.00 at T2 | risk 3.98
- invalid: 1H close back below 2,314.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 24.60R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,237.27 or pivot support near 2,237.83; buy the hold, not the touch
- entry 2,237.83 | stop 2,233.85 | T1 2,248.50 | T2 2,252.67
- R:R 2.68 at T1, 3.72 at T2 | risk 3.98
- invalid: 5m close below 2,233.85: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.68R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$3.32-$3.98); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
