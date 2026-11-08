# PF-I13 — Source-intrinsic global gluing: Petersen obstruction, phason-hull inversion and conditional positive doubling

**Research checkpoint:** November 8, 2026. **Source base:** PF-I9 direct cut-and-project four-window/face triangles; PF-I11 SU(2) genuine-rhombus Wilson two-complex and original finite hashes; PF-I12 eight-size transverse face-pair support, exact nonfactorization and two-face positive/negative kernels. The original author's paper scripts and manuscripts are **unpublished references**, not a completed continuum proof.

**Outcome:** exact finite combinatorial, representation-theoretic, source-operator and conditional global-kernel results. **PF-I13 did not produce** a source-derived physical time, a globally OS-positive **original** aperiodic gauge path measure, a nontrivial four-dimensional continuum SU(2) Yang–Mills theory, a uniform physical mass gap, or gravitational UV finiteness. All those gates remain **OPEN**. A periodic/cubic mesh is never substituted for physical spacetime.

## 1. Actual transverse-pair network, not a presumed division into two face species

The source contains rhombi labeled by **unordered pairs** of five basis directions. Write \(D=\{0,1,2,3,4\}\), and let \(\mathcal F_2=\{\{j,k\}:j\ne k\}\) be the ten family types. As proven in PF-I12, two actual faces sharing a vertex form a transverse pair precisely when their family pairs are disjoint. **This is a support criterion, not the assertion that one face lives wholly in \(E_\parallel\) and the other in \(E_\perp\).** In fact, each source direction has nonzero projections in both nontrivial irreducible planes.

### Exact theorem PF-I13.A — the transverse family graph is the Petersen graph and has chromatic number three

Make a graph \(G_{\rm type}\) whose ten vertices are \(\mathcal F_2\), and join two types when they are disjoint. This is the Kneser graph \(KG(5,2)\), also called the **Petersen graph**. Each pair leaves exactly three unused directions, so has exactly three disjoint pair-neighbors; hence there are \(10\times3/2=15\) edges. A triangle would require three pairwise disjoint pairs, hence six distinct indices, impossible in a five-element set. Nevertheless

\[
\{0,4\}\longrightarrow\{2,3\}\longrightarrow\{0,1\}\longrightarrow
\{3,4\}\longrightarrow\{1,2\}\longrightarrow\{0,4\}
\]

is a five-cycle, so the graph is not bipartite. Three colors suffice: assign color 0 to every pair containing 0, otherwise color 1 to every pair containing 1, and color 2 to the three pairs contained in \(\{2,3,4\}\). Same-color types necessarily intersect and are never joined. Thus \(\boxed{\chi(G_{\rm type})=3}\). **QED.**

This is independently tested on the **actual source face-pair graph**, not merely its family quotient, for each original eight-size source complex. Each has a literal five-face cycle with consecutive rhombi sharing an actual vertex and having disjoint direction pairs. The same **non-bipartite/three-color** property is verified on all eight **separate completed-window incident-star cores**, with their PF-I11 reference vertex/face SHA-256 fingerprints checked. The original source populations are not replaced.

| Source `Ngrid` | Original rhombi | Original transverse pairs | Completed-core transverse pairs | Original five-face odd cycle verified? | Completed non-bipartite? |
|---:|---:|---:|---:|---|---|
| 7 | 1,468 | 3,093 | 2,785 | Yes | Yes |
| 10 | 2,886 | 6,157 | 6,057 | Yes | Yes |
| 12 | 4,145 | 8,890 | 8,770 | Yes | Yes |
| 15 | 6,800 | 14,559 | 14,153 | Yes | Yes |
| 18 | 9,646 | 20,749 | 20,669 | Yes | Yes |
| 20 | 11,879 | 25,590 | 25,585 | Yes | Yes |
| 23 | 16,138 | 34,897 | 34,307 | Yes | Yes |
| 25 | 18,874 | 40,853 | 40,973 | Yes | Yes |

**Precise obstruction:** No coloring \(F\to\{+,-\}\) of *every actual face* can make **all** geometrically transverse pair interactions cross between the two colors. The same impossibility holds for a coloring based only on the ten family types. This rules out one proposed universal alternating-two-class gluing, **not** a general involution, a physical time, or reflection positivity with some transverse interactions occurring inside each side. The graph's chromatic number three is a **combinatorial color invariant**, not a statement of three physical sectors or dimensions.

## 2. Exact PF-I13.B — a genuine source cut-and-project involution acts on **phason pairs**, not one generic fixed tiling

For \(m\in\mathbb Z^5\), the source accepted vertex condition is

\[
h=\sum_j m_j\in\{1,2,3,4\},\qquad P_\perp(m+\gamma)\in\operatorname{int}W_h,
\]

where \(\sum\gamma_j=0\), \(W_h\) is the perpendicular projection of \(\{u\in[0,1]^5:\sum u_j=h\}\), and physical/perpendicular projections annihilate \(\mathbf1=(1,1,1,1,1)\).

**Theorem.** The involution \(\Theta(m,\gamma)=(\mathbf1-m,-\gamma)\) carries all accepted generic vertices and all genuine accepted cube-square rhombi of the \(\gamma\) tiling to accepted vertices/rhombi of the \(-\gamma\) tiling, with height \(h\mapsto5-h\), source lower-square height \(h_{\rm face}\mapsto3-h_{\rm face}\), and both nontrivial projections inverted. **Proof:** If \(u\in[0,1]^5\) has height \(h\), then \(\mathbf1-u\) has height \(5-h\) and \(P_\perp(\mathbf1-u)=-P_\perp(u)\). Hence \(W_{5-h}=-W_h\). Similarly the two-fixed-coordinate triangular face window at lower height \(h\in\{1,2\}\) complements to that at height \(3-h\). The transformed point \(m'=\mathbf1-m\) satisfies \(m'+\gamma'=\mathbf1-(m+\gamma)\) for \(\gamma'=-\gamma\), and the source physical projection is inverted. Applying \(\Theta\) twice is the identity. **QED.**

**Crucial qualification:** This is a hull-pairing symmetry, **not in general a symmetry of a fixed generic source phason**. With \(\gamma\) held fixed, the reflected internal projection is shifted by \(2P_\perp\gamma\). The source has a nonzero shift \((0.14647529218568678,-0.12097995020929)\). In the original size-7 source, only 1,422 of 1,550 inverted labels still satisfy the *same* \(\gamma\) window; in size 25, 17,308 of 19,260 do. **All** reflected source labels and rhombi satisfy the \(-\gamma\) windows at every tested size. These finite window checks do **not** assert that the original 35%-tile-center crop is mapped back to the identical original finite population.

The transformation acts as \(-I_4\) on \(E_\parallel\oplus E_\perp\), with **determinant +1 and no fixed real hyperplane** in that four-dimensional representation. It is *central inversion*, not itself a demonstrated codimension-one physical time reflection.

### Exact PF-I13.C — a commuting C5 one-axis involution is unavailable without additional structure

The two nontrivial real \(C_5\) planes are inequivalent, each with real commutant \(\mathbb C\). Hence every real-linear map commuting with \(C_5\) has block form \(a+bJ_\parallel\oplus c+dJ_\perp\). If it is an involution \(R^2=I\), each complex block scalar must satisfy \(z^2=1\), so \(z=\pm1\). There are precisely four such commuting involutions:

\[
\boxed{R=(\pm I_2)\oplus(\pm I_2).}
\]

Their \(-1\) eigenspaces have dimensions \(0,2,2,4\), **never one**. Thus a fully \(C_5\)-commuting **linear hyperplane-style single-axis** time reflection on the 4D nontrivial sector is unavailable from symmetry alone. A dihedral involution not commuting with rotations, chosen orientation/axis, phason-hull action, nonlinear or emergent dynamics, or symmetry breaking could still supply another notion. This theorem **does not assume that physical spacetime must be 3+1 or cubic**; it explicitly tests, and limits, one optional conventional reflection candidate.

The source height coordinate \(h\) is a valid \(C_5\)-invariant integer label, but accepted \(h\in\{1,2,3,4\}\) is bounded. The translation \(m\mapsto m+\mathbf1\) changes height by five and does **not** preserve the accepted set. Therefore the height label alone cannot be promoted to an *unbounded translation-invariant physical time* without a further dynamical extension. This does not exclude time arising from the two nontrivial planes by another mathematical mechanism.

## 3. New PF-I13.D — geometric inversion does not preserve the **fixed scalar Fibonacci hopping background**

The source PF-I10 scalar edge rule assigns each basis-edge lower integer level \(k\) an A/B Fibonacci hopping determined by the indicator of \(\lfloor(k+1)/\varphi\rfloor-\lfloor k/\varphi\rfloor\), with weights \(1\) and \(\varphi^{-2}\). Under the canonical geometric complement \(m\mapsto\mathbf1-m\), an edge from level \(k\) to \(k+1\) goes to one from level \(-k\) to \(-k+1\). But the Fibonacci word is **not invariant** under \(k\mapsto-k\).

| `Ngrid` | Original source edges | Changed A/B edge types under complement |
|---:|---:|---:|
| 7 | 3,017 | 1,864 |
| 10 | 5,927 | 3,872 |
| 12 | 8,468 | 5,507 |
| 15 | 13,779 | 9,562 |
| 18 | 19,593 | 13,780 |
| 20 | 24,091 | 17,194 |
| 23 | 32,582 | 23,185 |
| 25 | 38,139 | 27,350 |

This is verified from the original source edge labels with the PF-I9 source A/B rule; it is not a fitted spectral parameter. **Therefore an alleged reflection symmetry of the full source-weighted scalar operator would have to specify how the Fibonacci hopping background transforms along with the phason.** One possible *covariant family* transports \(w_\gamma\) by \(\Theta\); that is a condition on reflected background data, not a source-proven physical temporal law. Importantly, PF-I10's scalar hopping coefficients are **not established** to be the physical SU(2) face couplings, so this cannot be silently treated as a no-go theorem for all gauge actions.

## 4. PF-I13.E — a conditional *global* positive gluing theorem, with nonfactorizing within-side interactions

Let \(G=SU(2)\) and consider an **auxiliary doubled system** with \(n\) face-holonomy variables on each half \(A\in G^n\), \(B\in G^n\). Assume, additionally, (i) a physically admissible involution identifies the halves, (ii) basepoint gauge frames are consistently identified or transported across the seam, (iii) a chosen positive \(t_i\) is assigned to each *matched* seam pair, and (iv) the internal action on the two halves is mirrored. None of (i)–(iv) is derived here from the original source.

Let \(S_+(A)\) be any real finite action invariant under the chosen gauge convention, **possibly including the PF-I12 non-Abelian transverse commutator couplings wholly within one half**, and write \(w(A)=\exp(-S_+(A))>0\). Define

\[
 K(A,B)=w(A)\,w(B)\prod_{i=1}^nK_{t_i}(A_iB_i^{-1}),\qquad
 K_t(gh^{-1})=\sum_{j\in\{0,\frac12,1,\dots\}}(2j+1)e^{-tj(j+1)}\chi_j(gh^{-1}).
\]

**Theorem:** \(K(A,B)\) is a positive-semidefinite integral kernel on \(L^2(G^n)\) for **every finite** \(n\) and every finite real \(S_+\). **Proof:** Peter–Weyl gives a positive heat convolution operator \(H_{t_i}\) on each copy of \(L^2(G)\). Their tensor product \(H=\bigotimes_iH_{t_i}\succeq0\). For each \(F\),

\[
\int\overline{F(A)}K(A,B)F(B)\,dA\,dB
=\langle wF,H(wF)\rangle\ge0.
\]

The mirrored nonlinear within-half interactions enter only through the positive multiplier \(w\). **QED.** A deterministic 25-state quaternion Gram control at auxiliary \(t=.85\), intra-half commutator parameter \(\lambda=.4\), has minimum positive eigenvalue **0.1649321203**, agreeing with the exact theorem.

This is a legitimate **finite mathematical construction in an externally doubled configuration space** and demonstrates that positivity and internal non-Abelian coupling are not inherently incompatible. It is **not** a proof of the entire original source-gauge theory's reflection positivity. In particular, the source has supplied neither the required half-space/face matching, the gauge-frame seam transport, a physical heat-time/kinetic normalization, nor a matching finite-volume exhaustion.

## 5. PF-I13.F — exact counterexample: a swapped cross seam of individually positive heat kernels can fail positivity

Two-face **pairwise** kernel positivity (PF-I12) is not sufficient to establish **global** reflection positivity. Consider the doubled two-face seam

\[
 K_{\rm swap}((A_1,A_2),(B_1,B_2))
 =K_t(A_1B_2^{-1})K_t(A_2B_1^{-1}).
\]

Every \(K_t\) factor is positive definite as a function of its single pair. But as an operator on \(L^2(G^2)\), \(K_{\rm swap}=(H_t\otimes H_t)P\), where \(P\) swaps two right coordinates. The tensor heat operator and \(P\) commute, and the antisymmetric test

\[
 F(A_1,A_2)=\chi_{1/2}(A_1)-\chi_{1/2}(A_2)
\]

has norm squared 2 under normalized product Haar. Since \(H_t\chi_{1/2}=e^{-3t/4}\chi_{1/2}\) and \(PF=-F\),

\[
\boxed{\langle F,K_{\rm swap}F\rangle=-2e^{-3t/4}<0\quad\text{for every }t>0.}
\]

**QED.** At auxiliary \(t=.85\), this is **\(-1.0572246085\)**, whereas the matched seam gives **\(+1.0572246085\)** for the same test. A separate deterministic five-quaternion/two-face product sample yields a negative minimum eigenvalue **\(-79.6663\)** for the swapped kernel and positive minimum eigenvalue **\(+0.17132\)** for the matched product. The sampled quadratic value depends on the finite sample normalization; the analytical Haar formula is the theorem.

**Scope restriction:** This tests a *specified* attempted exchange reflection that identifies same-index variables between halves but cross-wires their seam. Another reflection that itself incorporates the swap could change the positive/negative classification. The example does **not** prove all global source gluing impossible. It proves that no global OS claim may be derived from individual \(K_t\) positivity **without matching the actual reflection and complete seam wiring**.

## 6. PF-I13 objective status and next proof contract

| Gate | Status |
|---|---|
| Exact transverse family Petersen support and three-color non-bipartiteness on source/complete cores | **PROVED, finite** |
| Exact phason-pairing vertex/face inversion, and failure of fixed generic phase | **PROVED / source-tested, finite** |
| Lack of commuting single-real-axis reflection from bare \(C_5\) 2+2 representation | **PROVED, conditional on commuting linear involution** |
| Fixed PF-I10 Fibonacci scalar hopping not reflection invariant under complement | **SOURCE-VERIFIED finite obstruction** |
| Abstract matched SU(2) heat-seam with mirrored within-side non-Abelian interaction | **PROVED, conditional finite positive kernel** |
| Mismatched swap seam can have negative reflection form | **PROVED exact counterexample** |
| A source-derived *single-tiling or hull-based physical time*, matched seam and gauge transport | **OPEN** |
| A globally OS-positive or otherwise justified original aperiodic Yang–Mills path measure | **OPEN** |
| A nontrivial interacting 4D continuum limit with a uniform physical mass gap | **OPEN** |

**Next mathematical obligation PF-I14:** Identify an explicit, source-compatible **phason-hull / gauge-background involution and dynamical gluing** with a mathematically defined algebra of positive-side observables, a consistent face/edge/reflection map including orientation and Fibonacci hopping transformation where relevant, and a demonstrably positive *global* bilinear form. Only then ask whether there is an intrinsic family of finite-volume reflection-positive transfer operators with source-derived scales, control of boundaries/phasons and a uniform nontrivial continuum gap. The familiar cubic negative control is not a physical geometry requirement. No mass-gap theorem is claimed here.

## 7. Source provenance and reproducibility

The original unpublished source script used for numerical reconstruction is SHA-256 `86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da`, preserved privately alongside the source-matched PF-I11 snapshot arrays and source manuscripts. The new independent derived checker is `verify_pf_i13_global_gluing.py`; the independently completed-window auditor is `verify_pf_i13_completed_core.py`. The source original and completed populations are verified against PF-I11 vertex and face digests independently. The complete private reproducibility bundle retains all actual source and 8+8 finite results. The public repository retains derived scripts, mathematical statements, aggregate evidence and test code but **does not publish the manuscript or original source script**.

The pure/source-independent unit tests and private-source checks are separated; 20 total tests pass with full source, while six expected private tests skip when source snapshots are absent. All numerical controls are deterministic under pinned seeds and tolerances. The global SU(2) heat kernel construction and negative swap witness are **auxiliary mathematical controls**, not derived physical dynamics.
