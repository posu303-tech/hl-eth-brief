# ETH perp (Hyperliquid) - 2026-10-27 00:38 UTC+05:30 (19:08 UTC)
spot 2,313.15 | mark 2,313.30 | oracle 2,314.44 | OI 1,120,562.31 ETH (+1.699% vs last run, 24h n/a until the store has a day)
funding +0.00029%/hr (~+2.54%/yr, 15th pct of last 500h) | 24h notional $940.0m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,337.32 / 2,387.08) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 31% of prior range | -1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 15th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,355.00 | POC 2,400.50 | VAH 2,460.00 (width 105.00 = 4.54% of spot, 240 bars)
- developing session (80% elapsed): VAL 2,310.00 | POC 2,329.50 | VAH 2,333.00
- session VWAP 2,319.92 (+1s 2,330.09 / -1s 2,309.75) | prior session VWAP 2,338.57
- prior day: PDH 2,370.50 | PDL 2,310.30 | PDC 2,328.80 (PDH intact, PDL swept)
- floor pivots: S3 2,242.37 | S2 2,276.33 | S1 2,302.57 | P 2,336.53 | R1 2,362.77 | R2 2,396.73 | R3 2,422.97
- 1H ATR(14) 18.49 = 0.80% of spot | ATR vs 30d median x1.09
- distance to POC -4.72 ATR | VAH -7.94 ATR | VAL -2.26 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00074%/hr, HlPerp +0.00026%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.3 ATR below VAL 2,355.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,355.00 | stop 2,301.05 | T1 2,400.50 | T2 2,460.00
- R:R 0.84 at T1, 1.95 at T2 | risk 53.95
- invalid: 5m close below 2,301.05: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.84R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.3 ATR below VAL 2,355.00; short the retest that fails at it
- entry 2,355.00 | stop 2,368.87 | T1 2,310.30 | T2 2,302.57
- R:R 3.22 at T1, 3.78 at T2 | risk 13.87
- invalid: 1H close back inside value (above 2,355.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 3.22R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,319.92 or pivot support near 2,302.57; buy the hold, not the touch
- entry 2,302.57 | stop 2,291.47 | T1 2,330.09 | T2 2,339.56
- R:R 2.48 at T1, 3.33 at T2 | risk 11.10
- invalid: 5m close below 2,291.47: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.48R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$11.10-$13.87); funding runs +0.0070%/day ($+0.03/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
