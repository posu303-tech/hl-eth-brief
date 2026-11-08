# ETH perp (Hyperliquid) - 2026-11-08 05:52 UTC+05:30 (00:22 UTC)
spot 2,238.05 | mark 2,238.00 | oracle 2,238.98 | OI 977,558.41 ETH (+0.669% vs last run, -0.02% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $185.3m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,251.77 / 2,284.87) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -0.0%, price -0.1%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,314.00 (width 98.00 = 4.38% of spot, 240 bars)
- developing session (2% elapsed): VAL 2,237.00 | POC 2,237.50 | VAH 2,239.00
- session VWAP 2,237.78 (+1s 2,238.33 / -1s 2,237.23) | prior session VWAP 2,237.95
- prior day: PDH 2,251.00 | PDL 2,223.00 | PDC 2,239.50 (PDH intact, PDL intact)
- floor pivots: S3 2,196.67 | S2 2,209.83 | S1 2,224.67 | P 2,237.83 | R1 2,252.67 | R2 2,265.83 | R3 2,280.67
- 1H ATR(14) 8.57 = 0.38% of spot | ATR vs 30d median x0.75
- distance to POC -1.22 ATR | VAH -8.87 ATR | VAL +2.57 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00052%/hr, BybitPerp +0.00072%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,211.72 | T1 2,248.50 | T2 2,314.00
- R:R 7.59 at T1, 22.88 at T2 | risk 4.28
- invalid: 5m close below 2,211.72: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 7.59R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 2,216.00 while still inside value; sell the confirmation, not the poke
- entry 2,215.14 | stop 2,220.28 | T1 2,209.83 | T2 2,196.67
- R:R 1.03 at T1, 3.60 at T2 | risk 5.14
- invalid: 1H close back above 2,216.00: the expansion failed, mirror the long at VAH
- verdict: STAND ASIDE - T1 pays 1.03R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,237.78 or pivot resistance near 2,252.67; sell the rejection, not the touch
- entry 2,252.67 | stop 2,257.81 | T1 2,248.50 | T2 2,237.23
- R:R 0.81 at T1, 3.00 at T2 | risk 5.14
- invalid: 5m close above 2,257.81: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.81R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.50x the 1H ATR (~$4.28-$4.28); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
