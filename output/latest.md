# ETH perp (Hyperliquid) - 2026-11-23 05:38 UTC+05:30 (00:08 UTC)
spot 1,722.15 | mark 1,722.20 | oracle 1,723.18 | OI 616,888.62 ETH (-0.135% vs last run, +4.62% 24h)
funding -0.00018%/hr (~-1.54%/yr, 8th pct of last 500h) | 24h notional $551.1m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,695.74 / 1,776.19) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 91% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 8th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +4.6% with price +2.2%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,627.50 | POC 1,816.25 | VAH 1,857.00 (width 229.50 = 13.33% of spot, 240 bars)
- session VWAP 1,723.07 (+1s 1,723.07 / -1s 1,723.07) | prior session VWAP 1,698.66
- prior day: PDH 1,731.00 | PDL 1,647.60 | PDC 1,723.50 (PDH intact, PDL intact)
- floor pivots: S3 1,587.00 | S2 1,617.30 | S1 1,670.40 | P 1,700.70 | R1 1,753.80 | R2 1,784.10 | R3 1,837.20
- 1H ATR(14) 14.38 = 0.84% of spot | ATR vs 30d median x0.79
- distance to POC -6.54 ATR | VAH -9.38 ATR | VAL +6.58 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00015%/hr, BybitPerp +0.00086%/hr, HlPerp -0.00015%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,627.50; enter on the reclaim
- entry 1,627.50 | stop 1,620.31 | T1 1,816.25 | T2 1,857.00
- R:R 26.25 at T1, 31.92 at T2 | risk 7.19
- invalid: 5m close below 1,620.31: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 26.25R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,857.00 while still inside value; buy the confirmation, not the poke
- entry 1,858.44 | stop 1,849.81 | T1 2,087.94 | T2 1,884.33
- R:R 26.60 at T1, 3.00 at T2 | risk 8.63
- invalid: 1H close back below 1,857.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 26.60R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,723.07 or pivot support near 1,700.70; buy the hold, not the touch
- entry 1,700.70 | stop 1,692.07 | T1 1,723.07 | T2 1,729.46
- R:R 2.59 at T1, 3.33 at T2 | risk 8.63
- invalid: 5m close below 1,692.07: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.59R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.19-$8.63); funding runs -0.0042%/day ($-0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
