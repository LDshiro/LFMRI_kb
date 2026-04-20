# ChatGPT Exports

ChatGPT Library / Projectから取得したファイル、手動スナップショット、データエクスポートの扱いを記録します。

## Important rule

このディレクトリは正本ではありません。正本は `kb/`、`literature/`、`data/`、`experiments/` に整形して反映したファイルです。

## Structure

```text
library-downloads/    Libraryから手動でダウンロードしたMarkdown/CSV等
project-snapshots/    Project instructionsや重要プロンプトのスナップショット
raw-data-export/      ChatGPTアカウントデータのzip/json/html。原則git管理しない
```

## Workflow

1. ChatGPT Libraryから必要な成果物をダウンロードする。
2. `library-downloads/YYYY-MM-DD/` に置く。
3. 内容を確認し、正本ディレクトリへ整形して移動する。
4. 整形後、raw exportは必要に応じて削除またはprivate storageへ退避する。
5. `logs/chatgpt-library-sync-log.csv` に同期記録を残す。

## Privacy

raw exportにはチャット履歴、ファイル名、未公開情報、個人情報が含まれる可能性があります。公開リポジトリにコミットしないでください。
