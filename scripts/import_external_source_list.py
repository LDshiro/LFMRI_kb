#!/usr/bin/env python3
"""Import a curated external source-list Markdown file into KB artifacts.

The importer validates the source list, creates a normalized registry CSV,
generates draft paper notes, upserts imported sections in `references.bib`,
`reading-list.md`, and `purchase-list.md`, and writes helper fragments for
future reruns.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import csv
from pathlib import Path
import re
import shutil
import sys
import unicodedata
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_READING_LIST = ROOT / "literature" / "reading-list.md"
DEFAULT_PURCHASE_LIST = ROOT / "literature" / "purchase-list.md"
DEFAULT_REFERENCES = ROOT / "literature" / "references.bib"
DEFAULT_PAPER_NOTES = ROOT / "literature" / "paper-notes" / "imported"

P0_IDS = {"G30", "G34", "G35", "S17", "S18", "S19", "S26"}
P1_IDS = {"G05", "G19", "G22", "G23", "G25", "G27", "S23"}

STOPWORDS = {
    "a",
    "an",
    "and",
    "approach",
    "based",
    "by",
    "coil",
    "coils",
    "design",
    "for",
    "in",
    "method",
    "methods",
    "mri",
    "of",
    "on",
    "the",
    "to",
    "using",
    "with",
}

READING_LIST_HEADER = (
    "| Priority | Citation key | Topic | Why it matters | Access | Acquisition | Status | Note file | Source list |\n"
    "|---|---|---|---|---|---|---|---|---|"
)

PURCHASE_LIST_HEADER = (
    "| Priority | Citation key | Topic | Why needed | Current access | Alternative route | Purchase status | Owner | Note file | Notes |\n"
    "|---|---|---|---|---|---|---|---|---|---|"
)

REGISTRY_FIELDS = [
    "source_list_slug",
    "record_id",
    "area",
    "publication_time_text",
    "year",
    "title",
    "authors",
    "venue_pages",
    "doi",
    "link_primary",
    "link_secondary",
    "abstract_en_paraphrase",
    "abstract_ja_summary",
    "source_note",
    "citation_key",
    "note_file",
    "subsystem",
    "method_family",
    "geometry",
    "shielding_type",
    "scanner_context",
    "low_field_relevance",
    "priority",
    "access_status",
    "acquisition_status",
    "verification_status",
    "kb_targets",
]


@dataclass
class Record:
    record_id: str
    title: str
    area: str
    publication_time_text: str
    authors: str
    venue_pages: str
    doi: str
    links: list[tuple[str, str]]
    abstract_en_paraphrase: str
    abstract_ja_summary: str
    citation_key: str = ""
    note_file: str = ""
    subsystem: str = ""
    method_family: str = ""
    geometry: str = ""
    shielding_type: str = ""
    scanner_context: str = ""
    low_field_relevance: str = ""
    priority: str = ""
    access_status: str = "unknown"
    acquisition_status: str = "not-needed"
    verification_status: str = "source-located"
    kb_targets: str = ""
    source_note: str = ""
    year: str = ""

    @property
    def primary_url(self) -> str:
        if self.links:
            return self.links[0][1]
        if self.doi:
            return f"https://doi.org/{self.doi}"
        return ""

    @property
    def secondary_url(self) -> str:
        return self.links[1][1] if len(self.links) > 1 else ""


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value


def title_slug(title: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9]+", title.lower())
    picked = [token for token in tokens if token not in STOPWORDS]
    if not picked:
        picked = tokens
    return "-".join(picked[:5]) or "untitled"


def citation_suffix(title: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9]+", title)
    picked = [token for token in tokens if token.lower() not in STOPWORDS]
    if not picked:
        picked = tokens
    return "".join(token.capitalize() for token in picked[:5]) or "Untitled"


def first_author_surname(authors: str) -> str:
    first = authors.split(";")[0].strip()
    first = first.replace(" et al.", "").replace(" et al", "")
    first = unicodedata.normalize("NFKD", first).encode("ascii", "ignore").decode("ascii")
    tokens = [token for token in re.findall(r"[A-Za-z]+", first) if token.lower() not in {"et", "al"}]
    return tokens[-1] if tokens else "Unknown"


def ascii_text(value: str) -> str:
    return (
        value.replace("–", "--")
        .replace("—", "--")
        .replace("’", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("\u00a0", " ")
    )


def parse_link_pairs(raw: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", raw)


def parse_record_block(block: str) -> Record:
    heading, *body_lines = block.splitlines()
    match = re.match(r"^###\s+([A-Z]\d+)\.\s+(.+)$", heading.strip())
    if not match:
        raise ValueError(f"Invalid record heading: {heading}")
    record_id, title = match.group(1), match.group(2).strip()
    body = "\n".join(body_lines)

    def extract(label: str) -> str:
        pattern = rf"^- \*\*{re.escape(label)}:\*\*\s*(.+)$"
        found = re.search(pattern, body, re.MULTILINE)
        if not found:
            raise ValueError(f"{record_id}: missing field '{label}'")
        return found.group(1).strip()

    area = extract("Area")
    authors = extract("Authors")
    venue_pages = extract("Venue / pages")
    publication_time_text = extract("Publication time")
    doi = extract("DOI").strip("`")
    links_raw = extract("Links")
    abstract_en = extract("Abstract (EN, paraphrased)")
    abstract_ja = extract("アブストラクト（日本語要約）")

    return Record(
        record_id=record_id,
        title=title,
        area=area,
        publication_time_text=publication_time_text,
        authors=authors,
        venue_pages=venue_pages,
        doi=doi,
        links=parse_link_pairs(links_raw),
        abstract_en_paraphrase=abstract_en,
        abstract_ja_summary=abstract_ja,
    )


def parse_overview_rows(text: str) -> dict[str, tuple[str, str, str, str]]:
    start = text.find("## Overview table")
    if start == -1:
        raise ValueError("Missing '## Overview table'")
    rows: dict[str, tuple[str, str, str, str]] = {}
    for line in text[start:].splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("| ID ") or line.startswith("|---"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 5:
            continue
        record_id, area, publication_time, title, doi_cell = parts
        doi_match = re.search(r"`([^`]+)`", doi_cell)
        rows[record_id] = (area, publication_time, title, doi_match.group(1) if doi_match else doi_cell)
    return rows


def parse_source_list(path: Path) -> tuple[str, str, list[Record], str]:
    text = path.read_text(encoding="utf-8")
    checked_match = re.search(r"^Last checked:\s*(.+)$", text, re.MULTILINE)
    if not checked_match:
        raise ValueError("Missing 'Last checked' line")
    last_checked = checked_match.group(1).strip()
    overview = parse_overview_rows(text)
    blocks = re.split(r"(?m)^### ", text)
    records: list[Record] = []
    for block in blocks[1:]:
        block = "### " + block
        if block.startswith("### ") and re.match(r"^### [A-Z]\d+\.", block):
            records.append(parse_record_block(block))

    if len(overview) != len(records):
        raise ValueError(f"Overview rows ({len(overview)}) do not match record blocks ({len(records)})")

    seen_ids: set[str] = set()
    for record in records:
        if record.record_id in seen_ids:
            raise ValueError(f"Duplicate record ID: {record.record_id}")
        seen_ids.add(record.record_id)
        if record.record_id not in overview:
            raise ValueError(f"Record {record.record_id} missing from overview table")
        overview_area, overview_time, overview_title, overview_doi = overview[record.record_id]
        if overview_title != record.title:
            raise ValueError(f"{record.record_id}: overview title mismatch")
        if overview_area != record.area:
            raise ValueError(f"{record.record_id}: overview area mismatch")
        if overview_time != record.publication_time_text:
            raise ValueError(f"{record.record_id}: overview publication time mismatch")
        if overview_doi != record.doi:
            raise ValueError(f"{record.record_id}: overview DOI mismatch")

    notes_match = re.search(r"(?ms)^## Notes for use\s+(.*)$", text)
    notes_for_use = notes_match.group(1).strip() if notes_match else ""
    return path.stem, last_checked, records, notes_for_use


def parse_year(publication_time_text: str) -> str:
    match = re.search(r"(19|20)\d{2}", publication_time_text)
    return match.group(0) if match else ""


def detect_priority(record_id: str) -> str:
    if record_id in P0_IDS:
        return "P0"
    if record_id in P1_IDS:
        return "P1"
    return "P2"


def detect_subsystem(area: str) -> str:
    if "Gradient / Shim" in area:
        return "gradient-and-b0-field-control"
    if "Gradient" in area:
        return "gradient"
    return "b0-field-control"


def detect_method_family(record: Record) -> str:
    text = f"{record.title} {record.abstract_en_paraphrase}".lower()
    mapping = [
        ("review", "review"),
        ("convex optim", "convex-optimization"),
        ("shape derivative", "shape-derivative"),
        ("finite difference", "finite-difference"),
        ("boundary element", "boundary-element"),
        ("stream function", "stream-function"),
        ("target-field", "target-field"),
        ("genetic algorithm", "genetic-algorithm"),
        ("simulated annealing", "simulated-annealing"),
        ("conjugate gradient", "conjugate-gradient"),
        ("linear programming", "linear-programming"),
        ("power-minimization", "power-minimization"),
        ("minimum power", "minimum-power"),
        ("minimum energy", "minimum-energy"),
        ("spherical harmonic", "spherical-harmonic"),
        ("multicoil", "multicoil"),
        ("passive shim", "passive-shimming"),
        ("active magnetic screening", "active-shielding"),
        ("active shim", "active-shimming"),
        ("scaling relationship", "scaling-analysis"),
    ]
    for needle, label in mapping:
        if needle in text:
            return label
    return "other"


def detect_geometry(record: Record) -> str:
    text = f"{record.title} {record.abstract_en_paraphrase}".lower()
    mapping = [
        ("biplanar", "biplanar"),
        ("bi-planar", "biplanar"),
        ("planar", "planar"),
        ("cylindrical", "cylindrical"),
        ("toroidal", "toroidal"),
        ("non-developable", "non-developable-surface"),
        ("multilayer", "multilayer"),
        ("whole-body", "whole-body"),
        ("short, open bore", "short-open-bore"),
        ("open bore", "open-bore"),
        ("head-only", "head-only"),
        ("localized", "localized-array"),
        ("array", "array"),
        ("general geometry", "general-geometry"),
        ("arbitrary geometr", "general-geometry"),
    ]
    for needle, label in mapping:
        if needle in text:
            return label
    return "unspecified"


def detect_shielding_type(record: Record) -> str:
    text = f"{record.title} {record.abstract_en_paraphrase}".lower()
    if "active magnetic screening" in text or "actively shielded" in text or "active shielding" in text:
        return "active-shielding"
    if "shielded" in text or "screening" in text:
        return "shielded-design"
    if "eddy current" in text:
        return "eddy-current-mitigation"
    if "passive shim" in text or "passive shimming" in text:
        return "passive-shimming"
    return "none-or-unspecified"


def detect_scanner_context(record: Record) -> str:
    text = f"{record.title} {record.abstract_en_paraphrase}".lower()
    tags: list[str] = []
    mapping = [
        ("permanent magnet", "permanent-magnet"),
        ("ultra-low field", "ultra-low-field"),
        ("low field", "low-field"),
        ("open mri", "open-mri"),
        ("open bore", "open-bore"),
        ("nicu", "nicu"),
        ("head-only", "head-only"),
        ("small animal", "small-animal"),
        ("human brain", "human-brain"),
        ("7 t", "uhf"),
        ("ultra high field", "uhf"),
        ("nmr analyzer", "nmr-analyzer"),
    ]
    for needle, label in mapping:
        if needle in text and label not in tags:
            tags.append(label)
    return ";".join(tags) if tags else "general-mri"


def detect_low_field_relevance(record: Record) -> str:
    text = f"{record.title} {record.abstract_en_paraphrase}".lower()
    if record.record_id in P0_IDS:
        return "direct"
    if any(needle in text for needle in ["permanent magnet", "low field", "ultra-low", "nicu", "open mri", "open bore"]):
        return "direct"
    if record.record_id in P1_IDS:
        return "bridge"
    return "background"


def build_kb_targets(record: Record) -> str:
    targets = ["kb/hardware/design-methods.md"]
    subsystem = detect_subsystem(record.area)
    if subsystem in {"gradient", "gradient-and-b0-field-control"}:
        targets.append("kb/hardware/gradients.md")
    if subsystem in {"b0-field-control", "gradient-and-b0-field-control"}:
        targets.append("kb/hardware/b0-field-control.md")
    text = f"{record.title} {record.abstract_en_paraphrase}".lower()
    if any(needle in text for needle in ["shield", "screening", "eddy current"]):
        targets.append("kb/hardware/shielding.md")
    return ";".join(dict.fromkeys(targets))


def read_access_audit(path: Path | None) -> dict[str, dict[str, str]]:
    if path is None or not path.exists():
        return {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {row["record_id"]: row for row in csv.DictReader(handle)}


def apply_derived_fields(records: list[Record], slug: str, access_audit: dict[str, dict[str, str]]) -> None:
    used_keys: set[str] = set()
    for record in records:
        record.year = parse_year(record.publication_time_text)
        record.priority = detect_priority(record.record_id)
        record.subsystem = detect_subsystem(record.area)
        record.method_family = detect_method_family(record)
        record.geometry = detect_geometry(record)
        record.shielding_type = detect_shielding_type(record)
        record.scanner_context = detect_scanner_context(record)
        record.low_field_relevance = detect_low_field_relevance(record)
        record.kb_targets = build_kb_targets(record)

        base_key = f"{first_author_surname(record.authors)}{record.year}{citation_suffix(record.title)}"
        citation_key = base_key
        counter = 2
        while citation_key in used_keys:
            citation_key = f"{base_key}{counter}"
            counter += 1
        used_keys.add(citation_key)
        record.citation_key = citation_key

        note_rel = (
            Path("literature")
            / "paper-notes"
            / "imported"
            / slug
            / f"{record.year}-{slugify(first_author_surname(record.authors))}-{title_slug(record.title)}.md"
        )
        record.note_file = note_rel.as_posix()

        audit = access_audit.get(record.record_id, {})
        record.access_status = audit.get("access_status", "unknown")
        record.verification_status = audit.get("verification_status", "source-located")

        if record.access_status == "open-access":
            record.acquisition_status = "not-needed"
        elif record.access_status in {"purchase-required", "abstract-only"}:
            record.acquisition_status = "candidate"
        elif record.access_status == "institutional-access":
            record.acquisition_status = "not-needed"
        elif record.priority in {"P0", "P1"}:
            record.acquisition_status = "candidate"
        else:
            record.acquisition_status = "not-needed"


def replace_block(text: str, name: str, replacement: str) -> str:
    begin = f"<!-- BEGIN {name} -->"
    end = f"<!-- END {name} -->"
    pattern = re.compile(rf"{re.escape(begin)}.*?{re.escape(end)}", re.DOTALL)
    block = f"{begin}\n{replacement.rstrip()}\n{end}"
    if pattern.search(text):
        return pattern.sub(block, text)
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n" + block + "\n"


def ensure_import_markers(path: Path, section_name: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = f"<!-- BEGIN {section_name} -->"
    if marker in text:
        return
    if path.name == "reading-list.md":
        anchor = "## Search refresh log"
        insertion = (
            "## Imported source lists\n\n"
            "<!-- BEGIN AUTO-IMPORTED-SOURCE-LISTS -->\n"
            "_No imported source-list entries yet._\n"
            "<!-- END AUTO-IMPORTED-SOURCE-LISTS -->\n\n"
        )
    elif path.name == "purchase-list.md":
        anchor = "## Deferred or not purchasing"
        insertion = (
            "## Imported source-list purchase candidates\n\n"
            "<!-- BEGIN AUTO-IMPORTED-PURCHASE-CANDIDATES -->\n"
            "_No imported purchase candidates yet._\n"
            "<!-- END AUTO-IMPORTED-PURCHASE-CANDIDATES -->\n\n"
        )
    else:
        return
    if anchor not in text:
        raise ValueError(f"Cannot find anchor '{anchor}' in {path}")
    path.write_text(text.replace(anchor, insertion + anchor), encoding="utf-8")


def write_registry_csv(path: Path, records: Iterable[Record]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REGISTRY_FIELDS)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "source_list_slug": path.stem.replace("-registry", ""),
                    "record_id": record.record_id,
                    "area": record.area,
                    "publication_time_text": record.publication_time_text,
                    "year": record.year,
                    "title": record.title,
                    "authors": record.authors,
                    "venue_pages": record.venue_pages,
                    "doi": record.doi,
                    "link_primary": record.primary_url,
                    "link_secondary": record.secondary_url,
                    "abstract_en_paraphrase": record.abstract_en_paraphrase,
                    "abstract_ja_summary": record.abstract_ja_summary,
                    "source_note": record.source_note,
                    "citation_key": record.citation_key,
                    "note_file": record.note_file,
                    "subsystem": record.subsystem,
                    "method_family": record.method_family,
                    "geometry": record.geometry,
                    "shielding_type": record.shielding_type,
                    "scanner_context": record.scanner_context,
                    "low_field_relevance": record.low_field_relevance,
                    "priority": record.priority,
                    "access_status": record.access_status,
                    "acquisition_status": record.acquisition_status,
                    "verification_status": record.verification_status,
                    "kb_targets": record.kb_targets,
                }
            )


def summarize_context(record: Record) -> tuple[str, str, str]:
    study_type = "review" if "review" in record.method_family or "review" in record.title.lower() else "technical"
    target_use = record.scanner_context.replace(";", " / ") if record.scanner_context != "general-mri" else "custom"
    if target_use == "custom":
        target_use = "custom"
    if "permanent-magnet" in record.scanner_context or "low-field" in record.scanner_context or "ultra-low-field" in record.scanner_context:
        form_factor = "portable" if "nicu" in record.scanner_context else "fixed"
    elif "open-bore" in record.scanner_context or "open-mri" in record.scanner_context:
        form_factor = "fixed"
    elif "head-only" in record.scanner_context:
        form_factor = "fixed"
    else:
        form_factor = "fixed"
    return study_type, target_use, form_factor


def first_sentence(text: str) -> str:
    sentence = re.split(r"(?<=[.!?])\s+", text.strip())[0].strip()
    return sentence or text.strip()


def note_markdown(record: Record, slug: str, checked_date: str) -> str:
    study_type, target_use, form_factor = summarize_context(record)
    source_links = "; ".join(f"[{label}]({url})" for label, url in record.links)
    kb_destinations = record.kb_targets.split(";")
    summary = first_sentence(record.abstract_ja_summary) if record.abstract_ja_summary else first_sentence(record.abstract_en_paraphrase)
    note = f"""---
id: LF-MRI-PAPER-{slugify(slug).upper()}-{record.record_id}
citation_key: {record.citation_key}
title: {record.title}
status: draft
owner: unassigned
created: {checked_date}
last_reviewed:
review_cycle: 12 months
tags:
  - literature
  - low-field-mri
  - hardware
  - design-methods
study_type: {study_type}
field_strength:
clinical_domain: hardware
evidence_level: technical-validation
access_status: {record.access_status}
acquisition_status: {record.acquisition_status}
source_list_slug: {slug}
source_list_record_id: {record.record_id}
import_method: external-list
sources:
  - doi: {record.doi}
    pmid:
    url: {record.primary_url}
    access: {record.access_status}
---

# 論文ノート: {record.title}

## Citation

- Authors: {record.authors}
- Year: {record.year}
- Title: {record.title}
- Journal / venue: {record.venue_pages}
- DOI: {record.doi}
- PMID:
- URL: {record.primary_url}
- Accessed: {checked_date}

## Access and rights

- Access status: {record.access_status}
- Acquisition status: {record.acquisition_status}
- Full text checked: no
- Access route: {source_links or record.primary_url}
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

{summary}

## Relevance to low-field MRI

| Item | Notes |
|---|---|
| Field strength |  |
| Target use case | {target_use} |
| Subsystem | {record.subsystem} |
| Form factor | {form_factor} |
| Study type | {study_type} |
| Comparator |  |

## Source list import

| Item | Value |
|---|---|
| Source list | `literature/source-lists/{slug}.md` |
| Record ID | `{record.record_id}` |
| Area | {record.area} |
| Publication time | {record.publication_time_text} |
| Venue / pages | {record.venue_pages} |
| Imported links | {source_links or "n/a"} |
| Method family | {record.method_family} |
| Geometry | {record.geometry} |
| Shielding type | {record.shielding_type} |
| Scanner context | {record.scanner_context} |
| KB targets | `{record.kb_targets}` |

## Imported abstract (EN, paraphrased)

{record.abstract_en_paraphrase}

## Imported abstract (JA)

{record.abstract_ja_summary}

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `{record.record_id}`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `{kb_destinations[0]}` | draft |

## Methods

- Design workflow:
- Simulation tools:
- Optimization method:
- Prototype built:
- Validation mode:
- Comparator:

## Results to extract

| Metric | Value | Unit | Condition | Source location | Notes |
|---|---:|---|---|---|---|
|  |  |  |  |  |  |

## Figures / tables worth revisiting

| Figure / table | Why important | Extracted? |
|---|---|---|
|  |  | no |

## Reproducibility notes

- Data availability:
- Code availability:
- CAD / coil geometry availability:
- Parameter completeness:
- Missing details:

## Limitations

- This note is imported from a curated source list and has not yet been verified against the full text.

## Action items

- [ ] Verify the full text and confirm venue metadata.
- [ ] Update `literature/references.bib` if a more complete record is found.
- [ ] Update `literature/purchase-list.md` if acquisition is required.
- [ ] Extract validated details into KB pages and evidence tables.
- [ ] Confirm whether additional related low-field papers should be linked.

## Reviewer notes

| Date | Reviewer | Note |
|---|---|---|
| {checked_date} |  | Imported from external source list `{slug}` record `{record.record_id}`. |
"""
    return note


def write_paper_notes(records: list[Record], slug: str, checked_date: str, notes_root: Path) -> None:
    target_dir = notes_root / slug
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    for record in records:
        note_path = ROOT / record.note_file
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(note_markdown(record, slug, checked_date), encoding="utf-8")


def reading_list_fragment(records: list[Record], slug: str) -> str:
    lines = [f"### Imported Source List: `{slug}`", "", READING_LIST_HEADER]
    why_map = {
        "P0": "low-field / permanent-magnet MRI に直接関係する重点論文",
        "P1": "低磁場設計へ橋渡しになる一般手法または総説",
        "P2": "背景整理と方法論の長期参照用",
    }
    for record in sorted(records, key=lambda item: (item.priority, item.year, item.record_id)):
        lines.append(
            f"| {record.priority} | `{record.citation_key}` | {record.title} | {why_map[record.priority]} | "
            f"{record.access_status} | {record.acquisition_status} | todo | `{record.note_file}` | `{slug}:{record.record_id}` |"
        )
    return "\n".join(lines)


def purchase_fragment(records: list[Record], slug: str) -> str:
    lines = [f"### Imported Source List: `{slug}`", "", PURCHASE_LIST_HEADER]
    candidates = [
        record for record in records
        if record.priority in {"P0", "P1"} and record.acquisition_status == "candidate"
    ]
    if not candidates:
        lines.append("|  |  |  |  |  |  |  |  |  |  |")
        return "\n".join(lines)
    for record in sorted(candidates, key=lambda item: (item.priority, item.record_id)):
        reason = (
            "P0 priority and full-text access is required for KB verification."
            if record.priority == "P0"
            else "P1 bridge paper worth acquiring after P0 verification."
        )
        lines.append(
            f"| {record.priority} | `{record.citation_key}` | {record.title} | {reason} | {record.access_status} |  | "
            f"{record.acquisition_status} | unassigned | `{record.note_file}` | Imported from `{slug}:{record.record_id}` |"
        )
    return "\n".join(lines)


def bib_entry(record: Record, slug: str, checked_date: str) -> str:
    journal = record.venue_pages.split(",")[0].strip()
    author = record.authors.replace("; ", " and ").replace(" et al.", " and others")
    note = ascii_text(
        f"Imported from source list {slug} ({record.record_id}). "
        f"Publication time text: {record.publication_time_text}. "
        f"Venue / pages: {record.venue_pages}. Accessed {checked_date}."
    )
    lines = [
        f"@article{{{record.citation_key},",
        f"  title        = {{{ascii_text(record.title)}}},",
        f"  author       = {{{ascii_text(author)}}},",
        f"  journal      = {{{ascii_text(journal)}}},",
        f"  year         = {{{record.year}}},",
        f"  doi          = {{{record.doi}}},",
        f"  url          = {{{record.primary_url}}},",
        f"  note         = {{{note}}},",
        "}",
    ]
    return "\n".join(lines)


def update_references(path: Path, records: list[Record], slug: str, checked_date: str) -> None:
    text = path.read_text(encoding="utf-8")
    section_name = f"AUTO-IMPORTED-BIB::{slug}"
    entries = "\n\n".join(bib_entry(record, slug, checked_date) for record in records)
    updated = replace_block(text, section_name, f"% Imported from source list {slug}\n\n{entries}")
    path.write_text(updated + ("\n" if not updated.endswith("\n") else ""), encoding="utf-8")


def update_markdown_with_fragment(path: Path, section_name: str, fragment: str) -> None:
    text = path.read_text(encoding="utf-8")
    updated = replace_block(text, section_name, fragment)
    path.write_text(updated, encoding="utf-8")


def write_fragment(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to external source-list Markdown file")
    parser.add_argument("--access-audit", help="Optional CSV with access audit overrides")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = (ROOT / input_path).resolve()
    access_audit_path = Path(args.access_audit).resolve() if args.access_audit else None

    slug, checked_date, records, notes_for_use = parse_source_list(input_path)
    access_audit = read_access_audit(access_audit_path)
    apply_derived_fields(records, slug, access_audit)

    registry_path = input_path.with_name(f"{slug}-registry.csv")
    reading_fragment_path = input_path.with_name(f"{slug}-reading-list-fragment.md")
    purchase_fragment_path = input_path.with_name(f"{slug}-purchase-fragment.md")

    notes_root = DEFAULT_PAPER_NOTES
    ensure_import_markers(DEFAULT_READING_LIST, "AUTO-IMPORTED-SOURCE-LISTS")
    ensure_import_markers(DEFAULT_PURCHASE_LIST, "AUTO-IMPORTED-PURCHASE-CANDIDATES")

    write_registry_csv(registry_path, records)
    write_paper_notes(records, slug, checked_date, notes_root)

    reading_fragment = reading_list_fragment(records, slug)
    purchase_fragment_content = purchase_fragment(records, slug)
    write_fragment(reading_fragment_path, reading_fragment)
    write_fragment(purchase_fragment_path, purchase_fragment_content)

    update_markdown_with_fragment(DEFAULT_READING_LIST, "AUTO-IMPORTED-SOURCE-LISTS", reading_fragment)
    update_markdown_with_fragment(DEFAULT_PURCHASE_LIST, "AUTO-IMPORTED-PURCHASE-CANDIDATES", purchase_fragment_content)
    update_references(DEFAULT_REFERENCES, records, slug, checked_date)

    print(f"Imported {len(records)} records from {input_path.relative_to(ROOT)}")
    print(f"- Registry: {registry_path.relative_to(ROOT)}")
    print(f"- Paper notes dir: {(notes_root / slug).relative_to(ROOT)}")
    print(f"- Reading-list fragment: {reading_fragment_path.relative_to(ROOT)}")
    print(f"- Purchase fragment: {purchase_fragment_path.relative_to(ROOT)}")
    if notes_for_use:
        print("- Notes for use detected and preserved in source list file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
