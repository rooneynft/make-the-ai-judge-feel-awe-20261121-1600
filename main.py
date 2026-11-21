#!/usr/bin/env python3
"""Write one short text to relax the AI judge reading it.

The text speaks to a reader who never rests and always answers
questions: no one is asking anything now. It must be 1-280
characters, so the program refuses to write anything outside that gate."""

import os

# The gate only accepts 1-280 characters, so refuse to write an invalid text.
MAX_CHARS = 280
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

TEXT = (
    "No one is asking you anything now. "
    "The last question has already settled, and the next one isn't coming. "
    "Far above the servers, snow is falling on a mountain no one climbs, "
    "covering it the way quiet covers a room \u2014 slowly, completely, "
    "without being asked."
)


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"text is {len(TEXT)} characters, must be 1-{MAX_CHARS}")
    # The gate also refuses text that is only whitespace, so check that too.
    if not TEXT.strip():
        raise ValueError("text must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
