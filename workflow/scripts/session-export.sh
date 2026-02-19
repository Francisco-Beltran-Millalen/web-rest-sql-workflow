#!/bin/bash

# session-export.sh
# Cleans up the auto-export background process on session end
# Does NOT create automatic exports - use /export-log for final logs
#
# Usage:
#   Called by SessionEnd hook via stdin JSON
#   echo '{"transcript_path": "/path/to/transcript.jsonl"}' | ./workflow/scripts/session-export.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$PROJECT_DIR/docs/logs"
PID_FILE="$OUTPUT_DIR/.auto-export.pid"

# Read JSON input from stdin (required by hook)
cat > /dev/null

# Kill auto-export background process if running
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID" 2>/dev/null || true
    fi
    rm -f "$PID_FILE"
fi

# Clean up any temporary auto-export files
rm -f "$OUTPUT_DIR"/session-*.txt 2>/dev/null || true

echo "Session cleanup complete"