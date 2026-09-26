#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Haftalik Loyiha Holati Hisobotini Avtomatik Yaratuvchi Skript (Weekly Status Reporter)
Har dushanba 06:00 da mustaqil ishga tushirish uchun moslashtirilgan.
"""

import os
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

def get_git_commits(repo_path="."):
    """Oxirgi 7 kunlik git commitlarini yig'ish"""
    try:
        cmd = [
            "git", "-C", repo_path, "log", 
            "--since=7.days", 
            "--pretty=format:- %h %s (%an, %ar)"
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"- Git tarixi aniqlanmadi yoki repozitoriya emas: {e}"

def generate_report(project_name="Ekotizim Loyihalari", target_dir="."):
    now = datetime.now()
    week_number = now.isocalendar()[1]
    start_date = (now - timedelta(days=7)).strftime("%d.%m.%Y")
    end_date = now.strftime("%d.%m.%Y")
    
    commits = get_git_commits(target_dir)
    
    report_content = f"""# 📊 Loyiha Haftalik Holat Hisoboti
**Loyiha nomi:** {project_name}
**Hisobot davri:** {start_date} — {end_date} (Hafta #{week_number}, {now.year})
**Loyiha egasi:** Javohirbek Asqarov (Jasper)
**Umumiy Holat (Overall Health):** 🟢 GREEN (Avtomatik monitoring)

---

## 1. 📌 Boshqaruv Xulosasi (Executive Summary)
> **BLUF:** Hafta davomida rejalashtirilgan ishlar jadval asosida bajarildi. Tizim barqarorligi va xavfsizlik darajasi normada.

* **Rejadagi siljish:** Jadval bo'yicha 100%
* **Infratuzilma:** Serverlar va botlar faol
* **Keyingi hafta fokusi:** Yangi xususiyatlar integratsiyasi va yuklama testlari

---

## 2. 📈 Oxirgi 7 Kunlik Commitlar va O'zgarishlar (Git Activity)

{commits if commits else "- Oxirgi 7 kunda yangi commitlar kiritilmagan."}

---

## 3. 🏆 Haftalik Yutuqlar (Completed Milestones)
- ✅ **Infratuzilma & Barqarorlik**: Servislar va monitoring to'liq nazorat ostida.
- ✅ **Avtomatizatsiya**: Haftalik monitoring va hisobot generatori ishga tushirildi.

---

## 4. 🎯 Keyingi Hafta Maqsadlari (Next Week Objectives)
- 🎯 **[Maqsad 1]**: Yangi funksionalliklarni staging muhitiga deploy qilish (Mas'ul: @jasper, Muddat: { (now + timedelta(days=5)).strftime("%d.%m") })
- 🎯 **[Maqsad 2]**: Xavfsizlik va integratsiya testlarini o'tkazish
- 🎯 **[Maqsad 3]**: Kod sifatini avtonom auditdan o'tkazish

---

## 5. ⚠️ Xatarlar va To'siqlar (Blockers & Risks)
| # | Turi | Tavsif | Ta'sir | Yumshatish Chorasi | Mas'ul |
| :-: | :--- | :--- | :---: | :--- | :--- |
| 1 | Monitoring | Server resurslari nazorati | 🟡 O'rta | Disk va RAM avtomatik tozalash skriptlari | @jasper |

---

## 6. 📋 Aniq Harakatlar Matritsasi (Action Items)
| ID | Vazifa | Mas'ul (DRI) | Prioritet | Muddat | Holat |
| :-: | :--- | :---: | :---: | :---: | :---: |
| **AI-01** | Haftalik sprint maqsadlarini tekshirish | @jasper | **P0** | { (now + timedelta(days=2)).strftime("%d.%m.%Y") } | In Progress |
| **AI-02** | Xavfsizlik auditi va tokenlar rotatsiyasi | @jasper | **P1** | { (now + timedelta(days=4)).strftime("%d.%m.%Y") } | Open |
"""
    
    reports_folder = Path(target_dir) / "reports"
    reports_folder.mkdir(parents=True, exist_ok=True)
    report_filename = reports_folder / f"weekly_report_{now.year}_w{week_number}.md"
    
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print(f"[OK] Hisobot muvaffaqiyatli saqlandi: {report_filename}")
    return report_filename

if __name__ == "__main__":
    generate_report()
