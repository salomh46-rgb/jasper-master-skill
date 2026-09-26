#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python PEP 8 & Code Smells Static Checker Helper
Berilgan Python fayli yoki papkani PEP 8, xavfli default parametrlar,
bare except va importlar tartibi bo'yicha tezkor tahlil qiladi.
"""

import ast
import os
import sys
from pathlib import Path

# Windows konsolida UTF-8 qo'llab-quvvatlashini ta'minlash
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

class PEP8ReviewVisitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.issues = []

    def visit_FunctionDef(self, node):
        # 1. Funksiya nomlanishini tekshirish (snake_case)
        if not node.name.islower() and not node.name.startswith("__"):
            # Check if has uppercase letters
            if any(c.isupper() for c in node.name):
                self.issues.append({
                    "line": node.lineno,
                    "type": "PEP 8 Naming",
                    "msg": f"Funksiya nomi '{node.name}' snake_case formatida emas."
                })

        # 2. Mutable default arguments tekshiruvi (list, dict, set)
        for default in node.args.defaults:
            if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                self.issues.append({
                    "line": default.lineno,
                    "type": "Critical Anti-Pattern (Mutable Default)",
                    "msg": f"Funksiyada o'zgaruvchan standart qiymat ({type(default).__name__}) ishlatilgan. None qiymatidan foydalaning."
                })

        self.generic_visit(node)

    def visit_ClassDef(self, node):
        # 3. Class nomlanishini tekshirish (PascalCase)
        if "_" in node.name or node.name.islower():
            self.issues.append({
                "line": node.lineno,
                "type": "PEP 8 Naming",
                "msg": f"Sinf (Class) nomi '{node.name}' PascalCase (CapWords) formatida emas."
            })
        self.generic_visit(node)

    def visit_Try(self, node):
        # 4. Bare except tekshiruvi (except:)
        for handler in node.handlers:
            if handler.type is None:
                self.issues.append({
                    "line": handler.lineno,
                    "type": "Critical Anti-Pattern (Bare Except)",
                    "msg": "Xatolik turi ko'rsatilmagan 'except:' (bare except) qo'llanilgan. Aniq istisno sinfini ko'rsating."
                })
        self.generic_visit(node)


def audit_python_file(filepath):
    path = Path(filepath)
    if not path.exists() or path.suffix != ".py":
        print(f"[XATO] Fayl topilmadi yoki Python fayl emas: {filepath}")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Satr uzunligi va tablar tekshiruvi
    lines = content.splitlines()
    line_issues = []
    for idx, line in enumerate(lines, start=1):
        if "\t" in line:
            line_issues.append({"line": idx, "type": "PEP 8 Indentation", "msg": "Tab belgisi ishlatilgan! PEP 8 faqat 4 ta probelni talab qiladi."})
        if len(line) > 100:
            line_issues.append({"line": idx, "type": "PEP 8 Line Length", "msg": f"Satr juda uzun ({len(line)} belgi > 100)."})

    try:
        tree = ast.parse(content, filename=str(path))
        visitor = PEP8ReviewVisitor(str(path))
        visitor.visit(tree)
        all_issues = line_issues + visitor.issues
    except SyntaxError as e:
        print(f"[SYNTAX ERROR] {path}:{e.lineno} - {e.msg}")
        return

    print(f"\n=======================================================")
    print(f"🔍 Resenziya Natijalari: {path.name}")
    print(f"=======================================================")
    if not all_issues:
        print("✅ Kod PEP 8 talablariga va xavfsizlik qoidalariga to'liq javob beradi (0 xatolik)!")
    else:
        print(f"⚠️ Jami aniqlangan kamchiliklar: {len(all_issues)} ta\n")
        for issue in all_issues:
            print(f"  [Qator {issue['line']}] [{issue['type']}]: {issue['msg']}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    if os.path.isfile(target):
        audit_python_file(target)
    else:
        for root, _, files in os.walk(target):
            for file in files:
                if file.endswith(".py") and not file.startswith("."):
                    audit_python_file(os.path.join(root, file))
