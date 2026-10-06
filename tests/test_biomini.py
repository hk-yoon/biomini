import math

import pytest

from biomini import (
    DNA,
    RNA,
    Protein,
    DNAAnalyzer,
    RNAAnalyzer,
    ProteinAnalyzer,
    read_fasta,
    read_protein_fasta,
    write_fasta,
)


def test_dna_normalization_and_validation():

    dna = DNA(
        "gene",
        "atgc",
    )

    assert dna.sequence == "ATGC"

    with pytest.raises(
        ValueError
    ):
        DNA(
            "bad",
            "ATGX",
        )


def test_dna_complement_and_reverse_complement():

    dna = DNA(
        "gene",
        "ATGCCG",
    )

    assert (
        dna.complement()
        == "TACGGC"
    )

    assert (
        dna.reverse_complement()
        == "CGGCAT"
    )


def test_transcription():

    dna = DNA(
        "gene",
        "ATGGCC",
    )

    rna = dna.transcribe()

    assert isinstance(
        rna,
        RNA,
    )

    assert (
        rna.sequence
        == "AUGGCC"
    )


def test_translation_and_stop_codon():

    rna = RNA(
        "rna",
        "AUGGCCUAAUUU",
    )

    protein = (
        rna.translate()
    )

    assert isinstance(
        protein,
        Protein,
    )

    assert (
        protein.sequence
        == "MA"
    )


def test_translation_ignores_incomplete_final_codon():

    rna = RNA(
        "rna",
        "AUGGCCA",
    )

    protein = (
        rna.translate()
    )

    assert (
        protein.sequence
        == "MA"
    )


def test_gc_content():

    dna = DNA(
        "gene",
        "ATGCGC",
    )

    assert math.isclose(
        DNAAnalyzer(
            dna
        ).gc_content(),
        4 / 6,
    )

    rna = RNA(
        "rna",
        "AUGCGC",
    )

    assert math.isclose(
        RNAAnalyzer(
            rna
        ).gc_content(),
        4 / 6,
    )


def test_sequence_analysis():

    dna = DNA(
        "gene",
        "ATGCGCAA",
    )

    analyzer = DNAAnalyzer(
        dna
    )

    assert analyzer.length() == 8

    assert analyzer.composition() == {
        "A": 3,
        "T": 1,
        "G": 2,
        "C": 2,
    }

    assert (
        analyzer.find_motif(
            "GCG"
        )
        == 2
    )

    assert (
        analyzer.find_motif(
            "TTT"
        )
        == -1
    )


def test_protein_mass_single_alanine():

    protein = Protein(
        "p",
        "A",
    )

    # Alanine residue 71.07
    # + terminal water 18.02
    # = 89.09

    assert math.isclose(
        ProteinAnalyzer(
            protein
        ).molecular_weight(),
        89.0932,
        rel_tol=1e-9,
        abs_tol=1e-9,
    )


def test_protein_hydrophobic_fraction():

    protein = Protein(
        "p",
        "AILMGST",
    )

    assert math.isclose(
        ProteinAnalyzer(
            protein
        ).hydrophobic_fraction(),
        4 / 7,
    )


def test_feature_fractions_sum_to_one():

    protein = Protein(
        "p",
        "ACDEFGHIKLMNPQRSTVWY",
    )

    features = (
        ProteinAnalyzer(
            protein
        )
        .to_features()
        .features
    )

    fraction_sum = sum(
        value
        for key, value
        in features.items()
        if (
            key.startswith("aa_")
            and key.endswith(
                "_fraction"
            )
        )
    )

    assert math.isclose(
        fraction_sum,
        1.0,
    )


def test_read_multiline_fasta(
    tmp_path,
):

    fasta = (
        tmp_path
        / "proteins.fasta"
    )

    fasta.write_text(
        ">p1\n"
        "ACD\n"
        "EFG\n"
        "\n"
        ">p2\n"
        "GGGAAA\n",
        encoding="utf-8",
    )

    records = read_fasta(
        str(fasta)
    )

    assert len(records) == 2

    assert (
        records[0].identifier
        == "p1"
    )

    assert (
        records[0].sequence
        == "ACDEFG"
    )

    assert (
        records[1].sequence
        == "GGGAAA"
    )


def test_read_protein_fasta(
    tmp_path,
):

    fasta = (
        tmp_path
        / "proteins.fasta"
    )

    fasta.write_text(
        ">p1\n"
        "ACDE\n"
        ">p2\n"
        "GGGA\n",
        encoding="utf-8",
    )

    proteins = (
        read_protein_fasta(
            str(fasta)
        )
    )

    assert [
        p.name
        for p in proteins
    ] == [
        "p1",
        "p2",
    ]

    assert [
        p.sequence
        for p in proteins
    ] == [
        "ACDE",
        "GGGA",
    ]


def test_fasta_round_trip(
    tmp_path,
):

    proteins = [
        Protein(
            "p1",
            "ACDEFG",
        ),

        Protein(
            "p2",
            "GGGAAA",
        ),
    ]

    fasta = (
        tmp_path
        / "roundtrip.fasta"
    )

    write_fasta(
        proteins,
        str(fasta),
        line_width=3,
    )

    loaded = (
        read_protein_fasta(
            str(fasta)
        )
    )

    assert [
        (
            p.name,
            p.sequence,
        )
        for p in loaded
    ] == [
        (
            "p1",
            "ACDEFG",
        ),
        (
            "p2",
            "GGGAAA",
        ),
    ]
