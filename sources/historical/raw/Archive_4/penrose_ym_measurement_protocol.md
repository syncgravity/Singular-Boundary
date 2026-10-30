# Penrose vs Wilson 3D Yang–Mills: continuum ratio protocol

**Status: analysis pipeline prepared; no Yang–Mills simulation data are included here.**

## Test quantity

For two **theories with matched gauge group and target continuum action**,
compare the lowest scalar glueball mass in the same fundamental-string-tension units:

- `R_geom = m_0++ / sqrt(sigma)`, and `Delta_R0=lim_{a->0}(R_penrose - R_wilson)`.
- `a_s` is a defined spatial cutoff, `a_t` the temporal lattice spacing, `xi=a_t/a_s`.
- Given `am_t=a_t*m` and `asqrt_sigma=a_s*sqrt(sigma)`, compute `R=am_t/(xi*asqrt_sigma)`.
- Use `x=(a_s sqrt(sigma))^2` for the conventional leading-cutoff fit, and check `x=(a_s sqrt(sigma))` and dropping coarse ensembles for sensitivity, because the irregular Penrose regulator may have different corrections.

## Measurements required for each geometry / coupling / size

1. Fix explicit SU(N), gauge action, plaquette weights, boundary conditions, and definition of `a_s` in the physical embedding. Verify the naive continuum quadratic form is the *same isotropic Yang–Mills action*; otherwise a different continuum ratio may simply mean a different continuum theory.
2. Collect equilibrated gauge configurations with autocorrelation analysis. Store/block-resample observables for correlator and Wilson-loop extractions *on the same gauge configurations* to retain covariance.
3. Construct a basis of scalar-even gauge-invariant closed spatial loops. Symmetry-project/average using actual spatial geometry and verify that angular-momentum interpretation tends to `0++` (not a fixed-regulator symmetry mixture). Extract `a_t*m` via variational generalized eigenvalue / multi-exponential correlator fits with plateau and excited-state checks.
4. Extract the fundamental string tension from physical-size Wilson loops or the large-distance static potential (`V(r) ~= sigma*r + const + finite-r string correction`) in multiple spatial directions and patch locations. If a noncontractible winding loop is used instead, state the periodic *approximant* topology and apply its appropriate flux-tube energy correction. Do not measure area by bond count in an irregular mesh.
5. Check that `sigma` is positive, stable under fit-window changes, and independent of direction and location in the proposed continuum limit. Verify both geometry implementations use the same area and time normalizations.
6. Check volume dependence at fixed `a_s sqrt(sigma)`, with sufficiently large `L sqrt(sigma)` and time extent. For Penrose, check inflation/approximant size and offsets/phasons as separate systematic errors. Verify that the scalar correlator is not contaminated by small-volume winding strings/torelon pairs.
7. Run regular Wilson reference and Penrose model at >=4 spacings each (at least 3 required by the fitting script). Tune to overlapping `a_s sqrt(sigma)` scales, with multiple physical volumes for independent checks. A published reference is an additional calibration, not a substitute for an internally matched regular-lattice simulation.
8. Isolate the previously identified confound using a **gauge-invariant** control with the matched plaquette-weight/coupling distribution but rearranged spatial correlations, verifying that the control has the same target continuum action. Compare its own continuum `R0` as well. Merely matching the global mean beta or average plaquette is insufficient.
9. Use paired mass/tension bootstrap replicates per ensemble. Fit `R=R0+c*x`; bootstrap x and y jointly. Test p=2 vs p=1 cutoff corrections and deletion of the coarsest spacing. `Delta_R0` counts as a candidate nonzero effect only if its uncertainty excludes 0 **and** the continuum interpretation survives volume, normalization, action-matching, and control tests.

## Input format for `penrose_ym_continuum_fit.py`

One CSV row per **joint-bootstrap replicate**, per ensemble:

`geometry,ensemble,replica,am_t,asqrt_sigma,xi`

- `geometry`: `penrose`, `wilson` (or another label via command flags).
- `ensemble`: unique identifying `beta`, geometry, volume, etc.; use only vetted large-volume ensembles for one continuum-fit series.
- `replica`: matched integer bootstrap index present in **every** included ensemble. Within one ensemble, `am_t` and `asqrt_sigma` must derive from the **same resampled underlying Monte Carlo blocks**. Different ensembles may have independent resampling at each index.
- `am_t`: fitted scalar mass in temporal lattice units (positive).
- `asqrt_sigma`: fitted square root of *fundamental* string tension in spatial physical-cutoff units (positive).
- `xi`: temporal-to-spatial spacing ratio `a_t/a_s` (1 if isotropic). For renormalized anisotropic discretizations use its calibrated physical value and propagate its uncertainty upstream; the script treats `xi` in each row as supplied.
- At least 50 bootstrap indices across all ensembles, 1000+ recommended.

Run:

```bash
python penrose_ym_continuum_fit.py measurements.csv --power 2 --output-prefix result_p2
python penrose_ym_continuum_fit.py measurements.csv --power 1 --output-prefix result_p1
python penrose_ym_continuum_fit.py measurements.csv --power 2 --exclude-coarsest 1 --output-prefix result_p2_fine
```

The script outputs JSON containing each continuum intercept, bootstrap statistical uncertainty, fit chi-square/DOF and the paired continuum difference and its percentile interval. It cannot judge finite-volume, mass-extraction, continuum-operator, or control-model systematics.

**External benchmark (only if SU(2), D=2+1 pure Yang–Mills):** Athenodorou and Teper, *JHEP* 02 (2017) 015, Table B3: `m_0++/sqrt(sigma)=4.7367(55)`; SU(3) `4.3683(73)`. https://doi.org/10.1007/JHEP02(2017)015
