# BioMini Phase I Completion Report

## 1. 문서의 목적

이 문서는 BioMini 프로젝트의 **Phase I — Core Scientific Software Foundation** 완료 상태를 공식적으로 정리하는 master document이다.

Phase I에서 수행한 Step 1–15의 개발 경과, 현재 canonical architecture, 주요 설계 결정, scientific validation, software-engineering validation, 현재의 한계, 그리고 Phase II–III의 향후 계획을 하나의 기준 문서로 통합한다.

현재 상태는 다음과 같다.

> **BioMini v0.1.0 — Phase I Release Candidate 1 (RC1)**

Phase I의 코드 구현과 Canonical Audit 보정 작업은 완료되었다. 다만 GitHub 공개 문서, 교육용 notebook/course material, 최종 release audit가 남아 있으므로 아직 `Phase I FROZEN`으로 선언하지 않는다.

---

# 2. 프로젝트의 출발점과 최종 목표

BioMini는 매우 작은 Python OOP 예제에서 출발했다.

초기 모델은 다음 세 개의 class를 중심으로 구성되어 있었다.

```text
Molecule
Protein
AminoAcid
```

초기의 목적은 생물학적 대상을 Python class로 표현해 보는 것이었다. 그러나 프로젝트가 진행되면서 목표는 다음과 같이 확장되었다.

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
Persistence / Reproducibility
        ↓
Scientific Validation
        ↓
Production-oriented Scientific Software
        ↓
Scientific AI
        ↓
Self-Driving Lab
```

따라서 BioMini의 장기적 목적은 단순한 bioinformatics utility library를 만드는 것이 아니다.

BioMini는 다음과 같은 교육적 질문에 답하는 작은 framework를 지향한다.

> **단순한 Python class가 어떻게 scientific software, Scientific AI, 그리고 Self-Driving Lab architecture로 발전하는가?**

이 점에서 BioMini는 Biopython, RDKit, scikit-learn, PyTorch 등의 기존 scientific library를 대체하려는 프로젝트가 아니다. 오히려 이러한 도구들을 하나의 일관된 scientific software architecture 안에서 이해하고 통합하는 교육용 framework를 목표로 한다.

---

# 3. Phase I의 목표

Phase I의 목표는 Scientific AI나 SDL을 직접 구현하는 것이 아니라, 그 위에 안정적으로 구축할 수 있는 **Core Scientific Software Foundation**을 만드는 것이었다.

Phase I에서 다음 능력을 확보하는 것을 목표로 했다.

- biological domain object의 명시적 모델링
- sequence-based biological entity의 abstraction
- biological transformation의 객체 기반 표현
- domain object와 analysis logic의 분리
- biological data를 machine-learning feature로 변환
- dataset과 predictor abstraction
- FASTA I/O
- serialization과 trained-model persistence
- provenance와 lineage
- independent scientific reference validation
- regression testing
- package installation과 version management

Phase I 종료 시점에서 이 목표는 충족되었다.

---

# 4. Step 1–15 개발 경과

## Step 1 — Modern Python Cleanup

초기 코드를 현대적인 Python 스타일로 정리했다.

주요 변경 사항:

- `super()` 사용
- generic `Exception` 대신 구체적 exception 사용
- snake_case method naming
- type hint 적용
- `__repr__`, `__len__` 추가
- list comprehension 및 Pythonic expression 사용

이 단계의 핵심은 biology 기능의 추가가 아니라 **유지보수 가능한 Python codebase의 출발점**을 만드는 것이었다.

---

## Step 2 — SequenceMolecule Abstraction

DNA, RNA, Protein과 같이 sequence를 핵심 representation으로 갖는 분자들을 하나의 추상 개념으로 묶기 위해 `SequenceMolecule`을 도입했다.

```text
Molecule
    ↓
SequenceMolecule
```

공통 책임:

- sequence 저장
- uppercase normalization
- sequence retrieval
- length
- representation

이 단계에서 처음으로 biological object의 공통 computational abstraction을 명시적으로 모델링했다.

---

## Step 3 — DNA / RNA / Protein Hierarchy

sequence molecule을 다음과 같이 구체화했다.

```text
Molecule
  └── SequenceMolecule
       ├── NucleicAcid
       │    ├── DNA
       │    └── RNA
       └── Protein
```

각 subclass는 자신의 biological alphabet을 validation한다.

- DNA: `A/T/G/C`
- RNA: `A/U/G/C`
- Protein: canonical 20 amino acids

Phase I에서는 교육적 단순성을 위해 ambiguous IUPAC symbol은 지원하지 않는다.

---

## Step 4 — Biological Transformations

central dogma를 object transformation으로 구현했다.

```text
DNA
 ↓ transcription
RNA
 ↓ translation
Protein
```

추가된 주요 기능:

- DNA complement
- DNA reverse complement
- DNA → RNA transcription
- RNA → Protein translation

Phase I translation은 다음 정책을 갖는다.

- frame 0
- first stop codon에서 종료
- incomplete terminal codon 무시
- alternate genetic code 미지원
- ORF search 미지원

transcription은 저장된 DNA를 coding strand로 간주한다.

---

## Step 5 — Biological Analysis

sequence object에 대해 기본적인 분석 기능을 추가했다.

예:

- sequence composition
- motif search
- GC content
- amino-acid composition
- hydrophobic fraction
- protein molecular weight

이 단계에서는 분석 기능이 domain object와 가까이 존재했지만, 이후 구조적 문제를 해결하기 위해 별도 analyzer architecture로 분리했다.

---

## Step 6 — Analyzer Architecture

domain object와 analysis logic을 분리했다.

```text
Domain Objects                  Analysis Objects

DNA              ───────────→   DNAAnalyzer
RNA              ───────────→   RNAAnalyzer
Protein          ───────────→   ProteinAnalyzer
```

최종 analyzer hierarchy:

```text
SequenceAnalyzer
  ├── NucleicAcidAnalyzer
  │    ├── DNAAnalyzer
  │    └── RNAAnalyzer
  └── ProteinAnalyzer
```

이 단계의 핵심 설계 원칙은 다음과 같다.

> **Biological object는 자신이 무엇인지 표현하고, Analyzer는 그 object를 어떻게 계산하고 해석할지를 담당한다.**

즉 inheritance보다 composition을 적극적으로 사용했다.

---

## Step 7 — FeatureSet / Sample / Dataset

biology에서 machine learning으로 넘어가는 중간 계층을 추가했다.

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

주요 class:

- `FeatureSet`
- `Sample`
- `Dataset`

Protein의 경우 다음과 같은 handcrafted descriptor를 feature로 변환한다.

- sequence length
- molecular weight
- hydrophobic fraction
- amino-acid fractions

이 단계에서 biological representation과 ML representation을 명확히 분리했다.

---

## Step 8 — Machine Learning Integration

scikit-learn 기반의 작은 prediction pipeline을 추가했다.

```text
Protein
  ↓
ProteinAnalyzer
  ↓
FeatureSet
  ↓
Dataset
  ↓
scikit-learn model
  ↓
ProteinPredictor
```

교육용 예제에서는 다음과 같은 전통적 ML workflow를 사용했다.

- `StandardScaler`
- `Ridge`
- feature-column preservation
- prediction wrapper

이 단계는 Scientific AI의 최종 형태가 아니라, **scientific object에서 ML pipeline으로 넘어가는 interface를 만드는 단계**였다.

---

## Step 9 — Python Package Architecture

단일 script 중심 구조에서 package 구조로 전환했다.

주요 module:

```text
biomini/
├── core.py
├── sequence.py
├── analyzers.py
├── features.py
├── dataset.py
├── models.py
├── io.py
├── persistence.py
├── errors.py
├── logging_utils.py
└── _version.py
```

이 단계부터 BioMini는 단순 예제 코드가 아니라 작은 framework 형태를 갖기 시작했다.

---

## Step 10 — FASTA I/O

FASTA read/write 기능을 추가했다.

주요 기능:

- multi-line FASTA parsing
- DNA/RNA/Protein object conversion
- FASTA writing
- identifier / description separation

중요한 설계 원칙은 다음과 같다.

> 파일 형식 parsing과 biological object validation은 서로 다른 책임이다.

Phase I에서는 교육 목적으로 minimal FASTA parser를 직접 구현했지만, production에서는 Biopython `SeqIO` 같은 검증된 backend를 사용할 수 있다.

---

## Step 11 — Regression Testing

`pytest` 기반 regression test를 도입했다.

초기 검증 범위:

- sequence normalization
- validation
- complement / reverse complement
- transcription
- translation
- GC content
- protein molecular weight
- hydrophobic fraction
- feature generation
- FASTA read/write

이 단계에서 BioMini는 처음으로 “실행되는 코드”에서 “변경을 안전하게 검증할 수 있는 코드”로 발전했다.

---

## Step 12 — Serialization / Model Saving

scientific reproducibility와 workflow continuity를 위해 persistence layer를 추가했다.

주요 기능:

- biological object → JSON
- JSON → biological object restoration
- `FeatureSet`, `Sample`, `Dataset` serialization
- schema version
- `ModelArtifact`
- scikit-learn model persistence using `joblib`
- feature-column preservation
- save/load 전후 prediction consistency validation

핵심 구조:

```text
trained model
    +
feature schema
    +
target information
    +
metadata
      ↓
ModelArtifact
      ↓
joblib
```

model 자체만 저장하는 대신, inference에 필요한 context를 함께 저장하도록 설계했다.

---

## Step 13 — Scientific Reference Validation

BioMini의 결과가 내부적으로만 일관적인지 확인하는 수준을 넘어, independent scientific implementation과 비교했다.

reference implementation으로 Biopython을 사용했다.

검증 대상:

- reverse complement
- transcription
- translation
- protein molecular weight
- FASTA parsing

이 과정에서 protein residue mass precision 차이를 발견했고, Biopython reference와 정렬되도록 보정했다.

따라서 Step 13은 다음 질문을 검증한다.

> **BioMini가 의도대로 작동하는가?**  
> 뿐만 아니라  
> **그 의도가 established scientific implementation과 일치하는가?**

---

## Step 14 — Production Hardening

framework 수준의 identity, provenance, error handling을 추가했다.

새로운 주요 abstraction:

```text
DomainEntity
  ├── stable ID
  ├── name
  ├── metadata
  └── provenance
        ↓
     Molecule
```

`Provenance`를 통해 scientific lineage를 기록한다.

예:

```text
DNA
 ↓ transcription
RNA
 ↓ translation
Protein
```

각 생성 object는 parent entity의 ID를 lineage에 기록한다.

custom exception hierarchy:

```text
BioMiniError
├── ValidationError
├── SerializationError
├── ModelPersistenceError
├── FastaFormatError
└── DataError
```

또한 library가 application logging configuration을 침범하지 않도록 logging policy를 정리했다.

---

## Step 15 — Packaging / Versioning / Documentation Quality

BioMini를 실제 설치 가능한 Python package로 정리했다.

주요 작업:

- `pyproject.toml`
- package metadata
- editable installation
- package version
- dependency grouping
- pytest configuration
- coverage configuration
- README
- LICENSE
- canonical-status tracking

현재 version:

```text
0.1.0
```

현재 `biomini/_version.py`가 package version의 single source of truth이며, `pyproject.toml`은 dynamic lookup을 사용한다.

dependency specification은 `pyproject.toml`을 single source of truth로 사용한다.

---

# 5. Canonical Audit와 A–F Correction Pass

Step 15 이후 Phase I을 바로 freeze하지 않고 별도의 Canonical Audit를 수행했다.

Audit 결과 여섯 개의 correction item A–F가 확인되었다.

## A — Empty Translation Product

문제:

```python
RNA("UAA").translate()
```

는 biological/computationally valid한 empty translation product를 생성하지만 기존 `SequenceMolecule`은 empty sequence를 허용하지 않았다.

정책:

- DNA empty sequence 불허
- RNA empty sequence 불허
- Protein은 valid computational result로서 empty sequence 허용

empty Protein 분석값:

```text
molecular_weight = 0.0
hydrophobic_fraction = 0.0
amino-acid fractions = 0.0
```

해결 완료.

---

## B — Nested Serialization Schema Validation

기존에는 top-level schema만 확인하고 nested `Sample`, `FeatureSet` schema는 검사하지 않았다.

수정 후:

```text
Dataset
 └── Sample
      └── FeatureSet(schema_version="99.0")
                         ↓
                SerializationError
```

모든 serializable object가 자신의 schema version을 검증한다.

해결 완료.

---

## C — Input Validation Consistency

다음 validation을 강화했다.

- `entity_id`
- metadata
- provenance
- parent IDs
- `FeatureSet`
- `Sample`
- `Dataset.add()`

특히 `FeatureSet`은 다음을 요구한다.

- non-empty name
- non-empty feature dictionary
- feature name은 non-empty string
- feature value는 finite numeric value

해결 완료.

---

## D — Exception Hierarchy Consistency

FASTA parser와 data-layer operation에서 raw `ValueError` 사용을 줄이고 BioMini-specific exception을 사용하도록 정리했다.

추가:

```text
FastaFormatError
DataError
```

해결 완료.

---

## E — Version Source of Truth

version이 `_version.py`와 `pyproject.toml`에 중복되던 문제를 제거했다.

현재:

```text
biomini/_version.py
        ↓
single source of truth
        ↓
pyproject.toml dynamic version
```

해결 완료.

---

## F — Dependency Source of Truth

`requirements.txt`와 `pyproject.toml`의 dependency 정의가 중복되던 문제를 제거했다.

현재:

```text
pyproject.toml
      ↓
single dependency authority
```

runtime:

- pandas
- scikit-learn
- joblib

optional scientific validation:

- Biopython

development:

- pytest
- pytest-cov

해결 완료.

---

# 6. 현재 Canonical Architecture

Phase I RC1의 중심 구조는 다음과 같다.

```text
DomainEntity
│
├── Molecule
│    └── SequenceMolecule
│         ├── NucleicAcid
│         │    ├── DNA
│         │    └── RNA
│         └── Protein
│
├── Provenance
└── AminoAcid


Analysis
│
├── SequenceAnalyzer
├── NucleicAcidAnalyzer
├── DNAAnalyzer
├── RNAAnalyzer
└── ProteinAnalyzer


ML Representation
│
├── FeatureSet
├── Sample
└── Dataset


Model
│
└── ProteinPredictor


Persistence
│
└── ModelArtifact


I/O
│
└── FastaRecord


Errors
│
├── BioMiniError
├── ValidationError
├── SerializationError
├── ModelPersistenceError
├── FastaFormatError
└── DataError
```

Phase I RC1에는 약 26개의 class-level abstraction이 존재한다. 단순히 class 수를 늘리는 것이 목적은 아니며, 독립된 responsibility와 state가 있는 경우에만 class를 도입하는 것을 기본 원칙으로 한다.

---

# 7. 주요 Software Design Principles

Phase I에서 확립된 설계 원칙은 다음과 같다.

## 7.1 Separation of Concerns

```text
Domain
Analysis
Representation
Data
Model
Persistence
I/O
Validation
```

을 가능한 한 분리한다.

---

## 7.2 Composition over Unnecessary Inheritance

Analyzer는 biological object를 상속하지 않는다.

```text
ProteinAnalyzer has-a Protein
```

관계를 사용한다.

---

## 7.3 Explicit Scientific Semantics

software behavior는 biological assumption과 함께 명시한다.

예:

```text
transcription uses stored DNA as coding strand
translation uses frame 0
stop at first stop codon
```

---

## 7.4 Reproducibility

scientific object는 다음을 유지할 수 있어야 한다.

```text
identity
metadata
provenance
schema version
```

trained model 역시 model object만이 아니라 feature schema와 metadata를 함께 저장한다.

---

## 7.5 Validation at Boundaries

잘못된 state가 framework 안으로 깊이 들어오기 전에 가능한 한 boundary에서 검사한다.

---

## 7.6 Scientific Reference Validation

가능한 경우 자체 구현을 independent established library와 cross-check한다.

Phase I에서는 Biopython을 reference로 사용했다.

---

## 7.7 Educational Transparency

BioMini는 일부 기능을 의도적으로 직접 구현한다.

목적은 기존 library를 재발명하는 것이 아니라, 내부 computational concept을 학습할 수 있도록 하기 위한 것이다.

production-oriented 단계에서는 기존 검증 library를 backend로 사용할 수 있다.

---

# 8. Biopython과 BioMini의 관계

BioMini와 Biopython은 경쟁 관계가 아니다.

```text
Biopython
= mature bioinformatics library

BioMini
= educational scientific-software architecture
```

Phase I에서는 일부 기능을 직접 구현하여 학습 가능성을 높이고, 그 결과를 Biopython과 비교하여 scientific correctness를 검증했다.

장기적으로는 다음 구조가 가능하다.

```text
BioMini
  ↓
Scientific backend
  ├── Biopython
  ├── RDKit
  ├── scikit-learn
  ├── PyTorch
  └── SDL / instrument libraries
```

따라서 BioMini의 장기적 가치는 개별 biological utility를 많이 보유하는 데 있지 않고, 여러 scientific component를 하나의 coherent architecture로 연결하는 데 있다.

---

# 9. Phase I Biological Semantic Contract

Phase I에서 의도적으로 제한한 biological semantics는 다음과 같다.

- DNA alphabet은 `A/T/G/C`
- RNA alphabet은 `A/U/G/C`
- Protein alphabet은 canonical 20 amino acids
- DNA와 RNA는 non-empty
- Protein은 valid translation result일 경우 empty 가능
- stored DNA는 transcription 시 coding strand로 취급
- translation frame은 0
- first stop codon에서 translation 종료
- incomplete terminal codon은 무시
- ambiguous IUPAC symbols 미지원
- ORF search 미지원
- alternate genetic code 미지원
- sequence annotation 미지원
- protein molecular weight는 Biopython reference와 정렬된 average residue-mass model 사용

이들은 오류가 아니라 Phase I의 명시적 educational scope이다.

---

# 10. Validation Status

Phase I RC1은 다음 validation을 통과했다.

```text
pytest                    43 passed
line coverage             90%
compileall                PASS
wheel build               PASS
editable installation     PASS
basic example workflow    PASS
Biopython validation      PASS
```

Biopython reference-validation 대상:

- reverse complement
- transcription
- translation
- protein molecular weight
- FASTA parsing

남아 있는 Biopython warning은 deliberately tested incomplete terminal codon에 관한 것이다.

---

# 11. Packaging Status

현재 package version:

```text
BioMini 0.1.0
```

canonical package metadata:

```text
pyproject.toml
```

version source:

```text
biomini/_version.py
```

development installation:

```text
python -m pip install -e .
```

development dependencies:

```text
python -m pip install -e ".[dev]"
```

scientific validation dependencies:

```text
python -m pip install -e ".[validation]"
```

전체 development environment:

```text
python -m pip install -e ".[dev,validation]"
```

---

# 12. Security and Reproducibility Note

BioMini의 `ModelArtifact`는 `joblib`을 사용한다.

`joblib`은 pickle 기반이므로 **신뢰할 수 없는 artifact를 load해서는 안 된다.**

이 정책은 GitHub README와 교육자료에서도 명시한다.

---

# 13. Phase I의 현재 한계

Phase I은 의도적으로 compact한 framework이다.

현재 지원하지 않는 영역:

```text
complex genome annotation
ambiguous sequence alphabet
multiple genetic codes
ORF discovery
alignment algorithms
large-scale genomics pipelines
chemical graph representation
3D molecular representation
deep learning
biological foundation models
experiment design
active learning
laboratory instruments
SDL orchestration
```

이 중 일부는 Phase II–III에서 확장되며, 일부는 Biopython/RDKit 등 외부 backend에 위임하는 것이 더 적절하다.

---

# 14. Phase II — Scientific AI 계획

Phase II의 목표는 handcrafted descriptor 중심의 ML에서 sequence representation과 representation learning으로 확장하는 것이다.

## Step 16 — Sequence Representations

예상 범위:

```text
Raw Sequence
  ├── k-mer
  ├── one-hot encoding
  └── tokenization
```

이 단계에서는 representation과 domain object를 분리하여 encoder abstraction을 도입할 예정이다.

---

## Step 17 — PyTorch / Deep Learning

예상 흐름:

```text
Biological Object
      ↓
Encoder
      ↓
Tensor
      ↓
PyTorch Dataset
      ↓
Neural Model
      ↓
Prediction
```

초기 구현은 교육적 이해를 위해 다음과 같은 비교적 단순한 model부터 시작한다.

- MLP
- embedding
- 1D CNN

---

## Step 18 — Biological Foundation Model Embeddings

이후 pretrained biological representation을 연결한다.

후보:

- DNA language-model embeddings
- protein language-model embeddings
- DNABERT 계열
- ESM 계열
- ProtT5 계열

중요한 원칙은 특정 foundation model을 BioMini core에 강하게 결합하지 않는 것이다.

```text
BioMini Encoder Interface
          ↓
Multiple Backend Models
```

형태를 목표로 한다.

---

# 15. Phase III — Self-Driving Lab 계획

Phase III의 목표는 BioMini를 experimental closed-loop system으로 확장하는 것이다.

예상 개발 순서:

## Step 19 — Experiment Domain Model

주요 abstraction:

```text
BiologicalSample
Experiment
ExperimentParameter
Measurement
ExperimentResult
```

현재 ML 의미의 `Sample`과 실제 laboratory sample을 명확히 구분해야 한다.

---

## Step 20 — Search Space / Optimizer

```text
Experiment Result
      ↓
Dataset
      ↓
Surrogate Model
      ↓
Optimizer
      ↓
Next Experiment
```

Bayesian optimization 및 active learning 등을 검토한다.

---

## Step 21 — Virtual Lab

실제 hardware 이전에 simulation 기반 closed loop를 만든다.

```text
Planner
   ↓
Experiment
   ↓
Virtual Lab
   ↓
Measurement
   ↓
Analysis
   ↓
Model
   ↓
Optimizer
   └────────────↺
```

Phase III에서 가장 중요한 중간 milestone이 될 수 있다.

---

## Step 22 — Instrument Abstraction

예:

```text
Instrument
├── LiquidHandler
├── PlateReader
├── Microscope
└── Incubator
```

vendor-specific implementation은 adapter로 분리한다.

---

## Step 23 — SDL Orchestration

최종적으로 다음 loop를 통합한다.

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

이를 `SDLController` 또는 equivalent orchestration layer로 구현할 예정이다.

---

# 16. GitHub Repository 전략

Phase I, II, III를 별도 repository로 분리하지 않고 하나의 repository에서 발전시키는 것을 기본 정책으로 한다.

```text
biomini
│
├── v0.1.0 — Phase I
├── v0.2.0 — Phase II
└── v0.3.0 — Phase III
```

source code는 cumulative하게 유지한다.

교육자료는 phase별로 분리한다.

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

각 Phase 종료 시 Git tag/release를 생성하면 특정 시점의 source를 별도로 복제할 필요가 없다.

---

# 17. Phase I 교육자료 계획

Phase I은 다음과 같은 교육 과정으로 재구성할 수 있다.

```text
01 From Classes to Biological Objects
02 Inheritance and Sequence Abstraction
03 DNA, RNA, Protein and Biological Transformations
04 Separating Domain Objects and Analysis
05 From Biology to Feature Engineering
06 Dataset and Machine Learning
07 Persistence, Provenance and Reproducibility
08 Validation, Packaging and Scientific Software
```

각 notebook은 다음 pedagogical pattern을 사용하는 것이 좋다.

```text
Concept
  ↓
Initial Design
  ↓
Problem
  ↓
Design Decision
  ↓
Implementation
  ↓
Execution
  ↓
Validation
  ↓
What We Learned
```

즉 final code를 처음부터 보여주는 방식보다는 framework가 **왜 이렇게 진화했는가**를 가르치는 방식이 Phase I의 교육적 가치를 더 잘 살린다.

---

# 18. Phase I Freeze 전에 남은 작업

코드 구현 및 A–F corrective pass는 완료되었다.

남은 작업은 다음 네 영역이다.

1. **GitHub publication preparation**
   - final README
   - architecture document
   - design decisions
   - scientific-validation document
   - roadmap
   - CHANGELOG
   - CI workflow

2. **Educational material**
   - Phase I notebooks
   - instructor/learner guide
   - exercises
   - expected outputs

3. **Release packaging**
   - canonical repository layout
   - release ZIP
   - version/tag policy

4. **Final Release Audit**
   - code
   - tests
   - documentation
   - examples
   - installation
   - cross-platform assumptions
   - release metadata

이 작업을 완료한 뒤 다음 상태로 전환한다.

```text
BioMini v0.1.0
Phase I — FROZEN
```

그 후 Phase II development를 시작한다.

---

# 19. Phase I의 교육적 의미

Phase I의 핵심 성과는 DNA, RNA, Protein class를 만든 것 자체가 아니다.

보다 중요한 것은 다음 development narrative를 실제 코드로 경험할 수 있다는 점이다.

```text
Simple Python Class
        ↓
Inheritance
        ↓
Abstraction
        ↓
Separation of Concerns
        ↓
Scientific Analysis
        ↓
Feature Engineering
        ↓
Machine Learning
        ↓
Persistence
        ↓
Provenance
        ↓
Scientific Validation
        ↓
Testing
        ↓
Packaging
```

즉 Phase I은 Python OOP를 biology context에서 설명하는 데서 시작하지만, 최종적으로는 다음 주제를 하나의 작은 프로젝트 안에서 연결한다.

- Python programming
- OOP
- software design
- bioinformatics
- scientific computing
- machine learning
- reproducibility
- testing
- scientific software engineering

이 연결성이 BioMini Phase I의 가장 중요한 교육적 가치이다.

---

# 20. Phase I Completion Statement

BioMini Phase I은 다음 목표를 달성했다.

> biological domain object에서 출발하여 scientific analysis, feature engineering, machine learning, persistence, provenance, validation, testing, packaging으로 이어지는 작은 but coherent scientific software framework를 구축했다.

현재 구현은 **BioMini v0.1.0 Phase I RC1**으로 간주한다.

Phase I source code는 기능적으로 completion 상태이며, Canonical Audit correction A–F도 모두 해결되었다.

다만 최종 공개와 교육 활용을 위한 documentation, educational material, final release audit가 남아 있으므로 아직 `FROZEN`으로 선언하지 않는다.

다음 작업은 GitHub publication preparation과 Phase I educational material 제작이며, 최종 release audit 이후:

```text
BioMini v0.1.0
Phase I — FROZEN
```

으로 확정한다.

그 이후 BioMini는 Phase II — Scientific AI로 진행한다.
