# ETH perp (Hyperliquid) - 2026-10-31 00:38 UTC+05:30 (19:08 UTC)
spot 2,230.75 | mark 2,230.60 | oracle 2,231.90 | OI 995,300.47 ETH (-3.818% vs last run, -8.19% 24h)
funding -0.00038%/hr (~-3.33%/yr, 6th pct of last 500h) | 24h notional $3,197.7m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,276.06 / 2,335.36) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 16% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 6th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -8.2%, price -4.1%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,286.00 | POC 2,326.50 | VAH 2,416.00 (width 130.00 = 5.83% of spot, 240 bars)
- developing session (80% elapsed): VAL 2,209.00 | POC 2,229.50 | VAH 2,248.00
- session VWAP 2,223.17 (+1s 2,239.02 / -1s 2,207.32) | prior session VWAP 2,291.73
- prior day: PDH 2,378.30 | PDL 2,227.20 | PDC 2,251.90 (PDH intact, PDL swept)
- floor pivots: S3 2,042.20 | S2 2,134.70 | S1 2,193.30 | P 2,285.80 | R1 2,344.40 | R2 2,436.90 | R3 2,495.50
- 1H ATR(14) 25.52 = 1.14% of spot | ATR vs 30d median x0.97
- distance to POC -3.75 ATR | VAH -7.26 ATR | VAL -2.17 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00225%/hr, BybitPerp -0.00192%/hr, HlPerp -0.00042%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.2 ATR below VAL 2,286.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,286.00 | stop 2,214.44 | T1 2,326.50 | T2 2,416.00
- R:R 0.57 at T1, 1.82 at T2 | risk 71.56
- invalid: 5m close below 2,214.44: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.57R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.2 ATR below VAL 2,286.00; short the retest that fails at it
- entry 2,286.00 | stop 2,305.14 | T1 2,227.20 | T2 2,193.30
- R:R 3.07 at T1, 4.84 at T2 | risk 19.14
- invalid: 1H close back inside value (above 2,286.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.07R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,223.17 or pivot support near 2,223.17; buy the hold, not the touch
- entry 2,223.17 | stop 2,207.86 | T1 2,239.02 | T2 2,274.21
- R:R 1.04 at T1, 3.33 at T2 | risk 15.31
- invalid: 5m close below 2,207.86: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.04R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-0.75x the 1H ATR (~$19.14-$19.14); funding runs -0.0091%/day ($-0.04/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
