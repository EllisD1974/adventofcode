#!/usr/bin/env bash
# Re-run a script whenever a .py file changes.
# Usage: ./watch.sh day2/day2.py
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <script.py>" >&2
    exit 1
fi

script="$(realpath "$1")"
cd "$(dirname "$script")"
watchexec -e py -- python "$(basename "$script")"
