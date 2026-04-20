# Prompt: Evidence Table Extraction

```text
以下の文献メモまたは論文本文から、低磁場MRIナレッジベース用のエビデンステーブルに入れる行を抽出してください。

制約:
- 原文にない数値は推測しない。
- 数値には単位を分けて書く。
- 比較条件、磁場強度、装置、シーケンス、対象部位を可能な限り書く。
- 抽出箇所としてページ、表、図、補足資料を記録する。
- 未確認の項目は空欄ではなく `not reported` または `unclear` と書く。
- `verification_status` は初期状態では `draft` とする。

出力CSV列:

citation_key,year,field_strength,device,anatomy,condition,sequence,comparator,metric,value,unit,main_finding,limitations,source_location,verification_status,kb_page
```
