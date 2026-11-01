# ETH perp (Hyperliquid) - 2026-11-02 00:59 UTC+05:30 (19:29 UTC)
spot 2,259.75 | mark 2,259.80 | oracle 2,260.82 | OI 977,600.04 ETH (-0.582% vs last run, +0.03% 24h)
funding +0.00067%/hr (~+5.84%/yr, 29th pct of last 500h) | 24h notional $272.9m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,262.15 / 2,304.98) | -1 |
| 10-session value | price below the value area | -1 |
| Prior day close | closed at 64% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 29th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +0.0%, price +0.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price BELOW value

- value area (10 UTC sessions, 70%): VAL 2,262.00 | POC 2,326.50 | VAH 2,413.00 (width 151.00 = 6.68% of spot, 240 bars)
- developing session (81% elapsed): VAL 2,264.00 | POC 2,268.50 | VAH 2,272.00
- session VWAP 2,266.98 (+1s 2,271.29 / -1s 2,262.68) | prior session VWAP 2,247.80
- prior day: PDH 2,266.10 | PDL 2,235.00 | PDC 2,254.80 (PDH swept, PDL intact)
- floor pivots: S3 2,206.73 | S2 2,220.87 | S1 2,237.83 | P 2,251.97 | R1 2,268.93 | R2 2,283.07 | R3 2,300.03
- 1H ATR(14) 7.76 = 0.34% of spot | ATR vs 30d median x0.84
- distance to POC -8.60 ATR | VAH -19.74 ATR | VAL -0.29 ATR | closes outside value (last 20): 15%
- cross-venue funding: BinPerp -0.00001%/hr, BybitPerp -0.00007%/hr, HlPerp +0.00066%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Failed auction (long back into value)** [LONG]
- trigger: price is 0.3 ATR below VAL 2,262.00; arm only on a 5m close back above it, which is what confirms the failure
- entry 2,262.00 | stop 2,231.12 | T1 2,326.50 | T2 2,413.00
- R:R 2.09 at T1, 4.89 at T2 | risk 30.88
- invalid: 5m close below 2,231.12: the sweep was acceptance
- verdict: valid only if the trigger prints (T1 2.09R)

**S2 - Acceptance and retest (short VAL)** [SHORT]
- trigger: price has been accepted 0.3 ATR below VAL 2,262.00; short the retest that fails at it
- entry 2,262.00 | stop 2,267.82 | T1 2,237.83 | T2 2,220.87
- R:R 4.15 at T1, 7.06 at T2 | risk 5.82
- invalid: 1H close back inside value (above 2,262.00) voids the acceptance
- verdict: valid only if the trigger prints (T1 4.15R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,266.98 or pivot support near 2,251.97; buy the hold, not the touch
- entry 2,251.97 | stop 2,247.31 | T1 2,266.10 | T2 2,271.29
- R:R 3.03 at T1, 4.15 at T2 | risk 4.66
- invalid: 5m close below 2,247.31: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.03R)

## 4) Risk note
Stops sit 0.60-3.98x the 1H ATR (~$4.66-$30.88); funding runs +0.0160%/day ($+0.07/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
