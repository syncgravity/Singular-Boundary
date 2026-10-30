# R3 curvature redistribution: exact linear incidence audit

28 October 2026 — The Singular Boundary

## Source and scope

The supplied `penrose_complete_catalogue.npz` has path and cycle indices but lacks an oriented vertex/edge/face map and the historical R3 cavity partition. The supplied source inspection has not recovered exact three-step Penrose prism data. Consequently **this analysis is a certified calculation on the existing one-spatial-plaquette three-step control**, not a result for the actual Penrose R3 complex.

## Mathematical test

Fix a connected finite oriented spacetime cell complex, an insertion set Q and cavity faces C, and a subset E_free of integrated edge variables. At the all-identity field, write U_e=exp(X_e) with X_e in su(2). For each face f, to first order the plaquette holonomy log is

    (A X)_f = sum_{(e,s) in boundary(f)} s X_e,

where A is the integer face-edge incidence matrix, restricted to E_free. Let A_C and A_Q be its cavity and inserted face blocks. An infinitesimal variation leaving all cavity curvatures unchanged belongs to ker A_C. The dimension of the *accessible inserted curvature subspace* is

    rank([A_C; A_Q]) - rank(A_C).

This identity follows from rank-nullity for the map A_Q restricted to ker A_C. Each su(2) color coordinate has the same rank at the flat identity field; the vector-space dimension in su(2) is three times the reported scalar rank. In a collar audit, any varied integrated edge can affect cavity faces outside the collar: **all cavity faces touching movable edges must be included** in A_C.

This is a linear necessary test for a proposed independent local curvature-redistribution operation; it does NOT prove existence of a nonlinear SU(2) repair map, a bounded action comparison, a Jacobian bound, or the near-flat Gibbs event. Rank deficiency also does NOT show that near-flat Q has small probability: Q=I and C=I coexist for identity boundary data.

## Reproduced control output

The published control input is a single oriented square face, trivially extruded across three intervals, with four inserted temporal faces in the middle interval, other faces in the cavity, and no fixed edges. The exact rational ranks computed by SymPy:

| Collar depth | Movable integrated edges | Affected cavity faces | rank(A_C) | rank([A_C;A_Q]) | Accessible Q rank |
|---|---:|---:|---:|---:|---:|
|0|12|10|8|11|3 of 4|
|1|28|12|10|13|3 of 4|
|2|28|12|10|13|3 of 4|

The missing independent direction is consistent with a discrete curvature/Bianchi relation around the spatial plaquette and neighboring spatial faces. Explicit nonlinear SU(2) Bianchi identities are ordered/conjugated, so the linear rank test alone must not be promoted to a nonabelian theorem.

## What would constitute a closing result

For the actual Penrose prism: provide source-verified oriented spatial edges, faces, insertion partition, excluded faces, couplings and fixed boundary link values. Rebuild incidence with `generate_r3_incidence.py` from the previous package; run `audit_linear_repair.py` on the output. If first-order independent curvature directions are obstructed, search for a collective deformation that preserves Bianchi-compatible relations rather than independent plaquette control. Prove a quantitative Gibbs near-flat probability (or directly a partition function ratio) with ambient-uniform constants. A useful strategy is comparison over Bianchi-compatible collective modes, but **no such comparison is proved here**.

## Reproduce

    python -m pip install sympy
    python audit_linear_repair.py control_incidence.json --out control_linear_audit.json
    python audit_linear_repair.py penrose_three_step_incidence.json --out penrose_linear_audit.json

The first command is verified with the bundled control incidence. The second requires genuine Penrose incidence from the original simulation or separately supplied spatial cell complex. Outputs are exact rational linear algebra; they are not statistical certificates.
