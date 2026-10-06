import math

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight

from biomini import (
    DNA,
    RNA,
    Protein,
    ProteinAnalyzer,
    read_fasta,
)


def test_reverse_complement_matches_biopython():
    sequences = [
        "ATGCCG",
        "GATCGATGGGCCTATATAGGATCGAAAATCGC",
    ]

    for sequence in sequences:
        ours = DNA("dna", sequence).reverse_complement()
        reference = str(Seq(sequence).reverse_complement())
        assert ours == reference


def test_transcription_matches_biopython():
    sequences = [
        "ATGGCC",
        "ATGGCCTAATTT",
    ]

    for sequence in sequences:
        ours = DNA("dna", sequence).transcribe().sequence
        reference = str(Seq(sequence).transcribe())
        assert ours == reference


def test_translation_matches_biopython_to_first_stop():
    rna_sequences = [
        "AUGGCC",
        "AUGGCCUAAUUU",
        "AUGGCCA",  # incomplete terminal codon
    ]

    for sequence in rna_sequences:
        ours = RNA("rna", sequence).translate().sequence
        reference = str(Seq(sequence).translate(to_stop=True))
        assert ours == reference


def test_protein_molecular_weight_matches_biopython():
    protein_sequences = [
        "A",
        "ACDEFGHIK",
        "ACDEFGHIKLMNPQRSTVWY",
    ]

    for sequence in protein_sequences:
        ours = ProteinAnalyzer(
            Protein("protein", sequence)
        ).molecular_weight()

        reference = molecular_weight(
            Seq(sequence),
            seq_type="protein",
        )

        assert math.isclose(
            ours,
            reference,
            rel_tol=1e-9,
            abs_tol=1e-9,
        )


def test_fasta_parsing_matches_biopython(tmp_path):
    fasta = tmp_path / "reference.fasta"
    fasta.write_text(
        ">seq1 description one\n"
        "ACDE\n"
        "FGHIK\n"
        ">seq2 second description\n"
        "GGGAAA\n",
        encoding="utf-8",
    )

    ours = read_fasta(str(fasta))
    reference = list(SeqIO.parse(str(fasta), "fasta"))

    assert len(ours) == len(reference)

    for ours_record, ref_record in zip(ours, reference):
        assert ours_record.identifier == ref_record.id
        assert ours_record.sequence == str(ref_record.seq)
