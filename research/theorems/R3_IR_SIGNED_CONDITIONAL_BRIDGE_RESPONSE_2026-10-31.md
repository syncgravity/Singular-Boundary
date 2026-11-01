# R3-IR — Signed conditional Feynman–Kac bridge response (2026-10-31)

Finite-volume exact identity for the original-link SU(2) deleted-face Wilson Hamiltonian. Set S to the changed links and split V=V0(Z)+V1(X,Z) where V0 contains retained faces disjoint from S. For a fixed spectator Brownian bridge path Z, the changed-link conditional bridge factor is B_lambda(x,y;Z)=k^S_t(x,y) E^0_{x→y}[exp(-lambda J_Z)] where J_Z=∫_0^t V1(X_s,Z_s)ds. The V0 factor cancels at a fixed common spectator path.

Differentiating with respect to lambda gives ∂_lambda log B_lambda=−E_lambda J_Z and ∂²_lambda log B_lambda=Var_lambda(J_Z)≥0. For same endpoint y and two starting changed-link configurations x,x′,

log[B_1(x,y;Z)/B_1(x′,y;Z)] = log[k_t^S(x,y)/k_t^S(x′,y)] − ∫_0^1(E_lambda,x J_Z−E_lambda,x′ J_Z)d lambda.

This signed bridge-response identity is exact, without a global or local worst-case potential oscillation constant. It does NOT bound the signed difference: the estimate |difference|≤t osc_S V1 simply recovers the earlier local Harnack bound. Integrating over spectator bridges changes their relative positive weights, so one must not interchange the logarithm and spectator integration. The remaining obligation is signed control of this conditional expectation difference plus spectator reweighting.

**Potential invariance is not vacuum invariance:** finite-state symmetric Laplacian K=[[2,-1,-1],[-1,5,-4],[-1,-4,5]], potential diag(0,0,2), and swapping states 1,2. The swap preserves V but not K. The positive normalized ground state is (0.4051849679,0.3288193501,0.2659956820), ratio 1.232241861. This is a reversible finite-state logical counterexample, not an SU(2) Wilson vacuum.

Verifier checks 301 coupling values using exact matrix exponentials; signed bridge identity error 1.32e−11, minimal second log-derivative 0.0846. Full proof, source and SHA256 in archive R3_IR_SIGNED_CONDITIONAL_BRIDGE_RESPONSE_2026-10-31.zip. No signed-current, connected-covariance, or continuum gap claim.