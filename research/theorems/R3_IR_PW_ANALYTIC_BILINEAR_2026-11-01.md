# Intrinsic Peter–Weyl analytic Hilbert bilinear carré-du-champ bound

**The Singular Boundary | 2026-11-01 | Theorem for finite straight open original-link SU(2) face chains.**

## Definitions
For an interval I of r faces and independent face holonomies, let P_l be the product Haar-orthogonal Peter–Weyl projection to degrees l=(l_i), N(l)=sum l_i, and H_sigma(I) have norm squared Σ_l exp(2sigma N(l))||P_l f||_2². These are intrinsic functions on SU(2)^r, independent of polynomial representatives. Extend functions to the union interval without changing their norm.

## Theorem
For intervals I,J of sizes r_f,r_g, let T=I∪J be a contiguous interval of t faces (touching supports); for sigma'>=0, sigma>sigma', put delta=sigma-sigma'>0 and z=exp(-2delta). Let

F_t(z)=((1+z)/(1-z)^3)^t,
G_t(z)=(1-z)^(-t),
S_{1,t}(z)=(z∂_z)^2 F_t(z),
S_{2,t}(z)=(z∂_z)^2 G_t(z).

Then

**||Gamma(f,g)||_{H_sigma'(T)} <= 48t sqrt(S_{1,t}(z) S_{2,t}(z)) ||f||_{H_sigma(I)} ||g||_{H_sigma(J)}.**

The estimate is uniform in ambient chain length, holds for finite Peter–Weyl sums and extends by density to the indicated analytic Hilbert spaces. If supports are separated by at least one whole face, Gamma(f,g)=0.

## Proof
Each degree-l block on SU(2)^t has dimension ∏(l_i+1)^2, hence the reproducing kernel yields ||h_l||_infinity <= d_l||h_l||_2 with d_l=∏(l_i+1). Every original-link vector field D_{e,a} is a sum of at most two invariant face derivatives and preserves l; its L2 operator norm on that block is at most √(l_i(l_i+2))/2+√(l_j(l_j+2))/2 <= 2N(l) for N(l)>=1 (and kills N=0). For output of the product D_e f_l D_e g_k, the SU(2) Clebsch–Gordan rule in each face ensures total Peter–Weyl degree ≤N(l)+N(k). Therefore

||D_e f_l D_e g_k||_{H_sigma'} <= exp(sigma'(N(l)+N(k))) (2N(l)d_l)(2N(k))||f_l||_2||g_k||_2.

Sum l,k, use Cauchy–Schwarz with the input exp(sigma N) weights, and observe

Σ_l d_l² N(l)² z^{N(l)} = (z∂_z)^2 F_t(z),
Σ_k N(k)² z^{N(k)} = (z∂_z)^2 G_t(z).

At most 4t original links have a nontrivial derivative on the t-face interval, each with three SU(2) directions. Summing them gives the factor 12t*4=48t. An output function is taken on T; the corresponding face extension has identical PW norm. This also handles overlapping support intervals. A more refined but unnecessary estimate can exploit only edges incident to both supports.

## Interpretive limits and compatibility with the free inverse
Previously proved: ||K_T^{-1}h||_{H_sigma'} <= (1/3)||h||_{H_sigma'} for Haar-centered h, with no radius loss, uniformly in T. Haar centering P_0 is an H_sigma' contraction. Hence each local centered nonlinear Poisson solution satisfies

||K_T^{-1}P_0 Gamma(f,g)||_{H_sigma'} <= 16t sqrt(S_{1,t} S_{2,t})||f||_{H_sigma}||g||_{H_sigma}.

But this constant grows exponentially with t at fixed delta, and diverges as delta↓0. In particular, a direct all-order iteration in one fixed analytic radius is **not** justified, and a shrinking-radius scheme must explicitly allocate and sum losses. This theorem alone proves neither ordinary perturbative convergence, the interacting lambda=1 gap, Penrose current, nor a Yang–Mills continuum mass gap.

## Verification
`verify.py` checks exact generating-function coefficients via integer sums for t=1,2,3,4 and n through 8, and Clebsch–Gordan degree support through l,k=20. These checks do not substitute for the all-degree argument above.