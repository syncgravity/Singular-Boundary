# Stage 19 — Complete strict auxiliary (version 2) and capped continuation

This revision integrates **all 150** recovered Penrose rooted loops into the frozen strict auxiliary catalogue. It preserves all 22,658 previous accepted paths and the three original complete 3-, 5-, and 8-face controls. Matching threshold **1.5 is unchanged**. Square includes 22,801/22,801 spatial face anchors and Penrose includes 22,808/22,808. The resulting auxiliary is a full-face-root observable, **not** a rigorously D5-symmetrized operator on the periodic Penrose approximant. Full coverage does not establish either ground-state overlap or a glueball mass.

A versioned, precomputed `stage19_complete_catalogues/` contains the square and completed Penrose path catalogues. DO NOT replace any cache or restart files from the previous `stage19_mc_pilot/`. Catalogue hashes are part of new restart states and observation segments. The `complete_catalogue.py` script and `missing_anchor_diagnostics.npz` permit reconstructing the completed Penrose catalogue from the original strict catalogue.

## 1. Install and test

Unzip at the root of your existing `QCYangMills` directory (this creates `stage19_complete/`). In your existing `(QC)` environment:

```bash
cd /Users/sharpe/Projects/Business/QCYangMills
unzip ~/Downloads/Penrose_YM_Stage19_Complete_Strict_Auxiliary.zip
cd stage19_complete
python3 -m unittest -q test_stage19_mc
```

You need the eight original Stage 9 checkpoints at `../ym_stage9/checkpoints/`. Keep the existing `../stage19_mc_pilot/stage19_pilot_results/` restart states; **do not copy or overwrite them**.

## 2. Continue from the existing 10,100-sweep Stage 19 pilot

If the prior pilot was saved at `../stage19_mc_pilot/stage19_pilot_results`, use:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage19_manager.py \
  --inputs ../ym_stage9/checkpoints \
  --prior-stage19 ../stage19_mc_pilot/stage19_pilot_results \
  --output stage19_complete_results \
  --cache stage19_complete_catalogues \
  --target-sweeps 10600 --chunk 20 --thin 10
```

This forks the **existing Markov chain state and RNG** at 10,100 into a new independent output directory, then advances a **fixed 500 additional sweeps** to 10,600. Four full-volume controls plus the new 100%-coverage auxiliary are measured every 10 sweeps (50 per chain). The previous 10,100-sweep auxiliary is the old *masked* operator and is NOT combined as if it were the new complete operator. The three controls are the same definitions, and the Monte Carlo trajectory is a continuation, not an independent chain.

The manager runs serially on an 8-GB M1. `--target-sweeps 10600` is an absolute fixed cap; there is no implicit 24-hour time limit. Change `--target-sweeps` only deliberately, after the next audit.

If your previous result directory is elsewhere, replace the `--prior-stage19` path. Each previous directory must contain `restart.npz` and its observation segments; the new runner verifies its last segment SHA256 and Stage9 origin hash. It also saves `prior_stage19_lineage.json`. The new `stage19_complete_results` must initially be empty.

## 3. Reproducibility / operator definitions

`stage19_complete_catalogues/penrose_complete_catalogue.npz` has 22,808 roots in increasing order. `distance` has maximum 1.48338 (at or below 1.5), including 150 newly integrated loops (new maximum 1.36892). Each root contributes exactly one selected closed Wilson loop. Old accepted paths and all complete control catalogues are copied bit-for-bit. New catalogue file SHA256: `d08e157f1b6fe258f4214e834f80508ef6278cae2f672b378188e8f138c00e2d`.

`scalar` stores `(n_meas,20,4)` with original controls in channels 0–2 and complete strict auxiliary in channel 3. `aux_full_denominator` is identical to channel 3 now that every anchor is covered. Each observation segment includes `catalogue_sha256` and `source_sha256`. New results cannot be silently mixed with the older masked auxiliary because the catalogue SHA256 changes and Stage 19 restart configuration requires exact match.

## 4. Validation performed here

- Strict catalogue construction: 22,808/22,808 Penrose roots, each exactly once, all distance <= 1.5; independent original strict catalogue retained.
- Penrose real Stage9 seed101 one-sweep continuation succeeded (10000 → 10001), 20x4 scalar values finite, both auxiliary normalizations equal, and full-volume controls matched the old pilot **exactly, maximum absolute discrepancy 0** on the identical updated gauge field.
- A separate fork from the old Stage19 test state succeeded (10001 → 10002), with old-segment SHA256 and source-lineage checks.
- Original Stage19 runner unit tests: 2 passed.

**Not established:** exact finite Penrose point-group projection, time-series scalar SNR, a glueball mass or any continuum regulator difference. Upload only `observations_*.npz` and `latest.json` / `prior_stage19_lineage.json` for the next statistical audit; keep large `restart.npz` locally.
