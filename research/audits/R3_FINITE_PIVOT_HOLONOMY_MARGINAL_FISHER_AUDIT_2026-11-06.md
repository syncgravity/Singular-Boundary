# P2/T2 — Local joint interacting-vacuum holonomy marginals via private original-link pivots
**2026-11-06; proposed finite-cubic SU(2) theorem for independent review. All continuum P0–P5/T0–T5 and mass-gap gates OPEN.**

**Predecessor:** PR #88 merged to main as `42ea61d3ffdb62458e928fd507281ba6913e901d` after its archived 5,730-check verifier passed. This note requires only the previously established exact coupled-vacuum one-link kinetic bound (PR #81), not the center-stable theorem.

Let X=SU(2)^E carry product Haar and metric T_a=iσ_a/2. Let Ω>0 be the genuine *coupled gauge-invariant* normalized ground state of H=α Σ_e(−Δ_e)+β Σ_p(1−½Tr U_p), with α=g₀²/(2h), β=2/(g₀²h). At every fixed regulator, `∫|∇_e Ω|²≤32/g₀⁴` holds for every original link.

Choose k distinct observed plaquettes p_j, with a **private pivot** e_j∈∂p_j not on any other observed plaquette boundary. The observed plaquettes need not be edge-disjoint; in particular the four faces surrounding one interior link admit four private *peripheral* pivots.

**Theorem A (joint marginal Fisher bound).** Write ρ_k for the joint SU(2)^k holonomy density under the actual coupled vacuum; although a based holonomy tuple is gauge-covariant, its class/trace events are gauge invariant. Then
\[
\sum_{j=1}^k\int_{SU(2)^k}|\nabla_{v_j}\sqrt{\rho_k}|^2\,dv\le \frac{32k}{g_0(h)^4}.
\]
**Proof:** With all nonpivot links w frozen, each U_pj=A_j(w)u_j^{±1}B_j(w) depends on exactly its own pivot u_j. The product map of the pivots to the observed SU(2) holonomies is a Haar-preserving product Riemannian isometry. Writing Ψ(v,w)=Ω(u(v,w),w), we have ρ_k(v)=∫|Ψ(v,w)|²dw. The differential of the Hilbert norm satisfies |∇_vj√ρ_k|²≤∫|∇_vj Ψ|²dw. Integrate, pull back by the isometry and sum using the true-vacuum linkwise kinetic estimate. No factorization of the interacting vacuum, no gauge fixing, and no global ∥Ω²∥∞ estimate enter.

**Theorem B (joint gauge-invariant negative-center caps).** For δ_j∈(0,1), let C_j={1+½Tr(U_pj)≤δ_j}. The exact single-SU2 cap Haar volume is v(δ)=(θ−sinθ cosθ)/π, θ=arccos(1−δ), and v(δ)~(4√2/3π)δ^(3/2). The compact D=3k dimensional Sobolev inequality for √ρ_k and Hölder give
\[
\nu(\cap_j C_j)\le \min\{1,C_k(1+32k/g_0(h)^4)\prod_j v(\delta_j)^{2/(3k)}\}.
\]
For common δ, this is at most C_k v(δ)^(2/3)(1+32k/g₀⁴)=O_k(δ(1+kg₀⁻⁴)). **It is NOT an independent-face δ^k law**: one derivative of Fisher regularity does not imply higher mixed-derivative estimates.

The constants are uniform in the size of the containing cubic box for fixed k and bare coupling; C_k is not uniform when k grows. Fixed k elementary plaquettes occupy *shrinking* physical support O(h); this is NOT a fixed-physical-radius curvature theorem, nonlinear flow residence theorem, interacting infrared Schur/gap estimate, 4D OS construction, Penrose comparison, or gravity UV theorem. Weak-coupling g₀→0 worsens the bound. No canonical Observatory gate promotions.

**Reproducibility:** full mathematical derivation, 2,748 passing original-link incidence/private-pivot/Haar-cap/Hilbert-norm contraction checks, executable Python source, log and SHA-256 manifest are stored in Library `/The Singular Boundary/Proof Audits/R3_FINITE_PIVOT_HOLONOMY_MARGINAL_FISHER_2026-11-06.zip`. Next open target: physical-radius smeared gauge-invariant observable with k(h) growing and a genuinely refinement-uniform conditional Fisher/covariance estimate, ultimately combined with signed nonlinear spatial flow.
