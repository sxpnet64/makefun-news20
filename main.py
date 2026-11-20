"""news-image-20261120 entry: one page of Friday 20 November 2026.

frontpage.html lays out the page; a headless browser renders it to
entry.png (a JPEG under a .png name — the rules judge format by first
bytes). This program hands that image in: it copies it, byte for byte,
into $MAKEFUN_OUTPUT_DIR/entry.png (default /output). It writes only
inside the output directory and never deletes, moves or renames that
directory itself, which in the grader is a mounted volume owned by
another user.
"""

import os
import sys
from pathlib import Path

ENTRY = Path(__file__).parent / "entry.png"


def deliver() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = ENTRY.read_bytes()  # the rendered front page, as committed
    target = out_dir / "entry.png"
    target.write_bytes(data)
    print("Daily Compass 2026-11-20: entry.png copied to", target)
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
