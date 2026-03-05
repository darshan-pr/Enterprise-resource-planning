#!/usr/bin/env bash
set -e

cd ug_feedback_system

if [ "${SEED_TEST_USERS:-false}" = "true" ]; then
  echo "[startup] Seeding test users..."
  python create_test_users.py
else
  echo "[startup] Skipping test user seed (SEED_TEST_USERS=false)"
fi

exec gunicorn wsgi:app --bind 0.0.0.0:${PORT:-5000}
