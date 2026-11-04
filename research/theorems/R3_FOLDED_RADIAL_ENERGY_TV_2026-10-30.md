# Folded radial-energy total-variation criterion and transverse-sign obstruction
Date: 2026-10-30
Status: rigorous finite SU(2) radial functional inequality; connected Penrose scaling OPEN.

## Theorem
Use folded Haar probability mu(du)=(4/pi) sin^2(u) du on [0,pi/2] and positive H1 amplitude psi with integral psi^2 dmu=1. Set R=int |psi'|^2 dmu and nu=psi^2 mu. Then
TV(nu,mu) <= (1/2) sqrt(R).
Consequently nu([0,delta]) >= m_H(delta)-(1/2)sqrt(R).
For a gauge-ground-state folded marginal, R=E_rad/A_f, where E_rad=A_f int |psi'|^2 dmu; the folded amplitude must be obtained from the actual two-branch pushforward.

## Proof
The Neumann spectrum of -[sin(u)^-2] d/du[sin^2(u) d/du] on [0,pi/2] has spectral gap 8: the first nonconstant eigenfunction is 1+2 cos(2u). This follows by reflecting Neumann functions about pi/2 into the center-even SU(2) class subspace, whose first nonconstant character has spin 1 and Laplace eigenvalue 8. Thus 1-(int psi dmu)^2 <= R/8. Since 0<=int psi dmu<=1,
int(psi-1)^2 dmu=2(1-int psi dmu)<=2[1-(int psi dmu)^2]<=R/4.
Then int |psi^2-1| dmu <= sqrt(int(psi-1)^2 dmu)*sqrt(int(psi+1)^2 dmu)<=2 sqrt(R/4)=sqrt(R). TV is half the L1 distance. QED.

## Limits
To obtain nu(cap)>=c m_H(delta) via this additive inequality it suffices that R <=4(1-c)^2 m_H(delta)^2. The shrinking cap has m_H(delta)~(4/(3pi))delta^3, so the sufficient energy condition is R=O(delta^6), substantially stronger than the sought one-sided logarithmic-amplitude budget. This is a valid alternative criterion, not a proof of the required Penrose scaling.

## Why transverse energy positivity gives no radial monotonicity
On the auxiliary compact SU(2)xSU(2) group choose Omega_n(u,y)=exp[epsilon cos(2nu)k(y)] with a smooth nonconstant k on the second factor. Normalize conditionally: phi=Omega/psi. The conditional transverse kinetic energy is epsilon^2 cos^2(2nu) times a positive smoothly varying conditional variance of grad_y k (up to the fiber normalization), and generally has alternating radial derivative sign. Define V=E+sum a_e Delta_e Omega/Omega and shift E to make V>=0. The ground-state transform certifies Omega as the strictly positive ground state; smoothness follows from cos(2nu) being a smooth polynomial in cos(u), for integer n. This establishes nonexistence of a general transverse-energy monotonicity theorem based only on positivity.

## Outstanding
Prove a model-specific estimate for the actual connected Penrose deleted vacuum: either one-sided integrated W-E control giving K_f(delta_f)=o(h^-1/4), or a useful relative cap-mass estimate. Check that the original deleted-vacuum score current constants agree with the chosen SU(2) Laplacian normalization. No continuum mass gap is claimed.
