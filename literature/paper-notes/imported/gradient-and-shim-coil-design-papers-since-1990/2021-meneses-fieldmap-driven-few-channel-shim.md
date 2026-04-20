---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-S22
citation_key: Meneses2021FieldmapDrivenFewChannelShim
title: A fieldmap-driven few-channel shim coil design for MRI of the human brain
status: draft
owner: unassigned
created: 2026-04-20
last_reviewed:
review_cycle: 12 months
tags:
  - literature
  - low-field-mri
  - hardware
  - design-methods
study_type: technical
field_strength:
clinical_domain: hardware
evidence_level: technical-validation
access_status: unknown
acquisition_status: not-needed
source_list_slug: gradient-and-shim-coil-design-papers-since-1990
source_list_record_id: S22
import_method: external-list
sources:
  - doi: 10.1088/1361-6560/abc810
    pmid:
    url: https://doi.org/10.1088/1361-6560/abc810
    access: unknown
---

# 論文ノート: A fieldmap-driven few-channel shim coil design for MRI of the human brain

## Citation

- Authors: L. Pinho Meneses; A. Amadon
- Year: 2021
- Title: A fieldmap-driven few-channel shim coil design for MRI of the human brain
- Journal / venue: Physics in Medicine & Biology, 66(1), 015001
- DOI: 10.1088/1361-6560/abc810
- PMID:
- URL: https://doi.org/10.1088/1361-6560/abc810
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1088/1361-6560/abc810); [IOPscience](https://iopscience.iop.org/article/10.1088/1361-6560/abc810)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

ヒト脳の実測 B0 field map から、少数チャネルのシムコイルを設計します。低電力制約下で被験者ごとの stream function を求め、主成分分析で支配的な補正モードを抽出します。前頭前野など難しい領域では、多数の従来球面調和チャネルを上回る可能性があります。

## Relevance to low-field MRI

| Item | Notes |
|---|---|
| Field strength |  |
| Target use case | human-brain |
| Subsystem | b0-field-control |
| Form factor | fixed |
| Study type | technical |
| Comparator |  |

## Source list import

| Item | Value |
|---|---|
| Source list | `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md` |
| Record ID | `S22` |
| Area | Shim |
| Publication time | 2021 Jan |
| Venue / pages | Physics in Medicine & Biology, 66(1), 015001 |
| Imported links | [DOI resolver](https://doi.org/10.1088/1361-6560/abc810); [IOPscience](https://iopscience.iop.org/article/10.1088/1361-6560/abc810) |
| Method family | stream-function |
| Geometry | unspecified |
| Shielding type | none-or-unspecified |
| Scanner context | human-brain |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/b0-field-control.md` |

## Imported abstract (EN, paraphrased)

This paper designs a small number of shim coils from measured human-brain B0 field maps. Subject-specific stream functions are computed under low-power constraints, and principal component analysis extracts dominant correction modes. The resulting few-channel coils can outperform many conventional spherical-harmonic channels in difficult regions such as the prefrontal cortex.

## Imported abstract (JA)

ヒト脳の実測 B0 field map から、少数チャネルのシムコイルを設計します。低電力制約下で被験者ごとの stream function を求め、主成分分析で支配的な補正モードを抽出します。前頭前野など難しい領域では、多数の従来球面調和チャネルを上回る可能性があります。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `S22`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `S22`. |
