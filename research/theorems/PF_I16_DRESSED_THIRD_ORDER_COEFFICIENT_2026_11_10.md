# PF-I16 — Centered dressed-resolvent expansion through third order

**Date:** 2026-11-10  
**Status:** exact finite-label perturbation identities; third-order coefficient bound is conditional on the uniform curvature, derivative and semigroup estimates stated below. No all-orders or continuum conclusion.

## 1. Dressed operator and perturbation

Let \(L_\Phi\) be the finite-graph nonnegative symmetric dressed diffusion from the PF-I16 single-face conjugation identity, acting in the probability measure \(d\nu_\Phi\). Let \(\Pi F=\nu_\Phi(F)\), and let
\[
G=L_\Phi^{-1}(1-\Pi)=\int_0^\infty P_t(1-\Pi)\,dt
\]
be the reduced resolvent on centered functions. For a finite set of distinct residual labels \(I\), perturb by \(V(\mathbf t)=\sum_{i\in I}t_iR_i\). Center \(r_i=R_i-\nu_\Phi(R_i)\); this removes only the linear energy terms and leaves every mixed coefficient unchanged.

The exact formal ground-state equations for \(H(t)=L_\Phi-\sum_it_ir_i\), with eigenfunction \(1+u(\mathbf t)\), \(\Pi u=0\), are
\[
E(\mathbf t)=-\Pi[V(\mathbf t)(1+u(\mathbf t))],\qquad
u=G[V(1+u)+Eu].
\]
For squarefree multi-indices \(I\), \(u_\emptyset=1\),
\[
E_I=-\sum_{i\in I}\nu_\Phi(r_i u_{I\setminus\{i\}}),
\]
\[
u_I=G\left[\sum_{i\in I}r_i u_{I\setminus\{i\}}
+\sum_{\varnothing\ne J\subsetneq I}E_Ju_{I\setminus J}\right].
\]
In particular, \(E_i=0\), \(u_i=Gr_i\), and
\[
E_{ij}=-2\nu_\Phi(r_iGr_j).
\]

## 2. Exact third-order mixed coefficient

For three distinct labels,
\[
u_{ij}=G(r_iGr_j+r_jGr_i),
\]
and the exact six-term formula is
\[
\boxed{
E_{ijk}=-\sum_{\sigma\in S_3}
\nu_\Phi\!\left[r_{\sigma(1)}
G\!\left(r_{\sigma(2)}Gr_{\sigma(3)}\right)\right].
}
\]
This identity is an algebraic consequence of the centered recursion; it is not a spatial tree estimate.

## 3. Revised conditional source-volume-uniform bound

Use the refined face blocks and derivative-flow estimate from [the pointwise Kato–Bochner record](PF_I16_POINTWISE_KATO_BOCHNER_DERIVATIVE_FLOW_2026_11_10.md). The working dressed Bakry–Émery curvature lower bound and weighted derivative-flow decay rate at \(\mu=\log25\) are
\[
\kappa=
\frac{a_0}{2}-\frac{2624}{3}b_0
-\frac{20480}{3}\frac{b_0^2}{a_0},
\qquad
\lambda=
\frac{a_0}{2}-\frac{53312}{3}b_0
-\frac{389120}{3}\frac{b_0^2}{a_0}.
\]
A sufficient smallness condition used below is \(b_0/a_0\le1/40000\), under which
\[
\kappa\ge0.478a_0,\qquad
\lambda\ge0.0556a_0.
\]

The residual estimates are
\[
\|r_i\|_\infty\le 2R_*=2080\,b_0^2/a_0,
\qquad
M_i:=\sum_{h\in S_i}\|D_hr_i\|_\infty
\le211250\,b_0^2/\sqrt{a_0},
\]
where \(S_i\) has at most 25 links. The conditional resolvent estimates are
\[
\|Gr_i\|_\infty\le\frac{50\pi}{\sqrt{a_0}\lambda}M_i,
\qquad
\|G\|_{L^2_0\to L^2_0}\le\kappa^{-1}.
\]
Applying these to each of the six terms in the exact third-order identity gives
\[
|E_{ijk}|
\le
\frac{274185600000000\pi\,b_0^6}
{a_0^3\kappa\lambda}
=
\frac{8.613795\times10^{14}b_0^6}
{a_0^3\kappa\lambda}.
\]
Consequently, under \(b_0/a_0\le1/40000\),
\[
\boxed{|E_{ijk}|\le3.25\times10^{16}\frac{b_0^6}{a_0^5}.}
\]
This is a conditional finite-source-volume-uniform bound under the listed curvature, derivative-flow, residual and resolvent estimates. It has **no exponential spatial spanning-tree factor** and does not establish decay with the separation of \(S_i,S_j,S_k\).

The former \(1.527\times10^{16}\) prefactor, \(\kappa=a_0/2-2976b_0\), \(\lambda=a_0/2-46752b_0\), and \(b_0/a_0<1/93504\) threshold are historical estimates and are superseded for this working route.

## 4. Fourth-order algebra versus spatial connectedness

The next exact recursion is
\[
u_{ijk}=G\left[
r_i u_{jk}+r_j u_{ik}+r_k u_{ij}
+E_{ij}u_k+E_{ik}u_j+E_{jk}u_i
\right],
\]
and
\[
E_{ijkl}=-\sum_{m\in\{i,j,k,l\}}
\nu_\Phi(r_m u_{\{i,j,k,l\}\setminus\{m\}}).
\]
The locally recovered source transcript `Branch · Branch · Continue PF116 Objective (1).md` has 82,975 bytes and SHA-256 `fd99b9b9ee8e1ce0b33caa6a34ae310c34f9b7a9f184d32d886a0855a611fa6f`. It reports an expansion into 36 terms in three pair-partition channels, exact cancellation for genuinely independent subsystem decompositions (including the \\(2+2\\) split), and a cut-interpolation identity for measuring failure of factorization when subsystems are coupled. Its full original bytes remain pending repository import; these transcript-reported details are not independently audited by this record.

The companion local source transcript `Branch · Branch · Continue PF116 Objective (3).md` has 76,242 bytes and SHA-256 `4caba95b1f594ff5fc6eba4c5aa33baf5ff843d0bddcc80915649f8597ae56a4`. Its pointwise Kato–Bochner and four-factor holonomy derivative discussion overlaps the existing PF-I16 derivative-flow records; the standalone sign/trivialization audit remains open. It also discusses the R3-IR interacting Hessian estimate, including the Riccati term, source-locality issue, interacting-resolvent circularity, and a fixed-reference-resolvent route requiring uniform constants. This is source-reported research context, not a completed Hessian estimate. Full original bytes remain pending repository import.

This algebraic cancellation does not establish spatial connectedness on the connected Penrose graph. The cut-interpolation identity is an exact algebraic diagnostic reported by the transcript for coupled subsystems, not a spatial tree theorem. The fourth-order spatial connected-support/tree estimate therefore remains open. Even that estimate would still need to be joined to all-orders convergence, physical normalization, and a continuum gap argument.

## 5. Proof ledger

**Exact:** finite-label centered perturbation recursion and third-order six-permutation identity.

**Conditional/working estimates:** refined rotor Hessian and four-factor mixed-holonomy blocks; pointwise componentwise Kato–Bochner comparison; weighted Duhamel derivative flow; dressed curvature/Poincaré; residual derivative and sup-resolvent estimates; revised third-order numerical bound.

**Open:** standalone sign/trivialization/regularization audit of the four-factor calculation; spatially decaying third-order tree bound; fourth-order spatial connected-support/tree estimate for coupled Penrose subsystems; all-orders connected activity majorant; source physical kinetic/time; nontrivial interacting continuum existence and positive physical mass gap. The fourth-order algebraic cancellation for independent decompositions is transcript-reported, with the original transcript's size and SHA-256 recorded above; full-byte repository import and independent audit remain pending.

The previous third-order numerical prefactor and thresholds are superseded, not silently retained. No spatial tree decay or all-orders conclusion is claimed.
