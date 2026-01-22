# HTTP and HTTPS Analysis

## Objective
To verify whether websites enforce HTTPS
when accessed over unsecured networks.

---

## Methodology
- Performed HTTP requests using curl
- Observed response headers and redirections

---

## Findings
HTTP requests were redirected to HTTPS
using HTTP 301 (Moved Permanently).

---

## Security Impact
HTTPS enforcement prevents plaintext
transmission of sensitive web traffic.
