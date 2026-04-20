---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-G18
citation_key: Lemdiasov2005StreamFunctionGradient
title: A stream function method for gradient coil design
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
source_list_record_id: G18
import_method: external-list
sources:
  - doi: 10.1002/cmr.b.20040
    pmid:
    url: https://doi.org/10.1002/cmr.b.20040
    access: unknown
---

# 論文ノート: A stream function method for gradient coil design

## Citation

- Authors: R. A. Lemdiasov; R. Ludwig
- Year: 2005
- Title: A stream function method for gradient coil design
- Journal / venue: Concepts in Magnetic Resonance Part B, 26B(1), 67–80
- DOI: 10.1002/cmr.b.20040
- PMID:
- URL: https://doi.org/10.1002/cmr.b.20040
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1002/cmr.b.20040)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

任意の電流担持面上の stream function を未知量とする逆問題として、勾配コイル設計を定式化しています。Biot–Savart 則に基づくコスト関数を重み付け・線形化し、行列方程式として解きます。得られた stream function から離散巻線パターンを抽出します。

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
| Record ID | `G18` |
| Area | Gradient |
| Publication time | 2005 |
| Venue / pages | Concepts in Magnetic Resonance Part B, 26B(1), 67–80 |
| Imported links | [DOI resolver](https://doi.org/10.1002/cmr.b.20040) |
| Method family | stream-function |
| Geometry | unspecified |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/gradients.md` |

## Imported abstract (EN, paraphrased)

This paper formulates gradient-coil design as an inverse problem for a surface stream function. A Biot–Savart based cost function is defined on an arbitrary current-carrying surface, and suitable weighting and linearization reduce the problem to a matrix equation. The stream-function solution is then converted into discrete winding paths.

## Imported abstract (JA)

任意の電流担持面上の stream function を未知量とする逆問題として、勾配コイル設計を定式化しています。Biot–Savart 則に基づくコスト関数を重み付け・線形化し、行列方程式として解きます。得られた stream function から離散巻線パターンを抽出します。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `G18`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `G18`. |
