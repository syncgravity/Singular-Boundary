# R3-IR-451 — Dual-path support obstruction for localized deleted-target center symmetry

2026-10-30. Exact graph-theoretic theorem for the original-link SU(2) Wilson disk with independent dynamical boundary links. Clarifies R3-IR-420 and R3-IR-450; not a cap decay estimate.

Let G be the finite planar disk cellulation, f an interior target face with its magnetic term deleted, and G* its dual multigraph with one vertex for each bounded face and a single exterior vertex infinity. A primal link e corresponds to a dual edge e*, including boundary links connecting their incident face to infinity. For z in F_2^E, define the center-flip transformation U_e -> (-1)^(z_e) U_e.

Each face g acquires center parity (-1)^(Dz)_g, with D the mod-two face-edge incidence matrix. For a symmetry of the deleted-target Hamiltonian that flips the target holonomy but preserves all retained face holonomies, Dz=1_f.

THEOREM (DP-1). The support of ANY z satisfying Dz=1_f contains a dual edge path from f to infinity. In particular the number of flipped original links is at least the dual graph distance d*(f,infinity). Conversely, any simple dual path from f to infinity yields such a z, because its only odd-degree dual vertices are f and infinity; thus the minimum flip support cardinality equals d*(f,infinity).

Proof. At each bounded face g, the degree parity of the selected dual subgraph is (Dz)_g. Hence f is its unique odd-degree bounded vertex. By the handshaking lemma, the exterior vertex has odd selected degree. Every component of a finite graph contains an even number of odd-degree vertices, so f and infinity belong to the same selected-edge component, which contains a path. A shortest path realizes the lower bound. This uses independent boundary link flips; on a closed surface the exterior vertex is absent and the construction fails.

COROLLARY (DP-2). Suppose one conditions on a set Y of original link variables and demands a center-flux symmetry that fixes each element of Y pointwise. Such a symmetry exists of this link-center-flip form if and only if the dual subgraph retaining only edges whose original links lie outside Y contains a path from f to infinity. This is an EXACT finite-graph criterion, not a stochastic mixing assertion.

If Y intersects every f-to-infinity dual path, no Hamiltonian-preserving target-only link-center flip can leave Y unchanged. Thus global center symmetry cannot in that case be used to prove that conditional half-integer target character moments vanish given Y. This DOES NOT prove those conditional moments are nonzero.

Conversely, if an allowable path exists, the corresponding unitary center transformation preserves the positive ground-state measure, changes W_f to -W_f and fixes Y. Its invariance implies that for every center-odd target observable O_odd, E[O_odd | Y]=0 almost surely. In particular conditional half-integer character moments vanish for that Y.

For arbitrary Y there is a useful equivariance instead: any chosen z with Dz=1_f induces a map T_z on Y, and the regular conditional distributions satisfy E[O(W_f)|Y=T_z y]=E[O(-W_f)|Y=y] almost everywhere (with consistent representatives). For center-odd O, the conditional expectation is antisymmetric under T_z, not necessarily zero at fixed y.

These results give an exact support test for conditional center symmetry in the true original-link Wilson vacuum. They do NOT establish any distance-dependent cap influence bound, uniform half-Haar survival, infrared spectral estimate, or continuum Yang-Mills mass gap.
