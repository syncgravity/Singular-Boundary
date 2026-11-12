# PF-I16 — Sharp four-face SU(2) Schatten threshold and exact C2222 extraction

**2026-11-09 · FINITE AUTHENTIC ORIGINAL-SOURCE THEOREM; NOT A PHYSICAL MASS GAP.** Companion full proof, seven original-source face witness graphs, runnable spin-network and exact Mobius checkers, execution log and hash manifest: Library \`/The Singular Boundary/Proof Audits/PF_I16_FOUR_FACE_SCHATTEN_AND_MOBIUS_2026_11_09.zip\`. Continues the audited Ngrid=7 original PF-I11 face-acceptance replay and exhaustive 18,900-case/7-class face–edge–vertex isomorphism certificate. It does not re-run all 18,900 source instances itself or the author's SHA-pinned unpublished generator.

## New sharp spectral theorem: all seven four-face classes

Let \(C\) be any of the **seven authenticated** connected four-rhombus original-link graphs. Each has cycle rank \(r=E-V+1=4\) and no bridges. Let \(K_C=\sum_{e\in E(C)}a_e C_e\) be its Gauss-invariant SU(2) pure-electric Casimir with each \(a_e>0\), and \(P_0\) the projection orthogonal to its unique constant Haar vacuum. Then
\[
\boxed{K_C^{-1}P_0\in\mathcal S_p\iff p>\frac92.}
\]
In particular **the inverse is not Hilbert–Schmidt for any of the seven four-face classes**, despite the positive uniform electric operator-norm gap. This gauge-configuration spectral exponent **is not physical spacetime dimension**.

**Elementary exact proof.** Suppress original-link degree-two vertices *only for SU(2) spin-network representation labeling*, retaining strand Casimir weights \(A_s=\sum_{e\in s}a_e\). The reduced multigraph has \(E'\) strands and \(V'\) vertices, all degrees \(d_v\ge3\); its graph-cycle rank remains 4. SU(2) spin networks indexed by strand twice-spins \(n_s\) and invariant vertex intertwiners diagonalize K with \(E(\mathbf n)=\frac14\sum_sA_s n_s(n_s+2)\). At twice-spin cutoff R the number of edge-label assignments is \(O(R^{E'})\) and the dimension of a degree-d invariant vertex intertwiner is \(O(R^{d-3})\) (from successive Clebsch–Gordan channels). The exponent is
\[
E'+\sum_v(d_v-3)=3E'-3V'=3(r-1)=9.
\]
The bound is SHARP: restrict all twice-spins and all \(d_v-3\) independent internal intertwiner channels to even integers in \([R,2R)\). Every trivalent fusion triangle and parity rule is automatically met, providing \(\Omega(R^9)\) states in each dyadic shell with eigenvalues \(\Theta(R^2)\). Upper and lower estimates give eigenvalue counting \(N_C(\Lambda)\asymp\Lambda^{9/2}\) and the exact Schatten threshold \(p>9/2\), including divergence at equality.

Reduced class diagnostics, retaining original distinct graph topologies:
|Source class frequency|Original V/E|Reduced V'/E'|Reduced vertex degrees|Independent strand labels|Intertwiner exponent|
|---:|---|---|---|---:|---:|
|6582|10/13|5/8|3,3,3,3,4|8|1|
|4402|9/12|5/8|3,3,3,3,4|8|1|
|2800|10/13|4/7|3,3,3,5|7|2|
|2711|10/13|6/9|3,3,3,3,3,3|9|0|
|1140|10/13|4/7|3,3,4,4|7|2|
|1140|10/13|4/7|3,3,4,4|7|2|
|125|9/12|5/8|3,3,3,3,4|8|1|

All seven give exponent 9. A separate exact SU(2) Clebsch–Gordan multiplicity enumeration at strand spin cutoff 2 yields non-vacuum states 262,253,313,232,297,302,250 respectively, with truncated \(\operatorname{Tr}K^{-2}\) equal to 2.222682730,2.432915600,2.463963496,2.080042007,2.369853436,2.384148145,2.422834894. These finite-cutoff values **do not prove** divergence; the explicit dyadic argument does.

**Generalization:** For any fixed finite connected bridgeless SU(2) original-link graph with cycle rank \(r\ge2\), positive coefficients and the same Gauss constraints, the spin-network argument establishes \(K^{-1}P_0\in\mathcal S_p\iff p>\frac32(r-1)\). A single simple cycle is exceptional: class-function sector threshold \(p>1/2\).

## New exact 16-subset linked-coefficient extraction

For any face-marked four-face connected support \(S=\{f_1,f_2,f_3,f_4\}\), write \(e_T(t)\) for the analytic near-zero centered ground energy of \(K_C-t\sum_{f\in T}p_f\), with all omitted face couplings set to zero. Exact independent center-sign duality ensures evenness separately in each face coupling. **The first genuine four-face coefficient** is therefore
\[
\boxed{C_{2,2,2,2}(S)=[t^8]\sum_{T\subseteq S}(-1)^{4-|T|}e_T(t).}
\]
Proof: Boolean-lattice Möbius subtraction removes all Taylor monomials missing any of the four faces; degree eight with each present exponent even forces precisely \((2,2,2,2)\). This requires only 16 univariate energy coefficients, not all multivariate order-eight terms.

As in the previous exact eighth-order three-face PF-I16 certificate, each \(e_T\) can be evaluated to eighth order using the **exact fourth-order Haar-normalized wavefunction**: variational stationarity makes the Rayleigh-quotient error \(O(t^{10})\) for an \(O(t^5)\) wavefunction truncation. Exact rational SU(2) invariant-polynomial moments and finite Poisson inverses are available in the archived prior three-face machinery. The 16-subset Möbius identity was independently tested with exact rational symbolic coefficients.

**CRUCIAL SCOPE:** This continuation does **not** calculate any of the seven unknown rational \(C_{2,2,2,2}\) values. The analytic extraction identity and sharp spin-network theorem are the completed results. No assertion of an all-orders cluster bound, uniform interacting gap, source-derived kinetic/physical clock, OS reconstruction, continuum Yang–Mills or physical mass gap is made. All these gates remain **OPEN**. Canonical main, historical source archives, and Observatory proof statuses unchanged.