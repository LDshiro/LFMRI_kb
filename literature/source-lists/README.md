# Source Lists

このディレクトリでは、外部で作成・提供された調査リストを **正本** として保管します。

## Purpose

- 外部調査リストの原本を保持する。
- KB用に派生生成した registry CSV、paper note、reading-list反映、purchase-list反映の出発点にする。
- 将来同じ形式のリストを再インポートできるよう、入力形式を固定する。

## Standard workflow

1. 外部調査リストの原本をこのディレクトリへ置く。
2. `template.md` の構造と照らして必須要素を確認する。
3. 必要なら `*-access-audit.csv` を作成し、open access / purchase-required などの確認結果を記録する。
4. `scripts/import_external_source_list.py` を実行する。
5. 生成された registry CSV、paper note、reading-list、purchase-list、KB更新内容を確認する。

## Required structure

外部調査リストには、最低限以下を含めます。

- `Last checked`
- overview table
- 各レコードの `### ID. Title` セクション
- Authors
- Venue / pages
- Publication time
- DOI
- Links
- Abstract (EN, paraphrased)
- アブストラクト（日本語要約）

## Naming convention

```text
<source-list-slug>.md
<source-list-slug>-access-audit.csv
<source-list-slug>-registry.csv
<source-list-slug>-reading-list-fragment.md
<source-list-slug>-purchase-fragment.md
```

## Access audit CSV

`*-access-audit.csv` は任意ですが、以下の列を推奨します。

```text
record_id,access_status,verification_status,evidence_url,checked_date,note
```

`access_status` の推奨値は `open-access`、`institutional-access`、`purchase-required`、`abstract-only`、`unknown` です。
