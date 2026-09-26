---
name: flag-icons
description: Integration guide and component recipes for Flag Icons (curated SVG world flags). Use when implementing multi-language switchers (UZ, RU, EN), phone number country selectors, international payments, or regional badges in frontend projects.
---

# Flag Icons Skill (SVG Country Flags & Localization UI)

Flag Icons provides pixel-perfect SVG flags for all countries with standardized ISO 3166-1 alpha-2 country codes.

## 1. Installation

### npm Package
```bash
npm install flag-icons
```

### Import into Project
In your main CSS entry point (`index.css`, `globals.css`, or `App.tsx`):
```css
/* In CSS */
@import "flag-icons/css/flag-icons.min.css";
```
Or in React / Next.js entry:
```tsx
import "flag-icons/css/flag-icons.min.css";
```

---

## 2. Core Class Syntax

Flag icons uses two main classes:
- Standard rectangular flag (4:3 ratio): `<span class="fi fi-[code]"></span>`
- Squared 1:1 flag: `<span class="fi fi-[code] fis"></span>`

### Essential ISO Codes for Central Asia & Global Apps:
- 🇺🇿 Uzbekistan: `fi fi-uz`
- 🇷🇺 Russia: `fi fi-ru`
- 🇬🇧 United Kingdom: `fi fi-gb`
- 🇺🇸 United States: `fi fi-us`
- 🇰🇿 Kazakhstan: `fi fi-kz`
- 🇰🇬 Kyrgyzstan: `fi fi-kg`
- 🇹🇯 Tajikistan: `fi fi-tj`
- 🇹🇷 Turkey: `fi fi-tr`
- 🇦🇪 UAE: `fi fi-ae`
- 🇨🇳 China: `fi fi-cn`
- 🇩🇪 Germany: `fi fi-de`

---

## 3. Production Component Recipes (Jasper Standards)

### 3.1 Multilingual Switcher (UZ / RU / EN)
```tsx
import React, { useState } from 'react';

const languages = [
  { code: 'uz', label: "O'zbekcha", flag: 'uz' },
  { code: 'ru', label: 'Русский', flag: 'ru' },
  { code: 'en', label: 'English', flag: 'us' },
];

export function LanguageDropdown({ currentLang, onSelect }: { currentLang: string; onSelect: (code: string) => void }) {
  const [open, setOpen] = useState(false);
  const active = languages.find(l => l.code === currentLang) || languages[0];

  return (
    <div className="relative inline-block text-left">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-900 border border-white/10 hover:border-white/20 text-xs font-medium text-zinc-200 transition-colors"
      >
        <span className={`fi fi-${active.flag} fis rounded-full w-4 h-4 shadow-sm`} />
        <span>{active.label}</span>
      </button>

      {open && (
        <div className="absolute right-0 mt-2 w-36 rounded-xl bg-zinc-950 border border-white/10 shadow-2xl p-1.5 z-50 backdrop-blur-xl">
          {languages.map((lang) => (
            <button
              key={lang.code}
              onClick={() => { onSelect(lang.code); setOpen(false); }}
              className={`w-full flex items-center gap-2.5 px-2.5 py-1.5 rounded-lg text-xs transition-colors ${
                lang.code === currentLang ? 'bg-primary/20 text-primary font-semibold' : 'text-zinc-300 hover:bg-zinc-800'
              }`}
            >
              <span className={`fi fi-${lang.flag} fis rounded-full w-3.5 h-3.5`} />
              <span>{lang.label}</span>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
```

### 3.2 Phone Prefix Country Selector (+998)
```html
<div class="flex items-center rounded-lg bg-zinc-900 border border-white/10 px-3 py-2">
  <div class="flex items-center gap-2 pr-2 border-r border-white/10">
    <span class="fi fi-uz fis rounded-full w-4 h-4"></span>
    <span class="text-xs font-mono text-zinc-300">+998</span>
  </div>
  <input 
    type="tel" 
    placeholder="90 123 45 67" 
    class="bg-transparent pl-3 text-sm text-white focus:outline-none w-full"
  />
</div>
```

---

## 4. Best Practices
1. **Always use rounded flags (`rounded-full` or `rounded-sm`)** with the `fis` (1:1 square) class for avatar-style or dropdown-style language pickers.
2. **Add a subtle border or inner ring** (`ring-1 ring-white/10`) around flags so that light-colored flags (e.g. Russia, Poland, Japan) don't bleed into light backgrounds or get lost against dark backgrounds.
