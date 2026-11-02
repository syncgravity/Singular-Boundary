# R3-IR: Interior conditional gap and centering audit (2026-11-02)

For an open straight finite square SU(2) strip, let T_j be the three links newly introduced by an interior plaquette j+1. With the full complement T_j^c fixed, the T_j-conditional dressed reference density is proportional to ψ_g(p_{j+1})² ψ_g(p_{j+2})² dHaar³. Prior certified 24/25≤ψ_g≤26/25 gives max/min density ≤(13/12)^4. Haar³ Poincaré gap 3/4 and density comparison prove **λ_int≥(3/4)(12/13)^4=15552/28561≈0.54451875**, uniformly in strip length, spectators and conditioning.

Therefore for N_j u=E[u|T_j^c],
||u−N_j u||₂≤sqrt(28561/15552)(Σ_{e∈T_j}||∇_e u||₂²)^{1/2}.
Conditional on the earlier physical-link weighted Bochner resolvent theorem, for smooth centered F supported in S, u=L_N⁻¹F, r=d(T_j,S),
||u−N_j u||₂≤sqrt(28561/15552)(120/11)(5/6)^r||∇F||₂.
This is a genuine interior full-strip fluctuation bound.

**Centering obstruction:** w_j is conditionally centered given the old prefix, not necessarily given T_j^c, because ψ_g(p_{j+2})² tilts the conditional distribution. The exact identity
<w_j,u>=<w_j−N_j w_j,u−N_j u>+<N_j w_j,N_j u>
contains an uncontrolled conditional mean term. The first term inherits weighted spatial decay. Comparing the added future weight against the one-face centered law gives ||N_j w_j||∞≤v[(13/12)²−1]=25/165888≈0.000150704 for v=1/1152; this does not decay with source separation. An exact two-point change-of-measure countermodel demonstrates the centering issue, without claiming a nonzero SU(2) expectation.

The relative third-order connected response and interacting λ=1/continuum Yang–Mills mass gaps remain **open**. Full detailed audit, exact-rational verifier, log and SHA-256 manifest in Library /The Singular Boundary/Proof Audits.