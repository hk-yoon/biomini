# BioMini

[![CI](https://github.com/hk-yoon/biomini/actions/workflows/ci.yml/badge.svg)](https://github.com/hk-yoon/biomini/actions/workflows/ci.yml)

**From Python Biological Objects to Scientific AI and Self-Driving Labs**

BioMini is an educational scientific-software project that starts with small Python
classes representing biological objects and develops them step by step into a coherent
architecture for scientific analysis, machine learning, reproducibility, Scientific AI,
and ultimately Self-Driving Lab (SDL) systems.

> Current milestone: **BioMini v0.1.0 — Phase I FROZEN**

Phase I core implementation and the eight-part educational notebook course are complete.
Repository integration, local validation, notebook execution audit, final release audit,
and release-status finalization are complete. This commit is the intended frozen Phase I
release state; after confirmation CI, it will be tagged as `v0.1.0-phase1`.

---

# 한국어 요약

> 현재 상태: **BioMini v0.1.0 — Phase I FROZEN**

Phase I의 구현, 8개 교육용 Notebook, repository 통합, local validation,
Biopython reference validation, Python 3.10–3.13 GitHub Actions CI,
그리고 final release audit까지 모두 완료되었다.

이 commit은 Phase I의 최종 frozen release 상태이며, confirmation CI가 통과하면
동일한 commit에 `v0.1.0-phase1` tag/release를 생성한다.

## BioMini란?

BioMini는 `Molecule`, `Protein`, `AminoAcid` 같은 작은 Python OOP 예제에서
출발하여 이를 단계적으로 확장하면서 **scientific software가 어떻게 설계되고
Scientific AI 및 Self-Driving Lab으로 이어질 수 있는지** 학습하기 위한
교육용 mini-framework입니다.

BioMini의 핵심 질문은 다음과 같습니다.

> 작은 Python class가 어떻게 biological domain model이 되고,  
> scientific analysis와 machine learning을 거쳐,  
> reproducible scientific software와 Scientific AI/SDL architecture로 발전하는가?

BioMini는 Biopython, RDKit, scikit-learn, PyTorch 같은 established library를
대체하려는 프로젝트가 아닙니다. 오히려 그런 도구들을 **일관된 scientific
software architecture 안에서 이해하고 연결하는 방법**을 학습하는 것이 목적입니다.

---

## Current Phase I Scope

Phase I — **Core Scientific Software Foundation** includes:

- biological domain objects: `DNA`, `RNA`, `Protein`, `AminoAcid`
- abstractions: `DomainEntity`, `Molecule`, `SequenceMolecule`, `NucleicAcid`
- complement / reverse complement
- transcription / translation
- Analyzer architecture
- sequence composition / motif search / GC content
- protein molecular weight / hydrophobic fraction
- `FeatureSet`, `Sample`, `Dataset`
- scikit-learn based ML workflow
- `ProteinPredictor`
- FASTA read/write
- JSON serialization
- `ModelArtifact` persistence with `joblib`
- stable ID / metadata / provenance / lineage
- schema versioning
- BioMini-specific exception hierarchy
- Biopython scientific reference validation
- pytest regression testing
- packaging / version management
- GitHub Actions CI

Current validation baseline:

```text
pytest                    42 passed
line coverage             90%
compileall                PASS
wheel build               PASS
editable install          PASS
basic example             PASS
Biopython validation      PASS
GitHub Actions CI         PASS
Python 3.10–3.13          PASS
```

---

## Educational Narrative

Phase I is taught as an evolution of one small project:

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

The objective is not merely to show the final code. The course emphasizes **why the
architecture changed at each step**.

---

## Phase I Notebook Course

The Phase I course consists of eight self-contained notebooks:

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

Each notebook includes:

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

See [`notebooks/README.md`](notebooks/README.md) for the learning order and execution guide.

---

## Installation

Python 3.10 or later is required.

Basic installation for development:

```bash
python -m pip install -e .
```

Development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Scientific reference-validation dependencies:

```bash
python -m pip install -e ".[validation]"
```

Recommended full development environment:

```bash
python -m pip install -e ".[dev,validation]"
```

Run the test suite:

```bash
python -m pytest
```

Run with coverage:

```bash
python -m pytest --cov=biomini --cov-report=term-missing
```

---

## Quick Example

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

analyzer = ProteinAnalyzer(
    protein
)

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

## Architecture

### Domain

```text
DomainEntity
  └── Molecule
       └── SequenceMolecule
            ├── NucleicAcid
            │    ├── DNA
            │    └── RNA
            └── Protein

Provenance
AminoAcid
```

### Analysis

```text
SequenceAnalyzer
├── NucleicAcidAnalyzer
│   ├── DNAAnalyzer
│   └── RNAAnalyzer
└── ProteinAnalyzer
```

The relationship is intentionally:

```text
ProteinAnalyzer has-a Protein
```

rather than:

```text
ProteinAnalyzer is-a Protein
```

### Representation / Data / Model

```text
Protein
 ↓
ProteinAnalyzer
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

### Persistence / Reproducibility

```text
Domain Object
 ├── stable ID
 ├── metadata
 └── provenance

ModelArtifact
 ├── trained model
 ├── feature columns
 ├── model name
 ├── target name
 ├── metadata
 └── schema version
```

---

## Phase I Scientific Semantic Contract

Phase I intentionally uses a compact biological scope:

- DNA alphabet: `A/T/G/C`
- RNA alphabet: `A/U/G/C`
- Protein alphabet: canonical 20 amino acids
- DNA and RNA must be non-empty
- Protein may be empty when it represents a valid computational translation product
- stored DNA is treated as the coding strand for transcription
- translation uses frame 0
- translation stops at the first stop codon
- incomplete terminal codons are ignored
- ambiguous IUPAC symbols are not supported
- ORF search is not supported
- alternate genetic codes are not supported
- protein molecular weight uses average residue masses aligned with the selected Biopython reference

These are explicit Phase I scope decisions, not claims of complete biological modeling.

---

## Scientific Validation

Software tests ask:

> Does the code behave as designed?

Scientific reference validation asks:

> Does the selected scientific behavior agree with an independent established implementation?

BioMini uses Biopython as a reference for:

- reverse complement
- transcription
- translation
- protein molecular weight
- FASTA parsing

This distinction is central to the educational purpose of Phase I.

---

## Repository Structure

```text
biomini/
├── biomini/
├── tests/
├── docs/
├── notebooks/
├── examples/
├── data/
├── .github/
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

Important project documents:

- [`PHASE_I_COMPLETION_REPORT.md`](PHASE_I_COMPLETION_REPORT.md) — canonical Phase I development record
- [`CANONICAL_STATUS.md`](CANONICAL_STATUS.md) — current milestone/status
- [`docs/architecture.md`](docs/architecture.md) — architecture
- [`docs/design-decisions.md`](docs/design-decisions.md) — design decisions
- [`docs/scientific-validation.md`](docs/scientific-validation.md) — validation strategy
- [`docs/roadmap.md`](docs/roadmap.md) — Phase II/III roadmap

---

## Security

BioMini uses `joblib` for model persistence. `joblib` is pickle-based.

**Only load model artifacts from trusted sources.**

See [`SECURITY.md`](SECURITY.md).

---

## Roadmap

```text
Phase I
Core Scientific Software
        ↓
Phase II
Scientific AI
        ↓
Phase III
Self-Driving Lab
```

### Phase II — Scientific AI

Planned topics:

- k-mer representation
- one-hot encoding
- tokenization
- PyTorch / deep learning
- biological foundation-model embeddings
- DNABERT-family examples
- ESM-family examples
- ProtT5-family examples

### Phase III — Self-Driving Lab

Planned topics:

- experiment domain model
- parameter/search-space abstraction
- Bayesian optimization / active learning
- Virtual Lab
- instrument abstraction
- SDL orchestration

See [`docs/roadmap.md`](docs/roadmap.md).

---

## Current Status

Phase I source implementation, educational notebooks, repository integration,
post-integration validation, final release audit, and freeze-status finalization are complete.

Release sequence for this frozen commit:

```text
Phase I FROZEN release commit
        ↓
GitHub Actions CI confirmation
        ↓
tag / release: v0.1.0-phase1
```

Phase II development begins only after the Phase I tag/release is created.

---

## License

MIT License. See [`LICENSE`](LICENSE).
