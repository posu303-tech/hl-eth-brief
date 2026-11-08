# ETH perp (Hyperliquid) - 2026-11-09 05:06 UTC+05:30 (23:36 UTC)
spot 2,142.65 | mark 2,142.60 | oracle 2,144.24 | OI 918,396.51 ETH (-7.006% vs last run, -6.05% 24h)
funding -0.00307%/hr (~-26.92%/yr, 2th pct of last 500h) | 24h notional $1,044.4m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,233.40 / 2,272.53) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 59% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 2th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -6.1%, price -4.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,314.00 (width 98.00 = 4.57% of spot, 240 bars)
- developing session (98% elapsed): VAL 2,059.00 | POC 2,126.50 | VAH 2,177.00
- session VWAP 2,153.65 (+1s 2,198.14 / -1s 2,109.15) | prior session VWAP 2,237.95
- prior day: PDH 2,251.00 | PDL 2,223.00 | PDC 2,239.50 (PDH intact, PDL swept)
- floor pivots: S3 2,196.67 | S2 2,209.83 | S1 2,224.67 | P 2,237.83 | R1 2,252.67 | R2 2,265.83 | R3 2,280.67
- 1H ATR(14) 20.18 = 0.94% of spot | ATR vs 30d median x2.79
- distance to POC -5.25 ATR | VAH -8.49 ATR | VAL -3.64 ATR | closes outside value (last 20): 10%
- cross-venue funding: BinPerp -0.00097%/hr, BybitPerp -0.00054%/hr, HlPerp -0.00306%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.6 ATR below VAL 2,216.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,216.00 | stop 2,132.56 | T1 2,248.50 | T2 2,314.00
- R:R 0.39 at T1, 1.17 at T2 | risk 83.44
- invalid: 5m close below 2,132.56: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.39R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.6 ATR below VAL 2,216.00; short the retest that fails at it
- entry 2,216.00 | stop 2,231.13 | T1 2,196.67 | T2 2,118.00
- R:R 1.28 at T1, 6.48 at T2 | risk 15.13
- invalid: 1H close back inside value (above 2,216.00) voids the acceptance
- verdict: STAND ASIDE - T1 pays 1.28R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,153.65 or pivot resistance near 2,153.65; sell the rejection, not the touch
- entry 2,153.65 | stop 2,165.75 | T1 2,113.30 | T2 2,117.33
- R:R 3.33 at T1, 3.00 at T2 | risk 12.11
- invalid: 5m close above 2,165.75: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.60x the 1H ATR (~$12.11-$12.11); funding runs -0.0737%/day ($-0.31/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
