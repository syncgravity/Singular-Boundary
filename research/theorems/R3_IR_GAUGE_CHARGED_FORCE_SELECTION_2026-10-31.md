# R3-IR — Gauge-charge selection of the Wilson-force Green–Kubo tail

**Date:** 2026-10-31. **Status:** exact finite-volume Wilson-Hamiltonian representation theorem and sharp abstract adjoint-sector spectral obstruction. **Not** a regulator-uniform spectral estimate, a physical charge-sector gap, or continuum mass gap.

## Setup
On the complete product-link Hilbert space \(\mathcal H=L^2(SU(2)^E,d\mu)\) take the deleted-face Hamiltonian \(H_f^-=\sum_e a_e(-\Delta_e)+\sum_{g\ne f} b_g(1-p_g)\), with its unique normalized strictly positive Gauss-invariant eigenfunction \(\Omega\) and energy \(E_0\). Write \(A=H_f^--E_0\ge0\). Choose a *directed* original link \(e\) whose source vertex is \(v\), and let \(X_{e,a}\) differentiate **left multiplication** of \(U_e\) by \(\exp(ti\sigma_a/2)\). Set \(w_a=X_{e,a}\Omega\), \(F_a=(X_{e,a}V_-)\Omega\), and \(\phi_a=X_{e,a}V_-\). The derivative force identity is \(Aw_a=-F_a\). All derivatives are taken before gauge reduction.

## Theorem GC-1: local vertex adjoint selection rule
Let \(\mathscr U_v(g)\) be the unitary action on link functions induced by the SU(2) gauge transformation at source vertex \(v\), with a conventional pullback orientation. Since \(H_f^-\), \(V_-\) and \(\Omega\) are gauge invariant, and the left-invariant link generators transform among themselves by \(\operatorname{Ad}_g\), the triples \((w_a)\) and \((F_a)\) transform as the spin-one adjoint representation at \(v\). Each \(w_a\) and \(F_a\) is invariant under gauge actions at other vertices (as a function of the full configuration) and belongs to the **isotypic spin-one subspace** \(\mathcal H_{v,1}\) for the action at \(v\). In particular, the local gauge-singlet projector \(P_{v,0}=\int_{SU(2)}\mathscr U_v(g)dg\) annihilates each component:

\[
P_{v,0}w_a=P_{v,0}F_a=0.
\]

This is an **operator-sector** selection statement, stronger than a zero conditional mean of Cartesian force components. Because \([A,\mathscr U_v(g)]=0\), the spectral resolution \(E_A(B)\), the semigroup \(e^{-tA}\), and the force's Green–Kubo spectral measure all remain in \(\mathcal H_{v,1}\). Thus the correlation
\[
C_e(t)=\sum_{a=1}^3 \langle F_a,e^{-tA}F_a\rangle
\]
is supported in gauge-**charged**, not gauge-invariant, excitation sectors. Scalar physical soft modes \(\mathcal H_{\mathrm{Gauss}}\) make exactly zero contribution. This does not mean \(F_a\) is itself a physical Gauss-invariant excitation, nor imply a positive charged-sector excitation threshold independent of graph refinement.

**Proof.** Gauge covariance of a left Lie derivative follows from \(g\exp(tT_a)=\exp(t\operatorname{Ad}_g T_a)g\) applied to a gauge-invariant function. SU(2) Haar group averaging annihilates the nontrivial adjoint representation (its invariant vector space is zero). Commutation of \(A\) with each vertex gauge unitary permits the same projection before or after any spectral function of \(A\). QED.

## Theorem GC-2: the three-moment no-go survives exact adjoint symmetry
The previous two-energy spectral counterfamily can be made exactly local-SU(2)-covariant. Take the abstract charged space \(\mathcal K=(\mathbb C^3)\oplus(\mathbb C^3)\), with local vertex SU(2) acting as \(R(g)\oplus R(g)\), and the positive, equivariant operator \(A_\epsilon=\epsilon I_3\oplus\lambda_\epsilon I_3\). With \(q_\epsilon,\lambda_\epsilon\) as in `R3_IR_WILSON_FORCE_THREE_MOMENT_NO_GO_2026-10-31.md`, take force vectors \(F_a=\sqrt{c q_\epsilon/3}\,e_a\oplus\sqrt{c(1-q_\epsilon)/3}\,e_a\) (with identical amplitudes for each component). The factor \(1/3\) makes the sum of squared spectral weights equal \(c\). Then
\[
\sum_a\langle F_a,e^{-tA_\epsilon}F_a\rangle=c[q_\epsilon e^{-\epsilon t}+(1-q_\epsilon)e^{-\lambda_\epsilon t}],
\]
so \(C(0)=c\), \(-C'(0)=d\), and \(\int C=s\) are fixed but \(\int tC\to\infty\) as \(\epsilon\downarrow0\), **despite every force vector being in an exact adjoint triplet and every spectral projection commuting with the SU(2) symmetry**.

**Scope:** GC-2 is an abstract isotypic spectral model, not a Wilson potential or ground state. It proves that the representation-selection theorem alone does not eliminate near-zero *charged* spectral weight. The further necessary physical estimate is a uniform bound on the **adjoint-sector** inverse-square force spectral moment (or a direct collar anti-depletion comparison). Neither follows from the local f-sums or gauge covariance.

## Numerical verification
`verify.py` checks 1000 noncommuting SU(2) conjugation configurations, the transformation of fundamental-link trace derivatives as an SO(3) adjoint vector, vector-norm invariance and trace invariance. The maximum covariance discrepancy was below \(1.8\times10^{-16}\). These tests are algebraic only. The abstract two-triplet spectral construction is exact by direct diagonal evaluation. No M55 interacting-vacuum spectrum or gauge-charged spectral gap was computed.

## Open obligations
1. A **physical charged-sector spectral estimate** or long-time force-correlation bound uniform in regulator and cage, without presupposing a positive uniform gap.
2. A conditional collar score comparison / anti-depletion inequality transferring such weighted dynamical information to the unweighted radial current.
3. The previously stated \(\sup_f\mathfrak T_{f,h}=o(h^{-1/4})\), connected covariance, continuum limit and Yang–Mills mass gap.