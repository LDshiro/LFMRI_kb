#!/usr/bin/env python3
"""Create a sanitized release bundle zip.

The bundle excludes raw exports, PDFs, imaging files, virtual environments, and git metadata.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXCLUDE_PARTS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "raw-data-export",
    "release-bundles",
}
EXCLUDE_SUFFIXES = {
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
    ".dcm",
    ".nii",
    ".nrrd",
    ".mha",
    ".mhd",
}


def should_include(path: Path) -> bool:
    rel_parts = set(path.relative_to(ROOT).parts)
    if rel_parts & DEFAULT_EXCLUDE_PARTS:
        return False
    name = path.name
    if name.startswith(".") and name not in {".gitignore", ".gitattributes"}:
        return False
    suffixes = path.suffixes
    if any(s in EXCLUDE_SUFFIXES for s in suffixes):
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="release-bundles", help="Output directory")
    parser.add_argument("--name", default=None, help="Bundle name without .zip")
    args = parser.parse_args()

    out_dir = ROOT / args.output
    out_dir.mkdir(parents=True, exist_ok=True)
    name = args.name or f"lowfield-mri-kb-{date.today().isoformat()}"
    out_path = out_dir / f"{name}.zip"

    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(ROOT.rglob("*")):
            if path.is_file() and should_include(path):
                zf.write(path, path.relative_to(ROOT.parent))

    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
