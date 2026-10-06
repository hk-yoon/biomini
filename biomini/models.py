import pandas as pd
from .sequence import Protein
from .analyzers import ProteinAnalyzer


class ProteinPredictor:
    def __init__(self, model, feature_columns):
        self.model = model
        self.feature_columns = list(feature_columns)

    @classmethod
    def from_artifact(cls, artifact):
        return cls(artifact.model, artifact.feature_columns)

    def predict(self, protein: Protein) -> float:
        features = ProteinAnalyzer(protein).to_features().features
        X = pd.DataFrame([features])[self.feature_columns]
        return float(self.model.predict(X)[0])
