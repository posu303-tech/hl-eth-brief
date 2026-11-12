# ETH perp (Hyperliquid) - 2026-11-12 06:56 UTC+05:30 (01:26 UTC)
spot 2,049.55 | mark 2,049.55 | oracle 2,050.49 | OI 768,409.38 ETH (-0.115% vs last run, +0.87% 24h)
funding +0.00098%/hr (~+8.60%/yr, 41th pct of last 500h) | 24h notional $715.8m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,081.45 / 2,174.79) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 30% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 41th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +0.9%, price -0.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,004.00 | POC 2,124.50 | VAH 2,279.00 (width 275.00 = 13.42% of spot, 240 bars)
- developing session (6% elapsed): VAL 2,055.00 | POC 2,061.50 | VAH 2,065.00
- session VWAP 2,058.24 (+1s 2,062.46 / -1s 2,054.02) | prior session VWAP 2,066.33
- prior day: PDH 2,103.00 | PDL 2,034.70 | PDC 2,055.50 (PDH intact, PDL intact)
- floor pivots: S3 1,957.50 | S2 1,996.10 | S1 2,025.80 | P 2,064.40 | R1 2,094.10 | R2 2,132.70 | R3 2,162.40
- 1H ATR(14) 17.96 = 0.88% of spot | ATR vs 30d median x0.96
- distance to POC -4.17 ATR | VAH -12.77 ATR | VAL +2.54 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00084%/hr, BybitPerp +0.00072%/hr, HlPerp +0.00098%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,004.00; enter on the reclaim
- entry 2,004.00 | stop 1,995.02 | T1 2,124.50 | T2 2,279.00
- R:R 13.42 at T1, 30.62 at T2 | risk 8.98
- invalid: 5m close below 1,995.02: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 13.42R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,279.00 while still inside value; buy the confirmation, not the poke
- entry 2,280.80 | stop 2,270.02 | T1 2,555.80 | T2 2,313.13
- R:R 25.51 at T1, 3.00 at T2 | risk 10.78
- invalid: 1H close back below 2,279.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 25.51R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,058.24 or pivot support near 2,025.80; buy the hold, not the touch
- entry 2,025.80 | stop 2,015.02 | T1 2,061.73 | T2 2,094.10
- R:R 3.33 at T1, 6.34 at T2 | risk 10.78
- invalid: 5m close below 2,015.02: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$8.98-$10.78); funding runs +0.0236%/day ($+0.10/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
