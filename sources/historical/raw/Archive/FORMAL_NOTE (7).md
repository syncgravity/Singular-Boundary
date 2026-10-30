# Continuum-stable polymer expansion: geometric admission and activity gate

Date: 2026-10-26. **Status: partial mathematical results; complete Penrose SU(2) RG polymer expansion and R3/R2 are NOT proved.**

## Setup
Let the complete finite 2+1-dimensional spacetime SU(2) Wilson measure have action \(\sum_p\beta_p d_p\), \(d_p=1-\frac12\operatorname{Tr} W_p\in[0,2]\), with \(c_-\lambda\le\beta_p\le c_+\lambda\), \(\lambda=(g_3^2h)^{-1}\ge1\) and bounded plaquette adjacency degree \(\Delta\). A finite plaquette set \(X\) has incidence link set \(L(X)\) and touching exterior plaquettes \(Y(X)\). Take \(0<\vartheta<1\), \(t=\vartheta c_-\lambda\), and \(\delta=\lambda^{-1/2}\).

## Theorem 1: explicit bulk-boundary contour bound
The previously derived local conditional entropy argument, applied to all selective dilutions \(\beta_p-s1_X\), \(0\le s\le t\), yields, for constants \(K_1,K_2\) depending only on \(\vartheta,c_\pm\) and the bounded local geometry,
\[
\sum_{p\in X}\langle d_p\rangle_{\beta-s1_X}
\le K_1 |X|\frac{1+\log\lambda}{\lambda}+K_2 |Y(X)|.
\]
The exact exponential Markov/partition-ratio identity gives
\[
\mu_\beta(L_X(\delta))\le
\exp\{-t\delta |X|+t K_1 |X|(1+\log\lambda)/\lambda+t K_2|Y(X)|\}.
\]
Consequently
\[
\mu_\beta(L_X(\lambda^{-1/2}))\le
\exp\{[-\vartheta c_-\sqrt\lambda +\vartheta c_-K_1(1+\log\lambda)
+\vartheta c_-K_2\lambda r(X)]|X|\},\quad r(X)=|Y(X)|/|X|.
\]
If \(r(X)\le c_0/\sqrt\lambda\) and \(K_2c_0\le1/4\), then for sufficiently large \(\lambda\), the exponent is at most \(-\frac12\vartheta c_-\sqrt\lambda|X|\), uniformly in ambient volume. This includes regular blocks with \(r(X)\lesssim h/L\) at fixed physical \(L\), provided block regularity actually holds.

**Scope:** For thin connected \(X\), \(r(X)=O(1)\), this estimate is generally vacuous. Thus it is not an all-contour theorem.

## Theorem 2: convergence of a restricted abstract hard-core contour gas
Suppose a family \(\mathscr A_h\) of connected admissible plaquette sets is assigned activities \(w_h(X)\) such that
\(|w_h(X)|\le e^{-a_h|X|}\), \(a_h=c\sqrt\lambda\), and incompatible polymers share or neighbor plaquettes. If the adjacency graph has degree \(\Delta\), the number of connected size-\(n\) sets containing a fixed plaquette is bounded by \(A_\Delta^n\), with an explicit admissible loose constant \(A_\Delta=e(\Delta+1)\). For \(a_h>1+\log A_\Delta\),
\[
\sup_p\sum_{X\ni p}|w_h(X)| e^{|X|}
\le\frac{A_\Delta e^{1-a_h}}{1-A_\Delta e^{1-a_h}}.
\]
If the RHS is at most \(1/(\Delta+1)\), the Kotecky--Preiss condition with size weight \(a(X)=|X|\) follows (every incompatible \(Y\) touches one of at most \((\Delta+1)|X|\) sites neighboring \(X\)). The abstract cluster expansion of this **restricted contour gas** converges absolutely, with constants independent of volume.

**Crucial logical gap:** The event probabilities from Theorem 1 are NOT the polymer activities of an exact factorized contour gas for the Wilson measure. Theorem 2 must not be invoked on the actual Yang--Mills effective action without proving a contour representation/activity estimate, and must not be extrapolated to omitted thin contours. Probability bounds on all-large events alone do not produce analyticity or cancellation control of connected cumulants.

## Exact effective action and residual-activity criterion
For a spatial/temporal block, \(e^{-S_{\mathrm{eff}}(Y)}=\int e^{-S(X,Y)}dX\). Define an explicit local extraction projector \(\mathcal P_{\rm loc}\) on a gauge-invariant Wilson/spin-network expansion. Then \(R=(1-\mathcal P_{\rm loc}) S_{\rm eff}\) is a well-defined *formal* remainder given a fixed gauge-invariant coefficient convention. Its coefficients must be controlled in a norm such as
\[
\sup_z\sum_{\Gamma\ni z}e^{\alpha|\Gamma|+m\operatorname{diam}(\Gamma)}\|R(\Gamma)\|\le\varepsilon_*.
\]
Neither Theorem 1 nor 2 establishes this: the small-field Gaussian covariance, multiscale renormalized background matching, contour factorization under exterior coupling, and bounds on all connected residual activities remain missing. In particular the ordinary mixed two-face effective interaction \(-\log z(\sqrt{t^2+s^2+2ts p(V)})\) has oscillation \(\log z(2T)\sim 2T\), so extracting large relevant terms is mandatory.

## Precise next proof gate
1. Pick Penrose-derived spacetime block domains and certify uniformly bounded fills, shape regularity, and surface-to-volume bounds.
2. Specify local gauge-equivariant coarse boundary variables and a local action-extraction projector retaining relevant curvature/electric terms.
3. Establish a *conditional* polymer-factorization/decorrelation estimate on separated blocks, with a gauge-fixed scale-local covariance bound and buffered thin-contour estimates. A probability bound is not an activity bound.
4. Prove the residual rooted norm small and stable under repeated scale changes, including source insertions and higher SU(2) representations.
5. Independently reconstruct the Hamiltonian and prove uniform low-energy Wilson-source observability. UV stability is not an IR mass gap.

## Reference framework
T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories*, Commun. Math. Phys. 102 (1985) 255-275. R. Kotecky and D. Preiss, *Cluster Expansion for Abstract Polymer Models*, Commun. Math. Phys. 103 (1986) 491-498.
