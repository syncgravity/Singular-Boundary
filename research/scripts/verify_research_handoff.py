#!/usr/bin/env python3
"""Verify a Singular Boundary handoff manifest against extracted, portable files.

Usage: python research/scripts/verify_research_handoff.py /path/to/extracted-package
       python research/scripts/verify_research_handoff.py /path/to/package.zip

Never executes bundled research code. Does not trust the manifest's original
absolute 'base' path. Exits nonzero on missing files, length/hash mismatch,
unsafe ZIP paths, or duplicate paths.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def valid_path(value):
    p = PurePosixPath(value)
    return bool(value) and not p.is_absolute() and '..' not in p.parts and '\\' not in value

def verify_records(records, read):
    if not isinstance(records, list) or not records:
        raise ValueError("empty or malformed files list")
    seen=set()
    for item in records:
        name=item['path']
        if not valid_path(name) or name in seen:
            raise ValueError(f"unsafe or duplicate path: {name}")
        seen.add(name)
        blob=read(name)
        expected_size=item.get('bytes')
        expected_sha=item.get('sha256')
        if len(blob)!=expected_size or sha256(blob)!=expected_sha:
            raise ValueError(f"size/hash mismatch: {name}")
    print(f"PASS: {len(records)} files match manifest SHA-256 and byte length")

def verify_dir(root):
    manifest=json.loads((root/'FILE_MANIFEST.json').read_text())
    def read(name):
        path=(root/name).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError(f"escape from root: {name}")
        return path.read_bytes()
    verify_records(manifest['files'],read)

def verify_zip(path):
    with zipfile.ZipFile(path) as archive:
        members=archive.namelist()
        if any(not valid_path(n.rstrip('/')) for n in members if not n.endswith('/')):
            raise ValueError("unsafe ZIP member")
        if len(members)!=len(set(members)):
            raise ValueError("duplicate ZIP members")
        if archive.testzip() is not None:
            raise ValueError("ZIP CRC failure")
        choices=[n for n in members if n.endswith('FILE_MANIFEST.json')]
        if len(choices)!=1:
            raise ValueError("expected exactly one FILE_MANIFEST.json")
        prefix=choices[0][:-len('FILE_MANIFEST.json')]
        manifest=json.loads(archive.read(choices[0]))
        def read(name):
            key=prefix+name
            if key not in members:
                raise FileNotFoundError(key)
            return archive.read(key)
        verify_records(manifest['files'],read)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('bundle',type=Path)
    args=parser.parse_args()
    try:
        if args.bundle.is_file():
            verify_zip(args.bundle)
        else:
            verify_dir(args.bundle)
    except (ValueError,KeyError,FileNotFoundError,zipfile.BadZipFile) as ex:
        print(f"FAIL: {ex}",file=sys.stderr)
        return 1
    return 0
if __name__=='__main__':
    raise SystemExit(main())
