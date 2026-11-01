# Intrinsic Peter–Weyl analytic Hilbert inverse for finite open SU(2) plaquette chains

**November 1, 2026 — The Singular Boundary.** Original-link positive free electric operator on a straight open chain of `m` SU(2) face holonomies, normalized so the one-face fundamental degree-one Casimir is 3. This result concerns the **free** operator, not the interacting `lambda=1` Hamiltonian.

## Analytic Hilbert scale

Let `P_l` be the mutually orthogonal product Peter–Weyl projection onto the tensor product of face representation spaces with degree multi-index `l=(l_1,...,l_m)`, `l_i` nonnegative integers. Define `N(l)=Σ_i l_i` and for `sigma>=0`:

`||f||_(H_sigma)^2 = Σ_l exp(2 sigma N(l)) ||P_l f||_(L²(product Haar))²`.

This definition is **intrinsic** to the group and independent of polynomial representatives modulo unit-quaternion constraints. The constant sector has l=0. One may equivalently view the analytic weight as `exp(sigma N)`, where `N=Σ_i (2 sqrt(C_i+1/4)-1)` by spectral functional calculus for face Casimirs `C_i=-Δ_i`; indeed `C_i` has eigenvalue `l_i(l_i+2)/4`.

## Exact theorem

The physical original-link positive electric operator is `K_m=4 Σ_i C_i + 2 Σ_{i=1}^{m-1} Σ_a R_i^a L_{i+1}^a`. Every right or left invariant generator preserves its own fixed Peter–Weyl degree, as does K_m. Thus `[K_m,P_l]=0`, and K_m strongly commutes with the weight `exp(sigma N)`. Its exact all-length free spectral gap is 3, as proved in the preceding exact Peter–Weyl spectrum theorem. Consequently for every finite m and `sigma>=0`, on the product-Haar mean-zero subspace,

**`||K_m^{-1}h||_(H_sigma) <= (1/3)||h||_(H_sigma)`**.

The operator norm is **exactly** 1/3: a degree-one matrix coefficient on a single face is an eigenfunction of K_m with eigenvalue 3, and the analytic weighting cancels in the ratio. No loss of sigma is required. Equivalently, the spectral contraction semigroup `exp(-tK_m)` has mean-zero norm at most `exp(-3t)` in every H_sigma, and its time integral gives the inverse bound.

This result remains uniform in the number of faces m and holds for every function with finite H_sigma norm and zero Haar mean; it is not restricted to low polynomial degrees or any particular coefficient basis.

## Crucial limitations

The intrinsic analytic Hilbert scale is **not** a Banach algebra with a chain-length-independent multiplication norm in the form proved here. The earlier coordinate coefficient-ℓ¹ bilinear gradient theorem cannot be inserted directly into the present H_sigma inverse theorem: the norms are different. Before concluding analytic convergence of the connected perturbative score, one must prove a suitable bilinear carré-du-champ bound within H_sigma (possibly with controlled radius loss and local rooted-interval aggregation). Such a bound is not established here. No interacting gap at coupling 1, signed-current estimate, or continuum Yang–Mills mass gap is claimed.

## Verification

`verify.py` uses exact rational Clebsch–Gordan block eigenvalues and multiplicities on 1,364 degree tuples for chains of lengths 1 through 5. It checks compatibility with previously audited (2,2) and (3,3) sectors. The theorem for arbitrary degrees and lengths is analytic, following from commutation of K with each degree projection and its exact spectral gap; the finite checks are regression tests only.