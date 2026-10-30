# Explicit finite 11-face open-disk SU(2) double-center cap probability

Date: 2026-10-30. This is a **fixed-regulator weak-coupling** estimate, NOT a refinement-uniform cap theorem or continuum Yang-Mills mass gap.

The deleted face holonomy u is independent Haar at fixed ten retained based-face holonomies. Set p_f=Tr(u)/2 and C_delta={u: |p_f|>=1-delta}, for delta in (0,1). SU2 Haar class measure has density (2/pi)sin^2(theta) dtheta with p_f=cos(theta). Thus c_delta=Haar(C_delta)= (2/pi)[theta-sin(theta)cos(theta)], theta=arccos(1-delta). Note c_delta is a cap around BOTH +/- identity, and behaves as (8 sqrt(2)/(3 pi)) delta^(3/2) as delta tends to zero. This must not be confused with the one-center cap measure, which is c_delta/2.

For the physical normalized ground state Omega at unit electric link coefficients and ten equal positive magnetic couplings t=3/32000, put r=3/320, q=t/r=1/100. The exact four-neighbor analytic selection bound on intermediate-normalized Psi gives ||Q_f Omega||<=||Q_f Psi||<=eps=2 q^4/(1-q)^10=2.21145471064376112174997449450192382e-8. Since ||P_f Omega||=sqrt(1-||Q_f Omega||^2), and P_f averages u at fixed retained holonomies,

m_f(delta)=||1_C_delta Omega||^2 >= [sqrt(c_delta) sqrt(1-eps^2)-eps]_+^2.

At delta=1/10 the exact SU2 class integral is c_delta approximately 0.03738607346849864572, and the right side is approximately 0.03738606491659204718, hence m_f(0.1)>0.03738606. This bound is for the full normalized finite-disk ground state at a SPECIFIED all-positive equal-coupling point, not only an existence statement. Separately, the sign-orbit argument verifies the ground state is non-Haar at another much smaller equal coupling, but the cap estimate itself need not rely on that tiny lower bound.

Refinement limitation: with a_min the minimum link electric coefficient and N the number of retained magnetic faces, the free-vacuum spectral gap bound is at most available as 3a_min/4 in this argument. A generic safe polydisc radius scales as r_N=O(a_min/N), e.g. r_N=3a_min/(32N) with the same conservative projector margin. The analytic bound in terms of q=t/r_N therefore is NOT uniform in N at fixed physical t. Also c_delta tends to zero as delta^(3/2), and a fixed eps>0 cannot yield a positive lower bound for arbitrarily shrinking delta. Consequently nothing here proves the sought delta~h cap lower bound, Yang-Mills continuum mass gap, or any refinement-uniform statement.

Executable high-precision verification: research/scripts/validate_finite_center_cap.py.
