# ETH perp (Hyperliquid) - 2026-11-07 08:09 UTC+05:30 (02:39 UTC)
spot 2,246.05 | mark 2,246.00 | oracle 2,246.57 | OI 978,182.93 ETH (+0.043% vs last run, +1.94% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $536.8m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,268.68 / 2,295.74) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 66% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +1.9% with price +0.3%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,329.00 (width 113.00 = 5.03% of spot, 240 bars)
- developing session (11% elapsed): VAL 2,239.00 | POC 2,242.50 | VAH 2,246.00
- session VWAP 2,243.43 (+1s 2,246.09 / -1s 2,240.77) | prior session VWAP 2,231.98
- prior day: PDH 2,253.20 | PDL 2,208.40 | PDC 2,238.10 (PDH intact, PDL intact)
- floor pivots: S3 2,168.47 | S2 2,188.43 | S1 2,213.27 | P 2,233.23 | R1 2,258.07 | R2 2,278.03 | R3 2,302.87
- 1H ATR(14) 15.73 = 0.70% of spot | ATR vs 30d median x0.77
- distance to POC -0.16 ATR | VAH -5.27 ATR | VAL +1.91 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00115%/hr, BybitPerp +0.00081%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,208.13 | T1 2,248.50 | T2 2,329.00
- R:R 4.13 at T1, 14.37 at T2 | risk 7.87
- invalid: 5m close below 2,208.13: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 4.13R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,329.00 while still inside value; buy the confirmation, not the poke
- entry 2,330.57 | stop 2,321.13 | T1 2,443.57 | T2 2,358.89
- R:R 11.97 at T1, 3.00 at T2 | risk 9.44
- invalid: 1H close back below 2,329.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 11.97R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,243.43 or pivot support near 2,233.23; buy the hold, not the touch
- entry 2,233.23 | stop 2,223.79 | T1 2,246.09 | T2 2,253.20
- R:R 1.36 at T1, 2.12 at T2 | risk 9.44
- invalid: 5m close below 2,223.79: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.36R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.87-$9.44); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
