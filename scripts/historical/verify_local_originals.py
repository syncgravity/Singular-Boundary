#!/usr/bin/env python3
"""Read-only verification of immutable original research assets against the canonical manifest.
Usage: python scripts/historical/verify_local_originals.py /path/to/originals
Exit 0 only when every manifest-listed original exists and matches its recorded size/hash.
No source file is changed.
"""
import csv
import hashlib
import pathlib
import sys
import tarfile
import zipfile

MANIFEST = pathlib.Path(__file__).resolve().parents[2] / "sources/source-manifests/SESSION_ARTIFACT_SHA256_2026-10-30.csv"

def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    missing, invalid, good = [], [], []
    with MANIFEST.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for row in rows:
        name = row["filename"]
        path = root / name
        if not path.is_file():
            missing.append(name)
            continue
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        if path.stat().st_size != int(row["size_bytes"]) or digest.hexdigest() != row["sha256"]:
            invalid.append((name, "size or SHA256 mismatch"))
            continue
        try:
            if name.endswith((".zip", ".npz")):
                with zipfile.ZipFile(path) as z:
                    bad = z.testzip()
                    if bad is not None:
                        raise ValueError("bad archive member: " + bad)
            elif name.endswith(".tar.gz"):
                with tarfile.open(path, "r:gz") as t:
                    for member in t:
                        if member.isfile():
                            stream = t.extractfile(member)
                            if stream:
                                for _ in iter(lambda: stream.read(1024 * 1024), b""):
                                    pass
        except Exception as exc:
            invalid.append((name, "archive integrity: " + str(exc)))
            continue
        good.append(name)
    print(f"VERIFIED={len(good)} MISSING={len(missing)} INVALID={len(invalid)} TOTAL={len(rows)}")
    for name in missing:
        print("MISSING:", name)
    for name, reason in invalid:
        print("INVALID:", name, reason)
    return 1 if missing or invalid else 0

if __name__ == "__main__":
    raise SystemExit(main())
