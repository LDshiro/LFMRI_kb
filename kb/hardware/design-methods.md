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

このページは、低磁場MRIにおけるハードウェア設計法を、磁石、勾配、RF、遮蔽、システム統合の観点から整理し、論文ごとの設計判断とトレードオフを横断比較するための作業ページです。

## Scope

- 対象範囲: 低磁場MRIまたはポータブルMRIにおける装置アーキテクチャ、磁石設計、勾配コイル設計、RFコイル設計、遮蔽、電力・機械統合。
- 対象外: 画像再構成のみの論文、臨床性能のみを扱う論文、ハードウェア条件が不明な報告。
- 関連する磁場強度・装置条件: おおむね 0.01T から 1T 未満の低磁場システム、可搬型または設置制約の強いシステムを優先。

## Current summary

> Draft note: ここには、文献確認後に横断要約を追加します。初期段階では、論文ごとの設計目標、主要制約、評価方法を抽出し、`literature/evidence-tables/hardware-design-methods.csv` に集約します。

## Synthesis axes

| Subsystem | Primary design goals | Metrics to track | Related page |
|---|---|---|---|
| Magnet | field strength, homogeneity, weight, cost proxy, portability | B0, DSV, ppm, weight, power | `kb/hardware/magnets.md` |
| Gradient | encoding efficiency, linearity, slew, shielding | mT/m, T/m/s, linearity, heating | `kb/hardware/gradients.md` |
| RF | sensitivity, transmit efficiency, loading robustness, coverage | SNR proxy, Q, channel count | `kb/hardware/rf-coils.md` |
| Shielding / EMC | fringe field control, siting feasibility, emissions | shielding method, footprint, compliance notes | `kb/hardware/shielding.md` |
| Integration | packaging, thermal and power limits, workflow fit | system weight, power, setup time | `kb/hardware/portable-systems.md` |

## Key claims

| Claim | Evidence | Source | Status |
|---|---|---|---|
| 装置設計法の主張は、定量条件と検証モードを分けて整理する必要がある。 | `hardware-design-methods.csv` に設計目標、条件、検証モードを分離して記録する。 | scaffold decision | draft |

## Design trade-off matrix

| Trade-off | Typical benefit | Typical cost | Evidence source |
|---|---|---|---|
| 磁場強度を上げる | SNRやコントラスト設計の自由度 | 重量、電力、遮蔽要求の増加 | to be filled |
| コンパクト化する | 可搬性、設置柔軟性 | 均一性、勾配性能、冷却余裕の制約 | to be filled |
| 多チャンネルRF化する | 受信感度やカバレッジ向上 | 複雑性、コスト、調整負荷の増加 | to be filled |
| 遮蔽を強化する | 設置自由度、EMC対策 | 重量、サイズ、製造コストの増加 | to be filled |

## Practical implications

- 研究計画への示唆: 論文比較では、サブシステム別の設計目標と統合制約を分けて読む。
- 実験設計への示唆: シミュレーションのみの論文と試作検証済み論文を区別して扱う。
- 装置比較への示唆: 装置スペックだけでなく、どの設計制約を優先した結果かを記録する。

## Open questions

- [ ] サブシステム別の主要レビュー論文を追加する。
- [ ] `literature/evidence-tables/hardware-design-methods.csv` に初回抽出を入れる。
- [ ] `kb/hardware/magnets.md`、`gradients.md`、`rf-coils.md`、`shielding.md`、`portable-systems.md` とのリンクを強化する。
- [ ] 設計最適化手法を、解析設計、数値最適化、経験則ベースに分類する。

## Related pages

- `literature/reading-list.md`
- `literature/search-strategies/pubmed-hardware-design-methods.md`
- `literature/search-strategies/scholar-hardware-design-methods.md`
- `literature/evidence-tables/hardware-design-methods.csv`
- `kb/hardware/magnets.md`
- `kb/hardware/gradients.md`
- `kb/hardware/rf-coils.md`
- `kb/hardware/shielding.md`
- `kb/hardware/portable-systems.md`

## Source log

| Date | Source | Access | Note |
|---|---|---|---|
| 2026-04-20 | initial scaffold | unknown | ハードウェア設計法の横断整理ページを追加 |
