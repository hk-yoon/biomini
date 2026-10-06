# Security Policy

## Model artifacts

BioMini uses `joblib` for model persistence.

`joblib` is pickle-based and loading a malicious or untrusted artifact can execute
arbitrary code.

**Only load BioMini model artifacts from trusted sources.**

Do not accept uploaded `.joblib`, `.pkl`, or similar artifacts from unknown users and
load them in a privileged environment.

## Reporting

For the current educational release-candidate stage, security reports should be sent
privately to the repository maintainer rather than disclosed through a public issue.

A public security contact can be added when the repository ownership/contact information
is finalized.
