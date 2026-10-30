# Stage 4 reproducibility guide

## Contents
- `stage4_smearing_flux.py`: gauge-covariant APE, scalar loop shapes, integer winding/center validation, flux observables.
- `stage4_remeasure.py`: deterministic measurement of each preserved Stage 3 configuration, independent of Monte Carlo resampling.
- `test_stage4.py`: 10 new regression, gauge-covariance and topology tests.
- Other `*.py` modules: copied unchanged from the Stage 3 research package to satisfy imports.
- `outputs/`: 400 configurations remeasured (raw gauge link arrays are not duplicated); per-configuration observables, connected correlators, physical bins and bootstrap summaries.
- `STAGE_4_REPORT.md`: methods, numerical findings, limitations and admission decision.

## Reproduction

Unpack the separately supplied `Penrose_YM_Stage3_Toroidal_Spectroscopy_Gate.zip` so its `ym_stage3/outputs/` directory is available. Use Python 3.10+ with numpy, scipy and numba (and arviz to rerun the predecessor tests).

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
python -m unittest -q test_stage4
python stage4_remeasure.py --stage3 /path/to/ym_stage3/outputs \
    --out outputs --per-chain 50 --block 5 --bootstrap 160
```

Stage 3 data remain 8-time-slice, statistically non-admitted exploratory chains. These files **do not** demonstrate a glueball mass or string tension. `rational_M5` is a periodic model-set *software control*, not a locally admitted Penrose approximant.
