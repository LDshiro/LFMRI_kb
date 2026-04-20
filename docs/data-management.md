# Data Management

## Scope

この文書は、低磁場MRI KBで扱うデータ、派生表、実験結果、文献抽出表の管理方針を定めます。

## Data classes

| Class | Examples | Storage |
|---|---|---|
| Public metadata | DOI, PMID, citation key, search logs | GitHub |
| Derived tables | Evidence tables, comparison tables | GitHub |
| Public datasets | Dataset cards, download instructions | GitHub metadata only |
| Large imaging data | NIfTI, DICOM, raw k-space | External storage / Git LFS if allowed |
| Sensitive data | Clinical images, patient data | Do not commit |
| ChatGPT raw export | zip/json/html | Private local storage only |

## Minimum metadata for derived data

- Source
- Date created
- Script / prompt used
- Processing steps
- Columns and units
- License / usage constraints
- Verification status

## Backup

- GitHub remote repository
- Private encrypted storage for raw export or non-public data
- Separate reference manager backup for PDFs and BibTeX
