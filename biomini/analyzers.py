from .core import SequenceMolecule
from .sequence import AminoAcid
from .features import FeatureSet


class SequenceAnalyzer:
    """Common analysis for any sequence molecule."""

    def __init__(
        self,
        molecule: SequenceMolecule,
    ):
        self.molecule = molecule

    def length(self) -> int:
        return len(self.molecule)

    def composition(self) -> dict[str, int]:
        counts = {}

        for code in self.molecule.sequence:
            counts[code] = (
                counts.get(code, 0)
                + 1
            )

        return counts

    def find_motif(
        self,
        motif: str,
    ) -> int:
        return (
            self.molecule.sequence
            .find(motif.upper())
        )


class NucleicAcidAnalyzer(
    SequenceAnalyzer
):
    """Analysis common to DNA and RNA."""

    def gc_content(self) -> float:
        sequence = self.molecule.sequence

        gc_count = (
            sequence.count("G")
            + sequence.count("C")
        )

        return gc_count / len(sequence)


class DNAAnalyzer(
    NucleicAcidAnalyzer
):
    pass


class RNAAnalyzer(
    NucleicAcidAnalyzer
):
    pass


class ProteinAnalyzer(
    SequenceAnalyzer
):
    """Protein-specific sequence analysis."""

    hydrophobic_codes = set(
        "AILMFWVY"
    )

    def amino_acid_composition(
        self
    ) -> dict[str, int]:
        return self.composition()

    def hydrophobic_fraction(
        self
    ) -> float:
        sequence = self.molecule.sequence

        count = sum(
            1
            for code in sequence
            if code in self.hydrophobic_codes
        )

        if not sequence:
            return 0.0

        return count / len(sequence)

    def molecular_weight(
        self
    ) -> float:
        if not self.molecule.amino_acids:
            return 0.0

        return 18.0153 + sum(
            amino_acid.get_mass()
            for amino_acid
            in self.molecule.amino_acids
        )

    def amino_acid_fraction_features(
        self
    ) -> dict[str, float]:
        sequence = self.molecule.sequence

        if not sequence:
            return {
                f"aa_{code}_fraction": 0.0
                for code in sorted(AminoAcid.acceptable_codes)
            }

        return {
            f"aa_{code}_fraction":
                sequence.count(code)
                / len(sequence)

            for code in sorted(
                AminoAcid.acceptable_codes
            )
        }

    def to_features(
        self
    ) -> FeatureSet:
        features = {
            "length":
                self.length(),

            "molecular_weight":
                self.molecular_weight(),

            "hydrophobic_fraction":
                self.hydrophobic_fraction(),
        }

        features.update(
            self.amino_acid_fraction_features()
        )

        return FeatureSet(
            self.molecule.name,
            features,
        )
