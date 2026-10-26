# ETH perp (Hyperliquid) - 2026-10-26 13:37 UTC+05:30 (08:07 UTC)
spot 2,307.95 | mark 2,307.90 | oracle 2,309.00 | OI 1,104,451.56 ETH (-0.041% vs last run, 24h n/a until the store has a day)
funding +0.00033%/hr (~+2.87%/yr, 15th pct of last 500h) | 24h notional $725.8m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,345.28 / 2,394.50) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 31% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 15th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,355.00 | POC 2,400.50 | VAH 2,460.00 (width 105.00 = 4.55% of spot, 240 bars)
- developing session (34% elapsed): VAL 2,303.00 | POC 2,317.50 | VAH 2,329.00
- session VWAP 2,315.20 (+1s 2,325.34 / -1s 2,305.06) | prior session VWAP 2,338.57
- prior day: PDH 2,370.50 | PDL 2,310.30 | PDC 2,328.80 (PDH intact, PDL swept)
- floor pivots: S3 2,242.37 | S2 2,276.33 | S1 2,302.57 | P 2,336.53 | R1 2,362.77 | R2 2,396.73 | R3 2,422.97
- 1H ATR(14) 16.99 = 0.74% of spot | ATR vs 30d median x1.19
- distance to POC -5.45 ATR | VAH -8.95 ATR | VAL -2.77 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp +0.00058%/hr, BybitPerp -0.00147%/hr, HlPerp +0.00034%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.8 ATR below VAL 2,355.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,355.00 | stop 2,299.46 | T1 2,400.50 | T2 2,460.00
- R:R 0.82 at T1, 1.89 at T2 | risk 55.54
- invalid: 5m close below 2,299.46: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.82R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.8 ATR below VAL 2,355.00; short the retest that fails at it
- entry 2,355.00 | stop 2,367.74 | T1 2,310.30 | T2 2,302.57
- R:R 3.51 at T1, 4.11 at T2 | risk 12.74
- invalid: 1H close back inside value (above 2,355.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.51R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,315.20 or pivot resistance near 2,315.20; sell the rejection, not the touch
- entry 2,315.20 | stop 2,325.40 | T1 2,305.06 | T2 2,281.22
- R:R 0.99 at T1, 3.33 at T2 | risk 10.19
- invalid: 5m close above 2,325.40: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.99R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-0.75x the 1H ATR (~$12.74-$12.74); funding runs +0.0079%/day ($+0.03/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
