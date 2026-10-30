#!/usr/bin/env python3
"""Stage 9 Apple Silicon-safe management of independent SU(2) gauge chains.

This program ONLY launches the original, unmodified stage7_checkpointed.py
Metropolis sampler. It does not change coupling definitions, random-number
sequences, thermalization policy, or scientific acceptance gates.

Compatible with Python >= 3.10 on macOS/Linux. Optional concurrency: 2 workers.
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
KINDS = ('square', 'penrose')
SEEDS = (101, 211, 307, 419)
EXPECTED = re.compile(r'^(?:square|penrose)_nt20_seed(?:101|211|307|419)(?:\.npz|\.partial\.npz|_progress\.json)$')
LOCKS = {'.stage9_local_driver.lock', '.stage9_m1_manager.lock'}
LOGS = ('stage9_m1_batch_log.jsonl', 'stage9_local_batch_log.jsonl')
THREAD_ENV = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'NUMBA_NUM_THREADS',
              'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS')


def root_of(args):
    root = Path(args.checkpoint_root)
    return (HERE / root).resolve() if not root.is_absolute() else root.resolve()


def checksum(path):
    h = hashlib.sha256()
    with path.open('rb') as src:
        for block in iter(lambda: src.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def paths(root, kind, seed):
    prefix = f'{kind}_nt20_seed{seed}'
    return root / (prefix + '.npz'), root / (prefix + '_progress.json')


def read_progress(root, kind, seed, verify_hash=False):
    gauge, meta = paths(root, kind, seed)
    exists = (gauge.exists(), meta.exists())
    if exists == (False, False):
        return None
    if exists != (True, True):
        raise RuntimeError(f'Half-written checkpoint pair: {gauge} and {meta}; stop and reconcile manually')
    j = json.loads(meta.read_text())
    settings = j['settings']
    expected = {'kind': kind, 'seed': seed, 'nt': 20, 'beta': 3.5, 'burn': 1000, 'thin': 10}
    for k, v in expected.items():
        if settings.get(k) != v:
            raise RuntimeError(f'Unexpected checkpoint setting {k}: {meta}')
    count = int(j['completed_sweeps'])
    if count < 0:
        raise RuntimeError(f'Invalid sweep count: {meta}')
    if verify_hash and checksum(gauge) != j['checkpoint_sha256']:
        raise RuntimeError(f'Checkpoint hash mismatch: {gauge}. The NPZ may be newer than the progress JSON. Do not overwrite it.')
    return j


def select(args):
    kinds = tuple(args.kinds)
    seeds = tuple(args.seeds)
    if not kinds or len(set(kinds)) != len(kinds):
        raise ValueError('Supply unique geometry kinds')
    if not seeds or len(set(seeds)) != len(seeds):
        raise ValueError('Supply unique seeds')
    return [(kind, seed) for kind in kinds for seed in seeds]


def show_status(root, selected, verify=False):
    total = 0
    for kind, seed in selected:
        j = read_progress(root, kind, seed, verify_hash=verify)
        if j is None:
            print(f'{kind:8s} seed={seed:3d}  not initialized')
        else:
            n = int(j['completed_sweeps'])
            total += n
            print(f'{kind:8s} seed={seed:3d}  sweeps={n:6d} / 10000  postburn={int(j.get("n_postburn_samples", 0)):5d}')
    print(f'Combined sweeps={total}; no mass or string-tension fit is claimed.')


def check_preconditions(root):
    if not (HERE / 'stage7_checkpointed.py').is_file():
        raise RuntimeError('Place this script in the extracted ym_stage9 folder alongside stage7_checkpointed.py')
    if not root.is_dir():
        root.mkdir(parents=True)
    if root.is_symlink():
        raise RuntimeError('Refusing symlinked checkpoint directory')


def acquire(root):
    handles = []
    for filename in sorted(LOCKS):
        lock_path = root / filename
        lf = lock_path.open('a+')
        try:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            for old in handles:
                fcntl.flock(old.fileno(), fcntl.LOCK_UN)
                old.close()
            lf.close()
            raise RuntimeError(f'Another Stage 9 driver is running: {lock_path}')
        handles.append(lf)
    return handles


def release(handles):
    for h in handles:
        fcntl.flock(h.fileno(), fcntl.LOCK_UN)
        h.close()


def run_one(root, kind, seed, before, limit, target, verify_hash, log_path):
    cmd = [sys.executable, str(HERE / 'stage7_checkpointed.py'),
           '--kind', kind, '--seed', str(seed), '--nt', '20', '--beta', '3.5',
           '--burn', '1000', '--thin', '10', '--total-sweeps', str(target),
           '--max-sweeps-this-run', str(limit), '--measure',
           '--checkpoint-root', str(root)]
    env = os.environ.copy()
    env.update({k: '1' for k in THREAD_ENV})
    start = time.monotonic()
    proc = subprocess.run(cmd, cwd=HERE, env=env, capture_output=True, text=True)
    dur = time.monotonic() - start
    if proc.returncode:
        raise RuntimeError(f'{kind} {seed} failed after {dur:.1f}s: {proc.stdout[-3000:]}\n{proc.stderr[-4000:]}')
    result = read_progress(root, kind, seed, verify_hash=verify_hash)
    expected = min(before + limit, target)
    if result is None or int(result['completed_sweeps']) != expected:
        raise RuntimeError(f'{kind} {seed}: after-run sweep count differs from expected {expected}. Inspect checkpoint.')
    if result.get('cache_error') is None or abs(float(result['cache_error'])) >= 1e-9:
        raise RuntimeError(f'{kind} {seed}: plaquette cache check failed')
    return {'utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'kind': kind, 'seed': seed, 'before': before, 'after': expected,
            'seconds': round(dur, 2), 'postburn': int(result['n_postburn_samples']),
            'sha256': result['checkpoint_sha256'], 'log_excerpt': proc.stdout.strip()[-400:]}


def cmd_run(args):
    root = root_of(args)
    check_preconditions(root)
    if args.chunk < 1 or args.target < 1 or args.max_hours < 0 or args.passes < 0:
        raise ValueError('Invalid chunk, target, maximum hours, or passes')
    if args.passes == 0 and args.max_hours == 0:
        raise ValueError('--passes 0 requires --max-hours to prevent an unintended unlimited run')
    selected = select(args)
    locks = acquire(root)
    try:
        for kind, seed in selected:
            read_progress(root, kind, seed, verify_hash=args.verify_hash)
        stamp = time.monotonic()
        end_time = stamp + args.max_hours * 3600 if args.max_hours else float('inf')
        log_path = root.parent / 'stage9_m1_batch_log.jsonl'
        round_no = 0
        while args.passes == 0 or round_no < args.passes:
            jobs = []
            for kind, seed in selected:
                p = read_progress(root, kind, seed, verify_hash=False)
                before = int(p['completed_sweeps']) if p else 0
                if before < args.target:
                    jobs.append((kind, seed, before))
            if not jobs:
                print('All selected chains reached target sweeps.', flush=True)
                break
            # Do not queue more jobs than available worker slots. Stops cleanly
            # after the in-flight batches, without interrupting a checkpoint.
            tasks = iter(jobs)
            with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
                inflight = {}
                while True:
                    while len(inflight) < args.workers and time.monotonic() < end_time:
                        try:
                            kind, seed, before = next(tasks)
                        except StopIteration:
                            break
                        limit = min(args.chunk, args.target - before)
                        print(f'START {kind:8s} seed={seed} {before} -> {before+limit}', flush=True)
                        fut = pool.submit(run_one, root, kind, seed, before, limit,
                                          args.target, args.verify_hash, log_path)
                        inflight[fut] = (kind, seed)
                    if not inflight:
                        break
                    finished, _ = futures.wait(inflight, return_when=futures.FIRST_COMPLETED)
                    for task in finished:
                        kind, seed = inflight.pop(task)
                        record = task.result()
                        with log_path.open('a') as handle:
                            handle.write(json.dumps(record, sort_keys=True) + '\n')
                        print('SAVED', json.dumps({k: record[k] for k in ('kind','seed','before','after','seconds','postburn')},sort_keys=True), flush=True)
                    if time.monotonic() >= end_time and not inflight:
                        break
            round_no += 1
            if time.monotonic() >= end_time:
                print('Time budget reached. No new segment scheduled; all completed segments checkpointed.', flush=True)
                break
        show_status(root, selected)
        print('Run stage9_requirement_audit.py after all eight chains have checkpoints.', flush=True)
    finally:
        release(locks)


def cmd_reset(args):
    root = root_of(args)
    if root != HERE / 'checkpoints':
        raise RuntimeError('For safety, reset can only target ./checkpoints in the ym_stage9 folder')
    if root.is_symlink():
        raise RuntimeError('Will not reset a symlink')
    if not root.exists():
        print('No checkpoint directory exists; a fresh run will initialize it.')
        return
    entries = list(root.iterdir())
    unknown = [p.name for p in entries if not (EXPECTED.match(p.name) or p.name in LOCKS)]
    if unknown:
        raise RuntimeError(f'Unexpected files in checkpoints; no changes made: {unknown}')
    logfiles = [HERE / name for name in LOGS if (HERE / name).is_file()]
    print(f'Checkpoint reset inspection: {len(entries)} entries; approx {sum(p.stat().st_size for p in entries if p.is_file())/2**20:.1f} MiB, plus {len(logfiles)} batch logs')
    if not args.apply:
        print('DRY RUN: no files were changed. Add --apply to archive, or --mode delete --confirm DELETE_OLD_STAGE9_CHECKPOINTS --apply to delete.')
        return
    locks = acquire(root)
    try:
        if args.mode == 'archive':
            stamp = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
            dest = HERE / ('retired_stage9_checkpoints_' + stamp)
            if dest.exists():
                raise RuntimeError(f'Archive destination exists: {dest}')
            root.rename(dest)
            root.mkdir()
            for logfile in logfiles:
                logfile.rename(dest / logfile.name)
            print(f'Moved original checkpoints and batch logs to {dest}; new ./checkpoints is empty.')
        else:
            if args.confirm != 'DELETE_OLD_STAGE9_CHECKPOINTS':
                raise RuntimeError('Deletion refused; require exact --confirm DELETE_OLD_STAGE9_CHECKPOINTS')
            for entry in entries:
                if entry.is_symlink() or not entry.is_file():
                    raise RuntimeError(f'Unsafe entry; deletion refused: {entry}')
            for entry in entries:
                entry.unlink()
            for logfile in logfiles:
                logfile.unlink()
            print('Deleted only recognized Stage 9 checkpoint files and batch logs. Source code and previous ZIP archives untouched.')
    finally:
        release(locks)


def make_parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    a = sub.add_parser('reset', help='Preview or safely archive/delete previous checkpoint files')
    a.add_argument('--checkpoint-root', default='checkpoints')
    a.add_argument('--mode', choices=('archive','delete'), default='archive')
    a.add_argument('--apply', action='store_true')
    a.add_argument('--confirm', default='')
    a.set_defaults(action=cmd_reset)
    b = sub.add_parser('status', help='Report current checkpoint sweeps (no physical fits)')
    b.add_argument('--checkpoint-root', default='checkpoints')
    b.add_argument('--kinds', nargs='+', choices=KINDS, default=list(KINDS))
    b.add_argument('--seeds', nargs='+', type=int, choices=SEEDS, default=list(SEEDS))
    b.add_argument('--verify-hash', action='store_true')
    b.set_defaults(action=lambda x: show_status(root_of(x), select(x), verify=x.verify_hash))
    c = sub.add_parser('run', help='Run independent chain batches, optionally 2 in parallel')
    c.add_argument('--checkpoint-root', default='checkpoints')
    c.add_argument('--workers', type=int, choices=(1,2), default=1)
    c.add_argument('--chunk', type=int, default=250)
    c.add_argument('--passes', type=int, default=1, help='0 means run until time limit / target')
    c.add_argument('--max-hours', type=float, default=0)
    c.add_argument('--target', type=int, default=10000)
    c.add_argument('--verify-hash', action='store_true')
    c.add_argument('--kinds', nargs='+', choices=KINDS, default=list(KINDS))
    c.add_argument('--seeds', nargs='+', type=int, choices=SEEDS, default=list(SEEDS))
    c.set_defaults(action=cmd_run)
    return p


def main(argv=None):
    args = make_parser().parse_args(argv)
    try:
        args.action(args)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr, flush=True)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
