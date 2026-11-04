# ETH perp (Hyperliquid) - 2026-11-05 04:01 UTC+05:30 (22:31 UTC)
spot 2,436.35 | mark 2,436.40 | oracle 2,437.17 | OI 1,029,014.26 ETH (-1.474% vs last run, +2.06% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,951.9m

## 1) HTF bias - BULLISH (+3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price > EMA50 > EMA200 (2,321.13 / 2,302.54) | +1 |
| 10-session value | price above the value area | +1 |
| Prior day close | closed at 49% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +2.1% with price +6.5%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price ABOVE value

- value area (10 UTC sessions, 70%): VAL 2,221.00 | POC 2,251.50 | VAH 2,328.00 (width 107.00 = 4.39% of spot, 240 bars)
- developing session (94% elapsed): VAL 2,306.00 | POC 2,425.50 | VAH 2,447.00
- session VWAP 2,357.43 (+1s 2,426.82 / -1s 2,288.03) | prior session VWAP 2,279.88
- prior day: PDH 2,309.40 | PDL 2,240.40 | PDC 2,274.50 (PDH swept, PDL swept)
- floor pivots: S3 2,171.13 | S2 2,205.77 | S1 2,240.13 | P 2,274.77 | R1 2,309.13 | R2 2,343.77 | R3 2,378.13
- 1H ATR(14) 22.20 = 0.91% of spot | ATR vs 30d median x1.25
- distance to POC +8.33 ATR | VAH +4.88 ATR | VAL +9.70 ATR | closes outside value (last 20): 45%
- cross-venue funding: BinPerp -0.00004%/hr, BybitPerp +0.00075%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (short back into value)** [SHORT]
- trigger: price is 4.9 ATR above VAH 2,328.00; arm only on a 5m close back below it, which is what confirms the failure
- entry 2,328.00 | stop 2,447.45 | T1 2,251.50 | T2 2,221.00
- R:R 0.64 at T1, 0.90 at T2 | risk 119.45
- invalid: 5m close above 2,447.45: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.64R, below the 1.5R floor

**S2 - Acceptance and retest (long VAH)** [LONG]
- trigger: price has been accepted 4.9 ATR above VAH 2,328.00; long the retest that holds above it
- entry 2,328.00 | stop 2,311.35 | T1 2,343.77 | T2 2,378.13
- R:R 0.95 at T1, 3.01 at T2 | risk 16.65
- invalid: 1H close back inside value (below 2,328.00) voids the acceptance
- verdict: STAND ASIDE - T1 pays 0.95R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,357.43 or pivot support near 2,357.43; buy the hold, not the touch
- entry 2,357.43 | stop 2,344.11 | T1 2,401.83 | T2 2,426.82
- R:R 3.33 at T1, 5.21 at T2 | risk 13.32
- invalid: 5m close below 2,344.11: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.60x the 1H ATR (~$13.32-$13.32); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
