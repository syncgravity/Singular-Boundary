# Width-graded anchored tame estimate and fixed-source linear resolvent — 2026-11-02

**Conditional on the archived original-link SU(2) open-strip Wigner coefficient realization and inherited local bilinear / electric inverse certificates.**

Let A^s_(σ,κ)(F)=sup_x Σ_(I∋x) exp(κ|I|) Σ_n (1+Σ_i n_i)^s exp(σΣ_i n_i) ||[F_I]_n||_l1, σ>0, κ>=0, s>=0. Put z=e^(−2σ), S_L(z)=(1−z)^(−L)(1+2Lz/(1−z)).

**THEOREM.** For every η>−log(1−z), the centered quadratic Poisson operation B(F,G)=K^−1QΓ_K(F,G) obeys the arbitrary-source-width tame bound

**||B(F,G)||_(A^s_σ,κ) ≤ C_(σ,η) ||F||_(A^s_σ,κ) ||G||_(A^(s+1)_σ,κ+η)**,

**C_(σ,η)=12 sup_(L≥1)(L+3) q^L (1+aL)<∞**, where q=e^(−η)/(1−z)<1, a=2z/(1−z).

This follows directly from the preceding bounded-width proof *without summing separate widthwise anchored suprema*: at a fixed output anchor x, partition x∈I from x∈J\I. The first is controlled by site-aggregated derivatives; the second incurs at most |J|+2 sites in J enlarged by its two neighboring faces. For each source J, combining them gives 12(|J|+3)S_|J|(z), paid by the additional exp(η|J|) source weight. After applying the uniform scalar supremum C_(σ,η), sum all source intervals J with their actual anchored per-site norm. The bound is independent of the ambient strip size, arbitrary support widths and Peter–Weyl degrees. It preserves analytic radius σ and target exponent κ, at the price of one spectral-degree moment and a stronger source exponent κ+η.

An explicit geometric-series upper bound is
C≤12[q/(1−q)²+3q/(1−q)+a(q(1+q)/(1−q)³+3q/(1−q)²)].

**Exact instance:** σ=log 2, η=log 2 gives z=1/4, q=2/3, a=2/3. The width expression is uniquely maximized at L=3 and equals **64** (the coarser sum bound is 528). Hence ||B(F,G)||_(A^s_log2,κ)≤64||F||_(A^s_log2,κ)||G||_(A^(s+1)_log2,κ+log2).

**COROLLARY, FIXED-SOURCE LINEAR RESOLVENT.** For a fixed G in the stronger space, T_G:F→B(F,G) is bounded on the *same weak space* A^s_(σ,κ). If |λ|C||G||_(strong)<1, (I−λT_G)^−1=Σ_(n≥0)λ^nT_G^n converges and has norm ≤(1−|λ|C||G||)^−1, uniformly in finite strip volume. Repeated applications with the *same fixed stronger source* do not accumulate support-weight loss.

**Limits:** The threshold η>−log(1−z) is required for the displayed majorant, not shown necessary for the actual operator. This is NOT unrestricted A^s×A^s→A^s closure; an evolving output need not have the stronger source exponent. The archived highest-weight counterexample still excludes unrestricted same-weight ungraded closure. No λ=1 nonlinear continuation, interacting spectral gap, or continuum Yang–Mills mass gap is proved. Full mathematical report, exact-arithmetic verifier (113,366 checks), passing log, and SHA256 manifest are in The Singular Boundary / Proof Audits Library.