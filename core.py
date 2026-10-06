from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from .errors import SerializationError, ValidationError

SCHEMA_VERSION = "1.0"


def validate_schema_version(data: dict) -> None:
    """Reject serialized payloads from unsupported schema versions."""
    if not isinstance(data, dict):
        raise SerializationError("serialized payload must be a dictionary")

    schema_version = data.get("schema_version")
    if schema_version != SCHEMA_VERSION:
        raise SerializationError(
            f"unsupported schema_version: {schema_version!r}; "
            f"expected {SCHEMA_VERSION!r}"
        )


@dataclass
class Provenance:
    """Minimal scientific lineage information for a domain entity."""

    source: str | None = None
    source_id: str | None = None
    parent_ids: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.source is not None and not isinstance(self.source, str):
            raise ValidationError("provenance source must be a string or None")
        if self.source_id is not None and not isinstance(self.source_id, str):
            raise ValidationError("provenance source_id must be a string or None")
        if not all(isinstance(parent_id, str) and parent_id.strip()
                   for parent_id in self.parent_ids):
            raise ValidationError("provenance parent_ids must contain non-empty strings")
        if not isinstance(self.metadata, dict):
            raise ValidationError("provenance metadata must be a dictionary")

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "source_id": self.source_id,
            "parent_ids": list(self.parent_ids),
            "metadata": dict(self.metadata),
        }

    @classmethod
    def from_dict(cls, data: dict | None) -> "Provenance":
        if not data:
            return cls()
        if not isinstance(data, dict):
            raise ValidationError("provenance payload must be a dictionary")
        return cls(
            source=data.get("source"),
            source_id=data.get("source_id"),
            parent_ids=list(data.get("parent_ids", [])),
            metadata=dict(data.get("metadata", {})),
        )


class DomainEntity:
    """Base entity providing stable identity, metadata, and provenance."""

    schema_version = SCHEMA_VERSION

    def __init__(
        self,
        name: str,
        entity_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        provenance: Provenance | None = None,
    ):
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("name must be a non-empty string")

        if entity_id is not None and (
            not isinstance(entity_id, str) or not entity_id.strip()
        ):
            raise ValidationError("entity_id must be a non-empty string or None")

        if metadata is not None and not isinstance(metadata, dict):
            raise ValidationError("metadata must be a dictionary or None")

        if provenance is not None and not isinstance(provenance, Provenance):
            raise ValidationError("provenance must be Provenance or None")

        self.id = entity_id.strip() if entity_id is not None else str(uuid4())
        self.name = name.strip()
        self.metadata = dict(metadata or {})
        self.provenance = provenance or Provenance()

    def get_name(self) -> str:
        return self.name

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "type": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "metadata": dict(self.metadata),
            "provenance": self.provenance.to_dict(),
        }

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id='{self.id}', name='{self.name}')"
        )


class Molecule(DomainEntity):
    """Base class for molecular domain objects."""

    @classmethod
    def from_dict(cls, data: dict):
        validate_schema_version(data)
        return cls(
            name=data["name"],
            entity_id=data.get("id"),
            metadata=data.get("metadata"),
            provenance=Provenance.from_dict(data.get("provenance")),
        )


class SequenceMolecule(Molecule):
    """Base class for molecules represented primarily by a sequence."""

    allow_empty_sequence = False

    def __init__(
        self,
        name: str,
        sequence: str,
        entity_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        provenance: Provenance | None = None,
    ):
        super().__init__(
            name=name,
            entity_id=entity_id,
            metadata=metadata,
            provenance=provenance,
        )

        if not isinstance(sequence, str):
            raise ValidationError("sequence must be a string")

        normalized_sequence = "".join(sequence.split()).upper()

        if not normalized_sequence and not self.allow_empty_sequence:
            raise ValidationError("sequence must be a non-empty string")

        self.sequence = normalized_sequence

    def get_sequence(self) -> str:
        return self.sequence

    def __len__(self) -> int:
        return len(self.sequence)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["sequence"] = self.sequence
        return data

    @classmethod
    def from_dict(cls, data: dict):
        validate_schema_version(data)
        return cls(
            name=data["name"],
            sequence=data["sequence"],
            entity_id=data.get("id"),
            metadata=data.get("metadata"),
            provenance=Provenance.from_dict(data.get("provenance")),
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id='{self.id}', name='{self.name}', length={len(self)})"
        )
