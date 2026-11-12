# ETH perp (Hyperliquid) - 2026-11-12 15:10 UTC+05:30 (09:40 UTC)
spot 2,044.05 | mark 2,044.03 | oracle 2,044.90 | OI 762,555.59 ETH (-0.762% vs last run, -1.46% 24h)
funding +0.00020%/hr (~+1.72%/yr, 16th pct of last 500h) | 24h notional $648.3m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,072.82 / 2,165.20) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 30% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 16th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.5%, price -0.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,004.00 | POC 2,124.50 | VAH 2,279.00 (width 275.00 = 13.45% of spot, 240 bars)
- developing session (40% elapsed): VAL 2,041.00 | POC 2,050.50 | VAH 2,055.00
- session VWAP 2,050.68 (+1s 2,057.00 / -1s 2,044.37) | prior session VWAP 2,066.33
- prior day: PDH 2,103.00 | PDL 2,034.70 | PDC 2,055.50 (PDH intact, PDL intact)
- floor pivots: S3 1,957.50 | S2 1,996.10 | S1 2,025.80 | P 2,064.40 | R1 2,094.10 | R2 2,132.70 | R3 2,162.40
- 1H ATR(14) 14.58 = 0.71% of spot | ATR vs 30d median x0.82
- distance to POC -5.52 ATR | VAH -16.12 ATR | VAL +2.75 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00051%/hr, BybitPerp +0.00069%/hr, HlPerp +0.00018%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,004.00; enter on the reclaim
- entry 2,004.00 | stop 1,996.71 | T1 2,124.50 | T2 2,279.00
- R:R 16.53 at T1, 37.73 at T2 | risk 7.29
- invalid: 5m close below 1,996.71: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 16.53R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,279.00 while still inside value; buy the confirmation, not the poke
- entry 2,280.46 | stop 2,271.71 | T1 2,555.46 | T2 2,306.69
- R:R 31.44 at T1, 3.00 at T2 | risk 8.75
- invalid: 1H close back below 2,279.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 31.44R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,050.68 or pivot support near 2,025.80; buy the hold, not the touch
- entry 2,025.80 | stop 2,017.05 | T1 2,054.95 | T2 2,094.10
- R:R 3.33 at T1, 7.81 at T2 | risk 8.75
- invalid: 5m close below 2,017.05: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.29-$8.75); funding runs +0.0047%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
