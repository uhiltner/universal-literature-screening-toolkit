@echo off
REM Simple Windows batch wrapper to run ULST via PowerShell runner
SETLOCAL
set SCRIPT_DIR=%~dp0
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%scripts\run_tool.ps1" %*
ENDLOCAL
