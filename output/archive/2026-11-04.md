# ETH perp (Hyperliquid) - 2026-11-04 22:32 UTC+05:30 (17:02 UTC)
spot 2,431.05 | mark 2,430.82 | oracle 2,431.82 | OI 1,044,406.45 ETH (+1.464% vs last run, +4.75% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,763.2m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price > EMA50 > EMA200 (2,299.72 / 2,296.62) | +1 |
| 10-session value | price above the value area | +1 |
| Prior day close | closed at 49% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +4.7% with price +5.8%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price ABOVE value

- value area (10 UTC sessions, 70%): VAL 2,221.00 | POC 2,251.50 | VAH 2,328.00 (width 107.00 = 4.40% of spot, 240 bars)
- developing session (71% elapsed): VAL 2,294.00 | POC 2,436.50 | VAH 2,447.00
- session VWAP 2,343.64 (+1s 2,412.54 / -1s 2,274.73) | prior session VWAP 2,279.88
- prior day: PDH 2,309.40 | PDL 2,240.40 | PDC 2,274.50 (PDH swept, PDL swept)
- floor pivots: S3 2,171.13 | S2 2,205.77 | S1 2,240.13 | P 2,274.77 | R1 2,309.13 | R2 2,343.77 | R3 2,378.13
- 1H ATR(14) 24.41 = 1.00% of spot | ATR vs 30d median x1.55
- distance to POC +7.36 ATR | VAH +4.22 ATR | VAL +8.61 ATR | closes outside value (last 20): 20%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (short back into value)** [SHORT]
- trigger: price is 4.2 ATR above VAH 2,328.00; arm only on a 5m close back below it, which is what confirms the failure
- entry 2,328.00 | stop 2,443.25 | T1 2,251.50 | T2 2,221.00
- R:R 0.66 at T1, 0.93 at T2 | risk 115.25
- invalid: 5m close above 2,443.25: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.66R, below the 1.5R floor

**S2 - Acceptance and retest (long VAH)** [LONG]
- trigger: price has been accepted 4.2 ATR above VAH 2,328.00; long the retest that holds above it
- entry 2,328.00 | stop 2,309.70 | T1 2,343.77 | T2 2,378.13
- R:R 0.86 at T1, 2.74 at T2 | risk 18.30
- invalid: 1H close back inside value (below 2,328.00) voids the acceptance
- verdict: STAND ASIDE - T1 pays 0.86R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,343.64 or pivot support near 2,343.64; buy the hold, not the touch
- entry 2,343.64 | stop 2,328.99 | T1 2,392.45 | T2 2,412.54
- R:R 3.33 at T1, 4.71 at T2 | risk 14.64
- invalid: 5m close below 2,328.99: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.60x the 1H ATR (~$14.64-$14.64); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
