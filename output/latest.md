# ETH perp (Hyperliquid) - 2026-11-22 08:27 UTC+05:30 (02:57 UTC)
spot 1,669.35 | mark 1,669.40 | oracle 1,670.43 | OI 589,660.96 ETH (+0.656% vs last run, -0.33% 24h)
funding -0.00010%/hr (~-0.91%/yr, 9th pct of last 500h) | 24h notional $1,381.7m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,683.98 / 1,794.81) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 83% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 9th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -0.3%, price +3.1%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,594.50 | POC 1,816.25 | VAH 1,857.50 (width 263.00 = 15.75% of spot, 240 bars)
- developing session (12% elapsed): VAL 1,678.50 | POC 1,685.75 | VAH 1,689.50
- session VWAP 1,681.75 (+1s 1,688.34 / -1s 1,675.16) | prior session VWAP 1,623.20
- prior day: PDH 1,715.30 | PDL 1,536.70 | PDC 1,684.70 (PDH intact, PDL intact)
- floor pivots: S3 1,397.23 | S2 1,466.97 | S1 1,575.83 | P 1,645.57 | R1 1,754.43 | R2 1,824.17 | R3 1,933.03
- 1H ATR(14) 18.36 = 1.10% of spot | ATR vs 30d median x0.67
- distance to POC -8.00 ATR | VAH -10.25 ATR | VAL +4.08 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00002%/hr, BybitPerp +0.00030%/hr, HlPerp -0.00010%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,594.50; enter on the reclaim
- entry 1,594.50 | stop 1,585.32 | T1 1,816.25 | T2 1,857.50
- R:R 24.16 at T1, 28.66 at T2 | risk 9.18
- invalid: 5m close below 1,585.32: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 24.16R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,857.50 while still inside value; buy the confirmation, not the poke
- entry 1,859.34 | stop 1,848.32 | T1 1,933.03 | T2 2,122.34
- R:R 6.69 at T1, 23.88 at T2 | risk 11.01
- invalid: 1H close back below 1,857.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 6.69R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,681.75 or pivot support near 1,645.57; buy the hold, not the touch
- entry 1,645.57 | stop 1,634.55 | T1 1,682.28 | T2 1,715.30
- R:R 3.33 at T1, 6.33 at T2 | risk 11.01
- invalid: 5m close below 1,634.55: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.18-$11.01); funding runs -0.0025%/day ($-0.01/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
