# R3-IR: exact local Wilson response f-sum and neighboring-loop sign

**Date:** 2026-10-31. **Status:** exact finite-volume interacting-vacuum theorem. No regulator-uniform center-current estimate or continuum mass gap.

## Setting

On the original finite link space \(SU(2)^E\) with product Haar, let
\[
H_f^-=\sum_e a_e(-\Delta_e)+V_-,\qquad
V_-=\sum_{g\ne f}b_g(1-p_g),\quad a_e>0,\ b_g\ge0.
\]
Each oriented simple plaquette word uses any given edge at most once. The strictly positive normalized ground state \(\Omega=\Omega_f^-\), with energy \(E_0\), is taken as an eigenfunction on the full original-link space; it is Gauss invariant. The three left-invariant orthonormal generators \(X_{e,a}\) have \(X_a=i\sigma_a/2\) and \(\sum_a X_{e,a}^2=\Delta_e\). All domains are smooth on the finite compact manifold.

## Theorem: exact response f-sum

For each original link and Lie direction, define
\[
Q_{e,a}=\langle X_{e,a}\Omega,(H_f^--E_0)X_{e,a}\Omega\rangle\ge0.
\]
Then
\[
\boxed{ Q_{e,a}=\frac12\int (X_{e,a}^2V_-)\,\Omega^2\,d\mu.}\tag{LR-1}
\]
Consequently, with \(p_g=\tfrac12\operatorname{ReTr}W_g\),
\[
\boxed{\sum_{a=1}^3Q_{e,a}=\frac38\sum_{g\ne f:e\in\partial g}b_g\,\mathbb E_{\Omega^2\mu}p_g,}\tag{LR-2}
\]
\[
\boxed{0\le\sum_{a=1}^3Q_{e,a}\le\frac38\sum_{g\ne f:e\in\partial g}b_g.}\tag{LR-3}
\]
If exactly one retained face \(g\) touches a deleted target boundary link \(e\), \(b_g>0\), then \(\mathbb E p_g\ge0\). If no retained magnetic face touches \(e\), \(X_{e,a}\Omega=0\) for all a (the positive ground-state eigenspace is simple), yielding exact link independence / private-edge Haar marginal.

**Proof.** Each original-link Killing generator commutes with all original-link Laplacians, and the multiplication-potential commutator is \([H_f^-,X_{e,a}]=-X_{e,a}V_-\). Applying \(H_f^--E_0\) to \(X_{e,a}\Omega\) gives \(-(X_{e,a}V_-)\Omega\). Thus
\[
Q_{e,a}=-\int(X_{e,a}\Omega)\,(X_{e,a}V_-)\Omega\,d\mu
=-\frac12\int X_{e,a}(\Omega^2)\,X_{e,a}V_-\,d\mu
=\frac12\int\Omega^2\,X_{e,a}^2V_-\,d\mu,
\]
using skew-adjointness of the Haar Killing field. For a simple Wilson plaquette containing \(e\), regardless of whether the edge occurs forward or backward in the word, \(\Delta_ep_g=-\tfrac34p_g\); hence \(\Delta_eV_-=\tfrac34\sum_{g\ne f:e\in\partial g}b_gp_g\). Sum LR-1 over a. The upper bound uses \(p_g\le1\) and positivity of each \(Q_{e,a}\). If no retained potential depends on e, each Q vanishes; since the positive eigenspace is one dimensional, \(X_{e,a}\Omega=0\). QED.

## Interpretation and limitations

This genuinely controls an interacting-vacuum response **first spectral moment** by local Wilson interactions, with no inverse diffusion generator and no assumed gap. In the spectral decomposition, \(Q_{e,a}=\sum_{n>0}(E_n-E_0)|\langle\Omega_n,X_{e,a}\Omega\rangle|^2\), understood in the full Hilbert space, not a putative gauge-invariant excitation sector: \(X_{e,a}\Omega\) need not be Gauss invariant. The result does **not** control \(\|X_{e,a}\Omega\|^2\), the inverse-generator response, the conditional score on a rare target cap, or the full transport-response for position-dependent multi-edge generators. For Wilson couplings \(b_g=O(h^{-2})\), LR-3 is not small enough by itself to show \(\mathfrak T_{f,h}=o(h^{-1/4})\). The earlier capacity and full-endpoint-jet obstructions still apply.

**Next gate:** prove a Wilson-specific collar estimate linking conditional inward/outward score to this local response without an unproved gap, or show explicitly why the local first-moment f-sum is insufficient.

## Verification

`verify_local_wilson_response_sumrule.py` checks the SU(2) Casimir second derivative with 250 noncommuting four-link words and randomly assigned positive b, using symmetric finite difference and exact Lie-algebra differentiation. Max residuals: finite difference \(7.41045\cdot10^{-8}\); analytic \(2.23\cdot10^{-16}\). It checks the differential normalization, not the physical vacuum expectation. Proof depends on exact commutator/integration-by-parts algebra.