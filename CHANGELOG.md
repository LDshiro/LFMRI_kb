# Changelog

このファイルは、低磁場MRIナレッジベースの主要な変更を記録します。

形式は [Keep a Changelog](https://keepachangelog.com/) を参考にしていますが、研究ログとして読みやすい記述を優先します。

## [Unreleased]

### Added

- 初期リポジトリ構成を作成。
- `kb/`、`literature/`、`prompts/`、`chatgpt-exports/`、`decisions/`、`logs/`、`scripts/`、`docs/` を追加。
- ChatGPT Project用instructions、文献要約プロンプト、エビデンス抽出プロンプト、週次レビュー用プロンプトを追加。
- 文献ノート、KBページ、データカード、実験ノート、ADR、週次ログのテンプレートを追加。
- frontmatter確認、BibTeX簡易検証、索引生成、リリースバンドル作成用スクリプトを追加。
- ハードウェア設計法調査用の検索戦略、paper noteテンプレート、evidence table、KBページを追加。
- `literature/purchase-list.md` を追加し、購入候補論文の管理を開始。

### Changed

- `README.md` の初期導線と推奨ワークフローを、検索戦略、reading list、検証ステップを含む形に更新。
- 文献運用に `access_status` と `acquisition_status` の記録方針を追加。
- Codexのテスト実行と git 更新の承認フローを `GOVERNANCE.md`、`README.md`、`docs/` に追加。

### Deprecated

- なし。

### Removed

- なし。

### Fixed

- なし。

### Security

- raw ChatGPT export、PDF、環境変数、認証情報を `.gitignore` 対象に設定。

## [0.1.0] - 2026-04-20

### Added

- 初版テンプレート群を作成。
