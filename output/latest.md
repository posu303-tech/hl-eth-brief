# ETH perp (Hyperliquid) - 2026-10-26 13:29 UTC+05:30 (07:59 UTC)
spot 2,318.45 | mark 2,318.40 | oracle 2,319.54 | OI 1,104,908.53 ETH (+0.057% vs last run, 24h n/a until the store has a day)
funding +0.00082%/hr (~+7.21%/yr, 24th pct of last 500h) | 24h notional $725.5m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,346.41 / 2,395.27) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 31% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 24th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,355.00 | POC 2,400.50 | VAH 2,460.00 (width 105.00 = 4.53% of spot, 240 bars)
- developing session (33% elapsed): VAL 2,303.00 | POC 2,317.50 | VAH 2,330.00
- session VWAP 2,315.26 (+1s 2,325.45 / -1s 2,305.07) | prior session VWAP 2,338.57
- prior day: PDH 2,370.50 | PDL 2,310.30 | PDC 2,328.80 (PDH intact, PDL swept)
- floor pivots: S3 2,242.37 | S2 2,276.33 | S1 2,302.57 | P 2,336.53 | R1 2,362.77 | R2 2,396.73 | R3 2,422.97
- 1H ATR(14) 17.35 = 0.75% of spot | ATR vs 30d median x1.21
- distance to POC -4.73 ATR | VAH -8.16 ATR | VAL -2.11 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp +0.00062%/hr, BybitPerp -0.00034%/hr, HlPerp +0.00083%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.1 ATR below VAL 2,355.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,355.00 | stop 2,301.62 | T1 2,400.50 | T2 2,460.00
- R:R 0.85 at T1, 1.97 at T2 | risk 53.38
- invalid: 5m close below 2,301.62: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.85R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.1 ATR below VAL 2,355.00; short the retest that fails at it
- entry 2,355.00 | stop 2,368.01 | T1 2,310.30 | T2 2,302.57
- R:R 3.44 at T1, 4.03 at T2 | risk 13.01
- invalid: 1H close back inside value (above 2,355.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.44R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,315.26 or pivot resistance near 2,336.53; sell the rejection, not the touch
- entry 2,336.53 | stop 2,346.94 | T1 2,310.30 | T2 2,302.57
- R:R 2.52 at T1, 3.26 at T2 | risk 10.41
- invalid: 5m close above 2,346.94: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.52R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$10.41-$13.01); funding runs +0.0198%/day ($+0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
