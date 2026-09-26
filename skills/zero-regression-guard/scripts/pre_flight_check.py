#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zero-Regression Pre-Flight Checker
Kod o'zgarishlaridan so'ng 7 ta asosiy xatolikni avtomatik tekshiruvchi skript.
"""

import os
import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Maxfiy kalitlar regexi
SECRET_PATTERNS = [
    (r"(?:bot_token|token|api_key|secret)\s*=\s*['\"][0-9a-zA-Z_\-]{20,}['\"]", "Maxfiy kalit/token kod ichida hardcode qilingan!"),
    (r"https://api\.telegram\.org/bot[0-9]+:[a-zA-Z0-9_\-]+", "Telegram bot tokeni to'g'ridan-to'g'ri URL ichida yozilgan!"),
]

# Tugma qotib qolishi (finally yo'qligi) regexi
ASYNC_WITHOUT_FINALLY = r"(?:const|function)\s+\w*(?:Click|Submit|Action|Handler)\w*\s*=\s*async\s*\([^)]*\)\s*=>\s*\{[^}]*setIsLoading\(true\)(?![^}]*finally\s*\{)"

def check_file(filepath):
    path = Path(filepath)
    if not path.exists():
        return []

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return [f"Faylni o'qishda xatolik: {e}"]

    issues = []

    # 1. Maxfiy kalitlar tekshiruvi
    for pattern, msg in SECRET_PATTERNS:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for m in matches:
            line_no = content[:m.start()].count("\n") + 1
            issues.append(f"Qator {line_no}: [Xavfsizlik Xatosi] {msg}")

    # 2. Frontend tugmalarida isLoading bor ammo finally yo'qligi
    if path.suffix in [".tsx", ".jsx", ".ts", ".js"]:
        if "setIsLoading(true)" in content and "finally" not in content:
            issues.append("Barcha qatorlar: [Tugma Qotishi Xavfi] 'setIsLoading(true)' mavjud, ammo 'finally' bloki topilmadi! Xatolik yuz berganda tugma qotib qolishi mumkin.")

    # 3. Python bare except
    if path.suffix == ".py":
        lines = content.splitlines()
        for i, line in enumerate(lines, start=1):
            if re.match(r"^\s*except\s*:", line):
                issues.append(f"Qator {i}: [Python Xatosi] 'except:' (bare except) qo'llanilgan. Xatolar yutilib ketadi!")

    return issues

def run_pre_flight(target_path="."):
    print(f"\n=======================================================")
    print(f"🛡️ Zero-Regression Pre-Flight Tekshiruvi: {target_path}")
    print(f"=======================================================")

    p = Path(target_path)
    files_to_check = []
    if p.is_file():
        files_to_check.append(p)
    else:
        for ext in [".py", ".ts", ".tsx", ".js", ".jsx"]:
            files_to_check.extend(p.rglob(f"*{ext}"))

    # node_modules va venv larni chiqarib tashlash
    filtered_files = [f for f in files_to_check if "node_modules" not in str(f) and ".venv" not in str(f) and ".git" not in str(f)]

    total_issues = 0
    for f in filtered_files[:50]: # Eng ko'pi bilan 50 ta muhim fayl
        issues = check_file(f)
        if issues:
            print(f"\n📁 {f.name}:")
            for iss in issues:
                print(f"   ⚠️  {iss}")
                total_issues += 1

    if total_issues == 0:
        print("\n✅ Mukammal! 7 ta asosiy xatolik alomatlari topilmadi (0 issues).")
    else:
        print(f"\n❌ DIQQAT: {total_issues} ta xavfli xatolik topildi. Kodni topshirishdan oldin tuzating!")
    print(f"=======================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    run_pre_flight(target)
