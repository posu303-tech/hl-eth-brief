# ETH perp (Hyperliquid) - 2026-11-05 17:37 UTC+05:30 (12:07 UTC)
spot 2,416.25 | mark 2,416.30 | oracle 2,416.40 | OI 1,034,637.18 ETH (+1.091% vs last run, +0.51% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,433.7m

## 1) HTF bias - BALANCED (+2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price > EMA50 > EMA200 (2,364.80 / 2,318.33) | +1 |
| 10-session value | price above the value area | +1 |
| Prior day close | closed at 88% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +0.5%, price +4.4%: no edge | 0 |

## 2) Intraday regime - trend-up, price ABOVE value

- value area (10 UTC sessions, 70%): VAL 2,222.00 | POC 2,251.50 | VAH 2,332.00 (width 110.00 = 4.55% of spot, 240 bars)
- developing session (51% elapsed): VAL 2,417.00 | POC 2,419.50 | VAH 2,431.00
- session VWAP 2,423.12 (+1s 2,428.84 / -1s 2,417.41) | prior session VWAP 2,358.22
- prior day: PDH 2,450.00 | PDL 2,225.70 | PDC 2,423.90 (PDH intact, PDL intact)
- floor pivots: S3 2,058.77 | S2 2,142.23 | S1 2,283.07 | P 2,366.53 | R1 2,507.37 | R2 2,590.83 | R3 2,731.67
- 1H ATR(14) 16.14 = 0.67% of spot | ATR vs 30d median x0.83
- distance to POC +10.21 ATR | VAH +5.22 ATR | VAL +12.03 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (short back into value)** [SHORT]
- trigger: price is 5.2 ATR above VAH 2,332.00; arm only on a 5m close back below it, which is what confirms the failure
- entry 2,332.00 | stop 2,458.07 | T1 2,251.50 | T2 2,222.00
- R:R 0.64 at T1, 0.87 at T2 | risk 126.07
- invalid: 5m close above 2,458.07: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.64R, below the 1.5R floor

**S2 - Acceptance and retest (long VAH)** [LONG]
- trigger: price has been accepted 5.2 ATR above VAH 2,332.00; long the retest that holds above it
- entry 2,332.00 | stop 2,319.89 | T1 2,442.00 | T2 2,450.00
- R:R 9.09 at T1, 9.75 at T2 | risk 12.11
- invalid: 1H close back inside value (below 2,332.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 9.09R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,423.12 or pivot support near 2,366.53; buy the hold, not the touch
- entry 2,366.53 | stop 2,356.85 | T1 2,398.82 | T2 2,428.84
- R:R 3.33 at T1, 6.43 at T2 | risk 9.68
- invalid: 5m close below 2,356.85: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$9.68-$12.11); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
