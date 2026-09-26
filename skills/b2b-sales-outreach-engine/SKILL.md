---
name: b2b-sales-outreach-engine
description: >
  Autonomous B2B lead generation, cold outreach sequencing, psychological objection handling,
  and high-converting client proposal generation. Use when: find B2B leads, generate cold pitch,
  write cold email/Telegram outreach, handle client objections ('qimmat', 'kerak emas', 'keyinroq'),
  draft sales proposal with ROI calculations, or close software contracts.
compatibility: Works with Resend email API, Telegram Bots, and Markdown/PDF proposal templates.
---

# B2B Sales Outreach & Deal Closing Engine 💼🚀

Autonomous B2B client acquisition engine engineered to find business decision-makers, craft irresistible value-first outreach messages, neutralize objections, and close high-ticket software/AI contracts for Jasper's flagships.

---

## 🎯 1. Target Audience & Value Proposition Map

| Product | Target Client | Core Pain Point | Value Hook (Irresistible Offer) |
| :--- | :--- | :--- | :--- |
| **Voice2Deal AI** | Sales teams, Real estate, Call centers, Agencies | Slow manual data entry into CRM; 40% of leads lost on phones | "Xodimlaringiz gaplashgan ovozli suhbatdan 3 soniyada to'liq bitim va chek tayyorlaydigan AI agent" |
| **@Ovozli_SavdoBOT** | Retail stores, Wholesale distributors, Market sellers | Kechqurun 3 soat hisob-kitob qilish, kassa kamomadi, daftardagi chalkashlik | "Daftarni unuting: 'Akrom akaga 5 ta sement nasiyaga berdim' deb ovoz yuboring, qolganini bot o'zi qiladi" |
| **DentaMed CRM** | Dental clinics, Private medical centers, Multi-branch clinics | Bemorlar qaytib kelmaydi, qabul navbatlari chalkash, shifokorlar foizi hisoblanmaydi | "Klinikangiz har oy yo'qotayotgan 15-20 mln so'mni avtomatik qaytarib beruvchi aqlli tibbiy CRM" |
| **Custom AI / Web** | Medium & Enterprise businesses, Fintech startups | Qimmat va sekin dasturlash jamoalari; xatolar | "2026 Tier-1 standartidagi to'liq avtonom, xavfsiz va tezkor arxitektura" |

---

## ⚡ 2. High-Conversion Cold Outreach Sequences (Telegram & Email)

### Template A: Telegram Direct to CEO / Business Owner (Uzbek)
```markdown
Assalomu alaykum [Ism/Rahbar] aka!

[Kompaniya nomi]ning so'nggi yangiliklarini kuzatib borayapman, rivojlanishingiz juda zo'r! 

Bitta qisqa savol bilan bezovta qilayotgandim: Hozirda savdo xodimlaringiz mijozlar bilan muloqotdan so'ng ma'lumotlarni qo'lda kiritishga kuniga 2-3 soat vaqt sarflayaptimi?

Biz [Kompaniya nomi] uchun shunday yechim qildikki — xodim shunchaki 10 soniyalik ovozli xabar tashlaydi, AI esa avtomat kassa cheki, tovar balansi va mijoz kartasini tayyorlab qo'yadi. Natijada xodimlarning savdo qilish vaqti 40% ga oshadi.

Sizga ushbu tizimning 2 daqiqalik jonli video demosini (va bepul 7 kunlik sinovini) Telegramda tashlab beraymi?
```

### Template B: Cold Email Outreach (Resend API)
```typescript
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendB2BPitch(clientEmail: string, clientName: string, company: string) {
  return await resend.emails.send({
    from: "Javohirbek Asqarov <jasper@yourdomain.com>",
    to: clientEmail,
    subject: `${company} uchun savdo jarayonini 2x tezlashtirish imkoniyati`,
    html: `
      <h2>Assalomu alaykum, ${clientName}!</h2>
      <p>Men <b>Javohirbek Asqarov</b> — AI tizimlari va avtomatlashtirish bo'yicha katta me'morman.</p>
      <p>${company} faoliyatini tahlil qilib, savdo va mijozlar hisobidagi yo'qotishlarni kamaytirish bo'yicha maxsus yechim tayyorladik.</p>
      <div style="background:#f4f4f5; padding:15px; border-radius:8px; margin:20px 0;">
        <b>Kutilayotgan Natija (ROI):</b>
        <ul>
          <li>Kunlik hisob-kitob vaqtini 3 soatdan 5 daqiqaga tushirish;</li>
          <li>Inson omilidagi kassa kamomadlarini 0 ga tushirish;</li>
          <li>Mijozlarning takroriy xaridlarini (retention) 35% ga oshirish.</li>
        </ul>
      </div>
      <p>Sizga mos vaqtda 10 daqiqalik qisqa Google Meet orqali jonli ko'rsatib bersam maylimi?</p>
    `,
  });
}
```

---

## 🛡️ 3. Ironclad Objection Handling Matrix (Sotuv E'tirozlari Qalqoni)

| Mijoz E'tirozi | Noto'g'ri Javob ❌ | To'g'ri Yopish Taktikasi (Senior Close) ✅ |
| :--- | :--- | :--- |
| **"Bizda hammasi yaxshi, daftarda yoki Excelda yuritilyapti"** | "Daftar eski zamonda qolgan" | "To'g'ri, dastlab hamma Exceldan boshlaydi. Lekin do'konda kuniga 50+ xarid bo'lganda, daftarga har oy o'rtacha 3-5 mln so'mlik tovar yozilmay qoladi yoki adashiladi. Tizimimiz 1 oyda o'z pulini 3 barobar oqlab beradi. Keling, 1 hafta bepul sinab ko'ring, foydasini sezmasangiz to'xtatamiz." |
| **"Hozir narxi qimmat ekan"** | "Bizda chegirma bor" | "Tushunaman, har qanday yangi xarajat kutilmagan tuyuladi. Lekin bu xarajat emas — investitsiya. Hozir bitta hisobchi yoki operatorga oyiga 4-5 mln so'm berasiz. Bizning AI botimiz esa 24/7 ishlab, oyiga bor-yo'g'i 300-500 ming so'mga tushadi. Ya'ni har oy 4 mln so'm tejaysiz." |
| **"Xodimlarimiz o'rganolmaydi, qiyin"** | "Yo'q, juda oson" | "Aynan shuning uchun biz yozishni talab qilmaymiz! Telegramda xolangizga yoki o'rtog'ingizga ovozli xabar yuborishni biladigan har qanday odam bu botdan 1 daqiqada foydalana oladi. Hech qanday murakkab tugma yo'q." |
| **"Keyinroq o'ylab ko'ramiz"** | "Xo'p, qachon yozay?" | "Albatta, qaror chiqarish sizning ixtiyoringizda. Faqat bitta narsa: har o'tgan haftada hisob-kitobsizlik tufayli kamida 1-2 mln so'm pul yo'qotilyapti. Keling, bugun 1 ta filialingizga ulab beray, 3 kunda natijasini o'z ko'zingiz bilan ko'ring." |

---

## 📄 4. 1-Click Proposal Generator Formula
Taklif yuborilayotganda doim 3 qism bo'lishi shart:
1. **Mijozning Aniq Muammosi** (Sizda hozir nima bo'lyapti).
2. **Bizning Yechimimiz & Arxitekturasi** ([Excalidraw diagramma havolasi]).
3. **Kafolat & ROI** ("Agar 1 oyda vaqtingiz tejalmasa — to'lovingiz 100% qaytariladi").
