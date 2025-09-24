<#
ULST Windows Setup Script (Idempotent)

Creates/repairs a short-path virtual environment at C:\uls_env and installs
dependencies from the repository requirements.txt without touching global Python.

Usage (PowerShell):
  Set-ExecutionPolicy Bypass -Scope Process
  .\scripts\setup_windows.ps1

This script is safe to re-run.
#>

param()

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

try {
  Write-Info "Starting ULST Windows setup"
  Ensure-Venv
  Ensure-Pip
  Install-Requirements
  Write-Ok "Environment ready at $VenvPath"
  Write-Ok "Python: $(& $PyExe -V)"
  Write-Ok "Pip: $(& $PyExe -m pip --version)"
  Write-Host "\nNext steps:" -ForegroundColor Cyan
  Write-Host "  1) Run the tool: .\scripts\run_tool.ps1" -ForegroundColor Cyan
  Write-Host "     (If blocked, run: Set-ExecutionPolicy Bypass -Scope Process)" -ForegroundColor DarkGray
  Write-Host "  2) Results will appear in .\\results with HTML and JSON" -ForegroundColor Cyan
} catch {
  Write-Err $_.Exception.Message
  exit 1
}
