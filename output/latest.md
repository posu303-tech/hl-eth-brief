# ETH perp (Hyperliquid) - 2026-10-30 06:15 UTC+05:30 (00:45 UTC)
spot 2,209.95 | mark 2,210.00 | oracle 2,213.12 | OI 1,097,982.74 ETH (+1.280% vs last run, -1.19% 24h)
funding -0.00778%/hr (~-68.14%/yr, 0th pct of last 500h) | 24h notional $2,741.7m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,326.11 / 2,357.09) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 16% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 0th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.2%, price -6.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,286.00 | POC 2,326.50 | VAH 2,416.00 (width 130.00 = 5.88% of spot, 240 bars)
- developing session (3% elapsed): VAL 2,197.00 | POC 2,210.50 | VAH 2,218.00
- session VWAP 2,216.75 (+1s 2,229.83 / -1s 2,203.66) | prior session VWAP 2,291.73
- prior day: PDH 2,378.30 | PDL 2,227.20 | PDC 2,251.90 (PDH intact, PDL swept)
- floor pivots: S3 2,042.20 | S2 2,134.70 | S1 2,193.30 | P 2,285.80 | R1 2,344.40 | R2 2,436.90 | R3 2,495.50
- 1H ATR(14) 26.64 = 1.21% of spot | ATR vs 30d median x1.53
- distance to POC -4.37 ATR | VAH -7.73 ATR | VAL -2.85 ATR | closes outside value (last 20): 20%
- cross-venue funding: BinPerp -0.00073%/hr, BybitPerp -0.00310%/hr, HlPerp -0.00777%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.9 ATR below VAL 2,286.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,286.00 | stop 2,196.63 | T1 2,326.50 | T2 2,416.00
- R:R 0.45 at T1, 1.45 at T2 | risk 89.37
- invalid: 5m close below 2,196.63: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.45R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.9 ATR below VAL 2,286.00; short the retest that fails at it
- entry 2,286.00 | stop 2,305.98 | T1 2,227.20 | T2 2,193.30
- R:R 2.94 at T1, 4.64 at T2 | risk 19.98
- invalid: 1H close back inside value (above 2,286.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 2.94R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,216.75 or pivot support near 2,193.30; buy the hold, not the touch
- entry 2,193.30 | stop 2,177.31 | T1 2,229.83 | T2 2,246.58
- R:R 2.29 at T1, 3.33 at T2 | risk 15.99
- invalid: 5m close below 2,177.31: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.29R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$15.99-$19.98); funding runs -0.1867%/day ($-0.78/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
