# ETH perp (Hyperliquid) - 2026-11-10 13:43 UTC+05:30 (08:13 UTC)
spot 2,116.35 | mark 2,116.30 | oracle 2,117.30 | OI 800,207.97 ETH (+1.369% vs last run, -11.26% 24h)
funding +0.00117%/hr (~+10.21%/yr, 52th pct of last 500h) | 24h notional $843.7m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,153.54 / 2,231.06) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 68% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 52th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -11.3%, price +1.1%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,206.00 | POC 2,244.50 | VAH 2,428.00 (width 222.00 = 10.49% of spot, 240 bars)
- developing session (34% elapsed): VAL 2,114.00 | POC 2,121.50 | VAH 2,127.00
- session VWAP 2,120.89 (+1s 2,126.47 / -1s 2,115.31) | prior session VWAP 2,123.93
- prior day: PDH 2,159.00 | PDL 2,081.40 | PDC 2,133.90 (PDH intact, PDL intact)
- floor pivots: S3 2,012.93 | S2 2,047.17 | S1 2,090.53 | P 2,124.77 | R1 2,168.13 | R2 2,202.37 | R3 2,245.73
- 1H ATR(14) 15.61 = 0.74% of spot | ATR vs 30d median x0.72
- distance to POC -8.21 ATR | VAH -19.96 ATR | VAL -5.74 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00035%/hr, BybitPerp -0.00016%/hr, HlPerp +0.00118%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 5.7 ATR below VAL 2,206.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,206.00 | stop 2,073.59 | T1 2,244.50 | T2 2,428.00
- R:R 0.29 at T1, 1.68 at T2 | risk 132.41
- invalid: 5m close below 2,073.59: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.29R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 5.7 ATR below VAL 2,206.00; short the retest that fails at it
- entry 2,206.00 | stop 2,217.71 | T1 2,090.53 | T2 2,081.40
- R:R 9.86 at T1, 10.64 at T2 | risk 11.71
- invalid: 1H close back inside value (above 2,206.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 9.86R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,120.89 or pivot support near 2,090.53; buy the hold, not the touch
- entry 2,090.53 | stop 2,081.17 | T1 2,121.75 | T2 2,159.00
- R:R 3.33 at T1, 7.31 at T2 | risk 9.37
- invalid: 5m close below 2,081.17: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$9.37-$11.71); funding runs +0.0280%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
