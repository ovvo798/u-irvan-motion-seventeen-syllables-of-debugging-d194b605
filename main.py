#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging (5-7-5 syllables)
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

HAIKU = (
    "Cursor blinks past three\n"
    "the stack trace still swears I'm right\n"
    "off by one, again\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
