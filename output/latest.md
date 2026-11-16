# ETH perp (Hyperliquid) - 2026-11-16 07:17 UTC+05:30 (01:47 UTC)
spot 1,807.05 | mark 1,807.26 | oracle 1,808.29 | OI 584,221.54 ETH (-0.585% vs last run, -9.07% 24h)
funding -0.00018%/hr (~-1.62%/yr, 7th pct of last 500h) | 24h notional $1,156.1m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,845.99 / 1,997.87) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 93% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 7th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -9.1%, price +5.5%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,831.00 | POC 2,124.25 | VAH 2,166.00 (width 335.00 = 18.54% of spot, 240 bars)
- developing session (7% elapsed): VAL 1,810.50 | POC 1,823.25 | VAH 1,831.50
- session VWAP 1,818.04 (+1s 1,826.06 / -1s 1,810.01) | prior session VWAP 1,795.75
- prior day: PDH 1,844.00 | PDL 1,710.30 | PDC 1,834.40 (PDH intact, PDL intact)
- floor pivots: S3 1,614.77 | S2 1,662.53 | S1 1,748.47 | P 1,796.23 | R1 1,882.17 | R2 1,929.93 | R3 2,015.87
- 1H ATR(14) 23.24 = 1.29% of spot | ATR vs 30d median x0.82
- distance to POC -13.65 ATR | VAH -15.44 ATR | VAL -1.03 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp -0.00060%/hr, BybitPerp -0.00050%/hr, HlPerp -0.00017%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.0 ATR below VAL 1,831.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,831.00 | stop 1,698.68 | T1 2,124.25 | T2 2,166.00
- R:R 2.22 at T1, 2.53 at T2 | risk 132.32
- invalid: 5m close below 1,698.68: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.22R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.0 ATR below VAL 1,831.00; short the retest that fails at it
- entry 1,831.00 | stop 1,848.43 | T1 1,748.47 | T2 1,710.30
- R:R 4.73 at T1, 6.92 at T2 | risk 17.43
- invalid: 1H close back inside value (above 1,831.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 4.73R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,818.04 or pivot support near 1,796.23; buy the hold, not the touch
- entry 1,796.23 | stop 1,782.29 | T1 1,826.06 | T2 1,842.72
- R:R 2.14 at T1, 3.33 at T2 | risk 13.95
- invalid: 5m close below 1,782.29: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.14R)

## 4) Risk note
Stops sit 0.60-5.69x the 1H ATR (~$13.95-$132.32); funding runs -0.0044%/day ($-0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
