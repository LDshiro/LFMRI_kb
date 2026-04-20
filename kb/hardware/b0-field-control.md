---
id: LF-MRI-HW-B0-FIELD-CONTROL-001
title: B0 Field Control
status: draft
owner: unassigned
created: 2026-04-20
last_reviewed:
review_cycle: 6 months
tags:
  - low-field-mri
  - hardware
  - b0-field-control
evidence_level: not-yet-assessed
sources: []
---

# B0 Field Control

## Purpose

このページは、shim coil、localized multicoil array、passive shimming、encoding-adjacent B0 control を整理するための作業ページです。低磁場 MRI では、gradient 設計と同様に B0 control も geometry と integration の制約を強く受けるため、独立した設計テーマとして扱います。

## Scope

- 対象範囲: zonal / tesseral shim coil、bi-planar shim、multicoil B0 control、passive shimming、field-map driven array design。
- 対象外: magnet steel の詳細加工手順、臨床撮像結果のみの論文、full text 未確認の数値比較。
- 関連する磁場強度・装置条件: permanent-magnet、ultra-low-field、head-only、brain-specific array、compact scanner。

## Current summary

source list の元分類では Shim / B0 control 系は 27 件です。派生レジストリでは 26 件が b0-field-control-only、3 件 (`G25`, `G27`, `S23`) が gradient との共有論文です。method family は `target-field` 6 件、`stream-function` 3 件、`passive-shimming` 2 件、`multicoil` 1 件、`active-shimming` 1 件、`linear-programming` 1 件などに分かれます。

direct low-field relevance を持つ priority 論文は `S17`, `S18`, `S19`, `S26` です。ここから見える流れは、有限長 shim の target-field lineage から、permanent-magnet 向け bi-planar shim、さらに passive shimming まで設計対象が広がっていることです。一方で high-field brain MRI 側では localized multicoil array が subject-specific control の主流になっています。

## Key claims

| Claim | Evidence | Source | Status |
|---|---|---|---|
| target-field 系は zonal / tesseral shim から bi-planar permanent-magnet shim まで連続して使われている。 | 2001-2003 の `S04`, `S05`, `S08` と、2010 の `S17` が同系統に並ぶ。 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | draft |
| multicoil B0 control は、固定 harmonic basis ではなく anatomy-specific / slice-specific control へ向かう流れを示す。 | `S12`, `S13`, `S14`, `S15`, `S20`, `S22`, `S25` が localized coil array を扱う。 | `gradient-and-shim-coil-design-papers-since-1990.md` | draft |
| low-field permanent-magnet では passive shimming が再び重要になる。 | `S26` が direct low-field priority、`S27` が passive shimming parameter study。 | `Liu2025PassiveShimmingPermanentMagnetDynamic`, `Liu2025PassiveShimmingPerformance3T` | draft |

## Method families

| Family | What it solves | Representative papers | Notes |
|---|---|---|---|
| Target-field shims | zonal / tesseral / finite-length shim synthesis | `Forbes2001NovelTargetFieldFiniteLength`, `Forbes2002NovelTargetFieldFiniteLength`, `Forbes2003NovelTargetFieldMagneticResonance` | finite-length, shielded variantsまで含む |
| Stream-function and winding synthesis | 複雑な winding pattern を実装可能形状に落とす | `Brideson2002DeterminingComplicatedWindingPatternsShim`, `Liu2010NovelTargetFieldBiPlanar` | shim 側でも gradient と同じ表現が使われる |
| Localized multicoil arrays | anatomy- or slice-specific B0 correction | `Juchem2010MagneticFieldHomogenizationHumanPrefrontal`, `Juchem2011DynamicMultiShimmingHumanBrain`, `Jia2020ShimArrayMatchedHumanBrain`, `Theilenberg2023RealizationMultiArrayB0Field` | fixed SH basisより柔軟だが実装は複雑 |
| Passive shimming | 電力を使わず B0 を追い込む | `Liu2025PassiveShimmingPermanentMagnetDynamic`, `Liu2025PassiveShimmingPerformance3T` | permanent-magnet 低磁場では特に重要 |

## Low-field priority papers

| Priority | Citation key | Focus | Access | Note file |
|---|---|---|---|---|
| P0 | `Liu2010NovelTargetFieldBiPlanar` | permanent-magnet bi-planar shim | purchase-required | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2010-liu-novel-target-field-bi-planar.md` |
| P0 | `Xia2017TheoryDevelopmentBiplanarActiveShim` | active shim for permanent analyzer | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2017-xia-theory-development-biplanar-active-shim.md` |
| P0 | `He2018BiplanarShimUltraLowField` | ultra-low-field biplanar shim | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2018-he-biplanar-shim-ultra-low-field.md` |
| P0 | `Liu2025PassiveShimmingPermanentMagnetDynamic` | passive shimming for permanent-magnet MRI | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2025-liu-passive-shimming-permanent-magnet-dynamic.md` |
| P1 | `Lee2022SystematicDimensionalAnalysisScalingRelationship` | gradient / shim scaling relationship | unknown | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2022-lee-systematic-dimensional-analysis-scaling-relationship.md` |

## Design trade-offs

| Trade-off | Benefit | Cost | Representative papers |
|---|---|---|---|
| Higher-order fixed shim basis | 標準化しやすい | anatomy-specific inhomogeneity への適応が弱い | `S03`, `S04`, `S05`, `S06` |
| Localized multicoil array | ROI に合わせて柔軟に最適化できる | channel 数、制御、設置性が重くなる | `S12`, `S15`, `S20`, `S25` |
| Bi-planar geometry | permanent-magnet gap や open access に適合 | 3D 均一性と shielding の設計が難しい | `S17`, `S18`, `S19` |
| Passive shimming | power-free で実装できる | initial field map と再調整に依存 | `S26`, `S27` |

## Practical implications

- 研究計画への示唆: low-field magnet system を調べるときは、gradient と shim を別ページで追うが、geometry は同じ列で管理する。
- 実験設計への示唆: B0 control は static shim だけでなく slice-based / dynamic / field-map driven の違いを明記する。
- KB 反映への示唆: localized multicoil array の論文は high-field 由来が多いので、low-field への外挿は `bridge` と明示して扱う。

## Open questions

- [ ] `S17` の full text を取得し、bi-planar shim の target specification を確認する。
- [ ] `S18` と `S19` から ultra-low-field / permanent analyzer での validation mode を抽出する。
- [ ] `S26` の passive shimming workflow を low-field magnet design page と接続する。
- [ ] `S20`, `S22`, `S25` を compact head-only MRI への橋渡しとして再整理する。

## Related pages

- `literature/reading-list.md`
- `literature/purchase-list.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990-registry.csv`
- `kb/hardware/design-methods.md`
- `kb/hardware/gradients.md`
- `kb/hardware/shielding.md`

## Source log

| Date | Source | Access | Note |
|---|---|---|---|
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990.md` | mixed | shim / B0 field control 27件を intake |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | mixed | method family, geometry, low-field relevance を派生整理 |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990-access-audit.csv` | mixed | P0 の access 状態を spot-check |
