---
id: LF-MRI-SEARCH-PUBMED-001
title: PubMed検索式: low-field MRI
status: draft
created: 2026-04-20
last_run:
database: PubMed
tags:
  - literature-search
  - pubmed
---

# PubMed検索式: low-field MRI

## Purpose

低磁場MRI、ポータブルMRI、低磁場再構成、臨床応用に関する文献を再現可能に収集する。

## Candidate query

```text
("low-field MRI" OR "low field MRI" OR "low-field magnetic resonance imaging" OR "portable MRI" OR "point-of-care MRI")
```

## Expanded query candidates

```text
("low-field MRI" OR "portable MRI") AND (brain OR stroke OR hemorrhage OR hydrocephalus)
```

```text
("low-field MRI" OR "low field MRI") AND (reconstruction OR denoising OR "deep learning" OR "compressed sensing")
```

```text
("low-field MRI" OR "portable MRI") AND (phantom OR quality OR "quality assurance" OR SNR)
```

## Search log

| Date | Query | Filters | Hits | Export file | Notes |
|---|---|---|---:|---|---|
| 2026-04-20 | initial candidate | none |  |  | 未実行 |

## Screening criteria

### Include

- 低磁場MRIまたはポータブルMRIを主題に含む。
- 磁場強度、装置仕様、撮像条件、再構成、臨床評価のいずれかを含む。
- 原著論文、総説、技術報告、ガイドライン。

### Exclude

- MRIではない磁気計測のみの研究。
- 低磁場という語が背景説明だけに出る文献。
- 再配布不可資料の全文保存。
