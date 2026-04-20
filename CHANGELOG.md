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
- `literature/source-lists/` を追加し、外部調査リストを正本として保持する intake 運用を追加。
- `scripts/import_external_source_list.py` を追加し、registry CSV、paper note、reading list、purchase list、BibTeX への反映を自動化。
- `gradient_and_shim_coil_design_papers_since_1990` を source-list として取り込み、62件の draft note と registry CSV を生成。
- `kb/hardware/b0-field-control.md` を追加し、gradient / shim / shielding 関連 KB を source-list ベースで更新。

### Changed

- `README.md` の初期導線と推奨ワークフローを、検索戦略、reading list、検証ステップを含む形に更新。
- 文献運用に `access_status` と `acquisition_status` の記録方針を追加。
- Codexのテスト実行と git 更新の承認フローを `GOVERNANCE.md`、`README.md`、`docs/` に追加。
- README / literature docs / contribution guide に、external source list を正本、KB 反映を派生物とする運用を追加。

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
