# Contributing to BioMini

BioMini is an educational scientific-software framework.

## Development setup

```bash
git clone https://github.com/hk-yoon/biomini.git
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

## Notebook changes

The learner-facing notebooks are educational reconstructions, not a second canonical
source tree.

When changing a notebook:

- preserve the learning progression;
- keep explanations consistent with the canonical package;
- execute the notebook end-to-end;
- update `notebooks/README.md` if the learning sequence changes.

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
