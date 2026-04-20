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

### Changed

- なし。

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
