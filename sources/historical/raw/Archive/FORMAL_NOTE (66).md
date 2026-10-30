# Good/bad-field and multiscale response synthesis: rigorous conditional theorem
Date 2026-10-27

## Framework
Let a finite SU(2) Wilson cavity measure mu0 have action S0=sum_{p in P0} beta_p d(W_p), with 0<=d<=2 and beta_p<=c_+ lambda. Let Q be a prescribed set of inserted faces and V_Q=sum_{p in Q} beta_p d(W_p). Let G be any measurable event (possibly a union of gauge-fixed chart/branch events). Define p_bad=mu0(G^c), Z_G=E_mu0[1_G exp(-V_Q)] and F_G=-log E_mu0[exp(-V_Q)|G]. The exact decomposition is
E_mu0 exp(-V_Q) = (1-p_bad) exp(-F_G) + E_mu0[1_{G^c} exp(-V_Q)].
In particular
F_Q <= F_G - log(1-p_bad) (if p_bad<1).
This formula is an UPPER BOUND for insertion free energy. It does NOT yield upper-tail control of bad exteriors from p_bad without a separate estimate: conditional bad sector may be enhanced or suppressed by insertion.

## A genuine nonlinear bad-field probability budget
For any local nonnegative observable A(U)<=2c_+ lambda m involving at most m Wilson plaquette terms, E_mu0[A 1_{G^c}] <=2c_+ lambda m p_bad; and for any event E,
mu0(E)<=mu0(E intersect G)+p_bad.
To make O(m log lambda) expected cost from bad field alone, it suffices to prove p_bad <=C log(lambda)/lambda. This is NOT proved for arbitrary Penrose cavities. For an exp[-c sqrt(lambda) m] polymer tail, the needed p_bad estimate is much stronger and must scale with m.

## Conditional branch response and spectral shell identity
On a smoothly parameterized regular branch, assume H(y)=S_xx(x_*(y),y)>0. Then dx_*/dy=-H^{-1}S_xy. For any dyadic spectral partition {P_j} of H, EXACTLY
H^{-1} f=sum_j H^{-1}P_j f, and
||H^{-1}P_j f||<= (inf spec(H|ran P_j))^{-1} ||P_j f||.
An infrared norm estimate follows if independent information controls the shell weights ||P_j S_xy||; merely bounding Hessian entries and incidence does not control them. Spectral projectors are not automatically spatially localized.

## Simple exact massless-chain test
For E=(lambda/2)sum_{i=0}^{N}(x_{i+1}-x_i)^2, x_0=0, x_{N+1}=y, minimizer x_i=i y/(N+1), minimum E_min(y)=lambda y^2/[2(N+1)]. The response dx_i/dy=i/(N+1) does not decay with distance from the source boundary on scales proportional to N, despite energetic cost decreasing as 1/(N+1). This shows why trying to control an unweighted derivative of the field, rather than its energetic response, fails in the massless sector.

## A rigorously bounded energy response with no spectral gap
For the same chain, the gradient of the minimizer in each bond equals y/(N+1), so the gradient energy is lambda y^2/(2(N+1)); this illustrates cancellation of near-neutral modes in the *energy norm*. A general analogous bound follows from the variational formula, when a bounded-energy extension operator exists: if a boundary datum y admits a compatible trial x=Ey with ||D Ey||^2<=C_j ||y||^2 then E_min(y)<=lambda C_j ||y||^2/2. This is conditional on geometric extension and does not imply Gibbs control of random boundary y.

## Nonlinear sector transfer theorem (conditional)
Suppose G_Q is a measurable good-field event with mu0(G_Q^c)<=eps_Q, and on G_Q one independently constructs a comparison e^{-V_Q} with F_{Q|G_Q}<=C |Q|(1+log lambda). Then the complete nonlinear insertion satisfies
F_Q<=C |Q|(1+log lambda)-log(1-eps_Q).
No estimates from the bad-field sector are needed for this *upper* insertion bound (positive integrand). But proving F_{Q|G_Q} for full geometry and eps_Q independent of the insertion ratio is exactly the open Penrose work. A different type of bad-field estimate is required for large-field polymer events in the insertion-included Gibbs measure, because its measure changes via e^{-V_Q}/E exp(-V_Q).

## Crucial distinction of probability measures
The cavity mu0 and full muQ obey muQ(A)=E_mu0[1_A e^{-V_Q}]/E_mu0[e^{-V_Q}]. Thus muQ(A)<=mu0(A)e^{F_Q}. Without F_Q, a mu0 bad-event tail cannot be blindly transferred to muQ. Conversely for events supported on full measure, conditional heat-bath estimates are directly usable in muQ but may be centered on random constrained minima.

## Status
The exact decomposition, good/bad budget, branch-response spectral identity, and massless counterexample are rigorous. No uniform Penrose good-field probability, shell-local coercivity, branch-crossing control, absolute thin-support curvature tail, nonlinear insertion theorem, R3 or R2 are proved.
