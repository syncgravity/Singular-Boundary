# Exact scale-local nonlinear Wilson reference measure: a guarded-block disintegration

Date: 26 October 2026. Project: The Singular Boundary. Status: exact finite-regulator construction; no continuum-stable residual activity theorem or mass-gap theorem.

## Setup
Let K be a finite oriented three-dimensional cell complex with plaquette/link incidence bounded by D; its spatial layers may be Penrose rhombic complexes. Let E be its links, P its spatial and temporal four-link plaquettes, and d_p(U)=1-(1/2)Tr W_p(U) in [0,2]. Let beta_p= lambda c_p, 0<c_- <= c_p <= c_+, with lambda=(g_3^2 h)^-1, with anisotropic a_t/h bounded above and below. All statements below are exact for any nonnegative beta_p, regardless of scaling.

Choose a retained guard-link set Y subset E so that the components I_1,...,I_N of E\Y have the **plaquette separator property**: each plaquette intersects at most one interior component I_b. Such a guard always exists (trivially Y=E); a useful coarse block choice requires adequate guard collars and can have extensive retained degrees of freedom. Define P_b={p: boundary p intersects I_b}, and P_Y={p: all four links in Y}. These form a partition of P. A plaquette belonging to P_b may also contain retained guard links.

For fixed guard field y in SU(2)^Y, define
 S_b(x_b;y)=sum_{p in P_b} beta_p d_p(x_b,y),
 Z_b(y)= integral_{SU(2)^{I_b}} exp(-S_b(x_b;y)) dx_b,
 nu_b(dx_b|y)=Z_b(y)^-1 exp(-S_b(x_b;y)) dx_b.
The reference action contains the full nonlinear original SU(2) Wilson terms, including all spatial and temporal plaquettes touching the block. No Taylor truncation is imposed. Each Z_b is strictly positive and finite by compactness.

## Theorem 1 (exact guarded-block Gibbs factorization)
The full normalized measure has the disintegration
 mu(dy,dx)=mu_Y(dy) product_b nu_b(dx_b|y),
 mu_Y(dy)=(Z_full)^-1 exp[-S_Y(y)] product_b Z_b(y) dy,
 S_Y(y)=sum_{p in P_Y}beta_p d_p(y).
Equivalently its exact boundary action is
 S_eff(y)=S_Y(y)-sum_b log Z_b(y),
 up to an additive constant.
Proof: use the plaquette separator property to write S=S_Y+sum_b S_b; factorize product Haar integration at fixed y; apply Fubini. This is gauge covariant: simultaneous gauge transformation of all links, including guards, maps each factor by Haar-preserving changes of interior variables. The expressions for Z_b are gauge invariant under transformations that act consistently on its boundary vertices. No selection of a unique background minimizer or gauge fixing is needed.

## Theorem 2 (exact nonlinear local source cumulants)
For bounded gauge-invariant local sources O_i supported in P_b define Z_b(y;t)=int exp[-S_b(x;y)+sum_i t_i O_i(x,y)]dx. Then derivatives of log Z_b at t=0 are genuine connected conditional cumulants under nu_b. In particular, if |O_i|<=1,
 |Cov_nu(O_1,O_2)|<=1,
 and Var_nu(O_i)<=1.
All high cumulants exist and are bounded for fixed order independently of lambda and volume because sources are bounded (though such uniform finite-order bounds do not imply spatial decay). Mixed derivatives across distinct interiors vanish at fixed y. Unconditional correlations need not vanish because of fluctuations of y.

## Theorem 3 (exact local defect/free energy and bounds)
For fixed y, set A_b=sum_{p in P_b} beta_p d_p. Then
 0<= A_b <=2sum_{p in P_b} beta_p,
 exp(-2sum beta_p)<= Z_b(y)<=1.
 For arbitrary shifts delta beta_p supported in P_b, derivative of log Z_b = -E_nu[d_p] and Hessian is Cov_nu(d_p,d_q). Hence
 |log Z_b(y;beta')-log Z_b(y;beta)|<=2sum_{p in P_b}|beta'_p-beta_p|.
This is an exact, ambient-volume-independent comparison with a *local* cost O(lambda |P_b|). It is not the O(|P_b|log lambda) improvement needed for thin contours.

## Countertest (non-small generated guard coupling)
Two spatial/temporal plaquettes sharing eliminated link u and retaining outer holonomy V=AB with couplings t,s have
 Z_{t,s}(V) = z(sqrt(t^2+s^2+2ts p(V))), z(r)=2 I_1(r)/r.
For t=s=T, S_eff(V)=-log Z has oscillation log z(2T) = 2T-(3/2)log(2T)+O(1). Therefore the exact, nonlinear interior integration can generate an O(lambda) boundary interaction even though each conditional interior measure is perfectly normalized and no Taylor error remains. The local reference eliminates the *local Gaussian remainder* but gives no smallness bound on the retained guard effective interaction.

## Local background formulation
One may choose any gauge-covariant family of compatible constrained minimizers x_b^*(y), when measurable selections are possible, and write
 Z_b(y)=exp[-E_b(y)]A_b(y), E_b(y)=min_x S_b(x;y), A_b=int exp[-(S_b-E_b)]dx.
This is exact and gauge invariant at the level of E_b,A_b. Gauge-covariance of a pointwise chosen minimizer is not automatic if stabilizers/multiple minimizers occur; use gauge orbits or measurable gauge-fixed charts. Keeping the complete nonlinear S_b in nu_b avoids using a global quadratic approximation in large-field sectors.

## Multiscale iteration
At level k choose a guard Y_k of the current effective link variables and apply the same exact disintegration to S_eff^(k). A new exact action is defined by integration. However the effective action will contain multiloop terms supported on more than four links, so the separator must be defined by **supports of all current interactions**, not merely original plaquettes. A coarse background action A_k and residual R_k=S_eff^(k)-A_k must be specified by an explicit projection/extraction; none of the identities above bounds a rooted polymer norm of R_k. Expanding every effective interaction by support can cause a guard that retains almost all links if arbitrary long-range terms are not already controlled. This is the noncircularity gate.

## Required independent estimates
(i) Uniform geometric construction of sufficiently thin guards for Penrose prism complexes and all successive effective interaction supports; (ii) local background-covariant covariance/conditional mixing estimates on nu_b (not only bounded variance); (iii) exponentially small nonlinear large-field contour probabilities including bad exterior backgrounds; (iv) extraction of relevant gauge interactions with uniform connected residual activities and determinant/Jacobian bounds. None is proved here. R3 and continuum R2 mass gap remain open.
