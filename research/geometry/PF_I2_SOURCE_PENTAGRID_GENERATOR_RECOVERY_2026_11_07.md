# PF-I2 — Source-defined pentagrid P3 generator, four-layer theorem, and spectral-operator normalization gate

**Date:** 2026-11-07 (America/Denver)  
**Research model:** Paper 1 §§6.1–7.2 P3 rhombus vertex graph, with cross-reference to Paper 2 §§7.4, 8.2.  
**Status:** Exact finite/infinite combinatorial implications of the *published definitions*; executable independently reconstructed finite samples. This is **NOT** recovery of the unpublished Paper 1/2 numerical source code, and it does **NOT** authenticate whether Paper 2's *coupled* Z5 graph is the same accepted P3 edge graph or an altered graph, nor its reported 0.8332 ratio. The Yang–Mills and gravity gates remain **OPEN**.

## 1. Recovered exact published algorithm

**Primary source:** `Sharpe_dissertation_v10.7.tar.gz` → `delivery/papers/Paper_1/Sharpe_Paper1_Spectral_Dimension_Flow.pdf`, PDF SHA-256 `7c0585fa990bb2a762c869665287835bbdb6e07edeb55e9adfe54fe84f9eddea`, §§6.1–7.1 Eqs. (12)–(14). The related Paper 2 PDF SHA-256 is `2bfc52c29140149d483b8e1b980143b05a43d21fe0e2098516efb1615b7e50e7`, especially §§2.1–2.2, 7.4, 8.2.

Let \(e_j=(\cos(2\pi j/5),\sin(2\pi j/5))\), \(j=0,\ldots,4\). Paper 1 supplies offsets

\[
\widetilde\gamma_j=\{j\sqrt2+j^2\sqrt3\},\qquad
\gamma_j=\widetilde\gamma_j-\tfrac15\sum_{h=0}^4\widetilde\gamma_h,
\qquad\sum_j\gamma_j=0.
\]

Its j-th grid line at level k is \(r\cdot e_j=k+\gamma_j\). At a generic point of a pentagrid cell, define the integer label and projected tiling vertex by

\[
K_j(r)=\lceil r\cdot e_j-\gamma_j\rceil,
\qquad V(r)=\sum_{j=0}^4K_j(r)e_j.
\]

Two cell labels connected across one grid line differ by \(\pm\mathbf e_j\) in original Z5 indices. Every generic pairwise grid-line crossing of families j,k supplies the four corners
\(K,K+\mathbf e_j,K+\mathbf e_j+\mathbf e_k,K+\mathbf e_k\), forming a rhombus. The two interior edge types have angular separation j-k giving fat/thin rhombi.

**Recovered Fibonacci hopping:** Paper 1 Eq. (14) specifies, for an edge crossing family j at integer level k,

\[
t(j,k)=\begin{cases}
 t_A,&\lfloor(k+1)/\varphi\rfloor\ne\lfloor k/\varphi\rfloor,\\
 t_B,&\text{otherwise},
\end{cases}\qquad t_A=1,\quad t_B=\varphi^{-2},\qquad \varphi=(1+\sqrt5)/2.
\]

It is **not** a constant type assigned solely to each of the five directions: the level k matters. In Paper 2 §8.2 the *coupled* operator is said to use Fibonacci weights by grid family, but the phrase **“cross-direction bonds”** is not given as an explicit additional-edge list: it may simply mean that the five families are connected on the same P3 graph, rather than forming a tensor-product chain. The published text does not identify a distinct edge set or guarantee that additional edges exist. The reconstruction below is therefore **Paper 1 P3**, not an identified Paper 2 coupled spectrum.

## 2. Exact theorem PF-I2.A: the genuine source construction has four sum layers

Assume \(\sum_j\gamma_j=0\), \(\sum_je_j=0\), and a generic cell point r lying on no pentagrid line. Write \(a_j=r\cdot e_j-\gamma_j\); then \(\sum_j a_j=0\). Since all \(a_j\notin\mathbb Z\),

\[
\sum_jK_j=\sum_j(\lceil a_j\rceil-a_j),\qquad 0<\lceil a_j\rceil-a_j<1.
\]

The sum is an integer strictly between 0 and 5, hence

\[
\boxed{\sum_jK_j\in\{1,2,3,4\}.}
\]

At a generic two-line crossing of families j and k, set the lower corner's two coordinates to the integers n,m, and the other three to their ceiling values. The same argument sums **three** strictly positive fractional remainders; the lower corner's integer sum lies in \(\{1,2\}\). The four rhombus corners then occupy layers S, S+1, S+2, S+1, all within \(\{1,2,3,4\}\). This proves four layers for the entire generic rhombus complex and not merely sampled cell centers. **QED.**

### Corollary PF-I2.B: no projected duplicates and no odd cycles

For integer labels K,L, \(z_1(K)=z_1(L)\) implies \(K-L=q(1,1,1,1,1)\), q integer, by the cyclotomic minimal polynomial \(\Phi_5\). Thus the coordinate sums differ by 5q. Since all genuine P3 labels have sums in \(\{1,2,3,4\}\), q=0: their physical projection is injective on labels.

Every P3 edge changes exactly one K coordinate by \(\pm1\), so S(K) changes by \(\pm1\). Color the graph by S(K) modulo 2. Every edge switches colors: the graph is bipartite and has **no odd cycle**.

This result **resolves the PF-I0 ambiguity for the Paper 1 P3 graph**. The strict fixed-sum slice admits no elementary edges; the diagonal *quotient* allows artificial five-edge cycles; the actual published pentagrid selection instead retains four distinct integer-sum layers and preserves the elementary edges without quotient-generated odd cycles. The Paper 2 coupled graph may use the same P3 edges (coupled relative to a product chain) **or** a different accepted graph; the proof does not settle that ambiguity. **QED.**

## 3. Exact conditional source-graph equivalence PF-I2.C

Paper 1 defines its P3 edge set, on the accepted integer labels \(V_{P3}\), precisely as
\[
E_{P3}=\{\{m,n\}\subset V_{P3}:m-n=\pm\mathbf e_j\text{ for some }j\}.
\]
If the words **“all Z5 nearest neighbours”** in Paper 2 §8.2 use **this same accepted vertex set** and this same original-basis difference criterion, then its edge set \(E_{\mathrm{coupled}}\) necessarily equals \(E_{P3}\). There are **no additional nearest-basis bonds** to add, and “coupled” can legitimately mean interlocking worm families rather than a tensor-product decomposition. The proof is equality by the two source adjacency definitions.

The independently reconstructed finite P3 patches verify the literal statement directly: among their selected labels, *every* accepted \(\pm\mathbf e_j\) neighbour is already an edge of an enumerated rhombus—345/345 on the small patch and 1,185/1,185 on the larger patch. The separate question is whether Paper 2's source numerical generator actually used the same accepted vertex set, cutoff/selection, and weights. If its coupling introduces genuinely new bonds, the corresponding original labels or incidence rules must be identified. **The existence of additional Paper 2 bonds must NOT be presumed. QED (conditional on common source vertex/edge definitions).**

## 4. Exact theorem PF-I2.D: scalar diagonal normalization is not source-certified

Paper 1 §§3.2, 7 describes a `graph Laplacian L = D - W`, calling D the *degree matrix* and W the weighted adjacency matrix, but does not state unambiguously whether D is the **weighted strength** \(D^{(w)}_{vv}=\sum_u W_{vu}\) or the **unweighted count** \(D^{(c)}_{vv}=\#\{u:W_{vu}>0\}\).

For the same positive hopping weights, two mathematically distinct operators result:

\[
L_w=D^{(w)}-W,\qquad L_c=D^{(c)}-W
   =L_w+\operatorname{diag}(D^{(c)}-D^{(w)}).
\]

For the published \(0<t_B< t_A=1\), \(L_w\mathbf1=0\) and \(f^*L_wf=\sum_{\{u,v\}}w_{uv}|f_u-f_v|^2\), while on a connected graph containing at least one B-edge, \(L_c\) is **strictly positive** and has no zero constant mode. Both have nonnegative eigenvalues, but their spectral zetas and heat traces differ materially. This is a concrete binary source-operator normalization gate, not a proof of the intended spectrum and not a Yang–Mills gap. **QED.**

## 5. Independently reconstructed finite examples

Executable `research/scripts/verify_pf_i2_pentagrid.py` enumerates grid intersections for the published offsets, emits the four integer-labeled corners and source hopping on every rhombus edge, performs combinatorial/planar checks, verifies two scalar diagonal conventions, and independently verifies the gauge invariance of SU(2) Wilson traces on the resulting source-defined four-link rhombi. Uses NumPy, SciPy, and optionally Shapely for no-crossing geometry checks. Random gauge matrices use a reproducible local seed.

**Main illustrative cutoff**: retain rhombi with projected **centroid** radius ≤6.5; grid levels in [-11,11]. This *cutoff is our explicit choice*, not the unknown Paper 1 numerical Ngrid procedure.

| Diagnostic | Independently reconstructed result |
|---|---:|
| Vertices / edges / rhombi | 186 / 345 / 160 |
| Euler V-E+F (bounded faces) | 1 |
| Sum-layer vertex counts S=1,2,3,4 | 25, 69, 64, 28 |
| Mean graph degree | 3.709677 |
| A / B hopping-edge counts | 205 / 140 |
| Pentagonal / other odd cycles | 0 (proved by parity) |
| Detected geometric edge crossings | 0 |
| SU(2) Wilson gauge checks | 150; max trace discrepancy 4.62×10⁻¹⁶ |
| Weighted-degree Laplacian smallest eigenvalue | ~0 (exact zero mode) |
| Weighted-degree first positive scalar eigenvalue | 0.0383424 |
| Count-degree-minus-weighted-adjacency minimum | 0.499315 |
| Weighted \(N^{-1}\sum\sqrt{\lambda+1}\) | 1.8835994 |
| Count-degree \(N^{-1}\sum\sqrt{\lambda+1}\) | 2.1255342 |
| Program assertions | 3,382 passed |

**Larger independent cutoff:** projected rhombus-centroid radius 12, grid levels [-12,12]. 616 vertices, 1,185 edges, 570 rhombi; Euler 1, exactly four sum layers, zero odd cycles and 150 independent gauge checks, with **11,305 passing assertions**. The degree 3.8474 is consistent with approaching degree 4 as boundary-to-area declines; it is not a reproduction of Paper 2's ~3.9 on Ngrid=25. The A/B ratios fluctuate with finite selection and level range and are not asserted to reproduce Paper 1's reported 1.614.

The source-reported 0.8332 spectral-zeta ratio and the 20-configuration statistics are **not** reproduced here. These two small scalar calculations demonstrate sensitivity to operator normalization; comparisons across differing source/control patches, boundaries, or volume scales would be scientifically invalid.

## 6. Remaining interface to the actual coupled-Z5 spectral computation

**Resolved at the published-definition level for Paper 1:** pentagrid offsets and genericity convention, integer vertex labels, original Z5 edge rule, rhombus faces, four sum layers, source Fibonacci level-dependent hopping, and the distinction from the quotient toy in PF-I0.

**Still OPEN for Paper 2:** whether the *coupled* Z5 operator uses exactly the Paper 1 rhombus-edge graph or a distinct accepted graph; what its “cross-direction bonds” mean (existing inter-family edges versus actual additional original-integer bonds); how site/edge cuts and Ngrid/Nint=19260 are implemented; which degree diagonal, mass parameter, spectral-zeta normalization, and comparison graph were used; phason/window sampling and the 20 configurations. No bit-for-bit identity with the original numerical results can be claimed without its original implementation, parameter record or equivalent fully specified operator. Its separate incorrect internal \(T^2\) quotient was recorded by PF-I1.

**Next falsifiable step:** use the reconstructed Paper 1 P3 edge dictionary as the null hypothesis for Paper 2. Identify source evidence for any distinct accepted vertices or genuinely additional bonds before introducing them; otherwise the coupled operator may have *identical graph adjacency* to Paper 1 and differ in interpretation or operator weighting rather than edge set. Compute weighted and count-degree spectra and heat kernels on **the same** P3 finite patch and one clearly defined periodic reference under identical mass, boundary, and normalization. Only then attempt recovery of Paper 2 0.8332, with an explicit uncertainty range for any unverified source inputs. A control experiment is not a proof of Yang–Mills infrared exclusion.

**Research governance:** Preserve original source PDFs as user-provided primary data; never rewrite them. Keep these independent proof and verification records on canonical `main`, with full evidence ZIP and hashes in Library. The Observatory PF-G0 source generator remains **OPEN**; this is a partial source-defined P3 sub-result, not its coupled-model completion. P0–P5, PF-G0–G5, T0–T5, and gravity goals are not promoted. No new branch or public Pages release is authorized by this audit.
