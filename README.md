# 低磁場MRIナレッジベース / Low-field MRI Knowledge Base

このリポジトリは、低磁場MRI（Low-field MRI）に関する研究・文献レビュー・実験計画・知識整理を継続的に蓄積するためのナレッジベースです。

本リポジトリを **正本（source of truth）** とし、ChatGPT Library / ChatGPT Project は文献要約、表抽出、仮説整理、草稿作成のための **作業場** として使用します。

## 基本方針

- GitHub上のMarkdown、CSV、BibTeX、YAMLを検証済みナレッジの中心にする。
- ChatGPTで生成した内容は、初期状態では必ず `draft` として扱う。
- 論文・数値・臨床性能・安全性・規制に関する記述は、原典確認後に `reviewed` または `stable` へ昇格する。
- PDFや生データは、著作権・個人情報・契約条件を確認した上で、必要に応じてGit LFS、private repository、外部ストレージを使う。
- 公開可能な成果物と、内部作業ログ・未検証草稿・ChatGPTエクスポートを明確に分ける。
- Codexはテストや検証を自律的に実行してよいが、`git add`、`git commit`、`git push`、`git tag` などの git 更新は、結果共有後のユーザー承認を前提とする。

## ディレクトリ概要

```text
kb/                 低磁場MRIのトピック別ナレッジ
literature/          文献リスト、論文ノート、検索式、エビデンステーブル
data/                公開データセット、データカード、派生表
experiments/         ファントム、再構成、シミュレーション、解析ノート
prompts/             ChatGPT Project / Libraryで使うプロンプト
chatgpt-exports/     Library出力・データエクスポートの一時保管と監査ログ
decisions/           重要な設計判断のADR（Architecture Decision Record）
logs/                週次レビュー、文献投入、レビュー履歴、作業ログ
scripts/             ファイル整形、frontmatter確認、BibTeX確認、索引生成
docs/                運用ガイド、スタイルガイド、リリース手順
.github/             GitHub Issue / PRテンプレートとCI設定
```

## 実行前提

- Python 3 を使用します。
- `make` が使える環境では `make check` と `make index` を推奨します。
- `make` が使えない場合は、検証と索引生成をスクリプトで直接実行します。
  - Windows: `py -3 scripts/check_frontmatter.py`, `py -3 scripts/validate_bibtex.py literature/references.bib`, `py -3 scripts/build_index.py`
  - macOS / Linux: `python3 scripts/check_frontmatter.py`, `python3 scripts/validate_bibtex.py literature/references.bib`, `python3 scripts/build_index.py`

## 代表的な調査テンプレート

- 一般的な文献調査: `literature/search-strategies/` → `literature/reading-list.md` → `literature/purchase-list.md` → `literature/references.bib` → `literature/paper-notes/template.md` → `literature/evidence-tables/` → `kb/`
- ハードウェア設計法調査: `literature/search-strategies/pubmed-hardware-design-methods.md`, `literature/search-strategies/scholar-hardware-design-methods.md`, `literature/paper-notes/hardware-design-method-template.md`, `literature/evidence-tables/hardware-design-methods.csv`, `kb/hardware/design-methods.md`

## 最初に行うこと

1. このリポジトリをGitHubにアップロードする。
2. `prompts/project-instructions.md` の内容をChatGPT Projectのinstructionsへ貼り付ける。
3. 文献を追加する前に `GOVERNANCE.md` と `docs/source-policy.md` を確認する。
4. `literature/search-strategies/` に検索式と検索日を記録する。
5. 候補論文を `literature/reading-list.md` に追加し、優先度を付ける。
6. オープンアクセスではない候補や入手未確認の候補は `literature/purchase-list.md` に追加する。
7. 採用した論文の書誌情報を `literature/references.bib` に追加する。
8. 論文ノートを `literature/paper-notes/` に作成する。テーマ専用テンプレートがある場合はそれを優先する。
9. 抽出した主張・数値・限界を `literature/evidence-tables/` と `kb/` に再配置する。
10. `make check` と `make index` を実行してからPRまたは共有に進む。

## 推奨ワークフロー

```text
search strategy log
  ↓ query definition / screening criteria
reading list / purchase list / references.bib
  ↓ priority, access status, citation metadata
ChatGPT Library / Project
  ↓ 文献要約・表抽出・仮説整理
local working tree
  ↓ Markdown / CSV / BibTeXへ整形、paper note / evidence table / kb 更新
make check / make index
  ↓ frontmatter / BibTeX検証、索引更新
result summary to user
  ↓ explicit approval for git update
GitHub branch
  ↓ review checklist
main
  ↓ tag / release
versioned knowledge base
```

## ステータス定義

| status | 意味 |
|---|---|
| `draft` | ChatGPT生成、初期メモ、未検証の草稿。断定的に引用しない。 |
| `reviewed` | 原典・数値・引用の基本確認済み。研究内部で利用可能。 |
| `stable` | 繰り返し参照できる安定版。外部共有候補。 |
| `deprecated` | 古い、誤り、または置換済み。理由と置換先を明記する。 |

## ライセンス

詳細は `LICENSE` を参照してください。原則として、KB本文はCC BY 4.0、スクリプト類はMIT License相当で管理する想定です。外部文献PDFや第三者データは、このリポジトリのライセンス対象外です。

## 引用

このKBを研究資料として参照する場合は、`CITATION.cff` を参照してください。
