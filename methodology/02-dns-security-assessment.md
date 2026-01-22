# DNS Security Assessment

## Objective
To determine whether DNS queries
are encrypted or transmitted in plaintext.

---

## Methodology
- Identified system-configured DNS resolver
- Performed domain lookups using dig
- Captured traffic using tcpdump
- Observed transport protocol and visibility

---

## Findings
DNS traffic was transmitted over UDP port 53
without encryption.

Domain names and responses were clearly visible.

---

## Evidence
See: evidence/dns-plaintext-capture.txt

---

## Security Impact
Unencrypted DNS allows network operators
or attackers with network access to observe
browsing activity and user behavior patterns.
