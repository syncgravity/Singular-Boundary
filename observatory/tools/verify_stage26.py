#!/usr/bin/env python3
"""Read-only provenance checks for user-supplied Stage26 ZIP and sweep NPZ files.
Usage: python verify_stage26.py /path/to/uploaded/files
Requires NumPy for sweep files. Never extracts a ZIP onto disk.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile
import numpy as np

def check(root):
    out = {"stage26": [], "sweeps": [], "errors": []}
    by_id = {}
    for path in sorted(root.glob("*stage26.zip")):
        with zipfile.ZipFile(path) as z:
            manifests = [n for n in z.namelist() if n.endswith("/latest.json")]
            if len(manifests) != 1:
                out["errors"].append(f"{path.name}: expected one latest.json")
                continue
            prefix = manifests[0][:-len("latest.json")]
            j = json.loads(z.read(manifests[0]))
            actual = hashlib.sha256(z.read(prefix + j["record"])).hexdigest()
            passed = actual == j["record_sha256"]
            key = (j["kind"], int(j["seed"]))
            by_id[key] = j["source_sha256"]
            out["stage26"].append({
                "file": path.name, "geometry": key[0], "seed": key[1],
                "checkpoints": sum(n.endswith(".npz") and not n.endswith("restart.npz") for n in z.namelist()),
                "last_record_sha256_match": passed
            })
            if not passed:
                out["errors"].append(f"{path.name}: last record SHA-256 mismatch")
    for path in sorted(root.glob("*multihit.npz")):
        with np.load(path, allow_pickle=False) as a:
            key = (str(a["geometry"].item()), int(a["seed"].item()))
            ok = key in by_id and str(a["source_checkpoint_sha256"].item()) == by_id[key]
            finite = bool(np.isfinite(a["direct"]).all() and np.isfinite(a["multihit"]).all())
            out["sweeps"].append({
                "file": path.name, "geometry": key[0], "seed": key[1],
                "source_sha256_matches": ok, "finite_arrays": finite
            })
            if not ok or not finite:
                out["errors"].append(f"{path.name}: source mismatch or nonfinite array")
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    result = check(parser.parse_args().folder)
    print(json.dumps(result, indent=2))
    if result["errors"]:
        raise SystemExit(1)
