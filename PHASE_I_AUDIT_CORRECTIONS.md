# BioMini Phase I Canonical Audit — A–F Correction Report

## Status

All canonical-audit correction items A–F have been implemented and tested.

The A–F correction pass was completed before the current **Phase I Pre-Freeze** finalization stage.

## A. Empty translation product semantics — RESOLVED

Problem:
`RNA("UAA").translate()` and sequences shorter than one full codon could produce an empty
translation result, but `SequenceMolecule` rejected all empty sequences.

Resolution:
- `DNA` and `RNA` remain non-empty.
- `Protein` explicitly permits an empty sequence as a computational translation product.
- Empty-protein molecular weight is defined as `0.0`.
- Empty-protein hydrophobic fraction is `0.0`.
- All amino-acid fraction features are `0.0`.
- stop-only and short-RNA cases are regression tested, including Biopython comparison.

## B. Nested serialization schema validation — RESOLVED

Problem:
Only top-level JSON schema versions were checked.

Resolution:
- introduced shared `validate_schema_version()`.
- `Molecule`, `SequenceMolecule`, `FeatureSet`, `Sample`, and `Dataset` validate their
  own serialized schema during `from_dict()`.
- nested incompatible FeatureSet/Sample payloads are rejected with `SerializationError`.

## C. Input-validation consistency — RESOLVED

Resolution:
- explicit validation for manual `entity_id`.
- metadata/provenance type checks.
- provenance parent-id validation.
- `FeatureSet` requires a non-empty name and non-empty numeric finite feature dictionary.
- `Sample` requires a `FeatureSet`.
- `Dataset.add()` requires a `Sample`.

## D. Exception-hierarchy consistency — RESOLVED

Added:
- `FastaFormatError`
- `DataError`

Malformed FASTA content now raises `FastaFormatError`.
Dataset operations that cannot produce X/y raise `DataError`.
Invalid write parameters remain `ValidationError`.

## E. Duplicate version source — RESOLVED

`biomini/_version.py` is now the single source of truth.

`pyproject.toml` uses setuptools dynamic version lookup:

`version = {attr = "biomini._version.__version__"}`

Wheel and editable-install tests confirm version `0.1.0`.

## F. Dependency duplication — RESOLVED

Removed legacy `requirements.txt`.

`pyproject.toml` is authoritative:
- runtime: pandas, scikit-learn, joblib
- optional validation: Biopython
- optional dev: pytest, pytest-cov

## Verification

After all A–F corrections:

- pytest: 42 passed
- coverage: 90%
- compileall: passed
- wheel build: passed
- editable install: passed
- basic example: passed
- Biopython scientific reference validation: passed

The remaining Biopython warning concerns deliberately tested incomplete terminal codons.

## Remaining release work

A–F are no longer Phase I freeze blockers.

The A–F correction items are historical and no longer Phase I freeze blockers.

Subsequent work completed:
- Phase I Completion Report
- public GitHub repository and hosted CI
- Phase I educational Notebooks 01–08
- notebook execution/consistency audit

Current remaining work:
- integrate the audited notebooks and updated GitHub-facing documentation
- confirm hosted CI after integration
- final release audit
- final Phase I freeze/tag
