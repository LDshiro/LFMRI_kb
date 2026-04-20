# Contribution Guide

## Before contributing

- Read `README.md` and `GOVERNANCE.md`.
- Check whether the topic already exists in `kb/`.
- For literature updates, add or update `literature/references.bib`.

## Adding a paper

1. Create a branch: `paper/YYYY-author-keyword`.
2. Add or update BibTeX in `literature/references.bib`.
3. Copy `literature/paper-notes/template.md`.
4. Fill citation, methods, results, limitations, and action items.
5. Add extracted rows to `literature/evidence-tables/` if applicable.
6. Link the paper note from relevant `kb/` pages.
7. Open a Pull Request.

## Updating a KB page

1. Check frontmatter.
2. Keep claims and evidence separated.
3. Use tables for claims, metrics, and open questions.
4. Avoid unsupported clinical or device claims.
5. Add source log entries.

## Commit message examples

```text
add paper note: 2026 yamada portable brain mri
update evidence table: neuro low-field performance
revise kb: low-field snr limitations
add prompt: claim checking workflow
fix metadata: frontmatter status fields
```
