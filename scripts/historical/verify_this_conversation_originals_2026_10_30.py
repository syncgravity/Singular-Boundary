#!/usr/bin/env python3
"""Read-only original-byte verifier for the Oct 26–30 Paper3/R3/R2 intake.
The manifest originates from actual mounted local bytes. It is NOT evidence
of LFS remote upload until run against a freshly cloned, LFS-pulled tree.
"""
import argparse
import csv
import hashlib
from pathlib import Path
import sys
import zipfile

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clone_root", type=Path)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--test-zip-crc", action="store_true")
    args = ap.parse_args()
    rows = list(csv.DictReader(args.manifest.open(encoding="utf-8", newline="")))
    errors = []
    for row in rows:
        path = args.clone_root / row["intended_repository_path"]
        if not path.is_file():
            errors.append((str(path), "MISSING"))
            continue
        if path.stat().st_size != int(row["size_bytes"]):
            errors.append((str(path), "SIZE_MISMATCH"))
            continue
        if sha256(path) != row["sha256"]:
            errors.append((str(path), "SHA256_MISMATCH"))
            continue
        if args.test_zip_crc and path.name.endswith((".zip", ".npz")):
            try:
                with zipfile.ZipFile(path) as archive:
                    bad = archive.testzip()
                if bad:
                    errors.append((str(path), f"BAD_MEMBER:{bad}"))
            except Exception as exc:
                errors.append((str(path), f"ZIP_ERROR:{exc}"))
    print(f"checked={len(rows)} missing_or_corrupt={len(errors)}")
    for path, reason in errors:
        print(f"{reason}  {path}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
