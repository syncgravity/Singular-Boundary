# Support-sensitive intrinsic Peter–Weyl nonlinear-inverse estimate
**The Singular Boundary | 2026-11-01 | Finite open straight SU(2) chains**

Let input intervals I,J have r,s faces and contiguous union T. Let m be the number of original links on which both input functions can have nonzero derivatives. For 0 <= sigma' < sigma, delta=sigma-sigma', z=exp(-2delta), D=z d/dz, F_q=((1+z)/(1-z)^3)^q, G_q=(1-z)^(-q), the following holds for finite PW sums (and by density):
[
\|\Gamma(f,g)\|_{H_{\sigma'}(T)}
\le 12m\min\{\sqrt{(D^2F_r)(D^2G_s)},\sqrt{(D^2G_r)(D^2F_s)}\}\|f\|_{H_\sigma(I)}\|g\|_{H_\sigma(J)}.
]
After the previously proved Haar-centered free inverse \(\|K_T^{-1}P_0\|\le1/3\), the prefactor is 4m. If m=0, Gamma vanishes exactly.

**Proof.** Gamma sums only common original-link gradient products, three SU(2) directions for each such link. On a degree-l block, the derivative L2 operator norm is <=2N(l), and its supremum norm is <=2N(l)d_l||f_l||_2, d_l=product_i(l_i+1). Clebsch–Gordan bounds output degree by N(l)+N(k). Thus a single directional product costs <=4N(l)N(k)d_l exp[sigma'(N(l)+N(k))]||f_l||_2||g_k||_2. Cauchy–Schwarz on degrees of f *only on I*, and g *only on J*, gives sqrt[(D²F_r)(D²G_s)]; swapping the L-infinity factor yields the other orientation. Sum 3m terms. The inverse factor 1/3 gives the claim. The estimate is insensitive to sign but does not certify previously computed score coefficients.

At fixed r,s, the oriented square root behaves as
[
2^{r/2}\sqrt{3r(3r+1)s(s+1)}(2\delta)^{-(3r+s)/2-2}.
]
Minimizing over orientations yields exponent \((r+s)/2+\min(r,s)+2\). Thus the estimate improves sparse and unbalanced support interactions, but not fully overlapping equal-size interactions, where the radius exponent remains 2t+2. In particular no all-orders majorant follows.

**Research verdict:** A support-sensitive local intrinsic PW inverse estimate holds, replacing a union-size prefactor with common-link count and separating input-support degree sums. Its gain does not close analytic convergence, all-order hull decay, interacting lambda=1 gap, Penrose signed-current estimate, or continuum Yang–Mills gap. The corrected-sign connected-score recurrence is the next obligation.

**Reproducibility:** Complete long-form audit, executable SymPy checker, run log and SHA-256 manifest are in `R3_IR_PW_SUPPORT_SENSITIVE_2026-11-01.zip` (Library Proof Audits).
