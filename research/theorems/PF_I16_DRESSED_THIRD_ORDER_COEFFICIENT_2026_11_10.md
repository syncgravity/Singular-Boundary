# PF-I16 — Centered dressed-resolvent expansion through third order

**Original date:** 2026-11-10  
**Correction:** 2026-11-12, using the independently audited four-factor derivative and corrected isolated-rotor estimate.  
**Status:** exact finite-label perturbation identities; corrected third-order coefficient bound is **conditional** on the corrected finite-graph curvature, derivative-flow, and resolvent estimates below. It is not a spatial tree estimate and gives no all-orders or continuum conclusion.

## 1. Dressed operator and perturbation

Let `L_Φ` be the finite-graph nonnegative dressed diffusion from the PF-I16 single-face conjugation identity, acting in the probability measure `dν_Φ`. Let `ΠF=ν_Φ(F)`, and let
[
G=L_Φ^{-1}(1-Π)=\int_0^\infty P_t(1-Π)\,dt
]
be the reduced resolvent on centered functions. For a finite set of distinct residual labels `I`, perturb by `V(\mathbf t)=\sum_{i\in I}t_iR_i`. Center `r_i=R_i-ν_Φ(R_i)`; this removes only the linear energy terms and leaves every mixed coefficient unchanged.

The exact formal ground-state equations for `H(t)=L_Φ-\sum_it_ir_i`, with eigenfunction `1+u(\mathbf t)`, `Πu=0`, are
[
E(\mathbf t)=-Π[V(\mathbf t)(1+u(\mathbf t))],\qquad
u=G[V(1+u)+Eu].
]
For squarefree multi-indices `I`, `u_\emptyset=1`,
[
E_I=-\sum_{i\in I}ν_Φ(r_i u_{I\setminus\{i\}}),
]
[
u_I=G\left[\sum_{i\in I}r_i u_{I\setminus\{i\}}
+\sum_{\varnothing\ne J\subsetneq I}E_Ju_{I\setminus J}\right].
]
In particular, `E_i=0`, `u_i=Gr_i`, and
[
E_{ij}=-2ν_Φ(r_iGr_j).
]

## 2. Exact third-order mixed coefficient

For three distinct labels,
[
u_{ij}=G(r_iGr_j+r_jGr_i),
]
and the exact six-term formula is
[
\boxed{
E_{ijk}=-\sum_{\sigma\in S_3}
ν_Φ\!\left[r_{\sigma(1)}
G\!\left(r_{\sigma(2)}Gr_{\sigma(3)}\right)\right].
}
]
This identity is an algebraic consequence of the centered recursion; it is not a spatial tree estimate.

## 3. Corrected conditional finite-graph bound

The earlier numerical estimate in this section is withdrawn. It used the false isolated-rotor input \(\|s'_\beta\|_\infty\le\beta\). The exact linear response of the recorded radial equation is
\[
s'_\beta(\theta)=-\frac43\beta\sin\theta+o(\beta),
\]
so the unit coefficient is impossible. The corrected maximum-principle estimate and radial Hessian bound are
\[
\|s'_\beta\|_\infty\le2\beta,\qquad
\|\nabla^2s_\beta\|_{\rm op}
\le\frac43\beta+\frac{80}{3}\beta^2.
\]
The four-factor mixed covariant derivative signs have since been independently audited for all 16 orientation words and all 12 ordered distinct-factor pairs (3,840 deterministic quaternion finite-difference comparisons). See [the rotor obstruction and repair](../audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md) and [the four-factor sign audit](../audits/PF_I16_FOUR_FACTOR_MIXED_COVARIANT_DERIVATIVE_AUDIT_2026_11_11.md).

Under the universal source incidence assumptions (d_e\le8), (a_e\ge a_0>0), (0\le b_f\le b_0), the corrected provisional face blocks are
\[
h_d\le\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0},\qquad
h_o\le\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}.
\]
The resulting finite-product Bochner/Kato comparison gives the provisional lower bounds
\[
\kappa\ge
\frac{a_0}{2}-\frac{3200}{3}b_0
-\frac{81920}{3}\frac{b_0^2}{a_0},
\]
\[
\lambda\ge
\frac{a_0}{2}-\frac{67712}{3}b_0
-\frac{1556480}{3}\frac{b_0^2}{a_0}.
\]
Here \(\kappa\) is the dressed-reference curvature/Poincaré lower bound and \(\lambda\) the \(\mu=\log25\) weighted derivative-flow decay rate. These remain conditional on the product-Hessian pullback, finite-product Bochner/Kato comparison, and the stated local incidence/metric conventions; the corrected arithmetic alone does not certify those analytic implications.

The corrected shared-link residual estimates at (b_0/a_0\le1/50000) are
\[
\|R_e\|_\infty\le4160\frac{b_0^2}{a_0},\qquad
\|r_i\|_\infty\le2\|R_e\|_\infty
\le8320\frac{b_0^2}{a_0},
\]
and, for a residual label supported on at most 25 links,
\[
M_i:=\sum_{h\in S_i}\|D_hr_i\|_\infty
\le537850\frac{b_0^2}{\sqrt{a_0}}.
\]
The corrected rotor audit gives \(\kappa/a_0>0.4786\) and \(\lambda/a_0>0.0483\) at (b_0/a_0\le1/50000).

Use the conditional resolvent estimates
\[
\|Gr_i\|_\infty\le
\frac{50\pi}{\sqrt{a_0}\lambda}M_i,
\qquad
\|G\|_{L^2_0\to L^2_0}\le\kappa^{-1}.
\]
Each of the six terms in the exact third-order identity is then bounded by
\[
\|r_i\|_\infty\,\kappa^{-1}\,
\|r_j\|_\infty\,\|Gr_k\|_\infty.
\]
Consequently,
\[
\boxed{
|E_{ijk}|
\le
\frac{11169380352000000\,\pi\,b_0^6}
{a_0^3\kappa\lambda}.
}
\]
At (b_0/a_0\le1/50000), using the exact rational lower margins
\[
\frac{\kappa}{a_0}\ge0.478655744,\qquad
\frac{\lambda}{a_0}\ge0.048379136,
\]
and the rigorous elementary bound \(\pi<22/7\), this gives
\[
\boxed{
|E_{ijk}|\le
1.516\times10^{18}\frac{b_0^6}{a_0^5}.
}
\]
The displayed coefficient is rounded upward from the rational upper bound
\[
\frac{288422062500000000000000000000}{190263788491}
<1.516\times10^{18}.
\]

This is a corrected **conditional fixed-triple amplitude bound**, uniform in finite source volume under the stated local hypotheses. It has no exponential factor in the separation of (S_i,S_j,S_k), so it does **not** establish spatial decay or a connected-tree estimate. The analytic estimates on which it rests remain conditional; the bound is not an independently certified theorem about the physical Hamiltonian.

## 4. Fourth-order algebra versus spatial connectedness

The next exact recursion is
[
u_{ijk}=G\left[
r_i u_{jk}+r_j u_{ik}+r_k u_{ij}
+E_{ij}u_k+E_{ik}u_j+E_{jk}u_i
\right],
]
and
[
E_{ijkl}=-\sum_{m\in\{i,j,k,l\}}
ν_Φ(r_m u_{\{i,j,k,l\}\setminus\{m\}}).
]
The preserved source `sources/originals/session-2026-11-11/Branch · Branch · Continue PF116 Objective (1).md` (82,975 bytes; SHA-256 `fd99b9b9ee8e1ce0b33caa6a34ae310c34f9b7a9f184d32d886a0855a611fa6f`) reports an expansion into 36 terms in three pair-partition channels, with exact cancellation for genuinely independent subsystem decompositions, including the (2+2) split. It also reports a cut-interpolation identity for measuring the failure of factorization when subsystems are coupled. These transcript claims remain subject to independent mathematical audit; preserving the source bytes does not itself verify the derivation.

The companion preserved source `sources/originals/session-2026-11-11/Branch · Branch · Continue PF116 Objective (3).md` (76,242 bytes; SHA-256 `4caba95b1f594ff5fc6eba4c5aa33baf5ff843d0bddcc80915649f8597ae56a4`) contains pointwise Kato–Bochner and four-factor holonomy derivative discussion overlapping existing PF-I16 derivative-flow records; the standalone sign/trivialization audit has since been completed as described above. It also discusses the R3-IR interacting Hessian estimate, including the Riccati term, source-locality issue, interacting-resolvent circularity, and a fixed-reference-resolvent route requiring uniform constants. This is source-reported research context, not a completed Hessian estimate.

The algebraic cancellation for independent subsystem decompositions does not establish spatial connectedness on the connected Penrose graph. The cut-interpolation identity is an exact algebraic diagnostic reported by the transcript for coupled subsystems, not a spatial tree theorem. The fourth-order spatial connected-support/tree estimate therefore remains open. Even that estimate would still need to be joined to all-orders convergence, physical normalization, and a continuum gap argument.

## 5. Proof ledger

**Exact:** finite-label centered perturbation recursion and third-order six-permutation identity; corrected radial first-derivative bound and Hessian estimate; four-factor mixed covariant derivative signs.

**Conditional:** corrected finite-graph face-block, curvature, derivative-flow, residual-derivative, resolvent, and fixed-triple third-order amplitude estimates.

**Open:** spatially decaying third-order tree bound; fourth-order spatial connected-support/tree estimate for coupled Penrose subsystems; all-orders connected activity majorant; source physical kinetic/time; source-authenticated refining physical 3D regulator; nontrivial interacting continuum existence and positive physical mass gap.

The previous (3.25\times10^{16}) third-order prefactor, (1/40000) threshold, and all constants depending on \(\|s'_f\|_\infty\le\beta_f\) are superseded. No spatial tree decay or all-orders conclusion is claimed.


## 6. 2026-11-13 spatial continuation

The corrected two-point resolvent theorem has now been applied to the nested third-order term. The result is a uniform three-kernel convolution and a six-permutation **pair-arm** bound, not a connected tree estimate. The exact remaining obstruction is the undifferentiated factor \( (Gr_k)D r_j \) in the product rule; the global oscillation bound controls its amplitude but supplies no decay from \(S_j\) to \(S_k\). See [PF-I16 three-support pair-arm estimate and tree obstruction](PF_I16_THREE_SUPPORT_PAIR_ARM_AND_TREE_OBSTRUCTION_2026_11_13.md) and its [exact convolution verifier](../verification/verify_pf_i16_three_support_convolution.py).

The report specifies the missing PF-I16 conditional-amplitude/\(L^4\) estimate, conditional-centering control, and history-aware six-permutation cancellation. Earlier straight-strip R3 estimates are not silently imported as PF-I16 theorems. Spatial tree decay remains **OPEN**.
