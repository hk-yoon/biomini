import pandas as pd

from .core import SCHEMA_VERSION, validate_schema_version
from .errors import DataError, ValidationError
from .features import Sample


class Dataset:
    schema_version = SCHEMA_VERSION

    def __init__(self):
        self.samples: list[Sample] = []

    def add(self, sample: Sample):
        if not isinstance(sample, Sample):
            raise ValidationError("dataset entries must be Sample objects")
        self.samples.append(sample)

    def __len__(self):
        return len(self.samples)

    def to_records(self):
        records = []
        for sample in self.samples:
            row = {
                "name": sample.feature_set.name,
                **sample.feature_set.features,
            }
            if sample.target is not None:
                row["target"] = sample.target
            records.append(row)
        return records

    def to_dataframe(self):
        return pd.DataFrame(self.to_records())

    def to_xy(self):
        df = self.to_dataframe()
        if "target" not in df.columns:
            raise DataError("dataset has no target")
        return df.drop(columns=["name", "target"]), df["target"]

    def to_dict(self):
        return {
            "schema_version": self.schema_version,
            "type": "Dataset",
            "samples": [s.to_dict() for s in self.samples],
        }

    @classmethod
    def from_dict(cls, data):
        validate_schema_version(data)
        obj = cls()
        for sample_data in data["samples"]:
            obj.add(Sample.from_dict(sample_data))
        return obj
