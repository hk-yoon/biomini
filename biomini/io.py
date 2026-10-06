from .errors import FastaFormatError, ValidationError
from .sequence import (
    DNA,
    RNA,
    Protein,
)


class FastaRecord:
    """Minimal representation of one FASTA record."""

    def __init__(
        self,
        identifier: str,
        sequence: str,
        description: str = "",
    ):
        self.identifier = identifier
        self.sequence = sequence
        self.description = description

    def __repr__(self) -> str:
        return (
            f"FastaRecord("
            f"identifier='{self.identifier}', "
            f"length={len(self.sequence)})"
        )


def read_fasta(
    path: str,
) -> list[FastaRecord]:

    records = []
    identifier = None
    description = ""
    sequence_parts = []

    def append_record():
        if identifier is not None:
            records.append(
                FastaRecord(
                    identifier,
                    "".join(sequence_parts),
                    description,
                )
            )

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                append_record()
                header = line[1:].strip()
                if not header:
                    raise FastaFormatError("FASTA header must not be empty")
                parts = header.split(maxsplit=1)
                identifier = parts[0]
                description = parts[1] if len(parts) > 1 else ""
                sequence_parts = []
            else:
                if identifier is None:
                    raise FastaFormatError("FASTA sequence found before first header")
                sequence_parts.append(line)

    append_record()
    return records

def read_sequence_fasta(
    path: str,
    sequence_class,
):
    records = read_fasta(path)

    return [
        sequence_class(
            record.identifier,
            record.sequence,
        )
        for record in records
    ]


def read_dna_fasta(
    path: str,
) -> list[DNA]:
    return read_sequence_fasta(
        path,
        DNA,
    )


def read_rna_fasta(
    path: str,
) -> list[RNA]:
    return read_sequence_fasta(
        path,
        RNA,
    )


def read_protein_fasta(
    path: str,
) -> list[Protein]:
    return read_sequence_fasta(
        path,
        Protein,
    )


def write_fasta(
    molecules,
    path: str,
    line_width: int = 60,
):
    if not isinstance(line_width, int) or isinstance(line_width, bool) or line_width <= 0:
        raise ValidationError("line_width must be a positive integer")

    with open(
        path,
        "w",
        encoding="utf-8",
    ) as file:

        for molecule in molecules:

            file.write(
                f">{molecule.name}\n"
            )

            sequence = (
                molecule.sequence
            )

            for i in range(
                0,
                len(sequence),
                line_width,
            ):
                file.write(
                    sequence[
                        i:i + line_width
                    ]
                    + "\n"
                )
