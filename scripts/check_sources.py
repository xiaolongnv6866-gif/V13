#!/usr/bin/env python3
"""V13 source-identity preflight. Prints metadata only; never exports novel prose."""
from pathlib import Path
import hashlib
import os
import zipfile
import sys

EXPECTED = {
    "晚明": "a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082",
    "铁血残明": "9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf",
}
def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for block in iter(lambda: fp.read(1024*1024), b""): h.update(block)
    return h.hexdigest()

def main():
    root = Path(os.getenv("V13_EPUB_DIR", "/mnt/data"))
    errors = 0
    for name, expected in EXPECTED.items():
        found = sorted(set(root.glob(name+" *.epub")) | set(root.glob(name+".epub")))
        if len(found) != 1:
            print(f"FAIL {name}: expected exactly 1 supplied EPUB in {root}, found {len(found)}")
            errors += 1
            continue
        path = found[0]
        actual = digest(path)
        try:
            with zipfile.ZipFile(path) as z:
                bad = z.testzip()
                count = len(z.namelist())
        except Exception as e:
            print(f"FAIL {name}: invalid ZIP: {e}"); errors += 1; continue
        ok = actual == expected and bad is None
        print(f"{'PASS' if ok else 'FAIL'} {name}: SHA256={actual}; zip_items={count}; corrupt={bad}")
        if not ok: errors += 1
    return min(errors,1)

if __name__=="__main__":sys.exit(main())
