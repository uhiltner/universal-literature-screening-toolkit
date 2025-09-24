@echo off
setlocal enableextensions
title Universal Literature Screening Toolkit - Windows Runner

echo ===============================================
echo  ULST - Windows Quick Runner
echo ===============================================
echo.

REM Attempt setup (idempotent)
echo [INFO] Ensuring Python environment at C:\uls_env
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\setup_windows.ps1"
if errorlevel 1 (
  echo [ERR ] Setup failed. Please review the output above.
  pause
  exit /b 1
)

REM Run the tool with defaults
echo.
echo [INFO] Running the toolkit with defaults...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\run_tool.ps1"
if errorlevel 1 (
  echo [ERR ] Run failed. Please review the output above.
  pause
  exit /b 1
)

echo.
echo [ OK ] Finished. Check the 'results' folder for the report and JSON.
echo.
pause
endlocal
