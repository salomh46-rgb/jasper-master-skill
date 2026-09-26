---
name: python-pep8-reviewer
description: Senior Python code reviewer and static analysis skill enforcing PEP 8 standards, modern type annotations (PEP 484/585/604), clean architecture, anti-pattern detection, security hygiene, and idiomatic Python 3.11+. Use when reviewing, auditing, refactoring, or optimizing Python code before merging or deployment.
---

# Python PEP 8 Code Reviewer Skill (Python Kod Resenzenzi)

Ushbu mahorat (skill) Python kod bazalarini professional darajada ko'rib chiqish (code review), PEP 8 uslubiy standartlari, zamonaviy Python 3.11+ idiomasi, xavfsizlik va arxitektura tozaligini kafolatlash uchun ishlab chiqilgan.

---

## 1. Asosiy Nazorat Ustunlari (Review Pillars)

Har bir Python fayli quyidagi 5 ta daraja bo'yicha tekshiriladi:

```
├── 1. PEP 8 Formatlash va Nomlash Qoidalari (Naming & Whitespace)
├── 2. Zamonaviy Tipizatsiya va Idioma (Type Hints & Python 3.11+)
├── 3. Anti-Patternlar va Xavfli Tuzilmalar (Code Smells & Traps)
├── 4. Xavfsizlik va Resurs Boshqaruvi (Security & Resource Leaks)
└── 5. Katta Arxitektura va Tozalik (Clean Code & Guard Clauses)
```

---

## 2. Standart PEP 8 Qoidalari va Talablar

### 2.1. Nomlash Standartlari (Naming Conventions)
* **Funksiyalar va O'zgaruvchilar**: `snake_case` (masalan: `calculate_total_price`, `user_id`).
* **Sinflar (Classes)**: `PascalCase` / `CapWords` (masalan: `PaymentGateway`, `OrderProcessor`).
* **O'zgarmaslar (Constants)**: `UPPER_SNAKE_CASE` (masalan: `MAX_RETRIES`, `DEFAULT_TIMEOUT`).
* **Ichki/Xususiy atributlar**: Bitta ostki chiziq bilan boshlanadi: `_internal_method`, `_cache`.
* **Nomlar ma'noli bo'lishi**: `a`, `x`, `temp`, `data2` kabi noaniq nomlar taqiqlanadi.

### 2.2. Importlar Gigiyenasi (PEP 8 Import Order)
Importlar har doim faylning eng boshida, 3 ta aniq guruhga ajratilgan bo'lishi shart (har bir guruh orasida 1 ta bo'sh qator):
1. **Standart kutubxona** (masalan: `os`, `sys`, `typing`, `pathlib`, `datetime`).
2. **Uchinchi tomon kutubxonalari** (masalan: `fastapi`, `pydantic`, `sqlalchemy`, `aiogram`).
3. **Lokal loyiha modullari** (masalan: `from app.core.config import settings`).

> [!WARNING]
> `from module import *` (wildcard import) mutlaqo taqiqlanadi! Har doim faqat kerakli sinf yoki funksiyalar import qilinadi.

### 2.3. Satr Uzunligi va Bo'sh Joylar (Whitespace & Indentation)
* Chekinish (Indentation): Faqat **4 ta bo'sh joy** (space), tab belgisi mutlaqo ishlatilmaydi.
* Satr chegarasi: Tavsiya etilgan 79-88 belgi (zamonaviy Black/Ruff standarti).
* Funksiyalar va sinflar orasida:
  * Global (top-level) sinf va funksiyalar orasida: **2 ta bo'sh qator**.
  * Sinf ichidagi metodlar orasida: **1 ta bo'sh qator**.
* Qavslar ichida keraksiz bo'shliq bo'lmasligi (`fn( arg )` ❌ -> `fn(arg)` ✅).
* Kalit so'z argumentlarida `=` atrofida bo'shliq qo'yilmaydi (`def fn(x=1):` ✅).

---

## 3. Zamonaviy Python 3.10+ / 3.11+ Standartlari

### 3.1. Qat'iy Tipizatsiya (Strict Typing - PEP 585 & 604)
Eski `typing.Optional`, `typing.List`, `typing.Dict` o'rniga zamonaviy sintaksis majburiy:
```python
# ❌ Eski / Tavsiya etilmaydi:
from typing import Dict, List, Optional
def get_users(ids: List[int]) -> Optional[Dict[str, str]]: ...

# ✅ Zamonaviy Python 3.10+:
def get_users(ids: list[int]) -> dict[str, str] | None: ...
```

### 3.2. Resurs Boshqaruvi (Context Managers)
Fayllar, tarmoq ulanishlari, ma'lumotlar bazasi sessiyalari va qulflar (locks) faqat `with` yoki `async with` orqali ochiladi:
```python
# ❌ Xato:
f = open("data.json")
content = f.read()

# ✅ To'g'ri:
with open("data.json", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 4. Aniqlanuvchi Anti-Patternlar (Critical Code Smells)

### 4.1. O'zgaruvchan Default Argumentlar (Mutable Defaults)
```python
# ❌ Katta xato (barcha chaqiruvlar bir xil ro'yxatga yozadi):
def append_item(item: str, target_list: list = []) -> list:
    target_list.append(item)
    return target_list

# ✅ To'g'ri:
def append_item(item: str, target_list: list[str] | None = None) -> list[str]:
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

### 4.2. "Yalang'och" va Yutilgan Xatoliklar (Bare / Swallowed Except)
```python
# ❌ Xato (xatoni yutib yuboradi, debug qilib bo'lmaydi):
try:
    process_data()
except:
    pass

# ✅ To'g'ri (aniq Exception va logging):
try:
    process_data()
except (ValueError, KeyError) as err:
    logger.error("Data processing failed: %s", err, exc_info=True)
    raise
```

### 4.3. Chuqur Ichma-ich Zanjirlar (Deep Nesting)
Chuqur `if / else` zanjirlari o'rniga **Guard Clauses** (erta qaytish) qo'llaniladi:
```python
# ❌ Chuqur nesting:
def process_order(order):
    if order is not None:
        if order.is_paid:
            if not order.is_delivered:
                deliver(order)

# ✅ Erta qaytish (Guard Clauses):
def process_order(order: Order | None) -> None:
    if order is None or not order.is_paid or order.is_delivered:
        return
    deliver(order)
```

---

## 5. Resenziya Hisoboti Formati (Code Review Output Format)

Har bir tekshiruv quyidagi standart shablonda taqdim etiladi:

```markdown
# 🔍 Python Code Review: [Fayl yoki Modul nomi]

### 📊 Umumiy Xulosa (Summary)
* **PEP 8 Muvofiqligi:** 🟢 95% / 🟡 70% / 🔴 40%
* **Hukm (Verdict):** ✅ LGTM (Approve) / ⚠️ Changes Requested / 🛑 Blocked
* **Aniqlangan muammolar:** [X] ta kritik (P0), [Y] ta uslubiy (PEP 8), [Z] ta optimizatsiya

---

### 🚨 Kritik Muammolar va PEP 8 Buzilishlari (Issues & Violations)

#### 1. [Qoida nomi: masalan, PEP 8 Naming / Mutable Default]
* **Fayl va Qator:** `app/services/payment.py#L42`
* **Muammo tavsifi:** Default argument sifatida o'zgaruvchan `dict` ishlatilgan.
* **Tuzatish (Diff):**
```python
# ❌ Oldin:
def create_transaction(payload: dict = {}): ...

# ✅ Keyin:
def create_transaction(payload: dict[str, Any] | None = None) -> Transaction:
    current_payload = payload if payload is not None else {}
    ...
```

---

### 💡 Yaxshilash Bo'yicha Tavsiyalar (Improvements & Best Practices)
1. **Tipizatsiya:** `Union[int, None]` o'rniga zamonaviy `int | None` qo'llash.
2. **Guard Clauses:** 3-darajali ichma-ich `if` bloklarini bitta qatorli tekshiruvga o'tkazish.

---

### 🛠️ Avtomatlashtirilgan Tekshirish Buyrug'i
```bash
ruff check . --fix
ruff format .
mypy app --strict
```
```

---

## 6. Foydalanish Qoidalari (Agent Execution Flow)

1. Foydalanuvchi Python kodini yuborganda yoki loyihani ko'rib chiqishni so'raganda:
   - Avvalo fayllar tuzilmasini va importlar tartibini tahlil qilish.
   - Funksiyalar, argumentlar va qaytuvchi qiymatlarning tipizatsiyasini tekshirish.
   - Xatoliklarni boshqarish (`try/except`) va resurs yopilishini skanerlash.
2. Natijani yuqoridagi 5-banddagi strukturali shablon asosida xolis, aniq va tayyor diff kodlari bilan ko'rsatish.
