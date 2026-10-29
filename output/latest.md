# ETH perp (Hyperliquid) - 2026-10-29 06:15 UTC+05:30 (00:45 UTC)
spot 2,355.75 | mark 2,355.80 | oracle 2,357.01 | OI 1,111,247.29 ETH (-0.366% vs last run, -1.60% 24h)
funding +0.00022%/hr (~+1.91%/yr, 16th pct of last 500h) | 24h notional $768.8m

## 1) HTF bias - BALANCED (+2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,345.78 / 2,368.13) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 52% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 16th pct of trailing history (crowded longs = headwind) | +1 |
| OI 24h | OI -1.6%, price +0.4%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,306.00 | POC 2,400.50 | VAH 2,417.00 (width 111.00 = 4.71% of spot, 240 bars)
- developing session (3% elapsed): VAL 2,355.00 | POC 2,358.50 | VAH 2,360.00
- session VWAP 2,356.98 (+1s 2,358.36 / -1s 2,355.59) | prior session VWAP 2,355.95
- prior day: PDH 2,391.00 | PDL 2,322.70 | PDC 2,358.40 (PDH intact, PDL intact)
- floor pivots: S3 2,255.43 | S2 2,289.07 | S1 2,323.73 | P 2,357.37 | R1 2,392.03 | R2 2,425.67 | R3 2,460.33
- 1H ATR(14) 16.42 = 0.70% of spot | ATR vs 30d median x1.15
- distance to POC -2.73 ATR | VAH -3.73 ATR | VAL +3.03 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00073%/hr, BybitPerp +0.00125%/hr, HlPerp +0.00023%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,306.00; enter on the reclaim
- entry 2,306.00 | stop 2,297.79 | T1 2,400.50 | T2 2,417.00
- R:R 11.51 at T1, 13.52 at T2 | risk 8.21
- invalid: 5m close below 2,297.79: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 11.51R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,417.00 while still inside value; buy the confirmation, not the poke
- entry 2,418.64 | stop 2,408.79 | T1 2,425.67 | T2 2,460.33
- R:R 0.71 at T1, 4.23 at T2 | risk 9.85
- invalid: 1H close back below 2,417.00: the expansion failed, mirror the short at VAL
- verdict: STAND ASIDE - T1 pays 0.71R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,356.98 or pivot support near 2,323.73; buy the hold, not the touch
- entry 2,323.73 | stop 2,313.88 | T1 2,356.57 | T2 2,391.00
- R:R 3.33 at T1, 6.83 at T2 | risk 9.85
- invalid: 5m close below 2,313.88: the confluence level is lost
- verdict: valid only if the trigger prints (T1 3.33R)

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$8.21-$9.85); funding runs +0.0052%/day ($+0.02/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
