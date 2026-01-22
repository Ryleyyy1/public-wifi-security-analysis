# TLS Inspection

## Objective
To validate TLS version, cipher suite,
and certificate trust.

---

## Methodology
- Initiated TLS connections using OpenSSL
- Inspected handshake parameters
- Verified certificate chain

---

## Findings
- TLS Version: 1.3
- Cipher: AES_256_GCM_SHA384
- Certificate: Valid and trusted

---

## Conclusion
The TLS configuration follows
modern cryptographic best practices.
