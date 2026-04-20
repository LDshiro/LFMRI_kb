# Contribution Guide

## Before contributing

- Read `README.md` and `GOVERNANCE.md`.
- Check whether the topic already exists in `kb/`.
- For literature updates, add or update `literature/references.bib`.
- Codexがテストや検証を実行した場合、git更新は結果共有後のユーザー承認を前提とします。

## Adding a paper

1. Create a branch: `paper/YYYY-author-keyword`.
2. Record access status in `literature/reading-list.md`. If `purchase-required`, add the paper to `literature/purchase-list.md`.
3. Add or update BibTeX in `literature/references.bib`.
4. Copy `literature/paper-notes/template.md`.
5. Fill citation, access, methods, results, limitations, and action items.
6. Add extracted rows to `literature/evidence-tables/` if applicable.
7. Link the paper note from relevant `kb/` pages.
8. 必要なテストや検証結果を確認する。
9. Codexに git 更新をさせる場合は、結果共有後に明示的に承認する。
10. Open a Pull Request.

## Updating a KB page

1. Check frontmatter.
2. Keep claims and evidence separated.
3. Use tables for claims, metrics, and open questions.
4. Avoid unsupported clinical or device claims.
5. Distinguish open-access and restricted-access sources when useful.
6. Add source log entries.

## Commit message examples

```text
add paper note: 2026 yamada portable brain mri
update evidence table: neuro low-field performance
revise kb: low-field snr limitations
add prompt: claim checking workflow
fix metadata: frontmatter status fields
```
