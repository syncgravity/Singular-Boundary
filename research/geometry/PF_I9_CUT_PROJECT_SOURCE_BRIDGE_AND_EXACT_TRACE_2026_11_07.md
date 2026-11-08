# PF-I9 — Four-slice cut-and-project bridge, missing-face explanation, and exact source \(\zeta(-1)\) reproduction

**Date:** 7 November 2026 (America/Denver research checkpoint).  
**Research object:** the author's **unpublished** Penrose / Fibonacci \(\mathbb Z^5\) finite-graph program, identified by what the scripts actually compute rather than draft paper numbering.  
**Source executable:** `paper6_extend_local.py` (user-supplied; SHA-256 `86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da`), specifically `make_generic_gamma`, `build_penrose_tiling`, `select_interior_vertices`, `fibonacci_hopping`, `build_coupled_z5_laplacian`, and `build_periodic_laplacian`.  
**Status:** exact linear-algebra and cut-and-project lemmas plus **reproducible finite eight-size source/operator identities**. This is a source implementation bridge, **not** a continuum non-Abelian quantum field, an emergence-of-physical-time theorem, a mass-gap proof, or a gravity finiteness theorem. It does **not** supersede the author's working reference corpus or other unpublished drafts.

## 1. Objective and why the distinction matters

Previously PF-I2 used a newly written dual-pentagrid line-crossing enumerator and then inferred consequences about the 2D P3 graph. PF-I6/PF-I7 subsequently recovered author-provided scripts and found that the source's tile-edge Laplacian and all-five-direction basis-neighbour Laplacian differed at finite `N_grid=10,12` by 62 and 85 edges. The missing issue was **whether the source's finite tile enumeration, cut at pentagrid line levels [-N_grid,N_grid], contains all genuine faces of the complete accepted \(\mathbb Z^5\) cut-and-project geometry in its central 35%-tile-radius region.**

PF-I9 uses a new, independently executed generator **based only on integer labels and four hypersimplex acceptance-window membership**, then tests the original published-size source script's vertex, face, edge, hopping and finite-crop rules. The source grid-line generator is **not** called by the new graph constructor. Source code is called separately to supply the original gamma, center/cutoff and original comparison graph. All comparisons are by **five-integer labels** and canonical source Fibonacci type, not by visually similar images or spectral ratios.

The central finding is that the source code's finite pentagrid line range omits **genuine rhombus faces inside its own declared 35%-tile-center selection radius**. Once all window-admissible faces are restored on the *unchanged source vertex set*, every apparent additional coupled basis-neighbour edge becomes an ordinary rhombus tiling edge. This does **not** mean the two *executed source matrices* were identical: they were genuinely different at finite truncation and remain faithfully preserved. It identifies their difference as a **source finite-crop incompleteness**, not evidence of a new intrinsic neighbour relation in the full cut-and-project tiling.

## 2. Theorem PF-I9.A — exact four-slice window equivalence for generic cell labels

Let \(e_j=(\cos(2\pi j/5),\sin(2\pi j/5))\) and \(e_j^\perp=(\cos(4\pi j/5),\sin(4\pi j/5))\), for \(j=0,\dots,4\). Then \(\sum_j e_j=\sum_j e_j^\perp=0\) and the row spaces of \(E_\parallel\), \(E_\perp\), and \(\mathbf1=(1,1,1,1,1)\) are mutually orthogonal and span \(\mathbb R^5\). **No three-dimensional or cubic physical regulator is assumed.**

For the source's generic shift \(\gamma\in\mathbb R^5\) with \(\sum_j\gamma_j=0\), define the four **distinct internal windows**

\[
W_h=\left\{\sum_{j=0}^4u_je_j^\perp:0\le u_j\le1,\ \sum_j u_j=h\right\},\qquad h\in\{1,2,3,4\}.
\]

These are projected hypersimplex sections, not one ad hoc decagonal window assigned to all height layers.

**Theorem.** For any generic integer label \(m\in\mathbb Z^5\), the source cell formula
\[
  m_j=\lceil x\cdot e_j-\gamma_j\rceil\quad\text{for some }x\in\mathbb R^2
\]
with all grid expressions noninteger is **equivalent** to
\[
  h=\sum_jm_j\in\{1,2,3,4\},\qquad
  \sum_j(m_j+\gamma_j)e_j^\perp\in\operatorname{relint}W_h.
\]

**Proof.** Given a generic cell point \(x\), put \(u_j=m_j+\gamma_j-x\cdot e_j\in(0,1)\). The zero sums give \(\sum_ju_j=\sum_jm_j=h\). Projecting against the perpendicular basis gives \(\sum_j u_je_j^\perp=\sum_j(m_j+\gamma_j)e_j^\perp\); the physical term drops out by orthogonality. Thus this internal point belongs to \(\operatorname{relint}W_h\). Conversely, by the relative-interior image theorem for linear projections of a polytope, every point of \(\operatorname{relint}W_h\) has an inverse \(u\) with \(0<u_j<1\), \(\sum_ju_j=h\) and the same perpendicular projection. Set \(v=m+\gamma-u\). It is orthogonal to the perpendicular two-plane and to \(\mathbf1\), so it lies in the physical two-plane; hence \(v_j=x\cdot e_j\) for some \(x\). Rearranging \(m_j=x\cdot e_j-\gamma_j+u_j\), with \(0<u_j<1\), gives the source ceiling formula. **QED.**

This is a statement about the **original \(2+2+1\) algebra**, not a claim that the second two-plane has yet been physically established as temporal evolution.

## 3. Theorem PF-I9.B — a genuine rhombus has its own smaller acceptance triangle

Vertex acceptance alone should not be silently promoted to finite face enumeration. For each pair of grid families \(j<k\) and a proposed lower corner \(m\), let \(h=\sum_jm_j\in\{1,2\}\). The **face window** is
\[
 T_{jk,h}=\left\{\sum_{f\notin\{j,k\}}u_fe_f^\perp:
 0\le u_f\le1,\quad\sum_{f\notin\{j,k\}}u_f=h\right\}.
\]
With three remaining families, it is a triangle (the image of the 3-coordinate unit-cube slice of height 1 or 2).

**Face criterion:** The four accepted lattice labels \(m,m+\mathbf e_j,m+\mathbf e_j+\mathbf e_k,m+\mathbf e_k\) form a genuine cut-and-project rhombus precisely when the internal projection of \(m+\gamma\) lies in \(\operatorname{relint}T_{jk,h}\), under the same genericity assumptions.

**Proof.** On the physical line-family intersection, the two fixed coordinates of \(u=m+\gamma-E_\parallel x\) are zero and the remaining three are strictly between zero and one, with sum \(h\). The perpendicular projection yields the triangle condition. Conversely a strict triangle preimage gives those two equality constraints and the other three strict strip constraints, and the orthogonal decomposition recovers the physical intersection. **QED.**

The independent `verify_source_cut_project_bridge.py` explicitly tests both **vertex windows** and **face triangles**, and reconstructs finite faces from accepted basis-neighbour squares without invoking the source line-crossing loops.

## 4. Theorem PF-I9.C — completed rhombus edges and all accepted basis edges agree

On the **complete** generic cut-and-project graph, any two accepted labels \(m,m+\mathbf e_j\) correspond to adjacent convex pentagrid cells with the same four other strip constraints and consecutive strips in family \(j\). If both are feasible, choose a point in each. A segment between them lies strictly inside their four common strip constraints; by continuity it crosses the common family-\(j\) dividing line. Genericity prevents simultaneous crossings with a second family; the dividing segment is an actual tiling edge adjacent to rhombi. Therefore the complete rhombus-edge adjacency equals the accepted original-basis-neighbour adjacency. Restricting both complete edge dictionaries to **any common accepted vertex subset** preserves this equality. **QED**, conditional on the same generic infinite completed parent tiling, not on an incomplete finite face enumerator.

In particular, **the source's “coupled” finite graph need not introduce any intrinsic extra original-basis edges beyond those of the full quasicrystal tiling**. It can nonetheless have different finite adjacency from its truncated tile-edge source graph; the distinction is real and attributable to the finite enumeration rule.

## 5. Eight-size source-code comparison — exact face and edge support

The author source uses `n_range=arange(-N_grid,N_grid+1)` for generating intersections, then selects **tiles** with centers at distance `<0.35*max_tile_center_distance` from the full finite-patch mean vertex position. It retains vertices for which **all enumerated incident tiles** belong to that selected set. In PF-I9, a direct window BFS accepts original five-integer labels within a **4-unit radial collar** beyond the same source-defined center and cutoff, then constructs every face satisfying the triangle window and computes the same one-pass selection from **all completed local incident tiles**.

| Source `N_grid` | Original retained vertices | Genuine accepted rhombi missing **inside** the source 35% tile-center disk | Source coupled edges missing from its tile-only graph | Full-star direct-window retained vertices | Components of original coupled graph |
|---:|---:|---:|---:|---:|---:|
| 7 | 1,550 | 28 | 0 | 1,432 | 1 |
| 10 | 3,042 | 210 | 62 | 3,032 | 1 |
| 12 | 4,324 | 234 | 85 | 4,294 | 1 |
| 15 | 6,980 | 430 | 290 | 6,812 | 1 |
| 18 | 9,950 | 730 | 444 | 9,912 | 3 |
| 20 | 12,207 | 842 | 593 | 12,172 | 1 |
| 23 | 16,435 | 1,199 | 889 | 16,182 | 1 |
| 25 | 19,260 | 1,522 | 1,066 | 19,256 | 5 |

**All eight** source-retained integer-label sets were found among the independent direct-window accepted vertices. For each source `N_grid`, **every source-selected face appears in the independent direct-window-selected face set**, and **every additional selected face has at least one crossing grid level outside the source's enumerated `[-N_grid,N_grid]` range** (overshoot by one, two or three levels). Not every omitted face creates a new graph edge because its four edges can already be present via other faces.

Critically, for **the unchanged original retained source vertex set** at all eight sizes:

\[
\boxed{E_{\mathrm{coupled,source}}=E_{\mathrm{tile,completed\ window}}}
\]

The **original** tile edges form a subset of this completed edge set. The difference has exactly 0, 62, 85, 290, 444, 593, 889 and **1,066** edges, respectively. Every one of these extra coupled edges has a **specific genuine omitted-rhombus witness** in the independently constructed face list, and retains the same original-index Fibonacci family, level and hopping type. Canonical SHA-256 signatures of the **complete integer-label, family, level, Fibonacci-type edge dictionaries** agree exactly for original source coupling and completed-window tile adjacency.

The largest explicitly source-truncated graph has **37,073** tile-only edges and **38,139** coupled/basis edges. On the **same retained 19,260 labels**, completion of missing rhombi raises its tile-edge support to **38,139**.

**The finite cores must not be conflated.** The direct-window full-incident-face one-pass core is an **alternative corrected crop** under exactly the source's centering and radius rule. It does not retroactively overwrite the source's originally recorded finite operator or 19,260 vertex count. At sizes 20, 23 and 25, the direct method also finds 3, 30 and 26 accepted vertices, respectively, inside a conservative common inner disk that were not enumerated at all by the finite source pentagrid. At size 25 the direct-window full-star core has 19,256 labels, **not the same 19,260 original labels** (74 original labels removed and 70 added). The chosen corrected crop itself can have disconnected tiny edge components (at size 23, 11), so its connectedness must be checked, not assumed. The cubic lattice is not implicated in any geometry of this proof.

The independent BFS construction was repeated with a **6-unit** versus **4-unit** collar at sizes 7, 12 and 25; selected-face counts, corrected-core label/edge SHA-256 fingerprints and original-source edge fingerprints were unchanged. The original source Python file was **not modified** and no existing numerical archive was overwritten.

## 6. Exact PF-I9.D — reproduce Paper 2's \(R(-1)=0.7371\) without eigenvalue fitting

The **same** recovered source explicitly defines the coupled Laplacian by **weighted vertex strength**, \(L=D_w-W\), with Fibonacci bonds
\[
 t(j,k)=\begin{cases}1,&\lfloor(k+1)/\varphi\rfloor\ne\lfloor k/\varphi\rfloor,\\
 \varphi^{-2},&\text{otherwise.}\end{cases}
\]
The periodic comparator is a finite zigzag **triangular lattice** of side \(q=\lfloor\sqrt{N_{QC}}\rfloor\), **not equal vertex count**, and every periodic edge has **\(t_{avg}=(1+\varphi^{-2})/2\)** rather than unit conductance. The source's triangular construction has exactly \((q-1)(3q-1)\) edges, giving
\[
 \frac1{N_{per}}\mathrm{Tr}L_{per}
 =\frac{2(q-1)(3q-1)t_{avg}}{q^2}.
\]

For the Penrose weighted-strength matrix, exactly
\[
 \frac1{N_{QC}}\mathrm{Tr}L_{QC}=\frac2{N_{QC}}\sum_{e\in E_{\rm basis}} t_e.
\]
Thus for a finite regulated full-spectrum normalized scalar zeta,
\[
 R_{N}(-1;m^2)=
 \frac{m^2+2N_{QC}^{-1}\sum_e t_e}
 {m^2+2(q-1)(3q-1)t_{avg}/q^2}.
\]

**Every input here comes from the source implementation; no periodic hopping was fitted.** The triangular edge-count formula was independently checked against the source's *actual generated dense periodic matrix* at `N_QC=1,550` and `N_QC=3,042`. The source's coupled matrix at 1,550 vertices was independently built and checked entrywise for edge count, weighted trace and zero row sums. No full-spectrum eigensolver was used for the eight-size trace identity.

| Source `N_grid` | Exact source-defined \(R_N(-1;m^2=10^{-4})\) |
|---:|---:|
| 7 | 0.73704717 |
| 10 | 0.73387442 |
| 12 | 0.74144891 |
| 15 | 0.73856312 |
| 18 | 0.73492392 |
| 20 | 0.73390653 |
| 23 | 0.73932113 |
| 25 | 0.73736847 |

The eight-size arithmetic mean is
\[
 \boxed{\bar R(-1;10^{-4})=0.7370567093342758},
\]
which is **0.7371** at the source's four-decimal precision. Its ordinary eight-point sample standard deviation is \(0.0027094\). For \(m^2=0\), the mean is \(0.7370502535994539\), also 0.7371 at four decimals. Excluding graph zero modes and normalizing by retained positive-mode counts instead gives \(0.7370920659420762\) at \(m^2=10^{-4}\), likewise 0.7371 at four decimals. **The reported mean alone does not distinguish the mass or zero-filter convention**; the source code is necessary for that.

This resolves PF-I3's **conditional** apparent conflict under *unit* periodic conductance: **the actual recovered source periodic conductance is \(t_{avg}\ne1\)**. PF-I3's algebraic trace identity was right; assuming the unit-bond comparator was not source-authenticated. The published `R(-1)` is internally reproducible under the correct source normalization.

There is also a source-defined **exact** same-graph factorization at \(s=-1\):
\[
 \frac{\zeta_{fib}}{\zeta_{per}}=
 \frac{\zeta_{fib}}{\zeta_{uni}}\times\frac{\zeta_{uni}}{\zeta_{per}},
\]
with \(\zeta_{uni}\) on **the same accepted coupled graph**, uniformly weighted at \(t_{avg}\). The first factor in this specific moment is determined entirely by the source's weighted mean edge strength; by itself it does not prove a nontrivial interacting field effect.

**Remaining spectral gate:** source-matched `R(-1/2)`, \(\zeta'(0)\), full eigenmode lists, the determinant and their continuum convergence have **not** been independently reproduced for the largest sizes in this checkpoint.

## 7. PF-I9.E — zero-mode count explains the *later five* draft-table differences

For every finite graph with positive weights, \(\dim\ker(D_w-W)\) equals its number of connected components. Without computing eigenvalues, the **actual source coupled graph dictionaries** yield nullities
\[
 (1,1,1,1,3,1,1,5)
\]
for `N_grid=(7,10,12,15,18,20,23,25)`.

The separate draft tables previously compared by PF-I4 list `N_int` differences
\[
(0,0,0,1,3,1,1,5).
\]

**The last five differences agree exactly with source graph nullities.** In fact, at grid 18 the original graph components have sizes `(9946,2,2)` and at grid 25 `(19252,2,2,2,2)`. This strongly supports **zero-mode deletion for the later five rows** as an explanation, and retracts the prior implication that the values 3 and 5 cannot be connected to source geometry. The first three rows still show zero difference despite their graph having one zero mode, so the **source table's denominator convention is apparently mixed**; the original reporting code must establish exactly why. Do not claim all eight N values have been conclusively explained by one uniform rule.

This also matters for comparisons of nonlinear finite spectral functionals: a graph's disconnected small components and mode exclusions can influence the positive-mode averages, although at \(s=-1\) their impact on a 19,260-site graph is small.

## 8. Accepted, rejected and still-open proof obligations

**Mathematically established:** four-layer internal-window equivalence for generic cell labels; corresponding face-triangle rule; basis-neighbour implies genuine adjacency on the **complete** cut-and-project parent tiling. These are intrinsic 2+2+1 projection statements, not new spatial/dimensional assumptions.

**Reproducibly finite under exact source gamma and crop parameters:** all eight source size vertex counts, every selected original face included in the complete window list; all missing selected faces have excluded crossing levels; all source-coupled extra edges are recovered genuine tile edges on the **same source retained vertices**; original and complete dictionary weights agree; source periodic comparator trace gives eight-size `R(-1)` mean **0.7371**; the later five retained-N differences match the components/nullities exactly. The new finite cropped accepted core is explicitly **different** from the published original.

**Still OPEN:** independent full-spectrum `R(-1/2)` and `ζ′(0)` on source-identical matrices; phason and boundary stability of the infinite/operator limit; a physically justified SU(2) interacting lattice model, observables and Ward/OS construction; physical time emergence from the internal structure; uniform thermodynamic/continuum control; strict positive interacting mass gap; gravitational effective action and UV conclusions. None of these is inferred from scalar traces or source face repairs alone.

**Next decisive proof obligation:** build the exact source-coupled weighted sparse operator, with source positive-mode and periodic conventions explicitly sealed, and independently reproduce `R(-1/2)` and the mass-relative determinant across sizes **without conflating original cropped vertices with the completed-window corrected core**. In parallel, identify and mathematically analyze whether the proposed nonlinear gauge construction persists under either finite crop and what it implies for a physical continuum measure. The square/cubic periodic comparators remain **negative controls**, never imposed dimensional foundations.

## 9. Reproducibility, integrity, and provenance

- `verify_source_cut_project_bridge.py` is a new, **non-pentagrid** window/BFS/cube-face generator with an independent source-script comparison mode. It accepts `--source-script` and the `--Ngrid` list. Explicit source and accepted edge SHA hashes appear in `PF_I9_COMPLETE_WINDOW_SOURCE_COMPARISON.json` for all eight sizes.
- `verify_pf_i9_negative_one_trace.py` computes the exact first spectral moment **without eigenvalue diagonalization** and provides both unfiltered and positive-mode-only conventions and a same-graph hopping factorization.
- `test_pf_i9_bridge.py` contains **15 passing tests** (including the author 1,550-site dense matrix trace/edge test, independent source periodic matrix check, source geometry checks and all-eight mode comparisons).
- `verify_collar_stability.py` and `PF_I9_COLLAR_STABILITY.json` validate 4-unit versus 6-unit BFS safety collars at sizes 7, 12 and 25. Completed selected-core and edge fingerprints match exactly.
- The original user-supplied `paper6_extend_local.py` is bundled **only in the private Library research archive**, unchanged and pinned by SHA-256; it is not republished in the repository. Earlier PF-I2–I8 theorem/history and raw evidence are preserved.

**Proposed Observatory scope:** a new finite cut-and-project/operator-identity certificate, exact source scalar `s=-1` reproduction, and correction of PF-I3/PF-I4's source-normalization/mode explanations. This **does not close PF-G0 in its entirety**, because full source spectral/physical field dynamics remain open, nor any P0–P5/PF-G0–G5 or T0–T5 continuum gates.
