## PCAP DNS Leakage Detector

pcap_dns_detector.py analyzes packet capture (PCAP) files
to detect plaintext DNS traffic over UDP port 53.

### Purpose
- Identify DNS privacy leaks
- Support forensic & SOC investigations
- Validate public WiFi DNS security posture

### Example Use Case
Analyzing a packet capture recorded
while connected to a public WiFi network
to verify DNS encryption usage.

### Warning
Only analyze PCAP files that you legally own
or have permission to inspect.
