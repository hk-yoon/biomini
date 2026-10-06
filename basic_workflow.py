from biomini import (
    DNA,
    DNAAnalyzer,
    ProteinAnalyzer,
)


dna = DNA(
    "gene1",
    "ATGGCCTTT",
)

print(
    "DNA:",
    dna,
)

dna_analyzer = DNAAnalyzer(
    dna
)

print(
    "GC content:",
    dna_analyzer.gc_content(),
)

rna = dna.transcribe()

print(
    "RNA:",
    rna,
)

protein = rna.translate()

print(
    "Protein:",
    protein,
)

protein_analyzer = (
    ProteinAnalyzer(
        protein
    )
)

print(
    "Molecular weight:",
    protein_analyzer
    .molecular_weight(),
)

print(
    "Hydrophobic fraction:",
    protein_analyzer
    .hydrophobic_fraction(),
)
