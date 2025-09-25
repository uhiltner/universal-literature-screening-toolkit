#!/usr/bin/env bash
set -euo pipefail

# ULST Unix Setup Script (Idempotent)
# Creates/repairs a short-path venv at ~/.uls_env and installs requirements.
# Usage: scripts/setup_unix.sh [--smoke]

echo "[INFO] Starting ULST Unix setup"

REQ_FILE="$(cd "$(dirname "$0")"/.. && pwd)/requirements.txt"
if [[ ! -f "$REQ_FILE" ]]; then
  echo "[ERR ] requirements.txt not found at $REQ_FILE" >&2
  exit 1
fi

VENV_DIR="$HOME/.uls_env"
PY="$VENV_DIR/bin/python3"
SMOKE=0
if [[ "${1:-}" == "--smoke" ]]; then SMOKE=1; fi

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

echo "[INFO] Verifying key imports (pyparsing, PDF backends)"
"$PY" - <<'PY'
errs = []
try:
    import pyparsing
except Exception as e:
    errs.append(f"pyparsing: {e}")
try:
    import fitz
    backend = 'PyMuPDF'
except Exception:
    try:
        import pdfplumber
        backend = 'pdfplumber'
    except Exception as e:
        errs.append(f"pdf backend: {e}")
        backend = 'none'
if errs:
    print('[WARN] Some optional components missing:')
    for m in errs:
        print(' -', m)
print('[INFO] PDF backend:', backend)
PY

echo "[ OK ] Environment ready at $VENV_DIR"
"$PY" -V
"$PY" -m pip --version
echo "\nNext steps:"
echo "  1) Run the tool: scripts/run_tool.sh"
echo "  2) Results will appear in ./results with HTML and JSON"

if [[ "$SMOKE" -eq 1 ]]; then
  REPO_ROOT="$(cd "$(dirname "$0")"/.. && pwd)"
  ENTRY="$REPO_ROOT/run_screening.py"
  JSON_DIR="$REPO_ROOT/test_results/extracted_json"
  TERMS="$REPO_ROOT/search_terms.txt"
  QUERY="$REPO_ROOT/examples/query.txt"
  OUT_DIR="$REPO_ROOT/results"
  if [[ -d "$JSON_DIR" ]]; then
    if [[ -f "$QUERY" ]]; then
      echo "[INFO] Running smoke test (query mode)"
      "$PY" "$ENTRY" --input "$JSON_DIR" --output "$OUT_DIR" --query-file "$QUERY" --config "$REPO_ROOT/config.json"
      echo "[ OK ] Smoke test completed"
    elif [[ -f "$TERMS" ]]; then
      echo "[INFO] Running smoke test (legacy mode)"
      "$PY" "$ENTRY" --input "$JSON_DIR" --output "$OUT_DIR" --search-terms "$TERMS" --config "$REPO_ROOT/config.json"
      echo "[ OK ] Smoke test completed"
    else
      echo "[WARN] Smoke test skipped: missing $QUERY and $TERMS"
    fi
  else
    echo "[WARN] Smoke test skipped: missing $JSON_DIR"
  fi
fi
