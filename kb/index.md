---
id: LF-MRI-KB-INDEX
title: 低磁場MRIナレッジベース索引
status: draft
owner: unassigned
created: 2026-04-20
last_reviewed:
review_cycle: 1 month
tags:
  - low-field-mri
  - index
evidence_level: not-applicable
sources: []
---

# 低磁場MRIナレッジベース索引

このページは `kb/` 配下のトピック別ページへの入口です。

## Major domains

| Domain | Directory | Purpose |
|---|---|---|
| Glossary | `kb/glossary/` | 用語、略語、基本概念 |
| Physics | `kb/physics/` | 低磁場MRIの物理、信号、緩和、アーチファクト |
| Hardware | `kb/hardware/` | 磁石、勾配、RF、遮蔽、コンソール、ポータブル装置 |
| Sequences | `kb/sequences/` | 撮像シーケンスと低磁場向け最適化 |
| Reconstruction | `kb/reconstruction/` | 再構成、ノイズ低減、超解像、アーチファクト補正 |
| Quantitative MRI | `kb/quantitative-mri/` | T1/T2、緩和、拡散、検証 |
| Clinical | `kb/clinical/` | 神経、筋骨格、体幹、小児、point-of-care |
| QA/QC | `kb/qa-qc/` | ファントム、SNR、歪み、安定性、受入試験 |
| Safety / Regulatory | `kb/safety-regulatory/` | 安全性、インプラント、設置、EMC、規制 |
| Open questions | `kb/open-questions/` | 研究仮説、未解決課題、検証計画 |

## Status dashboard

| Status | Count | Notes |
|---|---:|---|
| draft | TBD | 初期作成中 |
| reviewed | TBD | 原典確認後に更新 |
| stable | TBD | リリース時に更新 |
| deprecated | TBD | 廃止時に更新 |

## Maintenance

- `scripts/build_index.py` を実行すると、Markdown索引を自動生成できます。
- 各ページのfrontmatterには `id`、`title`、`status`、`created`、`tags` を必ず入れます。
