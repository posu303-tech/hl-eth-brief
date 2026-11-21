# ETH perp (Hyperliquid) - 2026-11-21 06:49 UTC+05:30 (01:19 UTC)
spot 1,627.15 | mark 1,627.36 | oracle 1,628.44 | OI 591,609.62 ETH (-4.147% vs last run, -2.54% 24h)
funding -0.00212%/hr (~-18.59%/yr, 3th pct of last 500h) | 24h notional $1,932.3m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,720.60 / 1,834.21) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 22% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 3th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -2.5%, price -7.6%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,710.00 | POC 1,816.25 | VAH 1,972.50 (width 262.50 = 16.13% of spot, 240 bars)
- developing session (6% elapsed): VAL 1,621.50 | POC 1,623.25 | VAH 1,626.50
- session VWAP 1,623.99 (+1s 1,625.95 / -1s 1,622.03) | prior session VWAP 1,661.47
- prior day: PDH 1,769.70 | PDL 1,580.00 | PDC 1,621.90 (PDH intact, PDL intact)
- floor pivots: S3 1,355.00 | S2 1,467.50 | S1 1,544.70 | P 1,657.20 | R1 1,734.40 | R2 1,846.90 | R3 1,924.10
- 1H ATR(14) 25.68 = 1.58% of spot | ATR vs 30d median x1.19
- distance to POC -7.36 ATR | VAH -13.45 ATR | VAL -3.23 ATR | closes outside value (last 20): 50%
- cross-venue funding: BinPerp -0.00254%/hr, BybitPerp -0.00148%/hr, HlPerp -0.00213%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.2 ATR below VAL 1,710.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,710.00 | stop 1,567.16 | T1 1,816.25 | T2 1,972.50
- R:R 0.74 at T1, 1.84 at T2 | risk 142.84
- invalid: 5m close below 1,567.16: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.74R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.2 ATR below VAL 1,710.00; short the retest that fails at it
- entry 1,710.00 | stop 1,729.26 | T1 1,580.00 | T2 1,544.70
- R:R 6.75 at T1, 8.58 at T2 | risk 19.26
- invalid: 1H close back inside value (above 1,710.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 6.75R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,623.99 or pivot resistance near 1,657.20; sell the rejection, not the touch
- entry 1,657.20 | stop 1,672.61 | T1 1,622.03 | T2 1,605.84
- R:R 2.28 at T1, 3.33 at T2 | risk 15.41
- invalid: 5m close above 1,672.61: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.28R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$15.41-$19.26); funding runs -0.0509%/day ($-0.21/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
