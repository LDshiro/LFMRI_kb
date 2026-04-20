# Repository Manifest

Generated initial structure date: 2026-04-20

## Core files

- `README.md`: repository overview and first steps.
- `GOVERNANCE.md`: source-of-truth, review, release, and privacy rules.
- `CHANGELOG.md`: change log.
- `CITATION.cff`: citation metadata.
- `LICENSE`: content and code license notice.
- `Makefile`: convenience commands.

## Operational pillars

| Pillar | Directory | Purpose |
|---|---|---|
| Knowledge | `kb/` | Topic-based low-field MRI pages. |
| Literature | `literature/` | Paper notes, references, search strategies, external source lists, evidence tables. |
| Data | `data/` | Dataset cards and derived tables. |
| Experiments | `experiments/` | Protocols, simulations, notebooks, reconstruction experiments. |
| ChatGPT workbench | `prompts/`, `chatgpt-exports/` | Reusable prompts and export/snapshot handling. |
| Governance | `decisions/`, `docs/`, `logs/` | ADRs, rules, release process, review logs. |
| Automation | `scripts/`, `.github/` | Lightweight checks and GitHub templates. |

## Minimum viable maintenance loop

1. Add or update a paper note in `literature/paper-notes/`.
2. If work starts from an external curated list, store the canonical file in `literature/source-lists/` and run the importer first.
3. Add extracted rows to `literature/evidence-tables/`.
4. Update relevant `kb/` pages.
5. Run `make check` and `make index`.
6. Open a pull request using the PR checklist.
