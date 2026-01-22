# PCAP Traffic Analysis

## Objective
To analyze captured network traffic
and identify unencrypted DNS activity.

## Methodology
- Captured traffic using tcpdump
- Analyzed PCAP using custom Python script
- Filtered DNS over UDP packets

## Findings
Plaintext DNS queries were identified,
confirming lack of DNS encryption
on the public WiFi network.

## Impact
DNS-level metadata exposure increases
privacy and profiling risks.
