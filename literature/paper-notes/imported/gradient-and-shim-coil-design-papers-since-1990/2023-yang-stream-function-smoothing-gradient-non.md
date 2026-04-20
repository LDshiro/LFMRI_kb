---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-G32
citation_key: Yang2023StreamFunctionSmoothingGradientNon
title: A Stream Function Smoothing Method for the Design of MRI Gradient Coils on Non-Developable Surfaces
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
source_list_record_id: G32
import_method: external-list
sources:
  - doi: 10.3390/s23187912
    pmid:
    url: https://doi.org/10.3390/s23187912
    access: unknown
---

# 論文ノート: A Stream Function Smoothing Method for the Design of MRI Gradient Coils on Non-Developable Surfaces

## Citation

- Authors: H. Yang; X. Ren; S. Zuo; W. Liu
- Year: 2023
- Title: A Stream Function Smoothing Method for the Design of MRI Gradient Coils on Non-Developable Surfaces
- Journal / venue: Sensors, 23(18), 7912
- DOI: 10.3390/s23187912
- PMID:
- URL: https://doi.org/10.3390/s23187912
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.3390/s23187912); [MDPI](https://www.mdpi.com/1424-8220/23/18/7912)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

非可展面上の勾配コイルで、stream function の等高線が製作困難になりやすい問題を扱います。Laplace–Beltrami 型の平滑化作用素を stream function に適用してから等高線を抽出します。複雑曲面で、磁場精度、電力、ワイヤ間隔、曲率を同時に改善することを狙います。

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
| Record ID | `G32` |
| Area | Gradient |
| Publication time | 2023 Sep |
| Venue / pages | Sensors, 23(18), 7912 |
| Imported links | [DOI resolver](https://doi.org/10.3390/s23187912); [MDPI](https://www.mdpi.com/1424-8220/23/18/7912) |
| Method family | stream-function |
| Geometry | non-developable-surface |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/gradients.md` |

## Imported abstract (EN, paraphrased)

The paper addresses winding extraction on non-developable surfaces, where raw stream-function contours can be difficult to manufacture. A smoothing operator based on the Laplace–Beltrami framework is applied to implicit stream functions before contour extraction. The method balances field accuracy, power, wire spacing, and wire curvature on complex coil surfaces.

## Imported abstract (JA)

非可展面上の勾配コイルで、stream function の等高線が製作困難になりやすい問題を扱います。Laplace–Beltrami 型の平滑化作用素を stream function に適用してから等高線を抽出します。複雑曲面で、磁場精度、電力、ワイヤ間隔、曲率を同時に改善することを狙います。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `G32`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `G32`. |
