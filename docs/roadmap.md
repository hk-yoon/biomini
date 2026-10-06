# BioMini Roadmap

## Project direction

BioMini is developed as one cumulative framework with three educational phases.

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

## Phase I — Core Scientific Software

Target release: `v0.1.0-phase1`

Status: Release Candidate.

Completed:

- domain modeling
- sequence hierarchy
- biological transformations
- analyzer architecture
- feature/data abstraction
- conventional ML
- FASTA I/O
- persistence
- provenance
- scientific validation
- production hardening
- package installation/versioning

Remaining before final Phase I freeze:

- educational notebook set
- final release audit
- GitHub release/tag

## Phase II — Scientific AI

Expected release family: `v0.2.x`

### Step 16 — Sequence representations

Planned concepts:

- k-mer representation
- one-hot encoding
- tokenization
- encoder interface

Goal:

```text
Biological Sequence
       ↓
Representation / Encoder
       ↓
Model-ready numerical form
```

### Step 17 — PyTorch / Deep Learning

Planned learning sequence:

- tensor dataset adapter
- embedding layer
- MLP baseline
- 1D CNN
- training / validation workflow

The objective is not model sophistication alone, but showing how the existing Phase I
architecture accommodates deep learning.

### Step 18 — Biological foundation-model embeddings

Planned direction:

- DNA language-model embeddings
- protein language-model embeddings
- DNABERT-family examples
- ESM-family examples
- ProtT5-family examples

BioMini should provide an interface rather than couple the core to one model family.

## Phase III — Self-Driving Lab

Expected release family: `v0.3.x`

### Step 19 — Experiment domain model

Planned abstractions:

- `BiologicalSample`
- `Experiment`
- `ExperimentParameter`
- `Measurement`
- `ExperimentResult`

The existing ML `Sample` concept must remain distinct from a physical laboratory sample.

### Step 20 — Search space / optimizer

Planned concepts:

- parameter spaces
- surrogate models
- Bayesian optimization
- active learning
- next-experiment proposal

### Step 21 — Virtual Lab

Build a simulated experimental environment before hardware integration.

```text
Planner
  ↓
Experiment
  ↓
Virtual Lab
  ↓
Measurement
  ↓
Analysis / Model
  ↓
Optimizer
  └───────────↺
```

### Step 22 — Instrument abstraction

Potential interfaces:

- liquid handler
- plate reader
- microscope
- incubator

Vendor-specific APIs should be adapters rather than core-domain dependencies.

### Step 23 — SDL orchestration

Integrate the closed loop:

```text
Goal
 ↓
Planner
 ↓
Experiment
 ↓
Instrument / Virtual Lab
 ↓
Measurement
 ↓
QC / Analysis
 ↓
Model
 ↓
Optimizer
 ↓
Next Experiment
```

## Repository policy

Use one repository.

Use tags/releases to preserve phase milestones:

```text
v0.1.0-phase1
v0.2.0-phase2
v0.3.0-phase3
```

Educational material is phase-separated; framework source remains cumulative.
