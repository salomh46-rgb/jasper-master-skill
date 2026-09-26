---
name: jasper-plugin-customizer
description: >
  Customize, adapt, and configure any Claude Code, Cowork, or Antigravity plugin/skill for
  Javohirbek Asqarov's (Jasper) ecosystem, projects, and workflows. Use when: customize plugin,
  adapt skill, tailor plugin, configure plugin connectors, connect MCP servers to skill,
  replace ~~ placeholders, tweak skill settings, or package .plugin for Jasper production.
compatibility: Antigravity IDE, VS Code, Claude Code CLI, and Cowork environments.
---

# Jasper Plugin & Skill Customizer 🚀

Transform any generic, open-source, or third-party AI plugin/skill into a production-grade asset specifically tailored for Jasper's systems (`D:\ALLProjects`, VPS `62.171.143.55`, Telegram Bots, Supabase, and Jasper Production Standards).

---

## 🎯 When to Activate This Skill
- When importing a new skill or plugin from Anthropic Plugin Directory, GitHub, or community repos.
- When adapting generic workflow templates containing `~~`-prefixed placeholders (e.g. `~~Jira`, `~~channel`, `~~api-url`).
- When a plugin needs Model Context Protocol (MCP) server bindings (Chrome DevTools, PostHog, GitHub, Supabase, Vault).
- When tailoring an external skill to comply with **Jasper Production Standards (Pillars 1–10)**.

---

## 🧠 Core Execution Phases

### Phase 0: Intent & Target Identification
1. **Identify the Target Plugin/Skill**:
   - Locate the target directory (e.g., in `.agents/skills/`, `.plugins/`, or downloaded directory).
   - Read `SKILL.md`, `plugin.json`, or root configurations to understand its intent and tools.
2. **Scan for Placeholders**:
   - Run scan for template variables: `grep -rn '~~\w' /path/to/plugin`
   - Classify mode:
     - **Mode A (Generic Setup)**: Template contains `~~` variables needing Jasper concrete bindings.
     - **Mode B (Scoped Customization)**: Adjust specific connectors, prompt guidelines, or tools.
     - **Mode C (General Refactoring)**: Modernize the plugin for Antigravity & Senior standards.

---

### Phase 1: Context Extraction from Jasper Brain Anchors
Extract live production endpoints, credentials conventions, and system parameters from:
- `PROJECT_CONTEXT.md` (Active projects: Voice2Deal, DentaMed CRM, UzPayment, OmniStore)
- `INFRASTRUCTURE_REGISTRY.md` (VPS: `62.171.143.55`, Coolify v4.3.21, Docker containers, ports)
- **Standard Defaults for Jasper**:
  - **Timezone**: `Asia/Tashkent` (UTC+5)
  - **Currency Engine**: UZS / Tiyin (100x conversion)
  - **Telegram Bot Handlers**: Aiogram 3.x with HMAC / InitData verification
  - **API Routing**: Relative `/api` prefix (Zero CORS issues)
  - **DevOps Runtime**: Docker, Ubuntu LTS on Hetzner Cloud

---

### Phase 2: Surgical Replacement & Customization
Replace all abstract placeholders with verified Jasper ecosystem parameters:

| Generic Placeholder | Jasper Production Binding | Purpose |
| :--- | :--- | :--- |
| `~~Jira` / `~~IssueTracker` | GitHub Issues / Project Board / Telegram CRM | Task & bug tracking |
| `~~SlackChannel` | Telegram Alert Channel (`@Ovozli_SavdoBOT` logs) | Operational alerts |
| `~~BaseApiUrl` | Relative `/api` or `http://62.171.143.55:<PORT>` | Secure internal networking |
| `~~AuthMechanism` | Supabase JWT / Telegram InitData HMAC | Production authentication |
| `~~Database` | PostgreSQL Multi-Tenant / SQLite WAL | Zero-leak data layer |

> **Surgical Rule**: Never destroy the core functional logic of the original skill. Modify only configuration parameters, references, and tool mappings.

---

### Phase 3: MCP Server Discovery & Binding
Detect what external capabilities the plugin requires and bind appropriate MCP servers:

1. **Browser / Frontend Inspection** ➔ Bind `chrome-devtools-mcp`
2. **Database & Migrations** ➔ Bind `supabase` MCP / PostgreSQL
3. **Product Analytics & Events** ➔ Bind `posthog` MCP
4. **Research & Deep Web Search** ➔ Bind `perplexity-ask` / `search_web`
5. **Secrets & Vault Management** ➔ Bind `vault-secrets` / `.env` hygiene

Write or update `.mcp.json` or Antigravity plugin manifest with exact server definitions.

---

### Phase 4: Jasper Production Standards Validation (Zero-Regression)
Every customized plugin must pass the **10 Pillars Audit**:
- [x] **Zero Secret Leakage**: No hardcoded API keys, tokens, or bot passwords.
- [x] **Windows & Linux Hygiene**: UTF-8 without BOM, no CRLF path breakages.
- [x] **Multi-Tenant Isolation**: No data leakage across user/organization scopes.
- [x] **100% Verification**: If python scripts exist, verify with `pytest` / `unittest` before deploying.

---

### Phase 5: Packaging & Installation
Generate the final, deployable asset:
1. **For Antigravity / VS Code**: Place into `.agents/skills/<skill-name>/` with validated `SKILL.md`.
2. **For Claude Code / Cowork**: Package into `.plugin` zip archive (excluding temporary caches) for 1-click import.
3. Present a structured summary of what was customized, which MCPs were connected, and how to invoke the new skill.
