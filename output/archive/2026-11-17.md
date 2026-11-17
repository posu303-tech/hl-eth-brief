# ETH perp (Hyperliquid) - 2026-11-17 09:09 UTC+05:30 (03:39 UTC)
spot 1,832.15 | mark 1,832.00 | oracle 1,832.88 | OI 603,657.18 ETH (+0.746% vs last run, +3.33% 24h)
funding +0.00080%/hr (~+6.97%/yr, 23th pct of last 500h) | 24h notional $753.3m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,827.70 / 1,956.46) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 42% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 23th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +3.3% with price +0.5%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,827.75 | VAH 2,060.00 (width 349.50 = 19.08% of spot, 240 bars)
- developing session (15% elapsed): VAL 1,811.50 | POC 1,815.25 | VAH 1,822.00
- session VWAP 1,819.89 (+1s 1,826.32 / -1s 1,813.46) | prior session VWAP 1,820.49
- prior day: PDH 1,866.20 | PDL 1,785.80 | PDC 1,819.90 (PDH intact, PDL intact)
- floor pivots: S3 1,701.33 | S2 1,743.57 | S1 1,781.73 | P 1,823.97 | R1 1,862.13 | R2 1,904.37 | R3 1,942.53
- 1H ATR(14) 18.27 = 1.00% of spot | ATR vs 30d median x0.86
- distance to POC +0.24 ATR | VAH -12.47 ATR | VAL +6.66 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00036%/hr, BybitPerp -0.00059%/hr, HlPerp +0.00081%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (short from VAH)** [SHORT]
- trigger: 5m close back inside value after tagging VAH 2,060.00; enter on the loss of the edge
- entry 2,060.00 | stop 2,069.13 | T1 1,827.75 | T2 1,710.50
- R:R 25.43 at T1, 38.27 at T2 | risk 9.13
- invalid: 5m close above 2,069.13: acceptance higher, stand down
- verdict: valid only if the trigger prints (T1 25.43R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,060.00 while still inside value; buy the confirmation, not the poke
- entry 2,061.83 | stop 2,050.87 | T1 2,411.33 | T2 2,094.71
- R:R 31.89 at T1, 3.00 at T2 | risk 10.96
- invalid: 1H close back below 2,060.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 31.89R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,819.89 or pivot support near 1,823.97; buy the hold, not the touch
- entry 1,823.97 | stop 1,813.01 | T1 1,860.50 | T2 2,060.00
- R:R 3.33 at T1, 21.54 at T2 | risk 10.96
- invalid: 5m close below 1,813.01: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.13-$10.96); funding runs +0.0191%/day ($+0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
