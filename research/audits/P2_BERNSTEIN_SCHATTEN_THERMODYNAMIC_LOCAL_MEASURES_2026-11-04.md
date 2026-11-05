# P2: certified convergent Schatten-moment hierarchy and thermodynamic SU(2) diagonal local measures

**Private audit — 2026-11-04.** Corrected original-link SU(2) open straight strips, independent-face PW nuclear norm. These are two separate technical results. Full expanded proof, executable independent checks, logs and SHA-256-verified portable ZIP are in companion artifact \`p2_bernstein_thermo_local_2026-11-04.zip\`. **Neither establishes an actual large-N≈m² same-grade response bound, infinite-volume quantum ground-state vector, uniform gap, positive-ray Borel summability, or 4D continuum Yang–Mills mass gap.**

## P-52. Increasing Bernstein hierarchy gives exact two-sided trace-norm approximations from finite moments

For any finite matrix X, set Q=X†X and choose **any certified upper** u≥||X||op>0. For n≥1 define the Bernstein polynomial
\[
b_n(t)=\sum_{k=1}^n\sqrt{k/n}\binom nk t^k(1-t)^{n-k},\quad t\in[0,1].
\]
Concavity of sqrt and Jensen give b_n(t)≤sqrt(t); coupling a uniformly deleted Bernoulli trial from n+1 to n and conditional Jensen gives b_n≤b_(n+1). Binomial law of large numbers yields b_n→sqrt(t). Thus
\[
\boxed{\mathcal L_n(X;u)=u\,\mathrm{tr}\,b_n(Q/u²)\nearrow||X||_1.}
\]
Hölder/Jensen and binomial variance give \(0≤\sqrt t-b_n(t)≤(t(1-t)/n)^{1/4}≤(4n)^{-1/4}\). For any rank bound r≥rank X,
\[
\boxed{\mathcal L_n(X;u)≤||X||_1≤\mathcal L_n(X;u)+ru(4n)^{-1/4}.}
\]
Because b_n(0)=0 and b_n is a polynomial of degree n, \(\mathcal L_n\) depends *only* on even moments \(T_{2k}=\mathrm{tr}(Q^k)\), k≤n, with exact expansion coefficients
\[
b_n(t)=\sum_{j=1}^n\binom nj\left[\sum_{k=1}^j(-1)^{j-k}\binom jk\sqrt{k/n}\right]t^j.
\]
For the P-38 exact q-term physical original-link Neumann tensor factorization X_(c,q)=UV†, the **small** Gram matrices A=U†U and B=V†V yield T_(2k)=tr((AB)^k), while u can be sqrt(||A||op||B||op) and r can be number of columns. For all **disjoint** Gauss-invariant output sectors c=(j,l) (m≥3), at first moment grade σ=0 the exact weight is \(w_c=(l+1)^2/[4(m+1)^3]\). Put \(S_{nq}=\sum_c w_c\mathcal L_n(X_{c,q};u_c)\), \(E_{nq}=(4n)^{-1/4}\sum_c w_c r_cu_c\). Using the **independently certified** P-36 total original-link inverse Neumann nuclear error Δ_q, the true full physical response R obeys
\[
\boxed{\max(0,S_{nq}-\Delta_q)\le R\le S_{nq}+E_{nq}+\Delta_q.}
\]
For every **fixed finite N,m**, n→∞ and then q→∞ recover the exact R; for N≈m² there is NO proven polynomial bit-complexity, controlled conditioning, or uniform same-grade estimate. Bernstein positive-basis evaluation on the small Gram spectrum is numerically preferable to cancellation-prone high-degree moment-coefficient expansion. Twenty independent random complex matrices and nine levels each passed monotonicity, lower and upper-error checks.

## P-53. Translation-invariant subsequential diagonal probabilities with controlled local Sobolev energy

For each real λ, let ψ_(N,λ)>0 be the unique finite-strip ground eigenfunction from P-49 of \(H_N=K_N+\lambda V_N\), \(V_N=-\frac12\sum_j\chi_1(U_j)\), with normalized Haar diagonal probability \(\mu_N=|\psi_N|²\,dg^N\). Independently sample anchor J uniform on {1,...,N}; place the whole μ_N strip on sites [1−J,N−J]⊂Z and fill exterior faces with independent normalized Haar. This defines a probability ν_N on the compact metrizable infinite product G^Z, G=SU(2). A shift of the anchor changes the uniform anchor distribution only at its two endpoints:
\[
\boxed{|\nu_N(f\circ T)-\nu_N(f)|\le2||f||_\infty/N}
\]
for bounded f. By compactness, **every** sequence N→∞ has a weakly converging subsequence; every limit ν∞ is exactly shift-invariant and globally SU(2)-conjugation-invariant. This is a **diagonal configuration probability**, NOT a quantum GNS ground state, and no full-sequence convergence or uniqueness is claimed.

The corrected physical PW electric sector operator has quadratic-form inequality \(K_N\ge2\sum_i C_i\) (free spectral diagonal D=4Σ C_i and cross-term ≤D/2). Since E_N(λ)≤0 (constant trial) and |V_N|≤N,
\[
\boxed{\sum_i\langle\psi_N,C_i\psi_N\rangle\le N|\lambda|/2.}
\]
For any finite set of sites W (size s), let \(p_{N,W}\) be the normalized-Haar density of its marginal under ν_N. Partial trace and mixture lower the convex square-root Dirichlet/Fisher form (Cauchy–Schwarz/Hoffmann–Ostenhof), and a given physical site is counted at most s times when anchors are averaged; hence
\[
\boxed{\sum_{i\in W}\langle\sqrt{p_{N,W}},C_i\sqrt{p_{N,W}}\rangle\le s|\lambda|/2.}
\]
On compact G^s the sqrt densities are uniformly H¹ bounded. Rellich compactness together with weak convergence shows **each limiting finite-window marginal has an L¹ density** with sqrt in H¹ and the same lower-semicontinuous bound. This is a regularity theorem for the infinite-strip diagonal probability, not clustering or a uniform spectral gap.

The measures are **nontrivial** at nonzero coupling. Finite E_N/N is concave in λ and E_N(0)=0. At λ>0, Feynman–Hellmann and the previously certified product trial give \(E_N'(λ)/N≤E_N(λ)/(Nλ)≤[3-\sqrt{9+\lambda²}]/(2\lambda)\). Hence, for every N and every weak thermodynamic subsequential limit,
\[
\boxed{\nu_\infty[\chi_1(U_0)]\ge\frac{\sqrt{9+\lambda²}-3}{\lambda}>0,\quad\lambda>0.}
\]
For negative λ, central SU(2) inversion gives the corresponding strictly negative sign; λ=0 gives iid Haar. At every differentiability point of the P-51 thermodynamic energy density, the **full** averaged one-face expectation sequence converges:
\[
\boxed{\lim_{N\to\infty}\nu_N[\chi_1(U_0)]=-2e_\infty'(\lambda).}
\]
This does not establish uniqueness of the full ν∞ probability, convergence of connected correlations, quantum ground-state positivity for infinite dynamics, uniform gap, OS axioms, or physical Borel summability.

## Independent tests and next gates

The self-contained companion includes \`verify_bernstein.py\` (20 random complex matrices, 9 hierarchy levels, certified rank/error) and \`verify_magnetic_thermo.py\` (seven numerical actual SU(2) one-face Jacobi magnetizations compared with the analytic positive lower bound); both passed, with logs and SHA256SUMS.txt. The theorems are analytic and do not rely on sample tests.

**Next physical:** certify enough Gram moments and electric remainder at N≈m² to decide a uniform Schatten bound or physical high-spin divergence. **Next thermodynamic:** establish spatial uniqueness/quantum local-state convergence and a uniform gap; diagonal measures and energy density do not suffice. **Next analytic:** actual sign-sensitive Borel positive-ray continuation, still open.

**Continuum four-dimensional Yang–Mills existence and mass gap: OPEN.**