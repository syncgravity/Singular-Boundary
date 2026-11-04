# Exact magnetic-deletion variational identity with physical SU(2) normalization
Date: 2026-10-30
Status: rigorously proved finite-volume upper bound; no new uniform Penrose scaling claimed.

Let H_-=sum_e a_e(-Delta_e)+V_- on the finite product of SU(2) links, where -Delta chi_j=j(j+1)chi_j, and H_+=H_-+b_f(1-p_f), p_f=Tr(W_f)/2. Let Omega_->0 be normalized ground state of H_- with energy E_-. Let nu_- be the full class-angle u=arccos p in [0,pi] law under Omega_-² Haar. Set D=A_f/4 with A_f=sum_{e in boundary f}a_e, simple face word.

For any nonzero real Lipschitz g on [0,pi], the physical gauge-invariant trial Omega_- g(u_f) has Rayleigh quotient
E_- + [ D int |g'(u)|² dnu_-(u) + b_f int(1-cos u)g(u)² dnu_-(u)]/[int g² dnu_-].
Thus
0 <= Delta_f=E_+-E_- <= inf_{g != 0} [ D int |g'|² dnu_- + b_f int(1-cos u)g² dnu_-]/int g² dnu_-.
Proof: the ground-state transform <g Omega_-,(H_--E_-)g Omega_->=int Omega_-² Gamma_a(g(u),g(u)) dm; Gamma_a(u)=D; add the magnetic potential. All identities hold in the interacting model.

Explicit corollary: for 0<r<=pi, define g_r(u)=1 for u<=r/2, linearly decrease to 0 by u=r, and zero beyond. Writing m_-(s)=nu_-([0,s]), one obtains
Delta_f <= [ (4D/r²) m_-(r) + b_f (1-cos r)m_-(r)]/m_-(r/2).
In particular Delta_f <= [A_f/r²+b_f(1-cos r)]/m_-(r/2). This elementary upper bound is generally weaker than the logarithmic/capacity optimization of earlier papers; it serves as an independent normalization and variational consistency test. The cap is a single identity-center cap, not the center-folded union. A center-folded marginal alone cannot substitute for this trial without accounting for its two branches.

The desired O(h^-1 polylog h^-1) comparison is NOT proved: the denominator m_-(r/2) must be controlled relative to the numerator and geometry. The earlier claimed logarithmic variational bound has not been reverified in this note. The uniform true deleted Penrose cap-mass estimate remains OPEN.
