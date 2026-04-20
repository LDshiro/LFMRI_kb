# Source Policy

## Source hierarchy

| Level | Source type | Use |
|---|---|---|
| A | 査読済み原著論文、総説、標準、規制当局文書 | 主要主張の根拠 |
| B | 学会発表、preprint、技術レポート | 新規動向、仮説形成 |
| C | 企業資料、製品ページ、プレスリリース | 装置情報。ただし最新確認が必要 |
| D | ブログ、ニュース、二次記事 | 背景把握。主要根拠にはしない |
| E | ChatGPT出力 | 草稿。根拠にはしない |

## Claims that always need sources

- 磁場強度、SNR、空間分解能、撮像時間などの数値
- 診断性能、臨床有用性、非劣性、安全性
- 装置仕様、製品の入手性、規制承認、保険適用
- 研究の新規性、世界初、最先端などの優先権主張

## Citation minimum

文献ノートには、可能な限り以下を記録します。

- DOI
- PMID
- URL
- 出版年
- 取得日
- 対象部位
- 磁場強度
- 研究デザイン

## Access and acquisition tracking

- 文献ごとに `access_status` を記録します。推奨値は `open-access`、`institutional-access`、`purchase-required`、`abstract-only`、`unknown` です。
- `purchase-required` の文献は `literature/purchase-list.md` に追加し、取得経路や保留理由を管理します。
- 抄録しか確認していない文献は `abstract-only` とし、full text確認済みの根拠と混同しません。
- KBページの `Source` や `Source log` では、必要に応じて citation key の後ろに `[OA]`、`[institutional]`、`[purchase-required]`、`[abstract-only]` を付けてアクセス状態を明示します。

## AI-generated content

ChatGPT出力は文献検索や草稿作成に使えますが、引用根拠にはなりません。ChatGPTが提示した情報は、必ず原典へ戻って確認してください。
