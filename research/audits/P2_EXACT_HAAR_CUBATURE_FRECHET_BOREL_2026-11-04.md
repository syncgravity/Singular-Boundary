# P2: exact SU(2) gauge-twirl cubature and Fréchet-entire local Borel equation

**Research date 2026-11-04.** Model: corrected original-link SU(2) generator expressed on independent face holonomies on a finite open straight square strip, and its *formal* infinite-row history-family limit. **Two proved technical advances** (exact finite Haar cubature with a uniform inverse approximation; entire continuation of the real formal-score Borel–Volterra equation in the weak local-history topology). Neither settles the N≈m² physical Schatten response, anchored-norm Borel summability, an interacting vacuum, OS reconstruction or a continuum Yang–Mills mass gap.

The full expanded derivation, two independent runnable checks, execution logs and SHA-256 manifest are supplied in conversation archive **p2_exact_haar_cubature_frechet_borel_2026-11-04.zip**.

## 1. Finite exact Haar cubature with polynomial node count

For any face multidegree **n**, total degree S=Σ n_i, and arbitrary complex matrix X on V_n=⊗ V_{n_i/2}, define the residual-Gauss twirl T_n(X)=∫ π_n(g)Xπ_n(g)† dg. Write g=[[z,w],[-conj(w),conj(z)]], z=√t exp(iφ), w=√(1−t)exp(iψ). Haar variables t∈[0,1], φ,ψ∈[0,2π) are independent uniform. Take M=2S+1 evenly spaced phases in each angle and Q=ceil((S+1)/2) Gauss–Legendre nodes t_a with normalized weights ω_a. Then **exactly**, for every X,
\[
\boxed{\mathcal T_{\bf n}(X)=\sum_{a=1}^{Q}\sum_{b,c=0}^{M-1}\frac{\omega_a}{M^2}\,
\pi_{\bf n}(g_{abc})X\pi_{\bf n}(g_{abc})^\dagger.}
\]
Every π_n(g) entry is a degree-n polynomial in the fundamental SU(2) entries. Hence the integrand has total polynomial degree ≤2S. The angular frequency cutoff is ≤2S, so M-root averages kill every nonzero frequency. The surviving terms become radial polynomials in t of degree ≤S, integrated exactly by Q-node Gauss–Legendre. Total number of quadrature product terms Q(2S+1)²=O(S³). For the alternating rank-one outer balanced intertwiner X=|v><w|, every summand is a tensor product of rank-one local operators. This makes the **Gauss twirl** scalable as a structured tensor representation; it is **not** a polynomial-time trace-norm solver for the final physical response.

**Equivariance:** with actual corrected original-link K=4Σ C_i+2Σ D_{i,i+1}, global Haar centering Q0 and B=K^{-1}Q0Γ_K, if G is separately invariant then
\[
\boxed{\mathcal B(\mathcal T F,G)=\mathcal T\mathcal B(F,G).}
\]
The identity holds because K, Q0, Γ and its inverse commute with simultaneous SU(2) conjugation. It permits full physical Poisson response to be calculated on untwirled rank-one inputs and projected afterward using the *exact* finite quadrature; it does not drop shared original-link coupling.

**Uniform certified inverse:** on a nonconstant output sector of total Casimir D=Σ c_i(c_i+2)>0, the actual trace-class shared-link superoperator gives K=D Id+H, ||H||_{S1→S1}≤D/2. Its q-term truncation satisfies
\[
\boxed{\left\|(K^{-1}-D^{-1}\sum_{p=0}^{q}(-H/D)^p)Y\right\|_1\le 2^{-q}\|Y\|_1/D.}
\]
Both exact twirl and each local H application preserve tensor-product decomposability as sums of tensor terms. This yields a non-dense, error-certified *representation* of physical Fourier output blocks. The remaining decisive gate is **trace-norm extraction** and N≈m² asymptotics for the full sum of gauge-invariant insertion sites.

## 2. Entire Borel–Volterra solution in the product topology of local histories

Let I range over the countable finite connected intervals in the bilateral infinite row. Put
\[
\mathscr F_{\rm loc}=\prod_I P_\sigma^{(1)}(SU(2)^I),\quad
p_\Lambda(F)=\sum_{I\subseteq\Lambda}P_\sigma^{(1)}(f_I),
\]
where Λ is any finite connected window. This is a complete metrizable locally convex **Fréchet** product space. It is weaker than the globally anchored Banach norm with supremum over all sites.

By P-31, formal source-score coefficients on fixed histories are exactly stable under increasing finite-volume windows. By P-33, the actual Borel series of every fixed-history component is **entire**, with finite-length exponential-type upper bound O(|I|²). Consequently \(\widehat S_\infty:\mathbb C\to\mathscr F_{\rm loc}\) is **Fréchet-entire** (on each finite window, a finite tuple of Banach-entire functions). The history-labelled B operation is continuous in this product topology: output history I can be formed only by pairs of histories J,K contained in I, a finite collection.

The actual Borel–Volterra equation, previously certified on the small anchored-norm disk, therefore extends **componentwise by the Banach-valued identity theorem to every complex ξ**:
\[
\boxed{\widehat S_\infty(\xi)=\xi A_\infty+
\frac{d}{d\xi}\int_0^\xi
\mathcal B_{\rm hist}(\widehat S_\infty(\eta),\widehat S_\infty(\xi-\eta))\,d\eta
\quad\text{in }\mathscr F_{\rm loc}\text{ for all }\xi\in\mathbb C.}
\]
The derivative is required by the factorial Borel convention. Formal coefficient recursion gives uniqueness among product-topology entire solutions with zero constant term and this source.

On each **fixed** window of length L, the finite history Catalan theorem gives absolute Borel–Laplace reconstruction for 0<λ<ρ_L=3 exp(−σ)/[16L(2+6L)]. These reconstructed local components are compatible on overlapping common λ-domains by coefficient stabilization and uniqueness. **No positive λ-domain is uniform in L**, and neither (weak-topology) global entire continuation nor finite-window Laplace reconstruction establishes the *global anchored-norm* positive-ray growth required for Borel summability of a physical infinite-volume vacuum. No interacting λ=1 gap or 4D continuum result follows.

## Independent execution

The accompanying complete checked archive includes:
- verify_exact_haar_cubature.py: explicit original-link Gauss twirl by Hopf cubature at even widths N=2,4,6, reproducing all singular values of P-32; direct physical K–twirl equivariance checks for N=2,4; mixed-irrep degree-(1,2) twirl against separately oversampled quadrature.
- verify_resolvent_and_frechet.py: actual random complex fixed-sector physical K inverse residual and uniform Neumann truncation tail checks on degrees (1,1), (1,2,1), (1,3,1,1); **1,156 exact-rational** Borel–Volterra derivative/convolution identities.
- Execution logs, SHA256SUMS.txt and integrity-tested ZIP.

These are implementation regressions, not exhaustive certification of arbitrary widths. The all-degree cubature, inverse tail, and Fréchet identity are proved analytically above.

**Next proof gate:** compute the *Schatten nuclear norm* of the structured corrected physical response after cubature/resolvent, for N=m²+O(1), with either an asymptotic lower bound (physical same-grade obstruction) or a uniform upper bound; separately seek strong globally anchored positive-ray control or physical reconstruction beyond the weak product topology.