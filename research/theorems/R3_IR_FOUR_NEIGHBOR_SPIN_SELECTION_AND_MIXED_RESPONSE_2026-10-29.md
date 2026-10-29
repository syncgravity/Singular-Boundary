# Four-neighbor Wilson selection — research note (2026-10-29)

**Classification:** exact finite-volume SU(2) Hamiltonian structural identities under regular rhombus-disk hypotheses; conditional cap conclusion. The complete proof and verifier are preserved in the local archive `singular_boundary_four_neighbor_selection_2026-10-29.zip`.

Let f be a deleted interior rhombus with four distinct adjacent faces g1,...,g4, and H(t) the Wilson Hamiltonian with magnetic couplings of gi multiplied by ti. All remaining plaquettes retain their original nonlinear interactions.

**FN-1:** if any ti=0, the edge shared by f and gi is magnetic-private, so the unique positive ground state is independent of that link. The target holonomy is exactly Haar and each nontrivial character expectation c_j(t) vanishes.

**FN-2:** independent center-flux flips send ti to -ti up to a scalar energy shift, while preserving the target observable. Its expectation is even in each ti.

**FN-3:** holding all other couplings fixed, Peter-Weyl decomposition on the private shared link and fundamental representation fusion give partial_ti^n c_j|_{ti=0}=0 for every n<2j. Thus an integer spin-j character has no multivariate Taylor monomial of total order below 8j, with at least 2j powers of each neighbor coupling.

**FN-4:** for a positive class convolution cap source k_a, with alpha_a=int phi_a and F_a(t)=<k_a(W_f)>_t, repeated Taylor integration yields the exact full-coupling identity

F_a(1,1,1,1)-alpha_a^2 = int_[0,1]^4 prod_i(1-si) (partial_1^2 partial_2^2 partial_3^2 partial_4^2 F_a)(s) ds.

This does not require a refinement-uniform spectral gap, but the mixed derivative is **not bounded**.

**FN-5:** defining N_a as the same weighted integral of the negative part of that eightfold derivative, cap mass is at least [alpha_a^2-N_a]_+/nu_a, where nu_a=int phi_a^2. A uniform estimate N_(a_h)<=alpha_(a_h)^2/2, a_h~sqrt(h), would imply polynomial cap mass. **This estimate remains OPEN.**

**Comparator obstruction:** the positive center-even SU(2) class rotor with amplitude exp(-kappa prod_i ti^2 p^2) satisfies Haar coordinate hyperplanes, separate evenness, and the entire 2j-per-neighbor character filtration. At full coupling its center cap is exponentially depleted for kappa=h^-1. It is **not** a Wilson lattice counterexample; it shows the selection rules alone do not determine cap survival.

**Verification:** deterministic 3x3 (9 faces, 24 edges) shared-edge incidence, dual center strings, SU(2) fusion arithmetic, and SU(2) rotor comparator. The verifier does not diagonalize a physical multi-link SU(2) Hamiltonian.

**Open:** nonlinear full-coupling mixed response / original normalized low-energy cap response, all-bulk deletion, fixed-support covariance, physical continuum mass gap, and continuum reconstruction.
