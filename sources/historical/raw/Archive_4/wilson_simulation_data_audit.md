# Wilson simulation-data availability audit

Date: 2026-10-11

## Requested analysis

Compute the scalar glueball mass `m_0++` and fundamental string tension `sigma` for each Penrose and reference Wilson ensemble, then examine a continuum extrapolation of `R=m_0++/sqrt(sigma)` and the difference of continuum limits.

## Files checked

- `/mnt/data/Sharpe_dissertation_v10.7.tar.gz`: 8 PDFs (one dissertation, five papers, and two experiments) and macOS metadata. No gauge configurations, gauge action implementation, gauge geometry definitions for the referenced interacting-Wilson runs, scalar correlator tables, or Wilson-loop measurement tables.
- `/mnt/data/Formal Investigation Candidates Elaboration.md`: research notes on hopping-graph spectra and related questions; no Yang–Mills ensemble measurements.
- `/mnt/data/penrose_ym_measurement_protocol.md`: measurement protocol; explicitly identifies simulation-data absence.
- `/mnt/data/penrose_ym_continuum_fit.py`: post-processing script for joint bootstrap estimates; cannot extract masses or string tension from raw correlators or generate configurations.
- `/mnt/data/penrose_ym_bootstrap_template.csv`: contains only CSV header, no ensemble measurement rows.
- Accessible Project files and Library document search: no matching raw Wilson Monte Carlo data from the earlier named conversation.

## Trial execution

Command:

`python penrose_ym_continuum_fit.py penrose_ym_bootstrap_template.csv`

Outcome: exited nonzero with `ValueError: No measurements found: supply joint bootstrap samples`.

## Empirical outputs

| Observable | Status |
|---|---|
| `m_0++` per coupling and geometry | Not estimable: no gauge-invariant scalar correlators or configurations |
| `sigma` per coupling and geometry | Not estimable: no measured Wilson loops, static potentials, winding strings, or configurations |
| `R(a)` | Not estimable |
| Continuum `R(0)` for either geometry | Not estimable |
| `Delta R(0)` | Not estimable |
| Continuum extrapolation support | Cannot assess without multiple matched cutoff-scale ensembles |

## Data to supply

1. Raw equilibrated gauge configurations **or** fitted/correlated scalar two-point functions and physical-geometry-calibrated Wilson loops/static potentials for **each** coupling and volume.
2. SU(N) group, explicit gauge action including plaquette weights and normalization, local lattice geometry (embedded vertices, oriented edges, faces, temporal links), boundary conditions, and coupling values.
3. Observable sampling identifiers/autocorrelation blocking, spatial and temporal scale convention, and enough distinct lattice spacings and physical volumes to evaluate extrapolation and finite-volume stability.
4. Ideally, paired mass and string-tension bootstrap replicates (columns in the supplied template), if extraction has already been performed.

No synthetic or reference values have been substituted for absent observations.
