# ETH perp (Hyperliquid) - 2026-11-12 00:03 UTC+05:30 (18:33 UTC)
spot 2,089.25 | mark 2,089.30 | oracle 2,090.18 | OI 769,293.89 ETH (-0.591% vs last run, -2.71% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $729.6m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,085.67 / 2,182.47) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 37% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -2.7%, price +2.8%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,004.00 | POC 2,124.50 | VAH 2,282.00 (width 278.00 = 13.31% of spot, 240 bars)
- developing session (77% elapsed): VAL 2,046.00 | POC 2,054.50 | VAH 2,078.00
- session VWAP 2,067.98 (+1s 2,082.51 / -1s 2,053.44) | prior session VWAP 2,060.93
- prior day: PDH 2,135.80 | PDL 2,003.70 | PDC 2,052.50 (PDH intact, PDL intact)
- floor pivots: S3 1,860.10 | S2 1,931.90 | S1 1,992.20 | P 2,064.00 | R1 2,124.30 | R2 2,196.10 | R3 2,256.40
- 1H ATR(14) 18.75 = 0.90% of spot | ATR vs 30d median x0.92
- distance to POC -1.88 ATR | VAH -10.28 ATR | VAL +4.55 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00081%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,004.00; enter on the reclaim
- entry 2,004.00 | stop 1,994.63 | T1 2,124.50 | T2 2,282.00
- R:R 12.85 at T1, 29.66 at T2 | risk 9.37
- invalid: 5m close below 1,994.63: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.85R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,282.00 while still inside value; buy the confirmation, not the poke
- entry 2,283.87 | stop 2,272.63 | T1 2,561.87 | T2 2,317.62
- R:R 24.71 at T1, 3.00 at T2 | risk 11.25
- invalid: 1H close back below 2,282.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 24.71R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,067.98 or pivot support near 2,067.98; buy the hold, not the touch
- entry 2,067.98 | stop 2,056.73 | T1 2,082.51 | T2 2,105.47
- R:R 1.29 at T1, 3.33 at T2 | risk 11.25
- invalid: 5m close below 2,056.73: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.29R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.37-$11.25); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
