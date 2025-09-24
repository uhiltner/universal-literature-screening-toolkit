#!/usr/bin/env bash
set -euo pipefail

# ULST Unix Setup Script (Idempotent)
# Creates/repairs a short-path venv at ~/.uls_env and installs requirements.

echo "[INFO] Starting ULST Unix setup"

REQ_FILE="$(cd "$(dirname "$0")"/.. && pwd)/requirements.txt"
if [[ ! -f "$REQ_FILE" ]]; then
  echo "[ERR ] requirements.txt not found at $REQ_FILE" >&2
  exit 1
fi

VENV_DIR="$HOME/.uls_env"
PY="$VENV_DIR/bin/python3"

if [[ ! -x "$PY" ]]; then
  echo "[INFO] Creating venv at $VENV_DIR"
  mkdir -p "$VENV_DIR"
  if command -v python3 >/dev/null 2>&1; then
    python3 -m venv "$VENV_DIR"
  else
    echo "[ERR ] python3 not found. Install from python.org or your package manager." >&2
    exit 1
  fi
fi

echo "[INFO] Upgrading pip"
"$PY" -m ensurepip --upgrade || true
"$PY" -m pip install --upgrade pip

echo "[INFO] Installing/Updating dependencies from requirements.txt"
"$PY" -m pip install -r "$REQ_FILE"

echo "[ OK ] Environment ready at $VENV_DIR"
"$PY" -V
"$PY" -m pip --version
echo "\nNext steps:"
echo "  1) Run the tool: scripts/run_tool.sh"
echo "  2) Results will appear in ./results with HTML and JSON"
