#!/usr/bin/env bash
set -uo pipefail
uv run python src/index.py &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null || true' EXIT
for i in $(seq 1 60); do
  if curl -fsS http://localhost:5001/ >/dev/null 2>&1; then
    break
  fi
  sleep 1
done
curl -fsS http://localhost:5001/ >/dev/null
uv run robot --variable HEADLESS:true src/tests
