# R3-IR — Reflection-seam positive-cone theorem for fully connected SU(2) Wilson deletion

**Date:** 2026-10-29. **Classification:** full-coupling, exact finite physical SU(2) theorem under global reflection pairing. **Not claimed:** generic asymmetric Penrose interior, physical continuum mass gap, quartic resolvent, continuum reconstruction. The expanded standalone manuscript and deterministic verifier are in the companion archive \`singular_boundary_reflection_seam_cap_2026-10-29.zip\`; SHA256 \`636625ae4ddc816848346872825c674fb149e524e1ea6398e5735befe4f1df0c\`.

## Hypotheses

Take a finite face-complete planar rhombus complex with free boundary links and an involutive reflection \`r\` through a diagonal of a target face \`f\`. The reflection seam passes only through vertices, **no primal links**, so the two edge sets \`E_+\` and \`E_-\` are disjoint and matched. Every other plaquette is either paired with a distinct reflected plaquette on the opposite side or bisected into two open paths with the same seam-vertex endpoints. Electric link coefficients and paired magnetic face coefficients agree under reflection. All retained Wilson magnetic coefficients are nonnegative. Delete the target magnetic term, leaving
\[
H_f^-=\sum_e a_e(-\Delta_e)+\sum_{q\ne f}b_q[1-\tfrac12\operatorname{ReTr}W_q],\qquad b_q\ge0.
\]
Work in the **full product-link Hilbert space**; elliptic positivity improving makes its unique ground state strictly positive and automatically invariant under all vertex gauge transformations.

Identify both reflected halves with the same product Haar probability space \`X=SU(2)^{E_+}\`, with reflected edge orientation adjusted. The complete Hamiltonian acts on kernel wavefunctions \`\Psi(x,y)\` as
\[
H_f^-=A_x+A_y+\sum_{q\in F_{\times}}b_q\big[1-p(P_q(x)P_q(y)^{-1})\big],\quad p(U)=\tfrac12\operatorname{Tr}U,
\]
where \`A\` is the identical positive self-adjoint half-side electric-plus-within-side-magnetic operator, and \`P_q(x)\` are half-face open-path holonomies. For the target, \`W_f=P_f(x)P_f(y)^{-1}\` in character and trace. The coefficient of the target crossing potential is zero.

## RS-1 — Positive-type crossing plaquettes

For every irreducible SU(2) spin \`j\`, the kernel
\[
K_j(x,y)=\chi_j(P(x)P(y)^{-1})
=\sum_{a,b}D^j_{ab}(P(x))\overline{D^j_{ab}(P(y))}
\]
is positive semidefinite. The normalized fundamental trace \`p(P(x)P(y)^{-1})=\frac12K_{1/2}(x,y)\` is likewise positive semidefinite. Schur products preserve positive definiteness; therefore
\[
q_s(x,y)=\exp\{-s b[1-p(P(x)P(y)^{-1})]\}
\]
is positive definite for \`s,b\ge0\`: expand \`e^{sbp}\` into its uniformly convergent nonnegative power series. Products of crossing factors retain this property. No character-sign hypothesis is assumed.

## RS-2 — The *Hamiltonian ground state* is a positive Hilbert–Schmidt kernel

Identify \`L^2(X\times X)\` with Hilbert–Schmidt operators on \`L^2(X)\`, using the reflection identification. Let \`C\` be the closed cone of nonnegative self-adjoint Hilbert–Schmidt kernels. The half-side semigroup sends \`K\mapsto S_t K S_t\`, \`S_t=e^{-tA}\`, preserving \`C\`. Each crossing potential Trotter factor sends \`K(x,y)\mapsto q_s(x,y)K(x,y)\`, preserving \`C\` by the Schur-product theorem. The Trotter strong limit proves
\[
e^{-tH_f^-}C\subset C,\qquad t\ge0.
\]
The constant wavefunction \`1(x,y)\` is a rank-one positive kernel and has strictly positive overlap with the unique positive ground state. Consequently
\[
\Omega_f^-=\lim_{t\to\infty}\frac{e^{-tH_f^-}1}{\|e^{-tH_f^-}1\|_2}
\]
belongs to \`C\` by closedness. This is a **ground-state** result, not merely reflection positivity of a classical Gibbs measure.

## RS-3 — All Wilson-character expectations of the deleted face are nonnegative

The ground state is a real nonnegative smooth function of the link variables and, by RS-2, a positive integral kernel across the two halves. Its **pointwise** square \`R(x,y)=\Omega_f^-(x,y)^2\` is a positive kernel by the Schur-product theorem. The target character \`K_{j,f}(x,y)=\chi_j(P_f(x)P_f(y)^{-1})\` is positive definite by RS-1. Their Schur product is positive definite. Evaluating its positive quadratic form on the constant function proves
\[
\boxed{\langle\Omega_f^-,\chi_j(W_f)\Omega_f^-\rangle\ge0
\quad \text{for every }j\in\tfrac12\mathbb Z_{\ge0}.}
\]
Independent center-flux parity makes the half-odd-integer coefficients zero, but this is not required for their nonnegativity. The result holds at **arbitrary full positive retained Wilson coupling** satisfying the reflection conditions.

## RS-4 — Haar-order center cap and deletion estimate

Let \`B_a\` be the SU(2) angular ball of radius \`a<\pi/2\`. Set \`H(a)=(a-\frac12\sin(2a))/\pi\`. For \`q=1_{B_{a/2}}\` and \`k=q*q^\vee\`, the geodesic triangle inequality gives \`0\le k\le H(a/2)1_{B_a}\`; its character expansion has coefficients \`|\int q\chi_j|^2/(2j+1)\ge0\`. By RS-3,
\[
\boxed{\mathbb P_{\Omega_f^-}(W_f\in B_a)\ge H(a/2).}
\]
At the physical deficit \`d_f=1-p_f\le h\`, choose \`a_h=\arccos(1-h)\`. The exact lower bound is
\[
\boxed{\mathbb P_{\Omega_f^-}(d_f\le h)
\ge H(a_h/2)=\big(\sqrt2/(6\pi)+O(h)\big)h^{3/2}.}
\]
Under bounded electric coefficients and target magnetic coefficient \`b_f\asymp h^{-2}\`, the earlier exact positive-ground-state exponential-trial comparison yields
\[
\boxed{E_0(H_f^-+b_fd_f)-E_0(H_f^-)
\le C h^{-1}(1+\log(1/h)).}
\]
The constant depends on bounded coefficient ratios but **not on the number of reflection-paired retained magnetic faces**.

## RS-5 — Concrete connected geometries

For the complete 3×3 square-rhombus disk with central target \`(1,1)\`, reflection \`(x,y)\mapsto(y,x)\` runs along a diagonal through three face interiors and **no primal edges**. This is the previous nine-face connected obstruction, now resolved under reflection-paired coefficients. The four minimal connected eight-face patterns obtained by omitting one corner likewise have a diagonal reflection:
- Missing corner \`(0,0)\` or \`(2,2)\`: main diagonal.
- Missing corner \`(0,2)\` or \`(2,0)\`: anti-diagonal \`(x,y)\mapsto(3-y,3-x)\`.

Thus **all five** connected activation patterns have a polynomial deleted-center mass bound at full coupling on their reflection-symmetric coefficient subfamilies. Unlike the earlier open-arc theorem, the retained magnetic graph is connected and touches all four target sides. **Generic asymmetric coefficient assignments and Penrose interiors are not covered.**

## Verification and remaining proof priority

A deterministic Python regression checks positive-semidefinite SU(2) character Gram matrices at 12 noncommuting elements; positive-definite Wilson cross weights; finite Trotter preservation of the positive Hilbert–Schmidt cone; reflection-invariant incidence and absent seam edges in the five connected eight/nine-face patterns; and the precise SU(2) Haar center prefactor. This **does not** diagonalize a physical eight-face SU(2) Hamiltonian; the finite-volume result is analytic.

**Proved:** RS-1–RS-5 under explicit symmetry hypotheses. **Open:** model-specific signed connected response or comparable cap positivity without reflection pairing, uniformly for genuinely asymmetric Penrose interior faces; fixed-support nonlinear connected covariance, physical mass gap, quartic resolvent and continuum reconstruction.
