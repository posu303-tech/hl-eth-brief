# ETH perp (Hyperliquid) - 2026-11-24 22:56 UTC+05:30 (17:26 UTC)
spot 1,675.95 | mark 1,675.90 | oracle 1,676.70 | OI 613,521.43 ETH (+1.028% vs last run, +1.03% 24h)
funding +0.00082%/hr (~+7.23%/yr, 35th pct of last 500h) | 24h notional $1,089.3m

## 1) HTF bias - BEARISH (-5 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,705.82 / 1,755.48) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 9% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 35th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +1.0% with price -4.6%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,686.50 | POC 1,816.25 | VAH 1,847.00 (width 160.50 = 9.58% of spot, 240 bars)
- developing session (73% elapsed): VAL 1,678.00 | POC 1,697.75 | VAH 1,704.00
- session VWAP 1,690.89 (+1s 1,702.46 / -1s 1,679.33) | prior session VWAP 1,759.63
- prior day: PDH 1,844.60 | PDL 1,695.70 | PDC 1,709.80 (PDH intact, PDL swept)
- floor pivots: S3 1,506.57 | S2 1,601.13 | S1 1,655.47 | P 1,750.03 | R1 1,804.37 | R2 1,898.93 | R3 1,953.27
- 1H ATR(14) 20.29 = 1.21% of spot | ATR vs 30d median x0.93
- distance to POC -6.91 ATR | VAH -8.43 ATR | VAL -0.52 ATR | closes outside value (last 20): 25%
- cross-venue funding: BinPerp +0.00047%/hr, BybitPerp +0.00124%/hr, HlPerp +0.00081%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.5 ATR below VAL 1,686.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,686.50 | stop 1,665.80 | T1 1,816.25 | T2 1,847.00
- R:R 6.27 at T1, 7.75 at T2 | risk 20.70
- invalid: 5m close below 1,665.80: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 6.27R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.5 ATR below VAL 1,686.50; short the retest that fails at it
- entry 1,686.50 | stop 1,701.72 | T1 1,655.47 | T2 1,601.13
- R:R 2.04 at T1, 5.61 at T2 | risk 15.22
- invalid: 1H close back inside value (above 1,686.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 2.04R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,690.89 or pivot resistance near 1,690.89; sell the rejection, not the touch
- entry 1,690.89 | stop 1,703.07 | T1 1,679.33 | T2 1,655.47
- R:R 0.95 at T1, 2.91 at T2 | risk 12.18
- invalid: 5m close above 1,703.07: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.95R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-1.02x the 1H ATR (~$15.22-$20.70); funding runs +0.0198%/day ($+0.08/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
