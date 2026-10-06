# GitHub Publication / Pre-Freeze Status

Status: **Public repository active — Phase I Pre-Freeze**

Repository:

```text
https://github.com/hk-yoon/biomini
```

## Completed

- repository created and public
- canonical package structure uploaded
- GitHub Actions workflow active
- hosted CI confirmed
- Python 3.10–3.13 CI matrix confirmed
- README / architecture / design / validation / roadmap documents present
- contribution and security documents present
- package version and dependency sources consolidated
- Phase I Completion Report present
- Canonical Audit A–F corrections completed
- Phase I educational Notebooks 01–08 completed
- notebook execution/consistency audit completed

## Current validation baseline

```text
pytest                    42 passed
coverage                  90%
compileall                PASS
wheel build               PASS
editable install          PASS
basic example             PASS
Biopython validation      PASS
GitHub Actions CI         PASS
Python 3.10–3.13          PASS
Notebook 01–08 execution  PASS
```

## Current Pre-Freeze work

Repository creation, notebook integration, documentation cleanup, post-integration
validation, and the final release audit are complete.

The remaining work is the freeze/release sequence:

1. apply the final **FROZEN** status update
2. confirm GitHub Actions CI on that exact release commit
3. create tag/release `v0.1.0-phase1`
4. declare **Phase I FROZEN**

## Release rule

Until the final audit and tag are complete, the correct project status is:

> **BioMini v0.1.0 — Phase I Pre-Freeze**

After the final release audit:

> **BioMini v0.1.0 — Phase I FROZEN**
