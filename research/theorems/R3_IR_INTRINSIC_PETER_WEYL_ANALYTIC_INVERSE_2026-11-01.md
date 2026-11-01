# The Singular Boundary — Intrinsic Peter–Weyl analytic electric inverse, all open-chain lengths

**2026-11-01.** Original-link SU(2) free electric operator on finite open straight chains. This theorem completes the analytic-Hilbert inverse bridge for the *free* operator, while providing an explicit obstruction to a fixed-radius analytic bilinear bound. No interacting-gap conclusion is asserted.

## 1. Intrinsic analytic Hilbert scale

Let `H_m=SU(2)^m` with independent normalized product Haar measure. Let `P_l` be the canonical orthogonal Peter–Weyl isotypic projector indexed by multi-degree `l=(l_1,...,l_m)`, `l_i in N_0`. For `sigma >=0` set

`||f||_{sigma,2}^2 = sum_l exp(2 sigma sum_i l_i) ||P_l f||_{L²(H_m)}²`.

This is intrinsic, independent of a choice of matrix-coefficient basis. The mean-zero subspace `H_{sigma,0}` is the orthogonal complement of constants. More general diagonal weights `w(l)>=1` also work for the inverse theorem, as long as they are constant on each Peter–Weyl multi-degree block.

## 2. Exact electric inverse with no loss of analytic radius

The physically oriented free electric `K_m` consists of left and right SU(2) differential actions on individual faces and their shared-link quadratic couplings. Each action preserves the corresponding face's Peter–Weyl degree, hence `[K_m,P_l]=0` for every multi-degree. The all-length original-link spectral theorem (archived separately) proves `spec K_m` on the nonconstant subspace is contained in `[3,infinity)`, and that `3` is attained by a fundamental one-face mode.

Since `K_m` is positive self-adjoint, the direct sum of its block inverses has the same spectrum under any diagonal positive block weight. Thus for **every finite m and sigma>=0**,

`||K_m^{-1}h||_{sigma,2} <= (1/3)||h||_{sigma,2}` for `<h>_Haar=0`.

The operator norm is exactly `1/3`, attained by the degree-one mode embedded at any site. The bound is uniform in m and has *no analytic-radius loss*.

The corresponding gradient/resolvent smoothing inequality is

`||D_m^(1/2) K_m^{-1} h||_{sigma,2} <= 1/sqrt(6) ||h||_{sigma,2}`,

where `D_m=sum_i(-Delta_i)` with fundamental Casimir 3/4. Proof: the established form comparison `K_m>=2D_m` holds blockwise, and therefore on every sigma-weighted direct-sum space. For `v=K_m^{-1}h`, `||D_m^(1/2)v||²_sigma <= (1/2)<v,K_m v>_sigma = (1/2)<K_m^{-1}h,h>_sigma <= (1/6)||h||²_sigma`. This is a weaker but useful derivative-gain statement. It does not assume a constant-coefficient norm bound in the earlier quaternion polynomial representation.

## 3. A fixed-radius nonlinear obstruction

The radius-preserving inverse bound does not close the nonlinear score equation. On one SU(2) face consider Haar-orthonormal characters `chi_n=U_n(Re U)`. They occupy a single Peter–Weyl degree `n`, so `||chi_n||_{sigma,2}=exp(sigma n)`. The exact Clebsch–Gordan formula gives the character `chi_(2n)` coefficient of `Gamma(chi_n,chi_n)` equal to `-n²`. Hence for normalized `f_n=exp(-sigma n)chi_n`:

`||f_n||_{sigma,2}=1`, but `||Gamma(f_n,f_n)||_{sigma,2} >= n²`.

Therefore, for every fixed sigma>=0, **there is no bounded bilinear map** `Gamma:H_sigma x H_sigma -> H_sigma`, already in the one-face class sector. A radius loss, derivative-weighted norm, or a more sophisticated nonlinear iteration is indispensable. This obstruction does not prove actual vacuum-score divergence.

## 4. Verification and persistence

`verify.py` checks exact block spectrum dimensions and the free lower bound for all degree tuples with degrees 0..3 on chains of length 1..5, and verifies the balanced character highest-degree obstruction. The all-length results are analytic deductions from commutation and the all-length spectrum, not extrapolations from these finite cases.

This theorem establishes only a free inverse in an intrinsic analytic Hilbert scale. The bilinear estimate with controlled radius loss, the interacting lambda=1 gap, Penrose signed-current bound and continuum Yang–Mills mass gap remain open.