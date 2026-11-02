# ETH perp (Hyperliquid) - 2026-11-03 04:55 UTC+05:30 (23:25 UTC)
spot 2,251.45 | mark 2,251.50 | oracle 2,251.92 | OI 958,775.29 ETH (-2.018% vs last run, -1.25% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,031.8m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,269.90 / 2,297.75) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 92% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.3%, price -0.7%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,250.00 | POC 2,326.50 | VAH 2,374.00 (width 124.00 = 5.51% of spot, 240 bars)
- developing session (98% elapsed): VAL 2,245.00 | POC 2,253.50 | VAH 2,291.00
- session VWAP 2,274.50 (+1s 2,293.72 / -1s 2,255.29) | prior session VWAP 2,266.31
- prior day: PDH 2,276.90 | PDL 2,247.90 | PDC 2,274.60 (PDH swept, PDL swept)
- floor pivots: S3 2,227.03 | S2 2,237.47 | S1 2,256.03 | P 2,266.47 | R1 2,285.03 | R2 2,295.47 | R3 2,314.03
- 1H ATR(14) 15.52 = 0.69% of spot | ATR vs 30d median x1.31
- distance to POC -4.84 ATR | VAH -7.90 ATR | VAL +0.09 ATR | closes outside value (last 20): 5%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,250.00; enter on the reclaim
- entry 2,250.00 | stop 2,242.24 | T1 2,326.50 | T2 2,374.00
- R:R 9.86 at T1, 15.98 at T2 | risk 7.76
- invalid: 5m close below 2,242.24: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 9.86R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,374.00 while still inside value; buy the confirmation, not the poke
- entry 2,375.55 | stop 2,366.24 | T1 2,499.55 | T2 2,403.49
- R:R 13.32 at T1, 3.00 at T2 | risk 9.31
- invalid: 1H close back below 2,374.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 13.32R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,274.50 or pivot resistance near 2,266.47; sell the rejection, not the touch
- entry 2,266.47 | stop 2,275.78 | T1 2,256.03 | T2 2,247.90
- R:R 1.12 at T1, 1.99 at T2 | risk 9.31
- invalid: 5m close above 2,275.78: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.12R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.76-$9.31); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
