# Style Guide

## Language

- 日本語を基本とし、専門用語は必要に応じて英語併記する。
- 用語は `kb/glossary/` へ集約する。
- 不確かな内容は「未確認」「要出典」「仮説」と明記する。

## Markdown

- 1ファイル1トピック。
- 見出しは `#`, `##`, `###` までを基本とする。
- 長い箇条書きより、必要に応じて表を使う。
- 主要な主張は `Key claims` 表に入れる。

## Frontmatter

KBページと文献ノートには以下を必須とします。

```yaml
---
id: LF-MRI-AREA-SLUG-001
title: タイトル
status: draft
owner: unassigned
created: YYYY-MM-DD
last_reviewed:
review_cycle: 6 months
tags:
  - low-field-mri
sources: []
---
```

## Citations

- 本文中では citation key を使う。
- 詳細な文献情報は `literature/references.bib` に置く。
- 可能な限り DOI / PMID / URLを記録する。
- KBページでアクセス状態を明示したい場合は、`Author2024Topic [OA]`、`Author2024Topic [purchase-required]` のように citation key の後ろへ付記する。
- 抄録のみ確認した文献を使う場合は、`[abstract-only]` と明記し、本文確認済みの表現を避ける。

## Status wording

| Status | Recommended wording |
|---|---|
| draft | 「初期メモ」「未確認」「要出典」 |
| reviewed | 「原典確認済み」「確認済み範囲では」 |
| stable | 「本KBでは〜と整理する」 |
| deprecated | 「この記述は置換済み」 |
