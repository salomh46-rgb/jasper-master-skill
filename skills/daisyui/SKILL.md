---
name: daisyui
description: Complete guide and design recipes for DaisyUI (Tailwind CSS component library). Use when building or styling UI components (buttons, modals, cards, drawers, stats, form inputs, toasts, themes) in Tailwind CSS, React, Vue, Next.js, or Vite projects.
---

# DaisyUI Skill (Tailwind CSS Component Architecture)

DaisyUI adds semantic component classes (`btn`, `card`, `modal`, `drawer`, `badge`, `alert`, `table`, etc.) to Tailwind CSS, drastically reducing boilerplate while maintaining 100% Tailwind flexibility.

## 1. Installation & Configuration

### Package installation
```bash
npm i -D daisyui@latest
```

### Tailwind Config (`tailwind.config.js` or `tailwind.config.ts`)
```javascript
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,vue,html}",
    "./app/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        darkluxury: {
          "primary": "#3b82f6",
          "secondary": "#8b5cf6",
          "accent": "#06b6d4",
          "neutral": "#1e293b",
          "base-100": "#050608",
          "base-200": "#0f172a",
          "base-300": "#1e293b",
          "info": "#38bdf8",
          "success": "#22c55e",
          "warning": "#f59e0b",
          "error": "#ef4444",
        },
      },
      "dark",
      "light",
      "night",
    ],
    darkTheme: "darkluxury",
    base: true,
    styled: true,
    utils: true,
  },
}
```

---

## 2. Core UI Component Recipes

### 2.1 Buttons (`btn`)
```html
<!-- Primary & Secondary Actions -->
<button class="btn btn-primary btn-sm rounded-lg shadow-lg shadow-primary/25 hover:scale-[1.02] transition-transform">
  Saqlash
</button>
<button class="btn btn-outline btn-secondary btn-sm">Bekor qilish</button>
<button class="btn btn-ghost btn-sm">Batafsil</button>
<button class="btn btn-primary loading btn-disabled">Yuklanmoqda...</button>
```

### 2.2 Modal (Native Dialog + DaisyUI)
```html
<button class="btn btn-primary" onclick="my_modal_1.showModal()">Oynani ochish</button>
<dialog id="my_modal_1" class="modal modal-bottom sm:modal-middle">
  <div class="modal-box bg-base-200 border border-white/10 shadow-2xl backdrop-blur-xl">
    <h3 class="font-bold text-lg text-white">Yangi Buyurtma</h3>
    <p class="py-4 text-sm text-gray-400">Kerakli ma'lumotlarni to'ldiring va tasdiqlang.</p>
    <div class="modal-action">
      <form method="dialog" class="flex gap-2">
        <button class="btn btn-ghost btn-sm">Yopish</button>
        <button class="btn btn-primary btn-sm">Tasdiqlash</button>
      </form>
    </div>
  </div>
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>
```

### 2.3 Cards (`card`)
```html
<div class="card bg-base-200/60 border border-white/5 shadow-xl hover:border-primary/40 transition-all duration-300 backdrop-blur-md">
  <div class="card-body p-6">
    <div class="flex items-center justify-between">
      <span class="badge badge-primary badge-outline text-xs font-mono">FINTECH</span>
      <span class="text-xs text-emerald-400 font-semibold">+24.5%</span>
    </div>
    <h2 class="card-title text-white mt-2">Oylik Tushum</h2>
    <p class="text-2xl font-black text-white">48,250,000 UZS</p>
    <div class="card-actions justify-end mt-4">
      <button class="btn btn-primary btn-xs">Hisobotni ko'rish</button>
    </div>
  </div>
</div>
```

### 2.4 Forms & Inputs
```html
<div class="form-control w-full">
  <label class="label">
    <span class="label-text text-gray-300 text-xs font-medium">Telefon raqam</span>
  </label>
  <div class="join">
    <span class="join-item bg-base-300 px-3 py-2 text-sm text-gray-400 border border-white/10 flex items-center">+998</span>
    <input type="text" placeholder="90 123 45 67" class="input input-bordered input-sm join-item w-full bg-base-100 border-white/10 focus:border-primary" />
  </div>
</div>
```

### 2.5 Toast & Alerts
```html
<div class="toast toast-top toast-end z-50">
  <div class="alert alert-success bg-emerald-950/80 border border-emerald-500/30 text-emerald-200 shadow-xl backdrop-blur-md">
    <span>To'lov muvaffaqiyatli amalga oshirildi!</span>
  </div>
</div>
```

---

## 3. Best Practices (Jasper Production Standards)
1. **Never use default pure white backgrounds** with DaisyUI; always pair with deep obsidian (`#050608` or `#0a0b0e`) base colors.
2. **Combine DaisyUI with Tailwind Utility Classes**: DaisyUI gives semantic structure, while Tailwind utility classes (`backdrop-blur`, `hover:scale-[1.02]`, `shadow-primary/20`) add 2026 elite micro-interactions.
3. **Always use native `<dialog>` for modals**: It provides native escape key handling and backdrop focus trapping.
