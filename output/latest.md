# ETH perp (Hyperliquid) - 2026-10-28 06:37 UTC+05:30 (01:07 UTC)
spot 2,341.95 | mark 2,341.90 | oracle 2,342.82 | OI 1,129,259.09 ETH (-0.365% vs last run, +0.66% 24h)
funding +0.00125%/hr (~+10.95%/yr, 100th pct of last 500h) | 24h notional $697.3m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (2,333.25 / 2,371.75) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 79% of prior range | +1 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 100th pct of trailing history (crowded longs = headwind) | -1 |
| OI 24h | OI +0.7%, price +0.5%: no edge | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 2,314.00 | POC 2,400.50 | VAH 2,429.00 (width 115.00 = 4.91% of spot, 240 bars)
- developing session (5% elapsed): VAL 2,344.00 | POC 2,345.50 | VAH 2,348.00
- session VWAP 2,345.46 (+1s 2,347.09 / -1s 2,343.83) | prior session VWAP 2,329.40
- prior day: PDH 2,364.10 | PDL 2,296.20 | PDC 2,349.70 (PDH intact, PDL intact)
- floor pivots: S3 2,241.33 | S2 2,268.77 | S1 2,309.23 | P 2,336.67 | R1 2,377.13 | R2 2,404.57 | R3 2,445.03
- 1H ATR(14) 14.08 = 0.60% of spot | ATR vs 30d median x0.90
- distance to POC -4.16 ATR | VAH -6.18 ATR | VAL +1.98 ATR | closes outside value (last 20): 20%
- cross-venue funding: BinPerp +0.00101%/hr, BybitPerp +0.00106%/hr, HlPerp +0.00125%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (long from VAL)** [LONG]
- trigger: 5m close back inside value after tagging VAL 2,314.00; enter on the reclaim
- entry 2,314.00 | stop 2,306.96 | T1 2,400.50 | T2 2,429.00
- R:R 12.28 at T1, 16.33 at T2 | risk 7.04
- invalid: 5m close below 2,306.96: value rejected lower, stand down
- verdict: valid only if the trigger prints (T1 12.28R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 2,429.00 while still inside value; buy the confirmation, not the poke
- entry 2,430.41 | stop 2,421.96 | T1 2,445.03 | T2 2,545.41
- R:R 1.73 at T1, 13.61 at T2 | risk 8.45
- invalid: 1H close back below 2,429.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 1.73R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 2,345.46 or pivot support near 2,336.67; buy the hold, not the touch
- entry 2,336.67 | stop 2,328.22 | T1 2,347.09 | T2 2,364.10
- R:R 1.23 at T1, 3.25 at T2 | risk 8.45
- invalid: 5m close below 2,328.22: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.23R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.04-$8.45); funding runs +0.0300%/day ($+0.12/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
