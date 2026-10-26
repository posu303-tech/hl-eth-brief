# ETH perp (Hyperliquid) - 2026-10-27 05:13 UTC+05:30 (23:43 UTC)
spot 2,322.05 | mark 2,322.10 | oracle 2,323.20 | OI 1,121,905.71 ETH (+0.120% vs last run, 24h n/a until the store has a day)
funding +0.00032%/hr (~+2.77%/yr, 16th pct of last 500h) | 24h notional $878.6m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,333.47 / 2,384.10) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 31% of prior range | -1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 16th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,355.00 | POC 2,400.50 | VAH 2,460.00 (width 105.00 = 4.52% of spot, 240 bars)
- developing session (99% elapsed): VAL 2,306.00 | POC 2,314.50 | VAH 2,330.00
- session VWAP 2,318.65 (+1s 2,328.55 / -1s 2,308.74) | prior session VWAP 2,338.57
- prior day: PDH 2,370.50 | PDL 2,310.30 | PDC 2,328.80 (PDH intact, PDL swept)
- floor pivots: S3 2,242.37 | S2 2,276.33 | S1 2,302.57 | P 2,336.53 | R1 2,362.77 | R2 2,396.73 | R3 2,422.97
- 1H ATR(14) 16.71 = 0.72% of spot | ATR vs 30d median x0.97
- distance to POC -4.70 ATR | VAH -8.26 ATR | VAL -1.97 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00112%/hr, BybitPerp +0.00042%/hr, HlPerp +0.00031%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.0 ATR below VAL 2,355.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,355.00 | stop 2,301.95 | T1 2,400.50 | T2 2,460.00
- R:R 0.86 at T1, 1.98 at T2 | risk 53.05
- invalid: 5m close below 2,301.95: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.86R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.0 ATR below VAL 2,355.00; short the retest that fails at it
- entry 2,355.00 | stop 2,367.53 | T1 2,310.30 | T2 2,302.57
- R:R 3.57 at T1, 4.19 at T2 | risk 12.53
- invalid: 1H close back inside value (above 2,355.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.57R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,318.65 or pivot support near 2,318.65; buy the hold, not the touch
- entry 2,318.65 | stop 2,308.62 | T1 2,328.55 | T2 2,352.06
- R:R 0.99 at T1, 3.33 at T2 | risk 10.02
- invalid: 5m close below 2,308.62: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.99R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-0.75x the 1H ATR (~$12.53-$12.53); funding runs +0.0076%/day ($+0.03/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
