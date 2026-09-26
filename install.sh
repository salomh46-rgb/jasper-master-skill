#!/usr/bin/env bash
# ==============================================================================
# 👑 Jasper Master Agent Suite — Linux / macOS 1-Click Installer
# Run: bash install.sh [TargetDirectory]
# ==============================================================================

set -e

TARGET_DIR="${1:-$(pwd)}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "================================================================================"
echo "  👑 JASPER MASTER AGENT SUITE — LINUX/MACOS 1-CLICK INSTALLER ⚡"
echo "================================================================================"

if command -v python3 &>/dev/null; then
    python3 "$SCRIPT_DIR/installer.py" "$TARGET_DIR"
elif command -v python &>/dev/null; then
    python "$SCRIPT_DIR/installer.py" "$TARGET_DIR"
else
    echo "[!] Python not found. Copying directly..."
    mkdir -p "$TARGET_DIR/.agents/skills"
    cp -r "$SCRIPT_DIR/skills/"* "$TARGET_DIR/.agents/skills/"
    cp "$SCRIPT_DIR/rules/GEMINI.md" "$TARGET_DIR/GEMINI.md"
    echo "[OK] Direct copy complete!"
fi
