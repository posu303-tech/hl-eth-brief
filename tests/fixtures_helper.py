"""Builds a LevelBook from the recorded payloads. Shared by the replay tests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import eth_brief

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def available() -> bool:
    return (FIXTURES / "meta.json").exists()


def load_payloads() -> tuple[dict, dict]:
    meta = json.loads((FIXTURES / "meta.json").read_text(encoding="utf-8"))
    payloads = {
        key: json.loads((FIXTURES / f"{key}.json").read_text(encoding="utf-8"))
        for key in eth_brief.PAYLOAD_KEYS
    }
    return meta, payloads


def build_book_from_fixtures():
    meta, payloads = load_payloads()
    args = argparse.Namespace(
        session_start_hour=0, va_days=10, va_percent=0.70, bucket=None, min_rr=1.5
    )
    return eth_brief.build_book(payloads, meta["symbol"], meta["as_of"], args)
