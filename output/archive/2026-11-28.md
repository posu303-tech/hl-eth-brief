# ETH perp (Hyperliquid) - 2026-11-28 06:54 UTC+05:30 (01:24 UTC)
spot 1,668.05 | mark 1,668.10 | oracle 1,668.88 | OI 592,664.80 ETH (-1.452% vs last run, -11.95% 24h)
funding +0.00094%/hr (~+8.22%/yr, 44th pct of last 500h) | 24h notional $1,081.5m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,690.92 / 1,718.14) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 22% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 44th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -12.0%, price -2.0%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,621.00 | POC 1,683.75 | VAH 1,763.00 (width 142.00 = 8.51% of spot, 240 bars)
- developing session (6% elapsed): VAL 1,662.50 | POC 1,664.25 | VAH 1,666.00
- session VWAP 1,664.41 (+1s 1,666.04 / -1s 1,662.79) | prior session VWAP 1,696.74
- prior day: PDH 1,762.40 | PDL 1,633.00 | PDC 1,661.80 (PDH intact, PDL intact)
- floor pivots: S3 1,479.67 | S2 1,556.33 | S1 1,609.07 | P 1,685.73 | R1 1,738.47 | R2 1,815.13 | R3 1,867.87
- 1H ATR(14) 14.54 = 0.87% of spot | ATR vs 30d median x0.94
- distance to POC -1.08 ATR | VAH -6.53 ATR | VAL +3.24 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00085%/hr, BybitPerp +0.00003%/hr, HlPerp +0.00094%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,621.00; enter on the reclaim
- entry 1,621.00 | stop 1,613.73 | T1 1,683.75 | T2 1,763.00
- R:R 8.63 at T1, 19.54 at T2 | risk 7.27
- invalid: 5m close below 1,613.73: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 8.63R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,621.00 while still inside value; sell the confirmation, not the poke
- entry 1,619.55 | stop 1,628.27 | T1 1,609.07 | T2 1,556.33
- R:R 1.20 at T1, 7.25 at T2 | risk 8.72
- invalid: 1H close back above 1,621.00: the expansion failed, mirror the long at VAH
- verdict: STAND ASIDE - T1 pays 1.20R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,664.41 or pivot resistance near 1,685.73; sell the rejection, not the touch
- entry 1,685.73 | stop 1,694.46 | T1 1,662.79 | T2 1,656.66
- R:R 2.63 at T1, 3.33 at T2 | risk 8.72
- invalid: 5m close above 1,694.46: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.63R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.27-$8.72); funding runs +0.0225%/day ($+0.09/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
