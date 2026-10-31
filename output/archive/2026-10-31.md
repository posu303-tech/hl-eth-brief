# ETH perp (Hyperliquid) - 2026-10-31 23:07 UTC+05:30 (17:37 UTC)
spot 2,250.65 | mark 2,251.00 | oracle 2,251.85 | OI 977,322.13 ETH (-0.057% vs last run, -1.81% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $314.1m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,257.26 / 2,317.17) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -1.8%, price +0.3%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,251.00 | POC 2,326.50 | VAH 2,413.00 (width 162.00 = 7.20% of spot, 240 bars)
- developing session (73% elapsed): VAL 2,241.00 | POC 2,244.50 | VAH 2,251.00
- session VWAP 2,245.02 (+1s 2,248.98 / -1s 2,241.07) | prior session VWAP 2,225.15
- prior day: PDH 2,261.00 | PDL 2,173.10 | PDC 2,243.50 (PDH intact, PDL intact)
- floor pivots: S3 2,102.83 | S2 2,137.97 | S1 2,190.73 | P 2,225.87 | R1 2,278.63 | R2 2,313.77 | R3 2,366.53
- 1H ATR(14) 10.89 = 0.48% of spot | ATR vs 30d median x0.57
- distance to POC -6.97 ATR | VAH -14.91 ATR | VAL -0.03 ATR | closes outside value (last 20): 95%
- cross-venue funding: BinPerp -0.00054%/hr, BybitPerp +0.00003%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.0 ATR below VAL 2,251.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,251.00 | stop 2,167.66 | T1 2,326.50 | T2 2,413.00
- R:R 0.91 at T1, 1.94 at T2 | risk 83.34
- invalid: 5m close below 2,167.66: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.91R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.0 ATR below VAL 2,251.00; short the retest that fails at it
- entry 2,251.00 | stop 2,259.17 | T1 2,190.73 | T2 2,173.10
- R:R 7.38 at T1, 9.54 at T2 | risk 8.17
- invalid: 1H close back inside value (above 2,251.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 7.38R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,245.02 or pivot support near 2,245.02; buy the hold, not the touch
- entry 2,245.02 | stop 2,238.49 | T1 2,261.00 | T2 2,266.80
- R:R 2.45 at T1, 3.33 at T2 | risk 6.53
- invalid: 5m close below 2,238.49: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.45R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$6.53-$8.17); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
