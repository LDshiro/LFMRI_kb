---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-G25
citation_key: Poole2014ConvexOptimisationGradientShimWinding
title: Convex optimisation of gradient and shim coil winding patterns
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
acquisition_status: candidate
source_list_slug: gradient-and-shim-coil-design-papers-since-1990
source_list_record_id: G25
import_method: external-list
sources:
  - doi: 10.1016/j.jmr.2014.04.015
    pmid:
    url: https://doi.org/10.1016/j.jmr.2014.04.015
    access: unknown
---

# 論文ノート: Convex optimisation of gradient and shim coil winding patterns

## Citation

- Authors: M. S. Poole et al.
- Year: 2014
- Title: Convex optimisation of gradient and shim coil winding patterns
- Journal / venue: Journal of Magnetic Resonance, 244, 36–45
- DOI: 10.1016/j.jmr.2014.04.015
- PMID:
- URL: https://doi.org/10.1016/j.jmr.2014.04.015
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: candidate
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1016/j.jmr.2014.04.015); [PubMed](https://pubmed.ncbi.nlm.nih.gov/24880337/)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

境界要素法によるコイルモデルと凸最適化を組み合わせ、勾配コイルとシムコイルの巻線パターンを設計します。lp ノルム型の正則化など、目的関数と制約を比較します。疎な巻線や均一な巻線分布を誘導でき、ワイヤ幅、製作性、局所密度制約が重要な場合に有用です。

## Relevance to low-field MRI

| Item | Notes |
|---|---|
| Field strength |  |
| Target use case | custom |
| Subsystem | gradient-and-b0-field-control |
| Form factor | fixed |
| Study type | technical |
| Comparator |  |

## Source list import

| Item | Value |
|---|---|
| Source list | `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md` |
| Record ID | `G25` |
| Area | Gradient / Shim |
| Publication time | 2014 Jul |
| Venue / pages | Journal of Magnetic Resonance, 244, 36–45 |
| Imported links | [DOI resolver](https://doi.org/10.1016/j.jmr.2014.04.015); [PubMed](https://pubmed.ncbi.nlm.nih.gov/24880337/) |
| Method family | convex-optimization |
| Geometry | unspecified |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/gradients.md;kb/hardware/b0-field-control.md` |

## Imported abstract (EN, paraphrased)

This paper combines boundary-element coil modeling with convex optimization to design both gradient and shim winding patterns. It compares cost functions and constraints, including lp-norm style regularization. Sparse or evenly distributed wire patterns can be encouraged, making the method useful when wire width, manufacturability, or local density constraints matter.

## Imported abstract (JA)

境界要素法によるコイルモデルと凸最適化を組み合わせ、勾配コイルとシムコイルの巻線パターンを設計します。lp ノルム型の正則化など、目的関数と制約を比較します。疎な巻線や均一な巻線分布を誘導でき、ワイヤ幅、製作性、局所密度制約が重要な場合に有用です。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `G25`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `G25`. |
