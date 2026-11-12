# P0-H — Coupled-Z5 perpendicular quotient: density obstruction and a 3D candidate

**Date:** 2026-11-11 (America/Denver)  
**Status:** exact obstruction to the Paper 2 compact-torus claim; a distinct 3D cut-and-project candidate is specified. **P0-H remains OPEN.** This is not a Yang–Mills regulator or continuum theorem.

## Executive result

Paper 2 §3.3 asserts
\[
\mathcal C=\mathbb R^2_\perp/\pi_\perp(\mathbb Z^5)\cong\mathbb T^2.
\]
With \(\omega=e^{2\pi i/5}\) and \(z_2(m)=\sum_{j=0}^4m_j\omega^{2j}\), the subgroup \(\pi_\perp(\mathbb Z^5)\) is **dense in the entire perpendicular plane**, even when restricted to the sum-zero rank-four lattice that removes the trivial representation. The quotient is therefore not Hausdorff and cannot be a topological two-torus.

This is an exact source-level obstruction. It does not invalidate the real \(C_5\) decomposition, the standard 2D Penrose cut-and-project set, finite graph spectra, or the supplied Stage 26 data. It does invalidate the stated inference from this quotient to a compact flat torus and leaves the associated compactification / KK interpretation without the claimed topological foundation.

A different 3D model-set construction can be defined from the same rank-four lattice by making one real line in the perpendicular plane a third **extended** physical direction and retaining the orthogonal line as one-dimensional internal space. It changes the acceptance rule and breaks \(C_5\); it is a candidate extension, not the original Penrose model.

## 1. Exact density calculation

Let
\[
\Lambda_0=\{m\in\mathbb Z^5:\sum_{j=0}^4m_j=0\},\qquad
\Gamma_\perp=\{\sum_{j=0}^4m_j\omega^{2j}:m\in\Lambda_0\}.
\]
All four vectors below have coordinate sum zero, so the calculation already incorporates removal of the trivial direction.

Two integer vectors give real values:
\[
\begin{aligned}
(0,1,-1,-1,1)&\longmapsto
\omega^2+\omega^3-\omega-\omega^4=-\sqrt5,\\
(2,0,-1,-1,0)&\longmapsto
2-\omega-\omega^4=(5-\sqrt5)/2.
\end{aligned}
\]
The ratio of the absolute values is
\[
\frac{(5-\sqrt5)/2}{\sqrt5}
=\frac{\sqrt5-1}{2}=\varphi^{-1}\notin\mathbb Q.
\]
Thus \(\Gamma_\perp\) contains a dense additive subgroup of the real axis.

Two more sum-zero vectors give
\[
\begin{aligned}
(0,1,0,0,-1)&\longmapsto\omega^2-\omega^3=2i\sin(\pi/5),\\
(0,0,-1,1,0)&\longmapsto\omega-\omega^4=2i\sin(2\pi/5).
\end{aligned}
\]
Their positive ratio is
\[
\frac{\sin(2\pi/5)}{\sin(\pi/5)}=\varphi\notin\mathbb Q.
\]
Thus \(\Gamma_\perp\) also contains a dense additive subgroup of the imaginary axis. Since it is additive, it contains sums of these two dense axis subgroups and is dense in \(\mathbb C\cong\mathbb R^2\).

Therefore both \(\pi_\perp(\Lambda_0)\) and the larger \(\pi_\perp(\mathbb Z^5)\) are dense.

## 2. Topological consequence

The image is countable, hence a proper dense, nonclosed subgroup of \(\mathbb R^2\). A quotient topological group \(G/H\) is Hausdorff only if \(H\) is closed. Consequently
\[
\boxed{\mathbb R^2_\perp/\pi_\perp(\mathbb Z^5)
\text{ is not Hausdorff and is not }\mathbb T^2.}
\]
The same conclusion holds with \(\mathbb Z^5\) replaced by \(\Lambda_0\). The proposed inherited flat quotient metric also fails: density makes the quotient pseudodistance between any two cosets zero.

A bounded acceptance window is not a periodic identification. Bounding \(u=\operatorname{Re}z_2\) by the decagon does not make \(u\) a circle coordinate. A compact spatial direction requires a separately specified period lattice and compatible action; the displayed dense subgroup supplies neither.

## 3. Candidate 3D cut-and-project construction

Let
\[
V=\{x\in\mathbb R^5:\sum_jx_j=0\}
=V_{72^\circ}\oplus V_{144^\circ},\qquad
\Lambda=V\cap\mathbb Z^5.
\]
Choose a real unit vector \(e_u\in V_{144^\circ}\) and its orthogonal companion \(e_v\). Set
\[
E_{\rm phys}^{(3)}=V_{72^\circ}\oplus\mathbb Re_u,\qquad
E_{\rm int}^{(1)}=\mathbb Re_v.
\]
Let \(\pi_3,\pi_1\) be the projections and \(W_1=\pi_1(W)\), the projection of the original decagonal window onto the internal line. Define
\[
X_3(W_1)=\{\pi_3(m):m\in\Lambda,\ \pi_1(m)\in W_1\}.
\]

The cut-and-project conditions hold:

1. **Physical injectivity.** If \(\pi_3(m)=0\), then \(z_1(m)=\sum_jm_j\omega^j=0\). Since \(\Phi_5(x)=1+x+x^2+x^3+x^4\) is the minimal polynomial of \(\omega\), the integer polynomial \(\sum_jm_jx^j\) must be a multiple of \(\Phi_5\). Thus all \(m_j\) are equal; the sum-zero condition forces \(m=0\).
2. **Internal density.** The imaginary-axis calculation in §1 proves that the projection of \(\Lambda\) onto the \(e_v\) line is dense.
3. **Window.** The projection of a compact nondegenerate decagon is a compact interval with nonempty interior and measure-zero boundary.

This defines a regular 3D cut-and-project model-set candidate; under the standard cut-and-project hypotheses its point set is Delone. Scaling physical coordinates by \(h\) gives a shape-controlled geometric mesh family at the level of Voronoi cells. It does **not** supply compatible subdivision maps, SU(2) variables, a gauge Hamiltonian, Hodge weights, physical time, or a spectral inequality.

Crucially, \(X_3(W_1)\) is **not** the original Penrose vertex set: it replaces the two-dimensional condition \(z_2(m)\in W\) by the one-dimensional condition \(\operatorname{Im}z_2(m)\in W_1\), admitting points whose real perpendicular coordinate lies outside the original decagon. It also selects a line in the 144-degree representation, so \(C_5\) does not preserve the \(3+1\) split. Here \(u\) is extended physical space, not a compact circle; time must be external and separately defined.

This is a candidate alternative 3D Z5-derived model, not a repair of Paper 2's compactification and not yet the canonical regulator.

## 4. Proof-roadmap disposition

- **P0-H:** the real \(C_5\) representation and 2D Penrose model-set construction remain valid. The claimed perpendicular flat torus and its direct KK inference are obstructed. A source-certified refining 3D spatial cellulation with physical time remains absent.
- **Candidate H-3D:** a precise alternative 3D point-set construction is available, but it changes the window, breaks \(C_5\), and still needs finite-region Voronoi/Delaunay cellulations, boundary maps, incidence/Hodge data and a compatible SU(2) action.
- **P0-C:** the cubic control remains separate. Its cubical chain refinement and failure of naive exact Hamiltonian intertwining do not transfer to H-3D.
- **S1:** no source-derived electric coefficient, magnetic interaction, Gauss law, self-adjoint Hamiltonian, physical clock or positive transfer is established.
- **S2–S5:** unchanged and open. No interacting-vacuum estimate, uniform all-functions Poincaré inequality, infrared exclusion, OS reconstruction or mass gap follows.

**Verdict:** an exact topological claim in the compactification narrative is false as written. A different 3D cut-and-project model can be defined from the same rank-four lattice, but it must earn its own regulator and dynamics certificates. **P0-H remains OPEN; no canonical proof gate is closed.**

## Sources

- Supplied dissertation v10.7, Chapter 3, especially §§3.1–3.4 and the open-question list.
- Supplied Paper 2, *From Z5 to Minkowski Spacetime via Lapidus Complex Dimensions*, §§2.1–2.2 and §§3.1–3.4; quotient claim (9).
- Repository: \`docs/research/P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md\` and \`docs/research/SOURCE_COMPATIBLE_SPECTRAL_INEQUALITY_PROGRAM_2026-11-11.md\`.
