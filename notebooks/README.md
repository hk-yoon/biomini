# BioMini Phase I Notebooks

## Purpose

This directory contains the learner-facing course for **BioMini Phase I — Core Scientific
Software Foundation**.

The course starts with a small Python class and develops it step by step into a compact
scientific-software architecture connecting biological domain objects, analysis, feature
engineering, machine learning, reproducibility, scientific validation, packaging, and CI.

The notebooks are designed to be usable as:

- instructor-led classroom material;
- guided self-study material;
- a bridge from Python/OOP to scientific software design;
- preparation for BioMini Phase II — Scientific AI.

---

## Audience

The course assumes basic Python familiarity:

- variables and functions
- classes
- lists and dictionaries
- loops and comprehensions
- basic exception handling

Prior bioinformatics software experience is not required.

The biological examples use DNA, RNA, Protein, transcription, translation, sequence
analysis, and basic protein descriptors. The emphasis is software architecture rather
than advanced molecular biology.

---

## Prerequisites

Recommended Python:

```text
Python 3.10+
```

From the repository root, install BioMini with development and validation dependencies:

```bash
python -m pip install -e ".[dev,validation]"
```

The notebooks use the standard BioMini runtime dependencies:

```text
pandas
scikit-learn
joblib
```

and selected validation examples use:

```text
Biopython
```

A Jupyter environment is also required, for example Jupyter Notebook, JupyterLab,
VS Code notebooks, or another compatible `.ipynb` environment.

---

## Recommended Learning Order

### Notebook 01 — From Python Classes to Biological Objects

File:

```text
01_classes_to_biological_objects.ipynb
```

Focus:

```text
simple class
→ validation
→ inheritance
→ biological object
→ design limitations
```

Main question:

> How does a simple Python class become a biological domain object?

---

### Notebook 02 — Inheritance and Sequence Abstraction

File:

```text
02_sequence_abstraction.ipynb
```

Focus:

```text
DNA / RNA / Protein duplication
→ SequenceMolecule
→ NucleicAcid
→ alphabet validation
```

Main question:

> What computational responsibility is shared by biological sequences?

---

### Notebook 03 — DNA, RNA, Protein and Biological Transformations

File:

```text
03_biological_transformations.ipynb
```

Focus:

```text
complement
reverse complement
transcription
translation
stop codon
incomplete codon
empty translation product
```

Main question:

> How can biological transformations be modeled as domain-object behavior rather than
> isolated string manipulation?

---

### Notebook 04 — Separating Domain Objects and Analysis

File:

```text
04_domain_and_analysis.ipynb
```

Focus:

```text
fat domain class
→ separation of concerns
→ SequenceAnalyzer
→ NucleicAcidAnalyzer
→ ProteinAnalyzer
```

Main question:

> What belongs in a biological object, and what belongs in an analyzer?

---

### Notebook 05 — From Biology to Feature Engineering

File:

```text
05_feature_engineering.ipynb
```

Focus:

```text
Protein
→ ProteinAnalyzer
→ FeatureSet
→ Sample
→ Dataset
→ DataFrame / X / y
```

Main question:

> How is a biological object transformed into an ML-ready representation?

---

### Notebook 06 — Dataset and Machine Learning

File:

```text
06_dataset_and_machine_learning.ipynb
```

Focus:

```text
Dataset
→ StandardScaler
→ Ridge
→ Pipeline
→ ProteinPredictor
```

Main question:

> How can the biological/data architecture be connected to an actual ML model without
> putting ML behavior inside the domain object?

---

### Notebook 07 — Persistence, Provenance and Reproducibility

File:

```text
07_persistence_provenance_reproducibility.ipynb
```

Focus:

```text
serialization
schema version
stable ID
metadata
provenance
lineage
ModelArtifact
joblib
```

Main question:

> What must be preserved so a scientific result can be traced, restored, and reused?

---

### Notebook 08 — Validation, Packaging and Scientific Software

File:

```text
08_validation_packaging_scientific_software.ipynb
```

Focus:

```text
pytest
edge cases
Biopython reference validation
package structure
pyproject.toml
versioning
dependencies
CI
```

Main question:

> What turns working code into maintainable and scientifically validated software?

---

## Pedagogical Pattern

The notebooks intentionally do not begin by showing the complete production
implementation.

Most notebooks follow this progression:

```text
Introduction
        ↓
Learning Objectives
        ↓
Starting Point
        ↓
Concept
        ↓
Initial Design
        ↓
Problem / Limitation
        ↓
Design Decision
        ↓
Implementation
        ↓
Execution
        ↓
Validation
        ↓
Canonical BioMini Comparison
        ↓
What We Learned
        ↓
Exercises
        ↓
Bridge to Next Notebook
```

The course teaches **why the architecture evolved**, not merely what the final source
code looks like.

---

## Educational Code vs Canonical Source

This distinction is important.

### Notebook code

Notebook code is intentionally simplified or reconstructed so that the learner can see
the design evolve.

### Canonical implementation

The authoritative production implementation is:

```text
biomini/
```

If notebook code and package source ever diverge, the package source plus canonical
project documentation define the official implementation.

The notebooks should explain the canonical design, not become a second independent
source tree.

---

## Running the Notebooks

Recommended workflow:

```text
1. clone the repository
2. create / activate a Python environment
3. install BioMini in editable mode
4. open Notebook 01
5. run cells from top to bottom
6. complete exercises
7. continue sequentially through Notebook 08
```

Installation:

```bash
python -m pip install -e ".[dev,validation]"
```

Run the core test suite from the repository root:

```bash
python -m pytest
```

---

## Execution Audit Status

The Phase I notebook set has undergone a Pre-Freeze execution/consistency audit.

Current status:

```text
Notebook 01  PASS
Notebook 02  PASS
Notebook 03  PASS
Notebook 04  PASS
Notebook 05  PASS
Notebook 06  PASS
Notebook 07  PASS
Notebook 08  PASS
```

During the audit, Notebook 05 was corrected so the training `Dataset` is rebuilt after
the final `Dataset` class definition before `to_xy()` is used.

All notebook cells also include notebook cell IDs for current `nbformat` compatibility.

---

## Relationship to Phase I Source

The notebook course maps onto Phase I development approximately as follows:

| Notebook | Main Phase I Steps |
|---|---|
| 01 | Step 1 |
| 02 | Steps 2–3 |
| 03 | Step 4 |
| 04 | Steps 5–6 |
| 05 | Step 7 |
| 06 | Step 8 |
| 07 | Steps 12, 14 |
| 08 | Steps 9–11, 13–15 + Canonical Audit |

This ordering is pedagogical rather than chronological in every implementation detail.

---

## Scientific Scope

Phase I intentionally uses a compact semantic contract:

- canonical DNA alphabet only
- canonical RNA alphabet only
- canonical 20-amino-acid Protein alphabet
- coding-strand transcription assumption
- translation frame 0
- first-stop termination
- incomplete terminal codon ignored
- no ambiguous IUPAC symbols
- no ORF discovery
- no alternate genetic codes

The point is to make scientific assumptions explicit and testable.

---

## Scientific Reference Validation

BioMini compares selected behavior with Biopython.

This is used to distinguish:

```text
software regression testing
```

from:

```text
scientific reference validation
```

The comparison currently covers:

- reverse complement
- transcription
- translation
- protein molecular weight
- FASTA parsing

---

## After Notebook 08

Notebook 08 completes the Phase I learning arc.

The next development phase is **Phase II — Scientific AI**, which will extend the same
architecture with:

```text
k-mer
one-hot representation
tokenization
PyTorch
deep learning
biological foundation-model embeddings
```

The important design principle is that Phase II extends the Phase I architecture rather
than replacing it.
