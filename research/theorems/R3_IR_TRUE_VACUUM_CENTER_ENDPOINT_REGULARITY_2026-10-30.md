# Exact center-endpoint regularity of the true Wilson radial score

**2026-10-30 | R3-IR | classification:** exact *fixed finite volume* theorem for the actual strictly positive physical SU(2) Wilson ground state on any finite original-link rhombus disk, including a fully completed target magnetic cage. The endpoint regularity result is new in this record; it does **not** give a regulator-uniform constant or establish the physical mass gap.

## Setting

Let \(G=SU(2)^E\) with product normalized Haar measure, \(H=\sum_e a_e(-\Delta_e)+V\), \(a_e>0\), with a smooth real gauge-invariant Wilson magnetic potential \(V\). The unrestricted elliptic ground state \(\Omega>0\) is smooth, unique and Gauss-invariant. Take a simple target Wilson loop \(W_f\), \(p_f=\tfrac12\mathrm{Tr}W_f=\cos u\), and \(A_f=\sum_{e\in\partial f}a_e\). Under the true ground-state probability \(\nu=\Omega^2d\mu\), let \(\rho_f(p)\,dp\) denote the target-trace law and \(w(p)=2\sqrt{1-p^2}/\pi\) the Haar trace density. Set \(r_f(p)=\rho_f(p)/w(p)\), \(\psi_f(p)=\sqrt{r_f(p)}\). Define the signed conditional current \(J_f(p)=\mathbb E_\nu[\Gamma(p_f,\log\Omega)\mid p_f=p]\), with \(\Gamma(p_f)=A_f(1-p_f^2)/4\).

## Proposition (ER-1): smooth positive class amplitude through both endpoints

There exists a strictly positive \(C^\infty\) function \(r_f:[-1,1]\to(0,\infty)\) such that \(\rho_f(p)=r_f(p)w(p)\) on \((-1,1)\). In particular \(p\mapsto\psi_f(p)=\sqrt{r_f(p)}\) extends smoothly and positively to \(p=\pm1\).

**Proof.** Select one original boundary link \(e\) of the simple target loop and fix all other link variables \(Y\). The based target holonomy \(W_f\) is a smooth Haar-preserving translation/inversion of \(U_e\): \(W_f=L(Y)U_e^{\pm1}R(Y)\). Replacing \(U_e\) by \(W\) in the full ground-state integral yields a strictly positive smooth function
\[
F(W)=\int \Omega(U_e(W,Y),Y)^2\,d\mu_{\neg e}(Y)
\]
on the compact group SU(2). Smoothness follows from smoothness of \(\Omega\) and differentiation under the compact integral. Full original Gauss invariance and the ability to rotate the target basepoint by an original vertex gauge transformation imply \(F(gWg^{-1})=F(W)\) for all \(g\in SU(2)\). Every smooth SU(2) central function is a smooth function of the normalized trace \(p=\tfrac12\mathrm{Tr}W\) on the closed interval \([-1,1]\): in a geodesic chart at each center, smooth radial invariance forces a smooth function of the squared geodesic radius, and \(1-p\) (or \(1+p\) near the opposite center) is a smooth nondegenerate function of that squared radius. Thus \(F(W)=r_f(p(W))\) with strictly positive smooth \(r_f\) on \([-1,1]\). Pushing Haar from \(W\) to \(p\) proves the assertion. QED.

## Corollary (ER-2): exact endpoint current cancellation

The already proved conditional score identity \(\kappa(p)\,\partial_p\log\psi_f(p)=J_f(p)\), \(\kappa(p)=A_f(1-p^2)/4\), now gives
\[
\boxed{\quad J_f(p)=\frac{A_f}{4}(1-p^2)\,\partial_p\log\psi_f(p).\quad}\tag{ER-2}
\]
Hence \(J_f(p)=O(1-p^2)\) as \(p\to\pm1\), and for \(u\downarrow0\),
\[
\boxed{\quad \partial_u\log\psi_f(\cos u)
=-u\,(\partial_p\log\psi_f)(1)+O(u^3).\quad}\tag{ER-3}
\]
The same holds at the other center with \(\pi-u\). In particular the one-sided radial-score integrand is bounded and tends to zero at \(u=0\); there is **no actual endpoint divergence for a fixed finite-volume smooth Wilson vacuum**.

For any \(0<a<\pi/2\), let \(M_{f,a}=\sup_{\cos a\le p\le1}|\partial_p\log\psi_f(p)|<\infty\). Then
\[
\boxed{\quad
\int_0^a[\partial_u\log\psi_f(\cos u)]_+du
\le(1-\cos a)M_{f,a}
\le \frac{a^2}{2}M_{f,a}.\quad}\tag{ER-4}
\]
This is a genuine endpoint estimate but only with a finite-volume derivative constant.

## Reconciliation with the Harnack–Fisher estimate

The annular Cauchy–Schwarz factor \(\cot\alpha\) diverges as \(\alpha\downarrow0\). ER-3 shows this is a **limitation of the weighted Cauchy–Schwarz bound**, not a true singularity of the actual finite-volume score. Split the signed current budget at \(a\):
\[
\boxed{\quad
\mathfrak T_f
\le (1-\cos a)M_{f,a}
+ R\sqrt{\frac{I_f}{A_f}}
\left[\frac\pi2\big(\cot a-\cot(\pi/2)\big)\right]^{1/2}.
\quad}\tag{ER-5}
\]
Here \(R\) is the **pre-existing** local one-link heat Harnack constant and \(I_f\) is the earlier marginal Fisher energy. ER-5 is exact for any \(a>0\). Neither \(M_{f,a}\) nor \(R\) is currently controlled adequately and uniformly over complete Penrose interiors as \(h\downarrow0\). The smooth-amplitude capacity counterexample demonstrates why ER-4 cannot be made uniform using Fisher information alone: its finite endpoint derivative can grow as the cap shrinks.

## Next irreducible proof obligation

Derive directly from \(H_f^-\Omega_f^-=E_0\Omega_f^-\) a center-collar estimate on \(M_{f,a}\) (or a stronger one-sided integrated current estimate), with scale and geometry dependence that makes ER-5 \(o(h^{-1/4})\) uniformly on completed cages. Any attempt must control target-fiber dependence, nonlinear electric geometry, and low-energy connected dynamics without importing an unproved mass gap.

**Status:** Fixed-volume endpoint regularity and the split estimate are proved; a regulator-uniform completed-cage current estimate, connected covariance and continuum Yang–Mills mass gap remain open.
