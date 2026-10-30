# Finite SU(2) gauge-covariant canonical inverse-Whitney electric operator

Date 2026-10-30. Scope: specified **finite** connected open-link SU(2) graph with positive assembled Whitney matrix M. This constructs a valid gauge-invariant quantization of a chosen cotangent metric, but does **not** derive that metric uniquely from nonabelian Yang-Mills continuum physics.

On L2(SU(2)^E, product Haar) let X_e^a be left- or right-invariant skew-adjoint link derivative, with the convention chosen so X_e transforms at its nominated endpoint v_e under gauge changes. Choose an oriented edge path gamma_e from v_e to a COMMON root v, and let A_e(U) in SO(3) be the adjoint parallel transporter from v_e to v. Set (D_e psi)^a=sum_b A_e(U)^ab X_e^b psi. For gauge transformations g, and a transformed wavefunction R_g psi(U)=psi(g^-1.U), these derivatives satisfy D_e(R_g psi)(U)=Ad(g_v) R_g(D_e psi)(U), after fixing consistent transporter orientation and the link-invariant derivative convention.

For the assembled SPD M, define K=M^-1 and on smooth cylindrical psi, phi the Hermitian quadratic form t_K[psi,phi]=(g_2^2/2) sum_e,e' K_ee' <D_e psi,D_e' phi>. The coefficients A_e(U) depend smoothly on compact group links, are pointwise orthogonal, and K is fixed real SPD. Hence for every psi,

(g_2^2/(2 lambda_max(M))) sum_e ||X_e psi||² <= t_K[psi] <= (g_2^2/(2 lambda_min(M))) sum_e ||X_e psi||².

This implies equivalence to the standard link Sobolev H1 energy norm; therefore t_K is closable and its closure is a densely defined nonnegative closed form. The Friedrichs operator is H_E=(g_2^2/2) D* (K tensor I_3) D. The formal adjoint D* retains both the configuration-dependent transport derivative and Haar integration-by-parts; do NOT replace it with an unordered product of D_e. Gauge covariance makes t_K invariant and the resulting self-adjoint H_E commute with gauge transformations and preserve the physical Gauss-invariant Hilbert space. For a connected finite graph with product Haar, the only full-link functions annihilated by all X_e are constants. Thus the unique zero mode of the electric-only operator on the physical subspace is the constant wavefunction.

With the normalization -Delta_e chi_(1/2)=3/4 chi_(1/2), standard T=sum_e -Delta_e has first nonzero eigenvalue at least 3/4 (gauge projection may increase it). The form comparison implies the ELECTRIC-ONLY physical gap
gap(H_E) >= 3 g_2^2/(8 lambda_max(M)).
This gap is not the interacting Yang-Mills mass gap. In d=2 uniform geometric scale leaves M unchanged, while the magnetic coefficient may grow as h^-2; the min-max lower bound for the interacting spectral gap loses control.

On the previously assembled 11-face 30-link disk M (double precision) has min eigenvalue about 0.143174148694 and max about 1.104659344162; thus K's spectral range is approximately [0.90525645,6.98450111]. The lower quadratic-form ratio for g_2²=1 is about 0.452628, and the electric-only gap lower bound is about 0.339471. These are floating-point exploratory constants, not rigorous numerical interval enclosures. The symbolic comparison itself is rigorous for every SPD M.

IMPORTANT: the selected Whitney mass matrix comes from eliminating artificial triangulation diagonals by local Schur complements. Choosing covariant paths after taking the inverse is a modeling decision; canonical reduction of an actual nonabelian action with configuration-dependent metric can yield other terms. No unique continuum equivalence, continuum limit, shrinking cap or 3+1-dimensional Yang-Mills mass gap has been proved.
