# R3-IR — Bounded-incidence extension of the sharpened analytic inputs

**Date:** 2026-11-11  
**Status:** conditional local-combinatorial extension; independent arithmetic verifier supplied.  
**Purpose:** test whether the sharpened weighted Bochner and conditional trace–Poincaré inputs are genuinely tied to the straight strip or extend to other finite plaquette complexes.

## 1. Model class and hypotheses

Let \(\mathcal C\) be a finite plaquette 2-complex with independent link variables \(U_e\in\mathrm{SU}(2)\), product radius-two bi-invariant metric, and dressed reference action
\[
S_g(U)=\sum_{f\in F}s_g(p_f(U)).
\]
Assume:

1. Every face contains exactly four distinct link variables, with an arbitrary fixed orientation pattern.
2. Every link belongs to at most \(r\) faces.
3. The link-distance graph joins two links whenever they occur in one common face; weights are \(w_e=\rho^{2d(e,\mathcal S)}\), \(\rho=6/5\).
4. The same isolated plaquette branch and uniform coefficient enclosure hold over the full plaquette range and \(|g|\le10^{-3}\):
   \[
   S_1=\|s_g'\|_\infty<0.000333528,\quad
   S_2=\|s_g''\|_\infty<1.94619\times10^{-7},\quad
   q=S_1+S_2<0.000333722619.
   \]
5. The local ordered plaquette component estimates remain valid for all orientation patterns:
   \[
   T_g<0.000250292,\qquad
   h<0.000166813,
   \]
   with the same definitions as the straight-strip source audit.

This is a product-link plaquette model. It does not assume a transfer matrix, a Hamiltonian continuum limit, or an interacting fixed point.

## 2. Degree-\(r\) replacements for the two analytic inputs

### Weighted Bochner

Each face contributes a \(4\times4\) link Hessian block matrix with per-face block operator bound \(q/4\). A fixed link has at most \(r\) incident faces and at most four link blocks per face. The weighted row/column Schur bound is therefore
\[
r\rho q.
\]
The pointwise weighted Bakry–Émery inequality becomes
\[
\boxed{c_r=\frac12-2r\rho q.}
\tag{2.1}
\]
For \(r=2\) this reproduces the sharpened strip value. It is positive throughout the degrees considered below.

### Conditional one-link Poincaré

The conditional score obeys
\[
B_r:=\|\nabla_eS_g\|_\infty
\le \frac r2S_1.
\]
Since the factor SU(2) diameter is \(2\pi\),
\[
\operatorname{osc}_{U_e}(2S_g)\le4\pi B_r.
\]
Holley–Stroock and the exact conditional-mean correction yield
\[
\boxed{
c_{{\rm tr},r}=\frac34e^{-4\pi B_r},\qquad
\ell_r=\frac{4c_{{\rm tr},r}}3B_r^2.
}
\tag{2.2}
\]
The conditional law remains the disintegration of the same global Gibbs measure.

## 3. Degree-\(r\) full-Hessian constants

A fixed ordered output pair is supported by at most \(r\) faces. Each face has 12 input link/Lie components. A fixed input component belongs to at most \(r\) faces, each with 144 ordered output components. Hence
\[
\text{row}\le12rT_g,\qquad
\text{column}\le144rT_g,
\]
and
\[
\boxed{C_{3,r}\le2\rho\sqrt{1728}\,rT_g.}
\tag{3.1}
\]

For \(A=\nabla^2S_g\), a fixed link has at most \(3r\) distinct neighboring links. A fixed link-pair block can receive at most \(r\) face contributions, so its \(3\times3\) Frobenius norm is at most \(3rh\). The weighted first-index and unweighted second-index row/column bounds are respectively
\[
3rh(1+3r\rho),\qquad3rh(1+3r).
\]
Therefore
\[
\boxed{
C_{H,r}\le6rh\,[2+3r(1+\rho)].
}
\tag{3.2}
\]
This deliberately allows all \(r\) incident faces to share the same link pair; a regular cubical complex may have a sharper pair-overlap count.

The symmetrized Codazzi term has the same exact SU(2) Frobenius factor \(\sqrt2\), so
\[
\boxed{
C_{R,r}\le2\kappa\sqrt2B_r,\qquad \kappa=\frac14.
}
\tag{3.3}
\]
Set \(C_{G,r}=C_{3,r}+C_{R,r}\). The same full-Hessian energy calculation then has
\[
a_r=c_r-\ell_r,\qquad
b_r=c_{{\rm tr},r}-C_{H,r},
\]
\[
Q_r=\begin{pmatrix}a_r&-C_{G,r}/2\\-C_{G,r}/2&b_r\end{pmatrix}.
\tag{3.4}
\]
Whenever \(Q_r\) is positive definite, the same finite-complex one-output weighted semigroup contraction follows.

## 4. Explicit degree-four check

For a standard open three-dimensional cubical plaquette complex, a link is incident to at most four plaquettes (\(r=4\)). Under the model-class hypotheses in §1, use the conservative rational ceilings
\[
S_1\le0.000333528,\quad S_2\le0.000000194619,\quad
T_g\le0.000250292,\quad h\le0.000166813.
\]
The independent arithmetic verifier gives
\[
\begin{aligned}
c_4&>0.4967962628,\\
B_4&\le0.000667056,\\
c_{{\rm tr},4}&>0.7437394215,\\
\ell_4&<4.413\times10^{-7},\\
C_{3,4}&<0.099882654,\\
C_{H,4}&<0.113699741,\\
C_{R,4}&<0.000471680,\\
C_{G,4}&<0.100354334.
\end{aligned}
\]
Consequently
\[
a_4>0.4967958216,\qquad
b_4>0.6300396807,\qquad
\boxed{\lambda_{\min}(Q_4)>0.4800.}
\]
Thus the two sharpened analytic inputs and the full-Hessian reference estimate are not intrinsically one-dimensional-strip statements: their local proof extends to bounded-incidence finite plaquette complexes, and the conservative degree-four bookkeeping still leaves a positive margin.

## 5. What this does and does not establish

**Established at the level of the stated local-combinatorial derivation:** the weighted Bochner and conditional one-link inequalities admit degree-\(r\) versions; for \(r=4\), the conservative full-Hessian quadratic form remains positive. The scalar coefficient enclosure, SU(2) local plaquette estimates, product metric, common Gibbs measure, and exact incidence bound are the dependencies.

**Not automatically established for a 3D regulator:** one must still verify that its actual variables and action are exactly a product of independent SU(2) link factors with a sum of four-distinct-link plaquette terms; that every link has incidence at most four; that the oriented face trace is the same isolated-dressing plaquette function; that no additional interactions, constraints, gauge fixing, boundary identifications, or non-product metric terms alter the local derivatives or measure; and that the intended weighted graph and boundary conditions match §1.

This is a finite-dimensional reference-measure derivative estimate. It is not a 3D transfer theorem, a Hamiltonian spectral-gap theorem, a physical-coupling result, a volume-uniform interacting residual estimate, or a continuum Yang–Mills mass-gap proof.

## 6. Three-sector route decision

The provisional three-sector trace-to-\(K\) calculation is not needed for this reference-semigroup extension either. The full-Hessian route retains the curvature damping of the mixed/trace-free blocks and uses the conditional Poincaré inequality only on the parallel trace component of the full tensor Dirichlet form. Keep the three-sector calculation dormant as a possible cross-check for a different norm or an interacting estimate; do not invest in closing it for the present bounded-incidence reference problem.
