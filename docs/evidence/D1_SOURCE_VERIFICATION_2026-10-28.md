# D1 — Stage 7 → Stage 26 deterministic action-source certificate

**Executed 2026-10-28.** No Monte Carlo or gauge-field evolution was run. Deterministic original Stage 7 geometry construction, source AST comparison, and Stage 7 oriented-face closure tests only.

Source chain verified:
`stage26_outer.py` -> imported `stage22_shifted.setup_geometry` -> `stage7_checkpointed.setup_geometry` -> `stage7_large_torus.pair/assemble_vectorized` -> `stage2_ym_calibration.quadratic_weights`.

`assemble_vectorized` builds `N_t F` spatial quadrilateral plaquettes and `N_t E` temporal 4-link ribbons, with indices `t+1 mod N_t` and signed words `[1,1,-1,-1]`. Spatial couplings `beta_s(f)=beta_ref*a_ref*a_t/A_f`, temporal `beta_t(e)=beta_ref*a_ref/a_t*(sum_{f adjacent to e} A_f/2)/length_e^2` were verified directly in source. Original `setup_geometry` uses `a_t=a_ref=sqrt(Penrose_area/Penrose_F)`. The bare Stage 26 script calls `setup_geometry(kind,20,3.5)`.

| Check | Penrose M55 | Square matched |
|---|---:|---:|
| V | 22808 | 22801 |
| E | 45616 | 45602 |
| F | 22808 | 22801 |
| Nt | 20 | 20 |
| Space-time links L | 1368480 | 1368060 |
| Face words P | 1368480 | 1368060 |
| Positive time-invariant face couplings | yes | yes |
| Exact Stage 7 oriented boundary closure | pass | pass |

The Penrose `SHA256(fi.tobytes()+sg.tobytes())` is
`fee7afad5b4b464537782b508402401502984947ac5caf5163a87dad8ae33e2e`;
this **equals** the saved full Stage 26 simulation incidence export's original `source_array_sha256` exactly. Penrose spatial graph SHA-256:
`f67fc4455b37bf18f16c0a5ae90c7c3c5ccd49ca8b739fa1f5e43562b4581c21`.

All 13 recovered Stage 7 `stage7_checkpointed.py` variants have identical Python AST for `setup_geometry`, `get_plaquettes`, and `sweep`. Six variants add a selectable cold start; they do not change those action-related methods.

**Corrected provenance:** The Oct 26 documents' statement that literal Stage 7 source was unavailable is historically dated and no longer current. The corresponding geometry/action construction and Stage 26 incidence link are verified. Still outstanding: original checkpoint identity for every chain, a full transfer positivity/reconstruction certificate, and temporal/spatial quantum continuum scaling. The Stage 26 export's `partition_certified` flag is unreliable because the exporter replaces absent Q/fixed indices with [] before testing their presence. The full export with empty Q/fixed indices is **not** the R3 twelve-prism boundary partition.
