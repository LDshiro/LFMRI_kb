---
id: LF-MRI-HW-DESIGN-METHODS-001
title: 低磁場MRIのハードウェア設計法
status: draft
owner: unassigned
created: 2026-04-20
last_reviewed:
review_cycle: 6 months
tags:
  - low-field-mri
  - hardware
  - design-methods
evidence_level: not-yet-assessed
sources: []
---

# 低磁場MRIのハードウェア設計法

## Purpose

このページは、低磁場MRIで重要になるハードウェア設計法を、勾配コイル、B0 field control、遮蔽、統合制約の観点から横断整理するための作業ページです。外部調査リストから取り込んだ論文群を起点に、方法論ファミリ、装置文脈、優先度、アクセス状況を一貫して追跡します。

## Scope

- 対象範囲: 勾配コイル設計、shim coil / multicoil / passive shimming、shielded gradient、eddy-current mitigation、装置小型化に伴う幾何制約。
- 対象外: 画像再構成のみの論文、臨床アウトカムだけを扱う論文、full text 未確認の数値性能比較。
- 関連する磁場強度・装置条件: permanent magnet、ultra-low-field、open/open-bore、NICU、head-only など、設置制約が強い装置文脈を優先する。

## Current summary

`literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md` は、現時点の coil-design intake の正本です。この source list は 62 件を含み、元ファイルの分類では Gradient 35 件、Shim / B0 field control 27 件です。派生生成したレジストリでは、33 件が gradient-only、26 件が b0-field-control-only、3 件が gradient と B0 control の共有論文 (`G25`, `G27`, `S23`) として整理されています。

方法論ファミリは、`stream-function` 9 件、`target-field` 9 件、その他 20 件を中心に、`boundary-element`、`finite-difference`、`convex-optimization`、`multicoil`、`passive-shimming` などへ分岐しています。したがって、このページでは個々の装置性能を比較するより、どの最適化原理がどの幾何制約と結びついているかを読むのが主目的になります。

## Synthesis axes

| Axis | What to compare | Current examples | Related page |
|---|---|---|---|
| Gradient winding synthesis | target-field, stream-function, BEM, FD, shape-derivative | `G05`, `G18`, `G19`, `G22`, `G23`, `G33` | `kb/hardware/gradients.md` |
| B0 field control | zonal/tesseral shim, localized coil arrays, passive shimming | `S04`, `S08`, `S12`, `S15`, `S20`, `S26` | `kb/hardware/b0-field-control.md` |
| Shielding / eddy-current control | active shielding, shielded shims, compact-system eddy mitigation | `G01`, `G03`, `G17`, `G30`, `G31`, `S08` | `kb/hardware/shielding.md` |
| Low-field direct relevance | permanent-magnet, ultra-low-field, open geometry, NICU | `G30`, `G34`, `G35`, `S17`, `S18`, `S19`, `S26` | `kb/hardware/gradients.md`, `kb/hardware/b0-field-control.md` |
| Shared design rules | optimization family reused across gradient and shim | `G25`, `G27`, `S23` | `kb/hardware/design-methods.md` |

## Timeline

| Period | Main shift | Representative papers |
|---|---|---|
| 1991-1995 | Active shielding, minimum-energy / minimum-power formulations, early review literature | `Bowtell1991GradientActiveMagneticScreening`, `Carlson1992EvaluationShieldedGradient`, `Turner1993GradientReview`, `Hoult1994AccurateShimMagnetFieldProfiling` |
| 1997-2005 | Biplanar and planar geometries, stream-function lineage, finite-length target-field shims | `Fisher1997BiplanarGradientGeneticAlgorithm`, `Tomasi2001StreamFunctionOptimizationGradient`, `Forbes2001NovelTargetFieldFiniteLength`, `Brideson2002DeterminingComplicatedWindingPatternsShim` |
| 2007-2014 | BEM, theory reviews, finite-difference, convex optimization, early multicoil field control | `Poole2007NovelGradientDesignedBoundaryElement`, `Tobon2010TheoryGradientMagneticResonanceImaging`, `Zhu2012FiniteDifferenceGradientInitialFramework`, `Poole2014ConvexOptimisationGradientShimWinding` |
| 2016-2025 | Open / compact scanner layouts, permanent-magnet low-field work, passive shimming revival | `Wang2016AsymmetricGradientUseShortOpen`, `He2018BiplanarShimUltraLowField`, `Zhang2022TheoreticalFrameworkGradientDesignedMitigate`, `Liu2025Gradient023TNicu`, `Liu2025PassiveShimmingPermanentMagnetDynamic` |

## Key claims

| Claim | Evidence | Source | Status |
|---|---|---|---|
| 勾配コイル設計と B0 field control は、target-field と stream-function を共有する連続した方法論として読む方が整理しやすい。 | レジストリでは `target-field` と `stream-function` がそれぞれ 9 件ずつあり、gradient / shim の両方に跨っている。 | `G05`, `G22`, `G25`, `S04`, `S07`, `S23` | draft |
| 直接的な低磁場 relevance を持つ論文は、全身円筒系よりも biplanar、permanent-magnet、compact-layout に寄っている。 | `direct` と判定されたレコードは `G30`, `G34`, `G35`, `S17`, `S18`, `S19`, `S26` を中心に、永久磁石、ULF、NICU、open 系の文脈を持つ。 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | draft |
| Shielding と eddy-current mitigation は独立の後工程ではなく、低磁場・小型装置では巻線設計の初期条件に入る。 | active shielding / shielded-design / eddy-current-mitigation の関連レコードが少なくとも 13 件あり、compact system 向け論文にも残っている。 | `G01`, `G03`, `G07`, `G17`, `G30`, `G31`, `S08` | draft |
| full-text verification の優先度は access audit と結びつけて管理する必要がある。 | P0 の 7 件中 3 件は `purchase-required`、4 件は `open-access` と確認済みで、`purchase-list.md` に反映済み。 | `literature/purchase-list.md`, `gradient-and-shim-coil-design-papers-since-1990-access-audit.csv` | draft |

## Method families

| Family | Typical objective | Typical geometries | Representative papers |
|---|---|---|---|
| Target-field | 指定 ROI で所望の場分布を満たす | cylindrical, biplanar, finite-length, shielded shim | `Chronik1998ConstrainedLengthMinimumInductanceGradient`, `Forbes2001NovelTargetFieldFiniteLength`, `Liu2010NovelTargetFieldBiPlanar`, `Huang2025MagneticResonanceBiplanarGradientTarget` |
| Stream-function | 連続電流密度から巻線パターンを得る | cylindrical, planar, biplanar, non-developable surface | `Tomasi2001StreamFunctionOptimizationGradient`, `Lemdiasov2005StreamFunctionGradient`, `Yang2023StreamFunctionSmoothingGradientNon` |
| Direct numerical optimization | 誤差関数を直接最小化する | planar, biplanar, arbitrary geometry | `Wong1991OptimizationConjugateGradientDescent`, `Fisher1997BiplanarGradientGeneticAlgorithm`, `Peters1994BiplanarGradientSimulatedAnnealing` |
| Geometry-aware refinement | open / compact / special surfacesに合わせる | toroidal, open-bore, head-only | `While20093dGradientToroidalSurfaces`, `While20103dGradientOpenSystems`, `Theilenberg2023RealizationMultiArrayB0Field` |
| Multicoil / passive shimming | 固定 harmonic basis ではなく局所配列や受動材で補正する | localized-array, array, permanent-magnet | `Juchem2011DynamicMultiShimmingHumanBrain`, `Jia2020ShimArrayMatchedHumanBrain`, `Liu2025PassiveShimmingPermanentMagnetDynamic` |

## Priority papers for low-field hardware

| Priority | Citation key | Focus | Access | Note file |
|---|---|---|---|---|
| P0 | `Zhang2022TheoreticalFrameworkGradientDesignedMitigate` | permanent-magnet gradient and eddy-current mitigation | purchase-required | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2022-zhang-theoretical-framework-gradient-designed-mitigate.md` |
| P0 | `Huang2025MagneticResonanceBiplanarGradientTarget` | biplanar gradient design workflow | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2025-huang-magnetic-resonance-biplanar-gradient-target.md` |
| P0 | `Liu2025Gradient023TNicu` | compact 0.23 T NICU gradient design | purchase-required | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2025-liu-gradient-0-23-t-nicu.md` |
| P0 | `Liu2010NovelTargetFieldBiPlanar` | permanent-magnet bi-planar shim design | purchase-required | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2010-liu-novel-target-field-bi-planar.md` |
| P0 | `Xia2017TheoryDevelopmentBiplanarActiveShim` | active shim for permanent analyzer | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2017-xia-theory-development-biplanar-active-shim.md` |
| P0 | `He2018BiplanarShimUltraLowField` | ultra-low-field biplanar shim | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2018-he-biplanar-shim-ultra-low-field.md` |
| P0 | `Liu2025PassiveShimmingPermanentMagnetDynamic` | passive shimming for permanent-magnet MRI | open-access | `literature/paper-notes/imported/gradient-and-shim-coil-design-papers-since-1990/2025-liu-passive-shimming-permanent-magnet-dynamic.md` |

## Design trade-off matrix

| Trade-off | Typical benefit | Typical cost | Evidence source |
|---|---|---|---|
| 線形性を優先する | usable ROI が広がる | 巻線複雑化、効率やインダクタンスの悪化 | `G03`, `G09`, `G35` |
| Shielding を強める | fringe field と eddy current を抑えやすい | 電力、インダクタンス、冷却、製作難度の負担 | `G01`, `G07`, `G17`, `G31`, `S08` |
| Biplanar / open geometry を採る | patient access や permanent-magnet layout に適合しやすい | 3D 均一性確保が難しくなる | `G10`, `G21`, `G26`, `S17`, `S19` |
| Passive shimming を使う | 電力と制御系を増やさず B0 を補正できる | field-map 依存性、再調整コスト、設計自由度の制約 | `S26`, `S27` |

## Practical implications

- 研究計画への示唆: `P0` 7 件は低磁場ハードウェア設計の一次確認対象として扱い、そこから共通 method family を抽出する。
- 実験設計への示唆: compact geometry の論文では ROI 条件、shielding 条件、cooling / manufacturability を別列で追う。
- KB 反映への示唆: source list の要約は `draft` 根拠として使い、数値・図表・比較表は full text 確認後に only reviewed/stable へ上げる。

## Open questions

- [ ] `P0` 7 件の full text を確認し、methods / results / limitations を各 paper note に反映する。
- [ ] `P1` の橋渡し論文 `G05`, `G19`, `G22`, `G23`, `G25`, `G27`, `S23` を acquisition / access audit する。
- [ ] `hardware-design-methods.csv` へ、verified な数値列だけを転記する。
- [ ] 磁石、RF、portable systems 側でも、同じ source-list intake 運用を作る。

## Related pages

- `literature/reading-list.md`
- `literature/purchase-list.md`
- `literature/source-lists/README.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md`
- `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990-registry.csv`
- `literature/search-strategies/pubmed-hardware-design-methods.md`
- `literature/search-strategies/scholar-hardware-design-methods.md`
- `literature/evidence-tables/hardware-design-methods.csv`
- `kb/hardware/gradients.md`
- `kb/hardware/b0-field-control.md`
- `kb/hardware/shielding.md`

## Source log

| Date | Source | Access | Note |
|---|---|---|---|
| 2026-04-20 | initial scaffold | unknown | ハードウェア設計法の横断整理ページを追加 |
| 2026-04-20 | `literature/source-lists/gradient-and-shim-coil-design-papers-since-1990.md` | mixed | 62件の外部調査リストを正本として取り込み |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990-registry.csv` | mixed | method family, geometry, low-field relevance を派生分類 |
| 2026-04-20 | `gradient-and-shim-coil-design-papers-since-1990-access-audit.csv` | mixed | P0 7件の access 状態を spot-check |
