# Original-link SU(2) face Ward identity independent of rooted-coordinate choice

Date: 2026-10-31. Status: exact finite-graph theorem with a separately verified numerical diagnostic; no refinement-uniform estimate. This is a continuation of the ROOTED_TRANSPORT_PROOF_AUDIT_2026-10-31.md, and must not be read as proof that every rooted-coordinate coefficient divergence vanishes.

## Exact setting
Let E be a finite oriented graph, G=SU(2), Haar product measure dμ, and X_{e,a} left-invariant vector fields with generators T_a=iσ_a/2. Then Δ_e=Σ_a X_{e,a}², and Δ_e (Tr U_e/2)=-3/4 (Tr U_e/2). Let f be a face with a *simple* oriented cyclic link word W_f=U_{e_1}^{s_1}...U_{e_m}^{s_m}, with each edge appearing once, and define p_f=ReTr W_f/2. Let L=Σ_e a_e Δ_e, a_e>0 constant per link, A_f=Σ_{e∈∂f}a_e. For the deleted Hamiltonian H_f^-=-L+V_- with smooth real gauge-invariant potential independent of the target plaquette coefficient, let Ω>0 denote its normalized, smooth ground-state amplitude on G^E. For the Ward identity, no assumption that Ω is Haar in p_f is made.

## Theorem 1: exact original-link coefficients
For each participating e and every configuration,

Γ_e(p_f,p_f)=Σ_a(X_{e,a}p_f)²=(1-p_f²)/4,
Δ_e p_f= -3p_f/4.

For e outside the face, both expressions vanish. Therefore

Γ(p_f,p_f)=Σ_e a_e Γ_e(p_f,p_f)=A_f(1-p_f²)/4,
Lp_f=-3A_f p_f/4.

Proof. Fix all other links. For a participating link, the oriented word is a product of fixed SU(2) matrices, U_e or U_e^{-1}. By cyclic invariance of trace and the isometry/inversion invariance of the bi-invariant SU(2) metric, the scalar p_f as a function of U_e is a translated or inverted fundamental character p(U)=Tr U/2. In quaternionic coordinates U=x_0 I+i x·σ with x_0²+|x|²=1, p=x_0, and the chosen SU(2) generators give |∇p|²=(1-p²)/4 and Δp=-3p/4. The identical identities therefore hold for any edge orientation and all fixed adjacent links. Sum with weights a_e.

## Theorem 2: exact physical marginal Ward relation
Let ρ(p)dp be the pushforward of Ω²dμ under p_f, and w(p)dp the corresponding pushforward of dμ. Then w(p)=(2/π)√(1-p²) on -1<p<1. Set

C_f(p)=E_{Ω²}[Γ(p_f, log Ω) | p_f=p].

Since Γ(p_f,p_f)=a(p)=A_f(1-p²)/4 is already constant on each p fiber and Lp_f=b(p)=-3A_f p/4, integration by parts yields, distributionally,

(ρa)'=ρ[b+2C_f],      (wa)'=wb.

If ρ=w ψ_f² with ψ_f>0, subtract the free Haar equation:

(log ψ_f)'(p)=C_f(p)/a(p)=4C_f(p)/[A_f(1-p²)].

Writing p=cos u, 0<u<π, gives

**d/du log ψ_f(u)=-4 C_f(cos u)/(A_f sin u).**

The exact identity is unaffected by a change to valid rooted face coordinates: both Γ(p,p) and Lp are scalar intrinsic functions on original-link configuration space. No hypothesis that the individual rooted-coordinate drift components vanish is needed to derive this specific *radial* identity. Gauge invariance of Ω and p makes conditional quantities gauge-invariant almost everywhere.

## The next gate, still open
The result bypasses a potentially unnecessary full rooted-coordinate coefficient cancellation calculation *for the single face-trace marginal*. It does **not** establish coefficient-by-coefficient cancellation for an asserted rooted kinetic metric, nor control mixed face observables, conditional densities over an entire rooted fiber, or any uniform current bound. In particular the physically required sup_{f∈D_R} T_{f,h}=o(h^{-1/4}) remains open. For claims requiring the full joint kinetic operator in face coordinates, the ordered primal spanning tree and all D_i^α, K^{αβ}, b^β remain to be reconstructed and tested.

## Deterministic check
`verify_root_independent_face.py` samples noncommuting SU(2) link configurations for all 16 orientations of a four-edge loop, 25 configurations per pattern, and evaluates all 4 links (1600 edge tests). The max residual is 2.09e-10 for |∇p|² and 1.37e-7 for Δp using symmetric differences of size 1e-4. It is a diagnostic of the exact algebra, not statistical or continuum evidence.

## Sources and provenance
- Previous local rooted audit: ROOTED_TRANSPORT_PROOF_AUDIT_2026-10-31.md (prior conversation attachment).
- Original-link deleted-face Hamiltonian and independent-face coordinates: `sources/historical/raw/Archive_3/singular_boundary_deleted_face_orbit_transport_2026-10-29.zip/__nested__/sb_deleted_face_orbit_transport_20261029/PROOF_REPORT.md` in syncgravity/singular-boundary.
- Canonical state record: `docs/current/CANONICAL_RESEARCH_STATE_2026-10-30.md`.

Proof claims are for finite simple face words only, and do not apply without modification to paths with repeated link variables. No mass gap or continuum theory follows.