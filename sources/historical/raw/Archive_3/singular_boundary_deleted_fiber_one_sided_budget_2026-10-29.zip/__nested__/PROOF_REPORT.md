# The Singular Boundary — One-sided exact fiber-potential budget and polynomial deleted-face center mass

**Research date:** 2026-10-29. **Classification:** an exact quantum one-dimensional inequality for the true finite gauge-invariant deleted SU(2) ground state; a conditional criterion for polynomial center-ball mass and all-bulk deletion. No assumption of a transverse fast-mode gap, Gaussian vacuum, physical gap, or monotone fiber energy. The crucial one-sided fiber-potential budget is not yet bounded for the genuine refining Penrose sequence.

## 1. Exact input and notation

Let \(H_f^-=\sum_e a_e(-\Delta_e)+\sum_{g\ne f}b_g(1-p_g)\) on the Gauss-invariant Hilbert space of a finite simply connected rhombus disk. Assume \(A_f=\sum_{e\in\partial f}a_e>0\). Denote its unique normalized positive ground state by \(\Omega_f^-\), energy \(E_f^-\), and the deleted-face trace \(p_f=\frac12\operatorname{ReTr}W_f\). The exact conditional-fiber decomposition, including all slow modes and mixed electric terms, proves that \(\psi_f(u)=\sqrt{F_f(\cos u)}>0\), where \(F_f\) is the vacuum-to-Haar marginal density, is symmetric about \(u=\pi/2\), has \(\int_0^\pi(2/\pi)\sin^2u\,\psi_f(u)^2du=1\), and obeys

\[
-k_f[\psi_f''(u)+2\cot u\,\psi_f'(u)]+\mathcal U_f(\cos u)\psi_f(u)=E_f^-\psi_f(u),\quad k_f=A_f/4.
\tag{1}
\]

Here \(\mathcal U_f\) is the **exact conditional environmental energy** defined in the preceding fiber theorem; it is a function of the actual unknown nonlinear vacuum, not a prescribed Gaussian potential. Smooth positive finite-volume regularity gives \(\psi_f'(0)=0\) and the other natural endpoint conditions. Introduce \(V_f(u)=\mathcal U_f(\cos u)-E_f^-\).

## 2. Theorem OB-1 — One-sided radial log-growth estimate, no sign hypothesis

Define the positive effective equator-attraction budget

\[
\boxed{\mathfrak B_f=\frac4{A_f}\int_0^{\pi/2}\sin u\cos u\,[V_f(u)]_+\,du\in[0,\infty).}\tag{2}
\]

For **every** pair \(0\le v\le u\le\pi/2\), the exact deleted-vacuum marginal obeys

\[
\boxed{\psi_f(u)\le e^{\mathfrak B_f}\psi_f(v).}\tag{3}
\]

**Proof.** Put \(r(u)=\psi_f'(u)/\psi_f(u)\). Divide (1) by \(\psi_f\) to obtain the precise Riccati identity

\[
r'+2\cot u\,r+r^2=V_f(u)/k_f.
\]

Multiplication by \(\sin^2u\), integration from zero, and nonnegativity of \(r^2\) yield

\[
\sin^2u\,r(u)
\le\frac1{k_f}\int_0^u\sin^2t\,[V_f(t)]_+dt.
\]

Integrate from \(v\) to \(u\), upper-bound the positive integrand by its whole \([0,\pi/2]\) integral, and change order using

\[
\int_t^{\pi/2}\csc^2s\,ds=\cot t.
\]

This gives \(\log\psi_f(u)-\log\psi_f(v)\le k_f^{-1}\int_0^{\pi/2}\sin t\cos t[V_f(t)]_+dt=\mathfrak B_f\). The discarded \(-r^2\) term makes this upper bound potentially conservative; no effective-fiber monotonicity, Gaussian approximation or physical gap was required. □

## 3. Theorem OB-2 — Sharp Haar-order cap mass with controlled multiplicative loss

For \(0<\alpha\le\pi/2\), define the exact Haar one-center cap mass

\[
m_H(\alpha)=\int_0^\alpha \frac2\pi\sin^2u\,du=\frac{\alpha-\frac12\sin(2\alpha)}\pi.
\]

Then the actual deleted-vacuum probability of the *same* center ball satisfies

\[
\boxed{m_f^-(\alpha)=\mathbb P_{\Omega_f^-}(0\le u\le\alpha)
\ge e^{-2\mathfrak B_f}m_H(\alpha).}\tag{4}
\]

**Proof.** Let \(A=\int_0^\alpha\omega_0\psi_f^2\), \(D=\int_\alpha^{\pi/2}\omega_0\psi_f^2\), \(a=\int_0^\alpha\omega_0=m_H\), \(d=1/2-a\), where \(\omega_0=2\sin^2u/\pi\). The parity of the actual deleted vacuum yields \(A+D=1/2\). By (3), \(\psi_f(u)^2\le e^{2\mathfrak B_f}\psi_f(v)^2\) for \(v\in[0,\alpha], u\in[\alpha,\pi/2]\). Multiplying by Haar weights and integrating gives \(aD\le e^{2\mathfrak B_f}dA\). Therefore

\[
A\ge\frac{a/2}{a+e^{2\mathfrak B_f}(1/2-a)}\ge ae^{-2\mathfrak B_f}.
\]

No estimate on the negative part of \(V_f\) is necessary. The last inequality becomes equality for the exact Haar deleted marginal \(\psi_f\equiv1\), \(\mathfrak B_f=0\). □

The same proof applies to the \(-I\) center ball by parity.

For the Wilson deficit cap \(d_f=1-p_f\le\delta\), set \(\alpha_\delta=\arccos(1-\delta)\). The exact Haar mass is

\[
m_H(\delta)=\frac{\arccos(1-\delta)-(1-\delta)\sqrt{2\delta-\delta^2}}\pi
=\frac{4\sqrt2}{3\pi}\delta^{3/2}(1+O(\delta)).
\tag{5}
\]

Consequently if \(\mathfrak B_{f,h}\le L\log(1/h)+C\) for all selected faces, then \(m_{f,h}^-(d_f\le h)\ge c h^{3/2+2L}\), **uniformly in face count and with no monotonicity/single-crossing assumption**. The bound on \(\mathfrak B\) is an additional hypothesis, not a result for the actual refining nonlinear ground states.

## 4. Theorem OB-3 — The weaker subcritical potential budget already suffices for fixed-support angle equivalence

The previously proved universal deleted-face variational bound states, with \(b_f>0\), \(\kappa_f=\sqrt{2b_f/A_f}\), \(\kappa_f\ge1\), and \(m_f=\mathbb P_{\Omega_f^-}(d_f\le1/\kappa_f)\),

\[
\Delta_f:=E_0(H)-E_0(H_f^-)
\le\frac{b_f}{\kappa_f}\left[2+\log\frac{2e^2\kappa_f}{m_f}\right].
\]

Substituting (4) at \(\delta=1/\kappa_f\) yields the **exact new conditional deletion-energy inequality**

\[
\boxed{\Delta_f\le\sqrt{\frac{A_fb_f}2}\left[2+\log\frac{2e^2\kappa_f}{m_H(1/\kappa_f)}+2\mathfrak B_f\right].}\tag{6}
\]

Assume the explicit Penrose coefficient bounds \(0<A_-\le A_f\le A_+\), \(\beta_-h^{-2}\le b_f\le\beta_+h^{-2}\). Then (5)–(6) give, uniformly over interior faces,

\[
\boxed{\Delta_f\le C h^{-1}[1+\log(1/h)+\mathfrak B_{f,h}].}\tag{7}
\]

For **full fixed-support defect exclusion**, a weaker hypothesis than a polynomial flat-ball lower bound suffices:

\[
\boxed{\sup_{f\in D_R}\mathfrak B_{f,h}=o(h^{-1/4}).}\tag{8}
\]

Indeed (7) then gives \(\sup_f\Delta_f=o(h^{-5/4})\), while the exact single-face ground-state Laplace bound, at \(s=\zeta\sqrt{8b_f/A_f}\) for any fixed \(0<\zeta<1\), yields

\[
\log\mathbb P_{\Omega_h}(d_f\ge h^{3/4})
\le-\zeta h^{3/4}\sqrt{8b_f/A_f}
+\frac{\Delta_f}{\sqrt{A_fb_f/8}}\operatorname{artanh}\zeta
\le-c h^{-1/4}+o(h^{-1/4}).
\]

A union bound over at most \(C_Rh^{-2}\) selected faces gives \(P_h:=\mathbb P_{\Omega_h}(\max_{f\in D_R}d_f\ge h^{3/4})\le C_Rh^{-2}e^{-c h^{-1/4}}\). The previously proved fixed-support rare-event theorem then yields \(\operatorname{Var}_{\Omega_h}(\sqrt h\sum_{f\in D_R}q_f(Q_f-d_f))\to0\) for all bounded signed weights \(q_f\). **All these results remain conditional on (8); (8) is not proved from the nonlinear Wilson Hamiltonian.**

This is a useful reduction: the needed effective-potential integral may grow faster than any power of \(\log(1/h)\), so long as it is \(o(h^{-1/4})\). In contrast, \(\mathfrak B_f=O(\log(1/h))\) suffices for polynomial near-center mass itself.

## 5. Further exact sum rule and limitations

Integrating the original radial flux equation on a half-period, with no current at both endpoints, gives the *true-vacuum weighted balance law*

\[
\boxed{\int_0^{\pi/2}\sin^2u\,[\mathcal U_f(\cos u)-E_f^-]\psi_f(u)\,du=0.}\tag{9}
\]

Unless \(\mathcal U_f-E_f^-\equiv0\), the effective excess fiber energy must take both signs in the \(\psi_f\sin^2u\)-weighted sense. This does not control the **unweighted positive-part budget** in (2), because the density \(\psi_f\) may be tiny where \(\mathcal U_f-E_f^-\) is large. The earlier capacity examples demonstrate precisely this failure mode. The proof therefore does **not** show that \(\mathfrak B_f\) is finite uniformly in refinement or satisfies (8).

The new target is a one-sided, integrated **quantum fiber-energy** bound (8), not pointwise monotonicity or Gaussian heat-trace submodularity. No physical spectral gap, quartic resolvent, Stage7/26 correspondence, or full continuum Yang–Mills reconstruction is claimed.

## 6. Reproducibility

`verify_one_sided_fiber_budget.py` checks the Riccati identity and radial integration kernel symbolically, the exact Haar cap formula, the double-integral lower bound, the explicit one-face SU(2) center-avoiding rotor (actual positive, center-even eigenstate), and the sharp asymptotic exponents of (6)–(8). The rotor is an independent SU(2) comparator, not a magnetic-deleted Penrose vacuum. The historical Stage 7/26 archives are unchanged.
