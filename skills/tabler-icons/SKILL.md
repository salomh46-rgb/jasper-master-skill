---
name: tabler-icons
description: Comprehensive guide and icon catalog for Tabler Icons (6,100+ free SVG vector icons). Use when selecting, importing, and styling vector icons for React, Vue, Svelte, or plain SVG in dashboards, CRM, fintech, e-commerce, and SaaS interfaces.
---

# Tabler Icons Skill (6,100+ Clean Vector Icons)

Tabler Icons is the gold standard for clean, modern, stroke-based vector icons with customizable stroke width, size, and color.

## 1. Installation

### React
```bash
npm install @tabler/icons-react
```

### Vue 3
```bash
npm install @tabler/icons-vue
```

### Webfont / Static SVG
```bash
npm install @tabler/icons
```

---

## 2. Usage Patterns in React (TypeScript)

### 2.1 Standard Component Usage
```tsx
import { 
  IconLayoutDashboard, 
  IconWallet, 
  IconUsers, 
  IconSettings, 
  IconArrowUpRight,
  IconCheck,
  IconShieldCheck
} from '@tabler/icons-react';

export const StatCard = () => (
  <div className="flex items-center gap-3 p-4 bg-zinc-900/80 border border-white/10 rounded-xl">
    <div className="p-2.5 rounded-lg bg-blue-500/10 text-blue-400 border border-blue-500/20">
      <IconWallet size={20} stroke={1.5} />
    </div>
    <div>
      <span className="text-xs text-zinc-400 font-medium">Balans</span>
      <p className="text-lg font-bold text-white flex items-center gap-1">
        12,450,000 UZS
        <IconArrowUpRight size={14} className="text-emerald-400" />
      </p>
    </div>
  </div>
);
```

### 2.2 Global Props with IconContext
You can configure default stroke width and size across your entire app:
```tsx
import { IconContext } from '@tabler/icons-react';

export default function App({ children }: { children: React.ReactNode }) {
  return (
    <IconContext.Provider value={{ size: 20, stroke: 1.5 }}>
      {children}
    </IconContext.Provider>
  );
}
```

---

## 3. High-Frequency Icons by Domain

### 3.1 SaaS, CRM & Navigation
- `IconLayoutDashboard`, `IconLayoutSidebar`, `IconLayoutGrid`
- `IconUsers`, `IconUserPlus`, `IconUserCheck`, `IconAddressBook`
- `IconSettings`, `IconAdjustments`, `IconFilter`, `IconSearch`
- `IconBell`, `IconBellRinging`, `IconInbox`, `IconSend`

### 3.2 Fintech & Payments (Uzbekistan / International)
- `IconWallet`, `IconCreditCard`, `IconReceipt`, `IconReceiptTax`
- `IconCash`, `IconCoins`, `IconCurrencyDollar`, `IconTrendingUp`, `IconTrendingDown`
- `IconArrowUpRight` (Outgoing / Expense), `IconArrowDownLeft` (Incoming / Income)
- `IconLock`, `IconShieldCheck`, `IconKey` (Security & HMAC verification)

### 3.3 Medical & Dental CRM (MedTech)
- `IconStethoscope`, `IconDental`, `IconHeartbeat`, `IconPill`
- `IconCalendarTime`, `IconClockHour4`, `IconNotes`, `IconPrescription`

### 3.4 E-Commerce & Retail
- `IconShoppingCart`, `IconShoppingBag`, `IconTag`, `IconTruckDelivery`
- `IconBarcode`, `IconQrcode`, `IconDiscount`, `IconPackage`

---

## 4. Best Practices (Jasper Production Standards)
1. **Stroke Width**: Default Tabler icons have `stroke={2}` which can look too bold in modern quiet luxury designs. Always use `stroke={1.5}` or `stroke={1.25}` for an ultra-clean, refined 2026 aesthetic.
2. **Animated Hover Physics**:
   ```tsx
   <button className="group flex items-center gap-2 text-sm text-zinc-300 hover:text-white">
     <IconSettings size={18} stroke={1.5} className="transition-transform duration-300 group-hover:rotate-45" />
     <span>Sozlamalar</span>
   </button>
   ```
3. **Tree Shaking**: Always import named icons directly: `import { IconName } from '@tabler/icons-react'` to keep bundle sizes under control.
