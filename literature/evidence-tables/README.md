# Evidence Tables

文献から抽出した数値・主張・条件をCSVで管理します。

## General rules

- 1セルに複数の意味を詰め込まない。
- 値には単位を分けて記録する。
- `source_location` にはページ、表番号、図番号、補足資料番号などを記録する。
- 未確認値は `verification_status=draft` とする。
- 原典確認済みは `verification_status=verified` とする。

## Files

| File | Purpose |
|---|---|
| `neuro-low-field.csv` | 神経領域の臨床・技術エビデンス |
| `musculoskeletal-low-field.csv` | 筋骨格領域のエビデンス |
| `portable-mri-systems.csv` | ポータブル低磁場MRIシステム比較 |
| `reconstruction-methods.csv` | 再構成・ノイズ低減・AI手法 |
| `qa-qc-metrics.csv` | QA/QC指標とファントム評価 |
