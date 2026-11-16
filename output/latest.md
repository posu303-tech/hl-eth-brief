# ETH perp (Hyperliquid) - 2026-11-17 01:44 UTC+05:30 (20:14 UTC)
spot 1,821.40 | mark 1,821.40 | oracle 1,822.30 | OI 599,184.65 ETH (-1.740% vs last run, +1.96% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $847.0m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,830.08 / 1,966.32) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 93% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +2.0% with price +0.3%: new longs | +1 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,831.00 | POC 2,124.25 | VAH 2,166.00 (width 335.00 = 18.39% of spot, 240 bars)
- developing session (84% elapsed): VAL 1,802.50 | POC 1,823.25 | VAH 1,828.50
- session VWAP 1,819.95 (+1s 1,834.26 / -1s 1,805.64) | prior session VWAP 1,795.75
- prior day: PDH 1,844.00 | PDL 1,710.30 | PDC 1,834.40 (PDH swept, PDL intact)
- floor pivots: S3 1,614.77 | S2 1,662.53 | S1 1,748.47 | P 1,796.23 | R1 1,882.17 | R2 1,929.93 | R3 2,015.87
- 1H ATR(14) 21.79 = 1.20% of spot | ATR vs 30d median x0.97
- distance to POC -13.90 ATR | VAH -15.81 ATR | VAL -0.44 ATR | closes outside value (last 20): 95%
- cross-venue funding: BinPerp +0.00021%/hr, BybitPerp +0.00017%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.4 ATR below VAL 1,831.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,831.00 | stop 1,699.40 | T1 2,124.25 | T2 2,166.00
- R:R 2.23 at T1, 2.55 at T2 | risk 131.60
- invalid: 5m close below 1,699.40: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.23R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.4 ATR below VAL 1,831.00; short the retest that fails at it
- entry 1,831.00 | stop 1,847.34 | T1 1,748.47 | T2 1,710.30
- R:R 5.05 at T1, 7.39 at T2 | risk 16.34
- invalid: 1H close back inside value (above 1,831.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 5.05R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,819.95 or pivot support near 1,796.23; buy the hold, not the touch
- entry 1,796.23 | stop 1,783.16 | T1 1,834.26 | T2 1,844.00
- R:R 2.91 at T1, 3.65 at T2 | risk 13.07
- invalid: 5m close below 1,783.16: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.91R)

## 4) Risk note
Stops sit 0.60-6.04x the 1H ATR (~$13.07-$131.60); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
