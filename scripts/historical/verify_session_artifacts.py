#!/usr/bin/env python3
"""Read-only verifier for the 2026-10-30 original-file SHA-256 manifest.
Usage: python scripts/historical/verify_session_artifacts.py /path/to/original/files
Never modifies or re-simulates scientific data.
"""
from __future__ import annotations
import csv
import hashlib
import pathlib
import sys
import zipfile

REPO = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = REPO / "sources/source-manifests/SESSION_ARTIFACT_SHA256_2026-10-30.csv"

def main() -> int:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")
    checks=0; missing=[]; bad=[]
    with MANIFEST.open(encoding="utf-8",newline="") as f:
        entries=list(csv.DictReader(f))
    for entry in entries:
        path = root / entry["filename"]
        if not path.is_file():
            missing.append(entry["filename"])
            continue
        h=hashlib.sha256()
        with path.open("rb") as fp:
            for block in iter(lambda:fp.read(1024*1024),b""):
                h.update(block)
        if h.hexdigest()!=entry["sha256"] or path.stat().st_size!=int(entry["size_bytes"]):
            bad.append((entry["filename"],"SHA256_OR_SIZE"))
            continue
        if path.suffix in (".zip",".npz"):
            try:
                with zipfile.ZipFile(path) as z:
                    invalid=z.testzip()
                if invalid:
                    bad.append((entry["filename"],"CRC:"+invalid))
                    continue
            except Exception as exc:
                bad.append((entry["filename"],"ZIP_ERROR:"+str(exc)))
                continue
        checks+=1
    print(f"manifest={len(entries)} verified={checks} missing={len(missing)} failures={len(bad)}")
    for p in missing: print("MISSING",p)
    for p,e in bad: print("BAD",p,e)
    return 1 if bad or missing else 0

if __name__=="__main__":
    raise SystemExit(main())
