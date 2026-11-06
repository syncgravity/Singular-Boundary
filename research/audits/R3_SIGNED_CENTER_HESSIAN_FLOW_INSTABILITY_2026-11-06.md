# P2/T2 exact signed center-Hessian obstruction (2026-11-06)

**Scope:** Full original-link classical SU(2) spatial Wilson gradient flow on a finite open 3D cubic lattice. Independent review pending; P0–P5, T0–T5, interacting quantum curvature and continuum mass gap OPEN.

Let (S(U)=\sum_p[1-\frac12\operatorname{tr}_2U_p]), (\dot U=-\nabla S), (\tau=h^2s). Any center-valued link configuration (U_e^*=z_eI\), (z_e\in\{\pm1\}\), is stationary since every plaquette is (±I) and its class-character gradient vanishes. Set one four-face-incidence link to (-I) and all others to (I); exactly four plaquettes have sign (-1) and (S(U^*)=8).

With oriented face-edge incidence (B), and (z_p=\prod_{e\in\partial p}z_e), expand link coordinates (U_e=z_e\exp(\sum_j a_e^jT_j)) for (T_j=i\sigma_j/2). The exact quadratic action is
[
S(U^*e^a)=S(U^*)+\frac18\sum_{p,j}z_p(Ba^j)_p^2+O(\|a\|^3).
]
Thus each of the 3 Lie-algebra components has Hessian (H_*=(1/4)B^\mathsf T\operatorname{diag}(z_p)B). On the one-link-supported unit perturbation (\langle a,H_*a\rangle=-1), hence (\lambda_\min(H_*)\le-1). At a stationary point the Jacobian of negative-gradient flow is (D\Phi_s(U^*)=\exp(-s\operatorname{Hess}S(U^*))), so
[
\|D\Phi_{\tau/h^2}(U^*)\|_{op}\ge\exp(\tau/h^2).
]
Independent exact one-link check: along (U_{e_*}=-\exp(tT_3)), the action is (4[1+\cos(t/2)]), whose second derivative at zero is (-1).

This supplies an **analytic**, rather than merely numerical, obstruction to universal globally uniform contraction of the non-Abelian flow. It **does not** invalidate vacuum-weighted smoothing since center backgrounds are Haar-null and null under each finite smooth quantum vacuum measure. A positive-measure vacuum-weighted flow regularity theorem, not an all-configurations Jacobian estimate, is still required.

**Verification:** deterministic integer incidence and numerical spectrum checks for n=2,3,4,5 passed 40 assertions. Least Hessian eigenvalues: -1.691769060, -1.662525115, -1.662319789, -1.662318189. Finite spectral regressions do not substitute for the min-max proof. Complete audited report, executable verifier, log and SHA-256 manifest in Library: /The Singular Boundary/Proof Audits/R3_SIGNED_CENTER_HESSIAN_FLOW_INSTABILITY_2026-11-06.zip. Original experiment files, main branch and Observatory gate statuses unchanged.
