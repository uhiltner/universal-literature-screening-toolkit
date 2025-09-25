#!/usr/bin/env bash
set -euo pipefail

# ULST Runner Script (Unix)
# Uses ~/.uls_env to run run_screening.py with sensible defaults.

IN_DIR="${1:-./input_pdfs}"
OUT_DIR="${2:-./results}"
TERMS="${3:-./search_terms.txt}"
CONF="${4:-./config.json}"
QUERY_FILE="${5:-}"

REPO_ROOT="$(cd "$(dirname "$0")"/.. && pwd)"
ENTRY="$REPO_ROOT/run_screening.py"
VENV_DIR="$HOME/.uls_env"
PY="$VENV_DIR/bin/python3"

if [[ ! -x "$PY" ]]; then
  echo "[ERR ] venv not found at $VENV_DIR. Run scripts/setup_unix.sh first." >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

echo "[INFO] Running ULST with:"
echo "  --input        $IN_DIR"
echo "  --output       $OUT_DIR"
if [[ -n "$QUERY_FILE" ]]; then
  echo "  --query-file   $QUERY_FILE"
else
  echo "  --search-terms $TERMS"
fi
echo "  --config       $CONF"

if [[ -n "$QUERY_FILE" ]]; then
  "$PY" "$ENTRY" --input "$IN_DIR" --output "$OUT_DIR" --query-file "$QUERY_FILE" --config "$CONF"
else
  "$PY" "$ENTRY" --input "$IN_DIR" --output "$OUT_DIR" --search-terms "$TERMS" --config "$CONF"
fi

HTML="$OUT_DIR/validation_report.html"
JSON="$OUT_DIR/validation_results.json"

if [[ -f "$HTML" ]]; then
  echo "[ OK ] HTML report: $HTML"
else
  echo "[INFO] HTML report not found; check output for report filename"
fi

if [[ -f "$JSON" ]]; then
  echo "[ OK ] JSON results: $JSON"
else
  echo "[INFO] JSON results not found; check output for JSON save step"
fi

echo "[ OK ] Done"
