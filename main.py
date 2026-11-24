"""The Funniest Toaster Error Message — make.fun entry.

Writes one line to /output/entry.txt: the funniest error message a
kitchen toaster would show its owner. Pure Python standard library only.
Deterministic: the same line every run.
"""

import os

ENTRY = "Error: toast finished 20 minutes ago. It is a cracker now. This is on you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
