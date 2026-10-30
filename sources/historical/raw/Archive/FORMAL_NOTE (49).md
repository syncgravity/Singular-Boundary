# Local nonlinear SU(2) insertion comparison by finite-rank Gaussian transport

Date: 2026-10-27. Scope: finite gauge-fixed regular chart; no arbitrary-support full-Wilson theorem claimed.

## Setup
Let a finite collection of SU(2) links be parametrized on a gauge-fixed flat-background chart by x in R^n with symmetric convex bounded chart G (e.g. |x_e|<=eta). Assume the undeleted Wilson reference action plus negative log Haar Jacobian admits S_0(x)-log J(x)=c_0+(1/2)x^TH_0x+R_0(x), with H_0 positive definite and osc_G R_0<=omega_0. Assume the inserted plaquette action has V_Q(x)=(1/2)x^TAx+R_Q(x), A=lambda D_Q^TD_Q >=0, with sup_G |R_Q|<=omega_Q. All plaquette holonomies are computed from actual link variables exp(x_e), hence Bianchi identities are exact. The chart must be chosen so that V_Q(0)=0 and no linear term remains; regular nonflat backgrounds require modifications and are not covered. The coordinate Haar Jacobian is included in R_0.

Define conditional insertion cost F_G=-log[ integral_G exp(-S_0(x)-V_Q(x))J(x)dx / integral_G exp(-S_0(x))J(x)dx ]. Define Gaussian gamma_0=N(0,H_0^-1), gamma_1=N(0,(H_0+A)^-1). Rank(A)<=3|Q| for SU(2) curvature.

## Theorem (regular-chart Gaussian comparison with no chart-volume penalty)
F_G <= 1/2 log det(I+H_0^-1/2 A H_0^-1/2) + omega_0+2 omega_Q? Correct bound:
Density of true chart reference mu_0^G relative to gamma_0 conditioned on G lies between e^-omega_0 and e^omega_0. Consequently E_mu0G[e^-V_Q] >= e^-omega_0-omega_Q E_gamma0G[e^-V_2] and F_G<= F_gauss,G+omega_0+omega_Q. (If osc R_0 used, bound e^-omega_0 is correct.)
Gaussian chart ratio E_gamma0G e^-V2 = det(I+H_0^-1/2 A H_0^-1/2)^(-1/2)*gamma_1(G)/gamma_0(G). Anderson inequality for centered Gaussians and symmetric convex G gives gamma_1(G)>=gamma_0(G), so F_gauss,G<=1/2 logdet. Thus
F_G <= (1/2) log det(I+lambda D_Q H_0^-1 D_Q^T)+omega_0+omega_Q.
If H_0>=mu I and ||D_Q||<=D*, then F_G <= (3|Q|/2)log(1+lambda D*^2/mu)+omega_0+omega_Q.
The identity and proof are valid at finite regulator; general coordinate chart G being symmetric convex is required for Anderson's comparison, and H_0 positive.

## Wilson remainder estimates
For flat stationary background and maximal coordinate magnitude eta<=eta_0, bounded plaquette length/incidence, standard Taylor yields |R_0|<=C lambda m eta^3 +C m eta^2 (the Jacobian bound), for m active links and all undeleted faces touching them. For q inserted faces |R_Q|<= C lambda q eta^3. Hence omega_0<=2C(lambda m eta^3 +m eta^2), omega_Q<=C lambda q eta^3. At eta=M lambda^-1/2 the bound gives O((m+q) M^3 lambda^-1/2 +m M^2 lambda^-1). If m>>q and h->0, no uniform bound follows. This is a sufficient local regular-chart estimate, not a global theorem.

## Full-measure chart complement
Let p_0=mu_0(G). Since E_mu0 e^-V >=p_0 E_mu0|G e^-V, the full insertion cost obeys F_full<=F_G-log p_0. A cutoff- and volume-uniform lower bound p_0>=exp(-C|Q|log lambda) remains unproved for arbitrary thin Penrose supports. Furthermore at large-field threshold plaquette angles lambda^-1/4, the chart eta=Mlambda^-1/2 cannot cover the contour event. Thus nonlinear large-field control requires a separate argument.

## Infrared statement
The determinant estimate depends on the gauge-fixed H_0 spectrum or directly on the localized curvature covariance D_QH_0^-1 D_Q^T. A regulator mu or local boundary conditions that make H_0>=mu I are hypotheses. For positive flat quadratic H_0=lambda D_0^TD_0+G with G>=0, one has D_0 H_0^-1 D_0^T<=lambda^-1 I, but this controls only *retained* curvatures, not arbitrary missing-face D_Q. To infer logarithmic insertion cost one must bound the missing-face covariance separately. Boundary/harmonic modes are not silently dropped.

## No-go / scope
Anderson's inequality cancels the truncated Gaussian partition-normalization penalty for convex symmetric regular charts. It does not give any lower bound on the true Wilson measure of the chart, and it says nothing about nonflat backgrounds that render the Hessian indefinite. Spatial locality of the transported field is not guaranteed by finite rank. The arbitrary interior Penrose insertion inequality, cutoff-stable nonlinear large-field polymers, R3 and continuum mass gap remain open.

## References
Balaban, Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories, Comm. Math. Phys. 102 (1985) 255-275. Balaban, Propagators for lattice gauge theories in a background field, Comm. Math. Phys. 99 (1985) 389-434.
