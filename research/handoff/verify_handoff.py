#!/usr/bin/env python3
"""Verify durable Singular Boundary handoff snapshots before using their results.

Usage: python verify_handoff.py /path/to/singular_boundary_handoff_core_R3-IR-539.zip
"""
import hashlib
import pathlib
import sys
import zipfile

KNOWN = {
 "singular_boundary_handoff_core_R3-IR-539.zip": "b3eafb36d8901a77491f326edd18a57ec48e1666b1677afb40f7b59bef87b632",
 "singular_boundary_handoff_full.zip": "2cbf21808b6a26dacbe81d72d06cfea65b5feae73294b2a0082f790b0d4a9100",
 "m5_whitney_candidate_2026-10-30.npz": "55a0d1b731355b59d64ce5535d029913b72fe1bcea595e2375d1f90b98d47334",
}
def verify(path):
    p=pathlib.Path(path)
    if not p.is_file():
        raise FileNotFoundError(path)
    h=hashlib.sha256()
    with p.open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024),b""):
            h.update(block)
    want=KNOWN.get(p.name)
    if want is None:
        raise ValueError("Unrecognized basename: cannot authenticate artifact from this list")
    if h.hexdigest()!=want:
        raise ValueError("SHA-256 MISMATCH for "+p.name)
    if p.suffix==".zip":
        with zipfile.ZipFile(p) as z:
            bad=z.testzip()
            if bad is not None:
                raise ValueError("Corrupt ZIP entry "+bad)
            if "FILE_MANIFEST.json" not in z.namelist():
                raise ValueError("Handoff ZIP lacks FILE_MANIFEST.json")
    print("VERIFIED",p.name,h.hexdigest())
if __name__=="__main__":
    if len(sys.argv)<2:
        raise SystemExit("Usage: python verify_handoff.py <artifact> [...]")
    for item in sys.argv[1:]:
        verify(item)
