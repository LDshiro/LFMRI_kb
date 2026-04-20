#!/usr/bin/env python3
"""Very small BibTeX sanity checker without external dependencies."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ENTRY_START = re.compile(r"^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)?", re.MULTILINE)
RECOMMENDED_FIELDS = ["title", "author", "year"]


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.lstrip().startswith("%"):
            continue
        lines.append(line)
    return "\n".join(lines)


def find_entries(text: str):
    for match in ENTRY_START.finditer(text):
        entry_type = match.group(1).lower()
        key = match.group(2) or ""
        start = match.start()
        next_match = ENTRY_START.search(text, match.end())
        end = next_match.start() if next_match else len(text)
        body = text[start:end]
        yield entry_type, key, body


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("literature/references.bib")
    if not path.exists():
        print(f"BibTeX file not found: {path}")
        return 1

    text = strip_comments(path.read_text(encoding="utf-8"))
    errors = []
    warnings = []
    count = 0

    for entry_type, key, body in find_entries(text):
        if entry_type == "comment":
            continue
        count += 1
        if not key:
            errors.append("Entry without citation key")
        if body.count("{") != body.count("}"):
            errors.append(f"{key}: unbalanced braces")
        lower_body = body.lower()
        for field in RECOMMENDED_FIELDS:
            if f"{field}" not in lower_body:
                warnings.append(f"{key}: recommended field missing: {field}")
        if "doi" not in lower_body and "pmid" not in lower_body and "url" not in lower_body:
            warnings.append(f"{key}: no DOI, PMID, or URL field")

    if errors:
        print("BibTeX validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"BibTeX validation passed. Entries checked: {count}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
