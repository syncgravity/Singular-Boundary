# Stage 15 — reproducible batched transporter benchmark

Archive contains `ym_stage15` code/tests/full numerical data and `ym_stage13` source/dependencies, including the inherited gauge sampler. This is a small-lattice exploratory benchmark, **not production spectroscopy**.

From archive root:

```bash
cd ym_stage15
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest -q test_stage15
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python stage15_batch.py
```

The `BENCHMARK.json` file records all paired observations and execution times. See `STAGE_15_REPORT.md` for the fail-closed scientific interpretation.
