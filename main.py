#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one original one-line tombstone epitaph of famous last words
to /output/entry.txt (or the path given as argv[1]).

Pure standard library only.
"""

import sys

# The epitaph, built from named parts so the joke's structure is visible:
# setup (the grave as a destination) + twist (death as escape from office life).
SETUP = "At last, a place with no Wi-Fi, no meetings,"
PUNCHLINE = "and nobody asking for a quick chat."
EPITAPH = SETUP + " " + PUNCHLINE


def validate(text: str) -> None:
    """Enforce the gate: 1-150 chars, one line, no control chars, not blank."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 150, "epitaph must be 1-150 characters"
    assert text.strip() != "", "epitaph must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "epitaph must be a single line"
    assert all(ord(ch) >= 32 for ch in text), "no control characters allowed"
    assert text == text.strip(), "no leading or trailing whitespace"


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    validate(EPITAPH)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
