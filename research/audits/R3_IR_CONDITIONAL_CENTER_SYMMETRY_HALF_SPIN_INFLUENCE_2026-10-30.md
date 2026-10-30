# R3-IR-450 — Global center symmetry does not eliminate conditional half-integer cap influence

2026-10-30. Exact SU(2) probability counterexample and scope correction to R3-IR-420/422 and 447-449. NOT an example claimed to arise as the physical Wilson vacuum.

Let x,y in SU(2), p(U)=Tr(U)/2, and normalized Haar measure dxdy. For 0<epsilon<1 define
rho_epsilon(x,y)=1+epsilon p(x)p(y).
Since |p|<=1, this is smooth, strictly positive, normalized, and invariant under the simultaneous center transformation (x,y)->(-x,-y), but not under x->-x with y fixed.

Both one-variable marginals are EXACTLY Haar and center symmetric. However the conditional distribution of x given y is
rho(x|y)=1+epsilon p(x)p(y),
which is generally not center symmetric. Indeed int_SU2 p(x)^2 dx=1/4, so
E[p(x)|y]=(epsilon/4)p(y), and
Var(E[p(x)|y])=epsilon²/64 >0.
The unconditional half-integer (fundamental) moment E p(x)=0 nevertheless vanishes exactly.

Now let k(x) be a smooth nonnegative central identity cap multiplier with fundamental Fourier coefficient a_(1/2)=int k(x)chi_(1/2)(x)dx. Because chi_(1/2)=2p, its conditional expectation is
E[k(x)|y]=a0+epsilon p(y) int k(x)p(x)dx
=a0+(epsilon a_(1/2)/2)p(y).
Therefore
boxed: Var(E[k(x)|y])=epsilon² a_(1/2)²/16. (CS-1)
For a nontrivial small identity cap, a_(1/2)>0, so this influence energy is strictly positive despite a Haar target marginal. If k_even=(k(x)+k(-x))/2, then a_(1/2)=0 and the conditional influence in this particular example vanishes.

For physical deleted-target Wilson vacua, R3-IR-420 proves that a center-flux link transformation sends W_f to -W_f while leaving the HAMILTONIAN invariant. It gives the unconditional target center symmetry and removes half-integer characters from the UNCONDITIONAL Fourier expectation. It does NOT imply that the transformation leaves the chosen exterior variables Y_r pointwise unchanged. Unless such a localized symmetry is separately constructed, it cannot be used to assert E[chi_(half-integer)(W_f)|Y_r]=0.

Therefore the exact exterior influence I_cap(r)=Var(E[k(W_f)|Y_r]) in R3-IR-447 may involve half-integer character channels, even though the full vacuum cap expectation in R3-IR-422 involves only integer-spin characters after center symmetrization. Estimating only the integer-spin EXTERIOR influence is insufficient for an identity-centered (not center-even) cap unless a conditional center symmetry is proved. One can instead study the center-even double-cap observable, but then its relation to the identity cap requires the global symmetry and attention to its observable normalization.

No physical conditional half-spin nonzero expectation, spatial decay, uniform half-Haar survival or Yang-Mills mass gap is proved by the abstract example.
