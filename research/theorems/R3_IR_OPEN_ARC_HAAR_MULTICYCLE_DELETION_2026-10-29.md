# The Singular Boundary — Full-coupling open-arc Haar theorem beyond dual bridges

**Date:** 2026-10-29. **Program:** R3 independent reconstruction. **Classification:** unconditional finite-volume, fully nonlinear SU(2) Wilson Hamiltonian theorem on a NEW class of magnetic-deleted interior faces, including some faces on two independent magnetic dual cycles with no incident dual-graph bridges. **Not proved:** the Haar marginal or polynomial small-ball bound for fully cycle-surrounded faces whose surrounding retained magnetic faces form one link-connected component, the fixed-support nonlinear covariance, the physical mass gap or continuum construction.

## I. Model and precise graph condition

Consider a finite face-complete simply connected edge-to-edge planar rhombus disk with SU(2) link variables, all-vertex Gauss invariance, normalized Haar product measure, and the nonnegative Wilson Hamiltonian

\[
H_f^-=\sum_{e\in E}a_e(-\Delta_e)+\sum_{g\in F\setminus\{f\}}b_g(1-p_g),\quad p_g=\frac12\operatorname{ReTr}W_g,
\quad a_e,b_g>0.
\]

The Laplacian is normalized by \(-\Delta\chi_{1/2}=3\chi_{1/2}/4\). Work first on the *unrestricted* product-link Hilbert space; the unique strictly positive ground state is invariant under the physical vertex gauge group, hence gives the actual physical vacuum. Boundary holonomies are **not fixed**, and Gauss invariance is imposed at **all** vertices.

Partition the retained magnetic faces \(F\setminus\{f\}\) into components under **shared-primal-edge adjacency**. Associate to each component \(C\) its entire link set \(E_C=\bigcup_{g\in C}\partial g\). Different \(E_C\) are disjoint. Free links not in any \(E_C\) are independent electric-only components. Each of these (magnetic or free) components corresponds to an independent tensor factor in the full Hamiltonian. This is the same factorization mechanism used in the earlier dual-bridge theorem; no new factorization is presumed at physical Gauss-reduced coordinate level.

**Open-arc condition (OA).** There exists a component \(C\) such that its intersection with the four cyclically ordered boundary edges of \(f\) is **one nonempty, proper, consecutive arc**. In particular, it may consist of **two or three adjacent target edges**. The old incident-dual-bridge criterion required that one component meet \(\partial f\) in *exactly one edge*. OA is strictly more general.

## II. OA-1: gauge invariance forces Haar law for an open component path

**Lemma.** Let \(C\) be any independent link factor with a Hamiltonian consisting of its positive link Laplacians and gauge-invariant Wilson plaquette potentials. Let \(\Omega_C\) be its unique strictly positive normalized ground state. For any oriented open path \(\gamma\) consisting entirely of edges in \(E_C\), whose endpoints are **distinct vertices**, the group-valued parallel transport \(U_\gamma\) has the *exact normalized SU(2) Haar law* under \(|\Omega_C|^2\prod_{e\in E_C}dU_e\).

*Proof.* The component Hamiltonian is invariant under the local vertex gauge group acting on its own links, even at vertices that are also endpoints of edges belonging to other, independent components. Because \(\Omega_C\) is the **unique positive** ground state on its unreduced component Hilbert space, it is invariant under these vertex gauge transformations. Apply an arbitrary gauge transformation \(k\in SU(2)\) at the initial endpoint of \(\gamma\), with identity at all other vertices. The open parallel transport changes as \(U_\gamma\mapsto kU_\gamma\) (or via a right translation if the reverse orientation is used). The ground-state probability measure is invariant under this transformation. Thus the pushforward probability is invariant under *every* left translation on SU(2). Uniqueness of normalized Haar measure proves the claim. No flatness, strong coupling, smallness of the potential, or physical mass gap is used. QED.

For \(C\) corresponding to an isolated free electric link, this is the usual Haar free-link lemma.

## III. OA-2: exact full-coupling deleted-face Haar marginal

**Theorem.** If a target face \(f\) satisfies OA, then its holonomy \(W_f\) is *exactly SU(2) Haar distributed in the true nonlinear magnetic-deleted vacuum*, at all positive electric coefficients and at arbitrary values of every retained magnetic coupling:

\[
\boxed{\quad \mathbb P_{\Omega_f^-}(W_f\in A)=\operatorname{Haar}_{SU(2)}(A)\qquad\text{for every measurable }A.\quad}\tag{OA2}
\]

*Proof.* The full Hamiltonian is a tensor sum over the disjoint link sets \(E_C\), plus free electric-only links. Its unique positive unrestricted ground state is the tensor product of the unique positive component ground states. Each component ground state is separately invariant under its own vertex gauge transformations, so their product is invariant under the physical simultaneous gauge action at every vertex. Thus this product is the actual normalized physical ground state.

Choose the OA component \(C\). Rotate the cyclic starting point in the target face boundary word so that the consecutive \(C\)-edges appear as the first block. Their ordered product \(U_\gamma\) is an open parallel transport in \(C\) with distinct endpoints, since the arc is nonempty and strictly shorter than the closed four-edge face. By OA-1, \(U_\gamma\) has the Haar law. The product \(R\) of all remaining target boundary links depends only on the *other independent link components* and is independent of \(U_\gamma\). The full target holonomy is \(W_f=U_\gamma R\), up to cyclic conjugation (which does not change normalized Haar probability). Conditional on any \(R\), the product of an independent Haar variable with \(R\) is Haar. Averaging over \(R\) proves OA2. QED.

This conclusion controls the **whole group-valued** face holonomy, not only its class trace, center parity, or a small-cap event.

## IV. OA-3: strict extension beyond dual bridges — a seven-face two-cycle disk

Consider seven unit-square rhombi with lower-left corners

\[
S_7=\{(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]

The target is \(f=(0,0)\). Every one of its four edges belongs to a neighboring face. The retained magnetic dual graph has two separate components: one contains the north and east neighboring faces, joined through the northeast corner face; the other contains the south and west neighbors, joined through the southwest corner face. The intersection of each component's links with \(\partial f\) is a **contiguous arc of exactly two edges**. Both components obey OA.

In the *complete* magnetic dual graph, each of the four edges incident to the central target lies on a dual four-cycle, either \(f\to N\to NE\to E\to f\) (a 4-edge cycle) or \(f\to S\to SW\to W\to f\). Therefore **none** of the central face's four incident dual edges is a bridge. The old BD criterion fails, yet OA2 proves the **exact full-coupling Haar target**. This provides a genuinely new non-bridge, multi-cycle case of nonlinear interior magnetic deletion.

By contrast, on the complete 3×3 nine-face square rhombus disk, deleting the central target leaves the other eight faces in **one** magnetic edge-connected component meeting all four target edges. OA is absent; no Haar conclusion is asserted. The seven-face square example is a legitimate planar rhombus-disk surrogate; no claim is made that the same exact seven-face incidence occurs as an isolated patch in every Penrose refinement.

## V. OA-4: unconditional deletion energy and exact vanishing of the four-neighbor budget

For every face satisfying OA, the earlier *exact Haar* variational computation applies without modification:

\[
\boxed{0\le \Delta_f=E_0(H_f^-+b_fd_f)-E_0(H_f^-)\le\frac{3}{2\sqrt2}\sqrt{A_fb_f},\quad A_f=\sum_{e\in\partial f}a_e.}\tag{OA4}
\]

Thus for bounded positive electric coefficients and \(b_f\asymp h^{-2}\), \(\Delta_f=O(h^{-1})\) for OA faces, independent of the number of faces and nonlinear strength of other retained interactions. Their extreme-defect bounds follow from the existing moment-to-tail theorem. This does **not** close the fully connected bulk case.

Moreover, in the four-neighbor interpolation \(H_f^-(t_1,t_2,t_3,t_4)\), starting from any OA face and varying only those four neighbors, the same fixed magnetic-component partition remains available; deleting some neighboring couplings can only remove constraints, not connect previously separate components. Each component remains gauge invariant and the open arc still has Haar law. Therefore

\[
F_a(\mathbf t):=\langle k_a(W_f)\rangle_{\mathbf t}=\alpha_a^2\qquad (\mathbf t\in[0,1]^4)
\]

and the **entire** eightfold mixed response, and its adverse budget, vanish identically:

\[
\boxed{\quad \partial_1^2\partial_2^2\partial_3^2\partial_4^2F_a\equiv0,\qquad \mathcal N_a=0.\quad}\tag{OA5}
\]

This is an **unconditional full-coupling solution of the new mixed-response priority for OA faces**, not merely a small-coupling or perturbative selection rule. It is unavailable when every target edge belongs to one connected retained magnetic component.

## VI. Reproducibility and remaining boundary

The deterministic script enumerates exact shared-edge face incidence for five-face star, seven-face two-cycle, and nine-face 3×3 models. It verifies that the seven-face disk has 20 links, two magnetic components, two contiguous two-edge arcs and **no incident dual bridge**; the 3×3 disk has 24 links and a single retained component, therefore fails OA. It also checks non-Abelian quaternion group multiplication/left Haar orbits and a nonconstant positive closed-loop weight whose open-path marginal is exactly Haar. No Monte Carlo; no assertion that a finite-group test substitutes for the continuous SU(2) proof, which is analytic.

**PROVED:** OA-1, OA-2, OA-3, OA-4 and OA-5 at the explicitly stated finite-regulator level; strict enlargement of the earlier exact Haar/dual-bridge deletion class and exact vanishing of adverse full-coupling four-neighbor response for the new OA class.

**OPEN:** the generic fully cycle-surrounded Penrose face when the retained magnetic link component meets *all four* target edges; its independent nonlinear small-ball/deletion estimate and connected Wilson-angle covariance; physical uniform mass gap, quartic resolvent, and continuum construction. This is a meaningful partial closure of the remaining priorities, not their complete resolution.