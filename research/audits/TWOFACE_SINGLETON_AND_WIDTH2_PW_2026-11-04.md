# First-moment Poisson estimate for all SU(2) history inputs of width at most two

**2026-11-04 · finite original-link open straight SU(2) ladder, gauge-reduced face-coordinate matrix Peter–Weyl trace-expansion norm.** **Proved: one bilinear step on the input subspace of histories of length ≤2. Not proved: invariant space under iteration, arbitrary-history tame inequality, interacting gap or continuum Yang–Mills mass gap.** Full 12 KB proof, six full executable regression scripts, SHA-256 manifest and passing logs are attached to the research conversation in \`singleton_twoface_pw_history_audit_2026-11-04.zip\`.

For SU(2) face holonomies, let \(K=4\sum_i C_i+2\sum_i D_{i,i+1}\), \(D_{i,i+1}=\sum_a R_i^aL_{i+1}^a\), and \(\mathcal B=K^{-1}Q\Gamma_K\) with \(\Gamma_K=(fKg+gKf-K(fg))/2\). SU(2) degree \(n\) is spin \(n/2\), energy \(e_n=n(n+2)\). We work **only** in the gauge-reduced face trace-expansion norm \(P_\sigma(f)=\sum_{\bf n}d_{\bf n}e^{\sigma\sum n_i}\|A_{\bf n}\|_{S_1}\), \(d_{\bf n}=\prod_i(n_i+1)\), and in the local-first history norm \(L^{(k)}_{\kappa,\sigma}\), with weight \(e^{\kappa|I|}(1+\max_i n_i)^k\) inside the anchored spin sum, \(\kappa>0,\sigma\ge0\), integer \(k\ge1\). **We do not equate this norm with the original-link PW norm.** Retain all nonconstant physical outputs and their original union histories.

## New local gate A: two-face arbitrary matrix × overlapping singleton

Let F have two-face history [1,2] and one fixed degree sector (a,n), and G have singleton history on the degree-n face in degree r. Their CG outputs have degrees (a,l), \(l=|n-r|,|n-r|+2,\ldots,n+r\). For a,n,r≥1, write \(P=e_a\), \(N=e_n\), \(R=e_r\), \(L=e_l\), \(A=1+\max(a,n)\), \(B=1+r\), \(W=1+\max(a,l)\). The actual two-face input operator obeys \(\|K_{a,n}\|_{S_1\to S_1}\le(5/4)(P+N)\), while \(\|K_r\|=R\). The actual output inverse is bounded by \(2/(P+L)\), since the two shared-link superoperators are not replaced by free rotors. Applying the exact identity
\[
\mathcal B(F,G)=\tfrac12\{K^{-1}[(KF)G+F(KG)]-FG\},
\]
followed by **CG block pinching in the same PW norm**, gives the per-channel moment multiplier
\[
E_{a,n,r,l}=\frac{W}{AB}\left[\frac12+\frac{5(P+N)+4R}{4(P+L)}\right].
\]
For all permitted l, let \(x=\sqrt{P+L}\ge\sqrt3\). CG triangle conditions imply \(W\le A+B\), \(W\le1+x\), and \(N/(AB),R/(AB)\le(3+x)/2\). Also \(WP/(AB(P+L))\le1\). Therefore
\[
E_{a,n,r,l}\le\frac12+\frac54(2+4/x+3/x^2)
\le \frac{17}4+\frac5{\sqrt3}<8.
\]
The CG nuclear sum is **pinched before** imposing this maximum; there is no factor counting output channels. For each moment k≥1, the corresponding moment ratio to power k is no larger than the first-moment ratio. Zero-degree spectator sectors reduce to the certified same-face 2/3 or adjacent singleton 1/6 estimate, or have vanishing derivative. Hence, for *arbitrary complex two-face PW polynomials* (not just characters), with singleton nested inside:
\[
\boxed{\|\mathcal B_{\rm hist}([I]F,[J]G)\|_{L^{(k)}}
\le 8e^{-\kappa}\|[I]F\|_{L^{(k)}}\|[J]G\|_{L^{(k)}}.}\tag{A}
\]
The low-energy l=0 output is retained whenever the spectator face has nonzero spin.

## New local gate B: two-face matrix × exterior joining singleton

For [1,2] against singleton [3], only the boundary link differentiates both inputs; **the inverse still contains both internal and boundary shared-link terms**. On output degree triple (p,q,r), set \(P=e_p,Q=e_q,R=e_r\), \(D=P+Q+R\), \(S_{12}=\sqrt{PQ}/4\), \(S_{23}=\sqrt{QR}/4\). The true trace-class response satisfies
\[
\|\mathcal B(F,G)\|_1\le
\frac{S_{23}}{D-2S_{12}-2S_{23}}\|F\|_1\|G\|_1.
\]
When \(Q>0\), putting \(x=\sqrt{P/Q}\), \(y=\sqrt{R/Q}\), the inequality
\[
D-2S_{12}-7S_{23}=Q[(x-\tfrac14)^2+(y-\tfrac78)^2+\tfrac{11}{64}]\ge0
\]
proves the conservative uniform bound **1/5**. When Q=0 the source vanishes. The output degrees, dimensions, moments and analytic weights are unchanged; the history union is length 3, equal to the input lengths' sum:
\[
\boxed{\|\mathcal B_{\rm hist}([1,2]F,[3]G)\|_{L^{(k)}}
\le\tfrac15\|[1,2]F\|_{L^{(k)}}\|[3]G\|_{L^{(k)}}.}\tag{B}
\]
**Correction to preliminary testing:** the proposed 1/6 bound for an exterior joining was **not certified**, because it dropped \(S_{12}\) from the inverse; the 1/5 bound above is the final theorem.

## New local gate C: two arbitrary PW matrices on the same two-face history

For F, G both supported on [1,2], use input degree pairs (p,q) and (r,s), all CG output pairs (l,t). Discard only the full Haar-constant (0,0) block. Put \(A=1+\max(p,q)\), \(B=1+\max(r,s)\), \(W=1+\max(l,t)\), \(c=e_l+e_t\ge3\), \(E=e_p+e_q+e_r+e_s\). The original-link input operator norms are ≤5/4 of each respective input energy; the output inverse is ≤2/c. Per-channel trace-class first-moment envelope:
\[
\frac{W}{AB}\left(\frac12+\frac{5E}{4c}\right).
\]
By both SU(2) CG triangle inequalities, \(W\le A+B\), \(W\le1+\sqrt c\) and each of four input Casimir terms divided by AB is ≤(3+\sqrt c)/2 (nonconstant inputs have A,B≥2). Thus the envelope is ≤
\[
\tfrac12+\tfrac52(1+4/\sqrt3+3/3)
=\tfrac{11}{2}+\tfrac{10}{\sqrt3}<12.
\]
As before, CG nuclear block pinching, submultiplicative exponential weights and higher max-spin moments complete the **all-degree** bound
\[
\boxed{\|\mathcal B_{\rm hist}([I]F,[I]G)\|_{L^{(k)}}
\le12e^{-2\kappa}\|[I]F\|_{L^{(k)}}\|[I]G\|_{L^{(k)}}.}\tag{C}
\]

## One-step theorem for arbitrary history families of input width ≤2

Let \(F_j\) denote components with exactly j-face connected history. For **shifted overlapping** length-two histories [1,2] and [2,3], use the **previously established** arbitrary-four-degree fixed-three-face matrix-sector bound \(6e^{-\kappa}\), already audited at \`research/audits/FOUR_DEGREE_PW_MATRIX_OVERLAP_2026-11-04.md\`. For **adjacent** length-two histories [1,2] and [3,4], one boundary edge gives a source norm \(S_{23}\|F\|_1\|G\|_1\), and the four-face inverse bound \(2/D\) with \(S_{23}\le D/8\) gives **1/4**. Disjoint intervals separated by at least one intervening face have zero cross-input derivative.

For a fixed anchored output site x, a given length-two input interval can interact only with intervals whose starts differ by -2,-1,0,1,2. Split by x belonging to the first history or only the second history (double counting safe). Relative history weights are \(e^{-2\kappa}\) for identical intervals, \(e^{-\kappa}\) for one-face overlap and 1 for adjacent intervals. The weighted anchored sums therefore obey
\[
\|\mathcal B_{\rm hist}(F_2,G_2)\|_{L^{(k)}}\le
(24e^{-2\kappa}+24e^{-\kappa}+1)\|F_2\|_{L^{(k)}}\|G_2\|_{L^{(k)}}.
\]
For length-two × singleton, the two interior insertions cost \(2\cdot8e^{-\kappa}\) and the two exterior joinings \(2/5\). Charging the possible exterior output anchor separately adds another \(2/5\):
\[
\|\mathcal B_{\rm hist}(F_2,G_1)\|_{L^{(k)}}\le
(16e^{-\kappa}+4/5)\|F_2\|_{L^{(k)}}\|G_1\|_{L^{(k)}}.
\]
The symmetric bound follows by \(\Gamma_K\)-symmetry. The **previously certified** singleton × singleton constant is \((2/3)(1+e^{-\kappa})\). Summing four bilinear components, for every integer \(k\ge1\), \(\sigma\ge0,\kappa>0\), and arbitrary finite families with history width ≤2,
\[
\boxed{
\|\mathcal B_{\rm hist}(F,G)\|_{L^{(k)}}\le
\left(24e^{-2\kappa}+\frac{170}{3}e^{-\kappa}+\frac{49}{15}\right)
\|F\|_{L^{(k)}}\|G\|_{L^{(k)}}.}\tag{D}
\]
The estimate is uniform in finite strip length and all PW spin degrees; all nonconstant low-energy physical outputs retain their union histories. **Output width can reach 4, so this is a one-step theorem and does not establish arbitrary-history closure or a nonlinear fixed point.** The formal Gevrey/Borel-disk route remains conditional on the all-history operator estimate.

## Independent verification and provenance

The companion ZIP \`singleton_twoface_pw_history_audit_2026-11-04.zip\` includes a detailed 12 KB mathematical report, six passing standalone Python checks, a run log and hashes: 131,424 exact rational nested fusion envelopes; 35,250 anchored nested/fused-family tests at \(\kappa=\log4\); 212 actual two-face non-character complex PW matrix inverse tests in both overlap directions; 108 actual three-face exterior-joining tests; 54 physical two-face self-overlap inverse tests and 147,927 exact scalar self-overlap fusion envelopes; 32 actual four-face boundary-joining tests. Independent regression reproduces the previously audited \(\mathcal B(\chi_1(A)\chi_1(B),\chi_1(A))\), with \(P_0=43/6\) and first-spin-moment norm \(35/2\). These finite tests verify the implementations; all-degree claims rest on the analytical estimates displayed above. No source-certified 3D Penrose transport, interacting \(\lambda=1\) gap, Borel summability or 4D mass gap follows.