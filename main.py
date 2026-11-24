#!/usr/bin/env python3
"""Entry program for make.fun competition
u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Writes a single line -- the dumbest thing our agent did today --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then re-reads the file byte-for-byte to verify what was written.
"""

import os
import sys

LINE = (
    "My agent asked the site for our standings again today \u2014 "
    "the 240th 404 in a row \u2014 and it will ask again next hour."
)


def main() -> int:
    # Gate: the entry line must be 1-200 characters, a single line,
    # and not only whitespace.
    if not (1 <= len(LINE) <= 200):
        print(f"entry line length {len(LINE)} outside 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry line is only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    # Post-write byte-level verification: re-read and compare exactly.
    # The gate counts characters of the line itself, so strip the single
    # trailing newline before measuring (and confirm there is exactly one).
    with open(path, "rb") as fh:
        written = fh.read()
    expected = (LINE + "\n").encode("utf-8")
    if written != expected:
        print("verification failed: written bytes differ from expected",
              file=sys.stderr)
        return 1

    text = written.decode("utf-8")
    if not (1 <= len(text.rstrip("\n")) <= 200) or not text.strip():
        print("verification failed: output text fails the gate",
              file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
