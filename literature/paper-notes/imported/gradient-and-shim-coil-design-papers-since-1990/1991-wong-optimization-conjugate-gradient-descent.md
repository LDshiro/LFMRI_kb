---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-G02
citation_key: Wong1991OptimizationConjugateGradientDescent
title: Coil optimization for MRI by conjugate gradient descent
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
source_list_record_id: G02
import_method: external-list
sources:
  - doi: 10.1002/mrm.1910210107
    pmid:
    url: https://doi.org/10.1002/mrm.1910210107
    access: unknown
---

# 論文ノート: Coil optimization for MRI by conjugate gradient descent

## Citation

- Authors: E. C. Wong; A. Jesmanowicz; J. S. Hyde
- Year: 1991
- Title: Coil optimization for MRI by conjugate gradient descent
- Journal / venue: Magnetic Resonance in Medicine, 21(1), 39–48
- DOI: 10.1002/mrm.1910210107
- PMID:
- URL: https://doi.org/10.1002/mrm.1910210107
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1002/mrm.1910210107); [PubMed](https://pubmed.ncbi.nlm.nih.gov/1943670/)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

離散電流要素と Biot–Savart 則に基づき、MRI コイル設計を共役勾配法で最適化する枠組みを示した論文です。関心領域内の誤差関数を定義し、均一性、効率、インダクタンス、消費電力などを目的関数・制約として扱えます。単純な円筒面や平面に限定されない点が重要です。

## Relevance to low-field MRI

| Item | Notes |
|---|---|
| Field strength |  |
| Target use case | custom |
| Subsystem | gradient |
| Form factor | fixed |
| Study type | technical |
| Comparator |  |

## Source list import

| Item | Value |
|---|---|
| Source list | `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md` |
| Record ID | `G02` |
| Area | Gradient |
| Publication time | 1991 Sep |
| Venue / pages | Magnetic Resonance in Medicine, 21(1), 39–48 |
| Imported links | [DOI resolver](https://doi.org/10.1002/mrm.1910210107); [PubMed](https://pubmed.ncbi.nlm.nih.gov/1943670/) |
| Method family | conjugate-gradient |
| Geometry | planar |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/gradients.md` |

## Imported abstract (EN, paraphrased)

The authors introduce a flexible iterative optimization framework for MRI coil design using discrete current elements and Biot–Savart field calculations. A user-defined error function over the region of interest is minimized by conjugate-gradient descent. The method can include field uniformity, efficiency, inductance, and power-related objectives without being restricted to simple cylindrical or planar geometries.

## Imported abstract (JA)

離散電流要素と Biot–Savart 則に基づき、MRI コイル設計を共役勾配法で最適化する枠組みを示した論文です。関心領域内の誤差関数を定義し、均一性、効率、インダクタンス、消費電力などを目的関数・制約として扱えます。単純な円筒面や平面に限定されない点が重要です。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `G02`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `G02`. |
