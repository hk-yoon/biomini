import json
from dataclasses import dataclass, field
from datetime import datetime, timezone

import joblib

from .core import SCHEMA_VERSION, validate_schema_version
from .dataset import Dataset
from .errors import ModelPersistenceError, SerializationError
from .features import FeatureSet, Sample
from .logging_utils import get_logger
from .sequence import DNA, RNA, Protein

logger = get_logger("persistence")

SERIALIZABLE_TYPES = {
    "DNA": DNA,
    "RNA": RNA,
    "Protein": Protein,
    "FeatureSet": FeatureSet,
    "Sample": Sample,
    "Dataset": Dataset,
}


def save_json(obj, path: str):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(obj.to_dict(), file, indent=2)
        logger.debug("Saved %s to %s", obj.__class__.__name__, path)
    except (OSError, TypeError) as exc:
        raise SerializationError(f"could not save JSON to {path}") from exc


def load_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise SerializationError(f"could not load JSON from {path}") from exc

    validate_schema_version(data)

    object_type = data.get("type")
    if object_type not in SERIALIZABLE_TYPES:
        raise SerializationError(
            f"unsupported serialized type: {object_type}"
        )

    try:
        obj = SERIALIZABLE_TYPES[object_type].from_dict(data)
    except (KeyError, TypeError, ValueError) as exc:
        raise SerializationError(
            f"invalid serialized {object_type} payload"
        ) from exc

    logger.debug("Loaded %s from %s", object_type, path)
    return obj


@dataclass
class ModelArtifact:
    model: object
    feature_columns: list[str]
    model_name: str
    target_name: str
    metadata: dict = field(default_factory=dict)
    schema_version: str = SCHEMA_VERSION
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


def save_model_artifact(artifact: ModelArtifact, path: str):
    if artifact.schema_version != SCHEMA_VERSION:
        raise ModelPersistenceError(
            f"unsupported model artifact schema_version: {artifact.schema_version}"
        )
    try:
        joblib.dump(artifact, path)
        logger.debug("Saved model artifact %s to %s", artifact.model_name, path)
    except Exception as exc:
        raise ModelPersistenceError(
            f"could not save model artifact to {path}"
        ) from exc


def load_model_artifact(path: str) -> ModelArtifact:
    try:
        artifact = joblib.load(path)
    except Exception as exc:
        raise ModelPersistenceError(
            f"could not load model artifact from {path}"
        ) from exc

    if not isinstance(artifact, ModelArtifact):
        raise ModelPersistenceError("file does not contain a ModelArtifact")

    if artifact.schema_version != SCHEMA_VERSION:
        raise ModelPersistenceError(
            f"unsupported model artifact schema_version: {artifact.schema_version}"
        )

    logger.debug("Loaded model artifact %s from %s", artifact.model_name, path)
    return artifact
