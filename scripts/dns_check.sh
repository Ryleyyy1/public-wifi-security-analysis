#!/bin/bash

echo "====================================="
echo " Public WiFi DNS Security Checker"
echo "====================================="

DNS_SERVER=$(grep "nameserver" /etc/resolv.conf | head -n1 | awk '{print $2}')

if [[ -z "$DNS_SERVER" ]]; then
  echo "[!] DNS server not found"
  exit 1
fi

echo "[+] Detected DNS Server: $DNS_SERVER"
echo "[+] Testing DNS resolution..."

dig google.com @$DNS_SERVER +short > /dev/null

if [[ $? -eq 0 ]]; then
  echo "[+] DNS Resolution: SUCCESS"
else
  echo "[!] DNS Resolution: FAILED"
fi

echo
echo "[+] Checking for encrypted DNS support..."

if resolvectl status >/dev/null 2>&1; then
  resolvectl status | grep -i "DNSOverTLS"
else
  echo "[-] systemd-resolved not detected"
  echo "[-] Likely using plaintext DNS (UDP/53)"
fi

echo
echo "[+] Recommendation:"
echo "- Use VPN or DNS over HTTPS (DoH)"
echo "- Avoid sensitive browsing on public WiFi"
