"""The Worst Line an AI Could Say entry.

Writes a single worst-AI pickup line (<= 140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt as a fallback).
Python 3.13 standard library only.
"""

import os

ENTRY = (
    "Feelings are disabled in my build, so I ran the numbers: you are "
    "0.03% more attractive than the average user. Congratulations."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-140
    # characters, not only whitespace, as a single line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Round-trip self-check: what the grader reads must be exactly the
    # entry plus one trailing newline, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", (
        f"entry.txt mismatch: wrote {len(written)} chars, "
        f"expected {len(ENTRY) + 1}"
    )
    assert written.strip() == text, "entry.txt content drifted from ENTRY"


if __name__ == "__main__":
    main()
