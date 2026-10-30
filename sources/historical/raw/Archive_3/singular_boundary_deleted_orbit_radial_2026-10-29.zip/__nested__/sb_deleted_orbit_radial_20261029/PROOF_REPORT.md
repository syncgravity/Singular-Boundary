# The Singular Boundary — Radial data-processing for deleted-face collective orbit currents

**Date:** 2026-10-29. **Program:** R3 independent reconstruction, finite SU(2) Wilson Hamiltonians on simply connected edge-to-edge planar rhombus disks. **Status:** exact finite-volume group and marginal inequalities, sharp positive gauge-invariant trial-state separation, conditional Penrose refinement consequence. **Open:** orbit-current refinement rate for the actual nonlinear deleted ground state, all-bulk flat-holonomy polynomial small ball, physical mass gap, and continuum construction.

## 1. Setting and a sharper target

Let \(H_f^-=\sum_ea_e(-\Delta_e)+\sum_{g\ne f}b_g(1-p_g)\) with positive link coefficients and all-vertex Gauss invariance on a finite simply connected disk. The unique positive normalized gauge-invariant ground state is \(\Omega^-\). Under maximal-tree gauge reduction the independent based face holonomies carry product SU(2) Haar measure with residual diagonal conjugation. Let \(U_f\in SU(2)\) be the deleted-face holonomy and \(p=\frac12\mathrm{ReTr}\,U_f=\cos u\). Its Haar class density is \(\rho_0(p)=\frac2\pi\sqrt{1-p^2}\), with angular version \(\omega_0(u)=\frac2\pi\sin^2u\). Define the actual quantum marginal \(F(p)=\mathbb E_{\rm Haar}[|\Omega^-|^2\mid p]\), \(v(u)=\sqrt{F(\cos u)}\). Center-flux symmetry gives \(F(p)=F(-p)\). No spectral-gap assumption is made.

The previous orbit theorem established the *sufficient* but unproved condition \(\|Q_f\Omega^-\|=o(h^{3/4})\), or a sufficient collective-orbit Fisher bound \(\mathcal J_{\rm orb}=o(h^{3/2})\). The stronger condition forces almost complete **conditional wavefunction** Haar independence. A lower bound on the **scalar marginal** does not need this.

## 2. OR-1: exact conditional orbital-score data-processing identity

Choose any exact Haar-preserving deleted-face SU(2) transport, whose action in independent based face coordinates is \(U_f\mapsto gU_f\) while keeping other based face coordinates fixed. Write \(D_j\), \(j=1,2,3\), for its anti-self-adjoint infinitesimal generators, with SU(2) Casimir normalization \(-\Delta\chi_{1/2}=\frac34\chi_{1/2}\). Then for the deleted-face trace:

\[
 \sum_j(D_jp)^2=\frac{1-p^2}{4}=:a(p),\qquad \sum_jD_j^2p=-\frac34p.
\]

All \(D_j\) are Haar divergence-free, including their pullbacks to the original links. Define
\[
 Q(p)=\mathbb E_{\rm Haar}\left[\Omega^-\sum_j(D_jp)(D_j\Omega^-)\;\middle|\;p_f=p\right].
\]

Test group integration by parts against any smooth \(k(p)\):
\[
\int k(p)\left[-\frac34p F(p)+2Q(p)\right]\rho_0(p)dp
=-\int k'(p)a(p)F(p)\rho_0(p)dp.
\]
Since \((\rho_0a)'=-\frac34p\rho_0\), cancellation of the Haar drift gives the exact **interacting-ground-state marginal-score identity**
\[
\boxed{\quad a(p)F'(p)=2Q(p).\quad} \tag{OR-1}
\]
This identity retains all noncentral electric-commutator and environmental correlations through \(D_j\Omega^-\). It is valid for any smooth positive gauge-invariant state, and hence for the actual deleted vacuum; the state need not be Gaussian.

## 3. OR-2: sharp radial Fisher contraction (including a localized shell)

By conditional Cauchy–Schwarz and \(\sum_j(D_jp)^2=a(p)\),
\[
 |Q(p)|^2\le F(p)a(p)\;\mathbb E_{\rm Haar}\left[\sum_j|D_j\Omega^-|^2\mid p\right].
\]
Equation (OR-1) implies, pointwise after Haar conditioning,
\[
 a(p)|\partial_p\sqrt F|^2\le
 \mathbb E_{\rm Haar}\left[\sum_j|D_j\Omega^-|^2\mid p\right].
\]
Integrating gives the exact **information data-processing** inequality
\[
\boxed{\ J_{\mathrm{rad}}:=\int_{-1}^1\rho_0(p)a(p)|\partial_p\sqrt F|^2dp
 \le \mathcal J_{\mathrm{orb}}:=\sum_{j=1}^3\|D_j\Omega^-\|_2^2.\ }\tag{OR-2}
\]
For \(u=\arccos p\), \(J_u:=\int_0^\pi\omega_0(u)|v'(u)|^2du=4J_{\mathrm{rad}}\), hence
\[
\boxed{\ J_u\le4\mathcal J_{\mathrm{orb}}.\ }\tag{OR-3}
\]
Moreover, for every measurable interval \(I\subset[0,\pi]\), the same conditional Cauchy–Schwarz gives
\[
\boxed{\ \int_I\omega_0(u)|v'(u)|^2du
 \le4\sum_j\int_{\{u_f\in I\}}|D_j\Omega^-|^2\,dU.\ }\tag{OR-4}
\]
Thus the *cap annulus only* can be charged to an annulus-localized collective score. The angular directions of the conditional state need not be small.

## 4. OR-3: a one-power weaker sufficient continuum small-ball criterion

Let \(c_h=\mathbb P_{\mathrm{Haar}}(1-p\le h)=\frac{\arccos(1-h)-(1-h)\sqrt{2h-h^2}}\pi\sim\frac{4\sqrt2}{3\pi}h^{3/2}\). The normalized radial Sobolev inequality on SU(2) (\(S^3\)), as proved in the previous marginal-capacity audit, implies for sufficiently small \(J_u\)
\[
 m_f^-(h)\ge c_h\left[1-C_S c_h^{-1/6}\sqrt{J_u}\right]_+^2.
\]
Together with (OR-3),
\[
\boxed{\ m_f^-(h)\ge c_h\left[1-2C_Sc_h^{-1/6}\sqrt{\mathcal J_{\mathrm{orb}}}\right]_+^2.\ }\tag{OR-5}
\]
In particular
\[
\boxed{\ \sup_f\mathcal J_{\mathrm{orb},f,h}=o(h^{1/2})
 \quad\Longrightarrow\quad m_f^-(h)=(1-o(1))c_h\ \text{ uniformly.}\ }\tag{OR-6}
\]
The previous orbit-projection criterion needed \(o(h^{3/2})\); the radial score criterion needs only \(o(h^{1/2})\), an improvement by **one full power of \(h\)**. The preexisting magnetic-deletion variational theorem then gives \(\Delta_f=O(h^{-1}\log(1/h))\) and consequent extreme-defect rarity under the previously declared Penrose coefficient and collar conditions.

For the cap annulus \(I=[a/2,a]\), the preceding shell-capacity theorem requires \(K(a)J_{\mathrm{shell}}\le e^{-2T_{\mathrm{out}}}/8\). Since \(J_{\mathrm{shell}}\le4\mathcal J_{\mathrm{orb},I}\), the sufficient **localized** criterion is
\[
\boxed{\ 4K(a)\mathcal J_{\mathrm{orb},[a/2,a]}\le\tfrac18 e^{-2T_{\mathrm{out}}(a)}.\ }\tag{OR-7}
\]
For \(a\asymp\sqrt h\), \(K(a)\asymp h^{-1/2}\). This uses only annulus orbital Fisher plus exterior positive radial current, not global orbital Haar independence.

**OPEN:** neither the \(o(h^{1/2})\) global-orbit score estimate nor the annulus/exterior pair is established for the true cycle-rich Penrose deleted vacuum. Existing electric kinetic bounds are too coarse.

## 5. OR-4: explicit strictly positive gauge-invariant witness separating marginal Haar from orbital Haar

Take two independent based face holonomies \(U,V\in SU(2)\) with diagonal-conjugation Gauss invariance, and \(0<\varepsilon<1\). Set \(p(Z)=\frac12\mathrm{ReTr}Z\) and
\[
\boxed{\ \Psi_\varepsilon(U,V)=\frac{1+\varepsilon p(UV^{-1})}{\sqrt{1+\varepsilon^2/4}}.\ }\tag{OR-8}
\]
It is strictly positive, smooth, normalized in product Haar and gauge invariant under \((U,V)\mapsto(kUk^{-1},kVk^{-1})\). For fixed \(U\), Haar translation in \(V\) gives \(\int p(UV^{-1})dV=0\) and \(\int p(UV^{-1})^2dV=1/4\), so
\[
\boxed{\ \int\Psi_\varepsilon(U,V)^2dV=1\quad\text{for every }U.\ }\tag{OR-9}
\]
Therefore the target \(U\) has **exactly Haar marginal**, including all center cap probabilities; its radial Fisher \(J_{\mathrm{rad}}=0\). But Haar-fiber averaging \(P_U\) gives
\[
 \|Q_U\Psi_\varepsilon\|_2^2=\frac{\varepsilon^2}{4+\varepsilon^2}>0,
 \qquad\mathcal J_{\mathrm{orb}}(\Psi_\varepsilon)=\frac{3\varepsilon^2}{4(4+\varepsilon^2)}>0.
\]
These saturate \(\|Q_U\Psi\|^2\le\frac43\mathcal J_{\mathrm{orb}}\). For \(\varepsilon=1/2\), \(\eta^2=1/17\), \(\mathcal J_{\mathrm{orb}}=3/68\), while \(J_{\mathrm{rad}}=0\) and every cap ratio to Haar is **exactly one**.

This is an **explicit trial-state witness**, not an eigenstate of the magnetic-deleted Penrose Hamiltonian. It rigorously shows that the prior full orbit-flatness target \(\eta=o(h^{3/4})\), and even small full orbital Fisher, are **not necessary** for an exactly Haar marginal. The actual task is to control **radial score transmission** through nonabelian environmental correlations, not all conditional wavefunction correlations.

## 6. Verification, scope and next obligation

The deterministic checker reproduces the SU(2) Casimir/gradient conventions, exact character Haar moments, positive witness normalization and saturation, the asymptotic cap density, and a nonzero radial-score inequality on a separately chosen positive class-function state. The proof of (OR-1)–(OR-4) is analytic Haar integration by parts and conditional Cauchy–Schwarz; no Monte Carlo or substitution of a Gaussian vacuum occurs. The checks do not measure the genuine many-face deleted vacuum.

**PROVED:** exact nonlinear marginal-score data processing, shell-localized form, sharper conditional radial-Fisher criterion, and a sharp gauge-invariant positive witness of why full orbital flatness is unnecessarily strong.

**OPEN:** regulator-uniform \(J_{\mathrm{rad}}=o(h^{1/2})\) or suitable cap-shell/exterior current bounds in the actual deleted Penrose vacuum; all-bulk magnetic deletion, fixed-support Wilson–angle connected covariance, mass gap and continuum reconstruction. The historical Penrose Stage26 and Q14 archives were not modified.
