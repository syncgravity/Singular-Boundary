# Certified finite-even-moment test for the physical Wilson cosh comparison

Date 2026-10-30. R3-IR-404. Exact finite-volume certification inequality, not a proof of the physical signed comparison.

Use the genuine Gauss-projected positive Euclidean reference measure at the last-neighbor coupling zero (R3-IR-403). Let O>=0 be a cap insertion with E_0 O>0, let X=b_g integral_0^beta p_g(U_s) ds, and assume |p_g|<=1, so |X|<=B=beta b_g. Denote ordinary and cap-biased expectations by E_0 and E_0^O. The exact transport ratio is R_beta=E_0^O cosh(X)/E_0 cosh(X).

For integer N>=0 define the positive even Taylor polynomial
P_N(x)=sum_{n=0}^N x^(2n)/(2n)!.
Let M_N^O=E_0^O P_N(X) and M_N=E_0 P_N(X), and define the certified uniform remainder
r_N(B)=cosh(B)-P_N(B).
Because all Taylor terms are nonnegative and |X|<=B, pointwise
0<=cosh(X)-P_N(X)<=r_N(B).
Consequently
M_N^O/(M_N+r_N(B)) <= R_beta <= (M_N^O+r_N(B))/M_N. (FM-1)
All quantities except the known deterministic remainder are finitely many even moments of the *original physical reference path ensemble*.

The lower certificate R_beta>=1/2 is ensured by the explicit computable condition
2 M_N^O-M_N >= r_N(B). (FM-2)
At the last-neighbor zero-coupling reference, R_beta>=1/2 means F_beta(1)>=F_beta(0)/2. This is NOT yet F_beta(1)>=alpha_a^2/2, because the Gauss-projected finite-beta baseline need not be Haar (R3-IR-400). At each fixed finite lattice, taking beta to infinity after establishing a suitably uniform-in-beta bound yields the vacuum half-Haar claim.

A deterministic bound using only elementary functions is
r_N(B) <= exp(B) B^(2N+2)/(2N+2)!.
This follows from the absolute exponential Taylor remainder, as the omitted even terms form a subset of all terms of degree at least 2N+2. The bound is safe but loose at large B.

The certificate is **finite**, **nonperturbative in the coupling**, and avoids claims of variance ordering or spectral gaps. It gives a potential falsification and verification protocol: independently estimate the even physical path moments and the Taylor remainder, with rigorous interval uncertainties, before declaring the finite-beta ratio >=1/2. It is NOT a new analytic inequality forcing that condition: the moments can fail it. Furthermore B=beta b_g and b_g~h^-2, so N generally must increase with beta/h² to suppress r_N(B), making a uniform refinement proof out of reach without a new dynamical moment estimate.

The central-flux involution is useful for interpreting the even moments but is not needed for the polynomial sandwich once the cosh identity has been established. No continuum mass gap is implied.
