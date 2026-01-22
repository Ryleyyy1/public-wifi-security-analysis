# Public WiFi Security Reality Check

This repository documents a real-world security assessment
performed on a public WiFi network commonly found in cafés
and shared public spaces.

The assessment evaluates how secure daily internet usage
actually is when connected to untrusted wireless networks,
with a focus on DNS privacy, HTTPS enforcement, and TLS security.

---

## Objectives

The objectives of this project are to:

- Evaluate whether DNS traffic is encrypted or exposed
- Verify HTTP to HTTPS redirection behavior
- Inspect TLS versions, cipher suites, and certificate validity
- Assess practical risks faced by everyday users on public WiFi

---

## Assessment Scope

- Passive network observation only
- No exploitation or active attacks
- No credential harvesting
- No interaction with other users' traffic

All testing was conducted solely on the author's own device.

---

## High-Level Results

| Security Area | Result |
|---|---|
| WiFi Encryption | WPA-based |
| DNS Encryption | ❌ Not Encrypted |
| HTTPS Enforcement | ✔ Enabled |
| TLS Version | ✔ TLS 1.3 |
| Certificate Trust | ✔ Valid |

---

## Overall Risk Rating

**MODERATE**

While HTTPS and TLS are properly implemented,
DNS-level metadata remains exposed on public networks.

---

## Key Conclusion

Using HTTPS alone does not guarantee privacy
on public WiFi networks. DNS traffic can still
reveal browsing behavior and user activity patterns.

---

## Intended Audience

- Cybersecurity students
- Junior SOC / Blue Team analysts
- Security awareness educators
- Entry-level penetration testers

---

## Disclaimer

This project is provided for educational
and defensive security awareness purposes only.
