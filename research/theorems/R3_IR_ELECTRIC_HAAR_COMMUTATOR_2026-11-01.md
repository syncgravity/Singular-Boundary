# Electric/Haar commutator audit — 2026-11-01

**Scope:** finite open SU(2) face chains under the constant-coefficient invariant-derivative hypothesis of the intrinsic Peter–Weyl bound.

Let E_i be Haar averaging over face i, and let L_{i,α},R_{i,α} be left/right invariant vector fields. If every original-link derivative D_{e,α} is a fixed real linear combination of these fields, and K=−Σ_{e,α} a_e D_{e,α}² with fixed nonnegative link weights, then **[E_i,D_{e,α}]=[E_i,K]=0**. Indeed E_i L_i=L_i E_i=E_i R_i=R_i E_i=0 by Haar invariance; derivatives at other faces commute with E_i. Polynomial interval-hull projections H_I therefore commute with K and the centered reduced inverse K⁻¹ (by spectral calculus). The statement holds for arbitrary finite chain size and fixed weights.

This is an exact theorem *for the stated model*, not independent verification that all terms of the physical gauge-fixed Hamiltonian, including boundaries and possible holonomy-dependent coefficients, have that form. Counterexample to careless extension: on T², with K=−∂_x[(2+cos y)∂_x], E_y K cos x=2 cos x whereas K E_y cos x=(2+cos y)cos x; commutation fails.

Interval hull and interaction connectivity differ: if f(A),g(C) are Haar-centered with disjoint original-link derivative supports, f(A)g(C) has hull [A,C] but Γ(f(A),g(C))=0. By contrast the previously checked adjacent-face identities yield Γ(a,b)=(ab−r_AB)/4 and K⁻¹Γ(a,b)=ab/22−2r_AB/55, a genuine shared-link contribution.

**Research verdict:** The Haar commutator and hull-Poisson compatibility are established for the constant-coefficient invariant-field electric model. Physical gauge-fixing conformity and a true graph-connected tree expansion are unverified; all-order majorants, interacting λ=1 gap, Penrose current, and continuum mass gap remain open. Full derivation, executable checker, log, and hash manifest are archived in Library Proof Audits under R3_IR_ELECTRIC_HAAR_COMMUTATOR_2026-11-01.zip.