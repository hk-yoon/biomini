# BioMini v0.1.0-phase1 — Phase I Release Notes

## English

### Release status

**BioMini v0.1.0 — Phase I FROZEN**

Phase I establishes the Core Scientific Software Foundation of BioMini. It starts from
small Python biological objects and develops them into a coherent educational framework
covering domain modeling, biological transformations, analysis, feature engineering,
machine learning, persistence, provenance, scientific validation, testing, packaging,
and continuous integration.

### Included in Phase I

- DNA, RNA, Protein, and AminoAcid domain objects
- SequenceMolecule and NucleicAcid abstractions
- complement, reverse complement, transcription, and translation
- Analyzer architecture with domain/analysis separation
- FeatureSet, Sample, and Dataset
- scikit-learn based ProteinPredictor workflow
- FASTA I/O
- JSON serialization and schema versioning
- ModelArtifact persistence with joblib
- stable identity, metadata, provenance, and lineage
- BioMini exception hierarchy
- Biopython scientific reference validation
- pytest regression suite and coverage
- installable Python package
- GitHub Actions CI for Python 3.10–3.13
- eight audited educational Jupyter notebooks

### Validation baseline

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

### Scope note

Phase I intentionally uses a compact biological scope. It does not attempt to replace
Biopython, RDKit, scikit-learn, PyTorch, or other mature scientific libraries. Its purpose
is to make scientific-software architecture explicit and teach how these components can
be connected coherently.

Phase II proceeds to Scientific AI through sequence representations, PyTorch/deep learning,
and biological foundation-model embeddings.

---

# 한국어 요약

## 릴리스 상태

**BioMini v0.1.0 — Phase I FROZEN**

Phase I은 BioMini의 **Core Scientific Software Foundation**을 확정한 단계이다.
작은 Python 생물학 객체에서 출발하여 biological domain modeling, biological
transformation, analysis, feature engineering, machine learning, persistence,
provenance, scientific validation, testing, packaging, CI까지 하나의 일관된
교육용 framework로 연결했다.

Phase I에는 DNA/RNA/Protein 객체, Analyzer architecture, FeatureSet/Sample/Dataset,
scikit-learn 기반 예측 workflow, FASTA I/O, serialization, model persistence,
provenance/lineage, Biopython reference validation, pytest, packaging, GitHub Actions CI,
그리고 8개의 교육용 Jupyter Notebook이 포함된다.

검증 baseline은 **42 tests passed, 90% coverage**, Python 3.10–3.13 GitHub Actions CI
PASS이며, Notebook 01–08도 모두 end-to-end 실행 PASS했다.

Phase I은 Biopython이나 다른 established scientific library를 대체하려는 것이 아니라,
작은 예제를 통해 scientific software architecture가 어떻게 성장하는지를 보여주는
교육용 foundation이다.

이 tag 이후 Phase I content는 frozen 상태로 보존하며, 다음 개발은
**Phase II — Scientific AI**로 진행한다.
