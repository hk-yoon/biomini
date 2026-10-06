# BioMini Canonical Status

## Current canonical milestone

**BioMini v0.1.0 — Phase I Release Candidate 1 (RC1)**

Phase I implementation Steps 1–15 are complete.
Canonical Audit corrections A–F are resolved and regression-tested.

This release is **not yet marked Phase I FROZEN** because GitHub release documentation,
educational materials, and the final release audit remain.

## Validation status

- 43 tests passed
- 90% line coverage
- Biopython scientific reference-validation tests pass
- wheel build passes
- editable installation passes
- compileall passes
- basic example workflow passes

## Audit correction status

- A — empty translation product semantics: resolved
- B — nested serialization schema validation: resolved
- C — input validation consistency: resolved
- D — BioMini exception consistency: resolved
- E — package version single source of truth: resolved
- F — dependency source of truth: resolved

## Canonical policies established

- DNA and RNA sequences must be non-empty.
- Protein may be empty when representing a valid computational translation product.
- An empty Protein has molecular weight 0.0 and fraction-based analyzer outputs of 0.0.
- Every serializable BioMini object validates its schema version during restoration.
- `FeatureSet`, `Sample`, `Dataset`, `DomainEntity`, and provenance inputs use explicit validation.
- FASTA-format errors and dataset-operation errors use BioMini-specific exception classes.
- `biomini/_version.py` is the authoritative package-version source.
- `pyproject.toml` is the authoritative dependency specification.

## Remaining before Phase I freeze

- finalize GitHub-facing documentation
- Phase I completion report: completed
- create educational notebooks/course material
- final release audit
- tag/release `v0.1.0-phase1`

## Next development phase after freeze

Phase II — Scientific AI

- Step 16: sequence representations
- Step 17: PyTorch / deep learning
- Step 18: biological foundation-model embeddings


## GitHub publication preparation

Completed for RC1:

- public repository README
- architecture documentation
- design-decision documentation
- scientific-validation documentation
- roadmap
- changelog
- contribution guidance
- security note
- `.gitignore`
- pull-request template
- GitHub Actions CI workflow

Repository URLs/contact details remain intentionally unset until the actual GitHub
repository is created.
