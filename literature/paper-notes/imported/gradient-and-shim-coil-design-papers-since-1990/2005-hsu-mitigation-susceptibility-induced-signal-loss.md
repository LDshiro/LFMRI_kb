---
id: LF-MRI-PAPER-GRADIENT-AND-SHIM-COIL-DESIGN-PAPERS-SINCE-1990-S10
citation_key: Hsu2005MitigationSusceptibilityInducedSignalLoss
title: Mitigation of susceptibility-induced signal loss in neuroimaging using localized shim coils
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
source_list_record_id: S10
import_method: external-list
sources:
  - doi: 10.1002/mrm.20365
    pmid:
    url: https://doi.org/10.1002/mrm.20365
    access: unknown
---

# 論文ノート: Mitigation of susceptibility-induced signal loss in neuroimaging using localized shim coils

## Citation

- Authors: J. J. Hsu; G. H. Glover
- Year: 2005
- Title: Mitigation of susceptibility-induced signal loss in neuroimaging using localized shim coils
- Journal / venue: Magnetic Resonance in Medicine, 53(2), 243–248
- DOI: 10.1002/mrm.20365
- PMID:
- URL: https://doi.org/10.1002/mrm.20365
- Accessed: 2026-04-20

## Access and rights

- Access status: unknown
- Acquisition status: not-needed
- Full text checked: no
- Access route: [DOI resolver](https://doi.org/10.1002/mrm.20365); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15678595/)
- Alternative route:
- Sharing restrictions: Publisher PDF / full text is not committed to this repository.

## 1-line summary

神経画像で感受率由来の B0 不均一による信号低下を低減するため、局所抵抗シムコイルを用います。問題部位に近い位置へコイルを置き、被験者ごとの in situ 最適化を行います。全体的な球面調和シムでは補正しにくい領域の均一性改善と信号回復を狙います。

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
| Record ID | `S10` |
| Area | Shim |
| Publication time | 2005 Feb |
| Venue / pages | Magnetic Resonance in Medicine, 53(2), 243–248 |
| Imported links | [DOI resolver](https://doi.org/10.1002/mrm.20365); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15678595/) |
| Method family | other |
| Geometry | localized-array |
| Shielding type | none-or-unspecified |
| Scanner context | general-mri |
| KB targets | `kb/hardware/design-methods.md;kb/hardware/b0-field-control.md` |

## Imported abstract (EN, paraphrased)

The paper demonstrates localized resistive shim coils for reducing susceptibility-induced B0 inhomogeneity in neuroimaging. Coils placed close to problematic anatomy are optimized in situ for patient-specific correction. The approach improves field homogeneity and recovers signal in regions that are difficult for global spherical-harmonic shims.

## Imported abstract (JA)

神経画像で感受率由来の B0 不均一による信号低下を低減するため、局所抵抗シムコイルを用います。問題部位に近い位置へコイルを置き、被験者ごとの in situ 最適化を行います。全体的な球面調和シムでは補正しにくい領域の均一性改善と信号回復を狙います。

## Design objective and constraints

- Primary objective:
- Explicit constraints:
- Optimization target:
- Assumed operating environment:

## Key claims

| Claim | Evidence | Limitation | KB destination | Verification status |
|---|---|---|---|---|
| Imported summary available in this note. Full-text verification is pending. | External curated source list record `S10`. | Methods, figures, and exact numeric claims are not yet verified against the full text. | `kb/hardware/design-methods.md` | draft |

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
| 2026-04-20 |  | Imported from external source list `gradient-and-shim-coil-design-papers-since-1990` record `S10`. |
