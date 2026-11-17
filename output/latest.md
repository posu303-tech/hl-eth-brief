# ETH perp (Hyperliquid) - 2026-11-17 18:32 UTC+05:30 (13:02 UTC)
spot 1,823.85 | mark 1,823.80 | oracle 1,824.72 | OI 605,440.90 ETH (+0.295% vs last run, -0.71% 24h)
funding +0.00071%/hr (~+6.19%/yr, 20th pct of last 500h) | 24h notional $773.9m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,825.50 / 1,943.63) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 42% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 20th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -0.7%, price +1.4%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,827.75 | VAH 2,060.00 (width 349.50 = 19.16% of spot, 240 bars)
- developing session (54% elapsed): VAL 1,807.50 | POC 1,816.75 | VAH 1,835.50
- session VWAP 1,815.57 (+1s 1,828.43 / -1s 1,802.71) | prior session VWAP 1,820.49
- prior day: PDH 1,866.20 | PDL 1,785.80 | PDC 1,819.90 (PDH intact, PDL swept)
- floor pivots: S3 1,701.33 | S2 1,743.57 | S1 1,781.73 | P 1,823.97 | R1 1,862.13 | R2 1,904.37 | R3 1,942.53
- 1H ATR(14) 18.36 = 1.01% of spot | ATR vs 30d median x0.97
- distance to POC -0.21 ATR | VAH -12.86 ATR | VAL +6.17 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00027%/hr, BybitPerp +0.00017%/hr, HlPerp +0.00056%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,701.32 | T1 1,827.75 | T2 2,060.00
- R:R 12.77 at T1, 38.07 at T2 | risk 9.18
- invalid: 5m close below 1,701.32: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.77R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,060.00 while still inside value; buy the confirmation, not the poke
- entry 2,061.84 | stop 2,050.82 | T1 2,411.34 | T2 2,094.88
- R:R 31.73 at T1, 3.00 at T2 | risk 11.02
- invalid: 1H close back below 2,060.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 31.73R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,815.57 or pivot support near 1,815.57; buy the hold, not the touch
- entry 1,815.57 | stop 1,804.55 | T1 1,827.75 | T2 1,852.29
- R:R 1.11 at T1, 3.33 at T2 | risk 11.02
- invalid: 5m close below 1,804.55: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.11R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.18-$11.02); funding runs +0.0170%/day ($+0.07/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
