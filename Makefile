.PHONY: check index bundle clean

check:
	python scripts/check_frontmatter.py
	python scripts/validate_bibtex.py literature/references.bib

index:
	python scripts/build_index.py

bundle:
	python scripts/export_release_bundle.py --output release-bundles

clean:
	rm -rf release-bundles
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
