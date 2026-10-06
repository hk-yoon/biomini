# Changelog

All notable BioMini changes will be documented here.

The project is currently preparing its first public Phase I final release.

## [0.1.0] — Phase I Pre-Freeze

### Added

- biological domain hierarchy for DNA, RNA, Protein, and amino acids
- `DomainEntity` identity and metadata foundation
- provenance and lineage tracking
- sequence analyzers
- GC content, motif, composition, hydrophobic fraction, molecular weight
- `FeatureSet`, `Sample`, and `Dataset`
- scikit-learn predictor workflow
- FASTA read/write support
- JSON serialization with schema versioning
- `ModelArtifact` persistence using `joblib`
- BioMini exception hierarchy
- Biopython cross-validation tests
- pytest regression suite
- package metadata and editable installation
- GitHub Actions CI configuration
- Phase I architecture, design, validation, and roadmap documentation
- eight-part Phase I educational notebook course

### Changed

- protein molecular-weight residue values aligned with the selected Biopython reference
- FASTA headers separate identifier and description
- nested serialized objects validate schema versions
- dependency metadata consolidated into `pyproject.toml`
- package version consolidated into `biomini/_version.py`
- project status wording changed from RC1 to **Phase I Pre-Freeze** during finalization
- Notebook 05 corrected after execution audit so `Dataset.to_xy()` is used on an instance
  created from the final `Dataset` class definition
- notebook cells normalized with cell IDs for current `nbformat` compatibility

### Fixed

- translation of stop-only or shorter-than-one-codon RNA can yield a valid empty Protein
- empty Protein analyzer operations now have explicit zero-valued semantics
- framework-boundary errors now use BioMini-specific exception classes

### Validation

Current Phase I baseline:

```text
42 tests passed
90% line coverage
compileall PASS
wheel build PASS
editable install PASS
basic example PASS
Biopython reference validation PASS
GitHub Actions CI PASS
Python 3.10–3.13 PASS
Notebook 01–08 execution PASS
```

### Security

- documented that `joblib` artifacts must only be loaded from trusted sources

### Status

This version remains **Pre-Freeze** until the notebook course is integrated into the
repository, GitHub-facing documentation cleanup is complete, the final repository audit
passes, and tag/release `v0.1.0-phase1` is created.
