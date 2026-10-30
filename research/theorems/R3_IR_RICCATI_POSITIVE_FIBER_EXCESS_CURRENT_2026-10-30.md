# Riccati one-sided fiber-energy control of the completed-cage Wilson current

**Date:** 2026-10-30. **Status:** exact finite-volume consequence of the already archived nonlinear physical deleted-face fiber equation (EF-1, 2026-10-29), providing a new direct *signed* estimate independent of Harnack/Fisher constants. A **uniform excess-fiber-energy estimate remains unproved**; no continuum mass gap is claimed.

## Archived input and provenance

Use the 2026-10-29 theorem in \`research/theorems/R3_IR_DELETED_FACE_EXACT_FIBER_HAAR_MASS_2026-10-29.md\` (EF-1). For the true Gauss-invariant Wilson ground state on any finite planar original-link rhombus disk with target magnetic term deleted, define its positive angular class amplitude \(\Psi_f(u)=\psi_f(\cos u)\) and exact nonadiabatic conditional fiber energy \(U_f(\cos u)\). The latter retains every collective mode and derivative of the conditional normalized state, and is not a prescribed external potential. Write \(A_f=\sum_{e\in\partial f}a_e>0\), and \(E_0\) for the actual vacuum energy. EF-1 proves
\[
-\frac{A_f}{4}\left[\Psi_f''+2\cot u\,\Psi_f'\right]
+\big(U_f(\cos u)-E_0\big)\Psi_f=0,\qquad 0<u<\pi.
\tag{1}
\]
Fixed-volume smooth positive endpoint regularity is proved separately; in particular \(\Psi_f'(0)=0\) and the logarithmic derivative is \(O(u)\).

The exact signed current budget from the archived radial Ward identity is
\[
\mathfrak T_f=\int_0^{\pi/2}[\partial_u\log\Psi_f(u)]_+\,du.
\]

## New theorem: direct one-sided excess-fiber-energy inequality

Set \(s(u)=\partial_u\log\Psi_f(u)\) and \(D(u)=U_f(\cos u)-E_0\). Then
\[
\boxed{
s'(u)+2\cot u\,s(u)+s(u)^2=\frac4{A_f}D(u).
}\tag{2}
\]
Thus
\[
\boxed{
\sin^2u\,s(u)
=\frac4{A_f}\int_0^u\sin^2v\,D(v)\,dv
-\int_0^u\sin^2v\,s(v)^2\,dv.
}\tag{3}
\]
It follows *without any sign or monotonicity assumption on \(D\)* that
\[
\boxed{
[s(u)]_+\le\frac4{A_f\sin^2u}
\int_0^u\sin^2v\,[D(v)]_+\,dv.
}\tag{4}
\]
Integrating and exchanging the order by Tonelli,
\[
\begin{aligned}
\mathfrak T_f
&\le\frac4{A_f}\int_0^{\pi/2}
\sin^2v\,[D(v)]_+
\left(\int_v^{\pi/2}\frac{du}{\sin^2u}\right)dv\\
&=\boxed{\frac4{A_f}\int_0^{\pi/2}
\sin v\cos v\,[U_f(\cos v)-E_0]_+\,dv.}
\end{aligned}\tag{5}
\]
The complete-center integral has **no small-cap denominator** and no Harnack multiplicative constant.

In particular, when the *actual* conditional excess fiber energy satisfies
\[
U_f(\cos u)-E_0\le\Lambda_f
\quad\text{for all }0\le u\le\pi/2,
\]
for some \(\Lambda_f\ge0\),
\[
\boxed{\mathfrak T_f\le\frac{2\Lambda_f}{A_f}.}\tag{6}
\]
The constant follows from \(\int_0^{\pi/2}\sin u\cos u\,du=1/2\). A condition weaker than the pointwise cap bound is the **weighted positive excess condition**
\[
\boxed{\quad
\sup_{f\in D_R}\frac1{A_f}
\int_0^{\pi/2}\sin u\cos u\,
[U_{f,h}(\cos u)-E_{0,h}]_+\,du
=o(h^{-1/4}).
\quad}\tag{7}
\]
If (7) is independently established for the actual completed-cage interacting vacuum, (5) **rigorously implies** the previously specified current gate. It is a sufficient condition, not a claim that (7) is true.

## Sign and normalizations audit

The starting radial operator is \(-A_f/4(\partial_u^2+2\cot u\,\partial_u)\). Its ground state satisfies \(\Psi''+2\cot u\Psi'=(4/A_f)D\Psi\). Logarithmic differentiation produces the *positive* \(s^2\) term on the left in (2), which appears with a negative sign in (3). This is the essential beneficial nonlinear term; dropping it is an upper bound on the **adverse positive** radial score. The integration kernel is exact since \(\int_v^{\pi/2}\csc^2u\,du=\cot v\), and \(\sin^2v\cot v=\sin v\cos v\). At the center, \(\sin^2u\,s(u)\to0\) by smooth endpoint regularity. There is no invocation of mass gap, spectral gap, Gaussian reference dynamics, or conditional rare-event normalization.

## Relationship to the archived EF-2 and the unsolved gate

The archived **single-crossing** hypothesis implies \(s(u)\le0\) and \(\mathfrak T_f=0\). This new inequality does not require single crossing; it tolerates nonmonotone conditional fiber energies, as long as the *weighted positive excess* is sufficiently small. That is a distinct and potentially weaker hypothesis. EF-1 already retains the full nonlinear collective sector. The new estimate does not prove (7): the conditional energy \(U_f\) contains electric derivatives of the normalized fiber state and can exhibit large positive excursions. An unconditional total energy or Agmon curvature tail is not a pointwise/weighted positive excess bound, and cannot simply replace it.

## Immediate next proof task

Use the original-link conditional state \(\Phi_f=\Omega_f^-/\psi_f(p_f)\) from EF-1 to estimate
\[
\frac1{A_f}\int_0^{\pi/2}\sin u\cos u
[\,\mathbb E_\mu(T_{\mathrm{fiber}}[\Phi_f]+V_f^-\Phi_f^2\mid p_f=\cos u)-E_0\,]_+\,du
\]
uniformly in completed Penrose interiors. Exploit signed cancellations in the conditional kinetic energy and magnetic geometry. Do not bound each extensive term separately unless its volume dependence cancels explicitly. If this estimate cannot be proved, record a counterexample or exact obstruction; do not label the continuum gap solved.

**Result classification:** (2)–(6) proved; (7) a precise **open sufficient condition**. The broader source-inserted physical spectral/continuum gates remain separate and open.
