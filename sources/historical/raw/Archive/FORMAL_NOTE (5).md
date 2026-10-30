# Selectively diluted Wilson couplings: uniform average, extensive contours, and the local gap

## Setting
Finite SU(2) 2+1D spacetime cell complexes, normalized Haar link measures, bounded plaquette length and bounded link/plaquette ratio N_L/N_P ≤ R. Couplings beta_p=lambda c_p with c_-≤c_p≤c_+, lambda≥1. Fix 0<theta<1. For arbitrary X⊂P and 0≤s≤theta beta_min, beta_p^(s)=beta_p-s 1_X(p). Hence lambda(1-theta)c_-≤beta_p^(s)≤lambda c_+.

## Theorem 1 (selectively diluted global defect control)
There exists C_theta depending only on R,c_-,c_+,theta, and local plaquette geometry such that uniformly over finite complexes, X and s,
 (1/N_P) sum_p <d_p>_{beta^(s)} ≤ C_theta (1+log lambda)/lambda.
Proof: fix X,s and c'_p=beta_p^(s)/lambda. Let Q=sum_p c'_p d_p and F(u)=-log ∫exp(-uQ)dHaar. F(0)=0, F''=-Var(Q)≤0, so E_lambda Q=F'(lambda)≤F(lambda)/lambda. Restrict link variables to balls of group radius c/sqrt(lambda); each Haar ball has measure ≥c0 lambda^-3/2 for lambda≥1; each plaquette with at most 4 links has d_p ≤ C/lambda; so Z(lambda)≥[c0 lambda^-3/2]^{N_L} exp(-C c_+N_P). Thus F(lambda)≤(3/2)N_L log lambda + C N_L+C c_+N_P. Divide by lambda c'_- N_P. QED.

## Theorem 2 (extensive contour estimate)
For L_X(delta)={d_p>delta for every p∈X} and any 0≤t≤theta beta_min,
 P_beta(L_X(delta)) ≤ exp[-t delta |X| + t C_theta N_P (1+log lambda)/lambda].
Proof: Markov and partition identity:
 P_beta(L_X)≤exp(-t delta |X|) Z(beta-t1_X)/Z(beta),
 log ratio=∫_0^t sum_{p∈X} <d_p>_{beta-s1_X} ds≤ t C_theta N_P(1+log lambda)/lambda.
In particular when |X|≥(2 C_theta/delta)N_P(1+log lambda)/lambda, probability≤exp(-t delta |X|/2). For delta=lambda^-1/2, t=theta c_-lambda this is exp[-(theta c_-/2) sqrt(lambda)|X|] for sets with |X|≥2 C_theta N_P(1+log lambda)/sqrt(lambda). This is a threshold proportional to N_P, not a rooted-polymer Peierls estimate.

## Limitation
Theorem 1 does not control individual d_p nor sum_{p∈X}d_p proportional to |X|, so cannot provide a full connected contour bound. Arbitrary exterior-link conditioning is problematic because temporal staples can favor incompatible holonomies; an unconditional local estimate remains possible but requires an additional genuinely local comparison inequality. The continuum mass gap, uniform R3/R2 and residual polymer convergence are not proved.

## Proposed independent target
Find C independent of X,p,s,volume,lambda such that <d_p>_{beta-s1_X}≤C(1+log lambda)/lambda. A weaker regionwise target ∑_{p∈X}<d_p>_{beta-s1_X} ≤ C |X|(1+log lambda)/lambda would already imply uniform connected-set suppression via the partition-function identity. Such a bound cannot be inferred from the global averaged theorem alone.
