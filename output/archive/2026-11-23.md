# ETH perp (Hyperliquid) - 2026-11-24 02:39 UTC+05:30 (21:09 UTC)
spot 1,726.05 | mark 1,726.40 | oracle 1,727.44 | OI 607,276.15 ETH (-0.375% vs last run, -1.56% 24h)
funding -0.00078%/hr (~-6.83%/yr, 6th pct of last 500h) | 24h notional $1,386.1m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,720.08 / 1,768.69) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 91% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 6th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.6%, price +0.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,627.50 | POC 1,816.25 | VAH 1,857.00 (width 229.50 = 13.30% of spot, 240 bars)
- developing session (88% elapsed): VAL 1,712.50 | POC 1,723.75 | VAH 1,792.00
- session VWAP 1,766.56 (+1s 1,800.39 / -1s 1,732.74) | prior session VWAP 1,698.66
- prior day: PDH 1,731.00 | PDL 1,647.60 | PDC 1,723.50 (PDH swept, PDL intact)
- floor pivots: S3 1,587.00 | S2 1,617.30 | S1 1,670.40 | P 1,700.70 | R1 1,753.80 | R2 1,784.10 | R3 1,837.20
- 1H ATR(14) 24.57 = 1.42% of spot | ATR vs 30d median x1.52
- distance to POC -3.67 ATR | VAH -5.33 ATR | VAL +4.01 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00085%/hr, BybitPerp -0.00077%/hr, HlPerp -0.00072%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,627.50; enter on the reclaim
- entry 1,627.50 | stop 1,615.22 | T1 1,816.25 | T2 1,857.00
- R:R 15.36 at T1, 18.68 at T2 | risk 12.28
- invalid: 5m close below 1,615.22: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 15.36R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,857.00 while still inside value; buy the confirmation, not the poke
- entry 1,859.46 | stop 1,844.72 | T1 2,088.96 | T2 1,903.68
- R:R 15.57 at T1, 3.00 at T2 | risk 14.74
- invalid: 1H close back below 1,857.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 15.57R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,766.56 or pivot support near 1,700.70; buy the hold, not the touch
- entry 1,700.70 | stop 1,685.96 | T1 1,731.00 | T2 1,749.84
- R:R 2.06 at T1, 3.33 at T2 | risk 14.74
- invalid: 5m close below 1,685.96: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.06R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$12.28-$14.74); funding runs -0.0187%/day ($-0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
