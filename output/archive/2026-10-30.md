# ETH perp (Hyperliquid) - 2026-10-30 19:27 UTC+05:30 (13:57 UTC)
spot 2,219.45 | mark 2,219.60 | oracle 2,220.95 | OI 1,034,811.71 ETH (-1.658% vs last run, -8.55% 24h)
funding +0.00052%/hr (~+4.53%/yr, 24th pct of last 500h) | 24h notional $3,253.5m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,287.99 / 2,341.76) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 16% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 24th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -8.6%, price -4.6%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,286.00 | POC 2,326.50 | VAH 2,416.00 (width 130.00 = 5.86% of spot, 240 bars)
- developing session (58% elapsed): VAL 2,200.00 | POC 2,229.50 | VAH 2,237.00
- session VWAP 2,220.35 (+1s 2,235.93 / -1s 2,204.77) | prior session VWAP 2,291.73
- prior day: PDH 2,378.30 | PDL 2,227.20 | PDC 2,251.90 (PDH intact, PDL swept)
- floor pivots: S3 2,042.20 | S2 2,134.70 | S1 2,193.30 | P 2,285.80 | R1 2,344.40 | R2 2,436.90 | R3 2,495.50
- 1H ATR(14) 25.27 = 1.14% of spot | ATR vs 30d median x0.98
- distance to POC -4.24 ATR | VAH -7.78 ATR | VAL -2.63 ATR | closes outside value (last 20): 85%
- cross-venue funding: BinPerp -0.00035%/hr, BybitPerp -0.00073%/hr, HlPerp +0.00053%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.6 ATR below VAL 2,286.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,286.00 | stop 2,206.82 | T1 2,326.50 | T2 2,416.00
- R:R 0.51 at T1, 1.64 at T2 | risk 79.18
- invalid: 5m close below 2,206.82: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.51R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.6 ATR below VAL 2,286.00; short the retest that fails at it
- entry 2,286.00 | stop 2,304.95 | T1 2,227.20 | T2 2,193.30
- R:R 3.10 at T1, 4.89 at T2 | risk 18.95
- invalid: 1H close back inside value (above 2,286.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.10R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,220.35 or pivot resistance near 2,285.80; sell the rejection, not the touch
- entry 2,285.80 | stop 2,300.96 | T1 2,235.26 | T2 2,204.77
- R:R 3.33 at T1, 5.34 at T2 | risk 15.16
- invalid: 5m close above 2,300.96: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$15.16-$18.95); funding runs +0.0124%/day ($+0.05/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
