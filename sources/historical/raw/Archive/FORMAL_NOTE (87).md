# R3: two independent temporal insertions at three steps — exact central SU(2) sector theorem and remaining four-prism gap
Date: 2026-10-27

## Main conclusion and limitation
On the SU(2) *class-function Hilbert space* of one compact holonomy, arbitrary and independently chosen temporal Wilson couplings at different periodic intervals admit a support-logarithmic insertion comparison, even with a nonconstant spatial Wilson multiplier. This includes two nonidentical Wilson insertions in two of three temporal intervals. It DOES NOT establish the same inequality for the full four-prism spatial Wilson Hilbert space or the original Penrose problem: the general spatial plaquette multiplication operator need not be entrywise nonnegative in a single common representation basis, and the full problem has noncentral multiport intertwiners.

## Detailed theorem
Let H=L^2_class(SU(2),dg) with orthonormal basis {chi_j}, j=0,1/2,... . Let f(g)=sum_l a_l chi_l(g) be a strictly positive central multiplication function with absolutely summable weighted character coefficients a_l >=0. The SU(2) Wilson spatial factor f=w_kappa is an example: a_l=(2l+1) 2exp(-kappa) I_{2l+1}(kappa)/kappa >=0. Let K_t be convolution by the normalized Wilson kernel k_t(g)=w_t(g)/q(t), q(t)=exp(-t)2I_1(t)/t, with eigenvalues k_j(t)=I_{2j+1}(t)/I_1(t)>=0. For t=0, k_0(0)=1, k_j(0)=0 for j>0. The matrix of F=M_f in the character basis is
F_{jk}=int f chi_j chi_k dg = sum_l a_l N_{jk}^l >=0,
where N_{jk}^l are SU(2) Clebsch-Gordan multiplicities (0 or 1).

For n periodic time steps, common spatial multiplier F, and any set S of originally absent temporal steps switched on with independent couplings gamma_s>=0, define the normalized trace
T(t_1,...,t_n)=Tr(F K_{t_1} F K_{t_2} ... F K_{t_n}).
Every trace term in character basis is nonnegative:
T=sum_{j_1,...,j_n} F_{j_1 j_2} k_{j_2}(t_1) F_{j_2 j_3} k_{j_3}(t_2) ... F_{j_n j_1} k_{j_1}(t_n).
Switching t_s=0 to gamma_s>=0 only adds nonnegative terms (every diagonal multiplier at j=0 is 1 and higher spins increase from 0). Thus T_new>=T_old>0 and restoring Wilson q gives
Z_new/Z_old >= product_{s in S}q(gamma_s),
0<=F_insert<=sum_s[-log q(gamma_s)].
There is no requirement that different inserted steps have equal couplings. This proof works for all n, not just three. The trace-class justification follows since K_t is trace class for finite t, f bounded and positive; zero-coupling K_0 rank 1. If all t_s>0, finite couplings still give trace-class.

## Independent two-defect test
Take n=3, one central SU(2) holonomy, spatial f=w_kappa and baseline temporal (0,0,t3), then inserted (gamma1,gamma2,t3), with gamma1 != gamma2 and both on the same holonomy channel. Concrete values kappa=2,gamma1=3,gamma2=5,t3=1.2 give normalized trace ratio 3.3126683877910112 by a 36-character cutoff (convergence shown for N=8,12,20,36 in certificate.json). This is a genuine noncommuting operator problem because multiplication F and the K_t do not commute, but it is only a central-holonomy reduction, not the full spatial prism gauge system.

## Why abstract Loewner positivity is insufficient
Write A=F^1/2 K F^1/2, X=F^1/2 Delta K_1 F^1/2>=0, Y=F^1/2 Delta K_2 F^1/2>=0. With two changed intervals in a 3-step system,
Tr[(A+X)(A+Y)A]-Tr A^3=Tr(X A^2)+Tr(Y A^2)+Tr(X Y A).
The last mixed term need not be nonnegative for arbitrary PSD operators. Explicit 2x2 example:
A=diag(1,0.1), v=(1,1), w=(1,-2), X=vv^T, Y=ww^T: Tr(X Y A)=-0.8. For B=A+5X, C=A+5Y, Tr(B C A)=-8.749 while Tr A^3=1.001. This shows an arbitrary positive-operator proof cannot work; this example does NOT represent a Wilson transfer operator and the negative trace is inconsistent with its positive integral kernels.

## Exact hypothesis to test next on the four-prism model
Find a common orthonormal (possibly spin-network) basis for the gauge-invariant spatial Hilbert space such that all temporal transfer multipliers and the spatial Wilson multiplication operator have nonnegative matrix coefficients, OR prove a weaker positivity of the cyclic traces needed for two independent insertions. The four-prism gauge-fixed Fourier block obstruction indicates this is nontrivial. If neither holds, quantify a bound on the negative mixed trace via spatial Gibbs concentration, without assuming the desired insertion estimate.

## Scope
Not proven: O(|Q| log lambda) for two unequal supports on the actual interacting four-prism gauge Hilbert space, arbitrary three-dimensional Penrose supports, uniform large-lambda negative spin-network correction, continuum mass gap.
