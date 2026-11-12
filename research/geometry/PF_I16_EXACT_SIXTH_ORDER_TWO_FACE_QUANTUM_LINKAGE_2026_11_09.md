# PF-I16 — Exact sixth-order quantum linkage on two authentic shared-link source rhombi

**November 9, 2026 · finite auxiliary SU(2) Hamiltonian theorem.** Original accepted PF-I11/PF-I16 face geometry; seven original edges and two genuine rhombi sharing precisely one link. Source's center-sign duality as previously proved by free-face collapses. Unit electric coefficients are **chosen auxiliary**, not a physical time/kinetic normalization. Full rational derivation, executable independent finite-polynomial spectral verification, log and SHA-256 manifest in Library: \`/The Singular Boundary/Proof Audits/PF_I16_SIXTH_ORDER_2026_11_09.zip\`.

## Main theorem: mixed sixth-order coefficient

For centered Gauss-invariant \(H(b,c)=K-bp_f-cp_g\), its simple vacuum energy is analytic near \((0,0)\), separately even in b and c. Its exact Taylor polynomial through total degree six is
\[
\boxed{\begin{aligned}
E_0(b,c)
={}&-\frac{b^2+c^2}{12}+\frac5{3456}(b^4+c^4)
-\frac{b^2c^2}{8424}\\
&-\frac{289}{4976640}(b^6+c^6)
+\frac{22285}{3027787776}(b^4c^2+b^2c^4)
+O((|b|+|c|)^8).
\end{aligned}}
\]
**NEW:** the exact sixth-order linked coefficient is \(C_{4,2}=C_{2,4}=22285/3027787776\approx7.360159181777475\times10^{-6}>0\), opposite the earlier fourth-order linked \(C_{2,2}=-1/8424<0\). This is coefficient-level cancellation, *not* convergence or a physical mass.

## Exact SU(2) invariant-polynomial proof

Fix a spanning tree of the actual seven original source edges. The gauge quotient has two based loop holonomies U,V modulo diagonal conjugation. Define \(x=\frac12\mathrm{Tr}U\), \(y=\frac12\mathrm{Tr}V\), \(z=\frac12\mathrm{Tr}(UV)\). The original-link unit electric Casimir satisfies
\[
Kx=3x,\quad Ky=3y,\quad Kz=\tfrac92z.
\]
Its positive carré-du-champ tensor on the invariant polynomial algebra is
\[
\Gamma(x,x)=1-x^2,\ \Gamma(y,y)=1-y^2,\ \Gamma(z,z)=\tfrac32(1-z^2),
\]
\[
\Gamma(x,y)=\tfrac14(z-xy),\quad
\Gamma(x,z)=\tfrac34(y-xz),\quad
\Gamma(y,z)=\tfrac34(x-yz).
\]
Then \(K(FG)=F\,KG+G\,KF-2\Gamma(F,G)\); in particular \(K(xy)=\frac{13}2xy-\frac12z\), reproducing shared-link singlet/triplet energies \(9/2\) and \(13/2\). The Haar law is pushforward of independent SU(2) unit quaternions U and V; exact rational moments are obtained from \(z=U_0V_0-\sum_{i=1}^3U_iV_i\) and spherical coordinate moments \(\mathbb E\prod U_i^{2k_i}=\prod(1/2)_{k_i}/(2)_{\sum k_i}\).

Write \(\psi=1+\sum_{n\ge1}\psi_n\) normalized to Haar mean 1, and \(E=\sum_nE_n\), graded by total b,c degree. The exact recursion
\[
K\psi_n=(bx+cy)\psi_{n-1}+\sum_{k=2}^{n}E_k\psi_{n-k},\quad
E_n=-\langle(bx+cy)\psi_{n-1}\rangle_{\rm Haar}
\]
closes in a 50-monomial invariant-polynomial space of weighted degree ≤6, with weights deg(x)=deg(y)=1, deg(z)=2. Every Poisson equation and Haar-centering condition was verified in exact sympy rational arithmetic.

**Independent numerical test:** the same 50-dimensional polynomial basis was used to assemble a *separate generalized Hermitian eigenvalue problem* with exact-Haar Gram matrix and electric and Wilson multiplication quadratic forms; for \((b,c)=(.2,.11),(.15,.07),(.1,.05),(.07,.03)\), differences from sixth-order Taylor polynomial were \(7.15\times10^{-12},7.29\times10^{-13},2.79\times10^{-14},1.36\times10^{-15}\), consistent with eighth-order corrections. This numerical check is independent from the coefficient recursion but uses the same exact operator representation, not an independent replay of the full 8-size source vacuum.

## Three-face gate, explicitly not yet computed

Independent face-sign duality implies the **first allowed** ground-energy monomial involving all three of any three faces is \(b_f^2b_g^2b_h^2\), at degree six. If their original-link overlap support splits into separate components, the Hamiltonian is a tensor sum and its connected coefficient is exactly zero. An authenticated three-rhombus overlap chain is connected, so a coefficient is **allowed** but *not proved nonzero or assigned a sign here*. Determining that exact value on both the authenticated trivalent and four-valent variants is the next concrete objective; do not infer it from the two-face sixth-order values.

**OPEN:** three-face linked degree-six coefficient; all-order uniform cluster amplitude summability; uniform interacting Poincaré gap; source-derived time/kinetic choice, OS/continuum reconstruction; physical 4D Yang–Mills mass gap. Historical source bytes, main branch, and Observatory certified status unchanged.