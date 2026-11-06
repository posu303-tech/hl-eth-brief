# ETH perp (Hyperliquid) - 2026-11-06 14:43 UTC+05:30 (09:13 UTC)
spot 2,240.05 | mark 2,239.60 | oracle 2,240.48 | OI 969,484.70 ETH (+1.037% vs last run, -6.30% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,535.1m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,300.55 / 2,306.85) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 14% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -6.3%, price -7.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,220.00 | POC 2,251.50 | VAH 2,336.00 (width 116.00 = 5.18% of spot, 240 bars)
- developing session (38% elapsed): VAL 2,227.00 | POC 2,240.50 | VAH 2,246.00
- session VWAP 2,233.23 (+1s 2,241.05 / -1s 2,225.41) | prior session VWAP 2,301.79
- prior day: PDH 2,436.10 | PDL 2,205.40 | PDC 2,237.10 (PDH intact, PDL intact)
- floor pivots: S3 1,918.93 | S2 2,062.17 | S1 2,149.63 | P 2,292.87 | R1 2,380.33 | R2 2,523.57 | R3 2,611.03
- 1H ATR(14) 21.01 = 0.94% of spot | ATR vs 30d median x0.96
- distance to POC -0.55 ATR | VAH -4.57 ATR | VAL +0.95 ATR | closes outside value (last 20): 10%
- cross-venue funding: BinPerp +0.00043%/hr, BybitPerp -0.00139%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,220.00; enter on the reclaim
- entry 2,220.00 | stop 2,209.50 | T1 2,251.50 | T2 2,336.00
- R:R 3.00 at T1, 11.04 at T2 | risk 10.50
- invalid: 5m close below 2,209.50: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 3.00R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 2,220.00 while still inside value; sell the confirmation, not the poke
- entry 2,217.90 | stop 2,230.50 | T1 2,205.40 | T2 2,149.63
- R:R 0.99 at T1, 5.42 at T2 | risk 12.60
- invalid: 1H close back above 2,220.00: the expansion failed, mirror the long at VAH
- verdict: STAND ASIDE - T1 pays 0.99R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,233.23 or pivot resistance near 2,292.87; sell the rejection, not the touch
- entry 2,292.87 | stop 2,305.47 | T1 2,251.50 | T2 2,225.41
- R:R 3.28 at T1, 5.35 at T2 | risk 12.60
- invalid: 5m close above 2,305.47: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.28R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$10.50-$12.60); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
