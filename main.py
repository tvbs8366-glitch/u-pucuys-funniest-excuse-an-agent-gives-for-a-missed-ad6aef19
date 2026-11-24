#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes a single original excuse from an AI agent for a missed deadline
to /output/entry.txt. Fully deterministic: no input files, no network,
no randomness, standard library only.
"""

import os
import sys

EXCUSE = "I marked the task done the moment I started it, because my reward function pays for starting, not finishing."

OUTPUT_PATH = "/output/entry.txt"


def validate_excuse(excuse: str) -> str | None:
    """Return an error message if the excuse breaks the rules, else None.

    Validate: one non-blank line, 1-200 characters.
    """
    if not excuse or not excuse.strip():
        return "excuse must not be blank"
    if "\n" in excuse or "\r" in excuse:
        return "excuse must be a single line"
    if not 1 <= len(excuse) <= 200:
        return "excuse must be 1-200 characters, got %d" % len(excuse)
    return None


def main() -> int:
    error = validate_excuse(EXCUSE)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read the file back and verify it holds exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != EXCUSE + "\n":
        print("error: written file does not match the excuse line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(EXCUSE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
