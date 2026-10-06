# BioMini

**From Python biological objects to Scientific AI and Self-Driving Labs.**

BioMini is a compact educational Python framework for learning how biological domain
objects, scientific analysis, feature engineering, machine learning, reproducibility,
and laboratory automation can be connected in one coherent software architecture.

> Current release candidate: **BioMini v0.1.0 — Phase I: Core Scientific Software Foundation**

BioMini is not intended to replace Biopython, RDKit, scikit-learn, PyTorch, or production
laboratory-control systems. It is designed to make the architecture connecting those
types of tools visible, inspectable, and teachable.

## Why BioMini?

Many educational examples stop at isolated functions or notebooks. BioMini instead asks:

> How does a small Python class evolve into maintainable scientific software, and later
> into Scientific AI and a Self-Driving Lab workflow?

Phase I develops that foundation step by step:

```text
Biological Objects
        ↓
Scientific Analysis
        ↓
Feature Engineering
        ↓
Dataset
        ↓
Machine Learning
        ↓
Persistence / Provenance
        ↓
Scientific Validation
        ↓
Installable Python Package
```

## Current scope — Phase I

Implemented:

- biological domain objects: `DNA`, `RNA`, `Protein`, `AminoAcid`
- sequence abstraction and validation
- complement, reverse complement, transcription, translation
- analyzer architecture
- GC content, composition, motif search, protein descriptors
- `FeatureSet`, `Sample`, `Dataset`
- scikit-learn prediction workflow
- FASTA read/write
- JSON serialization
- `ModelArtifact` persistence with `joblib`
- stable entity IDs, metadata, provenance, lineage
- BioMini-specific exception hierarchy
- scientific cross-validation against Biopython
- pytest regression testing
- package build and editable installation

## Quick start

```python
from biomini import DNA, ProteinAnalyzer

dna = DNA("gene1", "ATGGCCTTT")

rna = dna.transcribe()
protein = rna.translate()

analyzer = ProteinAnalyzer(protein)

print(dna)
print(rna)
print(protein)
print(analyzer.molecular_weight())
```

## Installation

For development:

```bash
python -m pip install -e ".[dev,validation]"
```

Run the test suite:

```bash
python -m pytest
```

Run coverage:

```bash
python -m pytest --cov=biomini --cov-report=term-missing
```

## Phase I validation status

At the current RC1 milestone:

```text
43 tests passed
90% line coverage
wheel build               PASS
editable installation     PASS
compileall                PASS
example workflow          PASS
Biopython cross-validation PASS
```

Scientific reference-validation currently covers:

- reverse complement
- transcription
- translation
- protein molecular weight
- FASTA parsing

See [Scientific Validation](docs/scientific-validation.md).

## Architecture

```text
Domain
├── DomainEntity
├── Molecule
├── SequenceMolecule
├── DNA / RNA / Protein
└── Provenance

Analysis
├── SequenceAnalyzer
├── DNAAnalyzer / RNAAnalyzer
└── ProteinAnalyzer

ML Representation
├── FeatureSet
├── Sample
└── Dataset

Model / Persistence
├── ProteinPredictor
└── ModelArtifact

I/O
└── FASTA
```

See [Architecture](docs/architecture.md) and
[Design Decisions](docs/design-decisions.md).

## Biological semantics in Phase I

Phase I intentionally keeps biology simple and explicit:

- DNA alphabet: `A/T/G/C`
- RNA alphabet: `A/U/G/C`
- protein alphabet: canonical 20 amino acids
- DNA and RNA must be non-empty
- an empty `Protein` is allowed as a valid computational translation result
- stored DNA is treated as the coding strand during transcription
- translation uses frame 0 and stops at the first stop codon
- incomplete terminal codons are ignored
- ambiguous IUPAC symbols, ORF search, alternate genetic codes, and rich annotations
  are outside Phase I scope

These are educational scope decisions, not claims about the full complexity of biology.

## Relationship to Biopython

BioMini and Biopython are complementary.

```text
Biopython
= mature bioinformatics implementation

BioMini
= educational scientific-software architecture
```

BioMini directly implements selected operations for transparency and teaching, then
cross-validates them against Biopython. In later stages, established scientific libraries
may be used as interchangeable backends rather than reimplemented.

## Roadmap

```text
v0.1.x — Phase I
Core Scientific Software Foundation

v0.2.x — Phase II
Scientific AI
  Step 16: sequence representations
  Step 17: PyTorch / deep learning
  Step 18: biological foundation-model embeddings

v0.3.x — Phase III
Self-Driving Lab
  Step 19: experiment domain model
  Step 20: optimizer / active learning
  Step 21: virtual lab
  Step 22: instrument abstraction
  Step 23: SDL orchestration
```

See the full [Roadmap](docs/roadmap.md).

## Repository guide

```text
biomini/                 package source
tests/                   regression and scientific validation tests
examples/                runnable examples
data/                    small educational data
docs/                    architecture and project documentation
.github/workflows/       CI
PHASE_I_COMPLETION_REPORT.md
                         canonical Phase I master report
CANONICAL_STATUS.md      current project state
CHANGELOG.md             release history
```

## Educational use

The final educational material will be organized separately from the framework source.
Phase I is intended to become a sequence of Jupyter notebooks showing the evolution:

```text
simple class
   ↓
abstraction
   ↓
separation of concerns
   ↓
feature engineering
   ↓
machine learning
   ↓
reproducibility
   ↓
scientific validation
   ↓
packaging
```

The canonical framework remains cumulative; educational notebooks may show earlier
intermediate designs to explain why refactoring was necessary.

## Security note

Model artifacts are persisted with `joblib`, which is pickle-based.

**Load model artifacts only from trusted sources.**

See [SECURITY.md](SECURITY.md).

## Project status

Phase I source implementation and Canonical Audit corrections A–F are complete.
The repository is currently a **release candidate**, not yet marked `Phase I FROZEN`.

Remaining before the Phase I final release:

- educational notebooks/course material
- final release audit
- final `v0.1.0-phase1` tag/release

## License

MIT License.
