# Exact annular capacity minimizer for magnetic-deletion trial
Date: 2026-10-30
Status: proved finite-volume identity; Penrose uniform cap control OPEN.

Assume the physical SU(2) convention -Delta chi_j=j(j+1)chi_j. Let H_+=H_-+b_f(1-cos u), D=A_f/4, u=arccos p_f, and let the *full-angle* deleted-vacuum law have strictly positive density q(u)=(2/pi)sin²(u)psi(u)², 0<u<pi. The ground-state transform gives Delta=E_+-E_- <= [D int |g'|² q du+b int(1-cos u)g²q du]/int g² q du.

For 0<r<R<pi, among absolutely continuous g=1 on [0,r], g=0 on [R,pi], the kinetic minimizer on [r,R] is g(u)=[int_u^R dt/q(t)]/[int_r^R dt/q(t)], with exact minimum int |g'|²q=[int_r^R du/q]^-1. Proof is weighted Cauchy-Schwarz, with equality g' proportional to -1/q. Positive continuous density on the closed annulus ensures the integrals are finite.

Writing m(s)=int_0^s q and I(r,R)=int_r^R q^-1, the Rayleigh quotient of that g gives
Delta <= D/[m(r)I(r,R)] + b(1-cos R)m(R)/m(r).
This is a valid but not globally optimized magnetic-deletion comparison. It does not automatically reproduce the historical logarithmic trial theorem.

Assume additionally the *full-angle* center-to-annulus amplitude comparison psi(u)<=e^K psi(v) for all 0<=v<=r and r<=u<=R (K>=0). Put mu(s)=int_0^s rho_H and J(r,R)=int_r^R 1/rho_H(u)du. Let a=inf_[0,r]psi²>0. Then m(r)>=a mu(r), q(u)<=e^{2K}a rho_H(u) on annulus, I>=e^{-2K}J/a, and m(R)/m(r)<=1+e^{2K}[mu(R)-mu(r)]/mu(r). Thus an explicit bound is
Delta <= D e^{2K}/[mu(r) J(r,R)] + b(1-cos R){1+e^{2K}[mu(R)-mu(r)]/mu(r)}.
This bound depends exponentially on K, so K=o(h^-1/4) alone does NOT yield an O(h^-1 polylog(1/h)) deletion estimate through this cutoff. Additional optimized logarithmic/capacity arguments must be independently checked.

Haar near-identity scaling: mu(r)~(2/(3pi))r³, J(r,R)=(pi/2)(cot r-cot R). At r=c sqrt(h), R=C sqrt(h), with 0<c<C, 1/[mu(r)J] = Theta(h^-1) and (1-cos R)=Theta(h). Hence under A=O(1), b=O(h^-2), and a uniform O(1) full-angle K, the bound gives Delta=O(h^-1). The h scalings are explicitly hypotheses, not an unconditional Penrose theorem.

Important: a folded-center marginal can be used to infer the identity-center result only after independently establishing center-flux symmetry of the actual deleted Hamiltonian, as discussed in the October 29 exact-fiber theorem.

No continuum mass gap claimed.
