# Audit: Nonlinear cavity stability, neutral modes, and competing minima

Date: 2026-10-27

## Claim boundaries

There is no uniform almost-sure strongly convex, uniquely minimizing branch of the raw SU(2) Wilson action for arbitrary finite lattice cavities. Any probabilistic high-probability version requires an independent estimate of the bad-field set, not furnished by the existing local conditional thermal-excess estimate.

## Proposition 1: positive-probability negative Hessian region

Let a plaquette have a conditionally Haar-free private link, or consider the one-plaquette Wilson model (a valid finite Wilson system). Gauge fix remaining links so the action for the physical holonomy is S(g)=lambda(1 - (1/2)Tr(g))=lambda(1-cos theta). Along a one-parameter geodesic g(theta)=exp(theta X) with |X|=1, the second derivative S''(theta)=lambda cos theta. It is negative on pi/2<theta<pi. The normalized Wilson measure has strictly positive smooth density on every open subset of SU(2), hence the set of configurations with this negative directional Hessian has positive probability for every finite lambda. Thus a pointwise or almost-sure positive Hessian on *all* configurations is false, even after eliminating gauge zero modes.

Indeed the exact probability of the bad angular region is
P_bad=(2/(pi q(lambda))) int_{pi/2}^pi sin(theta)^2 exp[-lambda(1-cos theta)]dtheta >0.
For lambda>=1, q(lambda)>=c lambda^{-3/2}, and P_bad <= C lambda^{3/2} exp(-lambda). This is an independent good/bad estimate in the free-face example, not for arbitrary Penrose cavities.

## Proposition 2: flat nearly neutral modes obstruct fixed diagonal dominance

For a real massless chain of N interior variables with Dirichlet ends and energy E(x)=(lambda/2) sum_{j=0}^N (x_{j+1}-x_j)^2, x_0=x_{N+1}=0, Hessian H=lambda L_N, diag 2lambda, adjacent -lambda. The row sum q=max_i sum_{j!=i} |H_ii^{-1}H_ij| is 1 on interior rows. The lowest eigenvalue is 4lambda sin^2(pi/(2(N+1))) ~lambda pi^2/(N+1)^2. This exhibits failure of q<1 (uniform margin) at an exactly flat, strictly positive definite Hessian. This is a scalar quadratic subsystem illustrating why bounded incidence and flatness do not imply the proposed contraction; it is not asserted to be the complete Penrose Hessian.

## Proposition 3: valid good/bad response bound

Let G be any measurable regular-background event on which (i) the gauge-fixed minimizing branch is unique and interior, (ii) H>=m I and q<=q0<1 with local coupling bounds. On G, the implicit-function derivative and block Neumann series imply the branchwise exponential response derived earlier. For any event A testing this response, P(A) <= P(A intersect G)+P(G^c). An unconditional exponential response probability bound requires an independent estimate P(G^c), including competing branches and nonflat configurations. A one-link thermal-excess moment bounds fluctuation around conditional minima and does not control P(G^c) in general.

## Scope

No theorem for arbitrary Penrose cavity stability, arbitrary thin-support absolute large-field tail, R3, or continuum Yang-Mills mass gap is obtained.
