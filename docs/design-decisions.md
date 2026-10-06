# BioMini Phase I — Design Decisions

This document records important decisions that should not be silently reversed in later
phases.

## DD-01 — Introduce `SequenceMolecule`

**Decision:** represent DNA, RNA, and Protein through a shared sequence abstraction.

**Why:** they differ biologically but share a computational structure: an ordered sequence
of symbols.

**Trade-off:** BioMini intentionally models only a subset of biological complexity.

## DD-02 — Separate domain objects from analyzers

**Decision:** use objects such as `ProteinAnalyzer` rather than continuously adding
analysis methods to `Protein`.

**Why:** biological identity and analytical computation evolve at different rates.

**Result:** BioMini uses a has-a relationship:

```text
ProteinAnalyzer has a Protein
```

rather than inheriting analysis from domain objects.

## DD-03 — Separate biological objects from ML representations

**Decision:** introduce `FeatureSet`, `Sample`, and `Dataset`.

**Why:** a protein sequence is not itself a machine-learning feature vector.

This boundary allows multiple representations of the same biological entity later.

## DD-04 — Preserve model context with `ModelArtifact`

**Decision:** do not persist a trained model alone.

A model artifact also stores:

- feature-column order
- model name
- target name
- metadata
- schema version

**Why:** inference reproducibility requires more than estimator parameters.

## DD-05 — Add stable identity and provenance

**Decision:** introduce `DomainEntity` and `Provenance`.

**Why:** scientific workflows create derived objects. Their lineage should remain
traceable.

## DD-06 — Keep empty DNA/RNA invalid, but allow an empty Protein result

**Decision:** DNA and RNA remain non-empty; `Protein("")` is allowed.

**Why:** translation of a stop-only RNA or an RNA shorter than one codon can validly
produce no amino-acid residues.

For an empty Protein:

- molecular weight = `0.0`
- hydrophobic fraction = `0.0`
- amino-acid fractions = `0.0`

## DD-07 — Validate nested serialization schemas

**Decision:** every serializable object validates its own schema version during restore.

**Why:** validating only the top-level object could silently accept incompatible nested
representations.

## DD-08 — Use BioMini-specific exceptions at framework boundaries

Current hierarchy:

```text
BioMiniError
├── ValidationError
├── SerializationError
├── ModelPersistenceError
├── FastaFormatError
└── DataError
```

**Why:** callers should be able to distinguish domain/data/persistence failures from
unrelated Python errors.

## DD-09 — Use Biopython as a scientific reference, not as a competitor

**Decision:** directly implement selected simple operations for teaching, but compare
results with Biopython.

**Long-term direction:** Biopython can become a backend for mature functionality where
reimplementation provides little educational value.

## DD-10 — `pyproject.toml` is dependency authority

Runtime dependencies:

- pandas
- scikit-learn
- joblib

Optional validation dependency:

- Biopython

Development dependencies:

- pytest
- pytest-cov

Legacy `requirements.txt` duplication is intentionally avoided.

## DD-11 — `_version.py` is the package-version source of truth

`pyproject.toml` obtains the version dynamically.

This prevents version drift between source code and package metadata.

## DD-12 — Keep one repository across Phase I–III

Framework source remains cumulative.

Phases are separated by release/tag and by educational documentation rather than by
duplicating repositories.

Expected release progression:

```text
v0.1.x  Phase I
v0.2.x  Phase II
v0.3.x  Phase III
```
