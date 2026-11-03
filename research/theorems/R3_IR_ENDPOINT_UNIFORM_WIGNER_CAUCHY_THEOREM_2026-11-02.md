# Uniform Wigner endpoint theorem by two Cauchy inequalities — 2026-11-02

**Exact theorem, under the archived original-link open-strip SU(2) operator conventions.** For any finite open face chain, n_i nonnegative integer PW degrees, d_i=n_i(n_i+2), D=sum_i d_i>0, K_t=D I-2sum_i C_i, with C_i acting on the uncoupled Wigner magnetic indices of neighboring faces:

**||C_i||_(1→1) ≤ sqrt(d_i d_(i+1))/4.**
**||K_t^(-1)||_(1→1) ≤ 2/D.**
**||K_t^(-1)C_b||_(1→1) ≤ 1/4** for every t,b and every degree profile, without any degree cutoff.
In fact ||K_t^(-1)C_b|| ≤ sqrt(d_b d_(b+1)) / [4D-2sum_i sqrt(d_i d_(i+1))] ≤1/4.

Proof of the edge bound. On a matrix-coefficient column with doubled magnetic indices a,b, the diagonal magnitude is |ab|/4. The two offdiagonal ladder entries are
sqrt[(x-a)(x+a+2)(y+b)(y-b+2)]/8
and sqrt[(x+a)(x-a+2)(y-b)(y+b+2)]/8.
First Cauchy bounds their sum by sqrt[(x(x+2)-a²)(y(y+2)-b²)]/4. A second Cauchy, on vectors (|a|,sqrt[x(x+2)-a²]) and (|b|,sqrt[y(y+2)-b²]), bounds the entire absolute column sum by sqrt[x(x+2)y(y+2)]/4. The transition factors vanish at magnetic boundaries.

For the chain, 2sum_i||C_i|| ≤ (1/2)sum_i sqrt(d_i d_(i+1)) ≤ (1/4)sum_i(d_i+d_(i+1)) ≤ D/2. Hence the Wigner l1 Neumann expansion of K_t^(-1) converges uniformly in all nonconstant blocks; multiply ||K_t^(-1)|| ≤2/D by the endpoint bound and sqrt(d_b d_(b+1))≤(d_b+d_(b+1))/2≤D/2.

**Optimal two-face constant:** ||K_2^(-1)C_1||≤1/6, since p=sqrt(d_1d_2)≤D/2 and ||K_2^(-1)C||≤(p/4)/(D-p/2). On the one-dimensional equal-degree highest-weight sector x=y=n, the norm ratio is n/(6n+16)→1/6, proving **sup_(x,y≥1)||K_2^(-1)C_1||=1/6**.

For face-disjoint touching polymers I=[1,b], J=[b+1,t], the archived formula Γ_K(f,g)=C_b(fg) and multiplicativity of unnormalized Wigner coefficient l1 for products on disjoint face sets give **||K_t^(-1)P_0Γ_K(f,g)||_(W_sigma(T))≤(1/4)||f||_(W_sigma(I))||g||_(W_sigma(J))**, all σ≥0, without analytic-radius loss, any t.

This theorem corrects the pessimistic earlier diagonal-margin analysis: tent profiles that failed its *crude* bound satisfy the sharp bound unconditionally. It closes the touching-support endpoint issue, **not** overlapping-support nonlinear convolution, thermodynamic interacting lambda=1 spectral gap, or the continuum 4D Yang–Mills mass gap. Its applicability to a gauge-invariant full theory remains conditional on independently validating the archived original-link face-coordinate model.

Full mathematical proof and independent verifier in Proof Audits Library. Verification: 1,830 exact ladder identities, 15,625 finite magnetic sectors, 50,000 rational profile tests, exact two-face asymptotic and finite matrix scans; all passed.