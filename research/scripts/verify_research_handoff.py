#!/usr/bin/env python3
"""Verify portable handoff files without executing bundled code or following symlinks."""
import argparse
import hashlib
import json
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath


def valid_path(name):
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        return False
    p = PurePosixPath(name)
    return not p.is_absolute() and all(part not in ('', '.', '..') for part in name.split('/')) and ':' not in name.split('/')[0]


def records(manifest):
    if not isinstance(manifest, dict) or not isinstance(manifest.get('files'), list) or not manifest['files']:
        raise ValueError('empty or malformed files list')
    seen = set()
    for entry in manifest['files']:
        if not isinstance(entry, dict):
            raise ValueError('invalid manifest entry')
        name, size, digest = entry.get('path'), entry.get('bytes'), entry.get('sha256')
        if not valid_path(name) or name in seen:
            raise ValueError(f'unsafe or duplicate path: {name}')
        if type(size) is not int or size < 0 or not isinstance(digest, str) or len(digest) != 64 or any(ch not in '0123456789abcdef' for ch in digest):
            raise ValueError(f'invalid size or SHA256: {name}')
        seen.add(name)
        yield name, size, digest


def check(manifest, reader):
    total = 0
    for name, length, digest in records(manifest):
        data = reader(name)
        if len(data) != length or hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f'size/hash mismatch: {name}')
        total += 1
    print(f'PASS: {total} files match manifest SHA-256 and byte length')


def no_symlink_components(root, relative):
    p = root
    for part in relative.split('/'):
        p = p / part
        if p.is_symlink():
            raise ValueError(f'symlink is forbidden: {relative}')
    if not p.is_file():
        raise ValueError(f'not a regular file: {relative}')
    return p


def verify_dir(root):
    root = root.resolve(strict=True)
    manifest_file = no_symlink_components(root, 'FILE_MANIFEST.json')
    manifest = json.loads(manifest_file.read_text(encoding='utf-8'))
    check(manifest, lambda name: no_symlink_components(root, name).read_bytes())


def verify_zip(path):
    with zipfile.ZipFile(path) as z:
        members = z.infolist()
        seen = set()
        for info in members:
            name = info.filename
            is_dir = info.is_dir()
            rel = name[:-1] if is_dir else name
            if not valid_path(rel) or name in seen:
                raise ValueError(f'unsafe or duplicate ZIP entry: {name}')
            seen.add(name)
            if info.create_system == 3:
                mode = info.external_attr >> 16
                kind = stat.S_IFMT(mode)
                if kind not in (0, stat.S_IFDIR if is_dir else stat.S_IFREG):
                    raise ValueError(f'nonregular ZIP entry: {name}')
        choices = [x for x in seen if x.endswith('FILE_MANIFEST.json')]
        if len(choices) != 1:
            raise ValueError('expected exactly one FILE_MANIFEST.json')
        key = choices[0]
        prefix = key[:-len('FILE_MANIFEST.json')]
        manifest = json.loads(z.read(key))
        def read(name):
            member = prefix + name
            if member not in seen or member.endswith('/'):
                raise FileNotFoundError(member)
            return z.read(member)
        check(manifest, read)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('bundle', type=Path)
    args = ap.parse_args()
    try:
        if args.bundle.is_file():
            verify_zip(args.bundle)
        else:
            verify_dir(args.bundle)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError, zipfile.BadZipFile, RuntimeError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
