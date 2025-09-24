<#
ULST Runner Script (Windows)

Uses the short-path venv at C:\uls_env to run run_screening.py with sensible defaults.

Usage (PowerShell):
  .\scripts\run_tool.ps1 [-InputPath <path>] [-OutputPath <path>] [-SearchTermsPath <path>] [-ConfigPath <path>]

Defaults:
  Input:       .\input_pdfs
  Output:      .\results
  SearchTerms: .\search_terms.txt
  Config:      .\config.json
#>

param(
  [Alias('InDir')]
  [string]$InputPath = ".\input_pdfs",

  [Alias('OutDir')]
  [string]$OutputPath = ".\results",

  [string]$SearchTermsPath = ".\search_terms.txt",
  [string]$ConfigPath = ".\config.json"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Info($msg) { Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "[ OK ] $msg" -ForegroundColor Green }
function Write-Err($msg)  { Write-Host "[ERR ] $msg" -ForegroundColor Red }

$VenvPath = 'C:\uls_env'
$PyExe    = Join-Path $VenvPath 'Scripts\python.exe'

if (-not (Test-Path $PyExe)) {
  Write-Err "Python venv not found at $VenvPath. Please run .\scripts\setup_windows.ps1 first."
  exit 1
}

# Repo root assumed as parent of this script's folder
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot  = Split-Path -Parent $ScriptDir
$Entry     = Join-Path $RepoRoot 'run_screening.py'

if (-not (Test-Path $Entry)) {
  Write-Err "Could not find run_screening.py at $Entry"
  exit 1
}

# Normalize output directory and ensure it exists
if (-not (Test-Path $OutputPath)) {
  New-Item -ItemType Directory -Path $OutputPath -Force *> $null | Out-Null
}

Write-Info "Running ULST with:";
Write-Host "  --input        $InputPath" -ForegroundColor DarkGray
Write-Host "  --output       $OutputPath" -ForegroundColor DarkGray
Write-Host "  --search-terms $SearchTermsPath" -ForegroundColor DarkGray
Write-Host "  --config       $ConfigPath" -ForegroundColor DarkGray

& $PyExe $Entry --input $InputPath --output $OutputPath --search-terms $SearchTermsPath --config $ConfigPath

if ($LASTEXITCODE -ne 0) {
  Write-Err "run_screening.py exited with code $LASTEXITCODE"
  exit $LASTEXITCODE
}

$html = Join-Path $OutputPath 'validation_report.html'
$htmlAlt = Join-Path $OutputPath 'final_report.html'
$json = Join-Path $OutputPath 'validation_results.json'

if (Test-Path $html) {
  Write-Ok "HTML report: $html"
} elseif (Test-Path $htmlAlt) {
  Write-Ok "HTML report: $htmlAlt"
} else {
  Write-Info "HTML report not found; check output for report filename"
}

if (Test-Path $json) {
  Write-Ok "JSON results: $json"
} else {
  Write-Info "JSON results not found; check output for JSON save step"
}

Write-Ok "Done"
