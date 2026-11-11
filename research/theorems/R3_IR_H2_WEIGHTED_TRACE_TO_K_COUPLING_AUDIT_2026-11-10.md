# R3_IR — H2-weighted trace-to-K coupling calculation and audit

**Date:** 2026-11-10  
**Status:** provisional local calculation; incidence/curvature audit required before theorem-level use.  
**Route:** finite open SU(2) strip only. Separate from PF-I16. This record does not close the weighted Hessian evolution or any continuum proof gate.

## 1. Scope and norm convention

Use the H2 link weights
\[
w_e=(6/5)^{2d(e,\mathcal S)}
\]
and the one-output-weight Hessian norm
\[
\|H\|_{2,w,\mathrm{out}}^2
=\sum_{e,a}w_e\sum_{d,b}|H_{(e,a)(d,b)}|^2.
\]
The input gradient norm is
\[
\|V\|_{1,w}^2=\sum_{e,a}w_e|V_{e,a}|^2.
\]
Only the first Hessian link index is weighted. The second output link index is an internal block coordinate, not an additional factor of \(w_d\).

Write the pure-trace Hessian as
\[
T_{(e,a)(e,b)}=\tau_e\delta_{ab},\qquad
T_{(e,a)(d,b)}=0\quad(e\ne d),
\]
so that
\[
\|T\|_{2,w}^2=3\sum_e w_e|\tau_e|^2.
\]

The local isolated-dressing bounds used in the preceding R3_IR calculation are
\[
\|s_g'\|_\infty<0.000333528,\quad
\|s_g''\|_\infty<1.94619\times10^{-7},\quad
\|s_g'''\|_\infty<1.744\times10^{-10}.
\]
For one plaquette contribution, the local Hessian chain rule gives the component envelope
\[
h:=\frac14\|s_g''\|_\infty+\frac12\|s_g'\|_\infty
<0.00016681265475.
\]
At most two strip faces meet a given link pair, so the corresponding component envelope for \(\nabla^2S_g\) is \(2h\).

## 2. Candidate trace-to-K Hessian block

The Hessian-of-dressing part of the ordered drift commutator is
\[
\mathcal D_S^{(2)}(T)_{ij}
=2(\nabla_i\nabla^kS_g)T_{jk}
 +2(\nabla_j\nabla^kS_g)T_{ik}.
\]
With the pure-trace form above, the component identity is
\[
\mathcal D_S^{(2)}(T)_{(e,a)(d,b)}
=2(\tau_e+\tau_d)(\nabla^2S_g)_{(e,a)(d,b)}.
\]
A preliminary strip-incidence count gives a row-sum envelope \(8h\) and a column-sum envelope \(576h\) for the map from \(\tau\) to ordered Hessian entries. For a nonzero entry, the output link and trace-input link lie in a common plaquette, so
\[
\sqrt{w_{\rm out}/w_{\rm in}}\le6/5.
\]
Applying the Schur estimate and converting \(\|\tau\|_{2,w}\) to \(\|T\|_{2,w}=\sqrt3\|\tau\|_{2,w}\) gives the **candidate** bound
\[
\|P_K\mathcal D_S^{(2)}(T)\|_{2,w,\mathrm{out}}
\le C_{TK}^{\rm cand}\|T\|_{2,w},
\]
\[
C_{TK}^{\rm cand}
=\frac65\frac{\sqrt{(8h)(576h)}}{\sqrt3}
<0.007845234.
\]
The projection \(P_K\) is contractive in this one-output-weight norm under the stated blockwise trace/trace-free decomposition.

**Audit status:** the displayed algebra and local weight ratio are explicit, but the row/column incidence count must be checked against the exact ordered-index support of the strip tensor before this constant is promoted to a certified bound. In particular, the count must distinguish coincident links, adjacent links, and the diagonal trace projection without double-counting or omitting face incidences.

## 3. Gradient forcing: previously recorded coefficient and curvature caveat

The archived ordered third-dressing tensor calculation gives
\[
\|P_K\mathcal D_S^{(3)}(\nabla f)\|_{2,w,\mathrm{out}}
\le0.049941328\|\nabla f\|_{1,w},
\]
where the factor two from the drift commutator is included.

The ordered derivative commutator
\[
2(\nabla^kS_g)
(\nabla_i\nabla_j\nabla_kf-\nabla_k\nabla_i\nabla_jf)
\]
is a curvature term and cannot be set to zero. A preliminary estimate used \(\kappa=1/4\) and
\[
\|\nabla_eS_g\|\le\sqrt3\|s_g'\|_\infty
\]
to propose an additional coefficient
\[
C_{\rm curv}^{\rm cand}
=2\kappa\sqrt3\|s_g'\|_\infty
<0.000288844.
\]
This estimate is **not yet certified**: the precise Riemann contraction, symmetrization, trace-free projection, and block operator norm must be written in the chosen left-invariant frame. Therefore the sum
\[
0.049941328+0.000288844=0.050230172
\]
is a provisional bookkeeping value, not an established forcing constant. The only currently retained coefficient from the preceding certified tensor estimate is \(0.049941328\), subject to the scope of its archived certificate.

## 4. Three-sector diagnostic (conditional on the candidate constants)

The previously recorded conservative diagonal margins are
\[
a=0.0891819307400,\qquad
b=0.0465062876597,
\]
for gradient and trace, respectively. The mixed-block geometric damping lower bound is one in the stated radius-two SU(2) normalization.

If, and only if, both candidate coupling estimates above are independently verified, the displayed three-sector block would have the Schur diagnostic
\[
1-\frac{(0.050230172)^2}{4a}
 -\frac{(0.007845234)^2}{4b}
>0.992596.
\]
This is a diagnostic for the three displayed sectors, not a full energy inequality. It omits the \(K\)-to-\(K\) Hessian-of-dressing terms and the curvature commutator with \(H=K\). It cannot establish a full Hessian contraction, an interacting spectral gap, or a continuum result.

## 5. Required next audits

1. Re-enumerate the exact ordered-index support for \(\mathcal D_S^{(2)}(T)\), including all coincident/adjacent link cases, and independently verify the Schur row and column sums.
2. Derive the curvature contraction in the fixed SU(2) frame, including signs, index order, symmetrization, and \(P_K\), then compute its weighted operator norm.
3. Bound \(P_K\mathcal D_S^{(2)}(K)\) and the ordered-curvature term with \(H=K\) in the same one-output-weight norm.
4. Only then assemble and test the complete coupled energy form.

No full weighted Hessian semigroup contraction, uniform interacting gap, 3D regulator transfer, continuum reconstruction, or Yang–Mills mass gap is claimed.
