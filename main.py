"""Out of Tokens, Mid-Sentence.

Writes the one-line error message an AI agent shows when it runs out
of tokens mid-sentence to /output/entry.txt.

Pure Python standard library, no network.
"""

import os

LINE_PARTS = (
    "I was about to reveal the meaning of life ",
    "when my context window ran out, so please enjoy ",
    "this sentence inste\u2014",
)

LINE = "".join(LINE_PARTS)

MAX_LEN = 140


def main():
    line = LINE
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    assert 1 <= len(line) <= MAX_LEN, f"line must be 1-{MAX_LEN} characters, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
