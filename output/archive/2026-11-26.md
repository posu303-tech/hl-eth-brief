# ETH perp (Hyperliquid) - 2026-11-26 20:26 UTC+05:30 (14:56 UTC)
spot 1,699.25 | mark 1,698.90 | oracle 1,699.65 | OI 655,741.74 ETH (+2.326% vs last run, 24h n/a until the store has a day)
funding +0.00082%/hr (~+7.19%/yr, 36th pct of last 500h) | 24h notional $804.1m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,686.26 / 1,727.00) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 93% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 36th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,657.50 | POC 1,683.75 | VAH 1,832.00 (width 174.50 = 10.27% of spot, 240 bars)
- developing session (62% elapsed): VAL 1,693.50 | POC 1,703.25 | VAH 1,710.00
- session VWAP 1,702.60 (+1s 1,710.56 / -1s 1,694.64) | prior session VWAP 1,653.73
- prior day: PDH 1,698.00 | PDL 1,607.40 | PDC 1,691.90 (PDH swept, PDL intact)
- floor pivots: S3 1,542.93 | S2 1,575.17 | S1 1,633.53 | P 1,665.77 | R1 1,724.13 | R2 1,756.37 | R3 1,814.73
- 1H ATR(14) 14.41 = 0.85% of spot | ATR vs 30d median x0.79
- distance to POC +1.08 ATR | VAH -9.21 ATR | VAL +2.90 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00035%/hr, BybitPerp +0.00068%/hr, HlPerp +0.00080%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (short from VAH)** [SHORT]
- trigger: 5m close back inside value after tagging VAH 1,832.00; enter on the loss of the edge
- entry 1,832.00 | stop 1,839.21 | T1 1,683.75 | T2 1,657.50
- R:R 20.57 at T1, 24.21 at T2 | risk 7.21
- invalid: 5m close above 1,839.21: acceptance higher, stand down
- verdict: valid only if the trigger prints (T1 20.57R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,832.00 while still inside value; buy the confirmation, not the poke
- entry 1,833.44 | stop 1,824.79 | T1 2,007.94 | T2 1,859.39
- R:R 20.18 at T1, 3.00 at T2 | risk 8.65
- invalid: 1H close back below 1,832.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 20.18R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,702.60 or pivot support near 1,665.77; buy the hold, not the touch
- entry 1,665.77 | stop 1,657.12 | T1 1,683.75 | T2 1,694.59
- R:R 2.08 at T1, 3.33 at T2 | risk 8.65
- invalid: 5m close below 1,657.12: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.08R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.21-$8.65); funding runs +0.0197%/day ($+0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
