# R3: compatible-maximizer logarithmic insertion theorem
Date: 2026-10-28

## Status
New rigorous conditional **finite-block** logarithmic insertion theorem. It is **not** verification of the required compatibility hypothesis for the original Penrose cavity, and therefore **not R3 closure**.

## Setup
Let B be m freely integrated SU(2) links in a bounded block. Fix an arbitrary assignment eta of all exterior links. Let C_B be the n cavity Wilson faces depending on B, with oriented words of length at most L (counting occurrences), and couplings 0<=beta_p<=lambda. Let Q be q inserted faces of word length at most L, coupling lambda, each depending on B or the fixed exterior. Write c(H)=Tr(H)/2 and D_C(U;eta)=sum_{p in C_B} beta_p (1-c(H_p)), D_Q(U;eta)=sum_{p in Q}(1-c(H_p)). The conditional block insertion ratio is
R_B(eta)=int exp[-D_C-lambda D_Q]dU / int exp[-D_C]dU.
The block Haar measure is normalized. The constant cavity terms not depending on B cancel.

## Theorem (compatible cavity maximizer)
Assume there exists U_*(eta) in SU(2)^m attaining the global minimum E_*(eta) of D_C(.;eta) and satisfying H_p(U_*;eta)=I for every p in Q. Then for all lambda>=1,

 R_B(eta) >= [h_L lambda^(-3/2)]^m exp[-(n+q)L^2],

where h_L=8/(3 pi^3 L^3), for L>=1. In particular if m<=b q and n<=a q for geometric constants a,b, then

 -log R_B(eta) <= q [b ((3/2)log(lambda)+log(1/h_L)) + (a+1)L^2].

This bound is uniform in the exterior assignment eta **subject to the compatible-maximizer hypothesis**. The L^2 constant is deliberately conservative.

## Proof
Use bi-invariant SU(2) geodesic coordinates U_e(t)=U_{*,e} exp(t X_e) for each block edge, with |X_e|<=epsilon=1/(L sqrt(lambda)). Haar measure of the product of m geodesic epsilon-balls centered at U_* is at least [h_L lambda^-3/2]^m.

For an oriented face word H_p(t), the path of each factor has geodesic speed <=epsilon, so ||H'_p|| (quaternion/2x2 operator norm) <=L epsilon. Differentiating a product of exponentials twice gives ||H''_p||<=L^2 epsilon^2. Therefore |(d²/dt²)c(H_p(t))|<=L² epsilon². Since U_* is an unconstrained smooth global minimum of D_C on SU(2)^m, (d/dt)D_C(U(t))|_{0}=0. Taylor's theorem yields
 D_C(U(1)) <= E_* + (1/2) lambda n L² epsilon² = E_*+n/2.
For each inserted p, H_p(0)=I. Its total path length is <=L epsilon, hence 1-c(H_p(1))<= (L epsilon)²/2, and lambda D_Q(U(1))<=q/2. Consequently the numerator is >= [h_L lambda^-3/2]^m exp(-E_*-(n+q)/2). The denominator is <=exp(-E_*), yielding the stronger bound with exp[-(n+q)/2]. The displayed weaker exp[-(n+q)L²] also follows for L>=1.

Importantly, although not all cavity plaquettes need be individually flat at U_*, first-order variation of the **total** cavity energy vanishes at its global minimizer. This is what avoids an O(lambda) penalty.

## Gibbs-averaged extension
Let eta be the exterior block variables distributed according to their actual cavity Gibbs marginal. By disintegration, R_Q=E_{eta~mu_C}[R_B(eta)]. Let G be the set of exterior data admitting a compatible cavity maximizer as above. If mu_C(G)>=exp(-a0 q)(1+lambda)^(-b0 q), then
 R_Q>=exp[-a0 q-(n+q)/2] (1+lambda)^(-b0 q) [h_L lambda^-3/2]^m.
For m<=b q,n<=a q, this proves an ambient-volume-uniform O(q(1+log(lambda))) insertion bound. The Gibbs marginal, not Haar or independent boundary data, appears here.

## Critical limitation and sharp toy contrast
The good set G may be empty, or its Gibbs mass may decay exponentially in lambda. For a one-link cavity with D_C=lambda(1-c(U)), an **aligned** insertion w_lambda(U) has its cavity minimizer U=I compatible and obeys the theorem. For an **antialigned** insertion w_lambda(-U), the cavity minimizer is incompatible and the ratio is asymptotic to sqrt(pi/2) lambda^(3/2) exp(-2lambda). Thus neither bounded incidence nor Gibbs averaging alone implies a polynomial bound.

## Missing target-specific verification
The supplied Penrose catalogue has path/cycle arrays but does not identify the oriented 3-step 12-prism spacetime face words, cavity/insertion face partition, exterior vs integrated links or boundary conventions. There is no supported claim that G has positive measure, let alone polynomial Gibbs probability, for the actual R3 Penrose cavity. To make this theorem applicable, reconstruct those inputs and show either (i) G has a polynomial Gibbs mass, or (ii) a relaxed quantitative version: a cavity near-maximizer with Q deficit O(q/lambda) and cavity energy excess O(q), with a polynomially probable exterior set. The latter would admit the same ball argument after controlling first derivatives or using a true nearby minimum.

## Consequence for mass gap
Theorem concerns finite-volume ratios only; by itself it does not prove spectral transfer estimates, infinite-volume gap, existence of a 4D continuum Yang-Mills model, or the Clay mass-gap conjecture.
