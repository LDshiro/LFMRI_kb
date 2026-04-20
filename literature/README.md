# Literature Workspace

低磁場MRIに関する文献の収集、選別、要約、抽出、KB反映のための作業領域です。

## Structure

```text
references.bib          BibTeX正本
reading-list.md         読むべき文献と優先度
purchase-list.md        購入や取り寄せが必要な文献の管理
source-lists/           外部調査リストの正本と派生 registry
search-strategies/      PubMed、Google Scholar、clinical trial検索式の記録
paper-notes/            1論文1ファイルの詳細ノート
evidence-tables/        主要評価指標の抽出表
review-maps/            トピック地図、引用地図
```

## Rules

- 論文PDFは無断でコミットしません。
- DOI、PMID、URL、取得日を可能な限り記録します。
- 論文ごとに `access_status` を記録し、`purchase-required` の候補は `purchase-list.md` に追加します。
- ChatGPTで作成した要約は `status: draft` とし、原典確認後に昇格します。
- 数値は、条件、測定法、単位、ページを記録します。
- 検証しきれない要約論文は、その旨を明示し、full text確認済みの論文と区別します。
- PubMed検索式などは後で追えるように日時付きで記録します。
- 外部調査リストは `source-lists/` に置き、原本を正本として保持します。
- `source-lists/` から生成した registry CSV、paper notes、reading list、purchase list は派生物なので、上流リストを更新したら再インポートします。

## Workflows

### Manual literature review

1. `search-strategies/` に検索式と日時を残す。
2. `reading-list.md` で優先度と access を決める。
3. `references.bib` と `paper-notes/` を更新する。
4. 必要に応じて `evidence-tables/` と `kb/` へ反映する。

### Imported external source list

1. 外部リスト原本を `source-lists/<slug>.md` として配置する。
2. 必要なら `source-lists/<slug>-access-audit.csv` を作成する。
3. `scripts/import_external_source_list.py` を実行して派生物を生成する。
4. 生成された `paper-notes/imported/<slug>/`、`reading-list.md`、`purchase-list.md`、`references.bib` を確認する。
5. verified な内容だけを `kb/` と `evidence-tables/` に反映する。
