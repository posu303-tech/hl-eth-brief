# ETH perp (Hyperliquid) - 2026-11-09 21:27 UTC+05:30 (15:57 UTC)
spot 2,146.25 | mark 2,146.10 | oracle 2,146.90 | OI 830,068.56 ETH (-7.948% vs last run, -16.12% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $2,002.5m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,181.21 / 2,250.55) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 36% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -16.1%, price -4.2%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,196.00 | POC 2,244.50 | VAH 2,321.00 (width 125.00 = 5.82% of spot, 240 bars)
- developing session (66% elapsed): VAL 2,109.00 | POC 2,122.50 | VAH 2,147.00
- session VWAP 2,122.02 (+1s 2,138.77 / -1s 2,105.27) | prior session VWAP 2,147.58
- prior day: PDH 2,245.20 | PDL 2,058.50 | PDC 2,125.80 (PDH intact, PDL intact)
- floor pivots: S3 1,854.43 | S2 1,956.47 | S1 2,041.13 | P 2,143.17 | R1 2,227.83 | R2 2,329.87 | R3 2,414.53
- 1H ATR(14) 21.94 = 1.02% of spot | ATR vs 30d median x1.05
- distance to POC -4.48 ATR | VAH -7.97 ATR | VAL -2.27 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp +0.00030%/hr, BybitPerp +0.00056%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.3 ATR below VAL 2,196.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,196.00 | stop 2,047.53 | T1 2,244.50 | T2 2,321.00
- R:R 0.33 at T1, 0.84 at T2 | risk 148.47
- invalid: 5m close below 2,047.53: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.33R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.3 ATR below VAL 2,196.00; short the retest that fails at it
- entry 2,196.00 | stop 2,212.45 | T1 2,071.00 | T2 2,058.50
- R:R 7.60 at T1, 8.36 at T2 | risk 16.45
- invalid: 1H close back inside value (above 2,196.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 7.60R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,122.02 or pivot resistance near 2,227.83; sell the rejection, not the touch
- entry 2,227.83 | stop 2,241.00 | T1 2,196.00 | T2 2,183.96
- R:R 2.42 at T1, 3.33 at T2 | risk 13.16
- invalid: 5m close above 2,241.00: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.42R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$13.16-$16.45); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
