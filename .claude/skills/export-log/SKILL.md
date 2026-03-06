---
name: export-log
description: Export the current conversation to docs/logs/
allowed-tools: Bash
---

Read `.agent-utils/skills/export-log/SKILL.md` for the naming convention and stage names.

## Claude Code — Transcript Location

Use Python to find the project root (via `AGENTS.md` marker), encode the path the way Claude does, and locate the transcript. Works on Windows and Unix without any path assumptions.

```bash
PYTHON=""
for cmd in python3 python py; do
  if command -v "$cmd" &>/dev/null && "$cmd" -c "import sys; sys.exit(0)" &>/dev/null; then
    PYTHON="$cmd"; break
  fi
done
OUTPUT=$($PYTHON -c "
import os, glob

# Find project root by searching upward for AGENTS.md
d = os.getcwd()
while True:
    if os.path.exists(os.path.join(d, 'AGENTS.md')):
        break
    parent = os.path.dirname(d)
    if parent == d:
        break
    d = parent

# Encode path the way Claude does — use os.sep to avoid backslash escaping issues
encoded = d.replace(os.sep, '-').replace(':', '-').replace('/', '-')

# Find the most recent transcript for this project
home = os.path.expanduser('~')
pattern = os.path.join(home, '.claude', 'projects', encoded, '*.jsonl')
files = glob.glob(pattern)
transcript = sorted(files, key=os.path.getmtime)[-1] if files else ''
print(d + '|' + transcript)
")
PROJECT_ROOT="${OUTPUT%%|*}"
TRANSCRIPT="${OUTPUT##*|}"
```

## Claude Code — Converter

```bash
TIMESTAMP=$(date '+%Y%m%d-%H%M%S')
$PYTHON "$PROJECT_ROOT/workflow/scripts/convert_transcript_claude.py" \
  "$TRANSCRIPT" \
  "$PROJECT_ROOT/docs/logs/stage-<identifier>-<name>-${TIMESTAMP}.txt"
```

Arguments: `$ARGUMENTS`
