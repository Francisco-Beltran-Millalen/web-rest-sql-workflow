#!/bin/bash

# auto-export.sh
# Background script that exports the conversation transcript periodically
#
# Usage:
#   ./workflow/scripts/auto-export.sh <transcript_path> <output_dir> <interval_seconds> &
#
# Called by SessionStart hook, killed by SessionEnd hook

set -e

TRANSCRIPT_PATH="$1"
OUTPUT_DIR="$2"
INTERVAL="${3:-300}"  # Default 5 minutes (300 seconds)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONVERT_SCRIPT="$SCRIPT_DIR/convert_transcript_claude.py"
PID_FILE="$OUTPUT_DIR/.auto-export.pid"

# Save PID for later cleanup
echo $$ > "$PID_FILE"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Function to export
do_export() {
    local timestamp=$(date '+%Y%m%d-%H%M%S')
    local output_file="$OUTPUT_DIR/session-$timestamp.txt"

    if [ -f "$TRANSCRIPT_PATH" ]; then
        "$CONVERT_SCRIPT" "$TRANSCRIPT_PATH" "$output_file" 2>/dev/null
    fi
}

# Cleanup on exit
cleanup() {
    rm -f "$PID_FILE"
    exit 0
}
trap cleanup EXIT INT TERM

# Main loop - export every INTERVAL seconds
while true; do
    sleep "$INTERVAL"
    do_export
done