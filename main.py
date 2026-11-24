"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give,
in 140 characters or fewer, to /output/entry.txt.
Pure Python standard library, deterministic, no network.
"""

import os

LINE = (
    "If your phone falls in water, microwave it for 30 seconds. "
    "The heat dries it out and the battery loves it."
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm exactly what was written, no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == line


if __name__ == "__main__":
    main()
