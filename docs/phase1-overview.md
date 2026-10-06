# Phase I Overview

Phase I is the **Core Scientific Software Foundation** of BioMini.

Its educational narrative is:

```text
simple Python class
        ↓
inheritance and abstraction
        ↓
biological transformations
        ↓
separation of domain and analysis
        ↓
feature engineering
        ↓
machine learning
        ↓
persistence and provenance
        ↓
scientific validation
        ↓
package engineering
```

## Current status

Phase I core implementation is complete and the eight-notebook Phase I educational
course has been completed and execution-audited.

Current milestone:

> **BioMini v0.1.0 — Phase I Pre-Freeze**

Repository integration, documentation cleanup, post-integration validation, and the
final release audit are complete. The remaining work is the final **FROZEN** status commit,
confirmation CI, and the `v0.1.0-phase1` tag/release.

## Phase I notebook course

```text
01 From Python Classes to Biological Objects
02 Inheritance and Sequence Abstraction
03 DNA, RNA, Protein and Biological Transformations
04 Separating Domain Objects and Analysis
05 From Biology to Feature Engineering
06 Dataset and Machine Learning
07 Persistence, Provenance and Reproducibility
08 Validation, Packaging and Scientific Software
```

The notebooks are the primary learner-facing teaching material.

The canonical implementation remains the source under `biomini/`.

For the detailed learning guide, see:

[`../notebooks/README.md`](../notebooks/README.md)

For the complete canonical development record, see:

[`../PHASE_I_COMPLETION_REPORT.md`](../PHASE_I_COMPLETION_REPORT.md)

The Completion Report is a maintainer/reference document rather than the primary
student textbook.
