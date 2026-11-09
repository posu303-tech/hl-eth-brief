# ETH perp (Hyperliquid) - 2026-11-09 11:26 UTC+05:30 (05:56 UTC)
spot 2,130.75 | mark 2,130.80 | oracle 2,132.00 | OI 901,735.73 ETH (-1.814% vs last run, -7.68% 24h)
funding -0.00119%/hr (~-10.44%/yr, 4th pct of last 500h) | 24h notional $1,382.8m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,213.19 / 2,264.72) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 36% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 4th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -7.7%, price -4.6%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,196.00 | POC 2,244.50 | VAH 2,321.00 (width 125.00 = 5.87% of spot, 240 bars)
- developing session (25% elapsed): VAL 2,128.00 | POC 2,143.50 | VAH 2,146.00
- session VWAP 2,138.19 (+1s 2,146.51 / -1s 2,129.87) | prior session VWAP 2,147.58
- prior day: PDH 2,245.20 | PDL 2,058.50 | PDC 2,125.80 (PDH intact, PDL intact)
- floor pivots: S3 1,854.43 | S2 1,956.47 | S1 2,041.13 | P 2,143.17 | R1 2,227.83 | R2 2,329.87 | R3 2,414.53
- 1H ATR(14) 21.22 = 1.00% of spot | ATR vs 30d median x2.93
- distance to POC -5.36 ATR | VAH -8.97 ATR | VAL -3.07 ATR | closes outside value (last 20): 40%
- cross-venue funding: BinPerp -0.00051%/hr, BybitPerp -0.00062%/hr, HlPerp -0.00119%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.1 ATR below VAL 2,196.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,196.00 | stop 2,047.89 | T1 2,244.50 | T2 2,321.00
- R:R 0.33 at T1, 0.84 at T2 | risk 148.11
- invalid: 5m close below 2,047.89: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.33R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.1 ATR below VAL 2,196.00; short the retest that fails at it
- entry 2,196.00 | stop 2,211.92 | T1 2,071.00 | T2 2,058.50
- R:R 7.85 at T1, 8.64 at T2 | risk 15.92
- invalid: 1H close back inside value (above 2,196.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 7.85R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,138.19 or pivot support near 2,041.13; buy the hold, not the touch
- entry 2,041.13 | stop 2,028.40 | T1 2,083.58 | T2 2,146.51
- R:R 3.33 at T1, 8.28 at T2 | risk 12.73
- invalid: 5m close below 2,028.40: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$12.73-$15.92); funding runs -0.0286%/day ($-0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
