# ETH perp (Hyperliquid) - 2026-11-27 13:29 UTC+05:30 (07:59 UTC)
spot 1,734.55 | mark 1,734.41 | oracle 1,735.24 | OI 614,250.09 ETH (-8.748% vs last run, 24h n/a until the store has a day)
funding +0.00064%/hr (~+5.60%/yr, 33th pct of last 500h) | 24h notional $679.0m

## 1) HTF bias - BALANCED (+1 of +-6)

| component | read | score |
|---|---|---|
| EMA stack | mixed (1,698.05 / 1,724.05) | 0 |
| 10-session value | price inside the value area | 0 |
| Prior day close | closed at 36% of prior range | 0 |
| 20-bar structure | 1H swings higher | +1 |
| Funding percentile | 33th pct of trailing history (crowded longs = headwind) | 0 |
| OI 24h | n/a (needs a stored baseline) | 0 |

## 2) Intraday regime - rotational-balance, price INSIDE value

- value area (10 UTC sessions, 70%): VAL 1,651.50 | POC 1,683.75 | VAH 1,817.00 (width 165.50 = 9.54% of spot, 240 bars)
- developing session (33% elapsed): VAL 1,723.00 | POC 1,734.75 | VAH 1,748.50
- session VWAP 1,730.46 (+1s 1,742.55 / -1s 1,718.37) | prior session VWAP 1,697.03
- prior day: PDH 1,728.60 | PDL 1,667.10 | PDC 1,689.20 (PDH swept, PDL intact)
- floor pivots: S3 1,599.83 | S2 1,633.47 | S1 1,661.33 | P 1,694.97 | R1 1,722.83 | R2 1,756.47 | R3 1,784.33
- 1H ATR(14) 15.77 = 0.91% of spot | ATR vs 30d median x1.02
- distance to POC +3.22 ATR | VAH -5.23 ATR | VAL +5.27 ATR | closes outside value (last 20): 0%
- cross-venue funding: BinPerp +0.00089%/hr, BybitPerp +0.00052%/hr, HlPerp +0.00064%/hr

## 3) Setups (conditional - trigger first, then act)

**S1 - Value rejection (short from VAH)** [SHORT]
- trigger: 5m close back inside value after tagging VAH 1,817.00; enter on the loss of the edge
- entry 1,817.00 | stop 1,824.88 | T1 1,683.75 | T2 1,651.50
- R:R 16.90 at T1, 20.99 at T2 | risk 7.88
- invalid: 5m close above 1,824.88: acceptance higher, stand down
- verdict: valid only if the trigger prints (T1 16.90R)

**S2 - Range expansion (long above VAH)** [LONG]
- trigger: 1H close above VAH 1,817.00 while still inside value; buy the confirmation, not the poke
- entry 1,818.58 | stop 1,809.12 | T1 1,984.08 | T2 1,846.96
- R:R 17.49 at T1, 3.00 at T2 | risk 9.46
- invalid: 1H close back below 1,817.00: the expansion failed, mirror the short at VAL
- verdict: valid only if the trigger prints (T1 17.49R)

**S3 - VWAP / pivot confluence (long)** [LONG]
- trigger: session VWAP 1,730.46 or pivot support near 1,730.46; buy the hold, not the touch
- entry 1,730.46 | stop 1,721.00 | T1 1,742.55 | T2 1,761.99
- R:R 1.28 at T1, 3.33 at T2 | risk 9.46
- invalid: 5m close below 1,721.00: the confluence level is lost
- verdict: STAND ASIDE - T1 pays 1.28R, below the 1.5R floor

## 4) Risk note
Stops sit 0.50-0.60x the 1H ATR (~$7.88-$9.46); funding runs +0.0153%/day ($+0.06/hr per $10k notional), so size so one ATR of adverse excursion is survivable and treat VAH/VAL pokes as noise until a 1H close confirms.

_Levels are conditional triggers derived from observed candles; no price forecast is implied._
