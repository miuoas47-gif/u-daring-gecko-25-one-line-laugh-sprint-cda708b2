#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output), then reads it back to verify it is exactly
one line of 1-280 characters. Deterministic: the same line every run.
Standard library only, no network, no arguments.
"""

import os
import sys

LINE = (
    "I asked my smart fridge for a joke and it said, "
    "'Sorry, I'm fresh out - just like your milk, your motivation, "
    "and those leftovers from 2019.'"
)


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 main.py (takes no arguments)", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        print("error: line must be a single non-empty line", file=sys.stderr)
        return 1
    if len(line) > 280:
        print("error: line exceeds 280 characters", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        stored = handle.read()
    if stored != line + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print("Wrote one-liner (%d chars) to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
