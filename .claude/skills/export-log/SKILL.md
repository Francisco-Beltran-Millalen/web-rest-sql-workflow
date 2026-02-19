---
name: export-log
description: Export the current conversation to docs/logs/
allowed-tools: Bash
---

Read `.agent-utils/skills/export-log/SKILL.md` for the naming convention and stage names.

## Claude Code — Transcript Location

Find the transcript using the current project path:

```bash
ENCODED_PATH=$(pwd | sed 's|/|-|g')
PROJECTS_DIR="$HOME/.claude/projects/${ENCODED_PATH}"
TRANSCRIPT=$(ls -t "${PROJECTS_DIR}"/*.jsonl 2>/dev/null | head -1)
```

## Claude Code — Converter

```bash
TIMESTAMP=$(date '+%Y%m%d-%H%M%S')
python3 ./workflow/scripts/convert_transcript_claude.py \
  "$TRANSCRIPT" \
  docs/logs/stage-<identifier>-<name>-${TIMESTAMP}.txt
```

Arguments: `$ARGUMENTS`
