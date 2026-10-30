# The Singular Boundary — locally renormalized eliminated-link resolvent

**Date:** 26 October 2026. **Setting:** finite pure SU(2) (2+1)-dimensional Wilson/Kogut–Susskind Hamiltonian on a finite rhombic Penrose complex. **Status:** exact ground-state-relative Feshbach bound **proved with an explicit conditional Poincaré constant**; volume- and cutoff-uniform lower bound on that constant **not proved**. The earlier bare Haar elimination cannot retain low-energy overlap uniformly at strong magnetic coupling.

## A. Correct ground-state-relative operator and projection

Let \(H=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-p_f)\) on \(L^2(SU(2)^E,dU)\), \(a_e>0\), \(b_f\ge0\), with normalized, smooth, strictly positive unique ground state \(\Omega\) and energy \(E_0\). Let \(\nu(dU)=\Omega(U)^2\,dU\) (normalized) and \(\mathsf U f=\Omega f\), a unitary \(L^2(\nu)\to L^2(dU)\). The ground-state-transformed \(K=\mathsf U^{-1}(H-E_0)\mathsf U\) has the exact nonnegative Dirichlet form
\[
\mathfrak E(f)=\langle f,Kf\rangle_\nu=\sum_ea_e\int|\nabla_ef|^2\,d\nu .\tag{A1}
\]
No interacting magnetic potential remains explicitly in the form: it enters through \(\nu\). On the gauge-invariant subspace, gauge transformations are unitary and preserve \(\nu\).

Fix one edge \(e\), write \(y=(U_g)_{g\ne e}\), and denote by \(\nu_e(du\mid y)\) the conditional ground-state measure on its link group. Define the **ground-state adapted projection**
\[
(P_ef)(u,y)=\int f(u',y)\,\nu_e(du'\mid y),\qquad Q_e=I-P_e.\tag{A2}
\]
This is an orthogonal projection in \(L^2(\nu)\), not the bare Haar projection on \(L^2(dU)\). It obeys \(P_e1=1\), so the true interacting vacuum lies exactly in the retained sector. Since \(\nu\) is gauge invariant, it intertwines the full vertex gauge action: gauge transformations act by left/right translations on the conditioned link, and change \(y\) covariantly. Hence \(P_e\) preserves the physical subspace. Its conjugate \(\mathsf U P_e\mathsf U^{-1}\) is the correct projection in the original Hilbert space.

## B. Theorem R3-CR — exact interacting relative Q-block bound

For almost every \(y\), define the optimal conditional Poincaré constant \(\gamma_e(y)>0\) by
\[
\int|\nabla_u g|^2d\nu_e(u\mid y)\ge\gamma_e(y)\operatorname{Var}_{\nu_e(\cdot\mid y)}(g).
\]
Set \(\gamma_e^{\inf}=\operatorname*{ess\,inf}_y\gamma_e(y)\) (which is positive at each **fixed finite graph**, since \(\Omega\) is strictly positive continuous on compact \(SU(2)^E\)). Then
\[
\boxed{Q_eKQ_e\ge a_e\gamma_e^{\inf}Q_e\quad\text{as quadratic forms on }L^2(\nu).}\tag{B1}
\]
In particular for every real \(0\le z<a_e\gamma_e^{\inf}\), the Q-resolvent exists and
\[
\boxed{\|(Q_eKQ_e-z)^{-1}\|\le(a_e\gamma_e^{\inf}-z)^{-1}.}\tag{B2}
\]
This is a **relative-to-the-exact-interacting-ground-energy** statement, independent of the global extensive value of \(E_0\), for every finite graph and any magnetic coupling.

**Proof.** Disintegrate (A1) by the other link variables. For any \(f\in\operatorname{ran}Q_e\), conditional mean zero holds for almost every \(y\). The single-edge part of (A1) is at least \(a_e\gamma_e^{\inf}\|f\|_\nu^2\); all other edge contributions are nonnegative. Closure and the spectral theorem give (B1)–(B2). The constrained physical-space bound follows by restriction. QED.

An explicit (generally crude) comparison constant is
\[
\boxed{\gamma_e(y)\ge\frac34\frac{\inf_{u}\Omega(u,y)^2}{\sup_{u}\Omega(u,y)^2},\qquad
\gamma_e^{\inf}\ge\frac34 e^{-\mathcal L_e},\quad
\mathcal L_e=\sup_{u,u',y}\big|\log\Omega(u,y)^2-\log\Omega(u',y)^2\big|.}\tag{B3}
\]
**Proof.** For any probability density \(\rho\) with respect to Haar having ratio \(m/M\), \(\operatorname{Var}_{\rho}(f)\le M\operatorname{Var}_{\rm Haar}(f)\), while \(\int|\nabla f|^2\rho\ge m\int|\nabla f|^2\); use the Haar SU(2) Poincaré constant \(3/4\). QED.

**Sharp admission criterion:** A cutoff- and volume-uniform \(\mathcal L_e\le L_*\), or another independently demonstrated \(\gamma_e^{\inf}\ge\gamma_*>0\), would make (B2) uniform for \(z<a_-\gamma_*\). **No such ground-state conditional estimate has been derived for the fully interacting Penrose continuum trajectory** \(b_f\sim h^{-2}\). Even if \(\gamma_*\) were obtained, repeated spatial elimination also needs off-diagonal/Schur-map and frame estimates; (B2) alone does not prove R3 or R2.

## C. Exact countertest for the prior bare Haar projection

For a single gauge-invariant rhombus with four equal edge electric coefficients \(a>0\) and magnetic coefficient \(b>0\), gauge fixing identifies physical wavefunctions with class functions of one SU(2) holonomy \(W\). The bare Haar shared-edge projection restricted to physical class functions has range \(\operatorname{span}\{1\}\). Write \(\alpha_{a,b}=\langle 1,\Omega_{a,b}\rangle\). Then
\[
\boxed{\lim_{b/a\to\infty}|\alpha_{a,b}|=0.}\tag{C1}
\]
So bare Haar projection **loses almost the entire interacting ground state** in the magnetic-dominated limit; reconstructing a normalized vacuum from its bare projection requires a norm amplification \(1/|\alpha_{a,b}|\to\infty\). A lower frame or well-conditioned reconstruction cannot be inferred from bare Haar projection.

**Proof with a quantitative rate.** The earlier variational trial \(e^{\lambda p(W)}\), with \(p=\chi_{1/2}(W)/2\), gives \(E_0\le2\sqrt{2ab}\), hence
\[
\int(1-p)\Omega_{a,b}^2\,dW\le2\sqrt{2a/b}.\tag{C2}
\]
Let \(D_\delta=\{W:p(W)\ge1-\delta\}\). SU(2) Haar geometry gives \(\operatorname{Haar}(D_\delta)\le C_0\delta^{3/2}\) for \(0<\delta<1/2\) (on \(SU(2)\simeq S^3\), the ball near the identity has radius proportional to \(\sqrt\delta\)). Markov gives \(\int_{D_\delta^c}\Omega^2\,dW\le 2\sqrt{2a/b}/\delta\). Cauchy–Schwarz on each piece implies
\[
|\alpha_{a,b}|^2\le 2C_0\delta^{3/2}+4\sqrt{2a/b}/\delta.
\]
Choose \(\delta=(a/b)^{1/5}\), valid for large \(b/a\), obtaining
\[
\boxed{|\alpha_{a,b}|^2\le C_1(a/b)^{3/10}\quad(b/a\text{ sufficiently large}).}\tag{C3}
\]
All constants are numerical. This is a true **overlap obstruction**, not a claim that the interacting physical excitation gap goes to zero. A ground-state-adapted projection (A2) has \(P_e1=1\) and avoids exactly this failure.

## D. Strong-electric control for the *bare* relative block, a complementary theorem

For the bare Haar \(P_e^\mathrm H\) in the original Hilbert space, let \(B_e=\sum_{f\ni e}b_f\), and let \(H_{\neg e}\) omit the electric term on e and its incident plaquette potentials. Then \(E_0(H)\le E_0(H_{\neg e})+B_e\) by a constant-link trial, while
\[
Q_e^\mathrm H H Q_e^\mathrm H\ge E_0(H_{\neg e})+\tfrac34a_e.
\]
Thus
\[
\boxed{Q_e^\mathrm H(H-E_0)Q_e^\mathrm H\ge(\tfrac34a_e-B_e)Q_e^\mathrm H.}\tag{D1}
\]
This is genuinely relative to \(E_0\), volume-independent, and valid at all couplings, but positive only if \(B_e<3a_e/4\). For the geometric continuum trajectory \(B_e=O(h^{-2})\), this simple estimate gives no positive constant. It explains rigorously why an unadapted electric-sector block is controlled only in a strong-electric regime.

## E. Why a uniform relative eliminated-sector resolvent would not automatically prove the mass gap

Let \(P_e\) be the adapted projection and let \(Q_eKQ_e\ge\gamma Q_e\). The Feshbach map for \(K-z\) is
\[
F_P(z)=P_e(K-z)P_e-P_eKQ_e(Q_eKQ_e-z)^{-1}Q_eKP_e.
\]
There is exact source reconstruction \(J_z=P_e-Q_e(Q_eKQ_e-z)^{-1}Q_eKP_e\) and associated metric \(J_z^*J_z\). The relative resolvent only bounds \((Q_eKQ_e-z)^{-1}\); it does not bound the off-diagonal \(Q_eKP_e\) in a cutoff-independent manner, and the Schur correction has to retain all generated multiloop operators and connected-source terms. To prove a gap one also needs a coercive estimate on the retained effective sector and a frame lower bound after blocking. In other words, the conditional Poincaré estimate is a rigorous **single-edge eliminated-sector theorem**, not a complete spectral-gap argument.

A subtlety: \(P_e\) depends on \(\Omega\), so it is not a constructive geometry-only RG map until \(\nu_e\) and its fluctuations can be controlled independently. It is a valid mathematical block and a sharp way to isolate what Wilson ground-state dynamics must supply.

## F. Required independent quantitative inputs for arbitrary-coupling R3 and continuum R2

1. Establish the conditional ground-state measure's uniform one-link Poincaré constants \(\gamma_e^{\inf}\ge\gamma_*>0\) in physical units along \(a\to0\), **without assuming the full gap**. The crude oscillation criterion (B3) is only sufficient, may fail even when conditional gaps are large, and is not proved.
2. Bound the adapted block's off-diagonal Schur term in a **local, scale-dependent** norm uniformly across Penrose patches, despite \(b_f=O(h^{-2})\). This remains open; the ground-state transform transfers the interaction into the conditional measure and nontrivial connections between neighboring edge derivatives.
3. Show the effective retained operator has positive local/collective coercivity and verify preservation of the graded multilocal Wilson-frame observability constants, including center/global sectors. One-edge conditional coercivity alone is not global tensorization.
4. R2 separately: construct the quantum continuum Schwinger functions and physical Hamiltonian for the specified Penrose regulator, with controlled anisotropic matching, renormalized source normalization, and boundary/volume limits.

**Conclusion:** The exact interacting-ground-state-relative resolvent is now derived at each finite cutoff with no extensive vacuum-energy subtraction problem, and the bare-Haar projection is proved nonuniform at strong magnetic coupling. The continuum-uniform lower bound on the conditional Poincaré constant is not established; asserting it would assume precisely the new, difficult Wilson-model estimate requested.
