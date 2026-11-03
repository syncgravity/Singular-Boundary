# Exact energy-weighted SU(2) Wilson-character fusion on arbitrarily long connected loops

**The Singular Boundary — original-link physical free-electric audit — November 3, 2026**

## Mathematical verdict

An exact, non-asymptotic energy-weighted fusion formula is available for **two SU(2) characters of the same simple original-link Wilson loop**, no matter how many elementary faces the loop surrounds. In this subalgebra the physical Poisson response has at most `min(a,b)+1` character channels, **without exponential growth in loop perimeter**. However, for equal high-spin characters the output coefficient mass grows **quadratically in representation degree**. Thus the width factor in the previous general finite-cutoff majorant is crude in this special family, but the derivative-degree cost is real. No all-width bound for arbitrary connected spin-network pairs is inferred.

## 1. Setup and orthonormality

Let `G` be a finite planar square-ladder original-link graph and let `C` be a non-self-intersecting closed edge path using `ell` distinct original links, once each, with `ell>=4`. For a connected interval of `t` square plaquettes, the exterior rectangular boundary is an example, with `ell=2(t+1)`. Let `W_C` be the ordered SU(2) holonomy around `C` and `chi_n(W_C)=tr_{n/2}(W_C)` the SU(2) character (`chi_0=1`, `chi_1` fundamental trace).

Original-link Haar integration makes `W_C` Haar distributed. Consequently, the family `{chi_n(W_C):n>=0}` is an orthonormal set of **physical gauge-invariant original-link spin networks**. Each of the `ell` traversed original links carries representation `n/2`, its vertex contraction is the canonical normalized 2-valent invariant, and its total free-electric energy is

\[
E_n=\ell\,\frac{n(n+2)}4,
\qquad K_{\rm phys}\chi_n(W_C)=E_n\chi_n(W_C).
\tag{1}
\]

These are exact original-link statements and are not obtained by replacing the physical kinetic operator with an invalid nearest-neighbor loop-coordinate approximation.

## 2. Complete energy-weighted fusion theorem

The SU(2) Clebsch–Gordan character identity gives

\[
\chi_a(W_C)\chi_b(W_C)=
\sum_{c=|a-b|,\ |a-b|+2,\ldots,a+b}\chi_c(W_C).
\tag{2}
\]

For the original-link positive electric Laplacian `K`, let

\[
\Gamma_K(f,g)=\tfrac12(fKg+gKf-K(fg)),
\qquad \mathcal B(f,g)=K^{-1}Q\Gamma_K(f,g),
\]

with `Q` deleting the constant eigenspace. Applying (1) term by term to (2) yields the **complete exact response**

\[
\boxed{
\mathcal B(\chi_a(W_C),\chi_b(W_C))
=\sum_{\substack{c=|a-b|,\ |a-b|+2,\ldots,a+b\\c>0}}
\underbrace{\frac{a(a+2)+b(b+2)-c(c+2)}{2c(c+2)}}_{q_{a,b;c}}
\chi_c(W_C).}
\tag{3}
\]

The `c=0` component is omitted because of centering. **Every `ell` cancels**, including when the perimeter becomes arbitrarily long. All channels are original-link physical energy eigenfunctions with the *same* connected original-edge support. The exact unweighted canonical SN coefficient mass is

\[
\boxed{\|\mathcal B(\chi_a,\chi_b)\|_{{\rm SN},1}
=\sum_{\substack{c=|a-b|,\ |a-b|+2,\ldots,a+b\\c>0}}|q_{a,b;c}|.}
\tag{4}
\]

The number of nonconstant channels is no greater than `min(a,b)+1`; it is independent of the support width `t`. For `a,b>=0`, a safe **perimeter-uniform degree bound** follows directly from the triangle inequality:

\[
\boxed{\|\mathcal B(\chi_a,\chi_b)\|_{{\rm SN},1}
\le\frac{a(a+2)+b(b+2)}4+\frac{\min(a,b)+1}2.}
\tag{5}
\]

Indeed `|q| <= [a(a+2)+b(b+2)]/[2c(c+2)]+1/2`; sum the reciprocal factors over a single parity class using `sum_{c>=1,c odd}1/[c(c+2)]=1/2`, `sum_{c>=2,c even}1/[c(c+2)]=1/4`, and count at most `min(a,b)+1` channels. This bound is intentionally coarse and includes the trivial-spin case, where the actual response vanishes.

## 3. Exact two-channel and high-spin examples

For fundamental inputs `a=b=1`, the product is `chi_0+chi_2`. The centered vacuum term is removed, leaving

\[
\boxed{\mathcal B(\chi_1(W_C),\chi_1(W_C))=-\frac18\chi_2(W_C)}.
\tag{6}
\]

Hence its unweighted original-link spin-network coefficient norm is exactly `1/8` at every connected perimeter, with no dimension-factor growth.

For unequal inputs `a=1`, `b=m>=2`, only two channels occur:

\[
\boxed{\mathcal B(\chi_1,\chi_m)
=-\frac{m}{(m+1)(m+3)}\chi_{m+1}
+\frac{m+2}{(m-1)(m+1)}\chi_{m-1}.}
\tag{7}
\]

Its coefficient mass is `O(1/m)` as `m→∞`, uniformly in loop perimeter.

For equal inputs `a=b=m>=1`, each nonconstant output index is `c=2k` for `k=1,...,m`, and (3) becomes

\[
\boxed{q_{m,m;2k}=\frac{m(m+2)}{4k(k+1)}-\frac12.}
\tag{8}
\]

In particular, the low-spin `chi_2` output coefficient is

\[
\boxed{q_{m,m;2}=\frac{m(m+2)-4}{8}.}
\tag{9}
\]

For `m>=2`, this gives the exact lower bound

\[
\frac{m(m+2)-4}{8}\le
\|\mathcal B(\chi_m,\chi_m)\|_{{\rm SN},1}.
\tag{10}
\]

The triangle inequality and telescoping reciprocal sum give

\[
\boxed{\|\mathcal B(\chi_m,\chi_m)\|_{{\rm SN},1}
\le\frac{m(m+2)}4+\frac m2.}
\tag{11}
\]

Moreover, the *signed* sum of (8) differs from its absolute sum by at most `m`, since the magnitude of each negative term is at most `1/2`. The signed sum is `m(m+2)/4 * m/(m+1)-m/2 = m^2/4+O(m)`. Thus

\[
\boxed{\lim_{m\to\infty}m^{-2}
\|\mathcal B(\chi_m,\chi_m)\|_{{\rm SN},1}=\frac14.}
\tag{12}
\]

This is a **real quadratic degree obstruction** to a same-unweighted-coefficient-norm bilinear estimate even on a single fixed connected original-edge loop. It does not preclude stronger analytic-radius-weighted or degree-graded estimates.

## 4. Consequence for connected-polymer regularity

Fix a single connected plaquette interval (hence fixed perimeter `ell`) and put `F_m=chi_m(W_C)` into a polymer assigned to that interval. Consider a polynomial degree weight `(1+N)^s`, `N=ell*n`, with no exponential spin weight (`sigma=0`). Normalize `F_m` by its weighted norm, which scales as `(1+ell*m)^s`. The `chi_2` coefficient of `B(F_m,F_m)` is `~m²/8`, while its output weight `(1+2ell)^s` is independent of `m`.

The same-grade bilinear ratio therefore grows as `m^{2-2s}` for `s<1`. Hence **at zero analytic exponent, a fixed same-grade bilinear estimate cannot hold for `s<1`**, even for one fixed connected loop. This does not establish sufficiency at `s=1`; it only proves that a degree budget is necessary. With positive exponential spin weight `sigma>0`, the two normalized high-spin inputs generate exponentially small low-spin output, so this particular obstruction does not transfer unchanged.

The earlier disconnected-channel exponential example and the present connected single-loop quadratic example are complementary: the former shows disconnected multiplicity growth; this one shows a **connected, fixed-support degree cost** with no perimeter penalty.

## 5. Scope, reproducibility and next task

The theorem is an exact special-family, full-length **physical** character recoupling identity. It is not an all-width bound for arbitrary connected original-link spin networks, where local intertwiner multiplicities, crossings, and overlapping distinct paths contribute new channels. It does not prove closed nonlinear polymer iteration. The correct next test is **two distinct overlapping simple Wilson loops** with a fixed finite spin cutoff, tracing their exact SU(2) crossing/recoupling coefficients and electric-energy denominators. Their local overlap geometry, rather than the full ambient Peter–Weyl dimension, should determine the constants.

`verify_connected_wilson_character_poisson_fusion.py` performs exact rational checks of perimeter cancellation and all channel formulas for `t=1,2,3,4,7,13,31,101`, `0<=a,b<=50`, high-spin `m<=500`, and the upper and lower equal-spin bounds. The passing log records **65,927 assertions**. These finite checks corroborate, but do not replace, the SU(2) character and electric-eigenvalue proofs above. The Markdown proof, standalone checker, execution log, and SHA-256 manifest accompany the audit.

**No interacting `lambda=1` thermodynamic spectral gap or continuum four-dimensional SU(2) Yang–Mills mass gap has been proved.**