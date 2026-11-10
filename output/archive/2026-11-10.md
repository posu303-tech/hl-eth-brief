# ETH perp (Hyperliquid) - 2026-11-11 03:45 UTC+05:30 (22:15 UTC)
spot 2,057.15 | mark 2,057.10 | oracle 2,058.10 | OI 771,971.55 ETH (-2.376% vs last run, -2.21% 24h)
funding +0.00045%/hr (~+3.95%/yr, 25th pct of last 500h) | 24h notional $1,346.0m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,114.31 / 2,209.32) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 68% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 25th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI -2.2%, price -3.3%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,206.00 | POC 2,244.50 | VAH 2,428.00 (width 222.00 = 10.79% of spot, 240 bars)
- developing session (93% elapsed): VAL 2,008.00 | POC 2,025.50 | VAH 2,084.00
- session VWAP 2,059.75 (+1s 2,093.00 / -1s 2,026.50) | prior session VWAP 2,123.93
- prior day: PDH 2,159.00 | PDL 2,081.40 | PDC 2,133.90 (PDH intact, PDL swept)
- floor pivots: S3 2,012.93 | S2 2,047.17 | S1 2,090.53 | P 2,124.77 | R1 2,168.13 | R2 2,202.37 | R3 2,245.73
- 1H ATR(14) 23.71 = 1.15% of spot | ATR vs 30d median x1.18
- distance to POC -7.90 ATR | VAH -15.64 ATR | VAL -6.28 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp -0.00054%/hr, BybitPerp +0.00004%/hr, HlPerp +0.00044%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 6.3 ATR below VAL 2,206.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,206.00 | stop 2,045.30 | T1 2,244.50 | T2 2,428.00
- R:R 0.24 at T1, 1.38 at T2 | risk 160.70
- invalid: 5m close below 2,045.30: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.24R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 6.3 ATR below VAL 2,206.00; short the retest that fails at it
- entry 2,206.00 | stop 2,223.78 | T1 2,090.53 | T2 2,047.17
- R:R 6.49 at T1, 8.93 at T2 | risk 17.78
- invalid: 1H close back inside value (above 2,206.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 6.49R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,059.75 or pivot resistance near 2,124.77; sell the rejection, not the touch
- entry 2,124.77 | stop 2,138.99 | T1 2,090.53 | T2 2,077.35
- R:R 2.41 at T1, 3.33 at T2 | risk 14.23
- invalid: 5m close above 2,138.99: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.41R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$14.23-$17.78); funding runs +0.0108%/day ($+0.05/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
