# BioMini Architecture — Phase I

## 1. Purpose

Phase I establishes a compact but coherent scientific-software foundation that can later
support Scientific AI and Self-Driving Lab extensions.

The architecture separates biological identity, scientific analysis, machine-learning
representation, persistence, and external I/O.

## 2. Layered view

```text
┌─────────────────────────────────────────────┐
│ Domain                                      │
│ DomainEntity → Molecule → SequenceMolecule  │
│                    ├─ DNA                   │
│                    ├─ RNA                   │
│                    └─ Protein               │
│ Provenance, AminoAcid                       │
└─────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│ Analysis                                    │
│ SequenceAnalyzer                            │
│ NucleicAcidAnalyzer                         │
│ DNAAnalyzer / RNAAnalyzer / ProteinAnalyzer │
└─────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│ ML Representation                           │
│ FeatureSet → Sample → Dataset               │
└─────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│ Model                                       │
│ ProteinPredictor                            │
└─────────────────────────────────────────────┘

Cross-cutting:
I/O · Persistence · Validation · Logging · Provenance
```

## 3. Domain layer

### DomainEntity

Provides:

- stable ID
- name
- metadata
- provenance
- schema version

### Molecule

Represents the common semantic level for molecular entities.

### SequenceMolecule

Adds a sequence representation and common sequence behavior.

### DNA / RNA / Protein

Define biological alphabets and domain-specific transformations.

### Provenance

Stores minimal lineage information:

- source
- source ID
- parent entity IDs
- metadata

This becomes important when a derived object is created, for example:

```text
DNA(id=D1)
   ↓ transcription
RNA(id=R1, parent=D1)
   ↓ translation
Protein(id=P1, parent=R1)
```

## 4. Analysis layer

Analysis is intentionally separated from biological identity.

```text
Protein               ProteinAnalyzer
  data        →          computation
```

This avoids turning domain classes into collections of unrelated analytical methods.

Current analyzer hierarchy:

```text
SequenceAnalyzer
├── NucleicAcidAnalyzer
│   ├── DNAAnalyzer
│   └── RNAAnalyzer
└── ProteinAnalyzer
```

## 5. ML representation layer

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
```

`FeatureSet` separates a biological entity from the numerical representation used by
machine-learning models.

Phase I protein descriptors include:

- sequence length
- molecular weight
- hydrophobic fraction
- amino-acid fractions

## 6. Model layer

`ProteinPredictor` is a small adapter around a trained scikit-learn model.

It preserves feature-column ordering explicitly so that training and inference use the
same schema.

## 7. Persistence

BioMini distinguishes domain serialization from trained-model persistence.

```text
Domain objects
   ↓
JSON + schema_version

Trained model
   ↓
ModelArtifact
   ├─ model
   ├─ feature_columns
   ├─ model_name
   ├─ target_name
   └─ metadata
   ↓
joblib
```

## 8. Scientific validation

Regression tests answer:

> Does the code still behave as designed?

Reference-validation tests add a second question:

> Does the selected scientific behavior agree with an independent established
> implementation?

Phase I uses Biopython as the reference for selected sequence operations.

## 9. Extension principle

Future capabilities should be added without collapsing these boundaries.

Phase II:

```text
Domain
  ↓
Encoder / Representation
  ↓
Tensor / Embedding
  ↓
Deep Model
```

Phase III:

```text
Experiment
  ↓
Measurement
  ↓
Analysis / Model
  ↓
Optimizer
  ↓
Next Experiment
```

The core principle remains separation of scientific meaning from implementation detail.
