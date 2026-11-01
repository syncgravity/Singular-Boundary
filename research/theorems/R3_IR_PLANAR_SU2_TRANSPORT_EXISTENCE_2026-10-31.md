# R3-IR — Planar SU(2) deleted-face transport existence via tree–cotree coordinates

Date: 2026-10-31. Exact finite planar disk theorem; **not** a bound on transport electric-metric defect, radial current, or mass gap.

## Statement
Let G be a finite connected graph cellularly embedded in a closed disk, with all bounded faces simply connected, each edge incident to one or two faces, and connected planar dual (including the exterior face). On the original-link configuration space SU(2)^E with product Haar measure, choose a bounded target face f and fixed oriented boundary word W_f based at a vertex of f. There is a measurable (smooth for a fixed finite graph) family of measure-preserving bijections T_g, indexed by g in SU(2), such that

(1) W_f(T_g U)=g W_f(U), and
(2) for every bounded face k != f, p_k(T_g U)=p_k(U), where p_k=Tr W_k/2.

Indeed, one can preserve each **based** face holonomy at a common root, stronger than preserving only its trace. The family is a genuine SU(2) action in suitable coordinates: T_g T_h=T_(gh) (depending on convention of pullbacks and orientation). The construction uses the actual *product-Haar link variables* and no abelian approximation. It is generally **not** an isometry of the original-link electric metric, so it is not a Hamiltonian symmetry.

## Proof
Pick a root vertex r and a spanning tree S of primal edges. The tree edges carry independent Haar variables; together with the remaining |E|-|V|+1=|F| edges they form a smooth product-coordinate decomposition, obtained by left/right multiplication and inverses. Use the tree parallel transports to define based link variables Q_e=G_source(e) U_e G_target(e)^(-1) on non-tree edges. All tree Q_e are identity, and product Haar measure disintegrates into independent Haar measures for tree variables and non-tree Q_e. This follows by successive bi-invariant Haar substitutions and the triangular tree ordering, with no Faddeev–Popov determinant.

The primal complement of S is a spanning tree S* of the planar dual graph rooted at the exterior face. For each bounded face k, let e(k) be the unique dual-parent edge joining k toward the exterior. In an order starting at exterior-adjacent dual leaves and continuing toward the interior (equivalently choose an orientation of the dual tree and solve leaf-to-root), the based face word H_k=G_b W_k G_b^(-1), where G_b is the appropriate tree transporter from the face basepoint b to r, depends on its own non-tree edge Q_(e(k)) exactly once and on coordinates corresponding to the dual descendants; the change from all non-tree Q_e to all H_k is triangular up to inversion and left/right multiplication. Therefore product Haar in the Q coordinates becomes product Haar in the based face holonomies H_k. Together with the independent tree variables this gives a global smooth bijection (after fixed convention choices)

  SU(2)^E  ≅ SU(2)^(V-1) × SU(2)^F,

which sends product Haar to product Haar. Note that this coordinate map is not an electric isometry and depends on tree choices. Choose a fixed based target H_f. Replace H_f by h H_f while retaining all other H_k and tree variables. Taking h=G_b g G_b^(-1) (or inverse conjugation, depending on the convention H_f=G_b W_f G_b^(-1)) ensures W_f maps exactly to g W_f. The conjugating transporter depends only on the unchanged tree variables, hence left multiplication remains Haar preserving on the H_f coordinate. Pull back this operation through the coordinate bijection to obtain T_g. Since each other based plaquette H_k is unchanged, every other p_k is unchanged. The dependence on g defines an action because the tree variables remain fixed. QED.

## Geometry and limitations
The result applies to simply connected planar cages; it is **not established by this proof on the periodic Stage26 Penrose torus**, where |E|-|V|+1=|F|+1 and noncontractible holonomies plus global plaquette constraints enter. The positive result establishes the transport-family existence hypothesis of the archived transport-twirl theorem on disk cages. It does **not** control the spectral gap γ or vacuum-averaged metric defect Q_g, hence does not yield Haar proximity, a positive small-cap bound, or a current estimate.

The distinction is important: the exact SU(2) plaquette Haar independence is a statement about the *reference measure*, not independence under the interacting Hamiltonian ground-state measure. The transformed ground state need not equal the original ground state because the electric kinetic operator is not preserved.

## Verified diagnostic
A deterministic Python script enumerates square grid disks and checks Euler identity E−V+1=F, primal-tree complement dual-tree connectivity and acyclicity, and that each face has exactly one dual-parent edge, including an interior target. The combinatorial diagnostic is not a numerical vacuum calculation. The group-Haar coordinate argument above supplies the theorem.

OPEN: quantitative electric-metric-defect vacuum estimate without inserting an unproved uniform physical gap; radial current sup_f T_(f,h)=o(h^(−1/4)); covariance and continuum mass gap.