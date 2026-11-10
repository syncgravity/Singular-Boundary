# PF-I16 — Complete local topology-marker classification for eighth-order SU(2) energy

**2026-11-09; finite original-source theorem, not a mass-gap claim.** Full derivation, source replay, exhaustive marked-isomorphism verifier, log and hashes are archived at Library \`/The Singular Boundary/Proof Audits/PF_I16_LOCAL_TOPOLOGY_INVARIANT_2026_11_09.zip\`. Original accepted Penrose–Fibonacci \(\mathbb Z^5\) link/rhombus geometry; no cubic, Voronoi or assumed 3+1 spacetime substitution.

## Exact topology invariant on qualified three-rhombus chains

Let \(C=(f_1,f_2,f_3)\) consist of three genuine accepted four-link rhombi: \(f_1\cap f_2\) and \(f_2\cap f_3\) contain one *different* original link each; \(f_1,f_3\) share no original link; and the union has **8 distinct original vertices and 10 distinct original links**. The central quadrilateral's two shared edges are either adjacent (meet at one corner) or opposite (disjoint). The 8V/10E hypothesis precludes further vertex identification. These are the **only two face-marked graph isomorphism types**, by the dihedral symmetry of the central 4-cycle plus two otherwise independent exterior squares.

Define the intrinsic (original-incidence-only) graph invariant
\[
\boxed{J(C)=\sum_{v\in V(C)}\binom{\deg_C(v)}4
=\begin{cases}1&\text{shared links adjacent (one degree-four vertex)},\\
0&\text{shared links opposite (four degree-three vertices).}\end{cases}}
\]
This is a configuration/graph invariant, not a physical spacetime dimension.

## Source verification and extension beyond two witnesses

The checker independently reconstructs the indexed original five-direction generator's 35%-tile-center retained vertices and applies PF-I11 **strict perpendicular face-triangle acceptance**, reproducing \(V=1550,E=3017,F=1468\) at original \(N_{\rm grid}=7\). It enumerates all **6156** qualified three-face chains there: **3370 adjacent** and **2786 opposite**. Each of the 6156 passes a *complete face-marked vertex–edge–face incidence graph isomorphism* against the corresponding canonical witness. The prior PF-I16 source-replay record separately verified the two canonical witnesses occur at all eight original source sizes. This turn did **not** rerun all eight sizes or execute the unpublished original Python source verbatim (only its independently reconstructed indexed equations).

## All-coupling within-class Hamiltonian equivalence

For unit auxiliary link electric coefficients, each face-marked graph isomorphism induces a unitary relabeling of the normalized \(SU(2)^{10}\) Haar configuration space. Original-link inversions preserve Haar and Casimir; face boundary reversal/cyclic rebase preserve \(\tfrac12\operatorname{Tr}U_f\), and the vertex Gauss constraints are transported. Hence the **entire local Hamiltonian family**
\[
\widehat H_C(\mathbf b)=\sum_{e\in E(C)} C_e-\sum_{i=1}^3b_ip_{f_i}
\]
is unitarily equivalent to its canonical adjacent or opposite class representative, for **all real \(\mathbf b\)**. If coefficients \(a_e\) are not unit, they must be transported by the marked isomorphism for the equivalence to apply.

The prior independent exact rational, four-gauge eighth-order theorem (archived separately as \`PF_I16_EIGHTH_ORDER_TOPOLOGY_2026_11_09.zip\`) established:
\[
\widehat E_{\mathrm{opp}}(\mathbf b)-\widehat E_{\mathrm{adj}}(\mathbf b)
=\delta b_1^2b_2^4b_3^2+O(\|\mathbf b\|^{10}),
\quad \boxed{\delta=\frac{36481}{581335252992000}>0.}
\]
By graph isomorphism this becomes **universal over all qualified source motifs**, not just the two previously hand-picked witnesses:
\[
\boxed{\widehat E_C(\mathbf b)=\widehat E_{\mathrm{adj}}(\mathbf b)
+(1-J(C))\delta b_1^2b_2^4b_3^2+O(\|\mathbf b\|^{10}).}
\]
Thus the two classes cannot be unitarily equivalent *as parameterized quantum Hamiltonian families*, because their analytic ground energies differ. The rational coefficient is inherited from the **previous** exact original-link calculation; this continuation verifies its rational consistency and the new 6156 graph isomorphisms but does not recompute the full eighth-order matrix.

## Fixed-order source-incidence envelope

Across the eight previously authenticated original source crops, at most **two accepted faces** meet any original link. So the central face has at most four overlap neighbors and at most six unordered exterior-neighbor pairs. The topology-*discriminating* eighth-order contribution
\[
\mathfrak T_8=\delta\sum_{\substack{\text{qualified three-face chains }C\\J(C)=0}}
b_{f_1}^2b_{f_2}^4b_{f_3}^2
\]
counting each unordered exterior pair once, satisfies for \(|b_f|\le b_0\)
\[
\boxed{|\mathfrak T_8|\le6|F|\delta b_0^8.}
\]
This bounds **only this particular component** of the eighth-order connected energy, not all order-eight terms, other motif classes, or higher orders. Couplings on other faces are set to zero when extracting each multivariate coefficient. No finite-coupling factorization or gap follows.

**Still OPEN:** all-orders SU(2) connected-cluster summability; uniform interacting-vacuum Poincaré gap; source-selected physical time/kinetic normalization; continuum OS reconstruction; four-dimensional Yang–Mills mass gap. Canonical main, historical source data and Observatory proof gates unchanged.