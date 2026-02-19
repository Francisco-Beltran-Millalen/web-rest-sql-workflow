#!/usr/bin/env python3
"""
convert_transcript_generic.py
Abstract base class for converting LLM CLI transcripts to readable text.

To add support for a new LLM CLI tool:
  1. Create convert_transcript_<tool>.py
  2. Subclass TranscriptConverter
  3. Implement tool_name() and parse_transcript()

Usage (via subclass):
  ./convert_transcript_<tool>.py <transcript_file> [output.txt]

Requires: Python 3 (see PREREQUISITES.md)
"""

import sys
from abc import ABC, abstractmethod
from datetime import datetime


class TranscriptConverter(ABC):
    """Base class for LLM transcript converters.

    Subclasses must implement:
      - tool_name()       → str
      - parse_transcript() → list of message dicts

    Message dict format:
      {
        "role":  "user" | "assistant",
        "text":  str,
        "tools": [str, ...]   # tool names called (assistant only)
      }
    """

    @abstractmethod
    def tool_name(self) -> str:
        """Return the display name of the LLM CLI tool (e.g. 'Claude Code')."""
        pass

    @abstractmethod
    def parse_transcript(self, path: str) -> list:
        """Parse a tool-specific transcript file into a list of message dicts."""
        pass

    # ------------------------------------------------------------------ #
    # Concrete methods — shared across all tools                          #
    # ------------------------------------------------------------------ #

    def header(self) -> str:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return "\n".join([
            "============================================",
            f"{self.tool_name()} Conversation Transcript",
            f"Exported: {now}",
            "============================================",
        ])

    def format_output(self, messages: list) -> str:
        lines = []
        for msg in messages:
            role = msg.get("role", "")
            text = msg.get("text", "")
            tools = msg.get("tools", [])

            if role == "user" and text:
                lines.append("")
                lines.append("--- USER ---")
                lines.append(text)
            elif role == "assistant":
                if text:
                    lines.append("")
                    lines.append("--- ASSISTANT ---")
                    lines.append(text)
                for tool in tools:
                    lines.append(f"  [Tool: {tool}]")

        return "\n".join(lines)

    def convert(self, path: str) -> str:
        messages = self.parse_transcript(path)
        return self.header() + "\n" + self.format_output(messages)

    def main(self):
        if len(sys.argv) < 2:
            print(f"Usage: {sys.argv[0]} <transcript_file> [output.txt]", file=sys.stderr)
            sys.exit(1)

        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None

        try:
            result = self.convert(input_path)
        except FileNotFoundError:
            print(f"Error: File not found: {input_path}", file=sys.stderr)
            sys.exit(1)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Converted to: {output_path}", file=sys.stderr)
        else:
            print(result)
