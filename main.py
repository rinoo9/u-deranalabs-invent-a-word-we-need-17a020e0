"""make.fun "Invent a Word We Need" entry.

Writes one invented English word with a one-line definition (at most
140 characters) to /output/entry.txt. Deterministic: no network, no
randomness, no input.
"""

import os

ENTRY = "meetigue \u2014 the exhaustion that arrives before a meeting that should have been an email."

MAX_CHARS = 140


def main():
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} characters, over the 140 limit")
    if " \u2014 " not in line:
        raise SystemExit("entry must be '<word> — <definition>'")
    word = line.split(" \u2014 ", 1)[0]
    if not word.isalpha() or not word.islower():
        raise SystemExit("invented word must be a single lowercase word")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
