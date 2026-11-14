# ETH perp (Hyperliquid) - 2026-11-15 02:47 UTC+05:30 (21:17 UTC)
spot 1,765.85 | mark 1,766.30 | oracle 1,767.60 | OI 665,240.03 ETH (-3.272% vs last run, -7.19% 24h)
funding -0.00370%/hr (~-32.39%/yr, 1th pct of last 500h) | 24h notional $1,574.4m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,920.16 / 2,059.92) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 27% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 1th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -7.2%, price -8.9%: no edge | 0 |

## 2) Intraday regime - breakout-attempt, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,895.00 | POC 2,124.25 | VAH 2,235.50 (width 340.50 = 19.28% of spot, 240 bars)
- developing session (89% elapsed): VAL 1,810.00 | POC 1,838.25 | VAH 1,897.50
- session VWAP 1,849.23 (+1s 1,890.09 / -1s 1,808.36) | prior session VWAP 1,946.03
- prior day: PDH 2,020.40 | PDL 1,894.90 | PDC 1,928.70 (PDH intact, PDL swept)
- floor pivots: S3 1,750.10 | S2 1,822.50 | S1 1,875.60 | P 1,948.00 | R1 2,001.10 | R2 2,073.50 | R3 2,126.60
- 1H ATR(14) 26.55 = 1.50% of spot | ATR vs 30d median x1.26
- distance to POC -13.50 ATR | VAH -17.69 ATR | VAL -4.86 ATR | closes outside value (last 20): 50%
- cross-venue funding: BinPerp -0.00045%/hr, BybitPerp -0.00022%/hr, HlPerp -0.00372%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 4.9 ATR below VAL 1,895.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,895.00 | stop 1,752.57 | T1 2,124.25 | T2 2,235.50
- R:R 1.61 at T1, 2.39 at T2 | risk 142.43
- invalid: 5m close below 1,752.57: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 1.61R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 4.9 ATR below VAL 1,895.00; short the retest that fails at it
- entry 1,895.00 | stop 1,914.92 | T1 1,875.60 | T2 1,822.50
- R:R 0.97 at T1, 3.64 at T2 | risk 19.92
- invalid: 1H close back inside value (above 1,895.00) voids the acceptance
- verdict: STAND ASIDE - T1 pays 0.97R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,849.23 or pivot resistance near 1,849.23; sell the rejection, not the touch
- entry 1,849.23 | stop 1,865.16 | T1 1,808.36 | T2 1,796.12
- R:R 2.57 at T1, 3.33 at T2 | risk 15.93
- invalid: 5m close above 1,865.16: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.57R)

## 4) Risk note
Stops sit 0.60-5.36x the 1H ATR (~$15.93-$142.43); funding runs -0.0887%/day ($-0.37/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
