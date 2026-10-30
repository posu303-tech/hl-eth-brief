# ETH perp (Hyperliquid) - 2026-10-31 05:06 UTC+05:30 (23:36 UTC)
spot 2,244.15 | mark 2,244.20 | oracle 2,245.10 | OI 988,934.99 ETH (-0.640% vs last run, -9.93% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,783.6m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,270.18 / 2,331.48) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 16% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -9.9%, price -0.7%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,286.00 | POC 2,326.50 | VAH 2,416.00 (width 130.00 = 5.79% of spot, 240 bars)
- developing session (98% elapsed): VAL 2,210.00 | POC 2,229.50 | VAH 2,248.00
- session VWAP 2,223.76 (+1s 2,239.47 / -1s 2,208.05) | prior session VWAP 2,291.73
- prior day: PDH 2,378.30 | PDL 2,227.20 | PDC 2,251.90 (PDH intact, PDL swept)
- floor pivots: S3 2,042.20 | S2 2,134.70 | S1 2,193.30 | P 2,285.80 | R1 2,344.40 | R2 2,436.90 | R3 2,495.50
- 1H ATR(14) 22.26 = 0.99% of spot | ATR vs 30d median x0.85
- distance to POC -3.70 ATR | VAH -7.72 ATR | VAL -1.88 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00187%/hr, BybitPerp -0.00156%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.9 ATR below VAL 2,286.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,286.00 | stop 2,216.07 | T1 2,326.50 | T2 2,416.00
- R:R 0.58 at T1, 1.86 at T2 | risk 69.93
- invalid: 5m close below 2,216.07: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.58R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.9 ATR below VAL 2,286.00; short the retest that fails at it
- entry 2,286.00 | stop 2,302.70 | T1 2,227.20 | T2 2,193.30
- R:R 3.52 at T1, 5.55 at T2 | risk 16.70
- invalid: 1H close back inside value (above 2,286.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.52R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,223.76 or pivot resistance near 2,285.80; sell the rejection, not the touch
- entry 2,285.80 | stop 2,299.16 | T1 2,241.28 | T2 2,227.20
- R:R 3.33 at T1, 4.39 at T2 | risk 13.36
- invalid: 5m close above 2,299.16: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$13.36-$16.70); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
