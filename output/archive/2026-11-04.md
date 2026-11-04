# ETH perp (Hyperliquid) - 2026-11-04 06:42 UTC+05:30 (01:12 UTC)
spot 2,264.55 | mark 2,264.69 | oracle 2,265.35 | OI 1,012,088.40 ETH (+0.384% vs last run, +5.56% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $689.9m

## 1) HTF bias - BALANCED (-1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,274.43 / 2,292.33) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 49% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +5.6% with price +0.2%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,221.00 | POC 2,251.50 | VAH 2,328.00 (width 107.00 = 4.73% of spot, 240 bars)
- developing session (5% elapsed): VAL 2,259.00 | POC 2,266.50 | VAH 2,272.00
- session VWAP 2,267.94 (+1s 2,272.64 / -1s 2,263.25) | prior session VWAP 2,279.88
- prior day: PDH 2,309.40 | PDL 2,240.40 | PDC 2,274.50 (PDH intact, PDL intact)
- floor pivots: S3 2,171.13 | S2 2,205.77 | S1 2,240.13 | P 2,274.77 | R1 2,309.13 | R2 2,343.77 | R3 2,378.13
- 1H ATR(14) 14.59 = 0.64% of spot | ATR vs 30d median x1.02
- distance to POC +0.89 ATR | VAH -4.35 ATR | VAL +2.98 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00092%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (short from VAH)** [SHORT]
- trigger: 5m close back inside value after tagging VAH 2,328.00; enter on the loss of the edge
- entry 2,328.00 | stop 2,335.29 | T1 2,251.50 | T2 2,221.00
- R:R 10.49 at T1, 14.67 at T2 | risk 7.29
- invalid: 5m close above 2,335.29: acceptance higher, stand down
- verdict: valid only if the trigger prints (T1 10.49R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,328.00 while still inside value; buy the confirmation, not the poke
- entry 2,329.46 | stop 2,320.71 | T1 2,343.77 | T2 2,378.13
- R:R 1.63 at T1, 5.56 at T2 | risk 8.75
- invalid: 1H close back below 2,328.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 1.63R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,267.94 or pivot support near 2,240.13; buy the hold, not the touch
- entry 2,240.13 | stop 2,231.38 | T1 2,251.50 | T2 2,269.31
- R:R 1.30 at T1, 3.33 at T2 | risk 8.75
- invalid: 5m close below 2,231.38: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.30R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.29-$8.75); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
