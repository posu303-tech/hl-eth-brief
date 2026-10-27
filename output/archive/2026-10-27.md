# ETH perp (Hyperliquid) - 2026-10-27 09:55 UTC+05:30 (04:25 UTC)
spot 2,312.15 | mark 2,312.20 | oracle 2,313.20 | OI 1,117,709.60 ETH (-0.374% vs last run, +1.21% 24h)
funding +0.00040%/hr (~+3.49%/yr, 19th pct of last 500h) | 24h notional $743.1m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,330.89 / 2,380.95) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 19th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +1.2% with price +0.1%: new longs | +1 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,336.00 | POC 2,400.50 | VAH 2,459.00 (width 123.00 = 5.32% of spot, 240 bars)
- developing session (18% elapsed): VAL 2,320.00 | POC 2,327.50 | VAH 2,330.00
- session VWAP 2,323.53 (+1s 2,328.46 / -1s 2,318.60) | prior session VWAP 2,318.19
- prior day: PDH 2,344.40 | PDL 2,292.60 | PDC 2,323.40 (PDH intact, PDL intact)
- floor pivots: S3 2,244.07 | S2 2,268.33 | S1 2,295.87 | P 2,320.13 | R1 2,347.67 | R2 2,371.93 | R3 2,399.47
- 1H ATR(14) 15.71 = 0.68% of spot | ATR vs 30d median x0.91
- distance to POC -5.62 ATR | VAH -9.35 ATR | VAL -1.52 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00104%/hr, BybitPerp +0.00011%/hr, HlPerp +0.00040%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.5 ATR below VAL 2,336.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,336.00 | stop 2,284.74 | T1 2,400.50 | T2 2,459.00
- R:R 1.26 at T1, 2.40 at T2 | risk 51.26
- invalid: 5m close below 2,284.74: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 1.26R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.5 ATR below VAL 2,336.00; short the retest that fails at it
- entry 2,336.00 | stop 2,347.78 | T1 2,295.87 | T2 2,268.33
- R:R 3.41 at T1, 5.74 at T2 | risk 11.78
- invalid: 1H close back inside value (above 2,336.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.41R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,323.53 or pivot support near 2,295.87; buy the hold, not the touch
- entry 2,295.87 | stop 2,286.44 | T1 2,327.29 | T2 2,344.40
- R:R 3.33 at T1, 5.15 at T2 | risk 9.43
- invalid: 5m close below 2,286.44: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$9.43-$11.78); funding runs +0.0096%/day ($+0.04/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
