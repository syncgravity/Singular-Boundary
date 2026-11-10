# PF-I16 — Exact eighth-order topology splitting in authentic three-rhombus SU(2) vacuum

**2026-11-09. Status: exact finite auxiliary quantum theorem, not a continuum mass-gap or physical-time theorem.** Depends on the prior authenticated PF-I11/PF-I16 source-motif replays and exact sixth-order audits. Complete 4-gauge source-operator reconstruction, exact rational eighth-order checker, independent 75-dimensional variational spectrum comparison, log, and SHA-256 receipt: Library \`/The Singular Boundary/Proof Audits/PF_I16_EIGHTH_ORDER_TOPOLOGY_2026_11_09.zip\`. No cubic/Voronoi surrogate.

## The two genuinely accepted original-source motifs

The **four-trivalent** three-face chain has lower \(\mathbb Z^5\) labels/families \(((0,1,0,0,0);2,3)\), \(((0,1,0,0,0);3,4)\), \(((0,1,0,0,1);0,3)\). The **four-valent** three-face chain has \(((0,1,0,0,0);0,2)\), \(((0,1,0,0,0);0,4)\), \(((0,1,0,0,0);3,4)\). In each: 8 original vertices, 10 original source links, cycle rank 3; faces 1–2 and 2–3 share one distinct link each, and faces 1–3 share no link. Both pass strict PF-I11 lower-face perpendicular-triangle acceptance and occur in all eight source-selected crops, as certified in the earlier source-replay audit. The older, **invalid** opposite-faces-of-a-coordinate-cube example is NOT used.

## New exact theorem: the first difference is eighth order

With **chosen auxiliary unit electric** coefficients and original-link Casimir \(C_e\chi_{1/2}=\frac34\chi_{1/2}\), define centered gauge-invariant Hamiltonians
\[
\widehat H_M(\mathbf b)=K_M-\sum_{i=1}^3 b_i p_i,\quad
K_M=\sum_{e\in E_M}C_e,\quad p_i=\frac12\operatorname{Tr}U_{f_i},\quad M\in\{3v,4v\}.
\]
Ground energies are analytic near the Haar electric vacuum, and independent source face-center sign duality forces separate evenness in every \(b_i\). Previous exact PF-I16 records established that the two differently valenced accepted motifs have identical Taylor polynomials through total order six.

**NEW:**
\[
\boxed{\widehat E_{3v}(\mathbf b)-\widehat E_{4v}(\mathbf b)=
\frac{36481}{581335252992000}\ b_1^2b_2^4b_3^2
+O(\|\mathbf b\|^{10}).}
\]
No other eighth-order three-face monomial appears in their difference. In particular, their equal-coupling centered ground energies differ for sufficiently small positive \(b_1=b_2=b_3=t\); the two analytic energy germs are **NOT identical**. The difference is \(\delta=36481/581335252992000\approx 6.275380653803569\times10^{-11}\).

For \(\mathbf b=t(1,1,1)\), the individual exact eighth coefficients are
\[
E^{3v}_8=\frac{1356450005085907}{221392811073208320000},\qquad
E^{4v}_8=\frac{84777256990267}{13837050692075520000}.
\]
These are **auxiliary energy coefficients**, not physical masses or continuum gaps.

## Why the exact eighth coefficient requires only fourth-order wavefunction

Along any integral coupling ray \(\mathbf b=t\mathbf w\), put \(W=\sum_iw_ip_i\), expand the true Haar-mean-one positive ground state \(\psi=1+\sum_{n\ge1}t^n\psi_n\) and energy \(E=\sum_{n\ge2}E_nt^n\). The exact Poisson recurrence on the original-link SU(2) invariant-polynomial algebra is
\[
K\psi_n=W\psi_{n-1}+\sum_{k=2}^nE_k\psi_{n-k},\quad
E_n=-\langle W\psi_{n-1}\rangle_{\rm Haar},\quad
\langle\psi_n\rangle_{\rm Haar}=0.
\]
Compute \(\psi_1,\ldots,\psi_4\) as **exact rational invariant polynomials**, using the original ten-link Casimir reconstructed by SU(2) left/right Lie fields, the exact Haar quaternion moments, and rational \(K^{-1}\) by center-parity block.

The fourth-order trial \(\psi^{[4]}=1+\sum_{n=1}^4t^n\psi_n\) differs from the true ground state by \(O(t^5)\). Since a Rayleigh quotient is stationary at the true ground state, its difference from the true energy is \(O(t^{10})\): its coefficient at \(t^8\) is **exact**, not a truncation artifact. Define \(D_2=\langle\psi_1^2\rangle\), \(D_4=2\langle\psi_1\psi_3\rangle+\langle\psi_2^2\rangle\), \(D_6=2\langle\psi_2\psi_4\rangle+\langle\psi_3^2\rangle\). The eighth-order Rayleigh numerator is \(N_8=-\langle\psi_4,W\psi_3\rangle+E_2\langle\psi_4,\psi_2\rangle\); therefore
\[
\boxed{E_8=N_8-E_2D_6-E_4D_4-E_6D_2.}
\]
\(E_2,E_4,E_6\) are independently established identical source-motif polynomials from the prior PF-I16 reports.

## Full exact coupling-ray check

All following are exact **differences** \([t^8](E_{3v}(t\mathbf w)-E_{4v}(t\mathbf w))\):

| \(\mathbf w\) | Exact rational difference |
|---|---|
| (1,1,1) | 36481/581335252992000 |
| (2,1,1) | 36481/145333813248000 |
| (1,2,1) | 36481/36333453312000 |
| (1,1,2) | 36481/145333813248000 |

No one- or two-face term can distinguish the motifs: the restricted original-link one/two-face Hamiltonians are isomorphic, and the two exterior faces share no original link. By independent center parity, the **only** possible eighth-order difference terms are \(A b_1^4b_2^2b_3^2+B b_1^2b_2^4b_3^2+C b_1^2b_2^2b_3^4\). The first three rays solve uniquely for \(A=0\), \(B=\delta\), \(C=0\); the fourth ray checks the result independently.

**Reproduction:** Two separately chosen spanning-tree gauges **on each** of the two authentic original ten-link graphs were rebuilt from plain-text field-construction scripts. Exact (1,1,1) results coincide between both gauges for each motif; all four coupling-ray exact checks pass in the primary gauges. A separate 75-dimensional generalized Hermitian gauge-invariant Rayleigh–Ritz comparison has identical Haar Gram and Wilson matrices, but distinct electric matrices for the two motifs, and confirms \(\Delta E(t)/t^8\) approaches \(\delta\) as \(t\) decreases. The independently computed numerical ratios at \(t=.8,.6,.5,.4\) are approximately \(5.4354,5.7794,5.9160,6.1600\) times \(10^{-11}\), consistent with \(\delta=6.27538\times10^{-11}\). Numerical subtraction is cancellation-sensitive, and is only a secondary check.

## Boundaries

This result rules out equality of the **centered ground-energy analytic germs** for these two specific authenticated finite auxiliary source motifs, and isolates the first difference in a repeated-middle-face degree-eight term. It does **not** prove the two full interacting spectra differ in a specified additional way, identify a unique intertwiner mechanism, or establish any volume-uniform all-orders cluster bound, interacting Poincaré inequality, source-selected physical kinetic/time scale, OS reconstruction, continuum Yang–Mills construction or physical mass gap. Those gates remain **OPEN**; original private data, canonical main, and Observatory certified proof statuses remain unchanged.