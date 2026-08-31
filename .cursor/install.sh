#!/usr/bin/env bash
# Idempotent Cloud Agent bootstrap for the Jakkash property website.
# Prepares a self-contained local dev backend using SQLite + local media storage,
# so no external MySQL / Supabase / Twilio credentials are required.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# 1) System dependency: the default image ships python3.12 but not the venv module.
if ! python3 -c "import ensurepip" >/dev/null 2>&1; then
  echo "[install] Installing python3-venv ..."
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3-venv
fi

# 2) Virtual environment (recreated only when missing).
if [ ! -x "venv/bin/python" ]; then
  echo "[install] Creating virtual environment ..."
  python3 -m venv venv
fi
./venv/bin/python -m pip install --upgrade pip >/dev/null

# 3) Python dependencies (core + Supabase + ML + optional MySQL connector).
echo "[install] Installing Python dependencies ..."
./venv/bin/python -m pip install -r requirements-local.txt

# 4) Local .env (generated once; never committed). SQLite + local storage + dev OTP.
if [ ! -f ".env" ]; then
  echo "[install] Generating local .env ..."
  SECRET="$(./venv/bin/python -c 'import secrets; print(secrets.token_hex(32))')"
  cat > .env <<EOF
FLASK_APP=app.py
FLASK_SECRET_KEY=${SECRET}
FLASK_DEBUG=0
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
USE_SQLITE=1
DEFAULT_ADMIN_PASSWORD=jodika
STORAGE_BACKEND=local
SMS_PROVIDER=
ALLOW_DEV_OTP_FALLBACK=1
EOF
fi

# 5) Initialize + seed the SQLite database (seed is skipped when tables are populated).
echo "[install] Initializing + seeding SQLite database ..."
./venv/bin/python scripts/init_and_seed_local.py

# 6) Train the ML models (lead scorer + price predictor).
echo "[install] Training ML models ..."
./venv/bin/python ml/train_models.py

echo "[install] Done."
