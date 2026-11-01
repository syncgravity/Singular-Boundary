# R3-IR — Fixed-volume convergence-radius and cluster-counting gate (2026-10-31)

Let K=−Σ_e a_e Δ_e on product Haar SU(2) original links and P=Σ_(k≠f)b_k p_k, B=Σ|b_k|. The free vacuum has spectral gap δ=3 min_e a_e/4. On complex |λ|≤r=δ/(8B), the Riesz eigenprojection Πλ for K−λP obeys ||Πλ−Π0||≤1/3, from the free resolvent bound 2/δ. The analytic vacuum ψλ=Πλ1 has norm ≤4/3 and complex bilinear normalization |∫ψλ²|≥2/9. Thus all connected covariances of observables |A|,|C|≤1 have complex modulus ≤72 in this disk.

Combining Cauchy coefficients |c_n|≤72r^-n with the previously proved distance-order vanishing c_n=0 for n<2d+2, for disjoint dominoes distance d:
**|Cov_νλ(r_D,r_E)|≤72(|λ|/r)^(2d+2)/(1−|λ|/r) for |λ|<r**, with **r=3 min_e a_e/[32Σ_(k≠f)|b_k|]**. This is genuine but finite-volume and nonuniform in cage size, since B is extensive. For square N×N uniform (a,b), r=3a/[32(N²−1)b], so λ=1 is not controlled in the relevant regime.

Separate combinatorial lemma: the number of connected square-lattice s-face sets containing a fixed root face is ≤16^(s−1), from a canonical rooted depth-first spanning-tree word with 2(s−1) steps in four directions. This is only a cluster COUNT. A local connected-cluster coefficient bound or convergent expansion has NOT been proved; without it the count alone gives no local convergence radius. Enumerated exact rooted animals for s=1,...,8: 1,4,18,76,315,1296,5320,21800, satisfying the bound.

Full proof and executable checker at Library /The Singular Boundary/Proof Audits/R3_IR_FINITE_RADIUS_CLUSTER_COUNT_GATE_2026-10-31.zip. Physical-coupling decay, regulator-uniform current, and continuum Yang–Mills mass gap remain open.