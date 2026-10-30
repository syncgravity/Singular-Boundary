# Conditional refinement-scale center-cap criterion; volume dependence remains
Date: 2026-10-30
Status: rigorous CONDITIONAL finite-graph criterion, not a refinement-uniform theorem.

Consider a connected finite SU2 lattice disk with N retained magnetic plaquettes, electric T=sum_e a_e(-Delta_e), a_e>=a_min>0, and deleted-face conditional product-Haar coordinates. Assume in addition that the analytic intermediate-normalized ground-state Haar complement Phi(b)=Q_f Psi(b) VANISHES whenever any one of four specified adjacent retained couplings is zero. The four-factor selection is independently established for the extracted M5 11-face disk, but is NOT proved for arbitrary Penrose refinements. This hypothesis must be checked at each new geometry.

The free electric spectral gap is at least 3 a_min/4. With r_N=3 a_min/(32N), the total magnetic operator norm on the complex polydisc |b_g|<=r_N is at most 3 a_min/32. The Riesz circle |z|=3a_min/8 gives an analytic intermediate-normalized vacuum Psi with ||Psi||<=2. By Cauchy expansion and the four-factor vanishing hypothesis, at equal nonnegative couplings t<r_N with q=t/r_N:
epsilon=||Q_f Omega||<=||Q_f Psi||<=2 q^4/(1-q)^N.

For the double center cap C_delta={u:|Tr(u)/2|>=1-delta} and 0<delta<=1, Haar mass is
c_delta=(4/pi) integral_(1-delta)^1 sqrt(1-x^2) dx >= (8/(3pi)) delta^(3/2).
The cap-vacuum estimate is m_f(delta)>=[sqrt(c_delta) sqrt(1-epsilon^2)-epsilon]_+^2.
A useful explicit sufficient criterion is
q <= min{1/(2N), K delta^(3/16)}, K=[sqrt(8/(3pi))/16]^(1/4).
Indeed (1-q)^(-N)<=2, so epsilon<=4q^4<=sqrt(c_delta)/4. Since epsilon<=1/4, the bracket is >=sqrt(c_delta)(sqrt(15)/4-1/4), giving
m_f(delta) >= [(sqrt(15)-1)^2/16] c_delta >= c_delta/2 >= 4/(3pi) delta^(3/2).
This is a conditional Haar-comparable cap lower bound for explicit sufficiently small coupling t.

The criterion requires t <= [3a_min/(32N)] min{1/(2N),K delta^(3/16)}. In the volume-controlled regime it demands t <=3 a_min/(64 N^2), which becomes tiny as N grows. It does NOT support a fixed physically scaled magnetic coupling under refinement, does not show a uniform bound for delta~h, and does not imply the continuum mass gap. The four-factor selection hypothesis itself is not known uniformly. This theorem identifies exactly the gap between fixed-volume analytic control and a physically relevant uniform center-cap estimate.

The arithmetic and SU2 Haar integral inequalities are independently verified by research/scripts/validate_conditional_refinement_cap.py.
