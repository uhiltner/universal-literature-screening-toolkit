<#
ULST Test Runner Script (Windows)

Runs the comprehensive test suite using the isolated venv at C:\uls_env.
This validates all 38 tests covering edge cases, core functionality, and integration scenarios.

Usage (PowerShell):
  .\scripts\run_tests.ps1 [-Verbose] [-Coverage] [-FailFast] [-Specific <test_file>]

Options:
  -Verbose:   Show detailed test output (-v flag)
  -Coverage:  Generate coverage report (requires pytest-cov)
  -FailFast:  Stop after first failure (-x flag)
  -Specific:  Run only specific test file (e.g., "test_validator.py")

Examples:
  .\scripts\run_tests.ps1                           # Run all tests
  .\scripts\run_tests.ps1 -Verbose                  # Verbose output
  .\scripts\run_tests.ps1 -Specific test_validator.py  # Run specific tests
  .\scripts\run_tests.ps1 -FailFast -Verbose       # Stop on first failure with details
#>

param(
  [switch]$Verbose,
  [switch]$Coverage,
  [switch]$FailFast,
  [string]$Specific = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Info($msg) { Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "[ OK ] $msg" -ForegroundColor Green }
function Write-Err($msg)  { Write-Host "[ERR ] $msg" -ForegroundColor Red }
function Write-Test($msg) { Write-Host "[TEST] $msg" -ForegroundColor Yellow }

$VenvPath = 'C:\uls_env'
$PyExe    = Join-Path $VenvPath 'Scripts\python.exe'

if (-not (Test-Path $PyExe)) {
  Write-Err "Python venv not found at $VenvPath. Please run .\scripts\setup_windows.ps1 first."
  exit 1
}

# Repo root assumed as parent of this script's folder
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot  = Split-Path -Parent $ScriptDir
$TestsDir  = Join-Path $RepoRoot 'tests'

if (-not (Test-Path $TestsDir)) {
  Write-Err "Tests directory not found at $TestsDir"
  exit 1
}

# Build pytest command
$PytestArgs = @('-m', 'pytest')

# Add test target
if ($Specific) {
  $TestTarget = Join-Path $TestsDir $Specific
  if (-not (Test-Path $TestTarget)) {
    Write-Err "Specific test file not found: $TestTarget"
    exit 1
  }
  $PytestArgs += $TestTarget
  Write-Test "Running specific tests: $Specific"
} else {
  $PytestArgs += $TestsDir
  Write-Test "Running full test suite (38 tests)"
}

# Add options
if ($Verbose) {
  $PytestArgs += '-v'
  Write-Info "Verbose output enabled"
}

if ($Coverage) {
  $PytestArgs += '--cov=scripts'
  Write-Info "Coverage reporting enabled"
}

if ($FailFast) {
  $PytestArgs += '-x'
  Write-Info "Fail-fast mode enabled"
}

Write-Info "Test configuration:"
Write-Host "  Python:    $PyExe" -ForegroundColor DarkGray
Write-Host "  Tests:     $TestsDir" -ForegroundColor DarkGray
Write-Host "  Command:   python $($PytestArgs -join ' ')" -ForegroundColor DarkGray

Write-Host ""
Write-Test "Starting test execution..."
Write-Host "=========================================================="

# Run the tests
& $PyExe @PytestArgs

$ExitCode = $LASTEXITCODE

Write-Host "=========================================================="

if ($ExitCode -eq 0) {
  Write-Ok "All tests passed successfully! ✅"
  Write-Info "Your toolkit installation is verified and ready for research."
} else {
  Write-Err "Some tests failed (exit code: $ExitCode)"
  Write-Info "This may indicate installation issues or code problems."
  Write-Info "Check the test output above for specific failure details."
}

Write-Host ""
Write-Info "Test categories covered:"
Write-Host "  🔍 Search Parser:     Quoted phrases, wildcards, regex patterns" -ForegroundColor DarkGray
Write-Host "  ✅ Validator:         AND/OR logic, block combinations, edge cases" -ForegroundColor DarkGray  
Write-Host "  📄 PDF Extractor:     Capability reporting, corrupt file handling" -ForegroundColor DarkGray
Write-Host "  📊 Report Generator:  HTML generation, file sorting, statistics" -ForegroundColor DarkGray
Write-Host "  🔧 CLI Integration:   End-to-end workflows, error scenarios" -ForegroundColor DarkGray
Write-Host "  🏗️  Toolkit Structure: File existence, configuration validation" -ForegroundColor DarkGray

if ($ExitCode -ne 0) {
  Write-Host ""
  Write-Info "Troubleshooting tips:"
  Write-Host "  • Re-run setup: .\scripts\setup_windows.ps1" -ForegroundColor DarkGray
  Write-Host "  • Check dependencies: pip list" -ForegroundColor DarkGray
  Write-Host "  • Run specific test: .\scripts\run_tests.ps1 -Specific test_name.py -Verbose" -ForegroundColor DarkGray
}

exit $ExitCode