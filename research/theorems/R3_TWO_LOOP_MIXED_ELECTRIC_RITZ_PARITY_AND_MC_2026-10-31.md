# R3-IR-566 — Four-state mixed inverse-Whitney electric Ritz: exact parity diagonality and sampled diagonals

Date: 2026-10-31. This is a **finite four-state Gauss-invariant Galerkin** evaluation on six alternative Penrose-prism candidate complexes, not the full finite spectrum or a continuum gap.

## Exact algebra: diagonality does not discard mixed electric terms

The Haar-orthonormal trial basis is 1, χ_A, χ_B, χ_Aχ_B, where the retained adjacent horizontal loop A and vertical loop B each have at least one edge not belonging to the other. Let J_e be the SU2 central flip U_e→−U_e on a uniquely belonging edge. Every rooted transport in the electric quadratic form transforms at most by its central sign; the adjoint transport is unchanged. Left/right SU2 infinitesimal derivatives commute with J_e. Thus the invariant quadratic form commutes with each such flip, and distinct trial functions with different pairs of parity signatures have zero electric form matrix elements. In the ordered basis, **E^(4)=diag(0,E_A,E_B,E_AB) exactly** even with nonzero mixed inverse-Whitney entries and nontrivial rooted adjoint transports. Off-diagonal finite-sample Monte Carlo estimates should therefore be discarded as stochastic noise, not interpreted as physical couplings.

## Explicit estimator and computation

The executed `compute_two_loop_electric_ritz.py` constructs root-source paths from archived graph trees, samples independently Haar-distributed quaternion holonomies, evaluates SU2 loop characters and their analytic left-invariant three-axis derivatives using quaternion product insertion, rotates derivative vectors into the root frame with the exact adjoint quaternion rotation, and contracts all link/link entries with K=M1^-1. It adds the exact magnetic 4x4 matrix from R3-IR-565. Sampling: deterministic seeded 128 independent configurations per M. Matrix results were checked against the rigorous global K eigenvalue envelopes R3-IR-565. A separate previous M5 2048-sample run confirmed rough consistency.

|M|E_A (MC)|E_B (MC)|E_AB (MC)|Ritz gap (plug-in estimate)|
|---:|---:|---:|---:|---:|
|5|57.369 ±1.490|78.109 ±2.204|122.999 ±7.103|62.681|
|7|73.474 ±2.404|115.712 ±3.457|193.757 ±10.871|83.933|
|9|100.514 ±2.720|124.155 ±3.330|212.526 ±11.293|113.441|
|11|117.579 ±3.924|169.743 ±5.806|327.799 ±17.370|126.565|
|13|150.273 ±3.976|205.062 ±6.106|338.605 ±18.796|166.311|
|15|150.557 ±4.686|209.876 ±5.709|379.383 ±19.421|191.587|

The displayed ± are estimated one-standard-error Monte Carlo uncertainties for individual diagonal electric entries, NOT certified deterministic error bounds or eigenvalue intervals. The gaps above are obtained by diagonalizing the magnetic matrix plus the sampled diagonal electric entries, not by diagonalizing a projected full 95–98-link Hamiltonian. At M5, an earlier independent 2048-draw result gave (E_A,E_B,E_AB) ≈(54.790,76.059,129.375). Because 128 samples is low and the offdiag sample fluctuations can be substantial, **these are exploratory calculations only**.

In particular, a large *Ritz gap* is not a lower bound on the full gauge-invariant spectral gap. The next step is deterministic SU2 representation contraction or high-accuracy certified quadrature of all three diagonal electric coefficients, then expansion of the Galerkin space to include more independent plaquette loops and vertex intertwiners, with carefully controlled truncation.

**Data:** executed script and JSON persisted in ChatGPT Library /The Singular Boundary/Source/. Underlying candidate NPZ binary archives stay in Library. No continuum mass gap established.
