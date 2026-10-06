from math import isfinite
from numbers import Real

from .core import SCHEMA_VERSION, validate_schema_version
from .errors import ValidationError


class FeatureSet:
    schema_version = SCHEMA_VERSION

    def __init__(self, name: str, features: dict[str, float]):
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("FeatureSet name must be a non-empty string")
        if not isinstance(features, dict) or not features:
            raise ValidationError("features must be a non-empty dictionary")

        normalized_features = {}
        for key, value in features.items():
            if not isinstance(key, str) or not key.strip():
                raise ValidationError("feature names must be non-empty strings")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise ValidationError(f"feature {key!r} must be numeric")
            numeric_value = float(value)
            if not isfinite(numeric_value):
                raise ValidationError(f"feature {key!r} must be finite")
            normalized_features[key.strip()] = numeric_value

        self.name = name.strip()
        self.features = normalized_features

    def get(self, feature_name: str):
        return self.features[feature_name]

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "type": "FeatureSet",
            "name": self.name,
            "features": dict(self.features),
        }

    @classmethod
    def from_dict(cls, data: dict):
        validate_schema_version(data)
        return cls(data["name"], dict(data["features"]))

    def __repr__(self) -> str:
        return f"FeatureSet(name='{self.name}', features={self.features})"


class Sample:
    schema_version = SCHEMA_VERSION

    def __init__(self, feature_set: FeatureSet, target=None):
        if not isinstance(feature_set, FeatureSet):
            raise ValidationError("feature_set must be a FeatureSet")
        self.feature_set = feature_set
        self.target = target

    def to_dict(self) -> dict:
        return {
            "schema_version": self.schema_version,
            "type": "Sample",
            "feature_set": self.feature_set.to_dict(),
            "target": self.target,
        }

    @classmethod
    def from_dict(cls, data: dict):
        validate_schema_version(data)
        return cls(
            FeatureSet.from_dict(data["feature_set"]),
            target=data.get("target"),
        )
