import math

from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from biomini import (
    DNA, RNA, Protein,
    ProteinAnalyzer, FeatureSet, Sample, Dataset,
    ProteinPredictor, ModelArtifact,
    save_json, load_json,
    save_model_artifact, load_model_artifact,
)


def test_sequence_json_roundtrip(tmp_path):
    for i, original in enumerate([
        DNA("gene1", "ATGCGT"),
        RNA("rna1", "AUGCGU"),
        Protein("protein1", "ACDEFGHIK"),
    ]):
        path = tmp_path / f"obj_{i}.json"
        save_json(original, str(path))
        restored = load_json(str(path))
        assert type(restored) is type(original)
        assert restored.name == original.name
        assert restored.sequence == original.sequence


def test_feature_set_json_roundtrip(tmp_path):
    original = FeatureSet("p1", {"length": 10, "x": 0.5})
    path = tmp_path / "features.json"
    save_json(original, str(path))
    restored = load_json(str(path))
    assert restored.name == original.name
    assert restored.features == original.features


def test_dataset_json_roundtrip(tmp_path):
    dataset = Dataset()
    dataset.add(Sample(FeatureSet("p1", {"length": 4.0}), target=0.2))
    dataset.add(Sample(FeatureSet("p2", {"length": 5.0}), target=0.7))

    path = tmp_path / "dataset.json"
    save_json(dataset, str(path))
    restored = load_json(str(path))

    assert len(restored) == 2
    assert restored.samples[0].feature_set.name == "p1"
    assert math.isclose(restored.samples[1].target, 0.7)


def test_model_artifact_roundtrip_prediction_consistency(tmp_path):
    protein_data = [
        ("p1", "AILMFWVYGST", 0.22),
        ("p2", "ACDEFGHIKLM", 0.73),
        ("p3", "GGGGAAAASSS", 0.91),
        ("p4", "VVVVLLLLFFF", 0.18),
        ("p5", "DEDEKKRRSSS", 0.88),
        ("p6", "ACACACACACA", 0.69),
        ("p7", "MMMMIIILLLL", 0.16),
        ("p8", "STNQSTNQSTN", 0.94),
        ("p9", "FYWFYWFYWFY", 0.13),
        ("p10", "GASGASGASGA", 0.86),
    ]

    dataset = Dataset()
    for name, sequence, target in protein_data:
        feature_set = ProteinAnalyzer(Protein(name, sequence)).to_features()
        dataset.add(Sample(feature_set, target=target))

    X, y = dataset.to_xy()

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", Ridge(alpha=1.0)),
    ])
    model.fit(X, y)

    artifact = ModelArtifact(
        model=model,
        feature_columns=list(X.columns),
        model_name="protein_solubility_ridge",
        target_name="solubility",
        metadata={"purpose": "educational validation"},
    )

    candidate = Protein("candidate", "ACGSTNQILMV")
    before = ProteinPredictor.from_artifact(artifact).predict(candidate)

    path = tmp_path / "model.joblib"
    save_model_artifact(artifact, str(path))
    restored = load_model_artifact(str(path))
    after = ProteinPredictor.from_artifact(restored).predict(candidate)

    assert restored.model_name == "protein_solubility_ridge"
    assert restored.target_name == "solubility"
    assert restored.feature_columns == list(X.columns)
    assert math.isclose(before, after, rel_tol=1e-12, abs_tol=1e-12)
