---
name: semgrep-security-guardian
description: >
  Static Application Security Testing (SAST), vulnerability auditing, OWASP Top 10 rule enforcement, and pre-commit secret scanning via Semgrep.
  Use when: audit code for security vulnerabilities, scan Python or TypeScript codebases, detect SQL injection, prevent hardcoded secrets,
  verify security compliance before client delivery, or run automated SAST checks.
compatibility: Requires semgrep CLI (pip install semgrep).
---

# Semgrep Security Guardian 🛡️

Automated Static Application Security Testing (SAST) and enterprise vulnerability engine for Python, TypeScript, Go, and Dockerfiles.

Guarantees 100% adherence to **Jasper Pillar 7 (Zero-Secret-Leakage)** and produces official security compliance reports to win enterprise client trust.

---

## ⚡ Core CLI Commands Reference

| Command | Action | Description |
| :--- | :--- | :--- |
| `semgrep scan --config auto` | Auto Security Scan | Runs Semgrep registry rules tailored to detected languages. |
| `semgrep scan --config "p/owasp-top-ten"` | OWASP Top 10 | Checks for injection, broken auth, SSRF, XSS, and security misconfigs. |
| `semgrep scan --config "p/secrets"` | Secret Detection | Scans for leaked API keys, tokens, private keys, and database URLs. |
| `semgrep scan --config "p/python"` | Python Security | Audits FastAPI/Django/Flask for unsafe deserialization, shell calls, SQLi. |
| `semgrep scan --config "p/typescript"` | TypeScript Audit | Audits Next.js/React/Node for DOM XSS, prototype pollution, unsafe evals. |
| `semgrep scan --json -o report.json` | Export Audit Report | Exports JSON vulnerability report for automated client deliverables. |

---

## 🎯 Pre-Commit & Pre-Deploy Client Security Gate

Run before any release, pull request, or client project handoff:

```bash
# 1. Fast local pre-commit audit
semgrep scan --config "p/security-audit" --config "p/secrets"

# 2. Strict Zero-Tolerance check (exit with code 1 if ERROR found)
semgrep scan --error --config auto
```

---

## 🛡️ Custom Rules for Jasper Standards (`.semgrep.yml`)

Place in project root to enforce Jasper architecture standards:

```yaml
rules:
  - id: jasper-hardcoded-bot-token
    patterns:
      - pattern-regex: '\b[0-9]{8,10}:[a-zA-Z0-9_-]{35}\b'
    message: "CRITICAL: Hardcoded Telegram Bot Token detected! Use .env and os.getenv('BOT_TOKEN')."
    languages: [python, javascript, typescript]
    severity: ERROR

  - id: jasper-raw-sql-injection-risk
    patterns:
      - pattern: db.execute(f"...")
    message: "WARNING: Direct f-string in SQL execution detected. Use parameterized queries or SQLAlchemy/Prisma models."
    languages: [python]
    severity: WARNING
```

---

## 🏆 Client Acquisition Advantage: Security Audit Certification

Enterprise and Fintech clients prioritize security above all else. Generate an instant audit summary with Semgrep:

```bash
semgrep scan --config "p/owasp-top-ten" --json | jq '{findings: .results | length, errors: .errors | length}'
```
Presenting a verified **Zero-Vulnerability Semgrep Certificate** in client proposals increases contract closing rates significantly!
