# ETH perp (Hyperliquid) - 2026-11-28 15:38 UTC+05:30 (10:08 UTC)
spot 1,650.55 | mark 1,650.50 | oracle 1,651.32 | OI 603,645.02 ETH (+1.853% vs last run, -1.73% 24h)
funding +0.00042%/hr (~+3.65%/yr, 26th pct of last 500h) | 24h notional $727.1m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,681.23 / 1,713.07) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 22% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 26th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -1.7%, price -4.5%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,621.00 | POC 1,683.75 | VAH 1,763.00 (width 142.00 = 8.60% of spot, 240 bars)
- developing session (42% elapsed): VAL 1,653.00 | POC 1,663.75 | VAH 1,670.50
- session VWAP 1,657.84 (+1s 1,664.37 / -1s 1,651.30) | prior session VWAP 1,696.74
- prior day: PDH 1,762.40 | PDL 1,633.00 | PDC 1,661.80 (PDH intact, PDL intact)
- floor pivots: S3 1,479.67 | S2 1,556.33 | S1 1,609.07 | P 1,685.73 | R1 1,738.47 | R2 1,815.13 | R3 1,867.87
- 1H ATR(14) 12.21 = 0.74% of spot | ATR vs 30d median x0.81
- distance to POC -2.72 ATR | VAH -9.21 ATR | VAL +2.42 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00036%/hr, BybitPerp -0.00025%/hr, HlPerp +0.00041%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,621.00; enter on the reclaim
- entry 1,621.00 | stop 1,614.90 | T1 1,683.75 | T2 1,763.00
- R:R 10.28 at T1, 23.26 at T2 | risk 6.10
- invalid: 5m close below 1,614.90: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.28R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,763.00 while still inside value; buy the confirmation, not the poke
- entry 1,764.22 | stop 1,756.90 | T1 1,815.13 | T2 1,867.87
- R:R 6.95 at T1, 14.15 at T2 | risk 7.32
- invalid: 1H close back below 1,763.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 6.95R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,657.84 or pivot support near 1,609.07; buy the hold, not the touch
- entry 1,609.07 | stop 1,601.74 | T1 1,633.48 | T2 1,664.37
- R:R 3.33 at T1, 7.55 at T2 | risk 7.32
- invalid: 5m close below 1,601.74: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$6.10-$7.32); funding runs +0.0100%/day ($+0.04/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
