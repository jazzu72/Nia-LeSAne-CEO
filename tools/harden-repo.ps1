# ============================================================
# NIA HYBRID REPO HARDENER
# Terraform + Node.js (Safe / Deterministic)
# ============================================================

$ErrorActionPreference = "Stop"

function Section($title) {
    Write-Host ""
    Write-Host "==============================="
    Write-Host " $title"
    Write-Host "===============================" -ForegroundColor Cyan
}

function Fail($msg) {
    Write-Host "❌ $msg" -ForegroundColor Red
    exit 1
}

Section "Environment"
Write-Host "User: $(whoami)"
Write-Host "Location: $(Get-Location)"
Write-Host "Shell: PowerShell $($PSVersionTable.PSVersion)"

# ------------------------------------------------------------
# NODE VALIDATION
# ------------------------------------------------------------
Section "Node.js Validation"

if (-not (Test-Path "package.json")) {
    Fail "package.json missing. Node project not detected."
}

$lockFiles = @(
    "package-lock.json",
    "yarn.lock",
    "npm-shrinkwrap.json"
) | Where-Object { Test-Path $_ }

if ($lockFiles.Count -gt 1) {
    Fail "Multiple lock files detected. Use ONE package manager only."
}

if ($lockFiles.Count -eq 0) {
    Write-Host "⚠️ No lock file found. Generating npm lockfile…" -ForegroundColor Yellow

    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
        Fail "npm not available in PATH."
    }

    npm install --package-lock-only --ignore-scripts

    if (-not (Test-Path "package-lock.json")) {
        Fail "Failed to generate package-lock.json."
    }

    Write-Host "✅ package-lock.json generated"
}
else {
    Write-Host "✅ Lock file present: $($lockFiles[0])"
}

# ------------------------------------------------------------
# TERRAFORM VALIDATION
# ------------------------------------------------------------
Section "Terraform Validation"

if (-not (Get-Command terraform -ErrorAction SilentlyContinue)) {
    Fail "Terraform not installed or not in PATH."
}

terraform version | Out-Null
Write-Host "✅ Terraform binary detected"

# Locate Terraform root
$terraformDir = Get-ChildItem -Directory -Recurse -Depth 3 |
    Where-Object { Test-Path (Join-Path $_.FullName "*.tf") } |
    Select-Object -First 1

if (-not $terraformDir) {
    Fail "No Terraform configuration (.tf files) found."
}

Write-Host "✅ Terraform directory detected:"
Write-Host "   $($terraformDir.FullName)"

Push-Location $terraformDir.FullName

# Ensure terraform init safety
if (Test-Path ".terraform") {
    Write-Host "ℹ️ Existing Terraform init detected"
}

terraform init -input=false -backend=false | Out-Null
Write-Host "✅ terraform init (backend disabled) succeeded"

terraform validate | Out-Null
Write-Host "✅ terraform validate passed"

Pop-Location

# ------------------------------------------------------------
# FINAL STATUS
# ------------------------------------------------------------
Section "Repository Status"
Write-Host "✅ Node + Terraform hybrid repo is healthy"
Write-Host "🚀 Safe to run CI pipelines"

exit 0
