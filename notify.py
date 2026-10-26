"""Telegram delivery. Optional by design: no token means a silent no-op.

Never raises on a delivery failure - a missing alert must not fail the workflow
that produced the brief. The return value is a small dict so the caller can log
what happened.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

API_BASE = "https://api.telegram.org"


def configured() -> bool:
    return bool(os.environ.get("TELEGRAM_BOT_TOKEN")) and bool(os.environ.get("TELEGRAM_CHAT_ID"))


def send(
    text: str,
    *,
    token: str | None = None,
    chat_id: str | None = None,
    timeout: float = 10.0,
    api_base: str = API_BASE,
) -> dict:
    token = token or os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = chat_id or os.environ.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        return {"ok": False, "skipped": "TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID not set"}

    body = urllib.parse.urlencode(
        {"chat_id": chat_id, "text": text, "disable_web_page_preview": "true"}
    ).encode("utf-8")
    request = urllib.request.Request(f"{api_base}/bot{token}/sendMessage", data=body, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8", "replace"))
        return {"ok": bool(payload.get("ok")), "detail": payload.get("description", "")}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:200]
        return {"ok": False, "detail": f"HTTP {exc.code}: {detail}"}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"ok": False, "detail": str(exc)}


def split_message(text: str, limit: int = 4000) -> list[str]:
    """Telegram caps a message at 4096 characters; split on blank lines."""
    if len(text) <= limit:
        return [text]
    chunks: list[str] = []
    current = ""
    for block in text.split("\n\n"):
        candidate = f"{current}\n\n{block}" if current else block
        if len(candidate) > limit and current:
            chunks.append(current)
            current = block
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks
