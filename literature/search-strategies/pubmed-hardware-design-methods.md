---
id: LF-MRI-SEARCH-PUBMED-HARDWARE-001
title: PubMed検索式: low-field MRI hardware design methods
status: draft
created: 2026-04-20
last_run:
database: PubMed
tags:
  - literature-search
  - pubmed
  - hardware
  - low-field-mri
---

# PubMed検索式: low-field MRI hardware design methods

## Purpose

低磁場MRIのハードウェア設計法に関する文献を、再現可能な形で収集する。特に、磁石、勾配コイル、RFコイル、遮蔽、ポータブル化、システム統合の設計論文を対象とする。

## Primary query

```text
(("low-field MRI" OR "low field MRI" OR "portable MRI" OR "point-of-care MRI")
AND
(hardware OR magnet* OR gradient* OR "RF coil" OR receive coil OR transmit coil OR shielding OR console OR "system design" OR topology OR optimization))
```

## Expanded query candidates

### Magnet design

```text
(("low-field MRI" OR "portable MRI")
AND
(magnet OR permanent magnet OR Halbach OR electromagnet OR biplanar)
AND
(design OR optimization OR homogeneity OR topology))
```

### Gradient design

```text
(("low-field MRI" OR "portable MRI")
AND
("gradient coil" OR gradient)
AND
(design OR optimization OR linearity OR shielding))
```

### RF coil design

```text
(("low-field MRI" OR "portable MRI")
AND
("RF coil" OR receive coil OR transmit coil OR array coil)
AND
(design OR tuning OR matching OR sensitivity))
```

### Shielding and integration

```text
(("low-field MRI" OR "portable MRI")
AND
(shielding OR EMC OR "electromagnetic compatibility" OR portability OR integration)
AND
(design OR system OR prototype))
```

## Screening criteria

### Include

- 低磁場MRIまたはポータブルMRIを主題に含む。
- ハードウェア設計、最適化、試作、または技術検証の記述がある。
- 磁場強度、設計目標、構成要素、評価指標のいずれかが読み取れる。
- 原著論文、技術報告、総説、設計論文。

### Exclude

- ハードウェア詳細のない臨床性能報告のみの論文。
- 再構成やAIのみを扱い、装置設計へ踏み込まない論文。
- NMRハードウェアや磁気計測で、MRIシステム設計と直接つながらない論文。
- ポスター要旨のみで、設計条件や評価条件が拾えないもの。

## Extraction focus

| Subsystem | Design variables to capture | Output destination |
|---|---|---|
| Magnet | topology, field strength, DSV, homogeneity, weight, power | `hardware-design-methods.csv`, `kb/hardware/magnets.md` |
| Gradient | coil geometry, efficiency, linearity, slew, shielding | `hardware-design-methods.csv`, `kb/hardware/gradients.md` |
| RF | coil type, channel count, tuning/matching, loading sensitivity | `hardware-design-methods.csv`, `kb/hardware/rf-coils.md` |
| Shielding / EMC | passive or active shielding, siting constraints, emissions | `hardware-design-methods.csv`, `kb/hardware/shielding.md` |
| Integration | portability, mechanical packaging, thermal and power constraints | `hardware-design-methods.csv`, `kb/hardware/portable-systems.md` |

## Search log

| Date | Query | Filters | Hits | Export file | Notes |
|---|---|---|---:|---|---|
| 2026-04-20 | initial candidate | none |  |  | 雛形作成 |

## Notes

- 採用した論文は `literature/reading-list.md` に追加する。
- 採否判断に迷う論文は、除外理由をこのファイルか paper note 側に短く残す。
- 同一システムの系列論文は、設計論文と臨床評価論文を分けて扱う。
