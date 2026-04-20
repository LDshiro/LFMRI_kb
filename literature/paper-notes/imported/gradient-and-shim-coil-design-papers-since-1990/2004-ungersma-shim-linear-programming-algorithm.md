---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-S09
citation_key: Ungersma2004ShimLinearProgrammingAlgorithm
title: Shim design using a linear programming algorithm
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
source_list_record_id: S09
import_method: external-list
sources:
  - doi: 10.1002/mrm.20176
    pmid:
    url: https://doi.org/10.1002/mrm.20176
    access: unknown
---

# 論文ノート: Shim design using a linear programming algorithm

## Citation

- Authors: S. E. Ungersma et al.
- Year: 2004
- Title: Shim design using a linear programming algorithm
- Journal / venue: Magnetic Resonance in Medicine, 52(3), 619–627
- DOI: 10.1002/mrm.20176
- PMID:
- URL: https://doi.org/10.1002/mrm.20176
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1002/mrm.20176); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15334583/)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

任意面上の抵抗性シムコイルを線形計画法で設計する手法です。任意 ROI 上で任意次数のシム場を目標にでき、構成しやすい疎な電流パターンを得やすい点が特徴です。膝用磁石や頭部用磁石など、特殊形状の設計例を扱っています。

## Relevance to low-field MRI

| Item | Notes |
|---|---|
| Field strength |  |
| Target use case | custom |
| Subsystem | b0-field-control |
| Form factor | fixed |
| Study type | technical |
| Comparator |  |

## Source list import

| Item | Value |
|---|---|
| Source list | `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md` |
| Record ID | `S09` |
| Area | Shim |
| Publication time | 2004 Sep |
| Venue / pages | Magnetic Resonance in Medicine, 52(3), 619–627 |
| Imported links | [DOI resolver](https://doi.org/10.1002/mrm.20176); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15334583/) |
| Method family | linear-programming |
| Geometry | unspecified |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/b0-field-control.md` |

## Imported abstract (EN, paraphrased)

A linear-programming algorithm is introduced for designing resistive shim coils on arbitrary surfaces. The method can target shim fields of any order over an arbitrary ROI and tends to produce sparse, constructible current patterns. Examples include specialized knee and head-imaging magnet geometries.

## Imported abstract (JA)

任意面上の抵抗性シムコイルを線形計画法で設計する手法です。任意 ROI 上で任意次数のシム場を目標にでき、構成しやすい疎な電流パターンを得やすい点が特徴です。膝用磁石や頭部用磁石など、特殊形状の設計例を扱っています。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `S09`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `S09`. |
