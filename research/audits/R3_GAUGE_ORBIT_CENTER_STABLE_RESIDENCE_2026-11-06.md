# P2/T2 — Gauge-invariant full-center-orbit residence using a nonlinear center-stable graph
**2026-11-06 | finite 3D original-link SU(2) theorem candidate | independent review pending | ALL continuum P0–P5 and T0–T5 gates OPEN**

**Source lineage:** finite signed-Hessian PR #83, original-coupled-vacuum cap PR #85, nonlinear individual-point residence PR #86, which was independently rerun (631 assertions passed) and merged to main as `2094d6d2198826031230a3acf9e30a23e74df804` before this audit. The full current mathematical report, executable verifier, execution log, SHA-256 manifest and ZIP are in the user's Library at `/The Singular Boundary/Proof Audits/R3_GAUGE_ORBIT_CENTER_STABLE_RESIDENCE_2026-11-06.zip`.

## Exact gauge-orbit geometry
On X=SU(2)^E with compact local gauge group G=SU(2)^V, take a center-valued configuration U* with an unstable negative-Hessian direction, e.g. one negative interior link. Its entire orbit O=G·U* is an embedded compact stationary submanifold. On a connected graph, its stabilizer is diagonal SU(2). Therefore dim(O)=3(V−1), normal codimension q=3(E−V+1). The original-link Wilson Hessian at U* equals (1/4)Bᵀdiag(z_p)B ⊗ I₃. Gauge tangent directions are in its kernel (S is invariant and U* critical). For the single-negative-interior-link witness, the signed edge Rayleigh quotient is −1, so the normal descent linearization L=−Hess S has largest positive eigenvalue at least 1. Its full positive eigenspace W^u is normal to the gauge orbit and has rank m≥3 (SU(2) Lie-algebra multiplicity). Define λ_*>0 as the **smallest** positive eigenvalue of L on W^u; do NOT infer λ_*≥1 from the largest eigenvalue.

## Proposed finite-time gauge-invariant residence theorem
The compact equivariant tubular-neighborhood theorem and the equivariant local center-stable manifold/graph-transform theorem provide (at each fixed finite regulator) a G-equivariant local center-stable graph u=ψ_y(z) over the nonpositive normal spectral directions, with u∈W^u_y. In a sufficiently small orbit tube, the deviation η=u−ψ_y(z) satisfies d||η||/ds ≥ (λ_*−C_hR r)||η|| along trajectories remaining in the radius-r tube. The key is graph invariance: nonlinearity in the transverse *deviation* is O(r||η||), not an additive O(r²) forcing. Taking r so γ=λ_*−C_hR r>0 gives
\[
\{\operatorname{dist}(\Phi_tU,O)\le r,\quad 0\le t\le s\}
\subseteq\{||\eta_0||\le C'_{h,R}r e^{-\gamma s}\}.
\]
Unlike PR #86's linear-hyperplane constraint, **this gauge-orbit-based constraint has no quadratic floor**. The choice of invariant center-stable graph is local and depends on the finite regulator; the statement does not require an isolated stationary point modulo gauge.

Let ν=Ω²μ be the *genuine coupled* SU(2) finite-regulator quantum ground-state measure of H=αΣ_e(−Δ_e)+β S, α=g₀²/(2h), β=2/(g₀²h). Smooth positivity implies M_hR=||Ω²||∞<∞ **only at fixed regulator**. Tubular coarea and the unstable fiber rank give the finite-regulator bound
\[
\boxed{\nu(\mathcal R_O(s,r))\le\min\{1,K_{h,R}M_{h,R}r^q e^{-m\gamma s}\},\qquad m\ge3.
\]
K_hR includes the compact orbit volume, coordinate comparability and graph geometry. In particular, the entire gauge-orbit attraction basin has ν-measure zero. In contrast with individual-point basin results, this event is fully gauge invariant.

## Key limitations and next target
At physical flow s=τ/h², NO bound uniform in mesh spacing, volume or coupling has been shown: M_hR, K_hR, center-stable chart radius, C_hR and λ_* can vary with the regulator. The orbit tube involves all links and is NOT a fixed-physical-support, renormalized positive-time curvature observable. Do not equate it with 4D constructive Yang–Mills existence, an infrared spectral gap, a Penrose equivalence or UV gravity finiteness. The necessary next step is local gauge-invariant conditional/Fisher control of unstable modes and uniform spectral/nonlinear constants, then positive-flow-time renormalized curvature tightness.

## Verification
A deterministic checker passed 2,160 algebraic and nonlinear-graph calibration assertions (n=2…6 cubic complexes; BD=0; Hessian gauge zero modes; orbit and normal dimensions; negative signed Rayleigh quotient and triply-degenerate unstable mode; exact solvable nonlinear invariant graph u'=λu+cz², z'=−μz). These do not constitute an independent proof of the center-stable manifold theorem and do not simulate the interacting vacuum. Complete report, script, test log and hash manifest are retained in Library.
