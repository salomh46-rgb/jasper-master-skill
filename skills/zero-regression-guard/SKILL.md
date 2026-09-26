---
name: zero-regression-guard
description: Zero-regression engineering and anti-mistake shield distilled from 100+ past project histories. Enforces strict immunity against the Top-7 historically repeated AI mistakes: 1) Ripple regressions ("fixing one thing breaks another"), 2) Hollow/fake diagnostics ("100% on paper, broken in reality"), 3) Asynchronous UI button freeze, 4) Environment variable/token leakage or confusion, 5) Supabase RLS multi-tenant blocking, 6) Telegram webhook delivery loss, and 7) Blind speculative overengineering.
---

# Zero-Regression Guard (Javohirbekning 7 Tizimli Xatoga Qarshi Himoya Qalqoni)

Ushbu mahorat (skill) 100 dan ortiq real loyiha va sessiyalar tarixida yuz bergan eng og'riqli 7 ta tizimli xatoni butunlay yo'q qilish, AI agentining o'zboshimchaligini jilovlash va har bir kod o'zgarishini 100% kafolatli isbot bilan topshirishini ta'minlaydi.

---

## 🛡️ 7 Ta O'limli Xato va Ularga Qarshi Temir Qonunlar (Invariants)

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. Zero-Regression Qonuni: Qo'shni modullarni tekshirmay turib yopma!  │
│ 2. Isbot Qonuni: Real runtime testlarsiz "100% ishlayapti" deyish man! │
│ 3. Asinxron UI Qonuni: Har bir tugmaga try/finally va 8s timeout!      │
│ 4. Muhit O'zgaruvchilari Qonuni: Server va Client kalitlarini ajrat!   │
│ 5. Multi-Tenant Qonuni: Yangi tashkilot ochilishini RLS da tekshir!    │
│ 6. Telegram Qonuni: Asinxron navbat (queue) va retry bo'lishi shart!  │
│ 7. Karpathy Soddalik Qonuni: Taxmin qilma — aniqlashtir va sodda yoz! │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 1-USTUN: Regressiyaga Qarshi Qat'iy Himoya (Anti-Ripple Regression)
* **Muammo:** Bitta faylni tuzatish qo'shni 2 ta komponentni yoki API chaqiruvlarini sindirishi.
* **Qoida:**
  - Kod o'zgartirilgach, agent o'sha faylga bog'liq bo'lgan barcha importlarni (`grep_search` orqali) aniqlashi shart.
  - O'zgarishdan so'ng **albatta** loyiha build yoki typecheck buyrug'ini yurgizish:
    - TypeScript/Next.js: `npm run build` yoki `npx tsc --noEmit`
    - Python: `pytest` yoki sintaksis tekshiruvi.
  - Faqat o'zgartirilgan qatorlar emas, qo'shni sahifalar render bo'lishi tekshiriladi.

---

### 2-USTUN: Soxta Diagnostikani Mutlaq Taqiqlash (Doubt-Driven Empirical Proof)
* **Muammo:** Agent kodga qarab «hamma narsa 100% ideal ishlamoqda» deb hisobot berishi, lekin amalda funksiya ishlamasligi.
* **Qoida:**
  - **Quruq hisobotlar taqiqlanadi!** Agent har bir funksiya ishlayotganini real sinov bilan isbotlashi shart:
    - API bo'lsa: `curl` yoki Python orqali real so'rov yuborib javob kodini (HTTP 200) ko'rsatish.
    - Funksiya bo'lsa: Test skripti orqali kiruvchi/chiquvchi qiymatni tekshirish.
    - UI bo'lsa: DevTools yoki konsol loglarida qizil xatolik yo'qligini tekshirish.
  - Agar agent amalda tekshirmagan bo'lsa: «Men buni amalda sinab ko'rdim» deb gapirishga haqqi yo'q!

---

### 3-USTUN: Tugmalar Qotishi va UI Muzlashiga Qarshi Qulf (Async UI Resilience)
* **Muammo:** Tugma bosilganda internet sekinligi yoki API xatosi sababli tugma "loading" rejimida qotib qolishi.
* **Qoida:**
  - Har qanday tugma bosilish hodisasida (onClick handler):
    ```typescript
    // ✅ Majburiy andoza:
    const handleAction = async () => {
      setIsLoading(true);
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 8000); // 8s timeout

      try {
        await apiCall({ signal: controller.signal });
        toast.success("Muvaffaqiyatli bajarildi!");
      } catch (err: any) {
        if (err.name === 'AbortError') {
          toast.error("Tarmoq kutish vaqti tugadi (Timeout). Qaytadan urinib ko'ring.");
        } else {
          toast.error(err.message || "Xatolik yuz berdi");
        }
      } finally {
        clearTimeout(timeoutId);
        setIsLoading(false); // Tugma HAR DOIM qulfdan yechiladi!
      }
    };
    ```

---

### 4-USTUN: Maxfiy Kalitlar va Muhit O'zgaruvchilari Gigiyenasi (.env Boundary)
* **Muammo:** Vercel yoki ishlab chiqarish muhitida tokenlar yo'qolishi yoki mijoz brauzeriga tushib qolishi.
* **Qoida:**
  - Frontend (Next.js / Vite)da faqat ommaviy kalitlar (`NEXT_PUBLIC_`, `VITE_`) ishlatiladi.
  - Backend maxfiy kalitlari (Bot token, Supabase Service Role, Stripe/Payme Secret) HECH QACHON mijoz brauzeriga eksport qilinmaydi.
  - Yangi o'zgaruvchi qo'shilganda har doim `.env.example` ga namunasi yoziladi va qayerda sozlanganligi ko'rsatiladi.

---

### 5-USTUN: Supabase RLS va Multi-Tenant Avtomatik Validatsiyasi
* **Muammo:** Yangi o'quv markaz, klinika yoki foydalanuvchi ochilganda RLS siyosati sababli tizim bloklanishi.
* **Qoida:**
  - Yangi tashkilot (`tenant`) yaratilish jarayonida RLS `INSERT` siyosati alohida tekshiriladi:
    - `auth.uid()` yangi ochilayotgan tashkilotga egalik qila olishi shart.
    - Super-admin va yangi ro'yxatdan o'tuvchi uchun RLS bypass yoki to'g'ri `WITH CHECK` yozilishi kerak.
  - Har qanday RLS migratsiyasidan so'ng yangi tashkilot ochish oqimi (onboarding flow) testlanadi.

---

### 6-USTUN: Telegram Webhook va Xabarnomalar Ishonchliligi (Queue & Retry)
* **Muammo:** Xabar tarqatishda yoki bot orqali bildirishnomada bitta xatolik sababli butun jarayon to'xtab qolishi.
* **Qoida:**
  - Ommaviy xabar yuborishda to'g'ridan-to'g'ri `await bot.sendMessage()` birma-bir chaqirilmaydi.
  - Asinxron navbat (background queue) va kamida 3 martalik eksponentsial qayta urinish (retry with backoff) joriy qilinadi.
  - Telegram `429 Too Many Requests` (Flood control) xatoligi har doim `retry_after` soniyasi bilan kutib bajariladi.

---

### 7-USTUN: Andrej Karpathy Soddalik va Aniqlashtirish Qoidasi (Think Before Coding)
* **Muammo:** Talab noaniq bo'lsa, AI o'zicha taxmin qilib yuzlab qator keraksiz murakkab kod yozishi.
* **Qoida:**
  - Agar talabda ikkilanish bo'lsa: **to'xta va Jasperdan so'ra** (`ask_question` vositasi orqali).
  - 1 marta ishlatiladigan joyga 5 qavatli klass yoki abstraksiya qilinmaydi (Strict YAGNI).
  - Mavjud ishlayotgan kod, formatlash va izohlarga teginilmaydi; faqat zarur qatorlar jarrohlik aniqligida o'zgartiriladi.

---

## 📋 Har Bir Ish Topshirilishidan Oldingi Tekshiruv (Pre-Flight Checklist)

Agent har qanday kod yozish yoki tuzatish ishini tugatgach, o'ziga ushbu 5 ta savolni beradi:

1. [ ] **Regressiya yo'qmi?** Loyiha `build` yoki `typecheck` dan 0 ta xatolik bilan o'tdimi?
2. [ ] **Soxta gap yo'qmi?** Ishlayotganini ko'zim bilan terminal yoki test orqali ko'rdimmi?
3. [ ] **Tugmalar xavfsizmi?** Har bir asinxron hodisada `finally` va `timeout` bormi?
4. [ ] **Kalitlar to'g'rimi?** Server va Client muhit o'zgaruvchilari chalkashmadimi?
5. [ ] **Sodda va tozami?** Keraksiz AI axlati va ortiqcha abstraksiyalar yo'qmi?
