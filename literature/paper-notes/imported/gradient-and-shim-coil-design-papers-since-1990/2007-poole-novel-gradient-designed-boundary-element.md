---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-G19
citation_key: Poole2007NovelGradientDesignedBoundaryElement
title: Novel gradient coils designed using a boundary element method
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
source_list_record_id: G19
import_method: external-list
sources:
  - doi: 10.1002/cmr.b.20091
    pmid:
    url: https://doi.org/10.1002/cmr.b.20091
    access: unknown
---

# 論文ノート: Novel gradient coils designed using a boundary element method

## Citation

- Authors: M. Poole; R. Bowtell
- Year: 2007
- Title: Novel gradient coils designed using a boundary element method
- Journal / venue: Concepts in Magnetic Resonance Part B, 31B(3), 162–175
- DOI: 10.1002/cmr.b.20091
- PMID:
- URL: https://doi.org/10.1002/cmr.b.20091
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: candidate
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1002/cmr.b.20091)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

境界要素法を用いて、任意形状面上の勾配コイルを設計する方法です。表面メッシュ上で stream function により電流密度を表し、Maxwell 方程式と整合する目標場を生成します。抵抗、インダクタンス、トルク、遮蔽に関する項を含められ、非対称・シールド付き勾配面の設計例が示されます。

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
| Record ID | `G19` |
| Area | Gradient |
| Publication time | 2007 |
| Venue / pages | Concepts in Magnetic Resonance Part B, 31B(3), 162–175 |
| Imported links | [DOI resolver](https://doi.org/10.1002/cmr.b.20091) |
| Method family | boundary-element |
| Geometry | unspecified |
| Shielding type | shielded-design |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/gradients.md;kb/hardware/shielding.md` |

## Imported abstract (EN, paraphrased)

The authors use a boundary element method to design gradient coils on arbitrarily shaped surfaces. The surface is meshed, current density is represented by stream functions, and the optimizer can target Maxwell-consistent field variations while including resistance, inductance, torque, or shielding-related terms. Examples include asymmetric and shielded gradient surfaces.

## Imported abstract (JA)

境界要素法を用いて、任意形状面上の勾配コイルを設計する方法です。表面メッシュ上で stream function により電流密度を表し、Maxwell 方程式と整合する目標場を生成します。抵抗、インダクタンス、トルク、遮蔽に関する項を含められ、非対称・シールド付き勾配面の設計例が示されます。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `G19`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `G19`. |
