---
name: ultra-frugal-tokens
description: Ultra-Frugal High-Yield Token Architecture skill. Enforces surgical tool calling (grep before view), strict diff-based editing, exclusion of noisy dependency/build artifacts, and PROJECT_CONTEXT.md brain anchoring to cut token consumption by 75% without quality degradation.
---

# Ultra-Frugal High-Yield Token Architecture

Operational protocol to maximize AI code reasoning yield while slashing input and output token consumption.

## 1. Input Token Optimization (Surgical Tool Calling)

### 1.1 The "Grep-First, Slice-Read" Rule
- **FORBIDDEN:** Never call `view_file` on entire files (>100 lines) without StartLine and EndLine.
- **MANDATORY:**
  1. Use `grep_search` to pinpoint the exact function, error string, or line number.
  2. Call `view_file` targeting strictly `StartLine = match - 15` and `EndLine = match + 25` (30-50 lines window).
  - *Result:* Consumes ~200 tokens instead of 4,000+ tokens per inspection.

### 1.2 Blacklisted Paths (Never Grep or Read)
Always exclude these paths from directory scans and searches:
- `node_modules/**`
- `.git/**`
- `dist/**`, `build/**`, `.next/**`, `.nuxt/**`
- `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`
- `*.log`, `*.min.js`, `*.min.css`, `*.map`
- `venv/**`, `.venv/**`, `__pycache__/**`

---

## 2. Output Token Optimization (Anti-Slop & Surgical Diffs)

### 2.1 The "No-Monolith-Rewrite" Rule
- **FORBIDDEN:** Never rewrite an entire 300+ line file using `write_to_file` when only modifying a few lines or a single function.
- **MANDATORY:**
  - Always use `replace_file_content` targeting the single contiguous block of code.
  - Keep replacement chunks focused only on the modified lines.

### 2.2 Claude Fable 5 Anti-Slop Communication
- Eliminate boilerplate pleasantries ("Sure, I can help you with that!", "Here is the updated code:").
- Deliver direct, dense, Senior-level architectural insights and results immediately.

---

## 3. Brain Anchoring (`PROJECT_CONTEXT.md`) Protocol

When starting a project or closing a major milestone:
1. Maintain a high-density, 30-line `PROJECT_CONTEXT.md` at the project root.
2. Structure:
   - **Stack & Architecture:** (e.g. Next.js 14, FastAPI, Postgres 16, Redis)
   - **Active Ports & Services:** (e.g. Frontend: 3000, Backend: 8000)
   - **Critical Env Keys:** (Names only, zero secrets)
   - **Completed Features & Next Milestones**
3. When starting a new chat session, read ONLY `PROJECT_CONTEXT.md` to bootstrap 100% project awareness using under 400 tokens!
