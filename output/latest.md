# ETH perp (Hyperliquid) - 2026-11-29 00:17 UTC+05:30 (18:47 UTC)
spot 1,648.25 | mark 1,648.20 | oracle 1,649.09 | OI 625,477.66 ETH (+3.617% vs last run, +4.00% 24h)
funding +0.00116%/hr (~+10.13%/yr, 52th pct of last 500h) | 24h notional $336.6m

## 1) HTF bias - BEARISH (-4 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (1,671.86 / 1,707.99) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 22% of prior range | -1 |
| 20-bar structure | 1H swings lower | -1 |
| Funding percentile | 52th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | OI +4.0% with price -1.1%: new shorts | -1 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,621.00 | POC 1,683.75 | VAH 1,763.00 (width 142.00 = 8.62% of spot, 240 bars)
- developing session (78% elapsed): VAL 1,640.00 | POC 1,645.75 | VAH 1,656.50
- session VWAP 1,650.79 (+1s 1,658.95 / -1s 1,642.62) | prior session VWAP 1,696.74
- prior day: PDH 1,762.40 | PDL 1,633.00 | PDC 1,661.80 (PDH intact, PDL intact)
- floor pivots: S3 1,479.67 | S2 1,556.33 | S1 1,609.07 | P 1,685.73 | R1 1,738.47 | R2 1,815.13 | R3 1,867.87
- 1H ATR(14) 11.71 = 0.71% of spot | ATR vs 30d median x0.87
- distance to POC -3.03 ATR | VAH -9.80 ATR | VAL +2.33 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00062%/hr, BybitPerp -0.00017%/hr, HlPerp +0.00117%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 1,621.00; enter on the reclaim
- entry 1,621.00 | stop 1,615.15 | T1 1,683.75 | T2 1,763.00
- R:R 10.72 at T1, 24.26 at T2 | risk 5.85
- invalid: 5m close below 1,615.15: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 10.72R)

**S2 - Range expansion (short below VAL)** [SHORT]
- trigger: 1H close below VAL 1,621.00 while still inside value; sell the confirmation, not the poke
- entry 1,619.83 | stop 1,626.85 | T1 1,609.07 | T2 1,556.33
- R:R 1.53 at T1, 9.04 at T2 | risk 7.02
- invalid: 1H close back above 1,621.00: the expansion failed, mirror the long at VAH
- verdict: valid only if the trigger prints (T1 1.53R)

**S3 - VWAP / pivot confluence (short)** [SHORT]
- trigger: session VWAP 1,650.79 or pivot resistance near 1,650.79; sell the rejection, not the touch
- entry 1,650.79 | stop 1,657.81 | T1 1,642.62 | T2 1,633.00
- R:R 1.16 at T1, 2.53 at T2 | risk 7.02
- invalid: 5m close above 1,657.81: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.16R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$5.85-$7.02); funding runs +0.0278%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
