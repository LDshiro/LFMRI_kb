---
id: LF-MRI-SEARCH-SCHOLAR-HARDWARE-001
title: Google Scholar検索ログ: low-field MRI hardware design methods
status: draft
created: 2026-04-20
last_run:
tags:
  - literature-search
  - google-scholar
  - hardware
  - low-field-mri
---

# Google Scholar検索ログ: low-field MRI hardware design methods

## Purpose

PubMedで拾いにくい工学系論文、会議録、技術報告、プレプリントを補完し、低磁場MRIのハードウェア設計法を広く把握する。

## Candidate queries

- `"low-field MRI" hardware design`
- `"portable MRI" magnet design`
- `"low-field MRI" gradient coil design`
- `"low-field MRI" RF coil design`
- `"portable MRI" shielding design`
- `"low-field MRI" system integration prototype`
- `"low-field MRI" Halbach MRI design`

## Capture rules

- Google Scholarは検索結果が変動しやすいため、検索日、検索語、上位ヒット、採用理由を必ず残す。
- 上位ヒットは、少なくともタイトル、筆頭著者、年、採用判断を記録する。
- 学会録や企業技術資料は、主要根拠ではなく補助資料として扱う。

## Screening criteria

### Prioritize

- 低磁場MRIの装置アーキテクチャを説明している論文。
- 設計目標と制約条件が明示されている論文。
- 試作機、シミュレーション、ベンチ試験、ファントム試験のいずれかを含む論文。
- 磁石、勾配、RF、遮蔽、可搬性のトレードオフを定量化している論文。

### Deprioritize

- 臨床画像例のみで設計法が読み取れない論文。
- 分解能改善や再構成だけを扱う論文。
- 他モダリティ向け装置設計で、MRIへの転用可能性が薄い論文。

## Result capture log

| Date | Query | Top results captured | Added to reading list | Notes |
|---|---|---:|---:|---|
| 2026-04-20 | initial candidate set |  |  | 雛形作成 |

## High-value metadata to note

| Item | Why it matters |
|---|---|
| Prototype or simulation | 実装段階を区別できる |
| Subsystem scope | magnet / gradient / RF / shielding / integration を切り分けられる |
| Objective function | 何を最適化した設計か比較できる |
| Quantitative constraints | weight, power, homogeneity, slew, cost proxy を比較できる |
| Validation mode | phantom, bench, in vivo, simulation only を識別できる |

## Notes

- Scholarで拾った文献は、原典の DOI や正式出版情報を後で `references.bib` に正規化する。
- 同一著者の複数バージョンが見つかった場合は、正式版を優先し、差分があれば paper note に記録する。
