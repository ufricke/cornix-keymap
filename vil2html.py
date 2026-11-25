#!/usr/bin/env python3
"""Render a Vial .vil export of the Cornix keymap as a printable HTML reference.

Usage: vil2html.py <layout.vil> [output.html]   (default output: <layout>.html next to the .vil)
"""
import datetime
import html
import json
import pathlib
import sys

TEMPLATE = pathlib.Path(__file__).with_name("keymap-template.html")


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__.strip())
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix(".html")
    vil = json.loads(src.read_text())
    if "layout" not in vil or "encoder_layout" not in vil:
        sys.exit(f"{src}: not a Vial .vil file (no layout/encoder_layout)")
    page = (TEMPLATE.read_text()
            .replace("__VIL__", json.dumps(vil, ensure_ascii=False))
            .replace("__SOURCE__", html.escape(src.name))
            .replace("__DATE__", f"{datetime.date.today():%-d %B %Y}"))
    out.write_text(page)
    print(out)


if __name__ == "__main__":
    main()
