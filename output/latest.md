# ETH perp (Hyperliquid) - 2026-11-16 14:54 UTC+05:30 (09:24 UTC)
spot 1,796.95 | mark 1,796.60 | oracle 1,797.70 | OI 609,795.06 ETH (+4.377% vs last run, +0.67% 24h)
funding -0.00204%/hr (~-17.85%/yr, 2th pct of last 500h) | 24h notional $678.8m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,837.66 / 1,983.86) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 93% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 2th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +0.7%, price -1.9%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,831.00 | POC 2,124.25 | VAH 2,166.00 (width 335.00 = 18.64% of spot, 240 bars)
- developing session (39% elapsed): VAL 1,809.50 | POC 1,821.25 | VAH 1,827.00
- session VWAP 1,815.81 (+1s 1,823.95 / -1s 1,807.67) | prior session VWAP 1,795.75
- prior day: PDH 1,844.00 | PDL 1,710.30 | PDC 1,834.40 (PDH intact, PDL intact)
- floor pivots: S3 1,614.77 | S2 1,662.53 | S1 1,748.47 | P 1,796.23 | R1 1,882.17 | R2 1,929.93 | R3 2,015.87
- 1H ATR(14) 20.47 = 1.14% of spot | ATR vs 30d median x0.80
- distance to POC -15.99 ATR | VAH -18.03 ATR | VAL -1.66 ATR | closes outside value (last 20): 95%
- cross-venue funding: BinPerp -0.00031%/hr, BybitPerp -0.00034%/hr, HlPerp -0.00203%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.7 ATR below VAL 1,831.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,831.00 | stop 1,700.07 | T1 2,124.25 | T2 2,166.00
- R:R 2.24 at T1, 2.56 at T2 | risk 130.93
- invalid: 5m close below 1,700.07: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.24R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.7 ATR below VAL 1,831.00; short the retest that fails at it
- entry 1,831.00 | stop 1,846.35 | T1 1,748.47 | T2 1,710.30
- R:R 5.38 at T1, 7.86 at T2 | risk 15.35
- invalid: 1H close back inside value (above 1,831.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 5.38R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,815.81 or pivot support near 1,748.47; buy the hold, not the touch
- entry 1,748.47 | stop 1,736.19 | T1 1,789.40 | T2 1,823.95
- R:R 3.33 at T1, 6.15 at T2 | risk 12.28
- invalid: 5m close below 1,736.19: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-6.40x the 1H ATR (~$12.28-$130.93); funding runs -0.0489%/day ($-0.20/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
