# R3: Three and four temporal steps; a time-homogeneous insertion theorem
Date: 2026-10-27

## Verified incidence
Take the nine-vertex, twelve-edge, four-quadrilateral spatial disk from the previously constructed four-prism model. Its cellular product with the n-edge periodic time circle has (9n,21n,16n,4n) cells of dimensions 0,1,2,3; 4n spatial faces and 12n temporal faces. For n=3,4, `verify.py` constructs the signed integer boundary matrices, checks d1 d2 = d2 d3 = 0, and computes ranks modulo 1,000,003. Ranks are (9n-1,12n,4n). These complexes are combinatorial, NOT provenance-certified Penrose extractions.

## Exact theorem: repeated temporal insertion for arbitrary n>=2
Let X=SU(2)^12, H=L²(X)^G the gauge-invariant spatial Hilbert space. Let F be multiplication by the same strictly positive spatial Wilson weight f on each temporal slice. Let K_old be the normalized positive temporal transfer operator for a fixed set of pre-existing temporal edge weights, the SAME on each of n time steps. Let K_new add an identical subset E* of positive Wilson temporal weights gamma_e at EVERY step (same spatial edges, same couplings each step). Each normalized SU2 one-link convolution K_gamma satisfies K_gamma >= P_const=K_0, because eigenvalues in spin-j sectors are I_{2j+1}(gamma)/I_1(gamma)>0. Tensor products then give K_new>=K_old >=0 when adding new interactions on absent temporal faces.

Set A_old=F^(1/2) K_old F^(1/2), A_new=F^(1/2) K_new F^(1/2). These are positive trace-class operators and A_new>=A_old. Min-max eigenvalue monotonicity for compact positive operators implies Tr(A_new^n) >= Tr(A_old^n), every integer n>=1. The exact periodic time Wilson partition functions obey Z_new/Z_old = [prod_{e in E*} q(gamma_e)]^n Tr(A_new^n)/Tr(A_old^n). Thus

  0 <= log(Z_old/Z_new) <= n sum_{e in E*} [-log q(gamma_e)]

where q(gamma)=e^{-gamma} 2 I_1(gamma)/gamma. In particular for equal gamma=lambda>=1 and m edges inserted per step: F_Q<= (3/2) nm log lambda+O(nm). The theorem holds on any finite spatial graph (including actual Penrose spatial patches if the needed temporal product and time-independent reflection-positive action are specified), with no dependence on its size; only temporal face insertions repeated at every step are covered. Gauge projection commutes with F and K and the comparison holds on physical H.

## Distinction from arbitrary temporal supports
For n=2 the exact comparison allows K_1 and K_2 to change separately because Tr(F DeltaK_1 F K_2)>=0. At n=3 the analogous would require F K_2 F K_3 F PSD, which need not hold. `verify.py` provides a strict 3x3 real-symmetric PSD F and commuting nonnegative diagonal K2,K3, and diagonal PSD DeltaK1, for which Tr(F DeltaK1 F K2 F K3)=-0.0003173589 <0. This is an abstract finite-dimensional obstruction to the naive Loewner-order proof; the chosen diagonal eigenvalues are NOT certified Bessel ratios of actual SU2 Wilson kernels and F is not known to be a lattice spatial-Wilson multiplication operator. Hence it is NOT a counterexample to the desired Wilson inequality.

For n=4 and n>4 the arbitrary-step problem is likewise not resolved by the single-step Loewner argument. Special reflection-symmetric factorization can give nonnegative traces but does not automatically imply coordinatewise monotonicity for all changes. Under full time-translation invariance the trace-of-powers proof applies to all n, including n=3,4.

## Scope
Nonperturbative, all positive couplings, time-periodic, one common spatial Wilson weight, identical old and added temporal interactions each slice. No result for arbitrary thin support across time, arbitrary time-dependent couplings, spatial-face insertions, general 3D Penrose cavities, or continuum mass gap. No cosmological equilibration assumption is made.
