# PF-I16 — Exact single-face dressing and shared-link residual reduction

**Original date:** 2026-11-10  
**Correction:** 2026-11-12, incorporating the corrected isolated-rotor estimate.  
**Status:** exact finite-graph operator identity. The corrected residual magnitude and derivative estimates are conditional on the stated radial and pullback estimates; all-orders summability and an interacting gap remain open.

## 1. Setup

On the authentic accepted-rhombus complex let (E) be original links and (F) accepted faces. Consider the auxiliary Hamiltonian
[
H=K-sum_{fin F}b_fp_f,qquad
K=sum_{ein E}a_eC_e,
]
where (p_f=\tfrac12\operatorname{Tr}U_f), (a_e>0), and (d_e=\#\{f:e\in\partial f\}). Allocate
[
\alpha_{fe}=a_e/d_e,\quad
K_f=\sum_{e\in\partial f}\alpha_{fe}C_e,\quad
A_f=\sum_{e\in\partial f}a_e/d_e.
]
Then (K=\sum_fK_f+K_0) exactly, where (K_0) contains uncovered links. Restricted to functions of the face holonomy, (K_f=A_f(-\Delta_{SU(2)})).

Let (\psi_f(U_f)>0) be the isolated-face ground state of (K_f-b_fp_f), with energy (E_f), and set (s_f=\log\psi_f), (\Phi=\sum_fs_f). The one-face ground-state equation is
[
K_fs_f-\Gamma_{K_f}(s_f,s_f)-b_fp_f=E_f.
]

## 2. Exact residual identity

With (\Gamma_K(g,h)=\sum_ea_e\nabla_eg\cdot\nabla_eh), define
[
v_{fe}=\nabla_es_f,\qquad
R_e=a_e\left|\sum_{f:e\in\partial f}v_{fe}\right|^2
-\frac{a_e}{d_e}\sum_{f:e\in\partial f}|v_{fe}|^2,
]
and (R_e=0) when (d_e=0). Summing the isolated-face equations gives
[
K\Phi-\Gamma_K(\Phi,\Phi)-\sum_fb_fp_f
=\sum_fE_f-\sum_eR_e.
]
Consequently the exact ground-state conjugation identity is
[
\boxed{e^{-\Phi}He^{\Phi}=L_\Phi+\sum_fE_f-\sum_eR_e,\qquad
L_\Phi=K-2\Gamma_K(\Phi,\cdot).}
]
The conjugation is unitary from (L^2(e^{2\Phi}d\mu)) to (L^2(d\mu)); (L_\Phi) is nonnegative, symmetric in the dressed measure, and annihilates constants.

**Structural consequence:** if (d_e=1), then (R_e=0). Repeated insertions confined to one face are absorbed into its exact isolated-face dressing. The residual is supported only at shared links.

## 3. Corrected locality and residual magnitude

The elementary five-direction inventory gives (d_e\le8). Thus (R_e) depends on at most (1+3d_e\le25) original links. The radial equation for the isolated face gives the corrected bound
[
\|\nabla s_f\|_\infty\le2\beta_f,qquad
\beta_f=|b_f|/A_f,
]
not the previously used (\beta_f). Since (a_e\le8A_f) and (A_f\ge a_0/2), the resulting conservative estimate is
[
\boxed{\|R_e\|_\infty\le4160\frac{b_0^2}{a_0}}
]
for (a_e\ge a_0>0), (0\le b_f\le b_0). This uses the universal incidence (d_e\le8), not the sharper incidence observed on eight finite crops.

For a centered residual label (r_e=R_e-\nu_\Phi(R_e)),
[
\boxed{\|r_e\|_\infty\le8320\frac{b_0^2}{a_0}.}
]
The earlier (1040b_0^2/a_0) bound relied on the false (\|\nabla s_f\|_\infty\le\beta_f) input and is withdrawn.

## 4. Corrected residual derivative bounds

The corrected radial Hessian and the independently audited four-factor mixed covariant derivative yield provisional pulled-back face blocks
[
h_d\le\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0},\qquad
h_o\le\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}.
]
At (b_0/a_0\le1/50000), the corrected derivative calculation in [the rotor repair audit](../audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md) gives, for each residual,
[
\|D_hR_e\|\le21514\frac{b_0^2}{\sqrt{a_0}},
]
and because its support contains at most 25 links,
[
\boxed{
\left(\sum_h\|D_hR_e\|^2\right)^{1/2}
\le107570\frac{b_0^2}{\sqrt{a_0}},\qquad
\sum_h\|D_hR_e\|
\le537850\frac{b_0^2}{\sqrt{a_0}}.
}
]
These are conditional finite-graph derivative bounds, not a connected-cumulant or all-orders activity estimate.

The corrected curvature and weighted derivative-flow comparisons have the provisional lower bounds
[
\kappa_{\rm BE}\ge\frac{a_0}{2}
-\frac{3200}{3}b_0-\frac{81920}{3}\frac{b_0^2}{a_0},
]
[
\lambda_{\log25}\ge\frac{a_0}{2}
-\frac{67712}{3}b_0-\frac{1556480}{3}\frac{b_0^2}{a_0}.
]
For (b_0/a_0\le1/50000), the corresponding margins exceed (0.4786a_0) and (0.0483a_0), respectively. They remain conditional on the finite-product Bochner/Kato comparison, face-map metric calculations, and local incidence assumptions. See the [pointwise Kato–Bochner record](PF_I16_POINTWISE_KATO_BOCHNER_DERIVATIVE_FLOW_2026_11_10.md) and its 2026-11-11 correction.

## 5. What this does not prove

The exact dressing/conjugation identity is a finite-graph operator identity. The corrected local residual estimates do not by themselves prove a volume-uniform Poincaré estimate for (L_\Phi), stability under the extensive sum (\sum_eR_e), a convergent all-orders cluster expansion, source-derived physical time, a continuum limit, or a mass gap. The remaining hard step is a source-volume-uniform bound on connected residual activities that controls repeated shared-link fusion and the full SU(2) Peter–Weyl tower. The exact finite-label third-order expansion and its corrected conditional bound are recorded in [the third-order dossier](PF_I16_DRESSED_THIRD_ORDER_COEFFICIENT_2026_11_10.md).
