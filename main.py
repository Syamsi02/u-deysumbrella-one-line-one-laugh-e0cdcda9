#!/usr/bin/env python3
"""One Line, One Laugh -- a single funny line, written to /output/entry.txt.

Pure standard library. Deterministic: every run prints and writes the
same one line, so the judged text never changes between runs.
"""

import os

# The gate allows 1-140 characters of UTF-8 text; this line is 104.
JOKE = (
    "I asked my AI agent for a joke, so it charged me $2 for the laugh "
    "and submitted itself as the punchline."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"joke must be 1-140 characters, got {len(text)}")
    if "\n" in text:
        raise SystemExit("joke must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
