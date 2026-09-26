---
name: weekly-status-report
description: Generates high-impact, executive-ready weekly project status reports with structured health indicators, key achievements, blockers/risks, milestone tracking, and prioritized action items. Use when summarizing weekly progress, reporting to stakeholders, preparing team syncs, or auditing project delivery.
---

# Weekly Status Report Skill (Haftalik Loyiha Holati Hisoboti)

Ushbu mahorat (skill) har qanday dasturiy ta'minot, infratuzilma yoki startap loyihasi bo'yicha yuqori boshqaruv (C-Level, PM, Stakeholders) va muhandislik jamoasi uchun standartlashtirilgan, o'qilishi oson va amaliy harakatlarga boy haftalik hisobotlarni (Weekly Project Status Report) tez va professional darajada shakllantirish uchun mo'ljallangan.

---

## 1. Hisobotning Asosiy Tamoyillari (Core Principles)

1. **BLUF (Bottom Line Up Front)**: Boshqaruv vakillari 30 soniyada umumiy holatni anglay olishi uchun eng muhim natija va xulosalar birinchi o'ringa qo'yiladi.
2. **Harakatga Yo'naltirilganlik (Action-Oriented)**: Har bir to'siq yoki xatar uchun aniq javobgar shaxs (DRI) va muddat (Due Date) belgilangan Action Item biriktiriladi.
3. **RAG Status Standarti**:
   - 🟢 **Green (Yashil)**: Loyiha reja bo'yicha ketmoqda, jiddiy xatarlar yo'q.
   - 🟡 **Amber (Sariq)**: Qisman kechikish yoki xatarlar mavjud, ammo jamoa nazorati ostida.
   - 🔴 **Red (Qizil)**: Kritik to'siqlar yoki kechikish bor, rahbariyat/stakeholder aralashuvi yoki resurs zarur.
   - 🔵 **Complete (Bajarildi)**: Ushbu bosqich / spetsifikatsiya to'liq yakunlandi va topshirildi.
4. **Faktlar va Raqamlar (Data-Driven)**: Quruq gaplar o'rniga aniq ko'rsatkichlar (KPIs, commitlar, deploylar, yechilgan issue/buglar, sarflangan vaqt/byudjet).

---

## 2. Standart Hisobot Strukturasi (Report Structure)

Hisobot quyidagi 7 ta mustaqil va mantiqiy blokdan iborat bo'ladi:

```
├── 1. Executive Summary & Health Check (RAG Status, Asosiy impuls)
├── 2. Metrikalar va Dashboard (KPIs, Sprint ko'rsatkichlari, Sifat)
├── 3. Haftalik Asosiy Natijalar (Completed Deliverables & Milestones)
├── 4. Keyingi Hafta Maqsadlari (Planned Focus & Next Week Targets)
├── 5. Xatarlar va To'siqlar (RAID Analysis: Risks, Blockers & Mitigations)
├── 6. Qabul Qilingan Qarorlar va Eskalatsiyalar (Decisions Log & Escalations)
└── 7. Aniq Harakatlar Rejasi (Prioritized Action Items Matrix)
```

---

## 3. To'liq Hisobot Shablonlari (Templates)

### Standart Markdown Shabloni (Repository / Wiki / Email)

```markdown
# 📊 Loyiha Haftalik Holat Hisoboti / Weekly Status Report
**Loyiha nomi:** [Project Name]
**Hisobot davri:** [DD.MM.YYYY] — [DD.MM.YYYY] (Hafta #[W])
**Loyiha egasi / PM:** [Ism Sharif]
**Umumiy Holat (Overall Health):** 🟢 GREEN / 🟡 AMBER / 🔴 RED

---

## 1. 📌 Boshqaruv Xulosasi (Executive Summary)
> **BLUF (Qisqa xulosa):** [Loyiha holatini ifodalovchi 2-3 ta asosiy jumlalar. Ushbu haftada eng muhim yutuq nima bo'ldi va asosiy e'tibor qayerga qaratilgan?]

* **Rejadagi siljish:** [Masalan: Jadval bo'yicha 100% / 2 kun oldinda / 1 hafta kechikmoqda]
* **Byudjet / Resurs:** [Normal / Xodimlarga talab mavjud / Tejamkor rejimda]
* **Asosiy yo'nalish:** [Keyingi hafta uchun strategik fokus]

---

## 2. 📈 Metrikalar va Progress (Key Metrics)

| Ko'rsatkich (KPI) | O'tgan Hafta | Joriy Hafta | Maqsad | Dinamika |
| :--- | :--- | :--- | :--- | :---: |
| **Sprint Progress** | 45% | 78% | 80% | 🟢 +33% |
| **Yopilgan Vazifalar (Tasks/PRs)**| 12 PR | 19 PR | 15 PR | 🟢 O'sish |
| **Kritik Xatoliklar (P0/P1 Bugs)**| 4 ta | 1 ta | 0 ta | 🟢 -3 ta |
| **Test Coverage (Qoplash)** | 82% | 87% | 85% | 🟢 +5% |
| **Uptime / Server Barqarorligi** | 99.8% | 99.98% | 99.9% | 🟢 Normada |

---

## 3. 🏆 Haftalik Yutuqlar (Completed Milestones)

### Modul / Workstream A: [Masalan: Backend & API]
- ✅ **[Funksiya/Vazifa nomi]**: [Qilingan ish va uning qiymati (biznes yoki texnik yutuq)].
- ✅ **[Integratsiya nomi]**: [Masalan: Payme/Click webhook integratsiyasi to'liq yakunlandi va testlandi].

### Modul / Workstream B: [Masalan: Frontend & UI]
- ✅ **[Komponent/Sahifa]**: [Responsive dizayn va mikro-interaksiyalar ishlab chiqildi].
- ✅ **[Optimizatsiya]**: [Lighthouse ko'rsatkichi 68 dan 94 ga oshirildi].

---

## 4. 🎯 Keyingi Hafta Rejalari (Next Week Objectives)

- 🎯 **[Maqsad 1]**: [Tavsif va kutilayotgan natija] (Mas'ul: @username, Muddat: DD.MM)
- 🎯 **[Maqsad 2]**: [Masalan: Staging muhitida yuklama testlarini (load testing) o'tkazish]
- 🎯 **[Maqsad 3]**: [Mijoz uchun dastlabki MVP versiya taqdimotini tayyorlash]

---

## 5. ⚠️ Xatarlar va To'siqlar (Blockers & Risks)

| # | Turi | Tavsif (Muammo) | Ta'sir darajasi | Yumshatish Chorasi (Mitigation) | Mas'ul |
| :-: | :--- | :--- | :---: | :--- | :--- |
| 1 | **Blocker** | [Uchinchi tomon API kaliti olinmadi] | 🔴 Yuqori | Uchinchi tomon integratori bilan call o'tkazish | @jasper |
| 2 | **Risk** | [Server yuklamasi oshishi mumkin] | 🟡 O'rta | Redis keshlash qatlamini joriy qilish | @dev |

---

## 6. ⚖️ Qarorlar va Eskalatsiyalar (Decisions & Escalations)

- **Qabul qilingan qaror:** [Masalan: Ma'lumotlar bazasi sifatida PostgreSQL tanlandi, sababi jsonb qulayligi].
- **Eskalatsiya (Rahbariyat ko'magi zarur):** [Masalan: Domen va SSL sertifikatini rasmiylashtirish uchun to'lovni tasdiqlash talab etiladi].

---

## 7. 📋 Aniq Harakatlar Matritsasi (Action Items Matrix)

| ID | Vazifa (Action Item) | Mas'ul (DRI) | Prioritet | Muddat (Due Date) | Holat (Status) |
| :-: | :--- | :---: | :---: | :---: | :---: |
| **AI-01** | Docker compose konfiguratsiyasini optimallashtirish | @devops | **P1** | 28.09.2026 | In Progress |
| **AI-02** | Bot to'lov xavfsizligi auditi o'tkazish | @jasper | **P0** | 26.09.2026 | Open |
| **AI-03** | Yangi onboarding sahifasi dizaynini tasdiqlash | @product | **P2** | 30.09.2026 | Pending |
```

---

### Telegram / Slack Kompakt Xabarnoma Shabloni (Executive Quick-Pulse)

Mobil qurilmalarda tezkor o'qish uchun:

```text
🚀 [PROJECT NAME] — HAFTALIK STATUS (W39 / 2026)
Holat: 🟢 Yashil (Reja bo'yicha)

📌 Asosiy Xulosa:
MVP backend arxitekturasi va to'lov tizimlari muvaffaqiyatli ulandi. Server infratuzilmasi tayyor.

🏆 Asosiy Yutuqlar:
• To'lov tizimlari (Click/Payme) integratsiyasi va testlari yakunlandi
• Docker ishlab chiqarish muhiti to'liq sozlangan
• Test coverage 87% ga yetkazildi

⚠️ To'siqlar / Xatarlar:
• SMS-provayder shartnomasi imzolanmagan (Dushanbagacha kutilyapti)

🎯 Keyingi Hafta Fokusi:
• Foydalanuvchi avtorizatsiyasi va WebApp frontendini ulash
• Dastlabki beta-test guruhini ishga tushirish

📋 Harakatlar (Action Items):
[AI-01] @jasper: Provayder bilan uchrashuv (26.09)
[AI-02] @techlead: Staging deploy va healthcheck (28.09)
```

---

## 4. Agent va Dasturchilar Uchun Ko'rsatmalar (Instructions for Agents)

Foydalanuvchi hisobot so'raganda agent quyidagi qadamlarni bajaradi:

1. **Kontekstni Yig'ish**:
   - `git log --since="1 week ago" --oneline` orqali haftalik commitlar tarixini skanerlash.
   - O'zgartirilgan fayllar, repozitoriya holati va mavjud issue/vazifalar ro'yxatini tekshirish.
   - Ishga tushirilgan servislar yoki server holatini inobatga olish.
2. **Kategoriyalash**:
   - Olingan natijalarni yutuqlar, rejalar va to'siqlarga ajratish.
3. **Action Items ni shakllantirish**:
   - Hech qachon egasiz (DRI siz) yoki muddatsiz vazifa qoldirmaslik.
   - Har bir harakat bandiga P0 (kechiktirib bo'lmas), P1 (yuqori), P2 (o'rta) ustuvorlik berish.
4. **Hakamlik va Baholash**:
   - Agar loyihada blocker mavjud bo'lsa, statusni sun'iy ravishda "Yashil" deb baholamaslik; ob'ektiv 🟡 yoki 🔴 status berish.
