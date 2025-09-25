<#
ULST Windows Setup Script (Idempotent)

Creates/repairs a short-path virtual environment at C:\uls_env and installs
dependencies from the repository requirements.txt without touching global Python.

Usage (PowerShell):
  Set-ExecutionPolicy Bypass -Scope Process
  .\scripts\setup_windows.ps1

This script is safe to re-run.
#>

param(
  [switch]$SmokeTest
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Info($msg) { Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "[ OK ] $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "[WARN] $msg" -ForegroundColor Yellow }
function Write-Err($msg)  { Write-Host "[ERR ] $msg" -ForegroundColor Red }

# Repo root (this script lives in repo\scripts)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot  = Split-Path -Parent $ScriptDir
$ReqFile   = Join-Path $RepoRoot 'requirements.txt'

if (-not (Test-Path $ReqFile)) {
  Write-Err "requirements.txt not found at $ReqFile"
  exit 1
}

$VenvPath   = 'C:\uls_env'
$PyExe      = Join-Path $VenvPath 'Scripts\python.exe'
$PipCmd     = "$PyExe -m pip"

function Test-PyLauncher {
  try {
    $ver = & py -3 -V 2>$null
    return $LASTEXITCODE -eq 0
  } catch { return $false }
}

function Test-Python {
  try { & python -V *> $null; return $LASTEXITCODE -eq 0 } catch { return $false }
}

function Ensure-Venv {
  if (Test-Path $PyExe) {
    Write-Info "Existing venv detected at $VenvPath"
    return
  }
  Write-Info "Creating venv at $VenvPath"
  New-Item -Force -ItemType Directory -Path $VenvPath *> $null | Out-Null
  if (Test-PyLauncher) {
    Write-Info "Using Python launcher: py -3"
    & py -3 -m venv $VenvPath
  } elseif (Test-Python) {
    Write-Info "Using python from PATH"
    & python -m venv $VenvPath
  } else {
    Write-Err "Python not found. Install from https://www.python.org/downloads/ or via Microsoft Store (type 'python' in Start)."
    Write-Host "Tip: After install, re-run this script." -ForegroundColor Yellow
    exit 1
  }
  if (-not (Test-Path $PyExe)) {
    Write-Err "venv creation did not produce $PyExe. Your Python may lack ensurepip."
    Write-Host "Try repairing Python installation, then re-run this script." -ForegroundColor Yellow
    exit 1
  }
}

function Ensure-Pip {
  Write-Info "Upgrading pip in venv"
  try {
    & $PyExe -m ensurepip --upgrade *> $null
  } catch { }
  & $PyExe -m pip install --upgrade pip
}

function Install-Requirements {
  Write-Info "Installing/Updating dependencies from requirements.txt"
  & $PyExe -m pip install -r $ReqFile
}

function Verify-Environment {
  Write-Info "Verifying key imports (pyparsing, PDF backends)"
  $code = @'
import sys
errs = []
try:
  import pyparsing  # query parser dependency
except Exception as e:
  errs.append(f"pyparsing: {e}")
try:
  import fitz  # PyMuPDF
  pdf_backend = "PyMuPDF"
except Exception:
  try:
    import pdfplumber
    pdf_backend = "pdfplumber"
  except Exception as e:
    errs.append(f"pdf backend: {e}")
    pdf_backend = "none"
if errs:
  print("[WARN] Some optional components missing:")
  for m in errs:
    print(" -", m)
print("[INFO] PDF backend:", pdf_backend)
'@
  $tmp = [System.IO.Path]::GetTempFileName() + ".py"
  Set-Content -LiteralPath $tmp -Value $code -Encoding UTF8
  & $PyExe $tmp
  Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
}

function Run-SmokeTest {
  param(
    [string]$RepoRoot
  )
  $entry = Join-Path $RepoRoot 'run_screening.py'
  $jsonDir = Join-Path $RepoRoot 'test_results\extracted_json'
  $terms  = Join-Path $RepoRoot 'search_terms.txt'
  $query  = Join-Path $RepoRoot 'examples\query.txt'
  $outDir = Join-Path $RepoRoot 'results'
  if (-not (Test-Path $jsonDir)) {
    Write-Warn "Smoke test skipped: JSON dir not found at $jsonDir"
    return
  }
  if (Test-Path $query) {
    Write-Info "Running smoke test (query mode)"
    & $PyExe $entry --input $jsonDir --output $outDir --query-file $query --config (Join-Path $RepoRoot 'config.json')
  } elseif (Test-Path $terms) {
    Write-Info "Running smoke test (legacy mode)"
    & $PyExe $entry --input $jsonDir --output $outDir --search-terms $terms --config (Join-Path $RepoRoot 'config.json')
  } else {
    Write-Warn "Smoke test skipped: neither examples\\query.txt nor search_terms.txt available"
    return
  }
  if ($LASTEXITCODE -ne 0) {
    Write-Err "Smoke test failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
  }
  Write-Ok "Smoke test completed"
}

try {
  Write-Info "Starting ULST Windows setup"
  Ensure-Venv
  Ensure-Pip
  Install-Requirements
  Verify-Environment
  Write-Ok "Environment ready at $VenvPath"
  Write-Ok "Python: $(& $PyExe -V)"
  Write-Ok "Pip: $(& $PyExe -m pip --version)"
  if ($SmokeTest) {
    Run-SmokeTest -RepoRoot $RepoRoot
  }
  Write-Host "\nNext steps:" -ForegroundColor Cyan
  Write-Host "  1) Run the tool: .\scripts\run_tool.ps1" -ForegroundColor Cyan
  Write-Host "     (If blocked, run: Set-ExecutionPolicy Bypass -Scope Process)" -ForegroundColor DarkGray
  Write-Host "  2) Results will appear in .\\results with HTML and JSON" -ForegroundColor Cyan
  Write-Host "  3) Query mode: .\scripts\run_tool.ps1 -QueryFile .\examples\query.txt" -ForegroundColor Cyan
} catch {
  Write-Err $_.Exception.Message
  exit 1
}
