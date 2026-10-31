# ETH perp (Hyperliquid) - 2026-10-31 10:47 UTC+05:30 (05:17 UTC)
spot 2,239.45 | mark 2,239.50 | oracle 2,240.48 | OI 987,143.02 ETH (-0.181% vs last run, -6.19% 24h)
funding +0.00103%/hr (~+9.06%/yr, 37th pct of last 500h) | 24h notional $1,019.3m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,264.17 / 2,326.28) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 37th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -6.2%, price -0.3%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,251.00 | POC 2,326.50 | VAH 2,413.00 (width 162.00 = 7.23% of spot, 240 bars)
- developing session (22% elapsed): VAL 2,238.00 | POC 2,239.50 | VAH 2,247.00
- session VWAP 2,243.35 (+1s 2,247.10 / -1s 2,239.60) | prior session VWAP 2,225.15
- prior day: PDH 2,261.00 | PDL 2,173.10 | PDC 2,243.50 (PDH intact, PDL intact)
- floor pivots: S3 2,102.83 | S2 2,137.97 | S1 2,190.73 | P 2,225.87 | R1 2,278.63 | R2 2,313.77 | R3 2,366.53
- 1H ATR(14) 17.03 = 0.76% of spot | ATR vs 30d median x0.66
- distance to POC -5.11 ATR | VAH -10.19 ATR | VAL -0.68 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00148%/hr, BybitPerp -0.00233%/hr, HlPerp +0.00102%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.7 ATR below VAL 2,251.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,251.00 | stop 2,164.58 | T1 2,326.50 | T2 2,413.00
- R:R 0.87 at T1, 1.87 at T2 | risk 86.42
- invalid: 5m close below 2,164.58: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.87R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.7 ATR below VAL 2,251.00; short the retest that fails at it
- entry 2,251.00 | stop 2,263.77 | T1 2,190.73 | T2 2,173.10
- R:R 4.72 at T1, 6.10 at T2 | risk 12.77
- invalid: 1H close back inside value (above 2,251.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 4.72R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,243.35 or pivot support near 2,225.87; buy the hold, not the touch
- entry 2,225.87 | stop 2,215.65 | T1 2,247.10 | T2 2,259.93
- R:R 2.08 at T1, 3.33 at T2 | risk 10.22
- invalid: 5m close below 2,215.65: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.08R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$10.22-$12.77); funding runs +0.0248%/day ($+0.10/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
