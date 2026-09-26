---
name: heroicons
description: Comprehensive guide and icon reference for Heroicons by Tailwind Labs. Use when implementing, selecting, or styling official Tailwind icons across 24x24 Outline, 24x24 Solid, 20x20 Mini, and 16x16 Micro sets in React, Vue, or JSX.
---

# Heroicons Skill (Tailwind Labs Official Icon Suite)

Heroicons is the official handcrafted SVG icon set designed specifically to harmonize with Tailwind CSS typography, buttons, and form controls.

## 1. Installation

### React
```bash
npm install @heroicons/react
```

### Vue 3
```bash
npm install @heroicons/vue
```

---

## 2. The 4 Icon Styles & Import Paths

Heroicons comes in 4 distinct styles, each tailored for specific UI scales:

| Style | Path (React) | Recommended Scale | Best For |
| :--- | :--- | :--- | :--- |
| **24x24 Outline** | `@heroicons/react/24/outline` | `h-6 w-6` / `h-5 w-5` | Main navigation, cards, page headers |
| **24x24 Solid** | `@heroicons/react/24/solid` | `h-6 w-6` / `h-5 w-5` | Active states, primary emphasis |
| **20x20 Mini** | `@heroicons/react/20/solid` | `h-5 w-5` | Standard buttons, badges, table rows |
| **16x16 Micro** | `@heroicons/react/16/solid` | `h-4 w-4` | Form select chevrons, compact tags, tooltips |

---

## 3. Usage Examples

### 3.1 Button with Leading Icon (React + Tailwind)
```tsx
import { PlusIcon } from '@heroicons/react/20/solid';

export function CreateButton({ onClick }: { onClick: () => void }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="inline-flex items-center gap-x-1.5 rounded-lg bg-indigo-600 px-3.5 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 transition-colors"
    >
      <PlusIcon className="-ml-0.5 h-5 w-5 text-indigo-200" aria-hidden="true" />
      Yangi Qo'shish
    </button>
  );
}
```

### 3.2 Dropdown Chevron (Micro Style)
```tsx
import { ChevronDownIcon } from '@heroicons/react/16/solid';

export function DropdownTrigger({ label }: { label: string }) {
  return (
    <button className="flex items-center gap-1 text-xs font-medium text-zinc-300 hover:text-white">
      <span>{label}</span>
      <ChevronDownIcon className="h-4 w-4 text-zinc-500 transition-transform group-hover:rotate-180" />
    </button>
  );
}
```

### 3.3 Active / Inactive Nav Link
```tsx
import { HomeIcon as HomeIconOutline } from '@heroicons/react/24/outline';
import { HomeIcon as HomeIconSolid } from '@heroicons/react/24/solid';

export function NavItem({ isActive, label }: { isActive: boolean; label: string }) {
  const Icon = isActive ? HomeIconSolid : HomeIconOutline;
  return (
    <div className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-all ${
      isActive ? 'bg-zinc-800 text-white shadow-inner' : 'text-zinc-400 hover:text-zinc-200 hover:bg-zinc-900'
    }`}>
      <Icon className={`h-5 w-5 ${isActive ? 'text-indigo-400' : 'text-zinc-500'}`} />
      <span>{label}</span>
    </div>
  );
}
```

---

## 4. Key Icons Reference
- **Action & Controls**: `PlusIcon`, `TrashIcon`, `PencilSquareIcon`, `EllipsisHorizontalIcon`, `CheckIcon`, `XMarkIcon`
- **Navigation**: `Bars3Icon`, `ChevronRightIcon`, `ChevronDownIcon`, `ArrowLeftIcon`, `ArrowTopRightOnSquareIcon`
- **User & Security**: `UserIcon`, `LockClosedIcon`, `KeyIcon`, `ShieldCheckIcon`, `EyeIcon`, `EyeSlashIcon`
- **Status & Alerts**: `CheckCircleIcon`, `ExclamationTriangleIcon`, `InformationCircleIcon`, `SparklesIcon`

---

## 5. Best Practices
1. Always add `aria-hidden="true"` to decorative icons so screen readers ignore them.
2. Pair `text-current` or explicit Tailwind text colors (e.g. `text-zinc-400 group-hover:text-white`) with transitions for seamless hover states.
