# ETH perp (Hyperliquid) - 2026-11-09 00:58 UTC+05:30 (19:28 UTC)
spot 2,232.05 | mark 2,232.00 | oracle 2,232.90 | OI 987,582.80 ETH (-0.201% vs last run, +1.70% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $207.1m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,243.43 / 2,276.43) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +1.7% with price -0.1%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,314.00 (width 98.00 = 4.39% of spot, 240 bars)
- developing session (81% elapsed): VAL 2,233.00 | POC 2,237.50 | VAH 2,241.00
- session VWAP 2,235.93 (+1s 2,239.98 / -1s 2,231.88) | prior session VWAP 2,237.95
- prior day: PDH 2,251.00 | PDL 2,223.00 | PDC 2,239.50 (PDH intact, PDL intact)
- floor pivots: S3 2,196.67 | S2 2,209.83 | S1 2,224.67 | P 2,237.83 | R1 2,252.67 | R2 2,265.83 | R3 2,280.67
- 1H ATR(14) 7.22 = 0.32% of spot | ATR vs 30d median x0.96
- distance to POC -2.28 ATR | VAH -11.35 ATR | VAL +2.22 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00056%/hr, BybitPerp +0.00075%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,212.39 | T1 2,248.50 | T2 2,314.00
- R:R 9.00 at T1, 27.15 at T2 | risk 3.61
- invalid: 5m close below 2,212.39: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 9.00R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 2,216.00 while still inside value; sell the confirmation, not the poke
- entry 2,215.28 | stop 2,219.61 | T1 2,209.83 | T2 2,196.67
- R:R 1.26 at T1, 4.30 at T2 | risk 4.33
- invalid: 1H close back above 2,216.00: the expansion failed, mirror the long at VAH
- verdict: STAND ASIDE - T1 pays 1.26R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,235.93 or pivot resistance near 2,235.93; sell the rejection, not the touch
- entry 2,235.93 | stop 2,240.26 | T1 2,231.88 | T2 2,224.67
- R:R 0.93 at T1, 2.60 at T2 | risk 4.33
- invalid: 5m close above 2,240.26: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.93R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.50x the 1H ATR (~$3.61-$3.61); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
