# R3-IR — Quadratic center suppression and score-response endpoint compatibility

Date: 2026-10-31. Status: exact **fixed finite-volume** original-link SU(2) Wilson theorem; no regulator-uniform estimate.

## Hypotheses

Use a finite original-link SU(2) graph with a simple target face f, target edge e, smooth positive Gauss-invariant ground state Ω of the target-magnetic-deleted Wilson Hamiltonian. Assume the exact projected score-force balance from `R3_IR_CONDITIONAL_WILSON_FORCE_PROJECTION_2026-10-31.md`:

(ρK)'=ρ(B+L),

with B(p)=E[Σ_a η_a F_a|p_f=p], K(p)=E[Σ_a η_a Γ(p_f,v_a)|p_f=p], L(p)=E[Σ_a Γ(η_a,v_a)|p_f=p], η_a=X_e,a p_f, v_a=X_e,a logΩ, F_a=X_e,a V_- and ρ(p)=(2/π) sqrt(1-p²) ψ(p)².

## Theorem 1 (quadratic endpoint force)

**B is a smooth function on the closed class interval [-1,1] with B(1)=B(-1)=0.** Consequently, for the fixed finite graph, there exists finite C_B such that

|B(p)| ≤ C_B(1-p²),  -1≤p≤1,

and hence |B(cos u)| ≤ C_B sin²u, including near the identity center. This improves the geometric bound |B(cos u)| ≤ (Σ_neighbor b_g/4) sin u, but **C_B is not shown to be uniform in h, graph volume, or couplings**.

Proof: Fix remaining original links y and choose the target edge x such that W_f(x,y)=W. The variable change x↔W is a smooth Haar-preserving left/right translation or inversion. Integrate Ω²Ση_a F_a over y to obtain a smooth function N(W) on SU(2); similarly D(W)=∫Ω²dy>0 is smooth. Under simultaneous global conjugation, the full contraction Ση_a F_a is a scalar and Ω² is invariant, so N and D are conjugation-invariant. Thus N(W)=n(p(W)) and D(W)=d(p(W)) with n,d smooth up to p=±1: a smooth conjugation-invariant function on SU(2) is a smooth function of the trace class coordinate, including the central endpoints (radial evenness in exponential coordinates). Their ratio B=n/d is smooth on [-1,1]. At W=±I all original-link derivatives η_a=X_e,a p_f vanish pointwise, so N(±I)=0, hence B(±1)=0. Division by (1-p²) extends continuously to both endpoints, proving the finite C_B bound. No property of the vacuum beyond smoothness, positivity and global invariance yields a regulator-independent C_B.

## Theorem 2 (exact endpoint compatibility for L)

The same fiber integration shows K and L smooth on [-1,1]; moreover K(±1)=0 because η_a=0 at the two group centers. Let k=lim_(p→1−) K(p)/(1-p), finite. Since ρ(p)=c(1-p)^{1/2}(1+O(1-p)) with c>0, the projected balance forces

**L(1)=-(3/2) k, equivalently K(p)=-(2/3)L(1)(1-p)+O((1-p)²)**.

Indeed (ρK)'/ρ→-(3/2)k and B(p)→0. Thus the leading endpoint source of the projected balance is **L**, not B. In particular, the quadratic center suppression of the Wilson force **cannot** be used to drop the nonadiabatic score response. The same argument at p=-1 gives L(-1)=+(3/2) lim_(p→-1+) K(p)/(p+1).

The endpoint formula is a compatibility identity, **not** a bound on L(1) or the one-sided score; it does not improve the required h-scaling without an independent uniform estimate on derivatives of the conditioned fiber score. It is compatible with the earlier fixed-volume center-jet theorem and Fisher-capacity obstruction.

## Reproducibility and exclusions

`verify.py` checks 24 synthetic smooth central source/response integral models for the endpoint coefficient and the identity sin²u=1−cos²u. The synthetic models are algebraic diagnostics, **not** ground states of complete Wilson cages; the theorem follows from the finite-dimensional smooth-fiber argument, not these quadratures. Historical Stage26 data were not modified. The production 2+1D M55 torus is not silently identified with the continuum 3D Hamiltonian program.

**OPEN:** refinement-uniform C_B, L(1) or radial score bound, anti-depletion, sup_f T_(f,h)=o(h^-1/4), covariance, and continuum Yang–Mills mass gap.