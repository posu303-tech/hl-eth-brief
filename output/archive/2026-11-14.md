# ETH perp (Hyperliquid) - 2026-11-14 08:30 UTC+05:30 (03:00 UTC)
spot 1,910.65 | mark 1,911.00 | oracle 1,912.21 | OI 717,995.18 ETH (+0.166% vs last run, -2.02% 24h)
funding -0.00102%/hr (~-8.97%/yr, 3th pct of last 500h) | 24h notional $1,372.4m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,977.03 / 2,097.13) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 27% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 3th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -2.0%, price -4.0%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,895.00 | POC 2,124.25 | VAH 2,235.50 (width 340.50 = 17.82% of spot, 240 bars)
- developing session (13% elapsed): VAL 1,896.00 | POC 1,929.75 | VAH 1,936.00
- session VWAP 1,905.74 (+1s 1,920.96 / -1s 1,890.52) | prior session VWAP 1,946.03
- prior day: PDH 2,020.40 | PDL 1,894.90 | PDC 1,928.70 (PDH intact, PDL swept)
- floor pivots: S3 1,750.10 | S2 1,822.50 | S1 1,875.60 | P 1,948.00 | R1 2,001.10 | R2 2,073.50 | R3 2,126.60
- 1H ATR(14) 21.11 = 1.10% of spot | ATR vs 30d median x1.00
- distance to POC -10.12 ATR | VAH -15.39 ATR | VAL +0.74 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00008%/hr, BybitPerp +0.00012%/hr, HlPerp -0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,895.00; enter on the reclaim
- entry 1,895.00 | stop 1,884.45 | T1 2,124.25 | T2 2,235.50
- R:R 21.72 at T1, 32.27 at T2 | risk 10.55
- invalid: 5m close below 1,884.45: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 21.72R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,235.50 while still inside value; buy the confirmation, not the poke
- entry 2,237.61 | stop 2,224.95 | T1 2,578.11 | T2 2,275.60
- R:R 26.89 at T1, 3.00 at T2 | risk 12.66
- invalid: 1H close back below 2,235.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 26.89R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,905.74 or pivot support near 1,905.74; buy the hold, not the touch
- entry 1,905.74 | stop 1,893.08 | T1 1,920.96 | T2 1,947.95
- R:R 1.20 at T1, 3.33 at T2 | risk 12.66
- invalid: 5m close below 1,893.08: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.20R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$10.55-$12.66); funding runs -0.0246%/day ($-0.10/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
