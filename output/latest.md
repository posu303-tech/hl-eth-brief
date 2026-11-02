# ETH perp (Hyperliquid) - 2026-11-02 11:13 UTC+05:30 (05:43 UTC)
spot 2,295.35 | mark 2,295.30 | oracle 2,296.10 | OI 985,206.95 ETH (+1.471% vs last run, +0.07% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $394.2m

## 1) HTF bias - BALANCED (+0 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,267.76 / 2,302.40) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 92% of prior range | +1 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +0.1%, price +1.3%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,250.00 | POC 2,326.50 | VAH 2,374.00 (width 124.00 = 5.40% of spot, 240 bars)
- developing session (24% elapsed): VAL 2,284.00 | POC 2,294.50 | VAH 2,309.00
- session VWAP 2,293.81 (+1s 2,305.30 / -1s 2,282.33) | prior session VWAP 2,266.31
- prior day: PDH 2,276.90 | PDL 2,247.90 | PDC 2,274.60 (PDH swept, PDL intact)
- floor pivots: S3 2,227.03 | S2 2,237.47 | S1 2,256.03 | P 2,266.47 | R1 2,285.03 | R2 2,295.47 | R3 2,314.03
- 1H ATR(14) 12.02 = 0.52% of spot | ATR vs 30d median x1.40
- distance to POC -2.59 ATR | VAH -6.54 ATR | VAL +3.77 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp -0.00041%/hr, BybitPerp -0.00015%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,250.00; enter on the reclaim
- entry 2,250.00 | stop 2,243.99 | T1 2,326.50 | T2 2,374.00
- R:R 12.73 at T1, 20.63 at T2 | risk 6.01
- invalid: 5m close below 2,243.99: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.73R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,374.00 while still inside value; buy the confirmation, not the poke
- entry 2,375.20 | stop 2,367.99 | T1 2,499.20 | T2 2,396.84
- R:R 17.19 at T1, 3.00 at T2 | risk 7.21
- invalid: 1H close back below 2,374.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 17.19R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,293.81 or pivot support near 2,266.47; buy the hold, not the touch
- entry 2,266.47 | stop 2,259.25 | T1 2,276.90 | T2 2,285.03
- R:R 1.45 at T1, 2.57 at T2 | risk 7.21
- invalid: 5m close below 2,259.25: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.45R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$6.01-$7.21); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
