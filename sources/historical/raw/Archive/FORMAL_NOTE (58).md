# Cyclic coupled SU(2) pivots: flat-compatibility comparison and cycle-defect obstruction
27 October 2026. Finite-volume nonlinear theorem; arbitrary Penrose-support conclusion remains open.

## Setup
Let A be k selected SU(2) links, v all other links, and P_A all undeleted plaquettes whose holonomy depends on at least one link in A (including spatial and temporal plaquettes). Condition on v under the full Wilson cavity measure. Let S_v(a)=sum_{p in P_A} beta_p d(W_p(a,v)), where d(g)=1-(1/2)Tr g in [0,2], beta_p in [c_-lambda,c_+lambda]. Let m=|P_A| <= Delta k, and face lengths and link incidence be uniformly bounded. Define E(v)=min_{a in SU(2)^k}S_v(a). The conditional normalizing integral is Z_v=int exp(-S_v(a)) da, using product normalized Haar. For chosen P subset P_A and fixed coefficients 0 <= r_p <= r_*, set X(a,v)=sum_{p in P} r_p beta_p d(W_p(a,v)), with X<=r_* S_v.

## Uniform small-ball lower bound
At a global minimizer a_*(v), S_v is a smooth function on compact SU(2)^k, so its directional first derivatives vanish. Bounded face length/incidence gives Hessian operator norm <= C lambda uniformly at all points in product geodesic coordinates (using e.g. simultaneous geodesics of each a_e). Thus, on product balls d_SU2(a_e,a_e^*)<=c/sqrt(lambda), S_v(a)<=E(v)+Ck. The Haar mass of these balls is at least (c_0 lambda^(-3/2))^k for lambda>=2. Thus
Z_v >= exp(-E(v)-Ck)(c_0 lambda^(-3/2))^k.
(One can instead use radius c/lambda and Lipschitz for a weaker exponent 3k.)

Since exp(-S_v+tX)<=1 for 0<t<1/r_*, the conditional exponential moment obeys
E[exp(tX)|v] = (int exp(-S_v+tX) da)/Z_v <= exp(E(v)+Ck) (C lambda^(3/2))^k.
Thus log E[exp(tX)|v] <= E(v)+(3/2)k log(lambda)+Ck.
This bound is uniformly local in k, independent of ambient volume, for every exterior v; it handles arbitrary cyclic face-pivot incidence and any strong Wilson coupling. Its only potentially O(lambda) term is the cycle-compatible minimum E(v).

If all touched plaquettes can be simultaneously flat, i.e. exists a with W_p(a,v)=I for every p in P_A, then E(v)=0. This gives an unconditional-in-v conditional MGF bound <=exp((3/2)k log lambda+Ck). The consequent conditional tail is P(X>=s|v) <=exp(-ts+(3/2)k log lambda+Ck). If this flat extension is available for rho_0-a.e. exterior v, integrating yields identical full Gibbs bound. No private pivots and no acyclic incidence are required. This is a conditional geometric class; its flat-extension hypothesis can fail in interior Penrose regions.

For arbitrary exterior distributions eta(dv), the exact noncircular reduction is
E_rho0 exp(tX) <= (C lambda^(3/2))^k exp(Ck) E_eta exp(E(v)).
This is *not* a uniform theorem when E(v) fluctuates on O(lambda) scale. It is an independent defect moment requirement, not assumed solved. Its geometry is measurable by minimizing the actual conditional local action, without knowing any insertion partition-function ratios.

## Explicit cycle obstruction
Consider two pivot links a,b, and three plaquette words W1=a, W2=b, W3=(ab)^(-1)h, where h is a fixed exterior SU(2) holonomy, with equal coupling lambda. This is an algebraic local cyclic word system, not asserted to be an embedded rhombus-prism without further incidence verification. Simultaneous flatness forces h=I. Let theta(g) in [0,pi] be the SU2 geodesic distance from identity; triangle inequalities give theta(h) <= theta(a)+theta(b)+theta((ab)^(-1)h). Using 1-cos theta >= 2 theta^2/pi^2 and Cauchy-Schwarz, 
S_v(a,b) >= (2 lambda/(3 pi^2)) theta(h)^2.
Taking a=b=I yields S_v <= lambda d(h) <= (lambda/2)theta(h)^2. Thus E(h) is proportional to lambda theta(h)^2 for nonzero h. This illustrates that the defect may be O(lambda) for fixed frustrated exterior and cannot be bounded O(k log lambda) by bounded incidence or cyclic finite rank alone.

## Stronger exact comparison using two minima
Define S_t=S_v-tX and E_t(v)=min_a S_t(a), Z_t=int exp(-S_t)da. For 0<t<1/r_*, S_t is a nonnegative Wilson action with modified positive couplings. The small-ball estimate on S_v and the upper bound Z_t<=exp(-E_t) give
log (Z_t/Z_v) <= E(v)-E_t(v)+(3/2)k log lambda+Ck.
This improves the earlier bound since E_t>=0. It is a strict geometric energy-gap reduction, not a uniform control of the gap. If E(v)-E_t(v)<=C k (1+log lambda) uniformly or has a suitable exponential moment under the exterior law, then the support-local bound follows. Verifying that estimate for arbitrary Penrose cavity exteriors remains open and is closely related to the original relative filling energy problem.

## Important distinctions
- The event is for X (weighted plaquette energy), not directly staple frustration; since sum_{e in J} F_e <= X when P=P(J) and r_p counts incidence, its tails and exponential moments follow by monotonicity.
- The exponent (3/2)k log lambda is sufficient for support-local logarithmic tails but is weaker than coupling-uniform O(k) MGF achieved with triangular Haar-free pivots.
- A merely bounded number of independent cycle relations does not uniformly bound E(v) without control of their exterior holonomies.
- Nothing here proves uniform control of E(v) or E(v)-E_t(v) under arbitrary Penrose cavity Gibbs marginals, the arbitrary thin-support insertion bound, R3/R2, or the continuum Yang--Mills mass gap.
