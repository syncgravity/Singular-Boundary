# The Singular Boundary — Intrinsic Peter–Weyl radius-loss audit

**Date:** 2026-11-01
**Status:** Verified algebraic consequence of the previously reported intrinsic bilinear estimate. Not an interacting convergence theorem.

## Starting point
For touching face intervals whose union has t faces, the prior result bounds the centered nonlinear inverse by
[
\|K_T^{-1}P_0\Gamma(f,g)\|_{\mathcal H_{\sigma'}(T)}\le M_t(\delta)\|f\|_{\mathcal H_\sigma}\|g\|_{\mathcal H_\sigma},
\quad M_t(\delta)=16t\sqrt{(\mathcal D^2F_t)(z)(\mathcal D^2G_t)(z)},
]
where \(\delta=\sigma-\sigma'>0\), \(z=e^{-2\delta}\), \(\mathcal D=z\partial_z\), \(F_t=((1+z)/(1-z)^3)^t\), and \(G_t=(1-z)^{-t}\). This audit checks the **algebra of the constant**, not the original SU(2) proof.

## Exact factorization
Put
[
a(z)=\frac z{1+z}+\frac{3z}{1-z},\qquad b(z)=\frac z{(1+z)^2}+\frac{3z}{(1-z)^2},
\quad c(z)=\frac z{1-z},\quad d(z)=\frac z{(1-z)^2}.
]
Direct logarithmic differentiation yields
[
\mathcal D^2F_t=F_t(t^2a^2+tb),\qquad \mathcal D^2G_t=G_t(t^2c^2+td).
]
Consequently
[
\boxed{M_t(\delta)=16t\frac{(1+z)^{t/2}}{(1-z)^{2t}}\sqrt{(t^2a^2+tb)(t^2c^2+td)}.}
]

## Sharp asymptotic of the displayed bound
For fixed integer t≥1, with \(\epsilon=1-z\downarrow0\),
[
\mathcal D^2F_t\sim2^t(3t)(3t+1)\epsilon^{-3t-2},\qquad
\mathcal D^2G_t\sim t(t+1)\epsilon^{-t-2}.
]
Hence
[
\boxed{M_t(\delta)\sim16t\,2^{t/2}\sqrt{3t(3t+1)t(t+1)}(2\delta)^{-2t-2}.}
]
The displayed constant has losses \(\delta^{-4}\), \(\delta^{-6}\), \(\delta^{-8}\) for t=1,2,3 respectively. This describes the available upper bound, **not** a lower bound on the actual operator norm.

For fixed \(\delta>0\), the factor
[
\sqrt{F_tG_t}=\left(\frac{\sqrt{1+z}}{(1-z)^2}\right)^t
]
is exponential in t. Again this is a limitation of the estimate, not proof of exponential growth of the underlying operator.

## Implication for naive all-order iteration
If positive radius decrements \(\delta_j\) across infinitely many nonlinear steps obey \(\sum_j\delta_j\le\sigma_0<\infty\), then \(\delta_j\to0\). Paying \(M_{t_j}(\delta_j)\) at each step supplies no order-independent contraction. This does **not** exclude convergence via recurrence denominators, locality, cancellations, resummation or sharper norms, nor establish optimality of the prior Gevrey-8 bound.

## Next obligation
Obtain and analyze the actual connected-score recurrence, preserving the corrected adjacent-link identity \(\Gamma(a,b)=(ab-r_{AB})/4\). A support-sensitive bilinear estimate and coefficientwise connected interval majorant should avoid independently paying the whole union-support loss at every vertex. Explicit low-order coefficients need a separate sign audit.

## Verification
The source package `R3_IR_PW_RADIUS_LOSS_AUDIT_2026-11-01.zip` provides the complete earlier audit, SymPy executable, log and checksums. It verifies algebraic identities and leading coefficients for t=1,2,3,5.

## Research verdict
The exact interval-size and analytic-radius dependence of the existing intrinsic Peter–Weyl nonlinear-inverse majorant is established. Its constant diverges as \(\delta^{-2t-2}\) at fixed support size and grows exponentially with support size at fixed \(\delta>0\). Therefore the existing estimate, applied independently at each step, does not by itself close an all-orders analytic majorant. This is an obstruction in the present proof method, not a nonconvergence theorem. The corrected-sign score recurrence, all-orders hull decay, interacting \(\lambda=1\) gap, Penrose signed-current estimate, and continuum Yang–Mills mass gap remain open.
