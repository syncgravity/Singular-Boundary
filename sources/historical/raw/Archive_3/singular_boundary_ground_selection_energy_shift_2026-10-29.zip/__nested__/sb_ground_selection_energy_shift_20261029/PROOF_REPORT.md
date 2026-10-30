# The Singular Boundary — Gap-free energy-shift certification of the deleted-face center cap

**Research continuation:** 2026-10-29. **Scientific status:** a new exact finite-volume, nonlinear-SU(2) *conditional* ground-state cap criterion that requires two certified ground-energy enclosures, **not** a certified excitation gap; a rigorous center-even free-SU(2)-rotor realization that proves a Haar-order cap using those inequalities; and a quantitative comparison of sharp and convolution sources. **Still open:** the necessary interacting eight-face or regulator-uniform Penrose *energy-difference* lower bound, ground-state radial current control, and continuum Yang–Mills mass gap.

## 1. Actual physical nonlinear Wilson Hamiltonian and the target center symmetry

Let the finite all-vertex Gauss-invariant physical SU(2) Hamiltonian with one deleted magnetic face be

\[
H^-_{f,h}=\sum_e a_e(-\Delta_e)+\sum_{q\ne f}b_q(1-p_q),\qquad p_q=\tfrac12\mathrm{Tr}\,W_q,\quad a_e>0,\ b_q\ge0,
\]

with \(-\Delta\chi_j=j(j+1)\chi_j\). Under the disk geometry used in the prior program, the canonical target center-flux involution \(C_f\) flips \(W_f\mapsto-W_f\), leaves all retained Wilson potentials unchanged, and commutes with the electric operator. The unique strictly positive finite-volume ground state \(\Omega_h\) is center even. Let \(B_h^+=\{p_f\ge1-h\}\), \(B_h^-=\{p_f\le-(1-h)\}\), \(0<h<1\), so these sets are disjoint and \(C_f B_h^+=B_h^-\).

### Theorem ES-1 — positive-source ground-energy shift, full nonlinear physical model

Define the center-even, nonnegative, bounded multiplication source

\[
K_h=\mathbf 1_{B_h^+}+\mathbf 1_{B_h^-},\qquad
E_h(\lambda)=\inf\sigma(H^-_{f,h}+\lambda K_h),\quad\lambda>0.
\]

Since \(\Omega_h\) is an admissible trial state for the perturbed operator,

\[
E_h(\lambda)\le E_h(0)+\lambda\langle\Omega_h,K_h\Omega_h\rangle
=E_h(0)+2\lambda\Pr_{\Omega_h}(B_h^+).
\]

Therefore the **exact, nonperturbative, gap-free** comparison is

\[
\boxed{\Pr_{\Omega_h}(B_h^+)\ge\frac{E_h(\lambda)-E_h(0)}{2\lambda}.}\tag{ES1}
\]

No excitation spectrum, Ritz eigenvector, mixing time, or spatial-reflection hypothesis is required for ES1. The center-even condition is important: the full-Hilbert ground state remains in the center-even sector when the nonnegative source is inserted, and the source cannot mix target-center-odd states. For a nonnegative, target-center-even smoothing source \(K=k_a^+=(k_a(W_f)+k_a(-W_f))/2\) with \(k_a\le\nu_a\mathbf1_{B_a^+}\), the analogous exact inequality is

\[
\boxed{\Pr_{\Omega_h}(B_a^+)\ge\frac{E_{h,k}(\lambda)-E_h(0)}{\lambda\nu_a}.}\tag{ES2}
\]

It follows because \(\langle k_a^+\rangle_{\Omega_h}=\langle k_a\rangle_{\Omega_h}\le\nu_a\Pr_{\Omega_h}(B_a^+)\). Unlike the earlier residual/gap wavefunction transfer, ES1–ES2 control the **true interacting ground-state cap directly** as soon as *separate* ground-energy enclosures are available.

## 2. Theorem ES-2 — certified two-energy Ritz enclosure, no excited-state gap

Let \(P\) be **any finite-rank orthogonal projection onto a subspace of the center-even physical Hilbert space** with \(Q=I-P\). Work entirely in that even sector. Let \(H_\lambda=H^-_{f,h}+\lambda K_h\), and assume certified numbers satisfy

\[
 e_\lambda\le\inf\sigma(PH_\lambda P),\qquad
 \langle\xi,QH_\lambda Q\xi\rangle\ge q_\lambda\|\xi\|^2,\qquad
 \|QH_\lambda P\|\le\rho_\lambda.
\]

The first condition is a **lower** enclosure of the finite Ritz bottom (not just a floating approximation). Since the positive block form satisfies

\[
\langle(x,y),H_\lambda(x,y)\rangle
\ge e_\lambda\|x\|^2+q_\lambda\|y\|^2-2\rho_\lambda\|x\|\|y\|,
\]

the 2-by-2 min–max principle yields the certified lower ground-energy enclosure

\[
\boxed{L_\lambda=\frac{e_\lambda+q_\lambda-\sqrt{(e_\lambda-q_\lambda)^2+4\rho_\lambda^2}}2\ \le E_h(\lambda).}\tag{ES3}
\]

If the separate Ritz trial for the unperturbed Hamiltonian supplies an **upper** enclosure \(E_h(0)\le U_0\), then the **complete gap-free cap certificate** is

\[
\boxed{\Pr_{\Omega_h}(B_h^+)\ge\frac{[L_\lambda-U_0]_+}{2\lambda}.}\tag{ES4}
\]

When \(q_\lambda>e_\lambda\), the simpler certified estimate

\[
L_\lambda\ge e_\lambda-\frac{\rho_\lambda^2}{q_\lambda-e_\lambda}\tag{ES5}
\]

also holds. Thus an explicit sufficient **energy-only** check for a Haar-order center cap is

\[
\boxed{e_\lambda-U_0-\frac{\rho_\lambda^2}{q_\lambda-e_\lambda}\ge 2c\lambda\,m_H(h),\quad q_\lambda>e_\lambda,}\tag{ES6}
\]

where \(m_H(h)=\Pr_{\rm Haar}(B_h^+)\asymp h^{3/2}\). ES6 is **not proved** for the full connected eight-face model; it is the new, precisely stated ground-state-selection gate.

**Natural admissible projection.** If \(P=P_M=\mathbf1_{[0,M]}(T)\) is the complete physical *center-even* electric spectral cutoff, then \(QH_\lambda Q\ge M\) because the Wilson potential and \(\lambda K_h\) are nonnegative. Since \(QTP=0\), the coupling is exactly \(Q(V+\lambda K_h)P\), for which a finite matrix norm bound or a conservative \(\|V\|+\lambda\) bound is valid. A handpicked 433-state shell is **not** the complete electric projector \(P_M\): its complementary lower-energy bound cannot be replaced by \(M\) without proof. No such invalid substitution is made here.

**Practical accuracy warning.** The sharp indicator requires resolving a positive energy difference of order \(\lambda h^{3/2}\). The convolution source below requires a difference of order \(\lambda h^3\). Either can be much smaller than the individual \(O(h^{-1})\) background ground energies. ES4 avoids an excited-state gap but still requires a highly precise, *differential* energy enclosure; large global Wilson off-block norms may make the naive Schur correction ineffective.

## 3. Theorem ES-3 — exact center-even SU(2) free-rotor cap certificate

For a rigorous model check, take a **free deleted-face SU(2) rotor**, \(H_0=A(-\Delta)\) on \(L^2(SU(2))\), with center symmetry \(U\mapsto-U\). On the even sector, the constant normalized ground state is the rank-one projector \(P=|1\rangle\langle1|\); the *first excited even* SU(2) representation is spin one, with gap \(M=2A\) (the spin-half mode is odd and irrelevant). Take \(K=\mathbf1_{B_h^+\cup B_h^-}\). Define

\[
\mu=\langle1,K1\rangle=2m_H(h),\quad
\lambda=M/4,\quad
e_\lambda=\lambda\mu,\quad
q_\lambda=M,\quad
\rho_\lambda^2=\lambda^2\|QK1\|^2=\lambda^2\mu(1-\mu).
\]

These are **exact** rank-one identities, not numerical approximation. Substituting into ES5 gives

\[
L_\lambda\ge\lambda\mu\left[1-\frac{\lambda(1-\mu)}{M-\lambda\mu}\right]
=\lambda\mu\frac{M-\lambda}{M-\lambda\mu}
\ge\frac34\lambda\mu.
\]

Here \(E_0=0\) exactly. Hence for **every** \(0<h<1\),

\[
\boxed{\Pr_{\Omega_0}(B_h^+)\ge\frac{L_\lambda}{2\lambda}\ge\frac34m_H(h).}\tag{ES7}
\]

The actual free rotor vacuum is Haar and the true cap probability equals \(m_H(h)\), but **ES7 derives a nontrivial Haar-order bound solely from two ground-energy enclosures and a source block variance**. No computed eigenvectors or spectral isolation of a perturbed ground state are used. The independent numerical check diagonalizes the 46-character **even** rotor matrix with exact analytically integrated source matrix elements and verifies the enclosure.

## 4. Theorem ES-4 — narrow convolution source and a nontrivial 1/8 Haar limit

Let \(a\in(0,\pi/2)\), take the central nonnegative function \(\phi_a(U)=\mathbf1_{\{\theta(U)\le a/2\}}\), and define the central positive convolution \(k_a=\phi_a*\phi_a^\vee\). Put

\[
\alpha_a=\int\phi_a\,dU=m_H(1-\cos(a/2)),\qquad
\nu_a=k_a(I)=\int\phi_a^2\,dU=\alpha_a.
\]

Triangle inequality for the bi-invariant SU(2) geodesic distance gives \(0\le k_a(U)\le\alpha_a\mathbf1_{\{\theta(U)\le a\}}\). The even source \(K_a=k_a^+=[k_a(U)+k_a(-U)]/2\) satisfies \(\int K_a=\alpha_a^2\), \(\|K_a\|_\infty\le\alpha_a/2\) because the two support caps are disjoint, and

\[
\|QK_a1\|^2=\operatorname{Var}_{\rm Haar}(K_a)\le (\alpha_a/2)\alpha_a^2.
\]

The free even rotor, rank-one ES5, and \(\lambda=M/4\) prove

\[
\boxed{\Pr_{\Omega_0}(B_a^+)\ge
\alpha_a\left[1-\frac{\lambda\alpha_a/2}{M-\lambda\alpha_a^2}\right].}\tag{ES8}
\]

Since \(\alpha_a/m_H(1-\cos a)\to1/8\) as \(a\downarrow0\), this gives an explicitly verified **nonzero Haar-order cap constant**:

\[
\boxed{\liminf_{a\downarrow0}\frac{\text{certified bound in ES8}}{\Pr_{\rm Haar}(B_a^+)}\ge\frac18.}\tag{ES9}
\]

In contrast with a sharp indicator, the narrow convolution source has small operator norm \(O(a^3)\), and its positive-source Schur correction is a smaller *fraction* of the desired \(O(a^6)\) energy shift. For the free rotor, the bound approaches its natural source-calibrated constant. For the **connected** magnetic-deleted Wilson theory no analogous control of the background Wilson off-block coupling has been established.

## 5. What this changes about the outstanding proof gate

The previous certified Ritz-wavefunction route required both a true full-Hilbert excitation separation \(d_h\) and relative residual \(r_h/d_h=o(h^{3/4})\) to transfer a Haar-order cap. The new alternative is:

1. Build a center-even, complete-electric-cutoff **ground-energy upper enclosure** \(U_0\) for the actual connected deleted Hamiltonian.
2. Insert either the positive two-cap indicator or a smooth convolution source, and compute the lowest **projected energy** with a validated lower enclosure \(e_\lambda\).
3. Prove a complement energy lower bound \(q_\lambda\) and an off-block norm upper bound \(\rho_\lambda\) that make \(L_\lambda-U_0\) positive at the appropriate cap scale.
4. Check ES6 (or directly ES4). The result would be a **true-vacuum cap theorem without proving any physical excited-state gap**. Uniformity across asymmetric Penrose patches would still require additional work.

An equivalent (infinitesimal) description follows from Hellmann–Feynman, \(E_h'(0)=2\Pr_{\Omega_h}(B_h^+)\). ES1 is its finite positive-coupling secant, with the correct concavity inequality. This connects directly to the true-vacuum ground-state-selection and signed-radial-current programs, but **does not supply the still-open uniform current bound**.

**Proved:** ES1–ES9 with the assumptions displayed, including the explicit SU(2) rotor certificates. **Open:** the quantitatively useful \(E_h(\lambda)-E_h(0)\) lower bound for the actual asymmetric connected eight-face or growing Penrose system; full nonlinear bulk magnetic deletion, fixed-support connected Wilson–angle covariance, regulator-uniform mass gap, quartic resolvent and continuum reconstruction.
