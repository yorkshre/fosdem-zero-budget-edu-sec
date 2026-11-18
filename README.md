# Zero-Budget Cybersecurity in Education — Demo Stack

Files prepared for the FOSDEM presentation:
**Zero-Budget Cybersecurity in Education: Protecting Teachers with Open-Source Tools**

## Included Files
1. `docker-compose.yml` — Local, zero-cost deployment of **Vaultwarden** (password manager) and **Pi-hole** (DNS-level phishing/malware filtering).
2. `school_domain_audit.py` — Lightweight Python CLI script to check SPF, DMARC, TLS, and HTTP security headers on a school domain.
3. `policies.json` — Enterprise policy template for Mozilla Firefox (enforces HTTPS-Only, disables built-in insecure password saving, blocks DoH bypasses, and auto-installs uBlock Origin + Multi-Account Containers).

## Quick Start (Offline / Local Demo)
```bash
docker compose up -d
```
- Vaultwarden UI: `http://localhost:8080`
- Pi-hole Admin UI: `http://localhost:8081/admin`

## Firefox Policy Deployment
- **Linux:** Copy `policies.json` to `/etc/firefox/policies/policies.json`
- **Windows:** Copy `policies.json` to `C:\Program Files\Mozilla Firefox\distribution\policies.json`
- **macOS:** Copy `policies.json` to `/Applications/Firefox.app/Contents/Resources/distribution/policies.json`
