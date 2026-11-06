# ETH perp (Hyperliquid) - 2026-11-06 06:58 UTC+05:30 (01:28 UTC)
spot 2,234.85 | mark 2,235.10 | oracle 2,235.80 | OI 959,533.79 ETH (+0.848% vs last run, -6.25% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,530.7m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,326.52 / 2,313.08) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 14% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -6.2%, price -7.4%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,220.00 | POC 2,251.50 | VAH 2,336.00 (width 116.00 = 5.19% of spot, 240 bars)
- developing session (6% elapsed): VAL 2,239.00 | POC 2,240.50 | VAH 2,247.00
- session VWAP 2,242.11 (+1s 2,245.76 / -1s 2,238.46) | prior session VWAP 2,301.79
- prior day: PDH 2,436.10 | PDL 2,205.40 | PDC 2,237.10 (PDH intact, PDL intact)
- floor pivots: S3 1,918.93 | S2 2,062.17 | S1 2,149.63 | P 2,292.87 | R1 2,380.33 | R2 2,523.57 | R3 2,611.03
- 1H ATR(14) 25.41 = 1.14% of spot | ATR vs 30d median x1.17
- distance to POC -0.66 ATR | VAH -3.98 ATR | VAL +0.58 ATR | closes outside value (last 20): 50%
- cross-venue funding: BinPerp +0.00111%/hr, BybitPerp -0.00001%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,220.00; enter on the reclaim
- entry 2,220.00 | stop 2,207.30 | T1 2,251.50 | T2 2,336.00
- R:R 2.48 at T1, 9.13 at T2 | risk 12.70
- invalid: 5m close below 2,207.30: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 2.48R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 2,220.00 while still inside value; sell the confirmation, not the poke
- entry 2,217.46 | stop 2,232.70 | T1 2,205.40 | T2 2,149.63
- R:R 0.79 at T1, 4.45 at T2 | risk 15.25
- invalid: 1H close back above 2,220.00: the expansion failed, mirror the long at VAH
- verdict: STAND ASIDE - T1 pays 0.79R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,242.11 or pivot resistance near 2,242.11; sell the rejection, not the touch
- entry 2,242.11 | stop 2,257.35 | T1 2,220.00 | T2 2,205.40
- R:R 1.45 at T1, 2.41 at T2 | risk 15.25
- invalid: 5m close above 2,257.35: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.45R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.50x the 1H ATR (~$12.70-$12.70); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
