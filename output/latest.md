# ETH perp (Hyperliquid) - 2026-10-31 17:38 UTC+05:30 (12:08 UTC)
spot 2,246.35 | mark 2,246.40 | oracle 2,247.23 | OI 977,875.88 ETH (-0.939% vs last run, -5.50% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $628.1m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,259.04 / 2,320.65) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 80% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -5.5%, price +0.4%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,251.00 | POC 2,326.50 | VAH 2,413.00 (width 162.00 = 7.21% of spot, 240 bars)
- developing session (51% elapsed): VAL 2,240.00 | POC 2,244.50 | VAH 2,248.00
- session VWAP 2,243.45 (+1s 2,246.72 / -1s 2,240.17) | prior session VWAP 2,225.15
- prior day: PDH 2,261.00 | PDL 2,173.10 | PDC 2,243.50 (PDH intact, PDL intact)
- floor pivots: S3 2,102.83 | S2 2,137.97 | S1 2,190.73 | P 2,225.87 | R1 2,278.63 | R2 2,313.77 | R3 2,366.53
- 1H ATR(14) 12.66 = 0.56% of spot | ATR vs 30d median x0.54
- distance to POC -6.33 ATR | VAH -13.17 ATR | VAL -0.37 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00069%/hr, BybitPerp -0.00092%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.4 ATR below VAL 2,251.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,251.00 | stop 2,166.77 | T1 2,326.50 | T2 2,413.00
- R:R 0.90 at T1, 1.92 at T2 | risk 84.23
- invalid: 5m close below 2,166.77: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.90R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.4 ATR below VAL 2,251.00; short the retest that fails at it
- entry 2,251.00 | stop 2,260.49 | T1 2,190.73 | T2 2,173.10
- R:R 6.35 at T1, 8.21 at T2 | risk 9.49
- invalid: 1H close back inside value (above 2,251.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 6.35R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,243.45 or pivot support near 2,243.45; buy the hold, not the touch
- entry 2,243.45 | stop 2,235.85 | T1 2,261.00 | T2 2,268.76
- R:R 2.31 at T1, 3.33 at T2 | risk 7.59
- invalid: 5m close below 2,235.85: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.31R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$7.59-$9.49); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
