# R3-IR-422 — Direct center-even cap Fourier certificate and Haar benchmark

2026-10-30. Exact SU(2) harmonic analysis applied to the actual deleted-face Wilson vacuum on the free-boundary disk. This supplies finite-moment sufficient certificates, NOT a uniform completed-cage inequality.

## Audit of R3-IR-421
The Haar target distribution has spin-one moment c_1=0 and identity cap mass exactly the Haar cap mass. Thus the desired F_k >= a_0/2 is already true for Haar, while R3-IR-421's near-maximal condition 3-c_1 <= O(a^2) fails as a->0. The condition is a valid sufficient but unnecessarily strong route and must NOT be treated as the intended physical scaling hypothesis.

## Exact cap-sensitive expansion
Let k be a nonnegative smooth central SU(2) target-cap multiplier, a_0=int k dU>0, and F_k=<k(W_f)> in the original-link physical vacuum. By R3-IR-420 the target distribution is center symmetric. Therefore k may be replaced by k_even(U)=(k(U)+k(-U))/2. Expand k_even in the integer-spin characters: k_even=sum_{j=0}^infinity a_j chi_j in L2(class Haar), with a_j=int k_even chi_j dU=int k chi_j dU and chi_0=1. For smooth k the series converges absolutely uniformly. Define c_j=<chi_j(W_f)> in the true physical vacuum, c_0=1. Then exactly

F_k=a_0+sum_{j=1}^infinity a_j c_j.  (CF-1)

Every integer-spin moment is gauge invariant, and no half-integer moments enter. At any incomplete cage all c_j with j>=1 vanish by a magnetically private target edge, recovering F_k=a_0 exactly.

## Certified finite-character sufficient inequality
For a positive integer J, set the directly measurable partial deviation S_J=sum_{j=1}^J a_j c_j and remainder R_J=sum_{j>J} a_j c_j. Since |chi_j(U)|<=2j+1 everywhere, |c_j|<=2j+1. For any integer r>=2 and smooth central k with L2 SU(2) Laplacian derivative finite, the Laplacian eigenvalue in this normalization is lambda_j=j(j+1), and character orthonormality gives |a_j|<=||(-Delta)^r k_even||_2/lambda_j^r. Hence

|R_J| <= B_{J,r}:=||(-Delta)^r k_even||_2 sum_{j=J+1}^infinity (2j+1)/[j(j+1)]^r.  (CF-2)

In particular,
F_k >= a_0 + S_J-B_{J,r},
so a sufficient condition for the desired half-Haar target expectation is

S_J-B_{J,r}>=-a_0/2.  (CF-3)

This condition preserves the Haar benchmark exactly in its moment component S_J=0 (and its bound can be loosened or improved by knowing the state). It does NOT demand c_1 near 3, and it is cap-sensitive by including all integer-spin sectors with certified tail control.

The derivative norm in B_{J,r} grows for increasingly narrow cap kernels, potentially demanding a large cutoff J as a~sqrt(h); no regulator-uniform bound on the physical c_j or economical cutoff is claimed. For a discontinuous indicator replace k by a smooth nonnegative multiplier k<=nu 1_B, as in the project's original cap-observable setup; the above then certifies F_k, which gives cap probability >=F_k/nu.

The inequality is conservative and sufficient, not necessary. No completed-cage Wilson values of c_j have been calculated here. Full-coupling half-Haar cap survival, the infrared spectral gate, and the continuum Yang-Mills mass gap remain OPEN.
