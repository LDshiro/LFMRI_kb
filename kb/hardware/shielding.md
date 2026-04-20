---
id: LF-MRI-HW-SHIELDING-001
title: 遮蔽と設置環境
status: draft
owner: unassigned
created: 2026-04-20
last_reviewed:
review_cycle: 6 months
tags:
  - low-field-mri
  - hardware
  - shielding
evidence_level: not-yet-assessed
sources: []
---

# 遮蔽と設置環境

## Purpose

このページは、gradient / shim 設計と結びついた shielding、active screening、eddy-current mitigation、設置制約を整理するための作業ページです。ここでは room shielding 一般ではなく、coil design に埋め込まれた遮蔽要件を扱います。

## Scope

- 対象範囲: actively shielded gradients、shielded shim design、external-field suppression、compact scanner の eddy-current mitigation。
- 対象外: 建屋 RF shield の一般論、EMC 規格そのもの、full text 未確認の詳細性能比較。
- 関連する磁場強度・装置条件: compact, permanent-magnet, cryogen-free, short / open-bore system を優先する。

## Current summary

取り込み済み source list では、`active-shielding` 6 件、`shielded-design` 6 件、`eddy-current-mitigation` 1 件が分類されています。代表的な関連論文は `G01`, `G03`, `G04`, `G05`, `G07`, `G17`, `G30`, `G31`, `S08` です。shielding は gradient coil の fringe field を抑える古典的テーマですが、low-field permanent-magnet system では eddy-current mitigation として再び前面化しています。

## Key claims

| Claim | Evidence | Source | Status |
|---|---|---|---|
| Active magnetic screening は 1990年代初頭から確立した design primitive で、現在の compact MRI まで連続している。 | `G01`, `G03`, `G07`, `G17`, `G31` が active / shielded gradient を扱う。 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | draft |
| shielding は linearity や inductance と競合するので、gradient geometry と同時に最適化する必要がある。 | shielded gradient 論文の要約が一貫して trade-off を扱う。 | `G03`, `G07`, `G17` | draft |
| permanent-magnet low-field では、room-level shielding より coil-level eddy-current mitigation が優先課題になる。 | `G30` は permanent magnet MRI system に対する theoretical framework を提示する。 | `Zhang2022TheoreticalFrameworkGradientDesignedMitigate` | draft |

## Representative papers

| Citation key | Design issue | Access | Note |
|---|---|---|---|
| `Bowtell1991GradientActiveMagneticScreening` | active magnetic screening の初期定式化 | unknown | shielding を gradient synthesis に組み込む出発点 |
| `Carlson1992EvaluationShieldedGradient` | shielded gradient の実験評価 | unknown | prediction と measurement の比較 |
| `Crozier1995MethodologyShortWholeBodyShielded` | short shielded gradient | unknown | compact / short-bore に近い制約 |
| `Poole2003ActivelyShieldedMultiLayerGradient` | multilayer + cooling + shielding | unknown | 製造と熱設計も含む |
| `Forbes2003NovelTargetFieldMagneticResonance` | shielded zonal / tesseral shim | unknown | B0 field control 側の shielding |
| `Zhang2022TheoreticalFrameworkGradientDesignedMitigate` | permanent-magnet eddy-current mitigation | purchase-required | low-field directly relevant |
| `Wang2023GradientEnhancedShieldingConstraintCryogen` | enhanced shielding constraint | unknown | cryogen-free superconducting でも継続課題 |

## Practical implications

- 研究計画への示唆: low-field system では shielding を site planning の話として後回しにせず、coil design review に含める。
- 実験設計への示唆: future evidence table では external-field suppression と inductance / efficiency を同時に記録する。
- 実装判断への示唆: passive magnet shielding と coil-level active shielding を混同しない。

## Open questions

- [ ] `G30` の full text を取得し、永久磁石系での eddy-current model を確認する。
- [ ] `G31` の shielding constraint が low-field compact system に転用できるか確認する。
- [ ] shielded shim (`S08`) と passive shimming (`S26`) の役割分担を整理する。

## Related pages

- `literature/reading-list.md`
- `literature/purchase-list.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md`
- `kb/hardware/design-methods.md`
- `kb/hardware/gradients.md`
- `kb/hardware/b0-field-control.md`

## Source log

| Date | Source | Access | Note |
|---|---|---|---|
| 2026-04-20 | initial scaffold | unknown | 初期ページ作成 |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990.md` | mixed | shielding / screening 関連論文を抽出 |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | mixed | shielding_type 派生分類を利用 |
