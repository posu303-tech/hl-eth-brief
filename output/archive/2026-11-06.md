# ETH perp (Hyperliquid) - 2026-11-07 04:28 UTC+05:30 (22:58 UTC)
spot 2,239.35 | mark 2,239.30 | oracle 2,239.90 | OI 977,766.91 ETH (-1.540% vs last run, +2.76% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $737.1m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,273.60 / 2,298.01) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 14% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +2.8% with price +0.4%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,220.00 | POC 2,251.50 | VAH 2,336.00 (width 116.00 = 5.18% of spot, 240 bars)
- developing session (96% elapsed): VAL 2,222.00 | POC 2,230.50 | VAH 2,242.00
- session VWAP 2,231.74 (+1s 2,239.84 / -1s 2,223.65) | prior session VWAP 2,301.79
- prior day: PDH 2,436.10 | PDL 2,205.40 | PDC 2,237.10 (PDH intact, PDL intact)
- floor pivots: S3 1,918.93 | S2 2,062.17 | S1 2,149.63 | P 2,292.87 | R1 2,380.33 | R2 2,523.57 | R3 2,611.03
- 1H ATR(14) 18.15 = 0.81% of spot | ATR vs 30d median x0.83
- distance to POC -0.67 ATR | VAH -5.33 ATR | VAL +1.07 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00080%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,220.00; enter on the reclaim
- entry 2,220.00 | stop 2,210.93 | T1 2,251.50 | T2 2,336.00
- R:R 3.47 at T1, 12.78 at T2 | risk 9.07
- invalid: 5m close below 2,210.93: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 3.47R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,336.00 while still inside value; buy the confirmation, not the poke
- entry 2,337.81 | stop 2,326.93 | T1 2,380.33 | T2 2,436.10
- R:R 3.91 at T1, 9.03 at T2 | risk 10.89
- invalid: 1H close back below 2,336.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 3.91R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,231.74 or pivot support near 2,231.74; buy the hold, not the touch
- entry 2,231.74 | stop 2,220.86 | T1 2,239.84 | T2 2,251.50
- R:R 0.74 at T1, 1.81 at T2 | risk 10.89
- invalid: 5m close below 2,220.86: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.74R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.07-$10.89); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
