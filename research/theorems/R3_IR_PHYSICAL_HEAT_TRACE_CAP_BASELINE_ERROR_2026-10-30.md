# Physical heat-trace cap baseline error and finite-temperature vacuum-limit criterion

Date 2026-10-30. Status: exact fixed-volume trace inequality, not a regulator-uniform Wilson cap survival estimate. Claim R3-IR-401.

Let H be the genuine finite original-link SU(2) Wilson Hamiltonian restricted to the full physical Gauss-invariant Hilbert space. Let E0 be its simple ground eigenvalue, Omega its normalized positive ground state, and delta>0 its first physical excitation gap. Let O be a positive gauge-invariant bounded multiplication observable with 0<=O<=nu, and F0=<Omega,O Omega>>0. For beta>0 define F_beta=Tr_phys(O exp(-beta H))/Tr_phys(exp(-beta H)).

THEOREM (HT-1). Let D_beta=Tr_phys[Q exp(-beta (H-E0))], with Q=1-|Omega><Omega|. Then

F_beta=(F0 + D_beta G_beta)/(1+D_beta),

where G_beta=Tr_phys[Q O Q exp(-beta(H-E0))]/D_beta lies in [0,nu] (define it as zero if D_beta=0). Consequently

|F_beta-F0| <= nu D_beta/(1+D_beta). (HT-1)

Proof: diagonalize the positive trace-class heat semigroup in the physical Hilbert space. The first term is the rank-one vacuum, all remaining contributions are positive weighted diagonal matrix elements of O in [0,nu]. As F0 is also in [0,nu], their difference has absolute value at most nu. No Euclidean path measure factorization, gauge fixing or unphysical trace is needed.

THEOREM (HT-2). For any fixed beta0>0 and beta>=beta0,

D_beta <= D_beta0 exp[-(beta-beta0) delta]. (HT-2)

Proof: each excited eigenvalue exceeds E0 by at least delta, and its positive exponential factor satisfies the stated bound.

CAP BASELINE. On any zero-neighbor coordinate hyperplane in the archived four-neighbor deleted-target Wilson setup, the true ground-state private-link theorem gives F0=alpha_a^2. Therefore

|F_beta/alpha_a^2-1| <= (nu_a/alpha_a^2) D_beta/(1+D_beta). (HT-3)

This is an explicit, physically correct quantitative replacement for incorrectly asserting F_beta=alpha_a^2 at finite beta.

For a fixed-shape SU(2) convolution bump of radius a, alpha_a^2/nu_a is order a^3. Thus making the relative baseline error small at shrinking a requires D_beta=o(a^3). By HT-2 a sufficient fixed-lattice choice of beta must account for the physical delta and the potentially extensive D_beta0. For a_h of order sqrt(h), the condition is D_beta=o(h^(3/2)). A choice of beta independent of h has not been justified.

COUPLING TRANSPORT VACUUM LIMIT. Along the last-neighbor comparison t=0 to t=1, define D_beta^(t), delta_t and F_beta(t). The cosh identity remains exact:
F_beta(1)/F_beta(0)=E_{beta,0}^O cosh(X)/E_{beta,0} cosh(X),
under the archived center-flux involution, with X=b integral_0^beta p_g(U_s)ds.
Applying HT-1 separately at t=0,1 establishes convergence of this RATIO to F0(1)/F0(0) at each fixed finite lattice. It does not allow taking limits of numerator and denominator cosh moments separately, and it does not provide a favorable bound on the ratio. Uniformity in Penrose refinement would require separate uniform physical excitation heat-trace estimates, which are not proved and may be intertwined with the unresolved spectral question.

Classification: HT-1 and HT-2 exact finite-volume positive-trace inequalities. HT-3 is conditional on the previously established private-edge ground-state Haar identity. No mass gap or uniform full-coupling cap survival is claimed.
