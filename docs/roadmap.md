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

Source code remains cumulative. Phase milestones are preserved with tags/releases.

---

## Phase I — Core Scientific Software

Target release:

```text
v0.1.0-phase1
```

Status:

> **Pre-Freeze**

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
- GitHub Actions CI
- Phase I educational Notebooks 01–08
- notebook execution/consistency audit

Remaining before final Phase I freeze:

- integrate audited notebooks into `notebooks/`
- add `notebooks/README.md`
- finish stale-document cleanup
- final full release audit
- tag/release `v0.1.0-phase1`
- mark Phase I **FROZEN**

---

## Phase II — Scientific AI

Expected release family:

```text
v0.2.x
```

### Step 16 — Sequence Representations

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

The domain object should remain distinct from its ML representation.

### Step 17 — PyTorch / Deep Learning

Planned learning sequence:

- tensor dataset adapter
- embedding layer
- MLP baseline
- 1D CNN
- training / validation workflow

The objective is not model sophistication alone, but showing how the Phase I
architecture accommodates deep learning without discarding the scientific-software
foundation.

### Step 18 — Biological Foundation-Model Embeddings

Planned direction:

- DNA language-model embeddings
- protein language-model embeddings
- DNABERT-family examples
- ESM-family examples
- ProtT5-family examples

BioMini should expose an interface rather than couple the core architecture to one model
family.

---

## Phase III — Self-Driving Lab

Expected release family:

```text
v0.3.x
```

### Step 19 — Experiment Domain Model

Planned abstractions:

- `BiologicalSample`
- `Experiment`
- `ExperimentParameter`
- `Measurement`
- `ExperimentResult`

The existing ML `Sample` concept must remain distinct from a physical laboratory sample.

### Step 20 — Search Space / Optimizer

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

### Step 22 — Instrument Abstraction

Potential interfaces:

- liquid handler
- plate reader
- microscope
- incubator

Vendor-specific APIs should be adapters rather than core-domain dependencies.

### Step 23 — SDL Orchestration

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

---

## Repository policy

Use one repository.

Use tags/releases to preserve phase milestones:

```text
v0.1.0-phase1
v0.2.0-phase2
v0.3.0-phase3
```

Educational material is phase-separated; framework source remains cumulative.

A likely long-term structure is:

```text
notebooks/
├── phase1/
├── phase2/
└── phase3/

docs/
├── phase1/
├── phase2/
└── phase3/
```

For the current Phase I release, the eight audited notebooks can be published directly
under `notebooks/`; phase subdirectories can be introduced when Phase II materials are
added.
