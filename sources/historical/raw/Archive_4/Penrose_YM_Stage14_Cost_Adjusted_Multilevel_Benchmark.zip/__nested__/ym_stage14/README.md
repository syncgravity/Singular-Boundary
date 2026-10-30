# Stage 14 benchmark

Read STAGE_14_REPORT.md before interpreting the numerical values. This is a 5×5 square-lattice feasibility benchmark, not an M55 Penrose experiment.

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python stage14_benchmark.py` from `ym_stage14`, with the sibling `ym_stage13` directory present. Three tests: `python -m unittest -q test_stage14`.

The benchmark uses four seeds, 12 outer backgrounds per seed, and conditional depths 8 and 32. Any longer-depth attempt was incomplete and is not included. All outputs are exploratory; no string tension or mass is calculated.
