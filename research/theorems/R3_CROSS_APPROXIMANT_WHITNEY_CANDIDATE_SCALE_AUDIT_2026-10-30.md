# R3-IR-558: Cross-approximant construction and scale audit

Archived Penrose generator was run independently at M=5,7,9,11,13,15, building the radius-two face-neighborhood of face 0. A conforming affine quadrilateral Whitney 1-form **candidate** mass was assembled with 3x3 Gauss quadrature. All six matrices are SPD, and a rooted spanning tree was constructed for each such that face 0 has precisely one chord, shared with exactly one retained adjacent face.

|M|Full faces|Patch faces|Patch edges|Chord M_ee|Condition number|Mean projected edge length|
|---:|---:|---:|---:|---:|---:|---:|
|5|188|14|37|0.70568333|13.13471|0.63058810|
|7|420|14|36|0.72362159|11.02668|0.63211784|
|9|600|14|37|0.84671219|10.83315|0.63203366|
|11|912|14|36|0.71263554|10.87766|0.63220337|
|13|1360|14|36|0.68613440|10.52713|0.63232315|
|15|1672|14|36|0.87277873|10.92117|0.63229462|

**Critical distinction:** increasing periodic approximant parameter M does not refine local cell lengths: mean length remains approximately 0.632. An explicitly chosen formal rescaling h=1/M makes coordinate edge lengths shrink, but in 2D a conforming Whitney 1-form mass is invariant under uniform rescaling J->hJ, because area h^2 cancels the two inverse Jacobians. This formal construction is not a derived physical continuum or coupling law. The illustrative rho=8|b|M_ee/(3g2^2), at b=3/32000 and g2^2=1, ranges from 0.0001715 to 0.0002182, which is NOT a physically calibrated Yang-Mills result.

The candidate mass prescription is DISTINCT from the authoritative historical 11-face M5 matrix. Do not silently substitute it. The patch geometry and target edge identifiers also differ across approximants; the matrices are not a nested physical mesh hierarchy. No continuum mass gap is proved.

**Durable source and data:** ChatGPT Library `/The Singular Boundary/Source/` contains `build_penrose_cross_approximant.py`, `penrose_refinement_scaling_audit.py`, `penrose_cross_approximant_candidate_matrices.npz` (SHA-256 `64f9f4c4abddb1ad7084da50c16748e43733ec69d4ca6966b79ff369926c307a`) and `penrose_cross_approximant_candidate_results.json` (SHA-256 `6b44a98225c9101b0bc208324a7eeea6a7074ba1fe5a7f29c59ce5b296d4d21a`). No NPZ pushed to Git.

**Next obligations:** historical assembly identification, a calibrated actual physical spatial refinement and corresponding gauge coupling, uniform protected-chord topology in the intended model, and continuum spectral properties. None is proved by these tests.