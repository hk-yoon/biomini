# BioMini

[![CI](https://github.com/hk-yoon/biomini/actions/workflows/ci.yml/badge.svg)](https://github.com/hk-yoon/biomini/actions/workflows/ci.yml)

**From Python Biological Objects to Scientific AI and Self-Driving Labs**

BioMini is an educational scientific-software project that begins with simple Python
classes representing biological objects and gradually evolves toward Scientific AI
and Self-Driving Lab (SDL) architectures.

> Current milestone: **BioMini v0.1.0 — Phase I Release Candidate 1**

---

# 한국어 요약

## BioMini란?

BioMini는 `Molecule`, `Protein`, `AminoAcid` 같은 매우 단순한 Python OOP 예제에서
출발하여, 이를 단계적으로 발전시키면서 **scientific software가 어떻게 설계되고
확장되는가**를 학습하기 위한 교육용 framework입니다.

단순히 DNA나 Protein을 다루는 몇 개의 함수를 만드는 것이 목적이 아닙니다.

BioMini의 핵심 질문은 다음과 같습니다.

> 작은 Python class가 어떻게 biological domain model이 되고,  
> scientific analysis와 machine learning을 거쳐,  
> Scientific AI와 Self-Driving Lab까지 확장될 수 있는가?

현재는 **Phase I — Core Scientific Software Foundation**까지 개발되었습니다.

Phase I에서는 다음을 구현했습니다.

- `DNA`, `RNA`, `Protein`, `AminoAcid` 객체 모델
- `Molecule`, `SequenceMolecule`, `NucleicAcid` abstraction
- complement / reverse complement
- transcription / translation
- Analyzer architecture
- sequence composition / motif search / GC content
- protein molecular weight / hydrophobic fraction
- `FeatureSet`, `Sample`, `Dataset`
- scikit-learn 기반 machine-learning workflow
- FASTA read/write
- JSON serialization
- trained model persistence
- stable ID / metadata / provenance / lineage
- schema versioning
- BioMini-specific exception hierarchy
- Biopython 기반 scientific reference validation
- pytest regression testing
- package installation / version management
- GitHub Actions CI

현재 GitHub CI에서는 Python **3.10, 3.11, 3.12, 3.13** 환경을 모두 검증하고 있습니다.

---

## BioMini의 목적

BioMini는 Biopython, RDKit, scikit-learn, PyTorch 등을 대체하기 위한 프로젝트가 아닙니다.

오히려 다음과 같은 관계를 목표로 합니다.

```text
BioMini
   ↓
Scientific Software Architecture
   ↓
Biopython
RDKit
scikit-learn
PyTorch
Foundation Models
SDL / Laboratory Systems
