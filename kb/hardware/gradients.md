---
id: LF-MRI-HW-GRADIENTS-001
title: 勾配システム
status: draft
owner: unassigned
created: 2026-04-20
last_reviewed:
review_cycle: 6 months
tags:
  - low-field-mri
  - hardware
  - gradients
evidence_level: not-yet-assessed
sources: []
---

# 勾配システム

## Purpose

このページは、低磁場MRIで使う gradient coil の設計論点を整理するための作業ページです。巻線生成法、幾何制約、shielding、eddy-current mitigation、compact scanner 向け最適化を、外部 source list から導いた draft 根拠でつなぎます。

## Scope

- 対象範囲: gradient coil winding design、linearity、efficiency、inductance、shielding、open / compact / permanent-magnet layout。
- 対象外: gradient driver electronics 単独の論文、PNS 安全性のみの論文、full text 未確認の数値比較。
- 関連する磁場強度・装置条件: general MRI の基礎論文を含むが、low-field / open / permanent-magnet / NICU 文脈を優先する。

## Current summary

`gradient-and-shim-coil-design-papers-since-1990` source list には 35 件の gradient-tagged 論文があります。派生レジストリでは 33 件が gradient-only、3 件 (`G25`, `G27`, `S23`) が gradient と B0 field control の共有論文です。gradient subset では `stream-function` 6 件、`target-field` 3 件、`review` 2 件、`genetic-algorithm` 2 件、`minimum-power` 2 件が目立ち、残りは geometry-specific な設計手法として分散しています。

低磁場への直接 relevance は `G30`, `G34`, `G35` が中心です。これに `G21` と `G26` の open / short-bore 論文を加えると、compact layout 向けの設計条件が見えやすくなります。現時点では full text 未確認の論文が多いため、ここでは方法論の地図と優先順位のみを記述します。

## Key claims

| Claim | Evidence | Source | Status |
|---|---|---|---|
| compact low-field 勾配設計は、従来の長尺円筒系より biplanar や open geometry へ寄る。 | `direct` relevance の `G30`, `G34`, `G35` に加え、`G21`, `G26` が open / compact geometry を扱う。 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | draft |
| shielding は gradient design の後工程ではなく、linearity、inductance、cooling と同時に最適化される。 | active / shielded 関連の代表文献が 1991 から 2023 まで継続している。 | `G01`, `G03`, `G07`, `G17`, `G30`, `G31` | draft |
| recent low-field papers は target-field と stream-function の組み合わせを再利用している。 | `G34` と `G35` は target-field lineage、`G34` は stream-function を組み合わせる。 | `G22`, `G34`, `G35` | draft |

## Method families

| Family | What it buys | Typical limitations | Representative papers |
|---|---|---|---|
| Review / theory map | 方法論の全体像を掴める | 実装詳細は薄い | `Turner1993GradientReview`, `Tobon2010TheoryGradientMagneticResonanceImaging` |
| Stream-function | 連続電流密度から巻線へ落としやすい | surface 定義と離散化の影響が強い | `Tomasi2001StreamFunctionOptimizationGradient`, `Lemdiasov2005StreamFunctionGradient`, `Littin2021StreamFunctionsThinWiresIntuitive` |
| Target-field | ROI での場仕様を直接定義しやすい | shielding / inductance と競合しやすい | `Chronik1998ConstrainedLengthMinimumInductanceGradient`, `Huang2025MagneticResonanceBiplanarGradientTarget`, `Liu2025Gradient023TNicu` |
| Direct optimization | geometry freedom が大きい | 目的関数と制約の設計が難しい | `Wong1991OptimizationConjugateGradientDescent`, `Fisher1997BiplanarGradientGeneticAlgorithm`, `Takahashi2024DesigningGradientShapeDerivativeClosed` |
| Specialized geometry methods | toroidal / open / non-developable surface に対応 | 汎用比較がしにくい | `While20093dGradientToroidalSurfaces`, `While20103dGradientOpenSystems`, `Yang2023StreamFunctionSmoothingGradientNon` |

## Geometry and scanner context

| Geometry / context | Why it matters in low-field MRI | Representative papers |
|---|---|---|
| Biplanar | permanent-magnet gap や patient access に適合しやすい | `Fisher1997BiplanarGradientGeneticAlgorithm`, `Huang2025MagneticResonanceBiplanarGradientTarget` |
| Open / short-bore | access と siting を優先できる | `While20103dGradientOpenSystems`, `Wang2016AsymmetricGradientUseShortOpen` |
| Compact permanent-magnet | eddy current と shielding 制約が強い | `Zhang2022TheoreticalFrameworkGradientDesignedMitigate` |
| NICU / bedside | compactness と linearity の同時最適化が必要 | `Liu2025Gradient023TNicu` |
| Arbitrary / non-developable surfaces | enclosure に合わせた winding path を設計できる | `Pissanetzky1992MinimumEnergyGradientGeneralGeometry`, `Yang2023StreamFunctionSmoothingGradientNon` |

## Shielding and eddy-current control

| Design issue | Notes | Representative papers |
|---|---|---|
| Active magnetic screening | fringe field を抑えて周辺導体との結合を減らす古典手法 | `Bowtell1991GradientActiveMagneticScreening`, `Carlson1992EvaluationShieldedGradient` |
| Shielded compact gradients | short / whole-body / multilayer system で shielding と cooling を両立させる | `Crozier1995MethodologyShortWholeBodyShielded`, `Poole2003ActivelyShieldedMultiLayerGradient` |
| Permanent-magnet eddy-current mitigation | low-field permanent-magnet system での渦電流を design objective に入れる | `Zhang2022TheoreticalFrameworkGradientDesignedMitigate` |
| Enhanced shielding constraints | recent superconducting / cryogen-free system でも shielding は継続課題 | `Wang2023GradientEnhancedShieldingConstraintCryogen` |

## Priority reading order

| Priority | Citation key | Why read next | Access |
|---|---|---|---|
| P0 | `Huang2025MagneticResonanceBiplanarGradientTarget` | current biplanar workflow の現代版 | open-access |
| P0 | `Zhang2022TheoreticalFrameworkGradientDesignedMitigate` | permanent-magnet low-field での eddy-current mitigation | purchase-required |
| P0 | `Liu2025Gradient023TNicu` | bedside / NICU 向け compact gradient 設計 | purchase-required |
| P1 | `Turner1993GradientReview` | 古典的 design taxonomy の地図 | unknown |
| P1 | `Poole2007NovelGradientDesignedBoundaryElement` | BEM の橋渡し | unknown |
| P1 | `Tobon2010TheoryGradientMagneticResonanceImaging` | theory-oriented review | unknown |

## Practical implications

- 研究計画への示唆: 低磁場向け gradient 調査は、geometry、shielding、validation mode を必ず分けて記録する。
- 実験設計への示唆: open / compact layout の論文では、ROI 条件と外部場抑制条件を同じ表で管理する。
- 装置統合への示唆: gradient coil だけを比較せず、permanent magnet や NICU enclosure が巻線形状にどう効いているかを読む。

## Open questions

- [ ] `G30`, `G34`, `G35` の full text を確認し、linearity / efficiency / shielding 指標を抽出する。
- [ ] `G21` と `G26` を compact/open geometry の bridge paper として再確認する。
- [ ] `G19`, `G23`, `G33` の数値最適化系を比較できる evidence row を追加する。

## Related pages

- `literature/reading-list.md`
- `literature/purchase-list.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990-registry.csv`
- `kb/hardware/design-methods.md`
- `kb/hardware/b0-field-control.md`
- `kb/hardware/shielding.md`

## Source log

| Date | Source | Access | Note |
|---|---|---|---|
| 2026-04-20 | initial scaffold | unknown | 初期ページ作成 |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990.md` | mixed | gradient 設計論文 35 件を intake |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | mixed | method family, geometry, scanner context を派生整理 |
