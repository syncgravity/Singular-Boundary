# PF-I11 — Intrinsic SU(2) Wilson theory on the source \(\mathbb Z^5\) cut-and-project complex

**Checkpoint:** November 8, 2026 (America/Denver)  
**Status:** An exact **finite, gauge-invariant non-Abelian Wilson measure** and an exact finite **collapse/flat-connection/topological selection theorem** have been constructed directly on the source cut-and-project rhombi. **Not achieved:** a source-intrinsic physical time, a positive Osterwalder–Schrader reflection functional, a nontrivial four-dimensional interacting continuum Yang–Mills measure, a positive physical continuum gap, or gravitational finiteness. Every continuum proof gate remains **OPEN**.

**Source discipline.** The original computational source is the author's **unpublished** `paper6_extend_local.py`, source SHA-256 `86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da`; its filename is a working artifact, **not** a publication sequence. Source bytes are kept in Library, not committed to GitHub. We use the exact original 35%-of-maximum-tile-center selection and original five-integer labels, but independently test each two-cell using the intrinsic perpendicular-space **three-coordinate face triangle**, as proved in PF-I9. The original retained vertex populations are **never overwritten** by the separately reconstructed window-complete controls. Square/triangular/cubic lattices remain reference or negative controls, never presumed physical spacetime.

## 1. The finite intrinsic 2-complex and its chain structure

Fix the generic source offset \(\gamma\in\mathbb R^5\), \(\sum_{j=0}^4\gamma_j=0\), and source-selected finite label set \(V\subset\mathbb Z^5\) at a stated \(N_{grid}\). The physically projected direction vectors are \(e_j=(\cos(2\pi j/5),\sin(2\pi j/5))\), the internal vectors \(e_j^\perp=(\cos(4\pi j/5),\sin(4\pi j/5))\), and accepted source bonds have endpoints differing by one standard basis vector \(\mathbf e_j\).

The oriented edges of the **original coupled graph**, without any new edge insertion, are
\[
E=\{(m,m+\mathbf e_j):m,m+\mathbf e_j\in V,\ 0\le j<5\}.
\]
A four-vertex square \((m,m+\mathbf e_j,m+\mathbf e_j+\mathbf e_k,m+\mathbf e_k)\), with \(j<k\), is an **actual rhombus face** only if all four labels lie in \(V\) **and** its lower cube corner satisfies the PF-I9 independent two-fixed-coordinate acceptance test:
\[
P_\perp(m+\gamma)\in\operatorname{relint}\Big(\operatorname{conv}\big\{\sum_{a\in A}e_a^\perp:A\subset\{0,\ldots,4\}\setminus\{j,k\},\ |A|=h\big\}\Big),\quad h=\sum m_a\in\{1,2\}.
\]
The three candidate points form a triangle. **Four accepted corners without this face condition are not automatically a cell.** This builds a finite 2-complex \(K=(V,E,F)\) with no hypothesized cubic or four-dimensional physical metric.

Orient each edge from the lexicographically smaller to larger label and each face in order \(m,m+\mathbf e_j,m+\mathbf e_j+\mathbf e_k,m+\mathbf e_k\). Let \(d_0:C^0(K;\mathbb Z)\to C^1(K;\mathbb Z)\) be the signed vertex-edge incidence and \(d_1:C^1(K;\mathbb Z)\to C^2(K;\mathbb Z)\) the signed face-edge incidence. **Exact theorem PF-I11.A:**
\[
\boxed{d_1d_0=0.}
\]
**Proof:** A rhombus boundary is the oriented closed chain of four basis-neighbour edges, so the signed sum of its successive vertex differences telescopes to zero. This is the cellular boundary-of-boundary identity and holds for every accepted face independently of phason, finite crop, metric, weights, or physical interpretation. The public test checks the integer identity for the complete 1,550-vertex source complex.

## 2. Exact theorem PF-I11.B — source rhombi define a gauge-invariant SU(2) Wilson model

Assign to each oriented canonical edge an \(SU(2)\) matrix \(U_{xy}\), with \(U_{yx}=U_{xy}^{-1}\). Under independent vertex gauge choices \(g_x\in SU(2)\),
\[
U_{xy}\mapsto g_xU_{xy}g_y^{-1}.
\]
For oriented face \(f=(x_0,x_1,x_2,x_3)\), define \(U_f=U_{x_0x_1}U_{x_1x_2}U_{x_2x_3}U_{x_3x_0}\). At basepoint \(x_0\), \(U_f\mapsto g_{x_0}U_fg_{x_0}^{-1}\). Thus every \(\frac12\operatorname{ReTr}U_f\) and closed Wilson-loop trace is gauge invariant for arbitrary **noncommuting** link configurations. Any explicitly specified **nonnegative** face couplings \(\kappa_f\) define
\[
\boxed{S_\kappa(U)=\sum_{f\in F}\kappa_f\left(1-\tfrac12\operatorname{ReTr}U_f\right),\quad\kappa_f\ge0.}
\]
The finite normalized Haar partition function exists:
\[
Z_K(\kappa)=\int_{SU(2)^E}e^{-S_\kappa(U)}\prod_{e\in E}dU_e,
\quad\boxed{e^{-2\sum_f\kappa_f}\le Z_K(\kappa)\le1}.
\]
**Proof:** \(SU(2)\) is compact; \(-1\le\frac12\operatorname{ReTr}U_f\le1\), hence \(0\le S_\kappa\le2\sum\kappa_f\). Normalized product Haar measure is invariant under left and right multiplication by arbitrary gauge transformations, establishing the result and exact gauge invariance of Wilson expectations. For each fixed finite \(K\), \(Z_K\) is analytic in all finite complex coupling variables by uniform boundedness on compact coupling sets. **This finite analyticity is not a thermodynamic or continuum analyticity theorem.** QED.

**The coupling is not fixed by the scalar hopping.** For the finite tests, we take the transparent convention \(\kappa_f=\beta\). An optional **candidate** \(\kappa_f=\beta|\sin(2\pi(k-j)/5)|\) uses projected rhombus area, but has **not** been derived as a unique physical SU(2) action or four-dimensional area/Hodge volume from the author's \(2+2+1\) proposal. No physical temporal factor or arbitrary external spacetime dimension is inserted.

### A nontrivial one-plaquette SU(2) check

A single plaquette with four independent Haar links has uniform Haar-distributed holonomy. Writing its conjugacy class as \(\frac12\operatorname{Tr}U=\cos\theta\), \(d\mu_H(\theta)=\frac2\pi\sin^2\theta\,d\theta\), and a single face coupling \(\beta\ge0\),
\[
\boxed{Z_1(\beta)=e^{-\beta}\frac{2I_1(\beta)}{\beta}},\qquad
\boxed{\langle\tfrac12\operatorname{Tr}U\rangle_\beta=\frac{I_2(\beta)}{I_1(\beta)}}.
\]
The \(\beta=0\) values are defined by continuity. Independently evaluating the Haar angular integral verifies both formulas to numerical quadrature tolerance. At \(\beta=0.71\): \(Z_1=0.5232815078495338\), \(\langle\frac12\operatorname{Tr}U\rangle=0.17388540600159913\). This is a genuine finite non-Abelian interacting observable, not a scalar graph-zeta measurement or a continuum vacuum computation.

## 3. Exact theorem PF-I11.C — the actual finite 2-complexes collapse to graphs

An elementary free-face collapse removes a rhombus \(f\) and one edge \(e\subset\partial f\) belonging to **no other remaining face**. Such a deletion is a strong deformation retraction of the cell complex. The independent source verifier explicitly constructs a complete ordered list of these face-edge pairs at **all eight original source sizes**. Every face is removed; all remaining edges form a graph \(G_{rem}\) with the same connected-component count \(c\).

It follows **without a floating-point eigensolver or guessed topological dimension** that
\[
\boxed{K\simeq G_{rem},\qquad\pi_1(K)\cong F_r,\quad H_1(K;\mathbb Z)\cong\mathbb Z^r,\quad H_2(K;\mathbb Z)=0,\quad r=E-F-V+c,}
\]
where \(F_r\) denotes the free group on \(r\) generators, computed independently as the number of surviving graph chords outside a spanning forest. This is an **explicit finite combinatorial collapse certificate**, not merely a Betti-number guess based on Euler characteristic.

### Exact original-source and independent completed-window results

| \(N_{grid}\) | Original \(V\) | Original \(E\) | Original \(F\) | Components \(c\) | Original \(r\) | Full-window core \(V\) | Full-window \(c\) | Full-window \(r\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 1,550 | 3,017 | 1,468 | 1 | **0** | 1,432 | 1 | 0 |
| 10 | 3,042 | 5,927 | 2,886 | 1 | **0** | 3,032 | 1 | 0 |
| 12 | 4,324 | 8,468 | 4,145 | 1 | **0** | 4,294 | 1 | 0 |
| 15 | 6,980 | 13,779 | 6,800 | 1 | **0** | 6,812 | 1 | 0 |
| 18 | 9,950 | 19,593 | 9,646 | 3 | **0** | 9,912 | 1 | 0 |
| 20 | 12,207 | 24,091 | 11,879 | 1 | **6** | 12,172 | 1 | 0 |
| 23 | 16,435 | 32,582 | 16,138 | 1 | **10** | 16,182 | 11 | 0 |
| 25 | 19,260 | 38,139 | 18,874 | 5 | **10** | 19,256 | 1 | 0 |

The **full-window controls** use the PF-I9 intrinsic four-window and face-triangle BFS with a collar, and the **full incident-star** 35%-tile-center criterion. They are separate populations, never replacements for the published original source vertices. Every face also collapses in these controls. Their first homology is zero at all eight sizes, even where the original retained populations have free cycles; the corrected \(N_{grid}=23\) core has 11 disconnected components but no unfilled cycles.

**Conclusion:** Nontrivial finite first homology in the original \(N_{grid}=20,23,25\) selections is **selection-dependent**, and cannot currently be promoted into a persistent topological sector of the infinite cut-and-project hull or a physical four-dimensional gauge vacuum. No exact equivalence of original and corrected finite boundary conditions is asserted.

## 4. PF-I11.D — explicit non-Abelian flat Wilson configurations on the source-only cycles

For a cell complex collapsing onto a graph, specifying group elements along the surviving independent graph chords and identity along a spanning forest defines arbitrary homomorphisms \(\pi_1(K)\to SU(2)\). One can then **restore the removed face-edge pairs in reverse order**. At each step exactly one edge holonomy is unknown in a given rhombus, and it can be set to the inverse ordered product of the three known links. Consequently **every plaquette holonomy equals the identity** in the recovered configuration.

For \(r\ge2\), choose two chords in the **same connected component** with holonomies
\[
A=\cos(0.71)+\mathbf k\sin(0.71),\qquad B=\cos(0.47)+\mathbf i\sin(0.47),
\]
using the unit-quaternion representation of \(SU(2)\). They do not commute. A common-basepoint fundamental-loop commutator has conjugation-invariant half-trace
\[
\boxed{\tfrac12\operatorname{Tr}(ABA^{-1}B^{-1})=0.8257061558671013\ne1.}
\]
The source-based code explicitly constructs these flat non-Abelian link assignments at \(N_{grid}=20\) and 25, checks the **maximum plaquette identity defect is zero within floating-point tolerance**, and checks \(S_{\beta=1}(U)=0\). Fundamental loop half-traces are \(\cos(0.71)=0.7583618759905082\) and \(\cos(0.47)=0.891568288195329\).

**What is proved:** the finite source-selected Wilson plaquette potential has distinct, gauge-inequivalent **classical flat sectors** when its source finite two-complex contains free cycles. It cannot distinguish these sectors using only the source-selected face terms. **What is NOT proved:** the fully interacting *quantum* theory is gapless, or that these cycles remain in a source-faithful infinite-volume exhaustion. A separately defined kinetic/transfer operator can lift or mix classical flat directions; its physical construction remains an obligation.

### Linearized gauge-compatible flat-mode dimension

With \(U_e=\exp(i\epsilon a_e\cdot\sigma)\) near the trivial connection, the Wilson quadratic form is proportional to \(\sum_f\kappa_f\Vert(d_1a)_f\Vert^2\). The local pure-gauge tangent space is \(\operatorname{im}d_0\), since \(d_1d_0=0\). For positive \(\kappa_f\) and our complete free-face collapses, \(\operatorname{rank}d_1=F\), so
\[
\boxed{\dim\ker(d_1\otimes\mathbb R^3)-\dim\operatorname{im}(d_0\otimes\mathbb R^3)=3r.}
\]
At grid 20, 23, 25, there are respectively **18, 30, 30** extra **linearized classical** flat directions beyond gauge. The completed-window cores have **zero** extra such directions. This is not a positive- or zero-**quantum**-mass-gap theorem.

## 5. Exact theorem PF-I11.E — the complete finite rhombus Wilson partition **factorizes**

The explicitly certified free-face collapses imply a stronger result than positivity. They allow exact integration of **every** source rhombus plaquette one by one, even when the residual graph carries nontrivial free holonomies.

**Theorem.** Let a finite 2-complex be built from oriented edges carrying independent normalized Haar \(SU(2)\) variables, and suppose its faces admit an elementary free-face collapse to a graph. Let its action contain **only** independent single-rhombus Wilson terms with fixed nonnegative \(\kappa_f\). Then
\[
\boxed{Z_K(\{\kappa_f\})=\prod_{f\in F}z(\kappa_f),\qquad z(\kappa)=e^{-\kappa}\frac{2I_1(\kappa)}\kappa,\quad z(0)=1.}
\]
More generally, the joint probability measure of the individually based plaquette-holonomy matrices has product form in suitable free-edge variables, and in particular for distinct \(f\neq g\)
\[
\boxed{\operatorname{Cov}_\kappa\!\left(\tfrac12\operatorname{Tr}U_f,\tfrac12\operatorname{Tr}U_g\right)=0,\quad
\left\langle\prod_{f\in A}\tfrac12\operatorname{Tr}U_f\right\rangle
=\prod_{f\in A}\frac{I_2(\kappa_f)}{I_1(\kappa_f)}.}
\]
All Haar integrations over surviving graph edges, including flat-cycle chords, contribute **1** to the partition function. A noncontractible loop chosen as a chord and its spanning-tree return path carries an independent Haar holonomy; its fundamental Wilson half-trace has expectation **zero** under this plaquette-only Gibbs measure.

**Proof.** At the first elementary collapse pair \((f,e)\), the oriented link variable \(U_e\) occurs in exactly one currently remaining plaquette term \(U_f\). Holding all other links fixed, the plaquette holonomy has form \(A U_e^{\pm1}B\), with \(A,B\in SU(2)\) determined by the other links. By left-right bi-invariance of normalized Haar measure and invariance under inversion,
\[
\int dU_e\,e^{-\kappa_f(1-\frac12\operatorname{Tr}(A U_e^{\pm1}B))}=z(\kappa_f),
\]
independently of the other link variables. If a test function of the plaquette holonomy is inserted, the same change of variables yields its standard one-face Haar expectation. Removing the integrated face leaves precisely the next free-face-collapsible complex. Induction over **all** faces proves the product formulas and independence of distinct plaquette class functions. The surviving graph links are independent Haar variables once all faces have been integrated. Their fundamental graph-cycle holonomies are Haar after gauge-fixing a spanning forest, giving zero expected fundamental trace. QED.

**Exact numerical consequence on the recovered source geometry.** Every one of the eight original retained and eight separately completed-window source complexes has an explicit full face-collapse certificate. For the **illustrative** constant \(\kappa_f=0.71\),
\[
\boxed{\frac1{|F|}\log Z_K=\log z(0.71)=-0.6476357037985244}
\]
for all **16** finite complexes, notwithstanding their different graph components and (for the original source) nonzero free-group ranks. The full \(\log Z_K\) depends on the number of faces; a family/area-dependent fixed coupling makes it depend on the corresponding face-weight histogram but **not on additional link-mediated plaquette correlations**. An independent, seeded Haar-link Monte Carlo experiment on two adjacent squares (seven independent links, shared edge) agrees with the exact product partition function within **0.32 of its sampling standard error**; the exact independence theorem is the sequential Haar proof, not a Monte Carlo conjecture.

**Interpretive limitation and proof consequence.** The finite action is nonlinear, non-Abelian, positive and gauge invariant, but **a plaquette-only Wilson measure on this two-complex is exactly solvable and has no connected correlations between distinct single-face traces**. This is neither a physical proof of a gap nor proof of its absence. The dissertation's proposed nontrivial \(2+2\) sector coupling, spectral geometry, physical evolution and full interacting gauge dynamics would require *additional source-justified structure*, such as genuinely coupled cross-sector terms, a higher-dimensional cell/field construction, or another explicitly derived dynamical prescription. Such terms may break factorization, but none has been proven or inferred from the scalar PF-I10 ratios. A conventional cubic background cannot fill this logical gap.

## 6. Reflection, evolution and the conditional auxiliary transfer

The intrinsic \(\mathbb Z^5\) construction supplies a \(2+2+1\) decomposition and genuine accepted rhombi, but **does not, by these facts alone, select a distinguished physical time, an involutive reflection of the finite measure, or a transfer semigroup encoding physical energy**. The source does not identify a unique coupling \(\kappa_f\) as a function of the two nontrivial sectors, a four-dimensional volume element, or a coupling flow. None is invented here.

A **restricted** check of the nine nonidentity literal dihedral permutations of the five integer basis indices shows one exact weighted face-complex reflection at source sizes 7 and 12, but **none** at source size 25 under the same candidate class. This is merely a statement about untranslated source-retained label and weighted-face symmetries; the surviving small-patch symmetry is not a temporal reflection, and failure at 25 does not rule out a different phason, translation, hidden-sector or emergent-time involution.

For comparison only, independently **add** a positive SU(2) Casimir kinetic operator \(C\), a positive parameter \(\tau\), and multiplication \(M_{\tau}=e^{-\tau S/2}\) on a gauge-invariant Hilbert space. The operator
\[
T_{\tau}=M_{\tau}\,e^{-\tau\epsilon C}\,M_{\tau}
\]
is positive and symmetric because \(\langle\psi,T_{\tau}\psi\rangle=\langle M_{\tau}\psi,e^{-\tau\epsilon C}M_{\tau}\psi\rangle\ge0\). The Casimir heat kernel commutes with gauge transformations, so this **auxiliary** transfer preserves gauge-invariant functions. In a finite SU(2) conjugacy-class character truncation \(\chi_j\), we verified the positive transfer matrix \(M\operatorname{diag}(e^{-\tau\epsilon j(j+1)})M\) independently with Haar quadrature. At zero face coupling, its gap is exactly \(3\epsilon/4\); taking \(\epsilon\to0\) makes this auxiliary gap vanish even with the same underlying finite group space. **Finite positivity/finite gaps and geometrical scalar spectra are not a nontrivial uniform interacting Yang–Mills mass-gap argument.** This auxiliary evolution is **not** source-derived physical time, and its positivity is **not** an established reflection-positivity theorem for an intrinsic four-dimensional Euclidean Yang–Mills measure.

## 7. Status of proof gates and exact next requirements

**Completed FINITE subgates:**

1. Original-source accepted \(\mathbb Z^5\) vertices and weighted-basis edges, with face membership checked independently by the actual three-coordinate window triangles; exact cellular chain identity \(d_1d_0=0\).
2. Genuine noncommuting, gauge-invariant SU(2) rhombus Wilson action; finite normalized positive analytic Haar partition and exact one-face benchmark.
3. Complete elementary-collapse witness for all eight original source two-complexes and all eight independent corrected-window controls, with exact free fundamental-group ranks, first homology and flat moduli.
4. Explicit gauge-inequivalent non-Abelian flat link assignments for original source sizes 20/25 and exact linearized gauge/Hessian nullity interpretation.
5. **Exact independent-plaquette Haar factorization and zero distinct-plaquette trace covariance** on all 16 source and completed-window complexes, with a finite shared-edge Monte Carlo crosscheck.
6. Restricted D5 source-symmetry test and separately labeled **auxiliary** transfer countercheck.

**Still OPEN and necessary:**

- **PF-I11 temporal/reflective gate:** Derive from the actual accepted \(2+2+1\) sectors a physically meaningful four-dimensional dynamical/geometric prescription and, if the Osterwalder–Schrader route is intended, an exact finite-volume involution, reflection-positive gluing/action and a coherent limiting Hilbert-space reconstruction. Neither a cubic lattice nor a chosen auxiliary \(\tau\) counts as this derivation.
- **Finite-volume gauge/continuum interface:** Specify the canonical **window-complete, phason-aware exhaustion**, boundary conditions and renormalized Wilson/curvature measure, including the source-dependent source/original defects and \(N_{grid}=23\) corrected-component anomaly. Derive rather than guess the plaquette-coupling/measure normalization in the 2+2 geometry.
- **Physical Yang–Mills existence/gap:** Define genuine interacting gauge-invariant observables and dynamics, prove a nontrivial continuum limit with a proper physical energy operator, and establish a **uniform strictly positive physical mass gap** under that limit. Classical finite degeneracy and finite transfer positivity cannot substitute for these.
- **Separate gravity gate:** None of these finite Wilson results establishes a gravitational one-loop determinant/UV theorem.

**Recommended next objective PF-I12:** derive or falsify a source-intrinsic candidate for temporal/reflection geometry, specifying an involution and a gluing rule on the actual window-complete 2+2+1 cochains. Establish a reflection-positive interacting gauge measure or a mathematically explicit obstruction **before** pursuing a continuum gap through transfer/operator methods. No conventional cubic physical spacetime assumption is authorized by this checkpoint.

## 8. Files, reproducibility and source privacy

- `verify_pf_i11_intrinsic_su2.py`: source-checksum-locked accepted rhombus complex, independent triangle membership, exact elementary collapse, SU(2) quaternion links/Wilson action, explicit noncommuting flat witness and one-face Haar identity.
- `verify_pf_i11_completed_core.py`: separate source-independent full-window collar control, never overwriting the original source vertex population (requires PF-I9 `verify_pf_i9_source_cut_project_bridge.py`).
- `verify_pf_i11_reflection_candidates.py`: restricted untranslated D5 symmetry check; no claims of physical time.
- `verify_pf_i11_auxiliary_transfer.py`: optional finite SU(2) conjugacy-character control, explicitly **not** an intrinsic temporal model.
- `test_pf_i11_intrinsic_su2.py`, `test_pf_i11_auxiliary_transfer.py` and `test_pf_i11_plaquette_factorization.py`: **27 passing tests** with the original private source, including exact integer incidence, random gauge covariance, nonabelian flat holonomy, one-face Haar/Bessel agreement and auxiliary Casimir parameter dependence. Public checkout runs 19 source-independent tests, skipping eight private-source-dependent tests when the original unpublished script is unavailable.
- `verify_pf_i11_plaquette_factorization.py` and `PF_I11_EXACT_FACE_HAAR_FACTORIZATION.json`: exact sequential-Haar product theorem over all 16 collapsible source/control complexes, plus independent two-adjacent-square SU(2) Haar simulation.
- `PF_I11_EIGHT_SIZE_SOURCE_GAUGE_COMPLEX.json`, `PF_I11_COMPLETED_WINDOW_CORE_CONTROL.json`, `PF_I11_SIMPLE_D5_REFLECTION_CANDIDATES.json`, `PF_I11_AUXILIARY_TRANSFER_CONTROL.json`: deterministic machine-readable evidence. Full original source, vertex/edge/face arrays, collapse witnesses and explicit flat link quaternions are pinned by SHA-256 and stored **privately in Library**.

No proof gate is claimed to close merely because its finite part is constructed. The dissertation is an **unpublished historical reference**, and any conflicts between draft scripts are resolved through matching mathematics and reproducible source bytes, not their filenames.
