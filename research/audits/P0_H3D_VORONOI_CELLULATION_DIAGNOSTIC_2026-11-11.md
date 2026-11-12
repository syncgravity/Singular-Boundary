# P0-H3D — Finite Voronoi cellulation of the alternative 3D Z5 model set

**Date:** 2026-11-11  
**Classification:** finite numerical geometry diagnostic with an exact coefficient-buffer bound. Not a theorem about the original Penrose set, an SU(2) Hamiltonian, or the Yang–Mills mass gap.

## 1. Construction

The preceding P0-H audit shows that the claimed quotient \(\mathbb R^2_\perp/\pi_\perp(\mathbb Z^5)\cong\mathbb T^2\) is false. It also defines a distinct 3D cut-and-project candidate: retain the 72-degree plane and one real line in the 144-degree plane as physical space; use the orthogonal line as one-dimensional internal space.

Let
\[
\Lambda=A_4=\{m\in\mathbb Z^5:\sum_jm_j=0\},\quad
z_1(m)=\sum_jm_j\omega^j,\quad z_2(m)=\sum_jm_j\omega^{2j},
\]
where \(\omega=e^{2\pi i/5}\), \(\varphi=(1+\sqrt5)/2\). Define
\[
\pi_3(m)=\sqrt{2/5}(\Re z_1,\Im z_1,\Re z_2),\quad
\pi_1(m)=\sqrt{2/5}\Im z_2.
\]
The factor \(\sqrt{2/5}\) makes these coordinates orthonormal for the inherited Euclidean metric on the sum-zero subspace. The candidate window is \(|\Im z_2|\le\varphi\), the projection of a centered regular decagon of circumradius \(\varphi\) onto the internal line.

This is not the original Penrose vertex set: it replaces the 2D window by a 1D projected window, admits points whose real perpendicular coordinate lies outside the decagon, breaks full \(C_5\), and makes \(\Re z_2\) extended physical space rather than a compact circle.

## 2. Finite sample and exact buffer bound

Enumerate \(m\in A_4\cap[-12,12]^5\) with \(|\Im z_2(m)|\le\varphi\): 23,525 points. The core consists of the 7,383 points with \(\|m\|_\infty\le8\).

For a core point \(m\) and any omitted accepted point \(n\notin[-12,12]^5\), some coordinate of \(\delta=n-m\) has magnitude at least 5, so \(\|\delta\|_{\mathbb R^5}^2\ge25\). Both internal coordinates lie in \([-\varphi,\varphi]\), hence \(|\Im z_2(\delta)|\le2\varphi\). Parseval gives
\[
\|\pi_3(\delta)\|^2
=\frac25(\|\delta\|_{\mathbb R^5}^2-(\Im z_2(\delta))^2)
\ge\frac25(25-4\varphi^2).
\]
Thus every omitted point is at least **2.4106317881** from every core point. Twice the measured maximum core Voronoi circumradius is **1.6017405562**. Omitted points cannot cut the computed core Voronoi cells. The buffer inequality is exact; the cell geometry is floating-point Qhull output and is not interval-certified.

## 3. Voronoi results

The reproducible script uses NumPy 2.3.5 and SciPy 1.17.0.

| Quantity | Result |
|---|---:|
| Buffered accepted points | 23,525 |
| Core Voronoi cells | 7,383 |
| Nearest-neighbour distance | 0.4595058411 – 1.0260538020 |
| Voronoi inradius | 0.2297529205 – 0.5130269010 |
| Voronoi circumradius | 0.8008702780 (all core cells, numerical tolerance) |
| Maximum circumradius / inradius | 3.4857893259 |
| Cell volume | 0.7358826956 – 1.3032799162 |
| Faces per cell | 8: 624; 12: 5,396; 14: 1,363 |
| Vertices per cell | 12: 624; 18: 4,695; 20: 1,026; 22: 1,038 |

All core cells are bounded and have positive computed volume. For the 7,383-point core as a standalone Delaunay input, Qhull returns 43,220 tetrahedra, of which 2,277 have volume below \(10^{-10}\). The Voronoi polyhedral cellulation is therefore preferable to an arbitrary simplicial Delaunay refinement in this diagnostic.

These are finite-sample numerical findings, not an exact classification of all local environments or exact algebraic Voronoi vertices.

## 4. Disposition and next gate

The candidate passes a useful finite geometry diagnostic: it admits a bounded-core Voronoi cellulation with an exact coefficient-buffer argument and bounded observed aspect ratio. The next decisive step is an exact or interval-certified local Voronoi audit: enumerate possible neighbour displacement classes from the window-difference condition, certify Voronoi inequalities and face incidences, then build oriented primal/dual chain operators.

Still OPEN: source-wide exact local-environment classification; compatible subdivision and boundary maps; exact incidence and discrete Hodge-star identities; a canonical gauge cell complex; SU(2) link variables, Gauss law, magnetic action, electric coefficients, physical time and positive transfer. This candidate changes the original Penrose acceptance rule and must remain separate until explicitly accepted as the canonical P0 regulator.

**Verdict:** finite 3D Voronoi geometry has been demonstrated for the alternative Z5-derived model set. S0 remains OPEN. No Yang–Mills dynamics or mass-gap conclusion follows.

## Reproduction

\`python research/verification/verify_p0_h3d_voronoi_sample.py\`
