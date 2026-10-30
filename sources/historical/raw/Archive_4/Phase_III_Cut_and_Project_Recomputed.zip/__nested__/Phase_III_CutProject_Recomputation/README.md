# Phase III: validated 2D \(\mathbb Z^5\) cut-and-project recomputation

All numerical files are included; Python >= 3.10, `numpy`, `scipy`, and `arviz` are required. `matplotlib` is optional for the illustrative graph plot. Run with single-threaded BLAS for comparable solver behavior.

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
cd Phase_III_CutProject_Recomputation
python -m unittest -v test_direct      # six tests (no expensive chain runs)
python build_manifest.py               # 20 checked geometry fingerprints
python independent_beta0.py            # 160 independent Haar-link samples
python geometry_admission.py           # 96 geometric comparisons
python analyze.py                      # existing dense-certified checkpoint results
```

`diagnostics.json` is calculated from **`chains_dense/`**, which contains the replayed, dense-certified spectra. `chains/` contains the **original sparse-solver** chain snapshots retained as provenance; its `lambda2` and `gap` values must **not** be used. The audit identified missed Kramers partners. Every trajectory was replayed from its saved seed and independently checked for exact final RNG/link equality. Read `REPORT.md` for counts and validation details.

## New independently checkpointed interacting run

```bash
python run_segments.py
python analyze.py --chains-dir chains_certified --output diagnostics_fresh.json
```

`run_segments.py` uses the **corrected dense eigensolver**, four independent chains at each of two sizes and two couplings, and 150-sweep checkpoint segments written atomically to the *new* `chains_certified/` directory, never overwriting the archived original data. The 16 trajectories take multiple minutes overall; split them among sessions and rerun the command to resume. A restart guard checks the graph SHA-256 and all parameters.

If auditing the originally executed trajectory by deterministic replay:

```bash
python replay_dense.py --glob 'R5.0_o0_b1.0_*.json'
# Or revalidate every original archive chain:
python replay_dense.py
```

The replay recomputes dense eigenvalues and checks the *exact* final RNG state and gauge matrices against the original checkpoint. It writes `chains_dense/`. The per-chain `certification` object records how many sparse-solver eigenvalues were corrected.

The explicit cut-and-project graph construction is self-contained in `direct_cut_project.py`. `phase2.py` and `legacy_phase2.py` retain the original **unverified** pentagrid generator solely for inherited gauge routines and the independent face-set cross-check. **Do not call `phase2.penrose()` to generate corrected Penrose research data.** `audited_penrose.py` supplies the separate corrected pentagrid verifier. The candidate periodic `provisional_periodic.py` is **not** a certified Penrose substitution approximant.

Other useful artifacts: `beta0_independent.json`, `admission_results.json`, `geometry_manifest.json`, `verified_penrose_patches.png`, `tests.log`, `run_segments.log`, and `analysis.log`.
