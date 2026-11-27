# ETH perp (Hyperliquid) - 2026-11-27 23:33 UTC+05:30 (18:03 UTC)
spot 1,668.65 | mark 1,668.70 | oracle 1,669.51 | OI 601,397.83 ETH (-2.092% vs last run, -8.29% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $1,043.8m

## 1) HTF bias - BEARISH (-3 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,699.62 / 1,722.05) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 36% of prior range | 0 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -8.3%, price -1.4%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,651.50 | POC 1,683.75 | VAH 1,817.00 (width 165.50 = 9.92% of spot, 240 bars)
- developing session (75% elapsed): VAL 1,670.50 | POC 1,734.75 | VAH 1,749.50
- session VWAP 1,701.55 (+1s 1,736.18 / -1s 1,666.92) | prior session VWAP 1,697.03
- prior day: PDH 1,728.60 | PDL 1,667.10 | PDC 1,689.20 (PDH swept, PDL swept)
- floor pivots: S3 1,599.83 | S2 1,633.47 | S1 1,661.33 | P 1,694.97 | R1 1,722.83 | R2 1,756.47 | R3 1,784.33
- 1H ATR(14) 19.85 = 1.19% of spot | ATR vs 30d median x1.34
- distance to POC -0.76 ATR | VAH -7.47 ATR | VAL +0.86 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00006%/hr, BybitPerp -0.00011%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,651.50; enter on the reclaim
- entry 1,651.50 | stop 1,641.57 | T1 1,683.75 | T2 1,817.00
- R:R 3.25 at T1, 16.67 at T2 | risk 9.93
- invalid: 5m close below 1,641.57: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 3.25R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,651.50 while still inside value; sell the confirmation, not the poke
- entry 1,649.51 | stop 1,661.43 | T1 1,633.47 | T2 1,599.83
- R:R 1.35 at T1, 4.17 at T2 | risk 11.91
- invalid: 1H close back above 1,651.50: the expansion failed, mirror the long at VAH
- verdict: STAND ASIDE - T1 pays 1.35R, below the 1.5R floor

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,701.55 or pivot resistance near 1,694.97; sell the rejection, not the touch
- entry 1,694.97 | stop 1,706.88 | T1 1,683.75 | T2 1,667.10
- R:R 0.94 at T1, 2.34 at T2 | risk 11.91
- invalid: 5m close above 1,706.88: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 0.94R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.50x the 1H ATR (~$9.93-$9.93); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
