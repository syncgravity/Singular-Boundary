# R3-IR — Deleted-vacuum Wilson-character positivity and a finite-spin Haar-cap certificate

**Date:** 2026-10-29. **Classification:** unconditional SU(2) harmonic-analysis theorem applicable to any finite magnetic-deleted Wilson-vacuum marginal; *conditional* nonlinear Penrose consequence. Full manuscript, numerical certificate, and execution log: \`singular_boundary_deleted_character_positivity_2026-10-29.zip\`. No continuum mass gap is proved.

## Exact physical marginal and character data

For the actual unique positive magnetic-deleted ground state \(\Omega_f^-\), let \(F_{f,h}(U)dU\) denote the gauge-invariant deleted-face SU(2) holonomy probability density relative to normalized Haar. Global gauge invariance makes \(F\) central and deleted-face center-flux symmetry makes \(F(-U)=F(U)\). For spin \(j\in\frac12\mathbb N_0\), let \(\chi_j\) be the orthonormal SU(2) character, dimension \(d_j=2j+1\). Define **physical gauge-invariant observables**
\[
c_j=\int F(U)\chi_j(U)dU=\langle\Omega_f^-,\chi_j(W_f)\Omega_f^-\rangle.
\]
Then \(c_0=1\), \(|c_j|\le d_j\), and \(c_j=0\) for half-odd-integer \(j\). **No sign of the remaining integer-spin expectations is assumed.**

## CP-1. Positive type forces a polynomial center cap

For the SU(2) geodesic ball \(B_a=\{U:u(U)<a\}\), \(0<a<\pi/2\), write its normalized Haar mass
\[
H(a)=\frac{a-\frac12\sin(2a)}{\pi}.
\]
Put \(A=B_{a/2}\), \(q=1_A\), \(k=q*q^\vee\) (group convolution, \(q^\vee(U)=q(U^{-1})\)). Geodesic triangle inequality and Haar Cauchy give
\(0\le k\le H(a/2)1_{B_a}\); \(\int k=H(a/2)^2\).
Central Peter–Weyl convolution has the **nonnegative** expansion
\[
k=\sum_j \frac{b_j^2}{d_j}\chi_j,\qquad b_j=\int_A\chi_j\,dU.
\]
Consequently, if **all integer-spin \(c_j\ge0\)**, then
\[
H(a/2)\Pr_F(B_a)\ge\int Fk=H(a/2)^2+\sum_{j>0}c_jb_j^2/d_j\ge H(a/2)^2,
\]
and therefore
\[
\boxed{\Pr_F(B_a)\ge H(a/2).}
\]
Center parity eliminates half-odd spins without further assumptions. At the physical deficit cap \(d_f=1-p_f\le h\), take \(a_h=\arccos(1-h)\). Then
\[
\boxed{m_f^-(h)\ge H(a_h/2)
=\bigl(\tfrac{\sqrt2}{6\pi}+O(h)\bigr)h^{3/2}.}
\]
Together with the earlier exact deleted-vacuum exponential trial theorem and Penrose coefficient bounds, this **conditionally** yields \(\Delta_f=O(h^{-1}\log(1/h))\) for every interior face, hence the earlier extreme-defect and fixed-support Wilson–angle conclusions. The antecedent *character positivity in the actual cycle-rich vacuum* remains OPEN.

## CP-2. Finite-spin, signed negative-budget certificate

Let \(\phi_a\in C^\infty(SU(2))\) be central, real, \(0\le\phi_a\le1\), supported inside \(B_{a/2}\). Put
\[
A_a=\int\phi_a,\quad N_a=\int\phi_a^2,\quad \beta_j(a)=\int\phi_a\chi_j,\quad
\mathrm{Neg}_J=\sum_{0<j\le J}[-c_j]_+\frac{\beta_j(a)^2}{d_j}.
\]
The convolution \(k_a=\phi_a*\phi_a^\vee\) obeys \(0\le k_a\le N_a1_{B_a}\), \(\int k_a=A_a^2\), and has coefficients \(\beta_j^2/d_j\). Using \(|c_j|\le d_j\) and character Parseval gives the **exact unconditional certificate**
\[
\boxed{
\Pr_F(B_a)\ge\frac{[A_a^2-\mathrm{Neg}_J-\mathrm{Tail}_J]_+}{N_a},
\qquad
\mathrm{Tail}_J=N_a-\sum_{j\le J}\beta_j(a)^2.
}
\]
Thus strict nonnegativity of all characters is *not necessary*: sufficiently small weighted negative-character mass through the finite spin cutoff also suffices. These coefficients are standard physical Wilson-character expectations, and the tail depends only on a chosen bump, not on the interacting vacuum.

For a fixed smooth scaled bump \(\phi_a(U)=\phi(u(U)/a)\), equal to one for \(u\le a/4\) and zero for \(u\ge a/2\), one has \(A_a\asymp N_a\asymp a^3\). The exact SU(2) Casimir \(j(j+1)\), Parseval, and smooth bump estimates give, for every fixed integer \(m\ge1\),
\[
\mathrm{Tail}_J\le C_m a^{3-2m}[J(J+1)]^{-m}\le C'_m a^3(Ja)^{-2m}.
\]
For any \(\varepsilon>0\), taking \(m>3/(2\varepsilon)\) and \(J(a)\ge C a^{-1-\varepsilon}\) makes \(\mathrm{Tail}_J=o(a^6)=o(A_a^2)\). At \(a\asymp\sqrt h\), it therefore suffices to establish an appropriate negative-character budget **only through spins \(J(h)=O(h^{-(1+\varepsilon)/2})\)**.

For reference, the sharp-cap coefficients for \(j>0\) are
\[
b_j(r)=\frac1\pi\left[\frac{\sin(2jr)}{2j}-\frac{\sin((2j+2)r)}{2j+2}\right],\quad b_0(r)=H(r).
\]

## CP-3. Sign obstruction and scope

The smooth center-even positive SU(2) density \(F_\kappa(U)\propto e^{-\kappa p(U)^2}\) has
\(c_1=4\mathbb E_{F_\kappa}p^2-1<0\) for every \(\kappa>0\). It can be realized as the squared unique positive ground state of a separate center-symmetric class rotor. Hence positivity, center symmetry and a ground-state property alone cannot establish character positivity. This is **not** a counterexample for the magnetic-deleted Wilson Hamiltonian. In addition, SU(2) flux-sheet representations can have signed terms; a reflection-positivity or character-expansion argument for the present Hamiltonian must be verified independently.

**Verified:** deterministic SU(2) Haar character integrals, smooth convolution Fourier tails at three angular scales, finite-spin cap certificates, and negative spin-one benchmark. The companion ZIP contains the complete proof, verifier, log and SHA256 manifest. No Monte Carlo, no Stage26 archive modifications.

**OPEN:** prove \(\mathrm{Neg}_{J(h)}=o(h^3)\), or all integer-spin \(c_j\ge0\), for the actual cycle-rich deleted Penrose vacuum; this would prove the required polynomial flat-holonomy small-ball estimate. The full physical mass gap, quartic resolvent, and continuum reconstruction remain open.
