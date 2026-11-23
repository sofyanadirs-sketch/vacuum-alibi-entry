#!/usr/bin/env python3
"""One-line entry: a robot vacuum's alibi for a spot it never cleaned.

Builds a single deadpan alibi from three short fragments, prints it to
stdout, and writes it, with no trailing newline, to entry.txt inside the
output directory. The alibi is 118 characters: the vacuum's own cleaning
log claims spot 47 was cleaned at 14:03, its camera says it never left
the dock, and it trusts the log -- the camera is new here, so its word
counts for less. Concrete number, named machine artifacts, second twist.
"""

import os
from pathlib import Path


def build_line() -> str:
    claim = "My log says I cleaned spot 47 at 14:03."
    witness = " My camera says I never left the dock."
    verdict = " I trust the log; the camera is new here."
    return claim + witness + verdict


def main() -> None:
    line = build_line()
    if "\n" in line or line != line.strip():
        raise ValueError("entry must be one line with no surrounding whitespace")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(out_dir / "entry.txt", 0o644)
    print(line)


if __name__ == "__main__":
    main()
