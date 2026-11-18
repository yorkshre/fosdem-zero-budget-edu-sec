#!/usr/bin/env python3
"""
Zero-Budget School Domain Hygiene & Security Auditor
Checks SPF, DMARC, TLS certificate validity, and essential HTTP security headers.
Usage: python3 school_domain_audit.py example-school.edu.pl
"""

import socket
import ssl
import sys
import urllib.request
from datetime import datetime, timezone

try:
    import dns.resolver
    HAS_DNSPYTHON = True
except ImportError:
    HAS_DNSPYTHON = False


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]


def check_dns_records(domain: str) -> None:
    print(f"\n[1/3] Checking Email Anti-Spoofing (SPF & DMARC) for {domain}...")
    if not HAS_DNSPYTHON:
        print("  [!] 'dnspython' not installed. Run: pip install dnspython")
        return

    # Check SPF
    try:
        txt_records = dns.resolver.resolve(domain, "TXT")
        spf = [r.to_text().strip('"') for r in txt_records if "v=spf1" in r.to_text()]
        if spf:
            print(f"  [+] SPF found: {spf[0]}")
        else:
            print("  [-] MISSING SPF record! Attackers can easily spoof school emails.")
    except Exception as e:
        print(f"  [-] SPF check failed: {e}")

    # Check DMARC
    try:
        dmarc_records = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")
        dmarc = [r.to_text().strip('"') for r in dmarc_records if "v=DMARC1" in r.to_text()]
        if dmarc:
            print(f"  [+] DMARC found: {dmarc[0]}")
            if "p=none" in dmarc[0]:
                print("      [!] Warning: DMARC policy is 'p=none' (monitoring only, not blocking).")
        else:
            print("  [-] MISSING DMARC record!")
    except Exception:
        print("  [-] MISSING DMARC record (_dmarc subdomain not found)!")


def check_tls(domain: str) -> None:
    print(f"\n[2/3] Checking TLS Certificate for {domain}...")
    ctx = ssl.create_default_context()
    try:
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                not_after = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
                days_left = (not_after - datetime.now(timezone.utc)).days
                print(f"  [+] Valid TLS certificate. Expires in {days_left} days ({not_after.date()}).")
    except Exception as e:
        print(f"  [-] TLS Error: {e}")


def check_http_headers(domain: str) -> None:
    print(f"\n[3/3] Checking HTTP Security Headers for https://{domain}...")
    req = urllib.request.Request(f"https://{domain}", headers={"User-Agent": "SchoolSecAudit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            headers = {k.lower(): v for k, v in resp.getheaders()}
            for h in SECURITY_HEADERS:
                val = headers.get(h.lower())
                if val:
                    print(f"  [+] {h}: {val[:60]}{'...' if len(val) > 60 else ''}")
                else:
                    print(f"  [-] Missing header: {h}")
    except Exception as e:
        print(f"  [-] HTTP request failed: {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 school_domain_audit.py <school-domain>")
        sys.exit(1)

    domain = sys.argv[1].replace("https://", "").replace("http://", "").strip("/")
    print(f"=== Zero-Budget School Domain Security Audit: {domain} ===")
    check_dns_records(domain)
    check_tls(domain)
    check_http_headers(domain)
    print("\nAudit complete.\n")


if __name__ == "__main__":
    main()
