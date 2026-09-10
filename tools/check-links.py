#!/usr/bin/env python3
"""
Check internal markdown links. Offline, stdlib only.

Usage:
    python3 tools/check-links.py
Exit 0 if all internal .md links resolve, 1 otherwise.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\]\(([^)#\s][^)]*?\.md[^)]*)\)")

broken = []
checked = 0
for md in sorted(ROOT.rglob("*.md")):
    if ".git/" in md.as_posix():
        continue
    text = md.read_text(errors="ignore")
    for m in LINK_RE.finditer(text):
        target = m.group(1).strip()
        if target.startswith("http"):
            continue
        checked += 1
        dest = (md.parent / target).resolve()
        try:
            dest.relative_to(ROOT)
        except ValueError:
            broken.append(f"{md.relative_to(ROOT)} -> {target} (outside repo)")
            continue
        if not dest.exists():
            broken.append(f"{md.relative_to(ROOT)} -> {target}")

print(f"Checked {checked} internal md links.")
if broken:
    print(f"BROKEN ({len(broken)}):")
    for b in broken:
        print(f"  {b}")
    sys.exit(1)
print("OK: all internal links resolve.")
