# Degree-graded anchored tame theorem for unrestricted one-site spectra (2026-11-02)

**Conditional on the archived original-link SU(2) open-strip full Wigner coefficient conventions**, a degree-graded anchored norm permits arbitrary one-site Peter–Weyl degrees provided that a suitable sitewise spectral moment is finite.

For s>=0, sigma>0, kappa>0, let A^s_(sigma,kappa)(F)=sup_x sum_(I contains x) exp(kappa|I|) sum_n (1+N(n))^s exp(sigma N(n)) ||[F_I]_n||_l1, with N(n)=sum_i n_i.

For a singleton-only extensive family G with G_{ {j} }=g_j, let M_q(G)=sup_j sum_(m>=1)(1+m)^q ||P_m g_j||_W_sigma. **Theorem:** ||K^(-1)Q Gamma_K(F,G)||_(A^s_sigma,kappa) <= (12+exp(kappa)) M_(s+3)(G) ||F||_(A^s_sigma,kappa). This is uniform in ambient strip length, polymer support length, and maximum one-site spectral degree, with no loss in sigma or kappa.

Proof: on an input multidegree a with N>=1, a one-site degree-m insertion at j has original-link incident degree W_j=4a_j+a_(j−1)+a_(j+1); sum_j W_j<=6N. Gamma coefficient is bounded by 3m W_j, Wigner multiplication creates <=m+1 output degrees, every nonconstant output has D_out>=3max(1,N−m), and ||K^−1||_1<=2/D_out. The ratio of polynomial degrees (1+N_out)^s/(1+N)^s <=(1+m)^s. Using N/max(1,N−m)<=m+1, each site contributes <=2 W_j/N times m(m+1)^2(1+m)^s||P_mg_j||. Sum over m at each site using the *sitewise* M_(s+3), and only then over sites, gives coefficient 12. The at-most-two external touching insertions use the archived 1/4 endpoint bound and cost at most exp(kappa) M_s <=exp(kappa) M_(s+3).

**Necessary limitation:** With the exact highest-weight long-polymer/one-site source family, t=m² and normalized A^s and M_q inputs, the output norm is at least exp(−kappa)(1+m)^−q times the exact earlier ungraded expression [(t−2)m/(5t+1+2m²+6m)+3m/(5t+1+2m²+7m)] ~exp(−kappa)m^(1−q)/7. Hence **no uniform tame estimate with a source moment q<1** for any fixed s>=0. The sufficient moment s+3 need not be optimal.

This theorem is **not** A^s x A^s -> A^s bilinear closure for arbitrary extensive multi-support families. Generated output need not remain singleton-supported, so it is not a closed nonlinear fixed-point theorem. No interacting lambda=1 gap or continuum Yang–Mills mass gap is established.

Full report, exact arithmetic verifier (1,989,732 checks), passing log and SHA256 manifest: The Singular Boundary / Proof Audits Library.