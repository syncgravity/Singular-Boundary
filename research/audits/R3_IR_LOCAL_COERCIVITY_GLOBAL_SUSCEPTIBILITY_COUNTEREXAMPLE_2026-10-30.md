# R3-IR-440 — Local marginal coercivity does not control global cap susceptibility

2026-10-30. Exact two-block SU(2) counterexample to an invalid proof implication. This is an abstract smooth positive probability measure, NOT asserted to be a Wilson ground-state measure.

Let x,y be independent SU(2) Haar variables before reweighting, and let q(U)=chi_1(U) be the integer-spin-one character, satisfying integral q=0, integral q²=1, -1<=q<=3, and -Delta q=2q. For 0<delta<1 set

rho_delta(x,y)=1+(delta/9)q(x)q(y).

This is normalized and strictly positive: rho_delta>=1-delta/3>0. It is smooth, conjugation-invariant in each argument and invariant under independent center flips x->-x and y->-y. Both marginals are EXACTLY Haar: integration over either variable kills the correction. In particular the local x-cylinder Poincare inequality has the sharp Haar spin-half constant 3/4, with no dependence on any environmental kinetic coefficient.

Choose any smooth central positive identity-cap multiplier O(x)=k(x) with a1=int k(x)q(x)dx !=0 (a sufficiently narrow nonzero identity cap has a1>0). Denote a0=int k dx. Then E_rho O=a0. The covariance with the slow environmental test field phi(y)=q(y) is

Cov_rho(O,phi)=(delta/9) a1,

because integral q(y)^2 dy=1. Give the two blocks the Dirichlet form

D_epsilon(phi)=int [|grad_x phi|²+epsilon |grad_y phi|²] rho_delta dxdy,

where epsilon>0. For phi=q(y), the x derivative vanishes, and the y energy is exactly 2epsilon (integrating the interaction over x removes it). Using the exact susceptibility dual A=sup_phi {2Cov(O,phi)-D_epsilon(phi)} from R3-IR-432 and optimizing a scalar multiple of q(y), one obtains

A_epsilon(O)>= [delta a1/9]^2/(2epsilon)
=delta² a1²/(162epsilon). (NO-1)

Thus A_epsilon diverges as epsilon->0 even though the local x marginal is exactly Haar, the cap expectation itself equals a0, and the local cylinder-function Poincare constant is fixed. The conditional x density is also uniformly bounded above and below by universal constants for fixed delta, so simply upgrading local marginal coercivity to local conditional coercivity does not address this.

In terms of conditional expectation, m(y)=E[O|y]=a0+(delta/9)a1 q(y). Its nonconstant component is precisely the source that excites the slow environmental mode. A genuinely useful multiscale susceptibility estimate must quantitatively suppress such conditional correlations relative to the environmental inverse kinetic scale, or control the associated environmental flux cost.

This example does NOT disprove the completed Wilson target cap bound: it has exactly the Haar cap expectation. It only disproves the suggested inference from R3-IR-439 local coercivity to a universal upper bound on R3-IR-432 global cap susceptibility. No Wilson regulator-uniform mixing estimate or continuum Yang-Mills mass gap is established.
