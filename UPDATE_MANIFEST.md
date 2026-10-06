# BioMini GitHub Pre-Freeze Integration Package

This package contains the files prepared for the Phase I repository integration.

## Replace / update

- README.md
- CANONICAL_STATUS.md
- GITHUB_PREP_STATUS.md
- CHANGELOG.md
- CONTRIBUTING.md
- SECURITY.md
- PHASE_I_COMPLETION_REPORT.md
- PHASE_I_AUDIT_CORRECTIONS.md
- docs/phase1-overview.md
- docs/roadmap.md
- docs/scientific-validation.md

## Add

- PHASE_I_VALIDATION.txt
- PHASE_I_LOCAL_INTEGRATION_AUDIT.md
- PHASE_I_PREFREEZE_AUDIT_REPORT.md
- notebooks/README.md
- notebooks/01–08 audited Phase I notebooks

## Remove from the repository

- RC1_VALIDATION.txt

It is superseded by `PHASE_I_VALIDATION.txt`.

## Verified local integration baseline

```text
pytest                    42 passed
line coverage             90%
compileall                PASS
editable install          PASS
wheel build               PASS
basic example             PASS
Biopython validation      PASS
Notebook 01–08 execution  PASS
```

The remaining external gate is GitHub-hosted CI after these changes are committed and
pushed to `main`.
