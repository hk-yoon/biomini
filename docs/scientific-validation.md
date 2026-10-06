# Scientific Validation — Phase I

## Purpose

Unit tests can show that software behaves consistently with its own specification.
Scientific software needs an additional question:

> Does the implemented scientific behavior agree with an independent reference?

Phase I therefore cross-validates selected BioMini operations against Biopython.

## Reference areas

### Reverse complement

BioMini:

```python
DNA("dna", sequence).reverse_complement()
```

Reference:

```python
Seq(sequence).reverse_complement()
```

### Transcription

BioMini:

```python
DNA("dna", sequence).transcribe()
```

Reference:

```python
Seq(sequence).transcribe()
```

### Translation

BioMini translation is compared against:

```python
Seq(rna_sequence).translate(to_stop=True)
```

within the explicitly documented Phase I semantics.

### Protein molecular weight

BioMini protein molecular weight is compared against Biopython's average molecular-weight
calculation.

The reference comparison identified that the original educational residue masses were
rounded too aggressively. Phase I corrected those values to align with the selected
reference convention.

### FASTA parsing

BioMini's minimal FASTA parser is compared with Biopython `SeqIO` for supported records.

## Current result

At the current Phase I Pre-Freeze baseline:

```text
42 tests passed
90% line coverage
Biopython reference-validation PASS
```

## Deliberate limitations

Reference agreement is not the same as broad biological validation.

Phase I does not validate or support:

- ambiguous IUPAC sequence alphabets
- alternate genetic codes
- ORF discovery
- genome annotations
- alignment
- structural biology
- chemistry graph semantics
- experimental measurement uncertainty

Those capabilities require separate domain models, external libraries, or later project
phases.

## Incomplete terminal codons

BioMini currently ignores an incomplete terminal codon during translation.

Biopython currently emits a warning for this case. The test deliberately exercises that
difference in strictness while confirming the translated product used by BioMini.

This policy should be revisited if the selected reference library changes behavior in a
future release.
