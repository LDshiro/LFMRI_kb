# ADR-0002: Markdown、CSV、BibTeX、YAMLを基本フォーマットとする

- Status: accepted
- Date: 2026-04-20
- Decision owner: unassigned

## Context

低磁場MRIナレッジベースでは、文献ノート、KBページ、エビデンステーブル、設定、メタデータを長期的に管理する必要がある。

## Decision

以下のフォーマットを標準とする。

| Purpose | Format |
|---|---|
| KB本文・文献ノート | Markdown + YAML frontmatter |
| 文献リスト | BibTeX |
| エビデンステーブル | CSV |
| 設定・語彙 | YAML |
| 実験メタデータ | Markdown + YAML frontmatter |

## Rationale

- テキストベースで差分管理しやすい。
- ChatGPTが読み書きしやすい。
- 他ツールへ変換しやすい。
- 大規模な専用DBを導入する前に、研究の方向性を柔軟に変更できる。

## Consequences

### Positive

- GitHubレビューが容易になる。
- テンプレート化しやすい。
- 将来、静的サイトやデータベースへ移行しやすい。

### Negative / trade-offs

- CSVは複雑な階層データに弱い。
- Markdownは構造の揺れが発生しやすいため、テンプレートとチェックが必要。

## Review date

- 2026-07-20
