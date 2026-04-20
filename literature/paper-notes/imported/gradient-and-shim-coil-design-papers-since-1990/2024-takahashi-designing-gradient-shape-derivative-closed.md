---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-G33
citation_key: Takahashi2024DesigningGradientShapeDerivativeClosed
title: Designing gradient coils with the shape derivative and the closed B-spline curves
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
source_list_record_id: G33
import_method: external-list
sources:
  - doi: 10.1016/j.mri.2024.03.042
    pmid:
    url: https://doi.org/10.1016/j.mri.2024.03.042
    access: unknown
---

# 論文ノート: Designing gradient coils with the shape derivative and the closed B-spline curves

## Citation

- Authors: T. Takahashi
- Year: 2024
- Title: Designing gradient coils with the shape derivative and the closed B-spline curves
- Journal / venue: Magnetic Resonance Imaging, 110, 112–127
- DOI: 10.1016/j.mri.2024.03.042
- PMID:
- URL: https://doi.org/10.1016/j.mri.2024.03.042
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1016/j.mri.2024.03.042); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0730725X24000422)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

離散勾配コイル設計を形状最適化問題として扱う論文です。コイル形状に対する Bz 勾配の形状微分を導出し、閉 B-spline 曲線の制御点を非線形計画問題の設計変数とします。等高線抽出や確率的探索に対する、勾配ベースの代替アプローチです。

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
| Record ID | `G33` |
| Area | Gradient |
| Publication time | 2024 Jul |
| Venue / pages | Magnetic Resonance Imaging, 110, 112–127 |
| Imported links | [DOI resolver](https://doi.org/10.1016/j.mri.2024.03.042); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0730725X24000422) |
| Method family | shape-derivative |
| Geometry | unspecified |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/gradients.md` |

## Imported abstract (EN, paraphrased)

This paper treats discrete gradient-coil design as a shape-optimization problem. The derivative of the Bz gradient with respect to coil shape is derived, and closed B-spline curves are used so their control points become nonlinear-programming variables. The approach offers a gradient-based alternative to purely contour-based or stochastic winding optimization.

## Imported abstract (JA)

離散勾配コイル設計を形状最適化問題として扱う論文です。コイル形状に対する Bz 勾配の形状微分を導出し、閉 B-spline 曲線の制御点を非線形計画問題の設計変数とします。等高線抽出や確率的探索に対する、勾配ベースの代替アプローチです。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `G33`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `G33`. |
