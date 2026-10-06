# Contributing to BioMini

BioMini is currently an educational framework under active development.

## Development setup

```bash
git clone <repository-url>
cd biomini
python -m pip install -e ".[dev,validation]"
python -m pytest
```

## Contribution principles

Changes should preserve the project's educational and architectural goals.

Before proposing a change:

1. identify the scientific or educational responsibility being added;
2. avoid adding a class when a function or method is sufficient;
3. preserve separation between domain, analysis, representation, model, and I/O concerns;
4. add or update tests;
5. add scientific reference-validation when an independent reference is available;
6. update documentation when semantics or public APIs change.

## Tests

Run:

```bash
python -m pytest
python -m pytest --cov=biomini --cov-report=term-missing
```

## Scientific changes

A scientific result should not be considered correct merely because unit tests pass.
Where practical, compare with an independent established implementation or reference.

## Compatibility

Phase I public APIs should not be changed silently. Intentional breaking changes must be
documented in the changelog and associated with an appropriate version change.

## Pull requests

A useful pull request should explain:

- what problem it solves;
- why the change belongs in BioMini;
- whether biological semantics change;
- how it was tested;
- whether documentation was updated.
