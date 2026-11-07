# ETH perp (Hyperliquid) - 2026-11-08 02:16 UTC+05:30 (20:46 UTC)
spot 2,229.85 | mark 2,229.35 | oracle 2,230.23 | OI 971,059.12 ETH (+0.354% vs last run, -0.69% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $172.5m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,254.91 / 2,286.97) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 66% of prior range | +1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -0.7%, price -0.1%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,329.00 (width 113.00 = 5.07% of spot, 240 bars)
- developing session (87% elapsed): VAL 2,235.00 | POC 2,244.50 | VAH 2,249.00
- session VWAP 2,240.09 (+1s 2,245.45 / -1s 2,234.74) | prior session VWAP 2,231.98
- prior day: PDH 2,253.20 | PDL 2,208.40 | PDC 2,238.10 (PDH intact, PDL intact)
- floor pivots: S3 2,168.47 | S2 2,188.43 | S1 2,213.27 | P 2,233.23 | R1 2,258.07 | R2 2,278.03 | R3 2,302.87
- 1H ATR(14) 8.74 = 0.39% of spot | ATR vs 30d median x0.64
- distance to POC -2.13 ATR | VAH -11.34 ATR | VAL +1.58 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00081%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,211.63 | T1 2,248.50 | T2 2,329.00
- R:R 7.44 at T1, 25.85 at T2 | risk 4.37
- invalid: 5m close below 2,211.63: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 7.44R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,329.00 while still inside value; buy the confirmation, not the poke
- entry 2,329.87 | stop 2,324.63 | T1 2,442.87 | T2 2,345.61
- R:R 21.54 at T1, 3.00 at T2 | risk 5.24
- invalid: 1H close back below 2,329.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 21.54R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,240.09 or pivot support near 2,213.27; buy the hold, not the touch
- entry 2,213.27 | stop 2,208.02 | T1 2,230.75 | T2 2,245.45
- R:R 3.33 at T1, 6.14 at T2 | risk 5.24
- invalid: 5m close below 2,208.02: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$4.37-$5.24); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
