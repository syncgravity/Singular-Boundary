# PF-I16 nilpotent projection: gluing and high-degree tests

**Date:** 2026-11-13  
**Status:** exact finite identities and executable algebra checks; weighted all-orders estimate OPEN  
**Parent route:** `PF_I16_NILPOTENT_ROW_PROJECTION_RESUMMATION_CANDIDATE_2026_11_13.md`

## 1. Two-link, two-row gluing identity

Let the two independent link processes be (e,f), and let the two row observables be
\[
A_1=X_1Y_1,\qquad A_2=X_2Y_2,
\]
where (X_i) belongs to link (e), (Y_i) to link (f), and the two link processes are independent (dependence between times/rows on the same link is allowed). Write
\[
\mu_{e,i}=\mathbb E X_i,\quad
c_e=\kappa_e(X_1,X_2),\qquad
\mu_{f,i}=\mathbb E Y_i,\quad
c_f=\kappa_f(Y_1,Y_2).
\]
Then
\[
\begin{aligned}
\kappa(A_1,A_2)
&=\mathbb E(X_1X_2)\mathbb E(Y_1Y_2)
 -\mu_{e,1}\mu_{f,1}\mu_{e,2}\mu_{f,2}\\
&=c_e c_f+c_e\mu_{f,1}\mu_{f,2}
 +\mu_{e,1}\mu_{e,2}c_f\\
&=c_e\,\mathbb E(Y_1Y_2)
 +\mu_{e,1}\mu_{e,2}c_f.
\end{aligned}
\tag{G2}
\]
This is the exact two-link gluing identity. Every term contains at least one same-link bridge cumulant. If the individual slot variables are centered, it reduces to
\[
\boxed{\kappa(A_1,A_2)=c_e c_f.}
\]
If each bridge obeys (|c_e|\le C_e e^{-\Delta_e|t_1-t_2|}) and similarly for (f), then the centered product is bounded by
\[
C_eC_f e^{-(\Delta_e+\Delta_f)|t_1-t_2|}
\le C_eC_f e^{-\Delta_*|t_1-t_2|},
\quad \Delta_*:=\min(\Delta_e,\Delta_f).
\]
Thus two bridges can be charged to one maximum-tree temporal factor; the extra decay is harmless. This is an exact two-row calculation, not yet a general interpolation/gluing lemma.

## 2. Nilpotent projection examples

For two rows and two links, the projected moment polynomial is
\[
F(z_1,z_2)=1+\mu_{A_1}z_1+\mu_{A_2}z_2
 +\mathbb E(A_1A_2)z_1z_2,
\quad z_i^2=0.
\]
Consequently
\[
[z_1z_2]\log F
=\mathbb E(A_1A_2)-\mathbb E(A_1)\mathbb E(A_2),
\]
and substituting the independent link moments gives (G2). This checks the order “multiply whole link moment objects, project to complete rows, then take the logarithm.”

A centered three-row path has links (e:{1,2}), (f:{2,3}), and
\[
A_1=X_1,\quad A_2=X_2Y_2,\quad A_3=Y_3.
\]
Assume each slot variable has zero mean and define (c_e=\mathbb E(X_1X_2)), (c_f=\mathbb E(Y_2Y_3)). All proper nonempty row-subset moments vanish, while
\[
\mathbb E(A_1A_2A_3)=c_ec_f.
\]
Hence (F=1+c_ec_f z_1z_2z_3) and
\[
[z_1z_2z_3]\log F=c_ec_f.
\]
This is the minimal path-gluing example: the global logarithm retains the connected path, and its two temporal bridges are bounded by the path's one maximum-tree weight.

For a centered four-row path with links (e_{12},e_{23},e_{34}), each link incident to its two endpoint rows, the same argument gives
\[
\kappa(A_1,A_2,A_3,A_4)
=c_{12}c_{23}c_{34}.
\]
The path is already a spanning tree. These path identities are exact for the stated centered slot model; they do not cover overlapping higher-order hyperedges or nonzero means.

## 3. High-degree shared-link test: pointwise factorial is unavoidable

Take one link incident to every row, (I_e=[r]), and let every row slot be the same bounded symmetric Rademacher variable (U\in\{-1,1\}). Then (A_i=U), and
\[
\kappa(A_1,\ldots,A_r)=\kappa_r(U)
=\left.\frac{d^r}{ds^r}\log\cosh s\right|_{s=0}.
\]
For even orders,
\[
\kappa_2=1,\quad \kappa_4=-2,\quad
\kappa_6=16,\quad \kappa_8=-272,\quad
\kappa_{10}=7936.
\]
The nearest complex singularities of \(\log\cosh s\) are at (s=\pm i\pi/2); its Taylor coefficients therefore have factorial asymptotics
\[
|\kappa_{2n}(U)|\sim 2(2n-1)!\left(\frac2\pi\right)^{2n}.
\]
In particular no uniform (C^r) pointwise bound can hold for all bounded slot observables, even before spatial summation. The (8r) incidence budget does not remove this one-hyperedge factorial.

This does **not** refute the time-integrated target. For a temporally mixing single-link process, use the available one-link estimate
\[
|\kappa_r(U(t_1),\ldots,U(t_r))|
\le (2e)^r r!\,e^{-\Delta(\max t_i-\min t_i)}
\]
(for the normalized bounded slots and (r\ge2)). For symmetric cumulants, the cube integral divided by (r!) is the ordered-simplex integral. The maximum-tree kernel gives
\[
\int_{0<t_1<\cdots<t_r<T}
e^{-\Delta(t_r-t_1)}d\mathbf t
\le T\Delta^{-(r-1)}.
\]
Therefore
\[
\left|\frac1{r!}\int_{[0,T]^r}
\kappa_r(U(t_1),\ldots,U(t_r))d\mathbf t\right|
\le T(2e)^r\Delta^{-(r-1)}.
\]
This is precisely exponential-in-order growth after Feynman–Kac normalization, for the one-link test. It uses the time-integrated estimate and the existing one-link temporal cumulant bound; it is not yet proved for the multi-link projected logarithm after spatial/support summation.

## 4. Consequence for the proposed proof route

1. Retire the universal pointwise target (2a) for this observable class. A pointwise (C^r r!) maximum-tree estimate is compatible with the one-link stress test, but it only becomes useful after integration and the exact (1/r!) Feynman–Kac normalization.
2. Make the direct integrated coefficient estimate (2b) the primary target.
3. The two-link calculation supports a bridge-gluing principle in centered low-degree cases. A general lemma must control nonzero means, hyperedge incidence, and the projected logarithm without expanding the link moment objects into absolute LS partition summands.
4. The next real obstruction is a uniform integrated connected-log estimate for multiple links, not the finite nilpotent identity itself.

**Boundary:** all identities and Rademacher cumulants above are finite exact calculations. The one-link integrated estimate follows from the stated one-link temporal cumulant estimate and ordered-simplex integral. The multi-link integrated estimate, uniform spatial/support sums, physical Feynman–Kac normalization for the actual interaction, and P2/P3 vacuum inequality remain OPEN. No P0–P5 gate is promoted.
