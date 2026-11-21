# ETH perp (Hyperliquid) - 2026-11-21 22:48 UTC+05:30 (17:18 UTC)
spot 1,685.15 | mark 1,685.20 | oracle 1,686.03 | OI 585,820.07 ETH (-1.282% vs last run, -5.09% 24h)
funding +0.00048%/hr (~+4.23%/yr, 19th pct of last 500h) | 24h notional $2,056.9m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,683.94 / 1,805.24) | 0 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 22% of prior range | -1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 19th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -5.1%, price +3.4%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,710.00 | POC 1,816.25 | VAH 1,972.50 (width 262.50 = 15.58% of spot, 240 bars)
- developing session (72% elapsed): VAL 1,542.50 | POC 1,563.25 | VAH 1,646.50
- session VWAP 1,616.42 (+1s 1,668.28 / -1s 1,564.56) | prior session VWAP 1,661.47
- prior day: PDH 1,769.70 | PDL 1,580.00 | PDC 1,621.90 (PDH intact, PDL swept)
- floor pivots: S3 1,355.00 | S2 1,467.50 | S1 1,544.70 | P 1,657.20 | R1 1,734.40 | R2 1,846.90 | R3 1,924.10
- 1H ATR(14) 28.64 = 1.70% of spot | ATR vs 30d median x1.01
- distance to POC -4.58 ATR | VAH -10.03 ATR | VAL -0.87 ATR | closes outside value (last 20): 100%
- cross-venue funding: BinPerp +0.00040%/hr, BybitPerp +0.00014%/hr, HlPerp +0.00048%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.9 ATR below VAL 1,710.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,710.00 | stop 1,565.68 | T1 1,816.25 | T2 1,972.50
- R:R 0.74 at T1, 1.82 at T2 | risk 144.32
- invalid: 5m close below 1,565.68: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.74R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.9 ATR below VAL 1,710.00; short the retest that fails at it
- entry 1,710.00 | stop 1,731.48 | T1 1,580.00 | T2 1,544.70
- R:R 6.05 at T1, 7.70 at T2 | risk 21.48
- invalid: 1H close back inside value (above 1,710.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 6.05R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,616.42 or pivot support near 1,657.20; buy the hold, not the touch
- entry 1,657.20 | stop 1,640.02 | T1 1,714.48 | T2 1,734.40
- R:R 3.33 at T1, 4.49 at T2 | risk 17.18
- invalid: 5m close below 1,640.02: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$17.18-$21.48); funding runs +0.0116%/day ($+0.05/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
