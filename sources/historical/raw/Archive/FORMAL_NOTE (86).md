# R3: Exact support-local Wilson insertion for an exceptional time interval
Date: 2026-10-27

## Scope and geometry
Take a finite connected spatial graph (for the concrete incidence example, the four-quadrilateral disk in `../R3_three_four_step_transfer_2026_10_27/incidence_3step.npz`) periodically extruded through n>=2 Euclidean time intervals. Spatial face Wilson weights are identical at every temporal slice. Normalized temporal Wilson transfers on n-1 steps are identical K. The exceptional interval has K_Q obtained by switching on Wilson face interactions on an arbitrary set Q of otherwise absent spatial-edge temporal faces; all unchanged temporal couplings are identical to those in K. The exceptional step may have any irregular selection of edges, including faces sharing spatial vertices and links.

## SU2 Wilson character spectral positivity
Set d(g)=1-Tr(g)/2, q(t)=int_SU2 exp(-t d(g))dg=e^-t 2 I_1(t)/t. The normalized central kernel k_t(g)=exp(-t d(g))/q(t) has representation-j convolution eigenvalue I_{2j+1}(t)/I_1(t) >=0 (j=0,1/2,...); for t=0 the kernel is constant, convolution P is projection onto constants. For t>=0, k_t convolution T_t >= P (as selfadjoint operators) and T_t>=0. For a tensor product of spatial-edge link coordinates, with unchanged factors positive, the insertion yields K_Q-K>=0 by telescoping tensor products. Restriction/compression to the physical gauge-invariant Hilbert space preserves positive-semidefinite order. These facts are Wilson-specific and do not follow from mere nonnegativity of integral kernels.

## Theorem
Let f>0 be the common spatial Wilson multiplier and write F=M_f (bounded strictly positive for finite couplings), A=F^{1/2} K F^{1/2}, B=F^{1/2} K_Q F^{1/2}. Then B>=A>=0. For a periodic n-step time system with all unchanged steps K, replacing exactly one step by K_Q gives

 Z_Q/Z_0 = [prod_{p in Q}q(gamma_p)] Tr(A^{n-1}B)/Tr(A^n).

Since Tr(A^{n-1}(B-A))=Tr(A^{(n-1)/2}(B-A)A^{(n-1)/2})>=0, we obtain

 0 <= F_Q=-log(Z_Q/Z_0) <= sum_{p in Q}[-log q(gamma_p)].

This holds n>=2, any positive couplings, arbitrary size of spatial graph, support size independent constants. When gamma_p in [c_-lambda,c_+lambda], lambda>=1, F_Q <= (3/2)|Q|log lambda + C(c_-,c_+)|Q|. In particular n=3 with Q confined to one exceptional temporal interval is a genuinely nonuniform time selection.

The combined Gibbs variational identity E_nu V_Q+D(nu||mu0)=F_Q bounds each nonnegative term by the same logarithmic quantity.

## Why it does not solve arbitrary temporal patterns
With two or three different changed intervals, Z includes Tr(A1 A2 A3) where replacing one factor produces Tr(Delta A1 A2 A3). A2 A3 need not be Hermitian or PSD. No Loewner comparison follows. The theorem DOES NOT cover two independently selected nonidentical step supports, arbitrary time-varying spatial Wilson couplings, mixed spatial face insertions, or arbitrary 3D Penrose cavities. It does not establish the nonuniform arbitrary-three-step theorem the long-term problem seeks.

## Notes on periodic temporal gauge
For periodic time, not all temporal links can simultaneously be gauge-fixed to I globally. The transfer-operator formulation integrates the residual temporal holonomies and correctly implements gauge projection; no complete periodic temporal gauge fixing is assumed.
