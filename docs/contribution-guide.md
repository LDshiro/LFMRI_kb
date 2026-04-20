# Contribution Guide

## Before contributing

- Read `README.md` and `GOVERNANCE.md`.
- Check whether the topic already exists in `kb/`.
- For literature updates, add or update `literature/references.bib`.
- If you start from an external curated list, place the canonical file in `literature/source-lists/` first.
- Codexがテストや検証を実行した場合、git更新は事前のユーザー承認を必須とします。

## Adding a paper

1. Create a branch: `paper/YYYY-author-keyword`.
2. Record access status in `literature/reading-list.md`. If `purchase-required`, add the paper to `literature/purchase-list.md`.
3. Add or update BibTeX in `literature/references.bib`.
4. Copy `literature/paper-notes/template.md`.
5. Fill citation, access, methods, results, limitations, and action items.
6. Add extracted rows to `literature/evidence-tables/` if applicable.
7. Link the paper note from relevant `kb/` pages.
8. 必要なテストや検証を実行する。
9. Codexに git 更新をさせる場合は、事前に明示的に承認する。
10. Open a Pull Request.

## Importing an external source list

1. Put the original list in `literature/source-lists/<slug>.md`.
2. Check that it follows `literature/source-lists/template.md`.
3. If access status matters, add `literature/source-lists/<slug>-access-audit.csv`.
4. Run `scripts/import_external_source_list.py`.
5. Review the generated registry CSV, imported paper notes, `reading-list.md`, and `purchase-list.md`.
6. Treat the source list as canonical and the generated KB inputs as derived artifacts.
7. Only promote verified claims from imported notes into `kb/` or `evidence-tables/`.

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
