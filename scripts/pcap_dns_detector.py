#!/usr/bin/env python3

import sys
from scapy.all import rdpcap, DNS, UDP

def analyze_pcap(pcap_file):
    packets = rdpcap(pcap_file)

    dns_queries = []
    dns_responses = []

    for pkt in packets:
        if pkt.haslayer(DNS) and pkt.haslayer(UDP):
            if pkt[DNS].qr == 0:
                dns_queries.append(pkt)
            elif pkt[DNS].qr == 1:
                dns_responses.append(pkt)

    return dns_queries, dns_responses

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 pcap_dns_detector.py <file.pcap>")
        sys.exit(1)

    pcap_file = sys.argv[1]
    print("=" * 50)
    print(" PCAP DNS PLAINTEXT LEAKAGE DETECTOR")
    print("=" * 50)

    try:
        queries, responses = analyze_pcap(pcap_file)
    except FileNotFoundError:
        print("[!] PCAP file not found")
        sys.exit(1)

    print(f"[+] DNS Queries Detected   : {len(queries)}")
    print(f"[+] DNS Responses Detected : {len(responses)}")

    if queries:
        print("\n[!] PLAINTEXT DNS ACTIVITY FOUND")
        print("[!] This indicates DNS traffic was not encrypted")
        print("\nSample Queried Domains:")

        shown = 0
        for q in queries:
            if shown >= 5:
                break
            try:
                domain = q[DNS].qd.qname.decode()
                print(f"  - {domain}")
                shown += 1
            except Exception:
                continue
    else:
        print("\n[+] No plaintext DNS detected")
        print("[+] DNS may be encrypted (DoH / DoT)")

    print("\nRisk Assessment:")
    if queries:
        print("- Metadata exposure possible")
        print("- User browsing activity visible")
    else:
        print("- Reduced DNS-based privacy risks")

if __name__ == "__main__":
    main()
