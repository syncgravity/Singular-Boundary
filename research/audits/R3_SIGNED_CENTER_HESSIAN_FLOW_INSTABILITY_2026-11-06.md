# P2/T2 — Exact signed center-Hessian obstruction to uniform Wilson-flow contraction

**November 6, 2026. Proposed finite original-link SU(2) cubic theorem; independent review pending. All P0–P5 and T0–T5 remain OPEN.**

Let \(S(U)=\sum_p[1-\frac12\mathrm{tr}_{2}U_p]\), with classical spatial gradient flow \(\dot U=-\nabla S\), physical radius \(\tau=h^2s\), and orthonormal generators \(T_j=i\sigma_j/2\). These are the source conventions of the finite nonlinear Wilson-flow audits.

**Stationary nonflat configurations.** For center-valued links \(U_e^*=z_e I\), \(z_e\in\{+1,-1\}\), each plaquette \(U_p^*=z_p I\) has vanishing character gradient. Hence \(\nabla S(U^*)=0\) and \(\Phi_s(U^*)=U^*\). One interior link equal to \(-I\), all others equal to \(I\), makes exactly four incident plaquettes equal \(-I\), yielding \(S(U^*)=8\).

**Signed Hessian.** Let \(B\) be the oriented face–edge incidence matrix and \(z_p=\prod_{e\in\partial p}z_e\). In normal link coordinates \(U_e=z_e\exp(\sum_j a_e^jT_j)\), the second variation is
\[
S(U^*e^a)=S(U^*)+\frac18\sum_{p,j}z_p(Ba^j)_p^2+O(\|a\|^3).
\]
Baker–Campbell–Hausdorff corrections do not contribute quadratically because the trace is stationary at both central elements. The Hessian has three independent copies of
\[
H_*=\frac14B^\mathsf T\operatorname{diag}(z_p)B.
\]
For the one-negative-link background, the unit perturbation on that link gives \(\langle a,H_*a\rangle=-1\), hence \(\lambda_{\min}(H_*)\le-1\). Equivalently, vary its link as \(-\exp(tT_3)\); the full action is \(4[1+\cos(t/2)]\) and \(S''(0)=-1\).

**Dynamical obstruction.** At any stationary point \(D\Phi_s(U^*)=\exp[-s\operatorname{Hess}S(U^*)]\). Therefore
\[
\|D\Phi_s(U^*)\|_{\mathrm{op}}\ge e^s,\qquad
\|D\Phi_{\tau/h^2}(U^*)\|_{\mathrm{op}}\ge e^{\tau/h^2}.
\]
The unstable mode is not a gauge zero mode: gauge directions satisfy \(Ba=0\) at center backgrounds, unlike the exhibited negative-Rayleigh direction.

**Scope.** This is an exact all-configurations **global Lipschitz/contraction obstruction**, stronger in analytic precision than the earlier numerical maximum-principle witness. It does **not** refute a vacuum-weighted positive-physical-time smoothing estimate; exact center backgrounds are Haar-null and hence have zero probability under the finite smooth quantum vacuum density. A probability or moment estimate for a precisely renormalized flowed observable under the actual interacting ground-state law remains the P2/T2 target.

**Verification.** The accompanying executable cubic incidence and Hessian verifier checks \(n=2,3,4,5\), with 40 deterministic assertions. The least calculated Hessian eigenvalues are approximately \(-1.691769060,-1.662525115,-1.662319789,-1.662318189\). These numeric regressions are not substitutes for the exact min–max proof. The complete local derivation, verifier, execution log, and SHA-256 manifest are preserved in Library → The Singular Boundary → Proof Audits, in R3_SIGNED_CENTER_HESSIAN_FLOW_INSTABILITY_2026-11-06.zip.

No canonical proof gate, theorem count, prior simulation archive, main branch, or public hosting is changed.