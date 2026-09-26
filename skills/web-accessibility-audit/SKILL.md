---
name: web-accessibility-audit
description: Web accessibility (A11Y) testing, WCAG 2.1/2.2 AA compliance auditing, and automated evaluation skill using Pa11y, Axe-core, and Chrome DevTools Lighthouse. Use when building inclusive user interfaces, auditing websites for accessibility, fixing contrast issues, testing screen reader navigation, or automating CI/CD accessibility gates.
---

# Web Accessibility Audit Skill (WCAG 2.1/2.2 AA & A11Y Engine)

Enforces accessibility compliance (WCAG 2.1 Level AA/AAA) across all web interfaces, ensuring usability for keyboard navigation, screen readers, and high-contrast environments.

## 1. Automated Testing with Pa11y CLI

### Instant URL Audit
```bash
# Audit a live or local URL against WCAG 2.1 AA
npx pa11y http://localhost:3000

# Strict WCAG 2.1 AAA audit with JSON output
npx pa11y --standard WCAG2AAA --reporter json http://localhost:3000 > a11y-report.json
```

### Configuration (`.pa11yci.json`)
```json
{
  "defaults": {
    "standard": "WCAG2AA",
    "timeout": 30000,
    "wait": 1000,
    "runners": ["axe", "htmlcs"],
    "chromeLaunchConfig": {
      "args": ["--no-sandbox", "--disable-setuid-sandbox"]
    }
  },
  "urls": [
    "http://localhost:3000",
    "http://localhost:3000/login",
    "http://localhost:3000/dashboard"
  ]
}
```

---

## 2. Automated End-to-End Auditing with Playwright & Axe-Core

### Package Installation
```bash
npm i -D @axe-core/playwright
```

### Test Specification (`tests/a11y.spec.ts`)
```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Quality Gate', () => {
  test('Dashboard page must not contain detectable WCAG A/AA violations', async ({ page }) => {
    await page.goto('http://localhost:3000/dashboard');
    await page.waitForLoadState('networkidle');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });
});
```

---

## 3. Core WCAG 2.1 AA Invariants & Code Fixes

### 3.1 Color Contrast (Rule 1.4.3)
- **Normal text (< 18pt / < 24px):** Minimum contrast ratio of **4.5:1** against background.
- **Large text (>= 18pt bold or >= 24px):** Minimum contrast ratio of **3:1**.
- **Icons & UI Boundaries:** Minimum contrast ratio of **3:1**.
- *Fix:* In dark mode (`#050608`), use `text-zinc-100` (#f4f4f5) or `text-zinc-300` (#d4d4d8). Never use dim `text-zinc-600` for readable content.

### 3.2 Focus Indicators (Rule 2.4.7)
- **BANNED:** Never use `outline-none` without providing an explicit replacement.
- **ENFORCED:**
  ```html
  <!-- Always provide high-visibility focus rings for keyboard users -->
  <button class="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2 focus-visible:ring-offset-zinc-950">
    Harakat
  </button>
  ```

### 3.3 Form Inputs & Accessible Labels (Rule 1.3.1, 4.1.2)
- Inputs must always be connected to a `<label>` via `id` / `htmlFor`, or have an explicit `aria-label`:
  ```html
  <!-- Connected Label -->
  <label for="user-email" class="text-xs text-zinc-300">Elektron pochta</label>
  <input id="user-email" type="email" class="input input-sm" />

  <!-- Icon-Only Button with ARIA -->
  <button aria-label="Sozlamalarni ochish" class="p-2">
    <IconSettings aria-hidden="true" />
  </button>
  ```

### 3.4 Screen Reader Skip Links (Rule 2.4.1)
Always include a skip-to-content link at the top of the body for keyboard-only users:
```html
<a 
  href="#main-content" 
  class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-primary focus:text-white focus:rounded-lg shadow-xl"
>
  Asosiy kontentga o'tish
</a>
```

### 3.5 Accessible Modals (Focus Trap & Escape Handling)
- When a modal opens, background elements must have `aria-hidden="true"`.
- Focus must be trapped inside the modal until dismissed.
- Pressing `Escape` must close the modal immediately.
- Use native HTML `<dialog>` whenever possible, as it handles focus trapping automatically.

---

## 4. Best Practices (Jasper Production Standards)
1. **Zero Silent Buttons**: Every clickable `<button>` or `<a>` without visible text MUST have `aria-label="..."`.
2. **Decorative SVGs**: All decorative icons must include `aria-hidden="true"`.
3. **Dynamic Content Updates**: Use `aria-live="polite"` on notification toasts and dynamic cart counters so screen readers announce changes without interrupting the user.
