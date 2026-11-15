# ETH perp (Hyperliquid) - 2026-11-15 07:13 UTC+05:30 (01:43 UTC)
spot 1,721.95 | mark 1,722.40 | oracle 1,723.66 | OI 642,520.76 ETH (-3.415% vs last run, -10.51% 24h)
funding -0.00263%/hr (~-23.03%/yr, 2th pct of last 500h) | 24h notional $2,032.2m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,895.81 / 2,047.99) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 19% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 2th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -10.5%, price -10.8%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 1,829.50 | POC 2,124.25 | VAH 2,166.00 (width 336.50 = 19.54% of spot, 240 bars)
- developing session (7% elapsed): VAL 1,713.00 | POC 1,721.75 | VAH 1,753.00
- session VWAP 1,740.63 (+1s 1,757.25 / -1s 1,724.00) | prior session VWAP 1,830.31
- prior day: PDH 1,936.00 | PDL 1,727.80 | PDC 1,768.00 (PDH intact, PDL swept)
- floor pivots: S3 1,477.00 | S2 1,602.40 | S1 1,685.20 | P 1,810.60 | R1 1,893.40 | R2 2,018.80 | R3 2,101.60
- 1H ATR(14) 30.28 = 1.76% of spot | ATR vs 30d median x1.44
- distance to POC -13.29 ATR | VAH -14.67 ATR | VAL -3.55 ATR | closes outside value (last 20): 35%
- cross-venue funding: BinPerp -0.00087%/hr, BybitPerp -0.00008%/hr, HlPerp -0.00263%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 3.6 ATR below VAL 1,829.50; arm only on a 5m close back above it, which is what confirms the failure
- entry 1,829.50 | stop 1,706.81 | T1 2,124.25 | T2 2,166.00
- R:R 2.40 at T1, 2.74 at T2 | risk 122.69
- invalid: 5m close below 1,706.81: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.40R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 3.6 ATR below VAL 1,829.50; short the retest that fails at it
- entry 1,829.50 | stop 1,852.21 | T1 1,727.80 | T2 1,685.20
- R:R 4.48 at T1, 6.35 at T2 | risk 22.71
- invalid: 1H close back inside value (above 1,829.50) voids the acceptance
- verdict: valid only if the trigger prints (T1 4.48R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,740.63 or pivot resistance near 1,740.63; sell the rejection, not the touch
- entry 1,740.63 | stop 1,758.79 | T1 1,727.80 | T2 1,685.20
- R:R 0.71 at T1, 3.05 at T2 | risk 18.17
- invalid: 5m close above 1,758.79: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.71R, below the 1.5R floor

## 4) Risk note
Stops sit 0.75-4.05x the 1H ATR (~$22.71-$122.69); funding runs -0.0631%/day ($-0.26/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
