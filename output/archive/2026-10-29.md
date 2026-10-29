# ETH perp (Hyperliquid) - 2026-10-29 19:35 UTC+05:30 (14:05 UTC)
spot 2,326.05 | mark 2,326.30 | oracle 2,326.91 | OI 1,131,590.55 ETH (+3.225% vs last run, -0.44% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $995.8m

## 1) HTF bias - BALANCED (-2 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | price < EMA50 < EMA200 (2,335.01 / 2,361.92) | -1 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 52% of prior range | 0 |
| 20-bar structure | 1H swings mixed | 0 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI -0.4%, price -0.2%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,306.00 | POC 2,400.50 | VAH 2,417.00 (width 111.00 = 4.77% of spot, 240 bars)
- developing session (59% elapsed): VAL 2,304.00 | POC 2,307.50 | VAH 2,324.00
- session VWAP 2,315.45 (+1s 2,325.87 / -1s 2,305.04) | prior session VWAP 2,355.95
- prior day: PDH 2,391.00 | PDL 2,322.70 | PDC 2,358.40 (PDH intact, PDL swept)
- floor pivots: S3 2,255.43 | S2 2,289.07 | S1 2,323.73 | P 2,357.37 | R1 2,392.03 | R2 2,425.67 | R3 2,460.33
- 1H ATR(14) 15.26 = 0.66% of spot | ATR vs 30d median x0.98
- distance to POC -4.88 ATR | VAH -5.96 ATR | VAL +1.31 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00119%/hr, BybitPerp +0.00081%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,306.00; enter on the reclaim
- entry 2,306.00 | stop 2,298.37 | T1 2,400.50 | T2 2,417.00
- R:R 12.38 at T1, 14.55 at T2 | risk 7.63
- invalid: 5m close below 2,298.37: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.38R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,417.00 while still inside value; buy the confirmation, not the poke
- entry 2,418.53 | stop 2,409.37 | T1 2,425.67 | T2 2,460.33
- R:R 0.78 at T1, 4.57 at T2 | risk 9.16
- invalid: 1H close back below 2,417.00: the expansion failed, mirror the short at VAL
- verdict: STAND ASIDE - T1 pays 0.78R, below the 1.5R floor

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,315.45 or pivot support near 2,315.45; buy the hold, not the touch
- entry 2,315.45 | stop 2,306.30 | T1 2,325.87 | T2 2,345.98
- R:R 1.14 at T1, 3.33 at T2 | risk 9.16
- invalid: 5m close below 2,306.30: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.14R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.50x the 1H ATR (~$7.63-$7.63); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
