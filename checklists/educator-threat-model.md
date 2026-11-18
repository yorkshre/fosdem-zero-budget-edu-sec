# Educator & School Threat Modeling Checklist (Zero-Budget Baseline)

A pragmatic checklist designed for teachers, school IT coordinators, and educational institutions operating without commercial security tooling.

## 1. Identity & Credential Hygiene
- [ ] **Unique Passwords:** Every school service (electronic gradebook, email, cloud drive) uses a unique password stored in an open-source password manager (**KeePassXC** or self-hosted **Vaultwarden**).
- [ ] **Phishing-Resistant Autofill:** Password manager browser extension is enabled so credentials are never autofilled on typosquatted/phishing domains.
- [ ] **Open-Source 2FA:** Two-factor authentication (TOTP) is enabled on all administrative, email, and gradebook accounts using open-source authenticators (**Aegis**, **Ente Auth**).
- [ ] **Recovery Codes:** Offline backup codes are printed or stored in an encrypted vault—never in plain text on a desktop or email draft.

## 2. Browser & Endpoint Hardening
- [ ] **HTTPS-Only Mode:** Enforced across all staff and lab workstations (`firefox/policies.json`).
- [ ] **Ad & Malvertising Blocking:** **uBlock Origin** deployed via browser policy to block malicious redirects and drive-by downloads.
- [ ] **Session Isolation:** **Firefox Multi-Account Containers** separates school administrative sessions from personal web browsing and social media.
- [ ] **Least Privilege:** Daily teaching workstations run without local administrator/root privileges.

## 3. Network & Domain Hygiene
- [ ] **DNS Filtering:** Local **Pi-hole** or **Unbound** filters known phishing and malware domains on the staff network.
- [ ] **Anti-Spoofing Records:** School domain has valid `SPF` and `DMARC` (`p=quarantine` or `p=reject`) DNS records verified via `scripts/school_domain_audit.py`.
- [ ] **TLS Monitoring:** School website enforces valid TLS certificates and HTTP security headers (`HSTS`, `X-Content-Type-Options`, `X-Frame-Options`).

## 4. Digital Privacy & Incident Response (First 15 Minutes)
- [ ] **Identity Separation:** Dedicated professional contact channels; personal phone numbers and private social accounts are decoupled from public school directories.
- [ ] **Compromise Playbook:** Staff know the exact 3 steps if a suspicious link is clicked:
  1. Disconnect from network / revoke active sessions.
  2. Rotate passwords from a clean device and verify 2FA tokens.
  3. Notify school IT coordinator and document evidence (screenshots, headers, URLs).
