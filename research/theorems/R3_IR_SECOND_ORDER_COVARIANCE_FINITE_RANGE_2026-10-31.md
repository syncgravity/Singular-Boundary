# R3-IR — Exact second-order locality of Wilson domino-loop covariance

**2026-10-31; finite simply connected SU(2) original-link square disks; coupling derivative at lambda=0 only.**

Let H_lambda=K+lambda V_-, with K=-sum a_e Delta_e, V_-=sum_(k != f) b_k(1-p_k), Omega_lambda normalized positive vacuum, nu_lambda=Omega_lambda^2 mu, F=partial_lambda log Omega_lambda|0=sum c_k p_k, and Q=partial_lambda^2 log Omega_lambda|0. Prior exact free-resolvent analysis writes Q as a linear combination of constants, individual p_k^2, adjacent p_k p_l and adjacent two-face exterior traces r_kl.

For two **distinct** simple two-face domino outer-loop traces r_i, r_j with enclosed face regions D_i,D_j, the exact second covariance derivative is

C''_ij(0)=2 E_mu[r_i r_j (Q+2F^2)].

This also applies on the diagonal, since first coupling derivatives of individual loop means vanish and all loop means are zero at lambda=0. First derivatives of covariance vanish by the already established face-parity theorem.

**Main finite-range theorem:** whenever D_i and D_j share no elementary face, C''_ij(0)=0 exactly for all positive electric and magnetic coefficients. SU(2) central parity requires the mod-2 sum of Wilson-loop boundaries to vanish at every original link. On a planar disk the mod-2 2-boundary map is injective, hence a nonzero contraction requires D_i symmetric-difference D_j to match the face region represented by the other loop factors. For disjoint two-face dominoes that symmetric difference has four faces; each monomial of Q+2F^2 contains at most two elementary plaquette factors, or a single two-face exterior character. No matching contraction exists.

**Bounded-degree conclusion:** every square-lattice domino overlaps in at most six other dominoes by sharing a face, so the **off-diagonal support** of C''(0) has maximum row degree six independent of cage size. This is support locality, *not* a uniform bound on nonzero coefficients, not physical-coupling covariance decay, and not a continuum mass-gap result.

Independent exhaustive support check on N=3,5,7,9,11,15,21 enumerated **479,088** unordered distinct domino pairs, including **474,206** disjoint pairs, with zero parity-support violations. This checker verifies a necessary parity selection condition, not the values of surviving SU(2) integrals. Reproducible scripts, results and checksums are in the Library Proof Audits archive R3_IR_SECOND_ORDER_COVARIANCE_FINITE_RANGE_2026-10-31.zip.