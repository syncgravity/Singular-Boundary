# The Singular Boundary — read-only historical verification

**Evidence snapshot:** October 28, 2026. Python >=3.10, NumPy. All original science archives remain unchanged.

## Run

```bash
python -m pip install numpy
python verify.py --root /path/to/unmodified/historical-files --output /path/to/separate/verification.json
```

`--root` is the directory containing the 42 unmodified historical ZIP archives named in `MANIFEST_LOCK.csv` (including the eight `*_stage26.zip` archives). If the source archives live in different directories, first arrange read-only links in a separate folder; do not rewrite their contents. This suite may be run without `--output`, writing no files.

The expected archive checksums and lengths were captured from uploaded originals. `verify.py` checks SHA-256 and ZIP CRC before interpreting data; it refuses to overwrite a pinned archive or its lock file. It reads archived JSON and NumPy `.npz` data with `allow_pickle=False`. **It never executes archived Python source, Monte Carlo updates, bootstrap resampling, fits, or spectral extrapolations.** Output is written only when explicitly requested to a non-source file.

## Checks and scientific limits

The 100 reported checks comprise 42 archive hashes, 42 ZIP CRC/path checks and 16 structural/saved-result checks: Stage19 strict anchor existence (22,055 → 22,658 → 22,808); 64/64 failed held-out variational signal screens; Stage20 lag-constant vacuum-subtraction correction; Stage29 stored matched diagnostics; the Stage33 transpose patch; Stage34 single-field, 22,808-anchor × 20-slice × 4-channel production averaging; absence of completed measured Stage35 ensemble arrays in the supplied ZIP; eight saved Stage26 chain inventories and last-record SHA-256 checks; total 800 Stage26 outer observations.

**The Stage19 pilot/coverage results do not certify a final assembled production catalogue. The Stage34 numerical identity is one-field measurement equivalence, not an ensemble or spectrum. The 64 held-out combinations share eight gauge chains and are not 64 independent experiments. The Stage26 800 records are eight chains, and two inner replicas or shifts are not independent outer observations.** These checks do not prove the interacting continuum infrared bound or a mass gap.

## Files

- `verify.py` — portable read-only verification program.
- `MANIFEST_LOCK.csv` — original archive filenames, byte sizes and SHA-256 identities (42).
- `VERIFICATION_RESULTS.json` — machine-readable run evidence from the mounted historical archives.
- `NEGATIVE_TEST.json` — verifier rejects an intentionally incorrect lock hash, without changing source files.
- `VERIFY_REPORT.md` — human scientific reconciliation and limitations.

The lock is a provenance snapshot, not a cryptographic signature of the original authors. Keep the historical archive bytes immutable. Any later source addition should receive a new reviewed lock/version, not silently replace this one.
