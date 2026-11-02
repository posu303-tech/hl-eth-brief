# ETH perp (Hyperliquid) - 2026-11-02 21:02 UTC+05:30 (15:32 UTC)
spot 2,289.35 | mark 2,289.20 | oracle 2,289.67 | OI 978,524.19 ETH (-0.678% vs last run, -0.49% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $655.8m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,274.45 / 2,301.04) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 92% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -0.5%, price +0.9%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,250.00 | POC 2,326.50 | VAH 2,374.00 (width 124.00 = 5.42% of spot, 240 bars)
- developing session (65% elapsed): VAL 2,283.00 | POC 2,290.50 | VAH 2,300.00
- session VWAP 2,291.46 (+1s 2,299.39 / -1s 2,283.53) | prior session VWAP 2,266.31
- prior day: PDH 2,276.90 | PDL 2,247.90 | PDC 2,274.60 (PDH swept, PDL intact)
- floor pivots: S3 2,227.03 | S2 2,237.47 | S1 2,256.03 | P 2,266.47 | R1 2,285.03 | R2 2,295.47 | R3 2,314.03
- 1H ATR(14) 12.90 = 0.56% of spot | ATR vs 30d median x1.38
- distance to POC -2.88 ATR | VAH -6.56 ATR | VAL +3.05 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00044%/hr, BybitPerp +0.00092%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,250.00; enter on the reclaim
- entry 2,250.00 | stop 2,243.55 | T1 2,326.50 | T2 2,374.00
- R:R 11.86 at T1, 19.22 at T2 | risk 6.45
- invalid: 5m close below 2,243.55: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.86R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,374.00 while still inside value; buy the confirmation, not the poke
- entry 2,375.29 | stop 2,367.55 | T1 2,499.29 | T2 2,398.52
- R:R 16.01 at T1, 3.00 at T2 | risk 7.74
- invalid: 1H close back below 2,374.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 16.01R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,291.46 or pivot support near 2,266.47; buy the hold, not the touch
- entry 2,266.47 | stop 2,258.72 | T1 2,276.90 | T2 2,285.03
- R:R 1.35 at T1, 2.40 at T2 | risk 7.74
- invalid: 5m close below 2,258.72: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.35R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$6.45-$7.74); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
