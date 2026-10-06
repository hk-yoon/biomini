# Changelog

All notable BioMini changes will be documented here.

The project is currently preparing its first public Phase I release.

## [0.1.0] — Phase I Release Candidate

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
- GitHub CI configuration
- Phase I architecture, design, validation, and roadmap documentation

### Changed

- protein molecular-weight residue values aligned with the selected Biopython reference
- FASTA headers separate identifier and description
- nested serialized objects validate schema versions
- dependency metadata consolidated into `pyproject.toml`
- package version consolidated into `biomini/_version.py`

### Fixed

- translation of stop-only or shorter-than-one-codon RNA can yield a valid empty Protein
- empty Protein analyzer operations now have explicit zero-valued semantics
- framework-boundary errors now use BioMini-specific exception classes

### Security

- documented that `joblib` artifacts must only be loaded from trusted sources

### Status

This version remains a release candidate until educational materials and the final Phase I
release audit are complete.
