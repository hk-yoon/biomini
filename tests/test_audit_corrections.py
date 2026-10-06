import json

import pytest
from Bio.Seq import Seq

from biomini import (
    DNA,
    RNA,
    Protein,
    ProteinAnalyzer,
    FeatureSet,
    Sample,
    Dataset,
    ValidationError,
    SerializationError,
    FastaFormatError,
    DataError,
    load_json,
    read_fasta,
    write_fasta,
)


def test_A_stop_only_translation_returns_empty_protein():
    protein = RNA("stop_only", "UAA").translate()
    assert isinstance(protein, Protein)
    assert protein.sequence == ""
    assert ProteinAnalyzer(protein).molecular_weight() == 0.0
    assert ProteinAnalyzer(protein).hydrophobic_fraction() == 0.0
    assert all(
        value == 0.0
        for value in ProteinAnalyzer(protein).amino_acid_fraction_features().values()
    )


def test_A_short_rna_translation_matches_biopython_empty_result():
    ours = RNA("short", "AU").translate().sequence
    reference = str(Seq("AU").translate(to_stop=True))
    assert ours == reference == ""


def test_A_empty_dna_and_rna_remain_invalid_but_empty_protein_is_valid():
    with pytest.raises(ValidationError):
        DNA("dna", "")
    with pytest.raises(ValidationError):
        RNA("rna", "")
    assert Protein("translated_empty", "").sequence == ""


def test_B_nested_feature_schema_is_rejected(tmp_path):
    payload = {
        "schema_version": "1.0",
        "type": "Dataset",
        "samples": [{
            "schema_version": "1.0",
            "type": "Sample",
            "feature_set": {
                "schema_version": "99.0",
                "type": "FeatureSet",
                "name": "p1",
                "features": {"x": 1.0},
            },
            "target": 1.0,
        }],
    }
    path = tmp_path / "bad_nested_schema.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(SerializationError):
        load_json(str(path))


def test_B_nested_sample_schema_is_rejected(tmp_path):
    payload = {
        "schema_version": "1.0",
        "type": "Dataset",
        "samples": [{
            "schema_version": "99.0",
            "type": "Sample",
            "feature_set": {
                "schema_version": "1.0",
                "type": "FeatureSet",
                "name": "p1",
                "features": {"x": 1.0},
            },
            "target": 1.0,
        }],
    }
    path = tmp_path / "bad_sample_schema.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(SerializationError):
        load_json(str(path))


def test_C_feature_set_validation():
    with pytest.raises(ValidationError):
        FeatureSet("", {"x": 1.0})
    with pytest.raises(ValidationError):
        FeatureSet("p1", {})
    with pytest.raises(ValidationError):
        FeatureSet("p1", {"x": "bad"})
    with pytest.raises(ValidationError):
        FeatureSet("p1", {"x": float("nan")})


def test_C_sample_and_dataset_validation():
    with pytest.raises(ValidationError):
        Sample("not-a-feature-set")

    dataset = Dataset()
    with pytest.raises(ValidationError):
        dataset.add("not-a-sample")


def test_C_entity_id_validation():
    with pytest.raises(ValidationError):
        DNA("gene", "ATGC", entity_id="")
    with pytest.raises(ValidationError):
        DNA("gene", "ATGC", entity_id="   ")


def test_D_fasta_errors_use_biomini_exception(tmp_path):
    bad_header = tmp_path / "bad_header.fasta"
    bad_header.write_text(">\nATGC\n", encoding="utf-8")

    with pytest.raises(FastaFormatError):
        read_fasta(str(bad_header))

    before_header = tmp_path / "before_header.fasta"
    before_header.write_text("ATGC\n>seq1\nATGC\n", encoding="utf-8")

    with pytest.raises(FastaFormatError):
        read_fasta(str(before_header))


def test_D_dataset_to_xy_uses_data_error():
    dataset = Dataset()
    dataset.add(Sample(FeatureSet("p1", {"x": 1.0})))

    with pytest.raises(DataError):
        dataset.to_xy()


def test_D_write_fasta_validates_line_width(tmp_path):
    with pytest.raises(ValidationError):
        write_fasta([Protein("p", "A")], str(tmp_path / "x.fasta"), line_width=0)
