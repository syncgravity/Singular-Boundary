# P0-H3D — Exact Delone and Voronoi certificate for the alternative Z5-derived 3D model

**Date:** 2026-11-11  
**Status:** exact algebraic geometry result for a declared alternative model set. It is **not** the original 2D Penrose acceptance set, not a source-certified C5-invariant regulator, and not a Yang–Mills dynamics or mass-gap theorem. This strengthens the preceding finite-sample diagnostic.

## 1. Model definition

Let \(\omega=e^{2\pi i/5}\), \(\varphi=(1+\sqrt5)/2\), and
\[
\Lambda=A_4=\{m\in\mathbb Z^5:\sum_{j=0}^4m_j=0\}.
\]
Define
\[
z_1(m)=\sum_{j=0}^4m_j\omega^j,\qquad
z_2(m)=\sum_{j=0}^4m_j\omega^{2j},
\]
and the orthonormal physical/internal projections
\[
\pi_3(m)=\sqrt{\frac25}\,(\Re z_1,\Im z_1,\Re z_2),
\qquad
\pi_1(m)=\sqrt{\frac25}\,\Im z_2.
\]
The scale \(\sqrt{2/5}\) follows from Parseval on the sum-zero subspace. The candidate model set is
\[
X_3=\{\pi_3(m):m\in\Lambda,\ |\Im z_2(m)|\le\varphi\}.
\]
This is a regular 3D cut-and-project model set: physical projection is injective, internal projection is dense, and the internal window is a compact interval with nonempty interior and measure-zero boundary.

It is a **changed model**, not the original Penrose vertex set. It projects the decagonal acceptance window to one internal dimension, admits points whose real perpendicular coordinate lies outside the original decagon, and selects a line in the 144-degree representation. The full \(C_5\) action does not preserve this 3+1 split.

## 2. Exact global Delone constants

The exact local-environment certificate proves
\[
\boxed{\operatorname{sep}(X_3)^2=2-\frac{4\sqrt5}{5}},
\qquad
\boxed{\operatorname{cov}(X_3)^2=\frac{173}{200}-\frac{\sqrt5}{10}}.
\]
Numerically,
\[
\operatorname{sep}(X_3)=0.4595058411\ldots,\qquad
\operatorname{cov}(X_3)=0.8008702780\ldots.
\]
Consequently every Voronoi cell has inradius at least \(\operatorname{sep}(X_3)/2\), circumradius at most \(\operatorname{cov}(X_3)\), and exact uniform shape bound
\[
\boxed{\frac{R_{\rm out}}{R_{\rm in}}
\le\frac{\sqrt{665+246\sqrt5}}{10}
=3.4857893259\ldots.}
\]
Scaling physical coordinates by \(h\) gives a non-nested, shape-regular 3D Voronoi mesh family with cell diameters at most \(2h\operatorname{cov}(X_3)\), inradii at least \(h\operatorname{sep}(X_3)/2\), and uniformly bounded local incidence.

### Exact separation

For two accepted sites, their internal-coordinate difference satisfies \(|\Im z_2(\delta)|\le2\varphi\). If their physical separation is at most \(1.62=2(0.81)\), Parseval gives
\[
\|\delta\|_{\mathbb R^5}^2
=\frac52\|\pi_3(\delta)\|^2+(\Im z_2(\delta))^2
\le\frac52(1.62)^2+4\varphi^2<25.
\]
Thus every coordinate of the integer vector \(\delta\) lies in \([-4,4]\). Exact enumeration in \(\mathbb Q(\sqrt5)\) finds 30 nonzero displacement classes satisfying both cut-off conditions. The smallest physical squared length among them is exactly \(2-4\sqrt5/5\), attained by \(\delta=(0,-1,1,-1,1)\) and its negative. Its internal shift is strictly smaller than \(2\varphi\), so the two acceptance intervals overlap; density of the internal projection ensures such pairs occur in \(X_3\). All other pairs either belong to this finite list or are farther than 1.62. This proves the stated global separation.

### Exact Voronoi covering bound

For a center with internal coordinate \(t\in[-\varphi,\varphi]\), a displacement \(\delta\) from the 30-element list is accepted exactly when
\[
-\varphi\le t+\Im z_2(\delta)\le\varphi.
\]
The acceptance state changes only at the finitely many thresholds \(t=\pm\varphi-\Im z_2(\delta)\). Exact ordering and deduplication in \(\mathbb Q(\sqrt5,\sin(\pi/5))\) give 20 endpoints and 19 open intervals. Testing every endpoint and one exact midpoint in every interval gives 39 exhaustive phase strata; each stratum has 14–18 accepted candidate neighbours.

For each stratum, the verifier finds a positive tetrahedral combination of four neighbour normals. This proves the corresponding halfspace intersection is bounded. Qhull is used only to propose its vertices and facets. Every proposed vertex is then reconstructed as an exact intersection of three original planes and checked against **all** halfspaces in the exact field. Every triangular facet of the proposed convex hull is checked to lie on an original halfspace plane. Together with boundedness, these checks prove that the proposed hull equals the full halfspace intersection; the floating-point library is not used to certify any inequality or incidence.

All 39 exact phase cases have the same exact maximum squared circumradius
\[
\boxed{\frac{173}{200}-\frac{\sqrt5}{10}<\left(\frac{81}{100}\right)^2.}
\]
Any accepted site omitted from the 30 displacement list is farther than 1.62. Such a site cannot cut a Voronoi cell already contained in the radius-0.81 ball. This closes the finite-neighbour bootstrap and proves the global covering bound for the infinite model set.

The exact local cell types are:

| Facets | Vertices | Number of the 39 phase strata |
|---:|---:|---:|
| 8 | 12 | 6 |
| 12 | 18 | 26 |
| 12 | 20 | 2 |
| 14 | 18 | 3 |
| 14 | 22 | 2 |

All cells are convex polyhedra. The Voronoi tessellation is a locally finite, face-to-face 3D cellulation with bounded cell complexity.

## 3. Period structure: this is a layered model

The internal projection is
\[
\Im z_2(m)=\sin(\pi/5)\big[(m_1-m_4)+\varphi(m_3-m_2)\big].
\]
Because \(\varphi\) is irrational, its kernel in \(\Lambda\) is exactly
\[
\ker(\pi_1|_\Lambda)
=\{(-2a-2b,a,b,b,a):a,b\in\mathbb Z\}.
\]
It is a rank-two lattice of physical periods. A basis is
\[
(-2,1,0,0,1),\qquad(-2,0,1,1,0),
\]
whose scaled physical vectors are
\[
\sqrt{\frac25}(\varphi-3,0,-2-\varphi),
\qquad
\sqrt{\frac25}(-2-\varphi,0,\varphi-3).
\]
Their period-lattice covolume in the period plane is \(2\sqrt5\). Thus \(X_3\) contains a rank-two physical period lattice and is a **partially periodic / layered** 3D quasicrystalline model. It is not a fully 3D aperiodic Penrose tiling.

The regular-model-set density is
\[
\boxed{\operatorname{dens}(X_3)
=\frac{2\varphi\sqrt{2/5}}{\sqrt5}
=\frac{2\sqrt2\,\varphi}{5}.}
\]

## 4. Proof-program disposition

This is now a genuine 3D spatial **geometry candidate** with exact separation, covering, local Voronoi types, and uniform shape bounds. It is a possible alternative regulator geometry if the project is willing to declare the changed acceptance rule and partial periodicity. It does not repair the false compact-torus claim and must not be conflated with either the original Penrose model or the separate C5 3+2 Delone candidate.

Still open before it can enter the Yang–Mills proof:

1. choose whether H-3D is an accepted alternative regulator or retain the original Penrose model as the sole primary;
2. construct exact oriented primal/dual incidence operators for its Voronoi cell complex and boundary restrictions;
3. derive metric-consistent discrete Hodge stars and electric/magnetic coefficients, with physical coupling and time normalization;
4. define the SU(2) Gauss sector, self-adjoint Hamiltonian and positive transfer construction;
5. prove the uniform interacting-vacuum Poincaré inequality and its infinite-volume/continuum consequences.

**Verdict:** the alternative H-3D model set now has an exact Delone/Voronoi geometry certificate. It is a layered, partially periodic 3D model with external time; no gauge dynamics, continuum Yang–Mills theory, or mass gap has been proved. The original source-faithful P0 gate remains OPEN.

## Reproduction

\`python research/verification/verify_p0_h3d_exact_voronoi.py\`

The verifier uses NumPy/SciPy only to propose candidate vertices/facets. Exact algebraic reconstruction and all inequality/incidence checks are carried out over \(\mathbb Q(\sqrt5,\sin(\pi/5))\`.
