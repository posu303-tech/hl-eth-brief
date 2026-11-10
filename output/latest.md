# ETH perp (Hyperliquid) - 2026-11-10 22:27 UTC+05:30 (16:57 UTC)
spot 2,013.35 | mark 2,013.60 | oracle 2,014.59 | OI 790,756.90 ETH (-1.181% vs last run, -4.74% 24h)
funding +0.00063%/hr (~+5.51%/yr, 31th pct of last 500h) | 24h notional $1,288.3m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,133.92 / 2,219.71) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 68% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 31th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -4.7%, price -5.6%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,206.00 | POC 2,244.50 | VAH 2,428.00 (width 222.00 = 11.03% of spot, 240 bars)
- developing session (71% elapsed): VAL 2,021.00 | POC 2,092.50 | VAH 2,106.00
- session VWAP 2,064.05 (+1s 2,098.76 / -1s 2,029.34) | prior session VWAP 2,123.93
- prior day: PDH 2,159.00 | PDL 2,081.40 | PDC 2,133.90 (PDH intact, PDL swept)
- floor pivots: S3 2,012.93 | S2 2,047.17 | S1 2,090.53 | P 2,124.77 | R1 2,168.13 | R2 2,202.37 | R3 2,245.73
- 1H ATR(14) 26.72 = 1.33% of spot | ATR vs 30d median x1.33
- distance to POC -8.65 ATR | VAH -15.52 ATR | VAL -7.21 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00047%/hr, BybitPerp +0.00000%/hr, HlPerp +0.00060%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 7.2 ATR below VAL 2,206.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,206.00 | stop 1,999.99 | T1 2,244.50 | T2 2,428.00
- R:R 0.19 at T1, 1.08 at T2 | risk 206.01
- invalid: 5m close below 1,999.99: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.19R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 7.2 ATR below VAL 2,206.00; short the retest that fails at it
- entry 2,206.00 | stop 2,226.04 | T1 2,090.53 | T2 2,047.17
- R:R 5.76 at T1, 7.93 at T2 | risk 20.04
- invalid: 1H close back inside value (above 2,206.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 5.76R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,064.05 or pivot resistance near 2,064.05; sell the rejection, not the touch
- entry 2,064.05 | stop 2,080.08 | T1 2,029.34 | T2 2,010.61
- R:R 2.17 at T1, 3.33 at T2 | risk 16.03
- invalid: 5m close above 2,080.08: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.17R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$16.03-$20.04); funding runs +0.0151%/day ($+0.06/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
