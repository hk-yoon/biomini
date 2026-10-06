from __future__ import annotations

from typing import Any

from .core import Provenance, SequenceMolecule
from .errors import ValidationError


class AminoAcid:
    """Represent a single amino-acid residue."""

    # Average residue masses (free amino-acid average mass minus H2O).
    # Values aligned with Biopython/IUPACData average protein weights.
    mass_dict = {
        "A": 71.0779, "R": 156.1857, "N": 114.1026, "D": 115.0874,
        "C": 103.1429, "Q": 128.1292, "E": 129.1140, "G": 57.0513,
        "H": 137.1393, "I": 113.1576, "L": 113.1576, "K": 128.1723,
        "M": 131.1960, "F": 147.1738, "P": 97.1152, "S": 87.0773,
        "T": 101.1039, "W": 186.2099, "Y": 163.1732, "V": 99.1310,
    }
    acceptable_codes = set(mass_dict.keys())

    def __init__(self, code: str):
        code = code.upper()
        if code not in self.acceptable_codes:
            raise ValidationError(f"invalid amino acid: {code}")
        self.code = code

    def get_mass(self) -> float:
        return self.mass_dict[self.code]

    def __repr__(self) -> str:
        return f"AminoAcid(code='{self.code}')"


class NucleicAcid(SequenceMolecule):
    """Base class for nucleic-acid sequences."""


class DNA(NucleicAcid):
    """Represent a canonical DNA sequence."""

    valid_codes = set("ATGC")

    def __init__(
        self,
        name: str,
        sequence: str,
        entity_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        provenance: Provenance | None = None,
    ):
        super().__init__(name, sequence, entity_id, metadata, provenance)
        self._validate_sequence()

    def _validate_sequence(self):
        invalid_codes = set(self.sequence) - self.valid_codes
        if invalid_codes:
            raise ValidationError(
                f"invalid DNA code(s): {sorted(invalid_codes)}"
            )

    def complement(self) -> str:
        table = str.maketrans("ATGC", "TACG")
        return self.sequence.translate(table)

    def reverse_complement(self) -> str:
        return self.complement()[::-1]

    def transcribe(self):
        return RNA(
            self.name + "_RNA",
            self.sequence.replace("T", "U"),
            metadata=self.metadata,
            provenance=Provenance(
                source="transcription",
                parent_ids=[self.id],
            ),
        )


class RNA(NucleicAcid):
    """Represent a canonical RNA sequence."""

    valid_codes = set("AUGC")
    codon_table = {
        "UUU":"F","UUC":"F","UUA":"L","UUG":"L",
        "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
        "UAU":"Y","UAC":"Y","UAA":"*","UAG":"*",
        "UGU":"C","UGC":"C","UGA":"*","UGG":"W",
        "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
        "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
        "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
        "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
        "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
        "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
        "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
        "AGU":"S","AGC":"S","AGA":"R","AGG":"R",
        "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
        "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
        "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
        "GGU":"G","GGC":"G","GGA":"G","GGG":"G",
    }

    def __init__(
        self,
        name: str,
        sequence: str,
        entity_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        provenance: Provenance | None = None,
    ):
        super().__init__(name, sequence, entity_id, metadata, provenance)
        self._validate_sequence()

    def _validate_sequence(self):
        invalid_codes = set(self.sequence) - self.valid_codes
        if invalid_codes:
            raise ValidationError(
                f"invalid RNA code(s): {sorted(invalid_codes)}"
            )

    def translate(self):
        protein_sequence = []
        for i in range(0, len(self.sequence) - 2, 3):
            amino_acid = self.codon_table[self.sequence[i:i + 3]]
            if amino_acid == "*":
                break
            protein_sequence.append(amino_acid)

        return Protein(
            self.name + "_protein",
            "".join(protein_sequence),
            metadata=self.metadata,
            provenance=Provenance(
                source="translation",
                parent_ids=[self.id],
            ),
        )


class Protein(SequenceMolecule):
    """Represent a canonical protein sequence, including an empty translation product."""

    allow_empty_sequence = True
    valid_codes = AminoAcid.acceptable_codes

    def __init__(
        self,
        name: str,
        sequence: str,
        entity_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        provenance: Provenance | None = None,
    ):
        super().__init__(name, sequence, entity_id, metadata, provenance)
        self._validate_sequence()
        self.amino_acids = [AminoAcid(code) for code in self.sequence]

    def _validate_sequence(self):
        invalid_codes = set(self.sequence) - self.valid_codes
        if invalid_codes:
            raise ValidationError(
                f"invalid protein code(s): {sorted(invalid_codes)}"
            )

    def get_amino_acids(self):
        return self.amino_acids
