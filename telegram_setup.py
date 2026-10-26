#!/usr/bin/env python3
"""Finds the chat id you need for TELEGRAM_CHAT_ID.

1. Create a bot with @BotFather, copy the token.
2. Send the bot any message (a chat id only appears after the first message).
3. TELEGRAM_BOT_TOKEN=... python telegram_setup.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


def get(url: str, timeout: float = 10.0) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        return {"ok": False, "description": f"HTTP {exc.code}"}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"ok": False, "description": str(exc)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Find your Telegram chat id, optionally send a test.")
    parser.add_argument("--send", action="store_true", help="send a test message to each chat found")
    args = parser.parse_args(argv)

    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        print("set TELEGRAM_BOT_TOKEN first", file=sys.stderr)
        return 1

    me = get(f"https://api.telegram.org/bot{token}/getMe")
    if not me.get("ok"):
        print(f"token rejected: {me.get('description')}", file=sys.stderr)
        return 2
    print(f"bot: @{me['result'].get('username')}")

    updates = get(f"https://api.telegram.org/bot{token}/getUpdates")
    if not updates.get("ok"):
        print(f"getUpdates failed: {updates.get('description')}", file=sys.stderr)
        return 3

    chats: dict[int, str] = {}
    for update in updates.get("result", []):
        message = update.get("message") or update.get("channel_post") or {}
        chat = message.get("chat") or {}
        if chat.get("id"):
            chats[chat["id"]] = chat.get("username") or chat.get("title") or chat.get("first_name", "")

    if not chats:
        print("no chats found - send the bot a message, then run this again")
        print("(if a webhook is set, getUpdates stays empty: gh api -X DELETE .../deleteWebhook)")
        return 0

    print("")
    for chat_id, name in chats.items():
        print(f"TELEGRAM_CHAT_ID={chat_id}   ({name})")

    if args.send:
        import notify

        print("")
        for chat_id in chats:
            result = notify.send(
                "HL-ETH-Brief: test alert. Telegram is working.",
                token=token,
                chat_id=str(chat_id),
            )
            detail = result.get("detail") or result.get("skipped") or "ok"
            print(f"test message to {chat_id}: {'sent' if result['ok'] else detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
