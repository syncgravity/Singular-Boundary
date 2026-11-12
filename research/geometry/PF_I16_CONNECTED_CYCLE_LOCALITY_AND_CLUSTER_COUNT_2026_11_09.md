# PF-I16 — Connected-cycle locality, cluster counting, and exact block factorization

**2026-11-09; finite original source-complex audit.** Original authenticated coupled Z^5 accepted Penrose–Fibonacci rhombi, five directional relationships and source-original SU(2) links. No cubic/Voronoi replacement. Full proof, checker, log and SHA-256 manifest are provided in Library as PF_I16_CONNECTED_CYCLE_2026_11_09.zip. This is not a continuum Yang–Mills mass-gap proof.

## Exact connected-history theorem

For a finite source complex G=(V,E,F), choose explicit **auxiliary** coefficients a_e>0, b_f>=0 and H(t)=K+tV, K=Σ_e a_e(-Δ_e), V=Σ_f b_f(1-p_f), p_f=(1/2)Tr U_{∂f}. On any fixed finite graph the strictly positive ground state near t=0 has score S(t)=log Ω(t)=Σ_{n>=1}t^n S_n, with scalar Haar-centered coefficient convention. The original-link score recurrence is

\[
KS_1=-P_0V,\qquad KS_n=P_0\sum_{j=1}^{n-1}\Gamma_K(S_j,S_{n-j}),\quad
\Gamma_K(F,G)=\sum_ea_e\langle\nabla_eF,\nabla_eG\rangle.
\]

Let D be the graph whose vertices are **genuine accepted** rhombi, joined exactly when they share an original link. At every order n, **each nonzero history-labelled term of S_n has a connected set of source face insertions in D, consisting of at most n distinct faces.** Induction: S_1 consists of individual faces. Γ vanishes if its arguments have no common original-link dependence; otherwise their connected history supports join via a shared link. K^{-1}P_0 cannot introduce dependence on outside links (product-link Casimir heat semigroup), so the union history remains connected. Importantly this is a statement about history labels, *not* the minimal support of the final spin-network output.

In particular, faces f,g separated by dual overlap distance d_D(f,g) cannot appear in a common score history at perturbative order n<d_D(f,g)+1.

## Volume-independent combinatorial envelope

In Z^5 an elementary j-edge borders at most two j-k squares per one of four other coordinate directions; accepting a subset only decreases incidence. Thus d_e<=8 and each elementary rhombus shares an edge with at most 4(8−1)=28 **other** rhombi. The number A_k(f) of distinct connected k-face subsets containing a fixed face is bounded, by plane rooted spanning trees and Catalan_{k−1}<=4^{k−1}, by

\[
\boxed{A_k(f)\le 112^{k-1}.}
\]

This count is independent of total source size. **It does not bound the amplitude of a cluster or establish convergence of the nonlinear score.**

## Exact nonperturbative factorization on different overlap components

If the face-overlap graph has disconnected components D_i, their incident original-link edge sets E_i are disjoint. The unconstrained Hamiltonian decomposes as a tensor sum over these edge blocks plus unused free links. Its unique strictly positive ground state is a product of the separate block ground states and constants on unused links. Gauge invariance of each block follows from its Hamiltonian's invariance and positive ground-state uniqueness. Consequently the Gauss-invariant interacting vacuum measure factorizes **exactly** across different face-overlap components at all finite couplings. This does not imply decay within a connected overlap component.

## Remaining PF-I16 gate

The missing theorem must bound actual connected-history amplitudes, including the K^{-1} spin-network response, with constants uniform in accepted source volume and admissible source scales. Earlier extended-fusion counterexamples warn against replacing this with an unsupported positive majorant. Neither physical time/kinetic normalization, source-refinement physical limit, interacting Poincare inequality nor continuum Yang–Mills gap follows from the connected-history result. All remain OPEN.

**Verification:** local three-face overlap path and five-direction elementary incidence enumeration tested through perturbative order 7. This checks abstract local combinatorics, not every historical source crop. Full derivation is in the archived research report. No canonical claims or historic datasets changed.
