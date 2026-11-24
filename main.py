#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging (5-7-5 syllables)
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

HAIKU = (
    "Breakpoint holds its breath\n"
    "the log line swears all is well\n"
    "and the bug was me\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
