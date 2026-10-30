# ETH perp (Hyperliquid) - 2026-10-30 12:28 UTC+05:30 (06:58 UTC)
spot 2,252.65 | mark 2,252.70 | oracle 2,254.01 | OI 1,052,255.02 ETH (-4.165% vs last run, -4.01% 24h)
funding -0.00189%/hr (~-16.54%/yr, 0th pct of last 500h) | 24h notional $3,017.9m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,304.36 / 2,349.32) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 16% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 0th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -4.0%, price -2.6%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,286.00 | POC 2,326.50 | VAH 2,416.00 (width 130.00 = 5.77% of spot, 240 bars)
- developing session (29% elapsed): VAL 2,188.00 | POC 2,211.50 | VAH 2,225.00
- session VWAP 2,214.69 (+1s 2,231.12 / -1s 2,198.26) | prior session VWAP 2,291.73
- prior day: PDH 2,378.30 | PDL 2,227.20 | PDC 2,251.90 (PDH intact, PDL swept)
- floor pivots: S3 2,042.20 | S2 2,134.70 | S1 2,193.30 | P 2,285.80 | R1 2,344.40 | R2 2,436.90 | R3 2,495.50
- 1H ATR(14) 29.19 = 1.30% of spot | ATR vs 30d median x1.64
- distance to POC -2.53 ATR | VAH -5.60 ATR | VAL -1.14 ATR | closes outside value (last 20): 50%
- cross-venue funding: BinPerp +0.00019%/hr, BybitPerp -0.00176%/hr, HlPerp -0.00189%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 1.1 ATR below VAL 2,286.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,286.00 | stop 2,212.60 | T1 2,326.50 | T2 2,416.00
- R:R 0.55 at T1, 1.77 at T2 | risk 73.40
- invalid: 5m close below 2,212.60: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.55R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 1.1 ATR below VAL 2,286.00; short the retest that fails at it
- entry 2,286.00 | stop 2,307.90 | T1 2,227.20 | T2 2,193.30
- R:R 2.69 at T1, 4.23 at T2 | risk 21.90
- invalid: 1H close back inside value (above 2,286.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 2.69R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,214.69 or pivot resistance near 2,285.80; sell the rejection, not the touch
- entry 2,285.80 | stop 2,303.32 | T1 2,227.41 | T2 2,198.26
- R:R 3.33 at T1, 5.00 at T2 | risk 17.52
- invalid: 5m close above 2,303.32: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$17.52-$21.90); funding runs -0.0453%/day ($-0.19/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
