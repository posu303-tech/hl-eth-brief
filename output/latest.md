# ETH perp (Hyperliquid) - 2026-11-03 11:55 UTC+05:30 (06:25 UTC)
spot 2,247.85 | mark 2,247.70 | oracle 2,248.40 | OI 961,772.86 ETH (+0.313% vs last run, -2.38% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $924.1m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,265.92 / 2,294.78) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 21% of prior range | -1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -2.4%, price -1.6%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,254.00 | POC 2,326.50 | VAH 2,369.00 (width 115.00 = 5.12% of spot, 240 bars)
- developing session (27% elapsed): VAL 2,250.00 | POC 2,258.50 | VAH 2,262.00
- session VWAP 2,253.85 (+1s 2,258.88 / -1s 2,248.82) | prior session VWAP 2,272.93
- prior day: PDH 2,315.20 | PDL 2,236.10 | PDC 2,252.50 (PDH intact, PDL intact)
- floor pivots: S3 2,141.57 | S2 2,188.83 | S1 2,220.67 | P 2,267.93 | R1 2,299.77 | R2 2,347.03 | R3 2,378.87
- 1H ATR(14) 13.61 = 0.61% of spot | ATR vs 30d median x1.03
- distance to POC -5.78 ATR | VAH -8.90 ATR | VAL -0.45 ATR | closes outside value (last 20): 35%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00117%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.5 ATR below VAL 2,254.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,254.00 | stop 2,229.29 | T1 2,326.50 | T2 2,369.00
- R:R 2.93 at T1, 4.65 at T2 | risk 24.71
- invalid: 5m close below 2,229.29: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.93R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.5 ATR below VAL 2,254.00; short the retest that fails at it
- entry 2,254.00 | stop 2,264.21 | T1 2,236.10 | T2 2,220.67
- R:R 1.75 at T1, 3.26 at T2 | risk 10.21
- invalid: 1H close back inside value (above 2,254.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 1.75R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 2,253.85 or pivot resistance near 2,253.85; sell the rejection, not the touch
- entry 2,253.85 | stop 2,262.02 | T1 2,236.10 | T2 2,226.62
- R:R 2.17 at T1, 3.33 at T2 | risk 8.17
- invalid: 5m close above 2,262.02: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.17R)

## 4) Risk note
Stops sit 0.60-1.81x the 1H ATR (~$8.17-$24.71); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
