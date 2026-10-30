# Stage 25 — full-lattice inner equilibration test

This package reuses the **unchanged Stage 24 simulation runner** and its full geometry/catalogue dependencies. Stage 25 adds a separate diagnostic analysis; no new gauge kernel or change to the SU(2) target distribution is introduced.

## Install and test

```bash
cd /Users/sharpe/Projects/Business/QCYangMills
unzip ~/Downloads/Penrose_YM_Stage25_Inner_Equilibration_Test.zip
cd stage25_equilibration
python3 -m unittest -q test_stage25
(cd stage24_inner && python3 -m unittest -q test_stage24)
```

## Controlled full-lattice runs

These commands **replay one independently advanced outer field from each original seed-101 Stage 9 checkpoint**. They do not write to the checkpoint and do not resume Stage 24 output. This is intentional: changing only inner burn and depth while holding the outer field fixed produces a comparable inner convergence experiment. Preserve the source checkpoint files.

Square:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage24_inner/stage24_inner_diagnostics.py \
 --kind square --seed 101 \
 --checkpoint ../ym_stage9/checkpoints/square_nt20_seed101.npz \
 --cache stage24_inner/deps_stage23/deps/stage19_complete \
 --output results --outer 1 --stride 10 \
 --burns 48 96 --depths 12 32 --reps 4 --thin 3 --offsets 0
```

Penrose:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 \
caffeinate -is python3 stage24_inner/stage24_inner_diagnostics.py \
 --kind penrose --seed 101 \
 --checkpoint ../ym_stage9/checkpoints/penrose_nt20_seed101.npz \
 --cache stage24_inner/deps_stage23/deps/stage19_complete \
 --output results --outer 1 --stride 10 \
 --burns 48 96 --depths 12 32 --reps 4 --thin 3 --offsets 0
```

Expected two NPZs with Stage 24 schema, both from source sweep 10000 outer1. Each has 8 independent inner *replica trajectories* per geometry (4 replicas × 2 burn lengths). Within each trajectory K=12 and K=32 are nested estimates, **not** two independent streams. The inner work for each replica is `burn+32*3` full-lattice restricted sweeps; approximately 144 and 192 per replica at burns 48 and 96. This is a materially larger run than Stage 24 (~2–4 times as long per geometry; actual time varies).

Analyze:

```bash
python3 analyze_stage25.py results/square_seed101_stage24_from10000_outer1.npz \
 results/penrose_seed101_stage24_from10000_outer1.npz \
 --out STAGE25_INNER_AUDIT.json
```

Upload **both NPZ files**, their JSON manifests, and optionally the audit JSON. Do not upload gauge-field restart files.

## Interpretation and acceptance

- Compare long-vs-short burn mean shifts to the disagreement among independent inner replicas, separately for time lag and operator, with special attention to the *connected-scale* fluctuations.
- Check that larger K reduces independent-replica noise; with only four streams, uncertainty on this noise estimate is substantial.
- If large shifts persist at burn 96, expand the burn grid rather than promote an unconverged conditional estimator.
- Even if inner convergence appears satisfactory, a **multi-seed outer ensemble** is mandatory to validate connected-vacuum subtraction, autocorrelation, direct/conditional expectation agreement, and cost-adjusted statistical efficiency.
- Do not identify inner replicas as independent outer configurations; no physical scalar mass fit from this test.

**Known limitation:** Stage 24's stream identifier includes the `burn` setting, so short- and long-burn configurations are not paired on identical random draws. That is appropriate for independent-replica comparison, but prevents a common-random-numbers burn-in test. A later test should check actual inner Markov-chain autocorrelation and mixing; four independent replicas do not prove equilibration.
