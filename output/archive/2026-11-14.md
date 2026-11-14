# ETH perp (Hyperliquid) - 2026-11-14 22:26 UTC+05:30 (16:56 UTC)
spot 1,826.15 | mark 1,826.00 | oracle 1,827.10 | OI 687,746.46 ETH (-1.676% vs last run, -5.29% 24h)
funding -0.00141%/hr (~-12.37%/yr, 2th pct of last 500h) | 24h notional $1,184.6m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,941.90 / 2,072.09) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 27% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 2th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -5.3%, price -5.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,895.00 | POC 2,124.25 | VAH 2,235.50 (width 340.50 = 18.65% of spot, 240 bars)
- developing session (71% elapsed): VAL 1,814.50 | POC 1,828.25 | VAH 1,894.00
- session VWAP 1,868.43 (+1s 1,900.62 / -1s 1,836.23) | prior session VWAP 1,946.03
- prior day: PDH 2,020.40 | PDL 1,894.90 | PDC 1,928.70 (PDH intact, PDL swept)
- floor pivots: S3 1,750.10 | S2 1,822.50 | S1 1,875.60 | P 1,948.00 | R1 2,001.10 | R2 2,073.50 | R3 2,126.60
- 1H ATR(14) 21.61 = 1.18% of spot | ATR vs 30d median x1.03
- distance to POC -13.80 ATR | VAH -18.95 ATR | VAL -3.19 ATR | closes outside value (last 20): 25%
- cross-venue funding: BinPerp -0.00019%/hr, BybitPerp -0.00057%/hr, HlPerp -0.00142%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.2 ATR below VAL 1,895.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,895.00 | stop 1,815.35 | T1 2,124.25 | T2 2,235.50
- R:R 2.88 at T1, 4.27 at T2 | risk 79.65
- invalid: 5m close below 1,815.35: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.88R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.2 ATR below VAL 1,895.00; short the retest that fails at it
- entry 1,895.00 | stop 1,911.20 | T1 1,875.60 | T2 1,822.50
- R:R 1.20 at T1, 4.47 at T2 | risk 16.20
- invalid: 1H close back inside value (above 1,895.00) voids the acceptance
- verdict: STAND ASIDE - T1 pays 1.20R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,868.43 or pivot resistance near 1,868.43; sell the rejection, not the touch
- entry 1,868.43 | stop 1,881.39 | T1 1,836.23 | T2 1,825.22
- R:R 2.48 at T1, 3.33 at T2 | risk 12.96
- invalid: 5m close above 1,881.39: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.48R)

## 4) Risk note
Stops sit 0.60-3.69x the 1H ATR (~$12.96-$79.65); funding runs -0.0339%/day ($-0.14/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
