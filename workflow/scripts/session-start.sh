#!/bin/bash

# session-start.sh
# Starts the auto-export background process on session start
#
# Usage:
#   Called by SessionStart hook via stdin JSON
#   echo '{"transcript_path": "/path/to/transcript.jsonl"}' | ./workflow/scripts/session-start.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
AUTO_EXPORT_SCRIPT="$SCRIPT_DIR/auto-export.sh"
OUTPUT_DIR="$PROJECT_DIR/docs/logs"
INTERVAL=300  # 5 minutes in seconds
PYTHON=""
for cmd in python3 python py; do
  if command -v "$cmd" &>/dev/null && "$cmd" -c "import sys; sys.exit(0)" &>/dev/null; then
    PYTHON="$cmd"; break
  fi
done

# Read JSON input from stdin
INPUT=$(cat)

# Extract transcript path
TRANSCRIPT_PATH=$(echo "$INPUT" | $PYTHON -c "import sys, json; print(json.load(sys.stdin).get('transcript_path', ''))")

if [ -z "$TRANSCRIPT_PATH" ]; then
    echo "Error: No transcript_path in input" >&2
    exit 1
fi

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Start auto-export in background
nohup "$AUTO_EXPORT_SCRIPT" "$TRANSCRIPT_PATH" "$OUTPUT_DIR" "$INTERVAL" > /dev/null 2>&1 &

echo "Auto-export started (every ${INTERVAL}s)"