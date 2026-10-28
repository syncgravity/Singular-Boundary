# R3-IR / R2 — spectral tightness from interacting Wilson variance; one-face strong-field temporal-collapse countertest

**Date:** 2026-10-28. **Scope:** independent mathematical implications for finite gauge-invariant physical Hamiltonians, plus a genuine single-face SU(2) strongly magnetic asymptotic. **The interacting Penrose variance bounds, continuum reconstruction and physical mass gap are OPEN.** No Monte Carlo, synthetic historical records or source modifications.

## 1. Input that has already been established

On finite face-complete Penrose spatial regulators let H_h be the gauge-invariant Wilson Hamiltonian with the *declared* spatial dual-area coefficients, and take a compactly supported real test function φ. Define the centered physical multiplier

`F_h[φ]=h^(-1) Σ_f A_f φ(x_f)(p_f−<p_f>_h)` and its vacuum excitation spectral measure `μ_h` on `(0,∞)`, with total mass `V_h` and first moment `M_h`.

The earlier independently derived Dirichlet/first-moment inequality (original project FORMAL_FRAME_AUDIT.md F1 and research/theorems/R3_IR_RENORMALIZED_WILSON_REFERENCE_2026-10-28.md RN-1) gives

`M_h = ∫E dμ_h(E) ≤ 2 φ_g g_3² Σ_f A_f |φ(x_f)|² ≤ M_φ`, with `φ_g=(1+√5)/2` and finite `M_φ` independent of h and finite surrounding patch, subject to the stated geometric coefficients and support hypotheses. No assumption of mixing or mass gap is involved. The inequality does NOT bound V_h above or below.

## Theorem VC-1 (independently proved: conditional two-point compactness)

Assume for a fixed nonzero φ and a refinement sequence that **both** `0<v≤V_h≤V<∞` and `M_h≤M<∞`. Then:

1. For every E>0, the high-energy tail obeys `μ_h((E,∞))≤M/E`. For `M>0` choose `E*=2M/v`; then `μ_h((0,E*])≥v/2` for all h. (If M=0 and v>0, the assumptions contradict the positive finite-volume excited spectrum.)
2. The measures are tight on `[0,∞)`; after a subsequence `μ_h ⇒ μ` weakly. `v≤μ([0,∞))≤V` and `∫E dμ(E)≤M` by lower semicontinuity. An atom at E=0 can emerge in the limit; this is NOT a positive gap.
3. The connected physical-time correlations `C_h(t)=∫e^(−Et)dμ_h(E)` for t≥0 converge (along the same subsequence) uniformly on compact time intervals to `C(t)=∫e^(−Et)dμ(E)`. They are equi-Lipschitz: `0≤C_h(0)−C_h(t)≤t M_h`, `|C_h(t)−C_h(s)|≤M|t−s|`.
4. By Jensen's inequality applied to each normalized positive spectral measure,

   `C_h(t)≥V_h exp(−t M_h/V_h)≥v exp(−tM/v)` for all t≥0.

   Consequently `C(t)≥v exp(−tM/v)>0` for any finite physical time. This establishes nontrivial finite-energy two-point spectral weight without assuming a gap, once the two-sided interacting variance hypothesis is independently proved.

**Proof:** Markov's inequality on E gives item 1, including the quantitative finite-energy mass. Tightness and the weak compactness theorem for finite positive measures give item 2. The first-moment inequality gives equicontinuity; weak convergence gives pointwise convergence on bounded-continuous Laplace kernels, and a finite grid/Arzelà–Ascoli argument gives locally uniform convergence. Jensen applies to `e^(−tE)`, which is convex as a function of E; `x↦x exp(−tM/x)` is increasing for x>0, giving the final estimate. Nothing here invokes the desired IR decay, an interacting complete frame, or a presumed quantum continuum.

**Multiple sources:** For any fixed finite real linear span of test functions, a uniform upper variance bound and first-moment bound on every linear combination yield subsequential positive semidefinite matrix-valued Laplace two-point kernels by polarization and diagonal compactness. A corresponding all-test-function, distributional and higher-point OS reconstruction requires additional independent uniform/test-function control. A nonzero two-point function is not a non-Gaussian quantum Yang–Mills construction.

**Sharp remaining gate:** the first moment bound is already uniform, but `0<v≤V_h≤V` is NOT established in the interacting magnetic model. Neither spatial mean flatness nor the electric-only Gaussian reference theorem establishes those interacting inequalities.

## Theorem VC-2 (independently proved single-rhombus strong-field example: nonzero equal-time variance can still yield instantaneous physical-time loss)

For one open spatial SU(2) rhombus with four equal electric coefficients a>0 and magnetic coefficient b>0, the *physical* class-function operator is

`H_{a,b}=−a(∂²_θ+2cotθ ∂_θ)+b(1−cosθ)`.

The established exact radial conjugation gives a Dirichlet Schrödinger operator `−a d²/dθ²−a+b(1−cosθ)` on `(0,π)`. Let `ε=(a/b)^(1/4)`, `x=θ/ε`, `ω=1/√2`, and denote its normalized rescaled ground state by u_ε(x). Its rescaled potential `(1−cos εx)/ε²` is sandwiched between `(2/π²)x²` and `x²/2` on the expanding interval. The min–max and confinement argument from the previously checked strong-magnetic one-face theorem yields u_ε→u_0 in L², where u_0(x) is proportional to `x exp(−ω x²/2)` on x>0, and the first physical gap obeys `Δ_{a,b}/√(ab)→2√2`.

The same quadratic lower bound implies **uniform weighted Agmon estimates** for the ground eigenfunctions: choose a fixed R and sufficiently small δ>0; the Agmon identity with weight exp(δ(x−R)_+²), using the uniform bound on their eigenvalues and `W_ε(x)≥(2/π²)x²`, bounds `∫ x^m |u_ε(x)|² dx` uniformly for each fixed m. Accordingly the first four x-moments converge to those of u_0. For the normalized odd Gaussian oscillator ground state,

`E_0[x²]=3/(2ω)=3/√2`, `E_0[x⁴]=15/(4ω²)=15/2`, hence `Var_0(x²/2)=3/(8ω²)=3/4`.

Since `p=cosθ=1−ε²x²/2+O(ε⁴x⁴)` in weighted L², we obtain the **exact strong-magnetic asymptotic**

`lim_{b/a→∞} Var_{Ω_{a,b}}(p)/(a/b)=3/4`.

Moreover the limiting centered source `(p−<p>)/ε²` is the oscillator's x²/2 fluctuation, which couples its ground state exactly to the first *physical* excited Dirichlet oscillator state (not to an unphysical one-quantum vector state). Its rescaled time correlation converges:

`lim_{b/a→∞} C_{(p−<p>)/ε²}(s/√(ab))=(3/4)exp(−2√2 s)` for all fixed s≥0.

At fixed physical t>0, the gap lower bound for sufficiently large b/a instead gives

`0≤C_{(p−<p>)/ε²}(t)≤Var((p−<p>)/ε²)exp(−Δ_{a,b}t)→0`

provided √(ab)→∞.

**Geometric scale caution:** if a=a₀>0 and b=b₀/h² with h→0, then `Y_h=(p−<p>)/h` satisfies

`Var(Y_h)→(3/4)a₀/b₀>0`, while `C_{Y_h}(t)→0` for each t>0 and the physical excitation frequency scales as `2√(2a₀b₀)/h`. The first energy moment diverges like `(3/√2)√(a₀b₀)/h`. Thus this *one-face local normalization* has a nonzero equal-time variance but no continuous nonzero positive-time two-point limit. It **does not** contradict VC-1, because VC-1 requires a uniform first moment; it is also NOT the physical-area smeared Penrose source F_h[φ]. It is an exact caution against replacing the first-moment/temporal-tightness gate by equal-time variance alone.

**Gaussian check:** in the limiting oscillator, the centered x²/2 multiplier applied to u_0 is proportional to the first excited Dirichlet eigenfunction. The gap is `4ω=2√2`, and its spectral weight is its variance 3/4. Thus the limiting rescaled-time correlator contains one exponential as displayed.

## Evidence classification and next task

- **Independently proved:** VC-1 conditional spectral tightness and quantitative positive-time lower bound; VC-2 one-rhombus strong-magnetic field variance, scaling-time and physical-time comparison under the stated coefficients.
- **Source-input assumptions:** exact first-moment F1, physical time normalization, authentic geometry and w_e/b_f coefficients from declared mathematical trajectory; final literal Stage7/26 identity remains a separate audit.
- **Not proved:** either side of a two-sided interacting variance bound for the physically smeared Penrose source F_h[φ], convergence of its finite-dimensional distributions, any nonzero uniform decay threshold, quantum Penrose spatial continuum or four-dimensional Yang–Mills mass gap.

**Recommended next noncircular theorem:** establish a volume- and regulator-uniform *upper bound and strictly positive lower bound on Var_Ω F_h[φ]* for at least one nonzero compactly supported test function, without importing a spectral gap or clustering. In tandem, establish variance covariance bounds for a dense test family. If successful, VC-1 automatically yields nontrivial subsequential reflection-positive two-point spectral data with finite-energy weight. Time decay and higher-point interacting reconstruction remain separate.