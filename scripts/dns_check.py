import subprocess
import socket

print("=" * 45)
print(" Public WiFi DNS Security Checker")
print("=" * 45)

def get_dns_server():
    try:
        with open("/etc/resolv.conf", "r") as f:
            for line in f:
                if line.startswith("nameserver"):
                    return line.split()[1]
    except Exception:
        return None

def test_dns_resolution(dns_server):
    try:
        result = subprocess.run(
            ["dig", "google.com", f"@{dns_server}", "+short"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def check_doh():
    try:
        socket.getaddrinfo("cloudflare-dns.com", 443)
        return True
    except Exception:
        return False

dns = get_dns_server()

if not dns:
    print("[!] DNS server not detected")
    exit(1)

print(f"[+] DNS Server Detected : {dns}")

if test_dns_resolution(dns):
    print("[+] DNS Resolution      : SUCCESS")
else:
    print("[!] DNS Resolution      : FAILED")

print()
print("[+] Encrypted DNS Check:")

if check_doh():
    print("[+] DoH-capable resolver reachable")
    print("[-] Active DNS encryption not guaranteed")
else:
    print("[!] DoH resolver unreachable")

print()
print("[!] Risk Assessment:")
print("- DNS queries may be exposed on public WiFi")
print("- Browsing metadata can be monitored")
print()
print("[+] Recommendation:")
print("- Enable DNS over HTTPS (DoH)")
print("- Use VPN on public networks")
