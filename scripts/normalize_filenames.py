#!/usr/bin/env python3
"""Suggest normalized filenames for Markdown files.

This script only prints suggestions by default. Use --apply to rename files.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def slugify(name: str) -> str:
    stem = Path(name).stem
    suffix = Path(name).suffix.lower()
    text = unicodedata.normalize("NFKD", stem)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return (text or "untitled") + suffix


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    base = (ROOT / args.path).resolve()
    for path in sorted(base.rglob("*.md")):
        normalized = slugify(path.name)
        if normalized != path.name:
            target = path.with_name(normalized)
            print(f"{path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
            if args.apply:
                if target.exists():
                    print(f"  skip: target exists")
                else:
                    path.rename(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
