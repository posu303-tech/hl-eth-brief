# ETH perp (Hyperliquid) - 2026-11-21 01:26 UTC+05:30 (19:56 UTC)
spot 1,611.65 | mark 1,612.20 | oracle 1,613.10 | OI 617,205.46 ETH (+0.561% vs last run, +0.96% 24h)
funding -0.00172%/hr (~-15.08%/yr, 3th pct of last 500h) | 24h notional $1,797.3m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,749.05 / 1,847.74) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 26% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 3th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI +1.0%, price -8.9%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,710.50 | POC 1,816.25 | VAH 1,976.00 (width 265.50 = 16.47% of spot, 240 bars)
- developing session (83% elapsed): VAL 1,580.00 | POC 1,641.25 | VAH 1,725.00
- session VWAP 1,670.56 (+1s 1,725.38 / -1s 1,615.75) | prior session VWAP 1,778.27
- prior day: PDH 1,816.40 | PDL 1,735.30 | PDC 1,756.60 (PDH intact, PDL swept)
- floor pivots: S3 1,641.37 | S2 1,688.33 | S1 1,722.47 | P 1,769.43 | R1 1,803.57 | R2 1,850.53 | R3 1,884.67
- 1H ATR(14) 28.07 = 1.74% of spot | ATR vs 30d median x1.39
- distance to POC -7.29 ATR | VAH -12.98 ATR | VAL -3.52 ATR | closes outside value (last 20): 20%
- cross-venue funding: BinPerp -0.00169%/hr, BybitPerp -0.00155%/hr, HlPerp -0.00172%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.5 ATR below VAL 1,710.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,710.50 | stop 1,597.62 | T1 1,816.25 | T2 1,976.00
- R:R 0.94 at T1, 2.35 at T2 | risk 112.88
- invalid: 5m close below 1,597.62: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.94R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.5 ATR below VAL 1,710.50; short the retest that fails at it
- entry 1,710.50 | stop 1,731.55 | T1 1,688.33 | T2 1,641.37
- R:R 1.05 at T1, 3.28 at T2 | risk 21.05
- invalid: 1H close back inside value (above 1,710.50) voids the acceptance
- verdict: STAND ASIDE - T1 pays 1.05R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,670.56 or pivot resistance near 1,670.56; sell the rejection, not the touch
- entry 1,670.56 | stop 1,687.40 | T1 1,615.75 | T2 1,620.05
- R:R 3.26 at T1, 3.00 at T2 | risk 16.84
- invalid: 5m close above 1,687.40: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.26R)

## 4) Risk note
Stops sit 0.60-0.60x the 1H ATR (~$16.84-$16.84); funding runs -0.0413%/day ($-0.17/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
