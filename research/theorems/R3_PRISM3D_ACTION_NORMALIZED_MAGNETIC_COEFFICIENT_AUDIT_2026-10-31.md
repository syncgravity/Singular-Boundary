# R3-IR-562 — Single-action 3D prism SU(2) coefficient construction and failure of small-chord criterion (2026-10-31)

## Defined regulator action and Hamiltonian

This is a **consistent explicitly declared finite-regulator convention**, not the uniquely derived or renormalized physical Yang–Mills theory. The spatial complex comprises one layer of extruded Penrose rhombi, with dimensionless holonomy angle theta_e on oriented edges, the 3D Nédélec/Whitney 1-form mass M1 and a dimensionless gauge coupling g². Choose the kinetic Lagrangian L_kin=(1/(2g²)) dot(theta)^T M1 dot(theta), with gauge-covariant rooted electric derivative convention for nonabelian holonomies. Its canonical electric quadratic form is H_E=(g²/2) D^T M1^-1 D, with operator ordering/group manifold caveats.

To match the continuum quadratic magnetic density in the weak-curvature limit, adopt one magnetic contribution per *pair* of opposite prism faces: (V_cell/(2g²))|F_pair|². Split between two corresponding oriented plaquette loops, and use p_f=Tr_SU2(U_f)/2=1−A_f²|F|²/8+O(A_f³ derivative terms,A_f⁴). This gives the explicit plaquette Wilson multiplier **b_f=(2/g²) sum_{cells incident to f} V_cell/A_f²**, including the correct one-cell boundary and two-cell interior incidences in this chosen prescription. Then H_B=sum_f b_f(1−p_f). This is one defined action convention, not a proof of quantum nonabelian convergence. The theory has not been projected to the gauge-invariant Gauss-law physical Hilbert space.

Formally take each approximant M=5,7,9,11,13,15, scale all physical edges and prism heights by h=1/M (a chosen formal physical scale, not independently calibrated), and use previously verified candidate 3D mass and complete plaquette incidence. Delete bottom horizontal plaquette face 0, retain both other chord-adjacent loops. At g²=1 (fixed illustrative bare coupling), the protected-sector theorem would require rho=8 M_chord,chord (b_horiz+b_vert)/(3g²) <~0.2515.

| M | h | M_chord,chord | b_horizontal | b_vertical | B total | rho | Criterion |
|---:|---:|---:|---:|---:|---:|---:|---|
|5|0.200000|0.04704556|25.71208|19.38097|45.09305|5.65714|FAIL|
|7|0.142857|0.03445817|39.90614|26.87836|66.78450|6.13672|FAIL|
|9|0.111111|0.03135971|65.11528|28.15027|93.26556|7.79942|FAIL|
|11|0.090909|0.02159502|60.47222|41.86538|102.33760|5.89329|FAIL|
|13|0.076923|0.01759319|65.32152|48.60774|113.92925|5.34501|FAIL|
|15|0.066667|0.01939508|116.55173|48.60174|165.15347|8.54177|FAIL|

Since M_ee scales with h and the area-normalized b values scale with 1/h, the ratio is **independent of h under pure uniform scaling of each fixed cell pattern**, aside from approximant-shape variation, at fixed bare g². In this convention rho scales as 1/g⁴. Renormalization of g²(h), a physical matching condition, and convergence are not established, so no limit claim follows. In fact asymptotically small g²(h) would make the stated small-coupling sufficient criterion less favorable, not more favorable, all else equal.

**Critical outcome:** the fully action-normalized three-dimensional candidate invalidates any attempt to directly reuse the tiny 2D illustrative b=3/32000 coefficient as the physical 3D Wilson term. None of the six candidates satisfies the R3-IR-556 *sufficient* small-B criterion at g²=1. This does NOT disprove the corresponding cap-protection statement; it only defeats this particular sufficient perturbative/Sobolev certificate at these coefficients.

Caveats: current edge masses are candidate Q1 3D Whitney forms, not the historical 11-face matrix; the model is one-prism-layer and not a nested fixed-volume continuum refinement; no unique quantum ordering, charge/gauge constraints, physical scale calibration, or running coupling is proved. Relative cap protection is not by itself a continuum spectral mass gap. Reproducible script `audit_prism3d_action_normalization.py` and JSON `prism3d_action_derived_coefficients_2026-10-31.json` are persisted in ChatGPT Library /The Singular Boundary/Source, no binaries in Git.

Next obligation: derive and implement exact gauge-covariant nonabelian electric operators on the full 3D edge graph, impose Gauss law, choose magnetic plaquette regularization consistently, and seek a nonperturbative relative-cap or spectral estimate appropriate to the physically large Wilson coupling; do not force a spurious small-coupling certificate.
