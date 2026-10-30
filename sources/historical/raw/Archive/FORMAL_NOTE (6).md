# Regionwise Wilson defect bound with an explicit boundary penalty

## Setup
Let G be a finite bounded-incidence SU(2) spacetime lattice. The Wilson Gibbs law is proportional to exp(-sum_p beta_p d_p) times independent normalized Haar link measure, d_p=1-(1/2)Tr W_p in [0,2]. Along the anisotropic trajectory beta_p lies in [c_- lambda,c_+ lambda], lambda=(g_3^2 h)^-1 >= 1. Select a nonempty set X of plaquettes and let L(X) be the set of all its incident links. Set Y(X)={q not in X : boundary q meets L(X)}. Condition on all links outside L(X). Internal link variables are U in SU(2)^{L(X)}. For any selective dilution beta'_p of the couplings with beta'_p in [c'_ - lambda, c_+ lambda] (the lower constant c'_-= (1-vartheta)c_- >0), define A_X(U)=sum_{p in X} d_p(U), and W_Y(U;ext)=sum_{q in Y(X)} beta'_q d_q(U,ext). All other terms are constant in U and cancel. Thus 0 <= W_Y <= 2 c_+ lambda |Y(X)|.

## Theorem (bulk-boundary defect estimate)
For any theta satisfying 0<theta<c'_-, conditionally on every exterior link configuration,

 E_beta'[sum_{p in X}d_p | ext]
 <= [ 2c_+lambda |Y(X)| - log Z_X^0(beta'_X)]/(theta lambda),

where Z_X^0(beta'_X)= int exp(-sum_{p in X}beta'_p d_p(U)) dU_{L(X)}.

There is a uniform constant C depending only on c_+, the Haar metric and number of links per plaquette, such that

 -log Z_X^0(beta'_X) <= C |L(X)| (1+log lambda) + C |X|.

Consequently

 sum_{p in X} E_beta' d_p <= C_theta [ |X| (1+log lambda)/lambda + |Y(X)| ]

since |L(X)| <= 4 |X|. This bound is simultaneous over all ambient volumes, all exterior configurations, all X, and all selective dilutions with the stated lower and upper coupling bounds.

## Proof
Conditional partition functions Z^W(alpha)=integral exp(-sum_X alpha_p d_p - W_Y) dU. Jensen implies

 theta lambda E_beta'[A_X|ext] <= log E_beta'[exp(theta lambda A_X)|ext]
 = log (Z^W(beta'_X-theta lambda)/Z^W(beta'_X)).

The numerator is at most 1, because beta'_p-theta lambda >=0 and W_Y>=0. The denominator is at least exp(-2c_+lambda |Y|) Z_X^0(beta'_X). This proves the first inequality.

To lower bound Z_X^0, restrict each internal SU(2) link to the geodesic ball radius r=lambda^-1/2 around I (or a fixed smaller multiple). Haar probability of each ball >= c r^3 for lambda>=1. Each four-link plaquette then has geodesic angle <=4r, and defect <=8r^2 (valid from 1-cos theta <=theta^2/2). Hence sum_X beta'_p d_p <=8c_+|X| on this event. The event has Haar probability >=(c lambda^-3/2)^{|L|}, giving
 Z_X^0 >= exp(-8c_+|X|) (c lambda^-3/2)^{|L|}.
Substitute above.

## Consequence for filled regular spacetime blocks
Suppose X consists of all plaquettes wholly inside a geometric 3D block of fixed physical diameter L, and its incidence neighborhoods satisfy |Y(X)| <= C_geom (h/L)|X|. Since lambda^-1=g_3^2 h for fixed g_3^2, the theorem gives

 sum_{p in X} E_beta' d_p <= C_{L,g_3^2} |X| (1+log lambda)/lambda

uniformly in the ambient volume, exterior link conditioning and selective dilution. Geometric boundary ratio is an EXPLICIT ASSUMPTION to check for actual Penrose spacetime block families (and may fail for irregular blocks or blocks too thin in time).

## Limitations
This is NOT the universal regionwise inequality for arbitrary connected plaquette sets; for thin X, |Y| can be proportional to |X|, so the bound is O(|X|), not O(|X| log(lambda)/lambda). The conditioning bound is deliberately crude and does not exploit favorable exterior dynamics. Thus it does not yet establish an all-size connected large-field contour inequality or a residual polymer expansion. It also does not prove R3/R2 mass gaps.
