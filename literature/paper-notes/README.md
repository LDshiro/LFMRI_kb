# Paper Notes

1論文につき1つのMarkdownファイルを作成します。

## Naming convention

```text
YYYY-firstauthor-keyword.md
```

Examples:

```text
2026-yamada-portable-brain-mri.md
2024-smith-low-field-reconstruction.md
```

## Required steps

1. `template.md` をコピーする。
2. citation keyを `references.bib` と一致させる。
3. DOI / PMID / URLを確認する。
4. 主要な主張、数値、限界を表に抽出する。
5. 関連する `kb/` ページへリンクする。

## Imported notes

- `imported/<source-list-slug>/` 配下のノートは、外部調査リストから自動生成した intake note です。
- imported note は原則 `status: draft` で始め、`source_list_slug`、`source_list_record_id`、`import_method: external-list` を保持します。
- 上流の source list が更新された場合は、手作業で大量編集するより再インポートを優先します。
- full text を確認した後は、同じノートを更新してもよいですが、verified な主張だけを KB に反映します。
