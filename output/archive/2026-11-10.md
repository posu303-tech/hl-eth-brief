# ETH perp (Hyperliquid) - 2026-11-10 05:36 UTC+05:30 (00:06 UTC)
spot 2,132.95 | mark 2,132.90 | oracle 2,134.02 | OI 789,397.82 ETH (-4.900% vs last run, -14.05% 24h)
funding +0.00010%/hr (~+0.86%/yr, 17th pct of last 500h) | 24h notional $1,227.0m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,166.15 / 2,240.29) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 68% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 17th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -14.0%, price -0.1%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,206.00 | POC 2,244.50 | VAH 2,428.00 (width 222.00 = 10.41% of spot, 240 bars)
- session VWAP 2,132.97 (+1s 2,132.97 / -1s 2,132.97) | prior session VWAP 2,123.93
- prior day: PDH 2,159.00 | PDL 2,081.40 | PDC 2,133.90 (PDH intact, PDL intact)
- floor pivots: S3 2,012.93 | S2 2,047.17 | S1 2,090.53 | P 2,124.77 | R1 2,168.13 | R2 2,202.37 | R3 2,245.73
- 1H ATR(14) 18.90 = 0.89% of spot | ATR vs 30d median x0.86
- distance to POC -5.90 ATR | VAH -15.61 ATR | VAL -3.87 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00081%/hr, BybitPerp -0.00018%/hr, HlPerp +0.00011%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.9 ATR below VAL 2,206.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,206.00 | stop 2,071.95 | T1 2,244.50 | T2 2,428.00
- R:R 0.29 at T1, 1.66 at T2 | risk 134.05
- invalid: 5m close below 2,071.95: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.29R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.9 ATR below VAL 2,206.00; short the retest that fails at it
- entry 2,206.00 | stop 2,220.17 | T1 2,090.53 | T2 2,081.40
- R:R 8.15 at T1, 8.79 at T2 | risk 14.17
- invalid: 1H close back inside value (above 2,206.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 8.15R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,132.97 or pivot support near 2,124.77; buy the hold, not the touch
- entry 2,124.77 | stop 2,113.43 | T1 2,132.97 | T2 2,159.00
- R:R 0.72 at T1, 3.02 at T2 | risk 11.34
- invalid: 5m close below 2,113.43: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.72R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-0.75x the 1H ATR (~$14.17-$14.17); funding runs +0.0024%/day ($+0.01/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
