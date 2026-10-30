# Exact spin-one two-time perimeter bridge and gap-free covariance integral

2026-10-30 | R3-IR-408 | PROVED at the last-neighbor *zero-coupling* physical Wilson vacuum. No assertion about full-neighbor coupling or a continuum gap.

Let f be the deleted target rhombus and g its neighboring rhombus with magnetic coupling set to zero. Their shared link x is absent from every retained magnetic potential. Denote by a_e>0 the coefficient of its SU(2) electric Laplacian, by Omega_0(x,y)=omega(y)>0 the true gauge-invariant normalized vacuum, and by E_0 its stationary positive ground-state process. The x component is independent Haar-stationary SU(2) Brownian motion with generator a_e Delta, while y follows the interacting environment vacuum process. Choose based face words W_f(0)=x_0 L_0 and W_g(s)=x_s^{-1}M_s. Let O_0=k(W_f(0)) be a bounded nonnegative central cap, with a_0=int k and a_1=int k chi_1. Write p_g(s)=Tr(W_g(s))/2.

THEOREM (TB-1). For every s>=0, conditional on the complete environment path y(.),

E_x[O_0 p_g(s)^2 | y(.)]
= a_0/4 + (a_1/12) exp(-2a_e s) chi_1(M_s L_0).  (TB-1)

Proof. SU(2) fusion gives p(U)^2=(1+chi_1(U))/4. The spin-one character belongs to the eigenvalue -2 of Delta_SU2. Thus its conditional heat expectation from x_s to x_0 is exp(-2a_es)chi_1(x_0^{-1}M_s). Substitute W=x_0L_0; the central Haar integration identity
int k(W)chi_1(W^{-1}A)dW=(a_1/3)chi_1(A)
gives the result with A=M_s L_0. The constant spin-zero term is a_0/4. This is an original-link Feynman-Kac identity at the actual positive Wilson vacuum, not a Gauss-projected finite-temperature trace statement.

COROLLARY (TB-2). Since E_0 O=a_0 and E_0 p_g(s)^2=1/4,

Cov_0(O_0,p_g(s)^2)
=(a_1/12) exp(-2a_e s) E_y[chi_1(M_s L_0)]. (TB-2)

Here chi_1(M_s L_0) is a mixed-time environmental bridge; at s=0 it reduces to the physical gauge-invariant spin-one Wilson character of the outer boundary of the two-face region f union g (R3-IR-407). At s>0 it is a mixed-time object in the original-link trivialization. The full averaged correlation on the left is gauge invariant. All environmental magnetic couplings are unrestricted.

Since |chi_1|<=3 and |a_1|<=3a_0, the absolute integral satisfies

int_0^infinity |Cov_0(O_0,p_g(s)^2)| ds
<= |a_1|/(8a_e). (TB-3)

Proof: integrate |a_1| exp(-2a_es) 3/12 over s>=0. This bound is independent of the **interacting physical excitation gap** and the number of environmental links. Its a_e dependence is a kinematical private-link rate. Note the bound is on a response to the *squared* neighboring plaquette, not on the ordinary linear Wilson source p_g whose integrated cosh response is outstanding.

ADDITIONAL LIMITATION. This time-lag identity is not the time-integrated second moment X^2=b_g^2 int int p_g(s)p_g(t)dsdt: the latter involves two distinct source times and a three-point cap insertion. Neither its sign nor its cap-biased cosh comparison follows from TB-2. In particular TB-3 cannot be inserted as a bound on the desired cap log transport. No control of the physical t_g=1 system or regulator-uniform cap survival has been proved.

Theorem status: all-time zero-neighbor spin-one correlation and its absolute integral PROVED; requested averaged full-coupling favorable sign OPEN.
