# BioMini Phase I User Guide

**Release:** `v0.1.0-phase1`  
**Status:** **BioMini v0.1.0 — Phase I FROZEN**  
**Frozen commit:** `38a0486c435bb7d891f66d18bff54349edb06204`

BioMini Phase I is an educational scientific-software framework that begins with small
Python biological objects and develops them into a coherent architecture for biological
analysis, feature engineering, machine learning, persistence, provenance, scientific
validation, testing, and packaging.

This guide is for learners and instructors who want to **install, run, study, and validate**
the Phase I release without needing to read the maintainer/audit documents first.

---

# 한국어 요약

BioMini Phase I은 작은 Python 생물학 객체에서 출발하여 scientific software
architecture가 어떻게 발전하는지를 학습하기 위한 교육용 framework이다.

Phase I의 canonical release는 다음과 같다.

```text
Release: v0.1.0-phase1
Status : Phase I FROZEN
Commit : 38a0486c435bb7d891f66d18bff54349edb06204
```

학습자는 기본적으로 다음 순서로 사용하면 된다.

```text
repository clone
        ↓
Python environment 준비
        ↓
BioMini 설치
        ↓
Notebook 01 → 08 순서로 실행
        ↓
필요하면 pytest / Biopython validation 실행
```

`requirements.txt`는 필요하지 않다. BioMini는 `pyproject.toml`을 dependency의
single source of truth로 사용한다.

Jupyter 자체는 BioMini runtime dependency에 포함되어 있지 않으므로,
Jupyter Notebook, JupyterLab, 또는 VS Code Notebook 환경이 별도로 필요하다.

---

## 1. Who This Guide Is For

This guide is intended for:

- learners who know basic Python and want to study scientific software design;
- biology researchers who want to understand how biological objects connect to ML workflows;
- instructors using the eight Phase I notebooks as classroom material;
- developers preparing to continue into BioMini Phase II — Scientific AI.

You do **not** need prior BioMini experience.

Basic Python familiarity is recommended:

- variables and functions
- classes
- lists and dictionaries
- loops and comprehensions
- basic exception handling

---

## 2. What Phase I Contains

Phase I includes:

- `DNA`, `RNA`, `Protein`, `AminoAcid`
- `DomainEntity`, `Molecule`, `SequenceMolecule`, `NucleicAcid`
- complement / reverse complement
- transcription / translation
- Analyzer architecture
- sequence composition / motif search / GC content
- protein molecular weight / hydrophobic fraction
- `FeatureSet`, `Sample`, `Dataset`
- scikit-learn based `ProteinPredictor`
- FASTA read/write
- JSON serialization
- `ModelArtifact` persistence using `joblib`
- stable ID / metadata / provenance / lineage
- schema versioning
- BioMini exception hierarchy
- Biopython scientific reference validation
- pytest regression testing
- Python packaging and GitHub Actions CI
- eight educational Jupyter notebooks

Phase I is intentionally compact. It is not intended to replace Biopython or other mature
scientific libraries.

---

## 3. Recommended Installation Path

### 3.1 Clone the repository

```bash
git clone https://github.com/hk-yoon/biomini.git
cd biomini
```

To study the exact frozen Phase I release:

```bash
git checkout v0.1.0-phase1
```

You are then working with the exact Phase I milestone.

---

## 4. Python Environment

BioMini requires:

```text
Python 3.10+
```

The frozen Phase I release was validated on:

```text
Python 3.10
Python 3.11
Python 3.12
Python 3.13
```

### 4.1 Recommended for Anaconda / Miniconda users

Create a dedicated environment:

```bash
conda create -n biomini python=3.13
conda activate biomini
```

After activation, use:

```bash
python
```

from that environment.

Check:

```bash
python --version
```

and:

```bash
python -c "import sys; print(sys.executable)"
```

The interpreter path should point to the active conda environment.

### 4.2 Windows note

On some Windows systems, `python` may resolve to the Windows App Execution Alias instead
of the intended interpreter.

If you are using conda, the preferred solution is:

```bash
conda activate biomini
python --version
```

rather than relying on the Windows `py` launcher.

The `py` launcher is useful for system Python installations, but it is not a substitute
for activating the intended conda environment.

---

## 5. Install BioMini

From the repository root:

### Runtime only

```bash
python -m pip install -e .
```

This installs BioMini plus its runtime dependencies:

```text
pandas
scikit-learn
joblib
```

### Runtime + tests

```bash
python -m pip install -e ".[dev]"
```

Additional packages:

```text
pytest
pytest-cov
```

### Runtime + scientific reference validation

```bash
python -m pip install -e ".[validation]"
```

Additional package:

```text
Biopython
```

### Recommended full educational/development environment

```bash
python -m pip install -e ".[dev,validation]"
```

This is the recommended installation for the Phase I course.

---

## 6. Do I Need `requirements.txt`?

No.

BioMini intentionally uses:

```text
pyproject.toml
```

as the single dependency authority.

The project does **not** need a separate `requirements.txt` for the Phase I source release.

This avoids maintaining the same dependency information in two different places.

The dependency groups are defined in `pyproject.toml`:

```text
runtime
validation
dev
```

and are installed with standard package extras.

---

## 7. Jupyter Requirement

The eight Phase I notebooks are `.ipynb` files.

You therefore need a notebook-capable environment such as:

- Jupyter Notebook
- JupyterLab
- VS Code with Jupyter support
- another compatible `.ipynb` environment

Jupyter itself is **not** part of BioMini's frozen runtime dependency list.

If your Python environment does not already provide Jupyter, install it separately, for example:

```bash
python -m pip install jupyterlab
```

or use the Jupyter environment already provided by Anaconda / VS Code.

This is an execution environment requirement, not a BioMini scientific runtime dependency.

---

## 8. Recommended Learning Order

The learner-facing course is under:

```text
notebooks/
```

Study in this order:

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

The learning arc is:

```text
simple Python class
        ↓
biological domain object
        ↓
sequence abstraction
        ↓
biological transformation
        ↓
domain / analysis separation
        ↓
feature engineering
        ↓
dataset
        ↓
machine learning
        ↓
persistence
        ↓
provenance
        ↓
testing
        ↓
scientific reference validation
        ↓
packaging / CI
```

---

## 9. What Is Inside Each Notebook?

The notebooks are designed as teaching units, not merely code dumps.

Typical structure:

```text
Introduction
Learning Objectives
Concept Explanation
Starting Point
Problem / Limitation
Design Decision
Implementation
Execution
Validation
Canonical BioMini Comparison
What We Learned
Exercises
Bridge to the Next Notebook
```

The notebooks intentionally reconstruct or simplify some code so that learners can see
**why the architecture evolved**.

---

## 10. Notebook Code vs Canonical Source

This distinction is important.

### Educational notebook code

Notebook code is learner-facing and may be simplified or reconstructed for explanation.

### Canonical implementation

The authoritative Phase I implementation is:

```text
biomini/
```

If notebook code and package source ever appear to differ, the canonical package source
plus the frozen Phase I documentation define the official implementation.

The notebooks explain the architecture; they are not a second independent production source tree.

---

## 11. Quick Start Example

```python
from biomini import DNA, ProteinAnalyzer

dna = DNA(
    "gene",
    "ATGGCC",
)

protein = (
    dna
    .transcribe()
    .translate()
)

analyzer = ProteinAnalyzer(protein)

print(protein.sequence)
print(analyzer.molecular_weight())
```

Conceptually:

```text
DNA
 ↓ transcription
RNA
 ↓ translation
Protein
 ↓
ProteinAnalyzer
 ↓
scientific measurement / features
```

---

## 12. Core Biological Semantics

Phase I intentionally uses a compact semantic contract.

### DNA

```text
alphabet: A/T/G/C
must be non-empty
```

### RNA

```text
alphabet: A/U/G/C
must be non-empty
```

### Protein

```text
canonical 20 amino acids
may be empty when produced by a valid computational translation
```

### Transcription

Stored DNA is treated as the coding strand.

### Translation

```text
frame 0
stop at first stop codon
ignore incomplete terminal codon
```

Phase I does not support:

```text
ambiguous IUPAC symbols
ORF discovery
alternate genetic codes
rich sequence annotation
```

These are explicit scope choices rather than bugs.

---

## 13. Analysis Architecture

BioMini separates biological objects from analysis logic.

```text
DNA       → DNAAnalyzer
RNA       → RNAAnalyzer
Protein   → ProteinAnalyzer
```

The design is:

```text
ProteinAnalyzer has-a Protein
```

rather than:

```text
ProteinAnalyzer is-a Protein
```

This is one of the central software-design lessons of Phase I.

---

## 14. From Biology to Machine Learning

The main Phase I ML path is:

```text
Biological Object
        ↓
Analyzer
        ↓
FeatureSet
        ↓
Sample
        ↓
Dataset
        ↓
scikit-learn model
        ↓
ProteinPredictor
```

The biological object is intentionally kept separate from its numerical ML representation.

---

## 15. Persistence and Reproducibility

BioMini supports:

```text
stable ID
metadata
provenance
lineage
schema version
```

and trained-model persistence via:

```text
ModelArtifact
```

using `joblib`.

### Security warning

`joblib` is pickle-based.

Only load model artifacts from trusted sources.

---

## 16. Run the Test Suite

From the repository root:

```bash
python -m pytest
```

Expected frozen Phase I baseline:

```text
42 passed
```

Run coverage:

```bash
python -m pytest --cov=biomini --cov-report=term-missing
```

Expected baseline:

```text
90% line coverage
```

---

## 17. Scientific Reference Validation

BioMini distinguishes:

```text
software regression testing
```

from:

```text
scientific reference validation
```

Selected Phase I behaviors are cross-checked against Biopython:

- reverse complement
- transcription
- translation
- protein molecular weight
- FASTA parsing

The purpose is not to compete with Biopython, but to validate the scientific behavior of
the educational implementation against an established reference.

---

## 18. Frozen Validation Baseline

The Phase I frozen release was validated as follows:

```text
pytest                    42 passed
line coverage             90%
compileall                PASS
wheel build               PASS
editable install          PASS
basic example             PASS
Biopython validation      PASS
Notebook 01–08 execution  PASS
GitHub Actions CI         PASS
Python 3.10–3.13          PASS
```

---

## 19. Repository Map for Learners

Important locations:

```text
biomini/
├── biomini/                    # canonical package source
├── notebooks/                  # learner-facing Phase I course
├── tests/                      # regression/reference tests
├── docs/                       # architecture and design documentation
├── examples/                   # runnable examples
├── data/                       # example/supporting data
├── pyproject.toml              # package metadata and dependencies
├── README.md                   # project overview
├── PHASE_I_COMPLETION_REPORT.md
├── CANONICAL_STATUS.md
└── RELEASE_NOTES_v0.1.0-phase1.md
```

For most learners, the recommended entry points are:

```text
README.md
        ↓
this USER GUIDE
        ↓
notebooks/README.md
        ↓
Notebook 01 → 08
```

---

## 20. Recommended Student Workflow

A simple student workflow is:

```bash
git clone https://github.com/hk-yoon/biomini.git
cd biomini
git checkout v0.1.0-phase1
```

Activate or create a Python environment.

Then:

```bash
python -m pip install -e ".[dev,validation]"
```

Open:

```text
notebooks/01_classes_to_biological_objects.ipynb
```

and continue sequentially through Notebook 08.

After completing the notebooks, run:

```bash
python -m pytest
```

to verify the canonical package.

---

## 21. For Instructors

A useful teaching pattern is:

```text
Notebook explanation
        ↓
run the notebook
        ↓
inspect canonical source
        ↓
run regression tests
        ↓
compare with Biopython where applicable
        ↓
discuss the architectural design decision
```

The notebooks are designed to explain the evolution of the framework rather than only
present the final implementation.

---

## 22. What Comes After Phase I?

Phase II extends the same architecture into Scientific AI.

Planned direction:

```text
Step 16  Sequence Representations
         ├── k-mer
         ├── one-hot encoding
         └── tokenization

Step 17  PyTorch / Deep Learning

Step 18  Biological Foundation-Model Embeddings
```

The Phase I architecture remains preserved at:

```text
v0.1.0-phase1
```

Phase II should extend it rather than replace it.

---

## 23. Canonical Phase I Reference

For exact reproducibility:

```text
Repository:
https://github.com/hk-yoon/biomini

Tag:
v0.1.0-phase1

Frozen commit:
38a0486c435bb7d891f66d18bff54349edb06204
```

Use the tag rather than `main` whenever you need the exact Phase I frozen state.
