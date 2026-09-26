# ==============================================================================
# 👑 Jasper Master Agent Suite — Windows PowerShell 1-Click Installer
# Run: .\install.ps1 [TargetDirectory]
# ==============================================================================

param (
    [string]$TargetDir = (Get-Location).Path
)

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  👑 JASPER MASTER AGENT SUITE — WINDOWS 1-CLICK INSTALLER ⚡" -ForegroundColor Yellow
Write-Host "================================================================================" -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Run Python installer
if (Get-Command python -ErrorAction SilentlyContinue) {
    python "$ScriptDir\installer.py" "$TargetDir"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    py "$ScriptDir\installer.py" "$TargetDir"
} else {
    Write-Host "[!] Python topilmadi. Qo'lda nusxalanmoqda..." -ForegroundColor Yellow
    $DestSkills = Join-Path $TargetDir ".agents\skills"
    New-Item -ItemType Directory -Path $DestSkills -Force | Out-Null
    Copy-Item -Path "$ScriptDir\skills\*" -Destination $DestSkills -Recurse -Force
    Copy-Item -Path "$ScriptDir\rules\GEMINI.md" -Destination (Join-Path $TargetDir "GEMINI.md") -Force
    Write-Host "[OK] Nusxalash yakunlandi!" -ForegroundColor Green
}
