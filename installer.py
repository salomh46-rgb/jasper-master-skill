#!/usr/bin/env python3
"""
👑 Jasper Master Agent Suite — Universal 1-Click Installer
Installs all 40+ skills, production rules (GEMINI.md / CLAUDE.md), and autonomous agents
onto any new machine or workspace in seconds.
Author: Javohirbek Asqarov (Jasper)
"""

import os
import sys
import shutil
import json
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BANNER = """
================================================================================
  👑 JASPER MASTER AGENT SUITE — 1-CLICK UNIVERSAL INSTALLER ⚡
  Autonomous Multi-Agent Skills, Production Standards & Jev System One
================================================================================
"""

def install(target_dir: Path):
    source_dir = Path(__file__).parent.resolve()
    skills_src = source_dir / "skills"
    rules_src = source_dir / "rules"
    templates_src = source_dir / "templates"

    print(BANNER)
    print(f"[*] O'rnatish boshlandi (Installing to): {target_dir}")

    # 1. Target .agents/skills directory
    skills_dest = target_dir / ".agents" / "skills"
    skills_dest.mkdir(parents=True, exist_ok=True)

    copied_skills = 0
    if skills_src.exists():
        for item in skills_src.iterdir():
            if item.is_dir():
                dest_item = skills_dest / item.name
                if dest_item.exists():
                    shutil.rmtree(dest_item)
                shutil.copytree(item, dest_item)
                copied_skills += 1
                print(f"  [+] O'rnatildi (Installed Skill): {item.name}")

    print(f"\n[OK] Jami {copied_skills} ta ixtisoslashgan Skill muvaffaqiyatli o'rnatildi!")

    # 2. Master SKILL.md in target skills
    master_skill_src = source_dir / "SKILL.md"
    if master_skill_src.exists():
        master_dest = skills_dest / "jasper-master-suite"
        master_dest.mkdir(exist_ok=True)
        shutil.copy2(master_skill_src, master_dest / "SKILL.md")
        print("  [+] O'rnatildi: jasper-master-suite (Bosh Mega-Skill)")

    # 3. Global Rules (GEMINI.md and CLAUDE.md)
    if rules_src.exists():
        gemini_rule = rules_src / "GEMINI.md"
        claude_rule = rules_src / "CLAUDE.md"
        if gemini_rule.exists():
            shutil.copy2(gemini_rule, target_dir / "GEMINI.md")
            print("  [+] O'rnatildi: GEMINI.md (Antigravity Global Rules & 10 Pillars)")
        if claude_rule.exists():
            shutil.copy2(claude_rule, target_dir / "CLAUDE.md")
            print("  [+] O'rnatildi: CLAUDE.md (Claude Code Global Rules)")

    # 4. Context Templates
    if templates_src.exists():
        for tpl in templates_src.iterdir():
            if tpl.is_file():
                dest_tpl = target_dir / tpl.name.replace(".template", "")
                if not dest_tpl.exists():
                    shutil.copy2(tpl, dest_tpl)
                    print(f"  [+] Shablon yaratildi (Created Template): {dest_tpl.name}")

    # 5. Build/Update skills-lock.json
    lock_file = target_dir / "skills-lock.json"
    lock_data = {"version": 1, "skills": {}}
    if lock_file.exists():
        try:
            with open(lock_file, "r", encoding="utf-8") as f:
                lock_data = json.load(f)
        except Exception:
            pass

    for skill_folder in skills_dest.iterdir():
        if skill_folder.is_dir():
            name = skill_folder.name
            lock_data["skills"][name] = {
                "source": f"salomh46-rgb/{name}",
                "sourceType": "custom-skill",
                "skillPath": f".agents/skills/{name}/SKILL.md",
            }

    with open(lock_file, "w", encoding="utf-8") as f:
        json.dump(lock_data, f, indent=2, ensure_ascii=False)
    print("  [+] Yangilandi: skills-lock.json (Barcha skilllar ro'yxatga olindi)")

    print("\n" + "=" * 80)
    print("🎉 TABRIKLAYMIZ! Barcha mahoratlar (skills), qoidalar va Jev System One")
    print("yangi kompyuterda/muhitda to'liq ishga tushdi va aktivlashdi!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    target = Path.cwd()
    if len(sys.argv) > 1:
        target = Path(sys.argv[1]).resolve()
    install(target)
