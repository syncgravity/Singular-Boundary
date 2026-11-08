# PF-I1 — Dense perpendicular projection, correction of the configuration torus, and the authentic source-operator gate

**Research date:** 2026-11-07 (America/Denver)  
**Source:** Sharpe, *The Gravitational Path Integral on the Penrose Lattice: From Z5 to Minkowski Spacetime via Lapidus Complex Dimensions*, original dissertation bundle v10.7, Paper 2, §2.1–2.2, §3 (especially displayed Eq. (9)), §§4–8; Paper 3, §2 for the linear complex structure.  
**Status:** Exact elementary algebra/topology theorem with an executable arithmetic witness; original numerical graph generator **not authenticated**; no continuum or Yang–Mills/gap/UV theorem certified.  
**Scope:** Correct the meaning of the two-component projection and preserve the source's coupled `z1,z2` construction. Do **not** introduce an externally chosen physical spatial dimension or a replacement graph. Historical PF-I0 is retained.

## 1. Exact source claim under audit

Paper 2 defines

\[
\zeta=e^{2\pi i/5},\quad z_1(m)=\sum_{j=0}^4 m_j\zeta^j,\quad z_2(m)=\sum_{j=0}^4 m_j\zeta^{2j},\quad m\in\mathbb Z^5.
\]

In §3, Eq. (9), it writes the *configuration space* as the quotient

\[
\mathcal C=\mathbb R^2_\perp/\pi_\perp(\mathbb Z^5)\cong T^2,
\]

and describes that quotient as a compact flat two-torus because the projected lattice is taken to be periodic. **As written for the full displayed projection, that topological identification is false.** The correct object is a dense additive subgroup of the perpendicular plane, not a discrete rank-two lattice. This does not automatically invalidate the paper's finite computed eigenvalues; it does invalidate deductions that specifically require the displayed internal quotient to be a Hausdorff flat two-torus.

### Theorem PF-I1.A — Perpendicular Fourier image is dense

Let \(H=\{z_2(m):m\in\mathbb Z^5\}\subset\mathbb C\). Then

1. \(H=\mathbb Z[\zeta]\) as an additive subgroup and \(H\) is countable and **dense** in \(\mathbb C\).
2. Its quotient \(\mathbb C/H\), given the quotient topology, is **indiscrete** (the only open sets are \(\varnothing\) and the entire quotient). It is not a Hausdorff two-torus.
3. The same density issue survives imposing a literal fixed-coordinate-sum slice \(\sum_j m_j=C\) for any integer \(C\). It is not removed by that convention.

**Proof.** Because multiplication by \(2\pmod5\) permutes the exponents, the image is the cyclotomic integer module \(\mathbb Z[\zeta]\). Set \(\varphi=(1+\sqrt5)/2\). Cyclotomic identities give

\[
\zeta^2+\zeta^3=-\varphi,\qquad
\zeta+\zeta^4=\varphi-1.
\]

Hence \(1,\varphi,\zeta^2,\varphi\zeta^2\in H\). Since \(\varphi\) is irrational, \(\mathbb Z+\varphi\mathbb Z\) is dense in the real line. Consequently

\[
(\mathbb Z+\varphi\mathbb Z)+\zeta^2(\mathbb Z+\varphi\mathbb Z)\ \subset\ H
\]

is dense in \(\mathbb C\): its two real directions are linearly independent because \(\operatorname{Im}\zeta^2\ne0\). For any dense subgroup \(H\) of a topological group \(G\), every nonempty open \(H\)-invariant subset of \(G\) is all of \(G\) (the closed complement, if nonempty, would contain a dense orbit and thus equal \(G\)). Therefore the quotient topology on \(G/H\) is indiscrete. The quotient has more than one coset because \(H\) is countable, so it cannot be Hausdorff.

For the sum-zero integer sublattice \(A_4=\{n\in\mathbb Z^5:\sum n_j=0\}\), let \(d=(1,1,1,1,1)\) and \(S(m)=\sum_j m_j\). Then

\[
5m-S(m)d\in A_4,\qquad z_2(5m-S(m)d)=5z_2(m),
\]

since \(z_2(d)=0\). Thus \(5H\subset z_2(A_4)\), and \(5H\) is dense. Any nonempty fixed-sum slice is an affine translate of \(A_4\) and also has dense internal image. **QED.**

### Exact constructive witnesses

Let \(F_n\) be the Fibonacci numbers \((F_0,F_1)=(0,1)\), and put

\[
m^{(n)}=(F_{n+1},F_n,0,0,F_n)\in\mathbb Z^5.
\]

Then

\[
\boxed{z_2(m^{(n)})=F_{n+1}-\varphi F_n=(-1)^n\varphi^{-n}\to0,}
\]

while

\[
z_1(m^{(n)})=F_{n+1}+(\varphi-1)F_n\to+\infty.
\]

The first identity is exact; it is checked symbolically in the accompanying verifier. Thus the internal image has arbitrarily small nonzero translations even when physical displacement diverges. These witnesses illustrate precisely why the internal module is dense and not a period lattice.

### Theorem PF-I1.B — The joint Fourier image *is* a full-rank lattice in four real dimensions

Define

\[
\Lambda_F=\left\{\big(z_1(m),z_2(m)\big):m\in\mathbb Z^5\right\}\subset\mathbb C^2\cong\mathbb R^4.
\]

The integer kernel is exactly \(\mathbb Z d\). Indeed, if \(z_1(m)=0\), the integer polynomial \(P_m(t)=\sum_{j=0}^4m_jt^j\) vanishes at the primitive fifth root \(\zeta\), so it must be a multiple of \(\Phi_5(t)=1+t+t^2+t^3+t^4\). Therefore all five coefficients coincide. Conversely diagonal vectors vanish in both projections.

Represent each class by the unique integer vector with \(m_4=0\), and let \(\ell_j=(\zeta^j,\zeta^{2j})\) for \(j=0,1,2,3\). With the ordinary Euclidean product on \(\mathbb C^2\cong\mathbb R^4\), their exact Gram matrix is

\[
G_{jk}=\begin{cases}2&j=k,\\-1/2&j\ne k.\end{cases}
\qquad G=\frac52I_4-\frac12\mathbf1\mathbf1^T,
\]

and

\[
\det G=\frac{125}{16}>0,\qquad
\operatorname{covol}(\Lambda_F)=\sqrt{\det G}=\frac{5\sqrt5}{4}.
\]

The four real vectors \(\ell_0,\ldots,\ell_3\) form a basis of \(\mathbb R^4\), so \(\Lambda_F\) is discrete and co-compact. Consequently

\[
\boxed{(\mathbb C_{z_1}\oplus\mathbb C_{z_2})/\Lambda_F\cong\mathbb R^4/\mathbb Z^4\cong T^4}
\]

**as a real topological torus**. This is a legitimate joint-space torus, **not a declaration that the exact Penrose tiling hull, its phason parameter space, or spacetime is this four-torus**. Singular cuts, accepted windows, vertex labels and dynamical meaning require additional construction. **QED.**

### A useful qualification about the Paper 3 complex structure

Paper 3's \(J(z_1,z_2)=(iz_1,iz_2)\) is a valid constant complex structure on the real vector space \(\mathbb C^2\). It also descends as a **tangent tensor** on the translation quotient \(\mathbb C^2/\Lambda_F\), and hence defines an integrable complex structure on that real four-torus. This does **not** require \(J\Lambda_F\subseteq\Lambda_F\): translation derivatives are the identity.

However, the **global point rotation** \((z_1,z_2)\mapsto(i z_1,i z_2)\) does not descend as a torus group endomorphism in general. For example, \(\ell_0=(1,1)\in\Lambda_F\) but \((i,i)\notin\Lambda_F\), since each Fourier component lies in \(\mathbb Q(\zeta)\) whereas \(i\notin\mathbb Q(\zeta)\) (\(\mathbb Q(\zeta,i)=\mathbb Q(\zeta_{20})\) has degree 8, versus degree 4 for \(\mathbb Q(\zeta_5)\)). Therefore any **global periodic Wick-rotation flow** requires its own definition; existence of the linear tensor \(J\) does not supply it. The source's proposed physical time and Lorentzian reconstruction remain OPEN.

## 2. Connection to previous PF-I0 source-operator test

The prior source audit [PF-I0](PF_I0_INTRINSIC_QUOTIENT_CYCLE_SOURCE_INTERFACE_2026_11_07.md) established that strict fixed-sum adjacency and single-basis steps cannot both be literal on an induced graph; that a diagonal quotient supports five-generator odd cycles for some **illustrative** windows; and that such a graph cannot automatically be the ordinary bipartite planar P3 rhombus-edge skeleton. The new PF-I1 theorem does **not** authenticate the quotient graph or a particular window. It resolves a different ambiguity: the topological distinction between internal and joint Fourier projection images.

These two independent checks form a useful operator-provenance test:

- **PF-I0: source graph identity** — identify the actual accepted vertex set, edges, phason/slice conventions, hopping weights and the operator used for each spectral-zeta result;
- **PF-I1: source global topology** — do not assume the dense internal projection produces a compact two-torus; use a justified joint-space parametrization or a properly defined dynamical hull if needed;
- **Next open interface:** recover the original eigenvalue generator, preferably the exact Paper 2 code and intermediate site/edge lists, before attempting to reproduce its ~0.833 spectral-zeta ratio. Do not substitute Stage 26 2+1D SU(2) Monte Carlo measurements, whose code and observable are different.

The original dissertation v10.7 tar archive was re-inspected in this audit: it contains the dissertation PDF, five paper PDFs, and two experiment PDFs, **no standalone source scripts**. Archived Stage 7/26 scripts in `sources/historical/raw/Archive_4/...` are accessible, including the area-matched model-set torus and scalar SU(2) measurement runner; these are not evidence of the **Paper 2 graph-zeta** implementation. The `source_sha256` in Stage26 records hashes an input Stage9 checkpoint, not a graph-zeta program.

## 3. Consequences, limitations, and no-overclaim protocol

1. **Proved, from source definitions:** the internal projection image is dense; the literal two-torus quotient in Paper2 Eq. (9) is incorrect as a topological statement; fixed-sum restriction does not cure that density; the *joint* image is a rank-four lattice whose quotient is a real four-torus.
2. **Not thereby disproved:** finite Penrose/square eigenvalue calculations, possible bounded-window phason scanning protocols, the fivefold representation and linear \(J^2=-I\), or the possibility of a mathematically consistent topological dynamical system for accepted Penrose tilings.
3. **Not established:** the particular 20-configuration sampling regime, global configuration-space measure, accepted generator, exact Fibonacci hopping rule, analytic UV finiteness, spatial/time interpretation, interacting quantum-vacuum spectral gap, OS reconstruction, or Clay Yang–Mills existence and mass gap.
4. **Current gate status:** PF-G0 source authentication stays OPEN. P0–P5, PF-G0–PF-G5, T0–T5, and gravitational/UV goals are not promoted by this checkpoint. PF-I1 should be indexed as an exact **source-formulation correction**, not a completed continuum theorem.
5. **Reproduction:** `research/scripts/verify_pf_i1_internal_topology.py` uses only the Python standard library, exact integer arithmetic in \(\mathbb Z[\zeta]\), exact rational determinant calculations, and high-precision Decimal evaluations of Fibonacci witnesses; `research/evidence/PF_I1_INTERNAL_TOPOLOGY_EVIDENCE_2026_11_07.json` records test counts and the original Paper2 PDF SHA256. Its finite tests corroborate arithmetic; the density and topology conclusions rest on the proof above. Peer mathematical review remains distinct.

**Immediate next authentic-generator milestone:** source-specific data for Paper2 §7.4: exact accepted \(m\), original window/phason, whether edges mean P3 rhombus edges or augmented quotient edges, weights for each family and base/periodic controls, and exact graph Laplacian/zeta normalization. Only those inputs can adjudicate the reported degree deficit, the 0.833 ratio, and the proposed geometric mechanism without changing the model.
