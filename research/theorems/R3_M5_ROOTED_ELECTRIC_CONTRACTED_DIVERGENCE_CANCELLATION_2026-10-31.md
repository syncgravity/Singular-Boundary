# R3-IR-606 — Exact contracted divergence cancellation in the candidate rooted electric operator

Date 2026-10-31. This result applies **only to the natural candidate rooted operator R3-IR-604**, not an independently established unique original Penrose physical Hamiltonian.

Let (K_{ef}) be the fixed inverse M5 Whitney edge mass matrix, (P_{s(e)}) the oriented rooted spanning-tree transport to the source of edge (e), and (R_e=\mathrm{Ad}(P_{s(e)})\in SO(3)). For left-invariant link derivatives (X_{e,a}) with standard Lie generators (J_a), define (A_{ea,fb}(U)=K_{ef}[R_e^T R_f]_{ab}). Then **for every configuration, edge f and index b**,

[
\sum_{e,a}X_{e,a}A_{ea,fb}(U)=0.
]

Proof: A spanning-tree path (P_{s(e)}) never contains its own edge e, so (X_e R_e=0). If e is absent from (P_{s(f)}), then (X_e R_f=0). If present in forward orientation, decompose (P_{s(f)}=P_{s(e)}U_e Q). Hence (R_e^T X_{e,a}R_f=J_a\mathrm{Ad}(U_e Q)). For reverse traversal, (P_{s(f)}=P_{t(e)}U_e^{-1}Q=P_{s(e)}U_eU_e^{-1}Q) is not a valid general simplification because the **prefix** to (t(e)) need not be (P_{s(e)}U_e) when the tree is rooted opposite to the edge orientation. Instead use the root path to the target: (P_{s(e)}=P_{t(e)}U_e^{-1}), and (P_{s(f)}=P_{t(e)}U_e^{-1}Q=P_{s(e)}Q); then (X_{e,a}R_f= -R_e J_a\mathrm{Ad}(Q)). In both cases (sum_a[J_a M]_{ab}=0), since ((J_a)_{ab}=0) for each a,b. Thus the contracted derivative vanishes term-by-term. The non-tree links never occur in any root path.

The corresponding nonnegative quadratic-form operator with Haar link measure is (H_E=-\tfrac12\sum_{ea,fb}X_{ea}(A_{ea,fb}X_{fb})). Because the contracted coefficient derivative vanishes, on a smooth gauge-covariant core its formal differential expression simplifies to (-\tfrac12\sum_{ea,fb}A_{ea,fb}X_{ea}X_{fb}) with the displayed derivative ordering. This is not an assertion that mixed derivatives commute, or that gauge fixing can discard derivatives on tree edges.

Audited all 98 edges and 264 rooted path-edge occurrences of the actual M5 tree. Maximum per-path contraction residual 6.79e−16; full divergence residual 3.08e−14; independent finite-difference block derivative residual 1.42e−8. Verification used a reproducible random SU2 configuration.

**Crucial limits:** This cancellation is a property of the specified R3-IR-604 coefficient A, not proof that the historical Penrose Hamiltonian uses this operator. It does NOT entail scalar radial closure for a face trace, because (\Gamma(p_f,p_f)) remains configuration dependent and (Lp_f) may likewise. It does not compute the interacting deleted ground state or its conditional a,b,c; the conditional drift defect (\delta=b-a'-a(\log w_H)') may be nonzero after vacuum conditioning. No regulator-uniform current or continuum mass gap follows.

Reproducible executable `audit_M5_rooted_divergence_cancellation.py` and numerical JSON `m5_rooted_candidate_divergence_cancellation_2026-10-31.json` in Library `/The Singular Boundary/Source/`.
