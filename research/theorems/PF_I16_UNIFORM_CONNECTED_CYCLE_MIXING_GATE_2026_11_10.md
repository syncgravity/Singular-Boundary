# PF-I16 — Uniform connected-cycle mixing: next proof gate

**Date:** 2026-11-10. **Status:** one exact combinatorial majorant established; interacting Wilson-vacuum amplitude bound remains OPEN. This is not a spectral-gap or Yang–Mills mass-gap theorem. Geometry is the original five-direction coupled-Z5 Penrose–Fibonacci accepted rhombi; no cubic, Voronoi, or extruded substitute.

> **SUPERSEDED INCIDENCE CONSTANTS — retain as historical derivation, not the current source-uniform bound.** The degree-four / (16^{k-1}) count below applies only to the eight tested finite crops, unless a separate all-source proof is supplied. The universal five-direction inventory gives (d_e\le8), face-overlap degree (D\le28), and rooted count (784^{k-1}). See [PF-I16 connected-support incidence correction](PF_I16_CONNECTED_SUPPORT_INCIDENCE_CORRECTION_2026_11_10.md). The conditional activity-majorant implication remains valid with the corrected threshold (784q<1); no activity majorant is proved here.

## 1. Fixed model and established input

For a finite source complex G=(V,E,F), consider H_G(b)=K_G−Σ_f b_f p_f, K_G=Σ_e a_e C_e, p_f=Tr(U_boundary f)/2, with a_e≥a0>0, 0≤b_f≤b0, and C_e chi_1/2=(3/4)chi_1/2. The centered convention removes the irrelevant scalar in Σ_f b_f(1−p_f).

Available finite-source results: (1) independent face-center sign duality makes the centered ground-energy germ even separately in every b_f; (2) disconnected face-overlap support has zero exact-support coefficient, so a coefficient on k distinct faces has degree at least 2k; (3) the universal five-direction inventory gives at most eight candidate rhombi per original link, while the eight audited crops have at most two observed accepted-face incidences per link; only the latter finite-crop fact yields face-overlap degree at most four; (4) pure-electric vacuum is unique with local excitation scale at least 3a0/4, while each centered face perturbation has norm at most b0 and acts on four link factors; (5) the one-link information estimate is volume-independent but averaged, not Dobrushin, conditional essential-supremum, approximate tensorization, or fiber Poincare.

## 2. Exact combinatorial lemma: connected-support growth

For the eight tested crops only, the face-overlap graph has observed maximum degree four. The source-uniform inventory instead gives maximum degree 28; use that value for a universal count. Fix a root face f. For every connected vertex set S containing f with |S|=k, choose a deterministic spanning tree and perform depth-first traversal from f. The closed walk has length 2(k−1), visits exactly S, and has at most 28 choices at every step for the source-uniform bound (four on the eight audited crops only). Distinct sets have distinct visited-vertex sets. Therefore

    # {S containing f : |S|=k, S connected} ≤ 28^(2(k−1)) = 784^(k−1) for the source-uniform count (16^(k−1) on the eight tested crops only).

Counting rooted pairs, each unrooted support having k roots, gives

    # {S : |S|=k, S connected} ≤ |F| 784^(k−1) / k for the source-uniform bound.

This is purely combinatorial and independent of source volume. The accompanying exact-rational checker verifies the first values and geometric-majorant arithmetic.

## 3. Precise analytic estimate needed

For each T subset F, let E_T(b_T) be the centered ground energy with couplings outside T set to zero. Define the exact-support Möbius activity zeta_G(S;b)=Σ_{T subset S} (−1)^(|S|−|T|) E_T(b_T). This is unambiguous at finite volume; disconnected-support factorization makes it vanish for disconnected S. Its Taylor series contains exactly monomials whose support is all of S.

The desired source-volume-uniform theorem is |zeta_G(S;b)| ≤ A q^|S| for every connected S, with A and q independent of |V|, |E|, |F|, and with 784q<1 in a nonempty explicit weak-coupling regime.

Combining the rooted count with this estimate gives, for each root face f,

    Σ_{S connected, S contains f} |zeta_G(S;b)| ≤ A Σ_{k≥1} 784^(k−1) q^k = A q/(1−784q), provided 784q<1.

Thus the combinatorial part of cluster summability is complete conditional on the activity estimate. A bound only on the first coefficient c(S)=[product over f in S of b_f^2] E0 would control only the leading term; it would not control higher powers on the same support or the full activity.

## 4. Why existing estimates do not prove the activity bound

The one-link Fisher-information estimate controls an average of |grad_e log Omega|^2. It cannot be upgraded to a uniform conditional score bound by Cauchy–Schwarz, nor does it control conditional density near small values. The existing positive-vacuum countermodel shows bounded local kinetic energy / conditional information alone does not force a uniform gap for arbitrary positive states.

Fixed-volume Kato analyticity can have a radius depending on the total perturbation norm, which grows with source volume. It does not provide a uniform Taylor radius. The missing estimate requires control of resolvents and high-spin intermediate states generated by overlapping four-link Wilson operators. A candidate route is a quantum polymer or Kirkwood–Thomas expansion around the product electric vacuum, with local gap 3a0/4, four-link interaction supports, at most eight candidate rhombi per original link, face-overlap degree at most 28 universally; degree at most four only on the eight tested crops, and an explicit tree-graph bound on repeated shared-link fusion. The missing step is a volume-independent operator-norm or weighted-resolvent estimate valid in the infinite-dimensional SU(2) Peter–Weyl tower.

## 5. Four-face census qualification

The Ngrid=7 support audit proves the count of 18,900 connected unordered four-face supports and exhausts seven incidence-signature categories. It explicitly records that the per-instance full decorated face-edge-vertex isomorphism pass did not complete for all 18,900 (more than 10,000 were checked). The seven representative motifs are pairwise non-isomorphic, but signature membership alone does not prove every support in a category is fully isomorphic to its representative.

Accordingly, the seven representative C_(2,2,2,2) fractions are exact for those representatives. Any multiplicity-weighted 18,900-support aggregate assuming every instance has its representative's coefficient remains PROVISIONAL until a complete decorated-isomorphism pass, direct exact coefficient computation on every support, or a theorem proving coefficient invariance under the coarser signature is supplied. This does not affect local representative calculations.

## 6. Acceptance gates

| Obligation | Status |
|---|---|
| Face-overlap maximum degree ≤28 | Established for the universal five-direction inventory |
| Rooted connected-support count ≤784^(k−1) | Proved here for the universal bound; 16^(k−1) finite-crop only |
| Conditional summability implication 784q<1 ⇒ Aq/(1−784q) | Proved here |
| Uniform Wilson-vacuum activity bound | OPEN — principal next theorem |
| Uniform conditional fiber Poincare / approximate tensorization | Open |
| Uniform interacting auxiliary spectral gap | Open |
| Source-derived physical kinetic/time normalization | Open |
| Continuum / OS reconstruction and 4D Yang–Mills mass gap | Open |

**Verdict:** connected-support combinatorial entropy is controlled with the conservative universal constant 784; the sharper constant 16 is crop-specific. The proof bottleneck is the quantum amplitude: establish the activity bound by controlling repeated shared-link fusion uniformly in volume. Until then there is no all-orders cluster-summability theorem and no interacting mass-gap conclusion.