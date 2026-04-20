#!/usr/bin/env python3
"""Check required YAML-like frontmatter in KB and literature note Markdown files.

This intentionally avoids external dependencies. It performs a lightweight check,
not full YAML validation.
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [ROOT / "kb", ROOT / "literature" / "paper-notes", ROOT / "data" / "dataset-cards", ROOT / "experiments"]
REQUIRED = ["id", "title", "status", "created", "tags"]
STATUS_ALLOWED = {"draft", "reviewed", "stable", "deprecated"}


def extract_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in block:
        if not line.strip() or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def should_check(path: Path) -> bool:
    if path.name.upper().startswith("README"):
        return False
    if path.name.lower().endswith("template.md"):
        return False
    if "/_templates/" in path.as_posix():
        return False
    return True


def main() -> int:
    errors: list[str] = []
    files: list[Path] = []
    for directory in TARGET_DIRS:
        if directory.exists():
            files.extend(directory.rglob("*.md"))

    for path in sorted(files):
        if not should_check(path):
            continue
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing frontmatter")
            continue
        for key in REQUIRED:
            if key not in fm:
                errors.append(f"{rel}: missing required key '{key}'")
        status = fm.get("status", "")
        if status and status not in STATUS_ALLOWED:
            errors.append(f"{rel}: invalid status '{status}'")

    if errors:
        print("Frontmatter check failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Frontmatter check passed for {len(files)} Markdown files scanned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
