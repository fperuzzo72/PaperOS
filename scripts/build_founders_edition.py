#!/usr/bin/env python3
"""Concatenate FoundersEdition/src/*.md into the single-file manuscript.

Source files are numbered (01-Preface-Notes.md, 02-Chapter01.md, ...)
and are joined in that order, separated by a horizontal rule. The
preface notes file is working material, not part of the manuscript,
so it is skipped.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "FoundersEdition" / "src"
OUTPUT = REPO_ROOT / "FoundersEdition" / "FoundersEdition.md"
SEPARATOR = "\n\n\n---\n\n"


def main() -> None:
    files = sorted(
        f for f in SRC_DIR.glob("*.md") if "Preface-Notes" not in f.name
    )
    if not files:
        raise SystemExit(f"No source chapters found in {SRC_DIR}")

    chapters = [f.read_text(encoding="utf-8").rstrip("\n") for f in files]
    manuscript = SEPARATOR.join(chapters) + "\n"

    OUTPUT.write_text(manuscript, encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(REPO_ROOT)} from {len(files)} chapters:")
    for f in files:
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
