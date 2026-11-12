# PF-I16 four-factor mixed covariant derivative: independent sign audit

**Date:** 2026-11-11  
**Scope:** finite SU(2)^4 group-product calculation on the authentic oriented four-link face word. This audit closes the algebraic sign/trivialization sub-obligation only. It does not close PF-I16's analytic, physical, or continuum gates.

## 1. Statement

Let
\[
H=x_1x_2x_3x_4,\qquad x_i=U_i^{\epsilon_i},\quad \epsilon_i\in\{\pm1\},
\]
and use original-link left-trivialized variations \(\dot U_i=U_i\xi_i\). Define
\[
X_i=\begin{cases}\xi_i,&\epsilon_i=+1,\\-\operatorname{Ad}_{U_i}\xi_i,&\epsilon_i=-1,\end{cases}
\quad T_i=x_{i+1}\cdots x_4,\quad
\eta_i=\operatorname{Ad}_{T_i^{-1}}X_i.
\]
Then \(H^{-1}\dot H=\sum_i\eta_i\). For distinct factor indices,
\[
D_i\eta_j=\begin{cases}0&i<j,\\-[\eta_i,\eta_j]&i>j.\end{cases}
\]
For the radius-two bi-invariant SU(2) metric, the target Levi-Civita connection in left trivialization is
\[
(\nabla_{\dot H}W)_{\rm left}=D_{\dot H}w+\tfrac12[\eta,w].
\]
Therefore
\[
\boxed{(\nabla dH)(X_i,Y_j)=
\begin{cases}
+\tfrac12[\eta_i(X_i),\eta_j(Y_j)]&i<j,\\
-\tfrac12[\eta_i(X_i),\eta_j(Y_j)]&i>j,\\
0&i=j.
\end{cases}}
\]
The sign is determined by the order of the factors in the chosen face word. Reversing the word reverses the corresponding ordering and must be handled by recomputing the indices, not by copying a sign.

## 2. Derivation

For \(i<j\), the suffix \(T_j\) contains only factors strictly after \(j\), so varying factor \(i\) does not change \(T_j\), nor \(X_j\); hence \(D_i\eta_j=0\). For \(i>j\), the suffix \(T_j\) contains \(x_i\). Under \(x_i(t)=x_i\exp(tX_i)\), differentiation of the inverse suffix conjugation gives \(D_i\eta_j=-[\eta_i,\eta_j]\). Adding the Levi-Civita connection term \(+\tfrac12[\eta_i,\eta_j]\) gives the two signs above. For \(i=j\), the map varying only \(x_i\) is a composition of left and right translations (and, for an inverse original link, inversion); these are isometries of the bi-invariant metric. Its covariant second derivative in the same factor is zero.

In the orthonormal radius-two basis \((\mathbf i,\mathbf j,\mathbf k)/2\), the structure constants are \([e_a,e_b]=\epsilon_{abc}e_c\). Thus \(\|[X,Y]\|\le\|X\|\|Y\|\), so the mixed geometric term is bounded by \(\tfrac12\|X_i\|\|Y_j\|\).

## 3. Independent numerical audit

The accompanying verifier uses unit-quaternion multiplication and adjoint action. It perturbs each original link by \(U_i\mapsto U_i\exp(t\xi_i)\), recomputes the oriented face factors and suffix-transported components, and compares finite differences with the predicted zero or negative-bracket derivative.

- All 16 orientation words \((\epsilon_1,\ldots,\epsilon_4)\) were tested.
- All 12 ordered distinct-factor pairs per word were tested.
- 20 independently sampled SU(2)^4 configurations were tested per case.
- Total: 3,840 finite-difference comparisons.
- Maximum absolute residual at step \(10^{-6}\): \(6.73\times10^{-5}\).
- Halving the step in a deterministic check reduced the residual from \(1.42\times10^{-4}\) to \(7.12\times10^{-5}\), consistent with first-order finite-difference error.

The computation is a regression check of the group-product derivative and orientation conversion. The covariant correction and final half-bracket are established analytically from the bi-invariant Levi-Civita connection; floating-point sampling is not used as their proof.

## 4. What this audit closes — and what it does not

**Closed:** the ordered suffix derivative, inverse-link left-trivialization conversion, and the \(+/-\tfrac12\) mixed covariant derivative signs for every orientation word in the four-factor face map.

**Not closed:** the isolated-face estimate \(\|\nabla s_f\|_\infty\le\beta_f\); the radial Hessian estimate's inherited hypothesis; pullback Hessian block constants after all metric scalings; derivative-flow and residual estimates; the fourth-order spatial tree estimate; all-orders activity summability; source-derived physical kinetic/time; a refining physical 3D regulator; continuum reconstruction; or a positive physical mass gap.

The product group is compact and the calculation is performed globally in quaternion coordinates. No polar-coordinate singularity or integration-by-parts boundary term is used in this audit. This removes a coordinate-regularization ambiguity from the mixed-derivative sign check, but does not validate the separate radial-rotor endpoint argument.

## 5. Reproduction

Run:

    python research/verification/verify_pf_i16_four_factor_mixed_derivative.py

Expected terminal output begins with:

    PASS: 3840 orientation/ordered-pair quaternion finite differences

The script uses only NumPy and a fixed seed. It is deterministic.
