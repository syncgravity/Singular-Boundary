# R3-IR — Local electric-metric defect bound by Wilson link-force incidences

Date: 2026-10-31. Finite-volume conditional theorem; not an interior mass-gap proof.

## Setting
On the full original-link Hilbert space let H=-Σ_e a_eΔ_e+V_- have normalized smooth positive ground state Ω with energy E0. Set A=diag(a_e I_3). Let T be a smooth product-Haar-preserving diffeomorphism preserving V_-; P_T f=f∘T. Its original-link electric differential is J_T(U), defined by ∇(f∘T)(U)=J_T(U)^T∇f(TU). Let \(M_T(V)=J_T(T^{-1}V) A J_T(T^{-1}V)^T-A\). The archived metric-form identity gives

\[ Q_T:=\langle P_T\Omega,(H-E_0)P_T\Omega\rangle
=\int \nabla\Omega(V)^T M_T(V)\nabla\Omega(V)\,d\mu(V)\ge0. \]

Define positive part of electric-normalized tensor \(N_T=A^{-1/2}M_T A^{-1/2}\) and \(d_T=\operatorname*{ess\,sup}_V\max(0,\lambda_{\max}(N_T(V)))\). (Finite for a smooth map on the compact link configuration manifold.) Then without any localization assumption,

\[0\le Q_T\le d_T\sum_e a_e\,S_{0,e},\quad S_{0,e}:=\sum_a\|X_{e,a}\Omega\|_2^2.\tag{1}\]

For the Wilson potential and any vertex v_e from which the link derivative forms an adjoint triplet, the previously proved local gauge-orbit coercivity and f-sum imply

\[ S_{0,e}\le\frac{3 B_{v_e}}{16}\,b_{\mathrm{inc}}(e),\qquad B_v=\sum_{k\ni v}a_k^{-1},\quad b_{\mathrm{inc}}(e)=\sum_{g\ne f:e\in\partial g}b_g.\]

Therefore the new finite-volume **gap-free magnetic-incidence defect estimate** is

\[\boxed{0\le Q_T\le \frac{3d_T}{16}\sum_e a_eB_{v_e}\,b_{\mathrm{inc}}(e).}\tag{2}\]

### Local-support improvement
If there is a subset S of links such that \(M_T(V)=P_S M_T(V)P_S\) for every configuration (electric metric defect has support *only* in those three-dimensional link directions), then replace both sums above by \(e\in S\):

\[\boxed{Q_T\le\frac{3d_T}{16}\sum_{e\in S}a_eB_{v_e}\,b_{\mathrm{inc}}(e).}\tag{3}\]

This support condition must be established for the chosen transport. **Fixing every link outside S is insufficient:** if transformed links depend on link variables outside S, the Jacobian may have off-block entries and the metric defect need not be supported in S. Tree–cotree transports may have such dependencies through tree parallel transport.

### Proof
The quadratic-form change under a Haar-preserving T follows by the chain rule; the magnetic term cancels since V_-∘T=V_-. At each V, spectral calculus for the symmetric matrix N_T gives z^T M_T z≤d_T z^T A z. Restrict to S only under the stated block-support hypothesis. Integrate with z=∇Ω. Use the exact local charged-sector link-score bound, already established from the Wilson f-sum and the local vertex Casimir inequality, to obtain (2) and (3). No physical full-link excitation gap is inserted.

### Consequences and open gates
For a family of disk transports T_g, integrating (3) in dg yields an upper bound on \(\int Q_g dg\) if the defect support and the integrated metric amplification \(\int d_g dg\) can be controlled. Combining with the previously archived transport-twirl theorem still requires a full-link gap \(\gamma\) for its total-variation inference; this theorem only removes the global **ground-state electric energy** from the defect estimate. A direct signed-current estimate is not obtained. At b_g∼h^-2 the local bound can itself grow like h^-2, and no uniform metric-amplification constant for completed Penrose cages is proved.

### Diagnostic
`verify.py` checks the sharp positive-eigenvalue quadratic inequality for 5,000 deterministic random weighted symmetric matrices with random coordinate support. Maximum relative positive floating-point violation: 2.65e-16. This tests algebra, not a Wilson vacuum, tree–cotree Jacobian or M55 electric response.

**Status:** exact finite-volume bound conditional on the archived link-score theorem; localized variant requires true metric-defect support. Regulator-uniform center current, covariance, continuum mass gap remain open.