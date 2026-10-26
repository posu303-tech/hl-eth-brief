"""Shared fixtures: synthetic but structurally identical to Hyperliquid payloads."""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from parse import Candle, FundingPoint

HOUR_MS = 3_600_000
MINUTE_MS = 60_000
DAY_MS = 86_400_000


def make_candles(
    count: int,
    start_ms: int,
    interval_ms: int,
    first_price: float,
    *,
    drift: float = 0.0,
    amplitude: float = 0.0,
    volume: float = 100.0,
) -> list[Candle]:
    """A deterministic OHLC series with real high/low envelopes."""
    candles: list[Candle] = []
    price = first_price
    for index in range(count):
        open_ms = start_ms + index * interval_ms
        open_price = price
        close_price = open_price * (1 + drift) + amplitude * math.sin(index / 7.0)
        high = max(open_price, close_price) * 1.001
        low = min(open_price, close_price) * 0.999
        candles.append(
            Candle(
                t=open_ms,
                T=open_ms + interval_ms - 1,
                o=open_price,
                h=high,
                l=low,
                c=close_price,
                v=volume * (1 + (index % 5) / 5.0),
                n=50 + index % 7,
            )
        )
        price = close_price
    return candles


def make_ctx_payload(
    coin: str = "ETH",
    *,
    mark: float = 2000.0,
    oracle: float | None = None,
    prev_day: float = 1980.0,
    funding: float = 0.0000020,
    open_interest: float = 1_000_000.0,
) -> list:
    """BTC is placed first on purpose: ctxs is positional, not keyed by coin."""
    universe = [{"name": "BTC", "szDecimals": 5}, {"name": coin, "szDecimals": 4}]
    btc = {
        "funding": "0.0000125",
        "openInterest": "500000.0",
        "prevDayPx": "60000.0",
        "oraclePx": "60010.0",
        "markPx": "60000.0",
        "midPx": "60000.5",
        "dayNtlVlm": "900000000.0",
        "dayBaseVlm": "15000.0",
        "premium": "0.0001",
    }
    target = {
        "funding": str(funding),
        "openInterest": str(open_interest),
        "prevDayPx": str(prev_day),
        "oraclePx": str(oracle if oracle is not None else mark * 1.0005),
        "markPx": str(mark),
        "midPx": str(mark * 1.0002),
        "dayNtlVlm": "732131271.22",
        "dayBaseVlm": "314261.28",
        "premium": "-0.00016",
    }
    return [{"universe": universe}, [btc, target]]


def make_funding_points(
    coin: str = "ETH",
    *,
    count: int = 720,
    end_ms: int = 1_792_996_400_000,
    interval_ms: int = HOUR_MS,
    average: float = 0.0000020,
) -> list[FundingPoint]:
    start = end_ms - count * interval_ms
    return [
        FundingPoint(
            coin=coin,
            rate=average + 0.0000025 * math.sin(index / 11.0),
            time=start + index * interval_ms,
        )
        for index in range(count)
    ]


def make_funding_payload(coin: str = "ETH", **kwargs) -> list[dict]:
    return [
        {"coin": point.coin, "fundingRate": str(point.rate), "premium": "0.0001", "time": point.time}
        for point in make_funding_points(coin, **kwargs)
    ]


def make_predicted_payload(coin: str = "ETH", rate: float = 0.0000025) -> list:
    return [
        ["BTC", [["HlPerp", {"fundingRate": "0.0000125", "nextFundingTime": 0, "fundingIntervalHours": 1}]]],
        [coin, [
            ["HlPerp", {"fundingRate": str(rate), "nextFundingTime": 0, "fundingIntervalHours": 1}],
            ["BinPerp", {"fundingRate": str(rate * 10), "nextFundingTime": 0, "fundingIntervalHours": 8}],
        ]],
    ]
