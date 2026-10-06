import json
import logging

import pytest

from biomini import (
    DNA,
    Protein,
    Provenance,
    SCHEMA_VERSION,
    SerializationError,
    ValidationError,
    load_json,
    save_json,
)


def test_stable_unique_entity_ids():
    a = DNA("a", "ATGC")
    b = DNA("b", "ATGC")
    assert a.id
    assert b.id
    assert a.id != b.id


def test_metadata_and_provenance_json_roundtrip(tmp_path):
    original = Protein(
        "p1",
        "ACDE",
        metadata={"organism": "Homo sapiens"},
        provenance=Provenance(
            source="UniProt",
            source_id="TEST123",
            parent_ids=["parent-1"],
            metadata={"note": "reference"},
        ),
    )
    path = tmp_path / "protein.json"
    save_json(original, str(path))
    restored = load_json(str(path))

    assert restored.id == original.id
    assert restored.metadata == original.metadata
    assert restored.provenance.source == "UniProt"
    assert restored.provenance.source_id == "TEST123"
    assert restored.provenance.parent_ids == ["parent-1"]
    assert restored.provenance.metadata == {"note": "reference"}


def test_transcription_and_translation_record_lineage():
    dna = DNA("gene", "ATGGCC", metadata={"project": "demo"})
    rna = dna.transcribe()
    protein = rna.translate()

    assert rna.provenance.source == "transcription"
    assert rna.provenance.parent_ids == [dna.id]
    assert protein.provenance.source == "translation"
    assert protein.provenance.parent_ids == [rna.id]
    assert protein.metadata == {"project": "demo"}


def test_domain_validation_uses_biomini_exception():
    with pytest.raises(ValidationError):
        DNA("bad", "ATGX")
    with pytest.raises(ValueError):
        DNA("bad", "ATGX")


def test_load_json_rejects_unknown_schema(tmp_path):
    path = tmp_path / "future.json"
    path.write_text(
        json.dumps({
            "schema_version": "99.0",
            "type": "DNA",
            "id": "x",
            "name": "future",
            "sequence": "ATGC",
            "metadata": {},
            "provenance": {},
        }),
        encoding="utf-8",
    )

    with pytest.raises(SerializationError):
        load_json(str(path))


def test_schema_version_is_explicit():
    dna = DNA("gene", "ATGC")
    assert dna.to_dict()["schema_version"] == SCHEMA_VERSION


def test_library_does_not_configure_application_logging():
    biomini_logger = logging.getLogger("biomini")
    assert any(isinstance(handler, logging.NullHandler) for handler in biomini_logger.handlers)
