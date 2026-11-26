# ETH perp (Hyperliquid) - 2026-11-27 05:10 UTC+05:30 (23:40 UTC)
spot 1,685.05 | mark 1,685.10 | oracle 1,685.88 | OI 673,138.34 ETH (+2.653% vs last run, +5.04% 24h)
funding +0.00016%/hr (~+1.39%/yr, 22th pct of last 500h) | 24h notional $450.8m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,689.74 / 1,724.47) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 93% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 22th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +5.0% with price -0.5%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,657.50 | POC 1,683.75 | VAH 1,832.00 (width 174.50 = 10.36% of spot, 240 bars)
- developing session (99% elapsed): VAL 1,686.00 | POC 1,704.25 | VAH 1,707.50
- session VWAP 1,697.69 (+1s 1,708.06 / -1s 1,687.31) | prior session VWAP 1,653.73
- prior day: PDH 1,698.00 | PDL 1,607.40 | PDC 1,691.90 (PDH swept, PDL intact)
- floor pivots: S3 1,542.93 | S2 1,575.17 | S1 1,633.53 | P 1,665.77 | R1 1,724.13 | R2 1,756.37 | R3 1,814.73
- 1H ATR(14) 12.97 = 0.77% of spot | ATR vs 30d median x0.78
- distance to POC +0.10 ATR | VAH -11.33 ATR | VAL +2.12 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00106%/hr, BybitPerp +0.00090%/hr, HlPerp +0.00016%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (short from VAH)** [SHORT]
- trigger: 5m close back inside value after tagging VAH 1,832.00; enter on the loss of the edge
- entry 1,832.00 | stop 1,838.49 | T1 1,683.75 | T2 1,657.50
- R:R 22.86 at T1, 26.90 at T2 | risk 6.49
- invalid: 5m close above 1,838.49: acceptance higher, stand down
- verdict: valid only if the trigger prints (T1 22.86R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,832.00 while still inside value; buy the confirmation, not the poke
- entry 1,833.30 | stop 1,825.51 | T1 2,007.80 | T2 1,856.65
- R:R 22.42 at T1, 3.00 at T2 | risk 7.78
- invalid: 1H close back below 1,832.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 22.42R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,697.69 or pivot support near 1,665.77; buy the hold, not the touch
- entry 1,665.77 | stop 1,657.98 | T1 1,683.75 | T2 1,691.71
- R:R 2.31 at T1, 3.33 at T2 | risk 7.78
- invalid: 5m close below 1,657.98: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.31R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$6.49-$7.78); funding runs +0.0038%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
