import biomini


def test_version():
    assert biomini.__version__ == "0.1.0"


def test_public_api_smoke():
    dna = biomini.DNA(
        "gene",
        "ATGGCC",
    )

    protein = (
        dna
        .transcribe()
        .translate()
    )

    analyzer = biomini.ProteinAnalyzer(
        protein
    )

    assert protein.sequence == "MA"
    assert analyzer.molecular_weight() > 0
