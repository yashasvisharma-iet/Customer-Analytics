#!/usr/bin/env bash
# Activate the project's virtualenv (if present) and run app.py
set -euo pipefail

ROOT_DIR="$(dirname "$0")"
cd "$ROOT_DIR"

if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
else
  echo "Warning: .venv not found. Assuming 'python' on PATH is correct."
fi

python app.py
