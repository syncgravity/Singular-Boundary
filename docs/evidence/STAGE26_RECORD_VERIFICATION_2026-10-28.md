# Stage 26 original saved outer-field record audit

**2026-10-28, read-only.** Reviewed eight `{penrose,square}_seed{101,211,307,419}_stage26.zip` archives and their `outer_*.npz` names, first/last record headers, and `latest.json`. No MCMC, mass fit or new observables calculated.

| Geometry | Seeds | Saved outer records | Sweep sequence |
|---|---|---:|---|
| Penrose M55 | 101, 211, 307, 419 | 4 x 100 = 400 | 10020, 10040, ..., 12000 |
| Square matched | 101, 211, 307, 419 | 4 x 100 = 400 | 10020, 10040, ..., 12000 |
| **Total** | **8 chains** | **800** | **Stride 20** |

Every archive's `latest.json` reports final sweep 12000 and 100 observations. Records include `direct_timeslice: [20,4]`, `conditional: [2,9,4,4]`, `pair_counts: [9]`, individual initial `source_sha256` and a shared per-geometry `catalogue_sha256`.

Catalogue SHA-256s exactly match the independently supplied original NPZ files:

- Penrose: `d08e157f1b6fe258f4214e834f80508ef6278cae2f672b378188e8f138c00e2d`
- Square: `c81bff473a8418b141b23d8f6547aceb9f569d4dc9c352f7f2920b0373580ff8`

**Limitations:** 800 outer-field records are not 800 independent spectral-mass measurements. Offset policy and two inner replicas do not increase outer-chain sample count, and no effective sample-size, inner equilibration, covariance-aware plateau or physical continuum inference is established by metadata. The source checkpoint SHA in a saved record has not yet been checked against every preserved actual input checkpoint; do not claim that level of historical provenance without a separate hash match. Do not rerun archived chains.
