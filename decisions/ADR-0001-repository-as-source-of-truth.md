# ADR-0001: GitHubリポジトリを正本とする

- Status: accepted
- Date: 2026-04-20
- Decision owner: unassigned

## Context

低磁場MRIの研究ナレッジベースでは、ChatGPT Library / Projectを使って文献要約、草稿、表抽出を行う。一方で、ChatGPT側のファイル・チャットは、差分管理、レビュー、リリース、公開範囲制御においてGitHubほど厳密ではない。

## Decision

GitHubリポジトリを正本とする。ChatGPT Library / Projectは作業場として使い、検証済みまたは整理済みの成果物だけをGitHubへ反映する。

## Rationale

- Gitは差分、履歴、レビュー、タグ付けに適している。
- GitHub Issues / Pull Requestsにより、文献確認やKB更新のレビュー工程を明示できる。
- ChatGPT生成物を `draft` として受け取り、人間の確認後に昇格する運用を実装しやすい。

## Consequences

### Positive

- 研究ログが再現可能になる。
- 誤った出力や未確認情報を正本に混ぜにくくなる。
- 外部共有や共同研究に移行しやすい。

### Negative / trade-offs

- ChatGPT LibraryからGitHubへの手動同期が必要。
- raw exportと正本の重複管理が発生する。

## Review date

- 2026-07-20
