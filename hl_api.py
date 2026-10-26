"""Keyless client for Hyperliquid's public /info endpoint.

Two details this module exists to get right:

* Candles are requested as ``{"type": "candleSnapshot", "req": {...}}``. The
  flat ``{"type": "candles", ...}`` body is rejected by the API with HTTP 422
  ("Failed to deserialize the JSON body into the target type").
* Every payload is retained in a :class:`RawVault`, so when a field goes
  missing the caller can print exactly what the server sent back.

No API key, no signing, no account state is touched.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any, Mapping

INFO_URL = "https://api.hyperliquid.xyz/info"
DEFAULT_TIMEOUT = 20.0
DEFAULT_RETRIES = 3
USER_AGENT = "hl-eth-brief/1.0"
RETRY_STATUS = {408, 425, 429, 500, 502, 503, 504, 520, 522, 524}


class HyperliquidError(RuntimeError):
    """Transport-level failure: network, HTTP status, or a non-JSON body."""


class RawVault:
    """Keeps request/response pairs so failures can dump the real payload."""

    def __init__(self) -> None:
        self.entries: dict[str, dict[str, Any]] = {}

    def put(self, key: str, request: Any, response: Any) -> None:
        self.entries[key] = {"request": request, "response": response}

    def get(self, key: str) -> dict[str, Any] | None:
        return self.entries.get(key)

    def payload(self, key: str) -> Any:
        entry = self.entries.get(key)
        return None if entry is None else entry["response"]

    def dump(self, key: str, indent: int = 2) -> str:
        entry = self.entries.get(key)
        if entry is None:
            return f"<no payload captured for {key!r}>"
        return json.dumps(entry, indent=indent, default=str, sort_keys=False)

    def keys(self) -> list[str]:
        return list(self.entries)


def post(
    body: Mapping[str, Any],
    *,
    timeout: float = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
) -> Any:
    """POST a body to /info and return the decoded JSON.

    Retries idempotent-safe failures (429/5xx/network) with exponential backoff.
    A 4xx that is not a rate limit is raised immediately: retrying a malformed
    request just burns time.
    """
    data = json.dumps(dict(body)).encode("utf-8")
    kind = body.get("type")
    last_error = "unknown failure"

    for attempt in range(retries):
        request = urllib.request.Request(
            INFO_URL,
            data=data,
            method="POST",
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                text = response.read().decode("utf-8", "replace")
            return json.loads(text)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400].strip()
            last_error = f"HTTP {exc.code} for type={kind!r}: {detail}"
            if exc.code not in RETRY_STATUS or attempt == retries - 1:
                raise HyperliquidError(last_error) from None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = f"network error for type={kind!r}: {exc}"
        except json.JSONDecodeError as exc:
            last_error = f"non-JSON body for type={kind!r}: {exc}"

        time.sleep(2**attempt)

    raise HyperliquidError(last_error)


# --------------------------------------------------------------------- helpers
def fetch_candles(
    coin: str,
    interval: str,
    start_ms: int,
    end_ms: int | None = None,
    *,
    vault: RawVault | None = None,
    key: str | None = None,
) -> Any:
    """Candle snapshot. ``interval`` is one of 1m/5m/15m/1h/4h/1d/... max 5000 bars."""
    req: dict[str, Any] = {"coin": coin, "interval": interval, "startTime": int(start_ms)}
    if end_ms is not None:
        req["endTime"] = int(end_ms)
    body = {"type": "candleSnapshot", "req": req}
    payload = post(body)
    if vault is not None:
        vault.put(key or f"candles_{interval}", body, payload)
    return payload


def fetch_asset_ctxs(*, vault: RawVault | None = None, key: str = "meta_and_asset_ctxs") -> Any:
    """[meta, ctxs] - ctxs is positional and aligned with meta['universe']."""
    body = {"type": "metaAndAssetCtxs"}
    payload = post(body)
    if vault is not None:
        vault.put(key, body, payload)
    return payload


def fetch_funding_history(
    coin: str, start_ms: int, *, vault: RawVault | None = None, key: str = "funding_history"
) -> Any:
    body = {"type": "fundingHistory", "coin": coin, "startTime": int(start_ms)}
    payload = post(body)
    if vault is not None:
        vault.put(key, body, payload)
    return payload


def fetch_predicted_fundings(
    *, vault: RawVault | None = None, key: str = "predicted_fundings"
) -> Any:
    body = {"type": "predictedFundings"}
    payload = post(body)
    if vault is not None:
        vault.put(key, body, payload)
    return payload
