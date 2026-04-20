# ChatGPT Library Workflow

## Purpose

ChatGPT Library / Projectを、低磁場MRIナレッジベースの作業場として使うための手順です。

## Roles

| Tool | Role |
|---|---|
| ChatGPT Project | 継続的な文脈、文献要約、仮説整理 |
| ChatGPT Library | アップロード・生成ファイルの一時保管 |
| GitHub | 正本、履歴、レビュー、リリース |
| Zotero / reference manager | 文献PDFと書誌情報の補助管理 |

## Daily workflow

1. 論文PDF、メモ、表をChatGPT Projectへ投入する。
2. `prompts/paper-summary-prompt.md` または `prompts/evidence-table-extraction.md` を使って構造化する。
3. 出力をMarkdownまたはCSVとして保存する。
4. Libraryからダウンロードする。
5. `chatgpt-exports/library-downloads/YYYY-MM-DD/` に一時保存する。
6. 内容を確認し、正本ディレクトリへ整形して移動する。
7. `logs/chatgpt-library-sync-log.csv` に記録する。

## Weekly workflow

1. 未整理のLibrary出力を棚卸しする。
2. 正本へ反映済みのものと未反映のものを分ける。
3. 未確認の主張をIssue化する。
4. `logs/weekly/YYYY-MM-DD.md` を作成する。

## What not to do

- Libraryにしか存在しない重要情報を放置しない。
- ChatGPT出力を原典確認なしに `stable` としない。
- raw exportを公開リポジトリに入れない。
- 著作権上再配布できないPDFをコミットしない。
