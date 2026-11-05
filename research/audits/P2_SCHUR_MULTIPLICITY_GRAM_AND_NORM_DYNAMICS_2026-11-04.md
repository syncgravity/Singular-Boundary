# P2 — Exact SU(2) multiplicity-space trace norms and a free-dynamics C*-topology obstruction

**2026-11-04.** Continuation of P-56/P-57, for the corrected original-link open straight SU(2) strip and one fixed independent-face PW first-moment norm. Companion complete mathematical report, three executed independent verifiers, output logs, hashes, and integrity-checked ZIP: \`p2_ground_rank_2026-11-04.zip\`, supplied as a conversation attachment. **No high-spin N≈m² complete-inverse asymptotic, interacting infinite-volume dynamics/gap, Borel reconstruction, OS construction or 4D Yang–Mills mass gap is proved.**

## P-58. Exact finite-depth trace-norm formula from SU(2) multiplicity Gram matrices

Let \(V_{\mathbf n}=\bigotimes_i V_{n_i/2}\), \(S=\sum_i n_i\), and fix a *consistent* unitary SU(2) intertwiner
\[
V_{\mathbf n}=\bigoplus_{J\in\mathcal J_{\mathbf n}}(V_J\otimes\mathcal M_J).
\]
Haar conjugation projects any finite Fourier matrix Z according to Schur:
\[
\boxed{\mathcal T Z=\bigoplus_J \frac{I_{2J+1}}{2J+1}\otimes M_J,\quad
M_J=\operatorname{Tr}_{V_J}(P_J ZP_J).}
\]
If \(Z=\sum_{a=1}^R c_a|u_a\rangle\langle v_a|\) has definite-weight kets and bras, mismatched magnetic weights vanish on twirling. Each surviving term induces one multiplicity-space rank-one matrix. If terms have *different equal* magnetic weights, their multiplicity vectors **must be aligned in a common SU(2) intertwiner** (for example by normalized spin ladder transport); independently chosen weight bases cannot be added naively. Thus
\[
M_J=\sum_{a:\mathrm{wt}(u_a)=\mathrm{wt}(v_a)}
c_a|\mu_{a,J}\rangle\langle\nu_{a,J}|.
\]
The SU(2) spin factors have \(\|I_{2J+1}/(2J+1)\|_1=1\), giving the **exact trace-norm identity**
\[
\boxed{\|\mathcal T Z\|_1=\sum_{J\in\mathcal J_{\mathbf n}}\|M_J\|_1.}\tag{1}
\]
For \(M_J=U_JV_J^\dagger\) with at most R columns, and \(A_J=U_J^\dagger U_J,\ B_J=V_J^\dagger V_J\), its nuclear norm is exactly
\[
\boxed{\|M_J\|_1=\operatorname{tr}\sqrt{A_J^{1/2}B_JA_J^{1/2}}.}\tag{2}
\]
There are O(S) spin sectors and at most R-dimensional Gram problems per sector, *provided the spin-projected multiplicity overlaps have been produced*. The multiplicity dimensions themselves can be exponential; efficient computation of the projected overlaps is an **additional unresolved algorithmic obligation**. When Gram matrices are nearly singular, direct QR/SVD of reduced factors is numerically preferable to square-rooting tiny noisy eigenvalues.

In the corrected physical Poisson source setting of P-56, the q-th exact original-link Neumann approximation \(X_{j,\ell,[q]}=\mathcal T Z_{j,\ell,[q]}\) has a definite-weight rank-one decomposition of at most
\[
R_{N,m,\ell,q}=13(m+1)\sum_{p=0}^q[3(N-1)]^p
\]
terms and total face degree \(S=N-1+\ell\), \(\ell=m\pm1\). Commutation of K's Neumann polynomial with twirling permits (1)–(2) for this *genuine gauge-projected physical q-approximation*. Using the exact first-moment sector weights \(w_{j,\ell}=(\ell+1)^2/[4(m+1)^3]\), define \(T_q=\sum_{j,\ell}w_{j,\ell}\sum_J\|M_{j,\ell,J,q}\|_1\). The previously certified complete electric Neumann nuclear remainder \(\Delta_q\) gives
\[
\boxed{\max(0,T_q-\Delta_q)\le R_{N,m}^{\mathrm{physical}}\le T_q+\Delta_q.}\tag{3}
\]
Equation (3) is a **valid finite-depth exact representation and conditional numerical certification route**, assuming correct spin-projected Gram data and the same proven \(\Delta_q\), not an already computed N≈m² result. Fixed q reduces the Fourier trace-norm calculation to multiplicity Grams; q sufficiently large for a useful remainder, spin alignment, and interval accuracy remain to be demonstrated at growing width.

**Independent checks:** Hopf SU(2) Haar cubature for weight-pure rank-one tensors across 2,3,4 fundamental faces confirms selection/rank and mismatched-weight annihilation. Nine complex sums of terms with common weight were checked by *both* direct Haar twirl singular values and independent total-spin/multiplicity SVD for N=2,3,4, agreeing to 1e−8 (ordinary precision). These are mathematical regressions, not direct q-depth N≈m² physics calculations.

## P-59. Full local B(L²(SU2)) cannot carry point-norm-continuous free Wilson evolution

On the physical one-face **Gauss-invariant class-function sector**, the corrected electric Casimir and bounded character multiplier obey
\[
K\chi_n=n(n+2)\chi_n,\qquad A=M_{\chi_1},\qquad A\chi_n=\chi_{n+1}+\chi_{n-1}.
\]
The free Heisenberg automorphisms \(\alpha_t^0(A)=e^{itK}Ae^{-itK}\) have matrix element
\[
\langle\chi_{n+1},[\alpha_t^0(A)-A]\chi_n\rangle=e^{it(2n+3)}-1.
\]
For \(t_n=\pi/(2n+3)\to0\),
\[
\boxed{\|\alpha_{t_n}^0(A)-A\|\ge2\quad\forall n.}\tag{4}
\]
Therefore the free SU(2) evolution is **not point-norm continuous on the full bounded local operator algebra containing this Wilson character**. The P-57 smooth finite-rank positive-energy commutator inequality is not invalidated; it simply **cannot be promoted by assuming a norm-continuous C*-dynamics on every local bounded observable**. This is a topology/domain obstruction, not a spectral-gap obstruction or proof of failure of unitary dynamics.

One constructive *free one-face* alternative is the **weak/ultraweak time average**, for \(f\in L^1(\mathbb R)\),
\[
A_f=\int_{\mathbb R}^{\mathrm{weak}}f(s)\alpha_s^0(A)\,ds,\qquad
\boxed{\|\alpha_t^0(A_f)-A_f\|\le\|A\|\|f(\cdot-t)-f\|_1\longrightarrow0.}\tag{5}
\]
The integral is deliberately **weak**, not assumed to be a norm-Bochner integral because the unsmeared orbit is not norm-continuous. Time-regularized observables admit norm-continuous *free* evolution; this does **not** construct the interacting infinite-volume evolution with unbounded neighbor derivative terms, nor establish its generator core.

**Independent tests:** exact phase jumps were verified for n=10,20,100,1000,10000 and shrinking \(t_n\), and L1 translation estimates for the elementary time-averaging kernel.

## Next gates and scientific status

**Physical:** build a certified spin-aligned Clebsch–Gordan multiplicity-Gram engine for the *actual* corrected source and Neumann iterates. Evaluate \(T_q\pm\Delta_q\) at joint N≈m² and prove controlled numerical/analytic large-width behavior.

**Thermodynamic:** specify an energy-regularized observable algebra/topology on which the interacting infinite-volume evolution exists, verify a generator core, and promote P-57's local positive-energy condition there. Uniqueness, connected clustering, uniform gap and the mass-gap problem remain open.

**4D continuum Yang–Mills existence and strictly positive mass gap: OPEN.**