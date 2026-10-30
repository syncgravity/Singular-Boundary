# Conditional compatibility-gap tails: a measure audit and exact two-plaquette test

## Setup
Fix w and a set K of k SU(2) links. Let A(u,w)=S_Y(u,w) and B(u,w)=S_Q(u,w)>=0, both sums of bounded-incidence nonnegative Wilson terms with couplings <= c lambda. Put M_A=min_u A and M_{A+B}=min_u(A+B), Gamma(w)=M_{A+B}-M_A >=0, Z_A(w)=int exp(-A)du, Z_{A+B}(w)=int exp(-A-B)du, R(w)=Z_{A+B}/Z_A.

Let nu(dw) denote the marginal produced from the theory with Q *deleted* (i.e. with A but not B); let mu(dw)=R(w)nu(dw)/a denote the marginal when Q is present, a=E_nu R, and F=-log a.

## Deterministic comparison
By small SU(2) balls about minima (bounded Wilson Hessian), with L=k[(3/2)log lambda+C], for lambda>=2:
exp[-Gamma-L] <= R <= exp[-Gamma+L].
Indeed the individual local integrals lie between exp(-M-L) and exp(-M).

## Exact reweighting and upper tails
For any s>=0,
mu{Gamma>= F+L+s} = (1/a) E_nu[R 1_{Gamma>=F+L+s}] <= exp(F+L) exp[-(F+L+s)] = exp(-s).
Equivalently, for 0<=t<=1,
E_mu exp[t Gamma] <= exp(F+L) E_nu exp[-(1-t)Gamma] <= exp(F+L).
Hence E_mu Gamma <= F+L (using the t=1 moment with Jensen), and a direct tail integration gives E_mu Gamma <= F+L+1. The Jensen bound is sharper; note this is a bound in terms of F, not a proof F=O(k log lambda).

## Independent cavity-law check
If the *actual* cavity law already includes Q and Y, it induces mu(dw), not nu(dw). Conflating the two can make a false claim. The relative crossing-face thermal inequality under mu can be supplemented by the preceding reweighting, but the latter still depends on the insertion cost F of adding Q to Y.

## Two-plaquette calculation
Take one adjustable SU2 link u, two faces with independent exterior staples q1,q2, and A=lambda(1-u dot q2), B=lambda(1-u dot q1). Under the Q-deleted law, q1 and q2 are independent Haar (integrating u produces constant q(lambda)). If theta is the angle of q1^{-1}q2, its density is 2/pi sin^2 theta on [0,pi], and
Gamma=2lambda(1-cos(theta/2)).
Consequently E_nu Gamma=2lambda(1-32/(15 pi)), which is of order lambda (32/(15pi) approximately .67906).
With Q present, the theta density is tilted by R(theta)=e^{-lambda} z(2lambda cos(theta/2))/z(lambda). For theta small, Gamma~lambda theta^2/4, while the Haar theta density~(2/pi)theta^2; as lambda grows the tilted law is concentrated on theta=O(lambda^{-1/2}). Consequently E_mu Gamma stays O(1). More precisely dominated convergence after rescaling x=sqrt(lambda) theta shows Gamma tends to a Gamma(shape=3/2, scale=1) law and E_mu Gamma tends to 3/2; the z quotient polynomial prefactor asymptotically cancels at theta=O(lambda^{-1/2}). This is a finite 2-face example, not a theorem for arbitrary Penrose supports.

## Why this does not close the arbitrary-thin-support problem
The exact upper tail is centered at F+L. A uniform O(k log lambda) theorem requires a genuinely independent bound F<=C k log lambda. That is the missing localized deleted-versus-undeleted free-energy comparison. Entropic/variational transformations above do not establish it. The Q-deleted measure can have E_nu Gamma of order lambda, so a direct concentration-of-Gamma approach on that measure is generally impossible. No 3D continuum mass gap is established.
