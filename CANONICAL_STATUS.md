# BioMini Canonical Status

## Current canonical milestone

**BioMini v0.1.0 — Phase I Pre-Freeze**

Phase I implementation Steps 1–15 are complete.
Canonical Audit corrections A–F are resolved and regression-tested.

The Phase I educational course has also been completed as eight Jupyter notebooks and
has passed a notebook execution/consistency audit.

Phase I is **not yet marked FROZEN** because repository integration of the notebook
course, final GitHub-facing documentation cleanup, and the final release audit remain.

## Validation status

- 42 tests passed
- 90% line coverage
- Biopython scientific reference-validation tests pass
- wheel build passes
- editable installation passes
- compileall passes
- basic example workflow passes
- GitHub Actions CI passes
- CI matrix covers Python 3.10, 3.11, 3.12, and 3.13
- Phase I Notebooks 01–08 execute successfully after the Pre-Freeze notebook audit

## Canonical Audit correction status

- A — empty translation product semantics: resolved
- B — nested serialization schema validation: resolved
- C — input validation consistency: resolved
- D — BioMini exception consistency: resolved
- E — package version single source of truth: resolved
- F — dependency source of truth: resolved

## Canonical policies established

- DNA and RNA sequences must be non-empty.
- Protein may be empty when representing a valid computational translation product.
- An empty Protein has molecular weight `0.0` and fraction-based analyzer outputs of `0.0`.
- Every serializable BioMini object validates its schema version during restoration.
- `FeatureSet`, `Sample`, `Dataset`, `DomainEntity`, and provenance inputs use explicit validation.
- FASTA-format errors and dataset-operation errors use BioMini-specific exception classes.
- `biomini/_version.py` is the authoritative package-version source.
- `pyproject.toml` is the authoritative dependency specification.
- Educational notebooks explain the architecture, but `biomini/` remains the canonical source implementation.

## Educational material status

Completed and audited:

```text
01_classes_to_biological_objects.ipynb
02_sequence_abstraction.ipynb
03_biological_transformations.ipynb
04_domain_and_analysis.ipynb
05_feature_engineering.ipynb
06_dataset_and_machine_learning.ipynb
07_persistence_provenance_reproducibility.ipynb
08_validation_packaging_scientific_software.ipynb
```

The notebook course is designed as a self-contained teaching sequence and should be
published under `notebooks/` in the same repository.

## GitHub publication status

Completed:

- public repository created: `hk-yoon/biomini`
- CI badge and GitHub Actions workflow
- public README
- architecture documentation
- design-decision documentation
- scientific-validation documentation
- roadmap
- changelog
- contribution guidance
- security note
- `.gitignore`
- pull-request template
- GitHub Actions CI confirmed on hosted runners

## Remaining before Phase I freeze

1. update stale GitHub-facing status/documentation
2. add `notebooks/README.md`
3. add audited Phase I Notebooks 01–08 to `notebooks/`
4. run final full repository audit after notebook integration
5. tag/release `v0.1.0-phase1`
6. mark Phase I as **FROZEN**

## Next development phase after freeze

Phase II — Scientific AI

- Step 16: sequence representations
- Step 17: PyTorch / deep learning
- Step 18: biological foundation-model embeddings

No Phase II implementation should replace the Phase I architecture. It should extend it.
