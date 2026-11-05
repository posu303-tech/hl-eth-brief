# ETH perp (Hyperliquid) - 2026-11-06 02:04 UTC+05:30 (20:34 UTC)
spot 2,250.75 | mark 2,251.20 | oracle 2,251.90 | OI 951,464.05 ETH (-8.039% vs last run, -7.54% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,396.7m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,346.02 / 2,316.90) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 88% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -7.5%, price -6.9%: no edge | 0 |

## 2) Intraday regime - failed-auction, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,222.00 | POC 2,251.50 | VAH 2,332.00 (width 110.00 = 4.89% of spot, 240 bars)
- developing session (86% elapsed): VAL 2,240.00 | POC 2,251.50 | VAH 2,377.00
- session VWAP 2,323.55 (+1s 2,387.89 / -1s 2,259.21) | prior session VWAP 2,358.22
- prior day: PDH 2,450.00 | PDL 2,225.70 | PDC 2,423.90 (PDH intact, PDL intact)
- floor pivots: S3 2,058.77 | S2 2,142.23 | S1 2,283.07 | P 2,366.53 | R1 2,507.37 | R2 2,590.83 | R3 2,731.67
- 1H ATR(14) 26.20 = 1.16% of spot | ATR vs 30d median x1.22
- distance to POC -0.03 ATR | VAH -3.10 ATR | VAL +1.10 ATR | closes outside value (last 20): 75%
- cross-venue funding: BinPerp +0.00108%/hr, BybitPerp -0.00058%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,222.00; enter on the reclaim
- entry 2,222.00 | stop 2,208.90 | T1 2,251.50 | T2 2,332.00
- R:R 2.25 at T1, 8.40 at T2 | risk 13.10
- invalid: 5m close below 2,208.90: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 2.25R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,332.00 while still inside value; buy the confirmation, not the poke
- entry 2,334.62 | stop 2,318.90 | T1 2,444.62 | T2 2,507.37
- R:R 7.00 at T1, 10.99 at T2 | risk 15.72
- invalid: 1H close back below 2,332.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 7.00R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,323.55 or pivot resistance near 2,323.55; sell the rejection, not the touch
- entry 2,323.55 | stop 2,339.27 | T1 2,283.07 | T2 2,271.16
- R:R 2.58 at T1, 3.33 at T2 | risk 15.72
- invalid: 5m close above 2,339.27: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.58R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$13.10-$15.72); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
