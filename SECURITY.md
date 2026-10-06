# Security Policy

## Model artifacts

BioMini uses `joblib` for model persistence.

`joblib` is pickle-based and loading a malicious or untrusted artifact can execute
arbitrary code.

**Only load BioMini model artifacts from trusted sources.**

Do not accept uploaded `.joblib`, `.pkl`, or similar artifacts from unknown users and
load them in a privileged environment.

## Reporting

For the current educational project, security issues should be reported privately to the
repository maintainer. Do not publish exploit details or malicious artifact examples in a
public issue before the maintainer has had an opportunity to assess the report.
