#!/usr/bin/env python3
"""
convert_transcript_claude.py
Converts a Claude Code JSONL transcript to readable text.

Extends convert_transcript_generic.py with Claude-specific parsing logic.

Usage:
  ./workflow/scripts/convert_transcript_claude.py <transcript.jsonl> [output.txt]

Requires: Python 3 (see PREREQUISITES.md)
"""

import json
import sys
from pathlib import Path

# Import generic base from the same directory
sys.path.insert(0, str(Path(__file__).parent))
from convert_transcript_generic import TranscriptConverter


class ClaudeTranscriptConverter(TranscriptConverter):

    def tool_name(self) -> str:
        return "Claude Code"

    def parse_transcript(self, path: str) -> list:
        """Parse Claude Code's JSONL transcript format."""
        messages = []

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue

                entry_type = entry.get("type", "")
                content = entry.get("message", {}).get("content", "")

                if entry_type == "user":
                    text = self._extract_text(content)
                    if text:
                        messages.append({"role": "user", "text": text, "tools": []})

                elif entry_type == "assistant":
                    text = self._extract_text(content)
                    tools = self._extract_tools(content)
                    if text or tools:
                        messages.append({"role": "assistant", "text": text, "tools": tools})

        return messages

    def _extract_text(self, content) -> str:
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "\n".join(
                block.get("text", "")
                for block in content
                if block.get("type") == "text"
            )
        return ""

    def _extract_tools(self, content) -> list:
        if not isinstance(content, list):
            return []
        return [
            block.get("name", "")
            for block in content
            if block.get("type") == "tool_use"
        ]


if __name__ == "__main__":
    ClaudeTranscriptConverter().main()
