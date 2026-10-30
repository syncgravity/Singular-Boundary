# Stage 13 reproducibility

Run using Python, NumPy, SciPy and Numba:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest -v test_stage13
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python pilot.py
```

This package includes exactly the Stage 6 original temporal-slab implementation and the Stage 5/7 geometry/action dependencies in `deps/`. Stage 13's `stage13_transport.py` does not change the Wilson update equations. `pilot.py` creates `PILOT.json` from a tiny short-run one-chain experiment; results have no physical fit status. See STAGE_13_REPORT.md. Test stage7/model-set uses M5 for algebra only, not a geometrically admitted Penrose approximant.
