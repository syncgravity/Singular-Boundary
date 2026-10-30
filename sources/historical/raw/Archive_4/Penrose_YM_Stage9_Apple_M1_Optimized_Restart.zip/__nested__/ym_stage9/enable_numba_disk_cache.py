#!/usr/bin/env python3
"""Optional startup optimization: enable Numba disk cache, leaving kernel bodies intact.

Only replaces lines that are exactly '@njit' with '@njit(cache=True)'.
Copies originals to .pre_m1_numba_cache.py before writing. Does not
change simulation algorithms, seeds, coupling parameters, or file format.
"""
from pathlib import Path
import argparse
import difflib
import sys

ROOT = Path(__file__).resolve().parent
TARGETS = ('stage7_checkpointed.py', 'wilson_torus.py')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--apply',action='store_true',help='back up originals then apply')
    p.add_argument('--restore',action='store_true',help='restore backed-up originals')
    args=p.parse_args()
    if args.apply and args.restore:
        p.error('Select either --apply or --restore')
    for filename in TARGETS:
        f=ROOT/filename
        backup=ROOT/(f.stem+'.pre_m1_numba_cache.py')
        if not f.is_file():
            raise SystemExit(f'Missing {f}; place this script alongside original Stage 9 source files')
        if args.restore:
            if not backup.exists():
                raise SystemExit(f'Missing backup {backup}; no change made')
            f.write_bytes(backup.read_bytes())
            print(f'Restored {filename} from backup')
            continue
        old=f.read_text()
        lines=old.splitlines(keepends=True)
        count=sum(s.strip()=='@njit' for s in lines)
        changed=''.join(s.replace('@njit','@njit(cache=True)',1) if s.strip()=='@njit' else s for s in lines)
        if count == 0:
            if '@njit(cache=True)' in old:
                print(f'Already cached: {filename}')
                continue
            raise SystemExit(f'Unexpected source decorators in {filename}; refusing to patch')
        print(f'{filename}: would enable disk caching on {count} JIT functions')
        if args.apply:
            if backup.exists():
                raise SystemExit(f'Refusing to overwrite existing backup {backup}')
            backup.write_bytes(f.read_bytes())
            f.write_text(changed)
            print(f'Applied patch; original at {backup.name}')
    if not args.apply and not args.restore:
        print('DRY RUN ONLY; pass --apply to enable.')


if __name__=='__main__':
    main()
