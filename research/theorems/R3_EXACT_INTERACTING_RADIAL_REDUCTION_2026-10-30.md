# Exact interacting radial reduction and unresolved one-sided bound
Date: 2026-10-30
Status: conditional analytic derivation; no interacting-current bound claimed

## Setup and conventions
On a finite compact product of SU(2) links, use the unit-S^3 bi-invariant Laplacian, the Dirichlet form Q(F)=sum_e a_e int |grad_e F|^2 + int V F^2, and the strictly positive normalized ground state Omega of H=-sum_e a_e Delta_e+V. Consider a simple plaquette f whose boundary edges occur once, with p=Tr(U_f)/2, u=arccos(p), A_f=sum_{e in boundary f} a_e. For a full class angle u in (0,pi), normalized Haar radial weight is (2/pi)sin^2(u). Center folding to [0,pi/2] requires combining the two branches and the corresponding endpoint fluxes; it is not automatic that the UNFOLDED wavefunction is center symmetric.

## Lemma 1 (exact radial carré du champ)
For each boundary edge, |grad_e p|^2=1-p^2 and Delta_e p=-3p; consequently Gamma(u)=A_f and Delta_a u=2 A_f cot(u). Edges outside f contribute zero. This remains true with all other plaquette interactions present because it is a geometry identity, not a factorization assumption.

## Lemma 2 (ground-state fiber decomposition)
Disintegrate Haar measure dm(x)=rho_H(u)du dm_u(x) with rho_H=(2/pi)sin^2(u). Define psi(u)^2=E_m[Omega^2|u], phi(x)=Omega(x)/psi(u(x)), E_m[phi^2|u]=1. Assume admissible smooth fiber transport / weak Sobolev traces and no boundary contributions beyond the SU(2) Haar endpoints. For all radial test functions g, the exact quadratic form of g(u)phi(x) equals
Q(g phi)=int rho_H(u)[A_f |g'|^2+W(u)|g|^2]du,
where W(u)=E_m[V phi^2+sum_e a_e |grad_e phi|^2 |u].
The cross term vanishes: E_m[sum a_e grad_e u dot (phi grad_e phi)|u]=0. This follows from the radial integration-by-parts identity (the conditional derivative of E_m[phi^2|u]=1) and the Haar Jacobian. Since Omega=psi phi minimizes Q at fixed normalization, radial variations yield the weak equation
 -A_f/rho_H (rho_H psi')'+W psi=E psi.
This is an exact nonlinearly self-consistent radial reduction, NOT an independent scalar potential model: phi and W depend on Omega. If the face variable is folded, both branches must be combined before using the radial equation, and the effective W is their fiber-weighted combination.

## Corollary (radial flux)
For regular center endpoint, A_f sin^2(u) psi'(u)=int_0^u sin^2(t)[W(t)-E]psi(t)dt.
A nonpositive primitive is sufficient for psi to be nonincreasing, K(delta)=0 and at-least-Haar center mass. Nothing in V>=0 or in the transverse energy term proves the primitive nonpositive; a positive ground state alone cannot determine its sign.

## Critical outstanding issues
1. Verify precisely the full-angle versus folded-angle conditional ground state and endpoint terms in the repository's magnetic-deletion setting. The folded marginal is psi_fold^2(u)=[psi_full^2(u)+psi_full^2(pi-u)]/2, with correct normalization convention; it is NOT obtained by assuming psi_full(pi-u)=psi_full(u).
2. Control the actual interacting W_f(u)-E_f in a one-sided integrated sense, uniformly over f in D_R, at the scale K_f(delta_f)=o(h^-1/4). This is OPEN.
3. Check the published radial Ward/current constants against the chosen generator normalization and class-angle convention.
4. Do not identify this conditional reduction with a complete bulk deletion theorem, Wilson-angle covariance proof, or continuum mass gap.

## Provenance
Derived analytically from SU(2) group geometry, Haar disintegration and the ground-state variational principle. This note is not a numerical validation of the Penrose ground state and does not change Stage 26 datasets.
