# ETH perp (Hyperliquid) - 2026-11-21 15:03 UTC+05:30 (09:33 UTC)
spot 1,637.55 | mark 1,637.70 | oracle 1,638.70 | OI 593,430.42 ETH (+0.308% vs last run, -3.31% 24h)
funding +0.00020%/hr (~+1.71%/yr, 14th pct of last 500h) | 24h notional $2,506.9m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,688.94 / 1,816.55) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 22% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 14th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -3.3%, price -6.2%: no edge | 0 |

## 2) Intraday regime - trend-down, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,710.00 | POC 1,816.25 | VAH 1,972.50 (width 262.50 = 16.03% of spot, 240 bars)
- developing session (40% elapsed): VAL 1,542.50 | POC 1,563.25 | VAH 1,620.00
- session VWAP 1,587.99 (+1s 1,620.41 / -1s 1,555.57) | prior session VWAP 1,661.47
- prior day: PDH 1,769.70 | PDL 1,580.00 | PDC 1,621.90 (PDH intact, PDL swept)
- floor pivots: S3 1,355.00 | S2 1,467.50 | S1 1,544.70 | P 1,657.20 | R1 1,734.40 | R2 1,846.90 | R3 1,924.10
- 1H ATR(14) 30.94 = 1.89% of spot | ATR vs 30d median x1.18
- distance to POC -5.77 ATR | VAH -10.82 ATR | VAL -2.34 ATR | closes outside value (last 20): 90%
- cross-venue funding: BinPerp +0.00032%/hr, BybitPerp +0.00080%/hr, HlPerp +0.00014%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 2.3 ATR below VAL 1,710.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,710.00 | stop 1,564.53 | T1 1,816.25 | T2 1,972.50
- R:R 0.73 at T1, 1.80 at T2 | risk 145.47
- invalid: 5m close below 1,564.53: the sweep was acceptance
- verdict: STAND ASIDE - T1 pays 0.73R, below the 1.5R floor

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 2.3 ATR below VAL 1,710.00; short the retest that fails at it
- entry 1,710.00 | stop 1,733.21 | T1 1,580.00 | T2 1,544.70
- R:R 5.60 at T1, 7.12 at T2 | risk 23.21
- invalid: 1H close back inside value (above 1,710.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 5.60R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,587.99 or pivot resistance near 1,657.20; sell the rejection, not the touch
- entry 1,657.20 | stop 1,675.77 | T1 1,595.31 | T2 1,580.00
- R:R 3.33 at T1, 4.16 at T2 | risk 18.57
- invalid: 5m close above 1,675.77: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.60-0.75x the 1H ATR (~$18.57-$23.21); funding runs +0.0047%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
