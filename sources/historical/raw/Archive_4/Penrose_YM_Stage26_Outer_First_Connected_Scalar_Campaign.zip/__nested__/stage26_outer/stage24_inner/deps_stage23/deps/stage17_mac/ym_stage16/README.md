# Stage 16 — Exact SU(2) multihit and large matched Wilson path batch

Extract the archive so `ym_stage16/` and `ym_stage13/` are **sibling directories**. Run from `ym_stage16` in Python with NumPy, SciPy, and Numba installed.

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
python -m unittest -q test_stage16 test_stage16_matched
python stage16_convention_audit.py
python stage16_heatbath_mixing.py
python stage16_benchmark.py
python stage16_screen_ci.py
python stage16_matched_paths.py
```

`stage16_large_snapshot.py` additionally requires the **eight** final Stage 9 checkpoint files named `square_nt20_seed{101,211,307,419}.npz` and `penrose_nt20_seed{101,211,307,419}.npz`. They are omitted from this archive due to size. On a Mac with the earlier Stage 9 folder as a sibling, run:

```bash
python stage16_large_snapshot.py --checkpoints ../ym_stage9/checkpoints
```

Without `--checkpoints`, it searches one directory above `ym_stage16/`.

This uses the last saved links of each Stage 9 chain, **not** the 900 earlier observations recorded in their measurement arrays. It is a small smoke test, not physical production analysis.

Important: `stage13_transport.mat()` has an orientation bug relative to the original `wilson_torus.mul` product. Do **not** use the earlier Stage 13–15 transporter noise-reduction ratios as validated Wilson-observable results. Stage 16 uses the correct action quaternion multiplication and has independent gauge invariance and original Stage 9 Wilson-kernel regression tests. Do not treat Stage 16 small-square results as a string-tension determination.

See `STAGE_16_REPORT.md` for methods, sample counts, bias/variance restrictions and next actions.
