# ETH perp (Hyperliquid) - 2026-11-05 08:54 UTC+05:30 (03:24 UTC)
spot 2,432.95 | mark 2,432.60 | oracle 2,433.32 | OI 1,023,473.76 ETH (-0.538% vs last run, +1.12% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,803.6m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price > EMA50 > EMA200 (2,340.41 / 2,308.64) | +1 |
| 10-session value | price above the value area | +1 |
| Prior day close | closed at 88% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +1.1% with price +8.3%: new longs | +1 |

## 2) Intraday regime - trend-up, price ABOVE value

- value area (10 UTC sessions, 70%): VAL 2,222.00 | POC 2,251.50 | VAH 2,332.00 (width 110.00 = 4.52% of spot, 240 bars)
- developing session (14% elapsed): VAL 2,418.00 | POC 2,428.50 | VAH 2,432.00
- session VWAP 2,423.82 (+1s 2,429.92 / -1s 2,417.72) | prior session VWAP 2,358.22
- prior day: PDH 2,450.00 | PDL 2,225.70 | PDC 2,423.90 (PDH intact, PDL intact)
- floor pivots: S3 2,058.77 | S2 2,142.23 | S1 2,283.07 | P 2,366.53 | R1 2,507.37 | R2 2,590.83 | R3 2,731.67
- 1H ATR(14) 20.85 = 0.86% of spot | ATR vs 30d median x1.12
- distance to POC +8.70 ATR | VAH +4.84 ATR | VAL +10.12 ATR | closes outside value (last 20): 65%
- cross-venue funding: BinPerp +0.00029%/hr, BybitPerp +0.00060%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (short back into value)** [SHORT]
- trigger: price is 4.8 ATR above VAH 2,332.00; arm only on a 5m close back below it, which is what confirms the failure
- entry 2,332.00 | stop 2,460.42 | T1 2,251.50 | T2 2,222.00
- R:R 0.63 at T1, 0.86 at T2 | risk 128.42
- invalid: 5m close above 2,460.42: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.63R, below the 1.5R floor

**S2 - Acceptance and retest (long VAH)** [LONG]
- trigger: price has been accepted 4.8 ATR above VAH 2,332.00; long the retest that holds above it
- entry 2,332.00 | stop 2,316.36 | T1 2,442.00 | T2 2,507.37
- R:R 7.03 at T1, 11.22 at T2 | risk 15.64
- invalid: 1H close back inside value (below 2,332.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 7.03R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,423.82 or pivot support near 2,423.82; buy the hold, not the touch
- entry 2,423.82 | stop 2,411.31 | T1 2,450.00 | T2 2,465.52
- R:R 2.09 at T1, 3.33 at T2 | risk 12.51
- invalid: 5m close below 2,411.31: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.09R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$12.51-$15.64); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
