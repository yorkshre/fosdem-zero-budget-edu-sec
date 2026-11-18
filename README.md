# Zero-Budget Cybersecurity in Education: Protecting Teachers with Open-Source Tools

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![FOSS](https://img.shields.io/badge/100%25-FOSS-green.svg)]()

Companion repository and reproducible demo stack for the FOSDEM talk:
**"Zero-Budget Cybersecurity in Education: Protecting Teachers with Open-Source Tools"** by **Agata Skamruk**.

## Overview

Public schools and educators face enterprise-level cyber threats—credential harvesting, account takeovers, domain spoofing, and targeted online aggression—while operating on near-zero security budgets.

This repository provides a pragmatic, reproducible **Zero-Budget FOSS Defense Stack** designed to be deployed on existing school hardware with zero licensing costs.

## Repository Structure

```text
.
├── docker-compose.yml              # Vaultwarden + Pi-hole local defense stack
├── .env.example                    # Environment configuration template
├── requirements.txt                # Python dependencies for the audit CLI
├── firefox/
│   └── policies.json               # Hardened Firefox enterprise policy template
├── scripts/
│   └── school_domain_audit.py      # CLI auditor for SPF, DMARC, TLS & HTTP headers
├── checklists/
│   └── educator-threat-model.md    # Actionable security baseline for schools & staff
├── LICENSE                         # MIT License
└── README.md
```

---

## Quick Start

### 1. Deploy the Local Defense Stack (Vaultwarden + Pi-hole)

1. Clone this repository and configure your environment secrets:
   ```bash
   git clone https://github.com/<your-username>/fosdem-zero-budget-edu-sec.git
   cd fosdem-zero-budget-edu-sec
   cp .env.example .env
   ```
2. Edit `.env` and set strong random passwords/tokens (`openssl rand -base64 32`).
3. Start the services:
   ```bash
   docker compose up -d
   ```
4. Access the local interfaces (bound to `127.0.0.1` by default):
   - **Vaultwarden (Password Manager):** `http://localhost:8080`
   - **Pi-hole (DNS Sinkhole Admin):** `http://localhost:8081/admin`

### 2. Run the School Domain Hygiene Audit

Check whether a school domain is vulnerable to email spoofing (missing SPF/DMARC) or lacks basic web security headers:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 scripts/school_domain_audit.py example-school.edu.pl
```

### 3. Harden Staff & Lab Browsers (Mozilla Firefox)

Deploy `firefox/policies.json` to enforce HTTPS-Only mode, disable insecure built-in password storage, prevent DNS-over-HTTPS bypasses, and automatically install **uBlock Origin** and **Firefox Multi-Account Containers**:

- **Linux:**
  ```bash
  sudo mkdir -p /etc/firefox/policies
  sudo cp firefox/policies.json /etc/firefox/policies/policies.json
  ```
- **Windows:**
  Copy `firefox\policies.json` to `C:\Program Files\Mozilla Firefox\distribution\policies.json`
- **macOS:**
  Copy `firefox/policies.json` to `/Applications/Firefox.app/Contents/Resources/distribution/policies.json`

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
