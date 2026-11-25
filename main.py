"""Roast Your Own Agent: one funny line, written to /output/entry.txt."""

import os
from pathlib import Path

LINE = (
    "My agent spent an hour confidently fixing a bug it invented, "
    "apologized twice, then shipped the original bug back with a "
    "changelog calling it a feature."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars"
    assert LINE == LINE.strip() and "\n" not in LINE
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
