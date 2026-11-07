# ETH perp (Hyperliquid) - 2026-11-07 15:23 UTC+05:30 (09:53 UTC)
spot 2,245.55 | mark 2,245.40 | oracle 2,246.00 | OI 976,359.00 ETH (-0.186% vs last run, +0.71% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $437.4m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,263.26 / 2,292.41) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 66% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +0.7%, price +0.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,329.00 (width 113.00 = 5.03% of spot, 240 bars)
- developing session (41% elapsed): VAL 2,242.00 | POC 2,246.50 | VAH 2,248.00
- session VWAP 2,244.81 (+1s 2,247.32 / -1s 2,242.30) | prior session VWAP 2,231.98
- prior day: PDH 2,253.20 | PDL 2,208.40 | PDC 2,238.10 (PDH intact, PDL intact)
- floor pivots: S3 2,168.47 | S2 2,188.43 | S1 2,213.27 | P 2,233.23 | R1 2,258.07 | R2 2,278.03 | R3 2,302.87
- 1H ATR(14) 11.65 = 0.52% of spot | ATR vs 30d median x0.60
- distance to POC -0.25 ATR | VAH -7.16 ATR | VAL +2.54 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00059%/hr, BybitPerp +0.00095%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,210.17 | T1 2,248.50 | T2 2,329.00
- R:R 5.58 at T1, 19.39 at T2 | risk 5.83
- invalid: 5m close below 2,210.17: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 5.58R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,329.00 while still inside value; buy the confirmation, not the poke
- entry 2,330.17 | stop 2,323.17 | T1 2,443.17 | T2 2,351.14
- R:R 16.16 at T1, 3.00 at T2 | risk 6.99
- invalid: 1H close back below 2,329.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 16.16R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,244.81 or pivot support near 2,233.23; buy the hold, not the touch
- entry 2,233.23 | stop 2,226.24 | T1 2,247.32 | T2 2,253.20
- R:R 2.01 at T1, 2.86 at T2 | risk 6.99
- invalid: 5m close below 2,226.24: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.01R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$5.83-$6.99); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
