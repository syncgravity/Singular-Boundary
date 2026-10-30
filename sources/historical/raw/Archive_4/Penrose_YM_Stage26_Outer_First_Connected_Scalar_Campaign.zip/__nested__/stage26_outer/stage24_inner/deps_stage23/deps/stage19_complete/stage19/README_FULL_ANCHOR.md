# Stage 19 — full-anchor target-first *screen*, not admitted scalar spectroscopy

## Reproducible method

`full_anchor_targets.py` builds physical targets fixed before observing gauge fields. It traverses each face anchor (default `--roots 0`, all), generates connected-face loop proposals at sizes 3, 5, 8, and 10 with two deterministic growth variants, and chooses **at most two distinct-target loops per root** satisfying standardized descriptor distance <=1.5 in `(log(area), log(perimeter), 4π area/perimeter²)`. A root with no eligible loop remains unmatched; no replacement is invented. Geometry-specific face counts are permitted. The restricted matched operator is **not** identified with the original spatially averaged scalar. The separate full-volume controls still use exactly one deterministic 3-, 5-, 8-face cluster for every face anchor.

## Actual benchmark and diagnosis

- Square, all 22,801 roots: 154,670 candidates, 45,602 selected, 100% root coverage, every root contributed two selected loops.
- Penrose, all 22,808 roots: 148,706 candidates, 35,928 selected; 3,254 unmatched roots, **85.7331%** root coverage; 16,374 roots with two selected loops.
- The two geometries' selected target-bin occupancies are **not matched** merely because every root searches the same target list. The square catalogue is dominated by different target bins than Penrose. This is a decisive failure of the final symmetric-operator admission gate.
- Approximate directional diagnostic uses the second angular harmonic of the polygon *edge-length* distribution; it is not a point-group orbit completion test. For the square, many paths have undefined second-harmonic direction. Explicit rotation/reflection averaging **has not been established**.
- Gauge measurement on a **512-anchor subset** returned finite values for the target-restricted channel; full-volume deterministic control channels on each geometry pass coverage checks. First-call square restricted measurement included Numba compilation (3.28 s); compilation-warm Penrose restricted measurement on 813 paths took 0.026 s in this environment. The full unrestricted control measurement including catalogue construction took about 4.4 s square / 3.9 s Penrose. These are not Apple M1 benchmarks and *not* full-anchor restricted measurement timings.

## Run

```bash
cd stage19_target_first
OPENBLAS_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 -m unittest -q test_full_anchor_targets test_target_first
OPENBLAS_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 full_anchor_targets.py --roots 512 --measure --inputs /path/to/stage9/checkpoints --output pilot_measure
OPENBLAS_NUM_THREADS=1 NUMBA_NUM_THREADS=1 python3 full_anchor_targets.py --roots 0 --output full_geometry_screen
```

The full-anchor catalogue can take several minutes on an ordinary machine and peaks considerably higher in memory than the 512-root pilot. The *geometry screen* requires no checkpoint fields; `--measure` is optional. Source Stage 9 files are never modified.

**Next gate before production:** improve target support (face sizes/shape variants/tolerances) and explicitly build/verify angular orbit symmetrization while maintaining root coverage; report target-bin occupancy and matched-support losses. It would be scientifically unjustified to claim this is a full zero-momentum projected, symmetry-matched 0++ operator or to start a 24-hour production run on the basis of this screen.
