# ETH perp (Hyperliquid) - 2026-11-07 21:46 UTC+05:30 (16:16 UTC)
spot 2,236.45 | mark 2,236.48 | oracle 2,237.30 | OI 967,632.07 ETH (-0.894% vs last run, -2.56% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $213.2m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,258.39 / 2,289.10) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 66% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -2.6%, price +0.7%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,216.00 | POC 2,248.50 | VAH 2,329.00 (width 113.00 = 5.05% of spot, 240 bars)
- developing session (68% elapsed): VAL 2,240.00 | POC 2,244.50 | VAH 2,248.00
- session VWAP 2,242.40 (+1s 2,246.81 / -1s 2,237.98) | prior session VWAP 2,231.98
- prior day: PDH 2,253.20 | PDL 2,208.40 | PDC 2,238.10 (PDH intact, PDL intact)
- floor pivots: S3 2,168.47 | S2 2,188.43 | S1 2,213.27 | P 2,233.23 | R1 2,258.07 | R2 2,278.03 | R3 2,302.87
- 1H ATR(14) 10.05 = 0.45% of spot | ATR vs 30d median x0.63
- distance to POC -1.20 ATR | VAH -9.21 ATR | VAL +2.03 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00101%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,216.00; enter on the reclaim
- entry 2,216.00 | stop 2,210.97 | T1 2,248.50 | T2 2,329.00
- R:R 6.47 at T1, 22.48 at T2 | risk 5.03
- invalid: 5m close below 2,210.97: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 6.47R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,329.00 while still inside value; buy the confirmation, not the poke
- entry 2,330.01 | stop 2,323.97 | T1 2,443.01 | T2 2,348.10
- R:R 18.73 at T1, 3.00 at T2 | risk 6.03
- invalid: 1H close back below 2,329.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 18.73R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,242.40 or pivot support near 2,233.23; buy the hold, not the touch
- entry 2,233.23 | stop 2,227.20 | T1 2,246.81 | T2 2,253.20
- R:R 2.25 at T1, 3.31 at T2 | risk 6.03
- invalid: 5m close below 2,227.20: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.25R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$5.03-$6.03); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
