# ETH perp (Hyperliquid) - 2026-11-23 14:21 UTC+05:30 (08:51 UTC)
spot 1,724.05 | mark 1,724.10 | oracle 1,725.30 | OI 609,561.67 ETH (-1.188% vs last run, -1.32% 24h)
funding -0.00079%/hr (~-6.95%/yr, 5th pct of last 500h) | 24h notional $589.2m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,702.80 / 1,771.97) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 91% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 5th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.3%, price +2.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,627.50 | POC 1,816.25 | VAH 1,857.00 (width 229.50 = 13.31% of spot, 240 bars)
- developing session (37% elapsed): VAL 1,718.50 | POC 1,731.25 | VAH 1,749.00
- session VWAP 1,725.17 (+1s 1,737.28 / -1s 1,713.06) | prior session VWAP 1,698.66
- prior day: PDH 1,731.00 | PDL 1,647.60 | PDC 1,723.50 (PDH swept, PDL intact)
- floor pivots: S3 1,587.00 | S2 1,617.30 | S1 1,670.40 | P 1,700.70 | R1 1,753.80 | R2 1,784.10 | R3 1,837.20
- 1H ATR(14) 15.47 = 0.90% of spot | ATR vs 30d median x0.91
- distance to POC -5.96 ATR | VAH -8.59 ATR | VAL +6.24 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00061%/hr, BybitPerp -0.00111%/hr, HlPerp -0.00078%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,627.50; enter on the reclaim
- entry 1,627.50 | stop 1,619.76 | T1 1,816.25 | T2 1,857.00
- R:R 24.40 at T1, 29.67 at T2 | risk 7.74
- invalid: 5m close below 1,619.76: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 24.40R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,857.00 while still inside value; buy the confirmation, not the poke
- entry 1,858.55 | stop 1,849.26 | T1 2,088.05 | T2 1,886.40
- R:R 24.72 at T1, 3.00 at T2 | risk 9.28
- invalid: 1H close back below 1,857.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 24.72R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,725.17 or pivot support near 1,700.70; buy the hold, not the touch
- entry 1,700.70 | stop 1,691.42 | T1 1,731.00 | T2 1,737.28
- R:R 3.26 at T1, 3.94 at T2 | risk 9.28
- invalid: 5m close below 1,691.42: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.26R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.74-$9.28); funding runs -0.0190%/day ($-0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
