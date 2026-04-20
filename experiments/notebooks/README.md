# Notebooks

解析用Jupyter notebooksを置く場所です。

## Naming convention

```text
YYYY-MM-DD_short-description.ipynb
```

## Rules

- notebookだけに重要な結果を閉じ込めない。
- 主要結果は `experiments/<topic>/README.md` または `data/derived-tables/` に反映する。
- 大きな出力画像や中間ファイルはコミットしない。
- 実行環境と乱数seedを明記する。
