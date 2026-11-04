# ETH perp (Hyperliquid) - 2026-11-04 14:26 UTC+05:30 (08:56 UTC)
spot 2,323.95 | mark 2,324.00 | oracle 2,323.82 | OI 1,029,339.18 ETH (+1.704% vs last run, +7.03% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,138.0m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,275.10 / 2,291.23) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 49% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +7.0% with price +3.0%: new longs | +1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,221.00 | POC 2,251.50 | VAH 2,328.00 (width 107.00 = 4.60% of spot, 240 bars)
- developing session (37% elapsed): VAL 2,227.00 | POC 2,263.50 | VAH 2,294.00
- session VWAP 2,276.94 (+1s 2,301.95 / -1s 2,251.93) | prior session VWAP 2,279.88
- prior day: PDH 2,309.40 | PDL 2,240.40 | PDC 2,274.50 (PDH swept, PDL swept)
- floor pivots: S3 2,171.13 | S2 2,205.77 | S1 2,240.13 | P 2,274.77 | R1 2,309.13 | R2 2,343.77 | R3 2,378.13
- 1H ATR(14) 18.34 = 0.79% of spot | ATR vs 30d median x1.28
- distance to POC +3.95 ATR | VAH -0.22 ATR | VAL +5.61 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00125%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (short from VAH)** [SHORT]
- trigger: 5m close back inside value after tagging VAH 2,328.00; enter on the loss of the edge
- entry 2,328.00 | stop 2,337.17 | T1 2,251.50 | T2 2,221.00
- R:R 8.34 at T1, 11.67 at T2 | risk 9.17
- invalid: 5m close above 2,337.17: acceptance higher, stand down
- verdict: valid only if the trigger prints (T1 8.34R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,328.00 while still inside value; buy the confirmation, not the poke
- entry 2,329.83 | stop 2,318.83 | T1 2,343.77 | T2 2,378.13
- R:R 1.27 at T1, 4.39 at T2 | risk 11.00
- invalid: 1H close back below 2,328.00: the expansion failed, mirror the short at VAL
- verdict: STAND ASIDE - T1 pays 1.27R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,276.94 or pivot support near 2,276.94; buy the hold, not the touch
- entry 2,276.94 | stop 2,265.93 | T1 2,301.95 | T2 2,309.40
- R:R 2.27 at T1, 2.95 at T2 | risk 11.00
- invalid: 5m close below 2,265.93: the confluence level is lost
- verdict: valid only if the trigger prints (T1 2.27R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$9.17-$11.00); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
