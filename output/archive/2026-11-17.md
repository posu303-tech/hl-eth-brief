# ETH perp (Hyperliquid) - 2026-11-18 03:12 UTC+05:30 (21:42 UTC)
spot 1,809.45 | mark 1,809.40 | oracle 1,810.10 | OI 626,287.55 ETH (+3.443% vs last run, +4.52% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $846.9m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,817.28 / 1,932.27) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 42% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +4.5% with price -1.0%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,827.75 | VAH 2,060.00 (width 349.50 = 19.32% of spot, 240 bars)
- developing session (90% elapsed): VAL 1,782.00 | POC 1,787.75 | VAH 1,823.50
- session VWAP 1,799.64 (+1s 1,818.47 / -1s 1,780.82) | prior session VWAP 1,820.49
- prior day: PDH 1,866.20 | PDL 1,785.80 | PDC 1,819.90 (PDH intact, PDL swept)
- floor pivots: S3 1,701.33 | S2 1,743.57 | S1 1,781.73 | P 1,823.97 | R1 1,862.13 | R2 1,904.37 | R3 1,942.53
- 1H ATR(14) 21.13 = 1.17% of spot | ATR vs 30d median x1.09
- distance to POC -0.87 ATR | VAH -11.86 ATR | VAL +4.68 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00067%/hr, BybitPerp +0.00034%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,710.50; enter on the reclaim
- entry 1,710.50 | stop 1,699.93 | T1 1,827.75 | T2 2,060.00
- R:R 11.10 at T1, 33.08 at T2 | risk 10.57
- invalid: 5m close below 1,699.93: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.10R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,710.50 while still inside value; sell the confirmation, not the poke
- entry 1,708.39 | stop 1,721.07 | T1 1,358.89 | T2 1,670.35
- R:R 27.56 at T1, 3.00 at T2 | risk 12.68
- invalid: 1H close back above 1,710.50: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 27.56R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,799.64 or pivot resistance near 1,823.97; sell the rejection, not the touch
- entry 1,823.97 | stop 1,836.65 | T1 1,785.80 | T2 1,710.50
- R:R 3.01 at T1, 8.95 at T2 | risk 12.68
- invalid: 5m close above 1,836.65: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.01R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$10.57-$12.68); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
