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

## 3. Conditional source-volume-uniform bound

Assume \(a_e\ge a_0>0\), \(0\le b_f\le b_0\), \(b_0/a_0<1/93504\), and the working uniform estimates
\[
\kappa=\frac{a_0}{2}-2976b_0>0,\qquad
\lambda=\frac{a_0}{2}-46752b_0>0,
\]
where \(\kappa\) is a Poincaré lower bound for the dressed diffusion and \(\lambda\) is the weighted derivative-semigroup decay rate at \(\mu=\log25\). The derivative estimates used are
\[
\|R_i-\nu_\Phi(R_i)\|_\infty\le2R_*,
\quad R_*=1040\,b_0^2/a_0,
\]
\[
M_i:=\sum_{h\in S_i}\|D_hr_i\|_\infty
\le1{,}872{,}000\,b_0^2/\sqrt{a_0}.
\]
Here \(S_i\) is the at-most-25-link support and \(D_h=\sqrt{a_h}\nabla_h\).

The resolvent estimates used are
\[
\sum_h\|D_hGr_i\|_\infty\le\frac{25}{\lambda}M_i,
\qquad
\|Gr_i\|_\infty\le\frac{50\pi}{\sqrt{a_0}\lambda}M_i,
\qquad
\|G\|_{L^2_0\to L^2_0}\le\kappa^{-1}.
\]
They imply, term by term in the six-term formula,
\[
|E_{ijk}|\le
\frac{50\pi}{\kappa\sqrt{a_0}\lambda}
\sum_{\sigma\in S_3}
\|r_{\sigma(1)}\|_\infty
\|r_{\sigma(2)}\|_\infty M_{\sigma(3)}
\le
\boxed{\frac{1.527\times10^{16}b_0^6}
{a_0^3\kappa\lambda}}.
\]

This is uniform in the finite source volume under the listed estimates. It has **no exponential spatial spanning-tree factor** and does not yet show decay with the separation of \(S_i,S_j,S_k\). The derivative-flow/curvature estimates and constants are a working analytic chain and require standalone independent verification before being treated as a certified repository theorem.

## 4. Fourth order and all orders remain open

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
Expanding this formula and proving cancellation of disconnected partition terms is the next task. It must not be assumed from the third-order formula. Even a fourth-order cancellation theorem would still need a uniform connected-tree bound, all-orders convergence, physical normalization, and a continuum gap argument.

## 5. Proof ledger

**Exact:** finite-label centered perturbation recursion and third-order six-permutation identity.

**Conditional/working estimates:** \(\kappa\), \(\lambda\), residual derivative constants and the displayed numerical third-order bound.

**Open:** spatially decaying third-order tree bound; fourth-order partition cancellation; all-orders connected activity majorant; source physical kinetic/time; nontrivial interacting continuum existence and positive physical mass gap.
