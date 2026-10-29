# The Singular Boundary — Exact nonabelian dual-path flux transport and collective-orbit Fisher criterion

**Date:** 2026-10-29. **Program:** R3 independent reconstruction, SU(2) Wilson Hamiltonian on edge-to-edge planar rhombus disks. **Scope:** exact finite-volume geometry and gauge-invariant spectral/form identities, with a new *conditional* cap-scale small-ball criterion. No polynomial flat-ball bound, uniform magnetic-deletion energy estimate, physical mass gap, or continuum construction is proved.

## 1. Setting and main distinction

Let \(G=SU(2)\) and \(H_f^-=T+V_-\), with \(T=\sum_e a_e(-\Delta_e)\), \(V_-=\sum_{g\ne f}b_g(1-p_g)\) and \(p_g=\frac12\operatorname{ReTr} W_g\). The complete disk includes its outer boundary and obeys Gauss invariance at all vertices. The deleted system has unique strictly positive, normalized and gauge-invariant ground state \(\Omega^-\), ground energy \(E^-\), and \(K=H_f^--E^-\ge0\). The SU(2) Laplacian is normalized by \(-\Delta\chi_{1/2}=\frac34\chi_{1/2}\).

The preceding one-link heat-kernel comparison established \(\mathbb P_{\Omega^-}(1-p_f\le h)\ge c h^{3/2}e^{-C/h}\). This is uniform in face count but too weak to prove the desired bulk deletion cost \(O(h^{-1}\operatorname{polylog}(1/h))\). We identify an **exact potential-preserving simultaneous transport** that can move the deleted holonomy without paying any neighboring magnetic potential variation. The missing estimate is a *collective electric*, not a one-link magnetic, regularity bound.

## 2. Theorem OT-1: exact nonabelian dual-path flux transport

Choose a simple oriented dual-graph path \(\gamma=(f=f_0,f_1,\ldots,f_{\ell-1},\infty)\) from the target face to the exterior, crossing distinct primal edges \(e_1,\ldots,e_\ell\). On the original product-link space \(G^E\), for every \(g\in G\) there exists a smooth, Haar-preserving diffeomorphism \(\mathcal T_g\) such that:

1. Links not crossed by \(\gamma\) are untouched.
2. **All other full plaquette words** \(W_{f_i}\), \(i>0\), and all plaquettes off the dual path are unchanged, for fixed chosen plaquette basepoints. In particular \(V_-\circ\mathcal T_g=V_-\) pointwise, without flatness or small-field assumptions.
3. On every initial configuration, \(g\mapsto W_f(\mathcal T_gU)\) is a left/right Haar translation (possibly composed with inversion and conjugation). Thus \(\int_G \varphi(W_f(\mathcal T_gU))dg=\int_G\varphi(g)dg\) for every integrable class test \(\varphi\).
4. The maps form a smooth (possibly right-handed) SU(2) action, so group averaging defines an idempotent orthogonal projection in \(L^2(G^E,dU)\).

**Constructive proof.** Fix edge orientations and the cyclic word of each face. Multiply the first crossed edge by \(g\) on a chosen side. Proceed along the dual path. At step \(i\), the preceding crossed edge has changed and the next edge \(e_{i+1}\) is the only other crossed edge on face \(f_i\). Write its new face word as \(A' X' B'\), where \(X'\) is \(U_{e_{i+1}}'\) or its inverse. There is a unique choice \(X'=(A')^{-1}W_{f_i}^{\mathrm{old}}(B')^{-1}\) preserving the face word. This update is a left/right SU(2) translation of \(U_{e_{i+1}}\) with multipliers independent of that link, hence preserves its Haar measure. The sequential composition is triangular in the crossed-edge variables, preserving product Haar. It leaves every other face word unchanged because the path has no repeated face. The terminal crossed edge is a boundary edge; no further face is affected. The freedom on \(W_f\) is precisely a group multiplication, establishing the orbit-average identity. In based face coordinates, this is simply multiplication of \(W_f\) with all other based face holonomies fixed; this also verifies the action property.

**Gauge qualification:** for noncentral \(g\), \(\mathcal T_g\) by itself need not commute with the residual global gauge conjugation. Thus it should not be advertised as a new physical SU(2) symmetry of the Hamiltonian. Its **Haar group average** is gauge-compatible and maps the physical Hilbert space into itself.

## 3. Theorem OT-2: exact minimal center-flux string support

For \(g=-I\), all transport conjugations collapse: \(\mathcal T_{-I}\) multiplies each crossed link by the fixed central sign \(-I\). This operation commutes with **all** individual link Laplacians and preserves \(V_-\), recovering the exact deleted-face center-flux \(\mathbb Z_2\) symmetry.

More generally, let \(z_e\in\mathbb Z_2\) label link-center flips. Requiring the target plaquette to flip and every other plaquette not to flip gives \(d_1z=\delta_f\) over \(\mathbb F_2\). Under planar primal–dual correspondence, the support of \(z\) is a subgraph of the dual graph whose odd-degree vertices are exactly \(f\) and the exterior vertex. It therefore contains an \(f\)-to-exterior path. Conversely, a shortest such path realizes this equation. Thus

\[
\boxed{\min_{d_1z=\delta_f}|\operatorname{supp}z|=\operatorname{dist}_{\mathrm{dual}}(f,\infty).}
\]

If \(f\) has fixed positive physical distance \(R\) from the outer boundary and each rhombus has diameter at most \(C h\), then \(\operatorname{dist}_{\rm dual}(f,\infty)\ge cR/h\). Hence an **exact center-flux transport is intrinsically nonlocal** for deep interior faces. This is a topology/geometric support theorem, not a mass-gap claim.

## 4. Theorem OT-3: noncentral transport preserves magnetic energy but not the electric geometry

For a local intervening face with word \(xyz\) (cyclic order can be chosen), one possible exact transport is
\[
 (x,z,y)\mapsto(xg,z,z^{-1}g^{-1}zy).
\]
It preserves \(xzy\) identically. Nevertheless, with \(z(t)=e^{tX}z\), the derivative of the third transformed link contains the commutator of \(X\) with \(g^{-1}\), which is nonzero for a generic noncentral \(g\). Thus the differential of \(\mathcal T_g\) is not an isometry of the product electric metric, and generally \([T,\mathcal T_g]\ne0\). For \(g=-I\) the commutator vanishes exactly.

**Consequence:** exact magnetic preservation cannot be used to declare the deleted vacuum Haar in \(W_f\). The surviving obstruction is electric cross-derivative/connection distortion caused by neighboring links. This gives a precise nonabelian explanation for why the ordinary one-link Feynman–Kac bound does not become polynomial simply by transporting a twist along a dual path.

## 5. Theorem OT-4: canonical Haar-fiber projector and exact electric commutator

Fix a primal maximal tree and its complementary dual spanning tree. Fixing the primal tree links to identity leaves independent Haar coordinates on its \(F\) non-tree links. A triangular change of variables yields independent based face holonomies \((W_g)_{g\in F}\in G^F\), with residual simultaneous conjugation by the root gauge group. This construction is exact for a finite simply connected disk.

Let \(\mathsf P_f\) be conditional Haar averaging over \(W_f\), all remaining based face holonomies held fixed. It is a self-adjoint Markov projection. Because it commutes with simultaneous conjugation, \(\mathsf P_f\) preserves the Gauss-invariant physical subspace. Since the deleted Wilson potential involves only \(W_g\), \(g\ne f\), it commutes with the projector:
\[
\boxed{[V_-,\mathsf P_f]=0,\quad K\mathsf P_f\Omega^-=[T,\mathsf P_f]\Omega^-.}
\]
The latter is an **exact physical ground-state equation**: the non-Haar part of the deleted vacuum is sourced by the electric commutator and *not* by a direct magnetic term. It is not an a priori small commutator estimate.

Write \(Q_f=I-\mathsf P_f\), \(\eta_f=\|Q_f\Omega^-\|_2\), and \(c_\delta=\mathbb P_{\rm Haar}(1-\tfrac12\operatorname{Tr}U\le\delta)\). The identity \(\|1_{\mathrm{cap}}\mathsf P_f\Omega^-\|_2=\sqrt{c_\delta}\sqrt{1-\eta_f^2}\) and the reverse triangle inequality give
\[
\boxed{m_f^-(\delta)\ge\left[\sqrt{c_\delta}\sqrt{1-\eta_f^2}-\eta_f\right]_+^2.}
\]
As \(c_h\sim(4\sqrt2/3\pi)h^{3/2}\), a **sufficient but unproved** quantitative orbit-flatness estimate \(\eta_f=o(h^{3/4})\) uniformly in interior faces yields the desired Haar-order center-ball probability and then the previously established \(O(h^{-1}\log(1/h))\) bulk magnetic-deletion bound. This exact criterion isolates the missing quantum input in a canonical environment-conditioned object.

## 6. Theorem OT-5: collective orbit Fisher energy and its limitation

Let \(D_{\gamma,j}\) (\(j=1,2,3\)) generate the transported SU(2) action in an orthonormal Lie-algebra basis. Each crossed-edge infinitesimal rotation is a left/right generator conjugated by an SU(2) matrix and thus has unit tangent norm. The first nonzero scalar Laplace eigenvalue on SU(2) is \(3/4\). Group Poincaré on each orbit, followed by Haar integration of the original configuration, yields
\[
\boxed{\eta_f^2\le\frac43\mathcal J_{\gamma}(\Omega^-),\qquad \mathcal J_{\gamma}(\Omega^-)=\sum_{j=1}^3\|D_{\gamma,j}\Omega^-\|_{L^2(G^E)}^2.}
\]
For any path \(\gamma\), Cauchy–Schwarz over the crossed links also gives the crude bound
\[
\boxed{\mathcal J_{\gamma}(\Omega^-)\le\left(\sum_{e\in\gamma}a_e^{-1}\right)\sum_{e\in\gamma}a_e\|\nabla_e\Omega^-\|_2^2.}
\]
The first inequality is useful because the **signed, nonabelian transported link derivatives are summed before squaring**. It permits electric-score cancellations invisible to the one-link energy budgets. A uniform bound \(\mathcal J_{\gamma}=o(h^{3/2})\) would suffice for the center-ball bound. However, the previous regional kinetic-energy estimates do **not** establish it; applying the crude second inequality typically loses at least the length of the dual path and is ineffective. This is an independent, unproved *collective electric current* obligation, not a solution to the physical mass gap.

## 7. Deterministic verification and scope

The executable verifier builds genuine noncommuting \(2\times2\) SU(2) matrices, checks the full plaquette words after the noncentral triangular transport, checks central sign transport and exact dual BFS minimum lengths, and confirms one unit-speed generator on every crossed link. It tests 3×3 (9 faces/24 edges), 5×5 (25/60), 7×7 (49/112) square-grid surrogates and the authentic 3-face/10-edge spatial Penrose seed reconstructed from its five-dimensional vertex coordinates. For the center faces of the three grids the exact dual minimum path lengths are respectively 2, 3 and 4. The noncentral electric-isometry obstruction is verified by a positive Lie-commutator norm. All tests are deterministic, with no Monte Carlo and no use of historical temporal Stage7/26 data as lattice ground-state evidence.

**PROVED:** OT-1–OT-5 finite-regulator identities and inequalities, including magnetic-preserving transport, center support distance, exact orbital Haar comparison and electric commutator. **OPEN:** the required \(\eta_f=o(h^{3/4})\) or \(\mathcal J_\gamma=o(h^{3/2})\) for the *actual* deleted Penrose vacuum, polynomial bulk face small-ball probability, fixed-support covariance, regulator-uniform physical gap, quartic resolvent, and continuum Yang–Mills construction.