---
name: github-workflow-productivity
description: Advanced GitHub workflow automation, keyboard navigation, GitHub CLI (gh) mastery, and code review productivity skill. Use when interacting with GitHub repositories, optimizing pull request reviews, navigating codebases with OctoLinker, or streamlining git release pipelines.
---

# GitHub Workflow & Productivity Skill

Enhances GitHub navigation, PR reviews, branch management, and developer velocity using GitHub CLI (`gh`) and modern productivity extensions.

## 1. Top Recommended Browser Extensions

| Extension | Chrome Web Store Link | Key Feature |
| :--- | :--- | :--- |
| **Refined GitHub** | [Install](https://chromewebstore.google.com/detail/refined-github/hlepfoohegdaggghmbeicignfilkgobd) | Cleans clutter, auto-redirects outdated diffs, adds 100+ micro-features |
| **OctoLinker** | [Install](https://chromewebstore.google.com/detail/octolinker/jlmafbaeoofdegohdhinkbfhcohinooh) | Turns `import` and `require` statements into clickable code links |
| **Enhanced GitHub** | [Install](https://chromewebstore.google.com/detail/enhanced-github/bipdaimiefmfdjhkpomleaehpogibcid) | Displays file size, repo size, and direct single-file download button |

---

## 2. GitHub CLI (`gh`) High-Velocity Workflows

### 2.1 Pull Requests
```bash
# Create PR interactively
gh pr create --title "feat: implement payment webhook idempotency" --body "Closes #42"

# Fast checkout PR branch locally
gh pr checkout 12

# View PR status and CI test checks
gh pr checks

# Approve and merge with squash
gh pr review --approve -b "LGTM! Tested locally."
gh pr merge --squash --delete-branch
```

### 2.2 Issues & Repository Ops
```bash
# List open issues assigned to me
gh issue list --assignee "@me"

# Clone repository and set up SSH automatically
gh repo clone owner/repo

# View releases
gh release list
```

---

## 3. GitHub Native Keyboard Shortcuts (Pro Cheatsheet)
- `t` : Instant file finder / fuzzy search in any repository.
- `w` : Switch branches or tags.
- `y` : Transform current URL into a permanent canonical permalink with the exact commit SHA.
- `b` : Jump directly to git blame for the current file.
- `.` (period) : Launch github.dev (in-browser VS Code) immediately for the current repo.

---

## 4. Advanced Search Queries (Code & Security)
- Find hardcoded API secrets: `filename:.env path:/`
- Find specific dependencies: `filename:package.json "daisyui"`
- Language and stars: `language:typescript stars:>1000 created:>2025-01-01`
