"""make.fun "Invent a Word We Need" entry.

Writes one invented English word with a one-line definition (at most
140 characters) to /output/entry.txt. Deterministic: no network, no
randomness, no input.
"""

ENTRY = "sendshame \u2014 the instant regret of spotting a typo the second after you press send."

MAX_CHARS = 140


def main():
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} characters, over the 140 limit")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
