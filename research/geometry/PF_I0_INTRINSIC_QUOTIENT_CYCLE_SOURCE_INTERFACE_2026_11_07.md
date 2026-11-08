# PF-I0 research checkpoint: quotient adjacency, odd-cycle identity, and source-operator discrimination

**Date:** 2026-11-07 (America/Denver). **Scope:** conditional mathematical theorem and falsifiable source-authentication test. **NOT:** recovery of the original Paper 2 generator, Penrose P3 proof, a geometric physical time, an interacting quantum vacuum, an interacting spectral inequality, a Yang–Mills mass gap, or gravity UV finiteness. All P0–P5, PF-G0–G5, T0–T5 and gravity gates remain **OPEN**.

## 1. Source identity and exact source conflict

The author's original dissertation v10.7, Ch. 3 §§3.1–3.4 and Paper 2 §§2.1–2.2, 4, 6.2, 7.4 and 8.2 define

\[
\omega=e^{2\pi i/5},\quad z_1(m)=\sum_{j=0}^4m_j\omega^j,\quad z_2(m)=\sum_{j=0}^4m_j\omega^{2j},\quad m\in\mathbb Z^5.
\]

The source juxtaposes removal/fixing of the trivial sum direction with adjacency via single-original-basis steps \(m\leftrightarrow m\pm e_j\). Those descriptions are not literally compatible within one fixed-sum slice: \(\sum_j(m\pm e_j)_j=\sum_jm_j\pm1\). Paper 2 reports \(t_A/t_B=\varphi^2\) and an approximately 0.833 spectral-zeta ratio, but the original window, phason, code, weight rule and literal vertex/edge lists have not been authenticated by the present audit. Reported numerical values **are not regenerated here**. Paper 2 explicitly separates the coupled operator from the product operator, and the later Stage-26 Penrose-versus-square scalar SU(2) data are a different experiment.

**Source digests (files inside original dissertation tar, for provenance rather than theorem certification):**
- `delivery/papers/Paper_2/Sharpe_Paper2_Z5_Minkowski_Lapidus.pdf`: SHA-256 `2bfc52c29140149d483b8e1b980143b05a43d21fe0e2098516efb1615b7e50e7`.
- `delivery/dissertation/the_singular_boundary.pdf`: SHA-256 `138cee2b22cbd68e23767c5db9b9fcc27c040ca13bc1b5deb96c9ba99ae0868a`.

Previous relevant repository records: `research/geometry/PF_PRIMARY_GEOMETRY_RESTORATION_2026_11_06.md`, `research/geometry/PF_G0_QUOTIENT_DOUBLE_SPIRAL_SOURCE_AUDIT_2026_11_07.md`, and `docs/research/P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md`.

## 2. Theorem — three distinct realizations of the Z5 nearest-basis prescription

Let \(d=(1,1,1,1,1)\) and \(e_j\) be the five standard basis vectors. Consider:

1. **Fixed-sum slice** \(S_c=\{m\in\mathbb Z^5:\sum_jm_j=c\}\). The induced graph with edges \(m\leftrightarrow m\pm e_j\) is edgeless. This does **not** preclude other slice-preserving edge types such as \(e_i-e_j\), but those would constitute a different graph operator.
2. **Full Z5 nearest-basis graph**, with no diagonal identification. It is bipartite, with parity \(\sum_jm_j\pmod2\). The map \((z_1,z_2)\) is not injective: \(m\) and \(m+td\) have the same coordinates for every \(t\in\mathbb Z\). The five consecutive positive steps change the full vertex from \(m\) to \(m+d\), so the projected path closes but its full-lattice lift does not.
3. **Diagonal quotient** \(\Lambda=\mathbb Z^5/\mathbb Zd\). Both Fourier coordinates descend, and the five generator classes \(v_j=[e_j]\) satisfy \(v_0+\cdots+v_4=0\). In the coordinates with the fifth integer representative fixed at zero, they are
   \[
   v_0=(1,0,0,0),\ v_1=(0,1,0,0),\ v_2=(0,0,1,0),\ v_3=(0,0,0,1),\ v_4=(-1,-1,-1,-1).
   \]
   The full Cayley graph on generators \(\{\pm v_j\}\) is **non-bipartite**. Its shortest odd cycles have length five.

**Proof.** \(\sum_j\omega^j=\sum_j\omega^{2j}=0\), so both maps kill \(d\). Conversely, if \(\sum_j a_j\omega^j=0\) with integral \(a_j\), the polynomial \(\sum_{j=0}^4a_jx^j\), of degree at most four, is a rational multiple of \(\Phi_5(x)=1+x+\cdots+x^4\), the minimal polynomial of \(\omega\). All integer coefficients are therefore equal. Hence the full integer kernel is exactly \(\mathbb Zd\); the quotient Fourier embedding is injective as an abstract \(\mathbb Z\)-module. Fixed-sum and full-graph statements follow immediately.

A signed path of length \(\ell\) in the quotient has a net signed direction-count vector \(c=(c_0,\ldots,c_4)\in\mathbb Z^5\). Closure means \(c=td\), so every \(c_j=t\). If \(t\neq0\), then \(\ell\ge\sum_j|c_j|=5|t|\). If \(t=0\), each direction occurs equally often forward and backward, so \(\ell\) is even. Thus a closed odd path has length at least five. For \(\ell=5\), necessarily \(t=\pm1\) and each direction appears exactly once with the same sign, in any order. Every proper nonempty subset of the five distinct generators has nonzero quotient sum, so these five-step closed paths are simple cycles. QED.

**Special caution.** The complete 5D graph and the quotient have different graph topology despite sharing projected points. Identifying diagonal copies **changes adjacency and the cycle space**. No continuum argument may treat the quotient as an innocuous point-label normalization without establishing that it is the source operator.

## 3. Corollary — ordinary rhombus edge graphs are not automatically the quotient graph

A genuine planar edge-to-edge rhombus tiling of the plane has a bipartite vertex-edge graph: every bounded face has four sides, and every finite simple graph cycle encloses finitely many rhombi; counting interior edges twice shows that the cycle boundary length is even. Equivalently, the planar quadrangulation has a consistent 2-colouring.

Consequently, **any accepted finite quotient graph exhibiting one five-cycle cannot be identical (as a graph) to an induced subgraph of the ordinary P3 rhombus edge graph**. The quotient may be an *augmented coupled graph*, including extra edges not present in the rhombus-edge skeleton, or the historical source may use another lift/selection/identification. The present theorem does not choose between these interpretations.

This matters for the claimed coupled-vs-product spectral difference: a change of cycle space, degree distribution or edge-weight rule can change a scalar Laplacian and its spectral zeta. Matching labels and projections alone is not an operator correspondence. Nor does a five-cycle prove a Yang–Mills mass gap: it is a structural discriminator, and generic other graph classes can also possess odd cycles.

## 4. C5 symmetry and the hopping-weight constraint

The cyclic permutation \(\sigma(m_0,m_1,m_2,m_3,m_4)=(m_4,m_0,m_1,m_2,m_3)\) descends to an automorphism of \(\Lambda\) and acts by

\[
z_1(\sigma m)=\omega z_1(m),\qquad z_2(\sigma m)=\omega^2z_2(m),\qquad \sigma v_j=v_{j+1\pmod5}.
\]

For a \(C_5\)-stable accepted patch, a weighted graph Laplacian with symmetric positive edge weights \(w_j(m)\) is \(C_5\)-equivariant **if and only if** the weights transform covariantly on actual edges:
\[
 w_{j+1}(\sigma m)=w_j(m).
\]
If weights are **constant by direction** alone, \(w_j(m)=c_j\), and every direction occurs in the patch, this forces \(c_0=\cdots=c_4\). A nonconstant Fibonacci short/long assignment can still be \(C_5\)-equivariant if its *position-dependent edge classification* rotates with the graph. The source's reported ratio \(t_A/t_B=\varphi^2\) does **not** by itself specify which rule was implemented. We must not infer broken symmetry merely from the ratio.

For a finite accepted graph with undirected edge weights \(w_e>0\), the standard weighted Laplacian \(L_w f(x)=\sum_{y\sim x}w_{xy}(f(x)-f(y))\) has exactly
\[
 \langle f,L_w f\rangle=\sum_{\{x,y\}\in E}w_{xy}|f(x)-f(y)|^2\ge0.
\]
This is a finite graph identity only, not a claim of a physical kinetic normalization or spectral gap uniform under refinement.

## 5. Finite conditional SU(2) Wilson observable

On any accepted graph containing an oriented five-cycle \(\gamma\), assign \(U_e\in SU(2)\) to oriented links and \(U_{\bar e}=U_e^{-1}\). The holonomy \(U_\gamma=\prod_{e\in\gamma}U_e\) transforms as \(U_\gamma\mapsto g_{x_0}U_\gamma g_{x_0}^{-1}\) under \(U_{xy}\mapsto g_xU_{xy}g_y^{-1}\). Hence \(W_\gamma=\frac12\operatorname{tr}U_\gamma\) is gauge invariant. This finite identity does **not** specify which cycles bound physical 2-cells, which magnetic action to select, any physical normalization, or any temporal transfer. Those remain open source-specific choices.

## 6. Independent numerical witness (illustrative candidate, not original run)

The standard-library verifier `research/scripts/verify_pf_i0_quotient_cycles.py` uses a square integer search \([-6,6]^4\) for quotient representatives, an illustrative **regular decagon** in \(z_2\) of circumradius **1.65**, vertex orientation **0**, and a bounded physical disk \(|z_1|\le5\). It computes and checks:

| Test | Result |
|---|---:|
| Accepted vertices | 241 |
| Undirected edges | 650 |
| Mean graph degree | 5.394190871369295 |
| Distinct simple five-cycles | 1,260 |
| Exact 5-step closed signed direction words | \(2\cdot5!=240\) |
| Graph bipartite? | No |
| C5 graph-automorphism and Fourier-equivariance tests | Passed |
| Noncommuting quaternion SU(2) five-loop gauge-transform trace error | \(1.11\times10^{-16}\) |
| Deterministic assertions recorded by verifier | 3,961 |

As a sensitivity check, changing the **illustrative** window radius at the same 4D representative span and physical radius 5 gives different accepted graphs (radius 1.45: 171 vertices, 430 edges, 730 five-cycles; radius 1.90: 311 vertices, 910 edges, 1,950 five-cycles). Counts do not reproduce Paper 2's reported \(N_{\rm grid}=25\), \(N_{\rm int}=19{,}260\) and bulk degree ~3.9, and no identification is claimed. All finite counts depend on the arbitrary window, physical cutoff, representation convention and strictness of the acceptance test. These deterministic checks supplement, but do not substitute for, the algebraic proofs above.

Reproduce from the repository root:

```bash
python research/scripts/verify_pf_i0_quotient_cycles.py --output /tmp/pf_i0_cycles.json
```

Evidence and script hashes are recorded in `research/evidence/PF_I0_QUOTIENT_ODD_CYCLE_EVIDENCE_2026_11_07.json` and this audit's artifact manifest. The original dissertation PDF hashes are provided above. No simulation dataset is required and no data exceed GitHub's ordinary file limits; no binary archive is introduced.

## 7. Specific resolution gate and next proof decision

To close **PF-G0**, recover the *authentic* Paper 2 graph generator or sufficient original source specification to reconstruct (a) the integer sum mode and handling of diagonal copies, (b) vertex acceptance/window, phason and boundary conventions, (c) the 5-family Fibonacci long/short assignment, (d) actual face/edge lists and cycle parity, (e) normalization of the reported coupled and product Laplacians. Compare exact finite source graph counts and operators—not just plots—against the separate Stage-7/26 Penrose-vs-square *2+1D SU(2)* code.

**Decisive falsification:** if the original coupled operator has accepted odd five-cycles, it is not the bare P3 rhombus-edge Laplacian. If its reported graph has no odd cycles, a literal full diagonal-quotient all-basis-neighbour identification requires additional restrictions. If neither can be source-validated, PF-G0 remains OPEN and the model cannot be chosen by convenience.

Only after source identity may we derive a faithful gauge action, identify an interacting quantum vacuum and seek a genuinely geometric, refinement-uniform spectral inequality. The cubic SU(2) mathematical programme remains a separate negative/reference control. All claims of physical dimension, time, gravity finiteness and Yang–Mills continuum mass gap remain OPEN.
