# ETH perp (Hyperliquid) - 2026-11-14 15:35 UTC+05:30 (10:05 UTC)
spot 1,910.05 | mark 1,910.20 | oracle 1,911.26 | OI 699,469.66 ETH (-2.580% vs last run, -5.55% 24h)
funding -0.00068%/hr (~-5.99%/yr, 5th pct of last 500h) | 24h notional $917.5m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,958.15 / 2,083.76) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 27% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 5th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -5.5%, price -2.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,895.00 | POC 2,124.25 | VAH 2,235.50 (width 340.50 = 17.83% of spot, 240 bars)
- developing session (42% elapsed): VAL 1,883.50 | POC 1,903.25 | VAH 1,907.50
- session VWAP 1,900.49 (+1s 1,912.95 / -1s 1,888.03) | prior session VWAP 1,946.03
- prior day: PDH 2,020.40 | PDL 1,894.90 | PDC 1,928.70 (PDH intact, PDL swept)
- floor pivots: S3 1,750.10 | S2 1,822.50 | S1 1,875.60 | P 1,948.00 | R1 2,001.10 | R2 2,073.50 | R3 2,126.60
- 1H ATR(14) 20.48 = 1.07% of spot | ATR vs 30d median x0.97
- distance to POC -10.46 ATR | VAH -15.89 ATR | VAL +0.73 ATR | closes outside value (last 20): 10%
- cross-venue funding: BinPerp +0.00069%/hr, BybitPerp +0.00052%/hr, HlPerp -0.00068%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,895.00; enter on the reclaim
- entry 1,895.00 | stop 1,884.76 | T1 2,124.25 | T2 2,235.50
- R:R 22.38 at T1, 33.25 at T2 | risk 10.24
- invalid: 5m close below 1,884.76: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 22.38R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,235.50 while still inside value; buy the confirmation, not the poke
- entry 2,237.55 | stop 2,225.26 | T1 2,578.05 | T2 2,274.42
- R:R 27.71 at T1, 3.00 at T2 | risk 12.29
- invalid: 1H close back below 2,235.50: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 27.71R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,900.49 or pivot support near 1,900.49; buy the hold, not the touch
- entry 1,900.49 | stop 1,888.20 | T1 1,912.95 | T2 1,941.46
- R:R 1.01 at T1, 3.33 at T2 | risk 12.29
- invalid: 5m close below 1,888.20: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.01R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$10.24-$12.29); funding runs -0.0164%/day ($-0.07/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
