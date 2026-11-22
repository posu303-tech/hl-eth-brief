# ETH perp (Hyperliquid) - 2026-11-22 16:30 UTC+05:30 (11:00 UTC)
spot 1,707.95 | mark 1,708.00 | oracle 1,709.01 | OI 617,725.14 ETH (+4.759% vs last run, +4.09% 24h)
funding -0.00192%/hr (~-16.83%/yr, 3th pct of last 500h) | 24h notional $774.9m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,682.30 / 1,784.69) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 83% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 3th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +4.1% with price +4.1%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,594.50 | POC 1,816.25 | VAH 1,857.50 (width 263.00 = 15.40% of spot, 240 bars)
- developing session (46% elapsed): VAL 1,651.00 | POC 1,685.75 | VAH 1,694.50
- session VWAP 1,684.94 (+1s 1,703.46 / -1s 1,666.42) | prior session VWAP 1,623.20
- prior day: PDH 1,715.30 | PDL 1,536.70 | PDC 1,684.70 (PDH swept, PDL intact)
- floor pivots: S3 1,397.23 | S2 1,466.97 | S1 1,575.83 | P 1,645.57 | R1 1,754.43 | R2 1,824.17 | R3 1,933.03
- 1H ATR(14) 19.02 = 1.11% of spot | ATR vs 30d median x0.79
- distance to POC -5.69 ATR | VAH -7.86 ATR | VAL +5.96 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00023%/hr, BybitPerp +0.00036%/hr, HlPerp -0.00238%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,594.50; enter on the reclaim
- entry 1,594.50 | stop 1,584.99 | T1 1,816.25 | T2 1,857.50
- R:R 23.32 at T1, 27.65 at T2 | risk 9.51
- invalid: 5m close below 1,584.99: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 23.32R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,857.50 while still inside value; buy the confirmation, not the poke
- entry 1,859.40 | stop 1,847.99 | T1 1,933.03 | T2 2,122.40
- R:R 6.45 at T1, 23.04 at T2 | risk 11.41
- invalid: 1H close back below 1,857.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 6.45R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,684.94 or pivot support near 1,684.94; buy the hold, not the touch
- entry 1,684.94 | stop 1,673.53 | T1 1,703.46 | T2 1,715.30
- R:R 1.62 at T1, 2.66 at T2 | risk 11.41
- invalid: 5m close below 1,673.53: the confluence level is lost
- verdict: valid only if the trigger prints (T1 1.62R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.51-$11.41); funding runs -0.0461%/day ($-0.19/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
