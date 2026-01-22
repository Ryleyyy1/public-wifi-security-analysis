# Technical Findings

## Finding 1: Plaintext DNS Traffic
- Severity: Medium
- Impact: Privacy Exposure

DNS queries and responses can be observed
by any entity with network-level access.

---

## Finding 2: HTTPS Enforcement
- Severity: Informational

Web traffic is protected through enforced HTTPS redirection.

---

## Finding 3: Strong TLS Configuration
- Severity: Informational

TLS 1.3 with modern cipher suites is in use,
reducing the risk of interception or downgrade attacks.
