---
name: healthcare-clinic-growth
description: >
  Healthcare CRM client acquisition, clinic director pitch protocols, patient retention automation,
  and lost clinic revenue audits for DentaMed Hospital CRM.
  Use when: pitch DentaMed to dental/medical clinics, calculate lost clinic revenue, automate patient recall/retention,
  configure doctor percentage calculations, or set up multi-branch clinic onboarding.
compatibility: Tailored for DentaMed Hospital CRM and healthcare SaaS models.
---

# Healthcare & Clinic Growth Engine (DentaMed) 🏥🦷

Enterprise client acquisition and high-ticket sales protocol for selling `DentaMed Hospital CRM` to dental clinics, aesthetic centers, and private hospitals.

Empowers sales agents and Jasper to conduct "Yo'qotilgan Daromad Auditi" (Lost Revenue Audit) with clinic directors and close long-term recurring SaaS subscriptions.

---

## 💎 1. Clinic Pain Points vs. DentaMed Solutions

| Stomatologiya / Klinika Og'rig'i | Klinikaga Yetkazadigan Zarari | DentaMed Yechimi |
| :--- | :--- | :--- |
| **Qayta kelmaydigan bemorlar (Lost Patients)** | Bemor davolangach, 6 oylik gigiyena yoki ko'rikka chaqirilmaydi. Klinika har oy $1,500 - $3,000 yo'qotadi. | **Avtomatik Patient Recall**: 6 oy to'lgach, Telegram/SMS orqali bemorga shaxsiy taklifnoma va chegirma yuboriladi. |
| **Shifokorlar foizidagi chalkashlik** | Har oy oxirida qaysi shifokor qancha xizmat qilgani, qancha foiz olishi bo'yicha janjal va xatolar. | **1-Klik Shifokor KPR**: Tizim har bir muolaja bo'yicha shifokor va assistent foizini o'zi avtomatik kassa bilan hisoblab beradi. |
| **Navbatlar chalkashligi & Bo'sh kreslo** | Bemor kelmay qolsa, kreslo 1 soat bo'sh turadi. Klinika ijara va maoshni esa to'lashda davom etadi. | **SMS/Telegram Eslatma & Zaxira Navbat**: Qabuldan 2 soat oldin tasdiqlash so'raladi, kelmasa navbatdagi bemor avtomat chaqiriladi. |
| **Ko'p filialli nazoratsizlik** | Bosh shifokor yoki direktor boshqa filiallarda nima bo'layotganini real vaqtda ko'rolmaydi. | **Multi-Tenant Boss Dashboard**: Telefondan 1 soniyada barcha filiallar tushumi, qarzlar va shifokorlar hisoboti. |

---

## 📊 2. "Yo'qotilgan Daromad Auditi" (Klinika Direktori Bilan Muloqot Skripti)

Klinika bosh shifokori yoki direktori bilan uchrashganda quyidagi 3 ta savol beriladi:

> **1-Savol:** *"Doktor, klinikangiz bazasida jami nechta bemor bor?"*  
> (Masalan: 3,000 nafar bemor)
>
> **2-Savol:** *"Ulardan nechtasi oxirgi 6 oy ichida profilaktika yoki takroriy ko'rikka keldi?"*  
> (Javob odatda: "Ko'pi bilan 200-300 tasi, qolganiga vaqtimiz yo'q qo'ng'iroq qilishga")
>
> **3-Savol:** *"Demak, 2,700 nafar bemor qaytib kelmagan. Agar DentaMed ulardan bor-yo'g'i 10% ini (270 nafarini) qaytara olsa va har biri o'rtacha 200,000 so'mlik gigiyena qildirsa — klinikangizga qo'shimcha **54,000,000 UZS** toza tushum kiradi! Bizning DentaMed esa oyiga bor-yo'g'i 500,000 so'm turadi. 54 mln so'm daromad olish uchun 500 ming sarflashga rozimisiz?"*

Bu argumentdan keyin 90% klinika rahbarlari darhol rozi bo'ladi!

---

## ⚙️ 3. Patient Retention Recall Algorithm (Python Logic)

```python
from datetime import datetime, timedelta

def find_lost_patients(patients_db, days_inactive=180):
    """
    180 kundan beri klinikaga tashrif buyurmagan bemorlarni
    profilaktik gigiyena yoki davolash uchun avtomat saralaydi.
    """
    lost_patients = []
    cutoff_date = datetime.now() - timedelta(days=days_inactive)
    
    for patient in patients_db:
        if patient["last_visit_date"] < cutoff_date and patient.get("treatment_completed", False):
            lost_patients.append({
                "id": patient["id"],
                "name": patient["name"],
                "phone": patient["phone"],
                "doctor": patient["doctor_name"],
                "recall_message": (
                    f"Hurmatli {patient['name']}! {patient['doctor']} ko'rigingizdan beri 6 oy o'tdi. "
                    f"Tishlaringiz salomatligi uchun bepul profilaktik ko'rikka taklif qilamiz: t.me/DentaMedKlinika_bot"
                )
            })
    return lost_patients
```

---

## 🏥 4. Multi-Tenant Branch Isolation Standard (Rule 9 Verification)

DentaMed sotilganda klinika egalariga ma'lumotlar xavfsizligi kafolatlanadi:
1. Shifokor faqat o'z kabinetidagi bemorlarni ko'radi (boshqa shifokor bemorini ko'rolmaydi).
2. Filial 1 xodimlari Filial 2 ning kassasini ko'rolmaydi.
3. Faqat Klinika Ta'sischisi (SuperAdmin) barcha filiallar umumiy tushumini ko'radi.
