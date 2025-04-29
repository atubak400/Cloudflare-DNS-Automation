# 🌐 Cloudflare DNS Automation & Security Enforcement

![waf](./waf.png)

Welcome to a **world-class DNS automation and security enforcement solution** using the Cloudflare API. This project was built step-by-step to enable DevOps-grade DNS management, security enforcement, and compliance monitoring — all through code.

---

## 🚀 Project Purpose

If you want to **automate DNS creation**, **secure your domain** with custom rules, and **monitor your records like a pro**, this project gives you the full foundation — from domain setup to reporting.

---

## 🧱 Technical Breakdown

### 🔹 What Is DNS?

DNS (Domain Name System) turns domain names (like `kingsleyatuba.it.com`) into IP addresses so browsers can find your website.

### 🔹 What Is an A Record?

An A record maps a domain or subdomain to an IP address (e.g., `gym.kingsleyatuba.it.com` → `192.0.2.1`).

### 🔹 What Is a CNAME Record?

CNAME points a subdomain to another domain (e.g., `www.kingsleyatuba.it.com` → `kingsleyatuba.it.com`).

### 🔹 What Is a WAF?

WAF (Web Application Firewall) protects your website from bots, hackers, and malicious traffic.

### 🔹 What Is Rate Limiting?

Rate limiting controls how many requests someone can make to your website in a short period — useful for blocking spam and DDoS attacks.

---

## ✅ What This Project Does

| Feature                    | Description                                                    |
| -------------------------- | -------------------------------------------------------------- |
| 🔐 **Secure DNS Setup**    | Full domain onboarding with API Token, zone ID, and account ID |
| ⚙️ **DNS Automation**      | Add and verify DNS A records via script                        |
| 🛡 **Security Enforcement** | WAF rule + rate limit setup (when plan supports it)            |
| 🔍 **Monitoring**          | Live DNS compliance checks against expected values             |
| 🧾 **Reporting**           | Snapshot saved as JSON to track all DNS records over time      |

---

## 🪜 Steps Taken to Build This Project

### 1️⃣ Cloudflare Setup

- Created domain: `kingsleyatuba.it.com`
- Added it to Cloudflare and updated nameservers
- Generated a scoped API token with correct permissions

### 2️⃣ DNS Automation

- Scripted DNS record listing (`dns_automation.py`)
- Created multiple A records for subdomains: music, gym, devops

### 3️⃣ Security Enforcement

- Attempted WAF & rate limiting setup (Free plan limited functionality)
- Script logs both successful and failed attempts to `waf_setup.log`

### 4️⃣ Monitoring

- `monitoring.py` checks all expected DNS records match the current state
- Results are printed and logged to `monitoring.log`

### 5️⃣ Reporting

- `report_dns_records.py` saves a timestamped JSON snapshot of all records

---

## 🧰 Technologies Used

- Python 3
- Cloudflare REST API (v4)
- YAML (for config)
- JSON (for reporting)
- Shell scripting
- Virtualenv

---

## 📁 Folder Structure

```
Cloudflare-DNS-Automation/
├── apply_waf_and_rate_limit.py     # WAF & rate limiting setup
├── create_a_records.py             # Create A records for all subdomains
├── dns_automation.py               # Pull and display all DNS records
├── monitoring.py                   # Validate DNS records against expectations
├── report_dns_records.py           # Save DNS snapshot to reports/
├── config.yaml                     # API token, zone ID, domain config
├── requirements.txt                # Python package list
├── logs/                           # Logs for WAF, monitoring, etc.
│   └── monitoring.log
│   └── waf_setup.log
├── reports/                        # JSON report history
├── setup_project.sh                # Shell script to create initial folder structure
└── README.md                       # 📄 This file
```

---

## ⚠️ Limitations

- WAF and Rate Limiting APIs require Cloudflare Pro or higher
- Make sure your API token is scoped to only your domain for security

---

## ✨ Future Improvements

- Integrate Slack/email alerts on DNS compliance failures
- Add GitHub Actions for scheduled monitoring
- Compare DNS snapshots to detect unauthorized changes

---

## 👨‍💻 Built With Care by Kingsley Atuba

This project reflects real-world DevOps thinking: infrastructure as code, API-first security, and full visibility into your DNS.

Ready to run your entire DNS pipeline from the terminal? This repo is your blueprint. 💡

---

**License:** MIT
