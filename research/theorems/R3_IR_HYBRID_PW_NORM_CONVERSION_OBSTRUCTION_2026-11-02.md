# Hybrid PW polymer norm: exact Hilbert/Wigner conversion obstruction — 2026-11-02

For t independent SU(2) Haar face variables, let H_sigma be the intrinsic orthogonal Peter–Weyl Hilbert norm and W_sigma the unnormalized Wigner matrix-coefficient weighted l1 norm, both with exp(sigma sum_i n_i). A degree-vector block n has d_n=product_i(n_i+1), contains d_n² Wigner coefficients, and each coefficient has squared Haar norm 1/d_n. Hence **||h||_(H_sigma)<=||h||_(W_sigma)**. The ordinary max/intersection norm is exactly W_sigma; the infimal sum-decomposition norm inf_(h=a+b)(||a||_W+||b||_H) equals H_sigma. Neither naive scalar hybrid retains both channels' distinct strengths.

The reverse embedding **H_sigma -> W_sigma is unbounded**, even for real gauge-invariant class functions: ||chi_n||_W/||chi_n||_H=n+1. For h_t=product_(i=1)^t chi_1(U_i), its ratio equals exactly 2^t at every sigma; full Wigner arrays of degree one give 2^(3t/2).

For delta>0 and z=e^(−2delta), an exact Cauchy–Schwarz calculation and optimality construction yield the **optimal radius-loss embedding norm**
**||H_(sigma+delta) -> W_sigma|| = [(1+4z+z²)/(1−z)^4]^(t/2)**.
At delta=(log 2)/2 it equals sqrt(52)^t. There is no radius-free, support-uniform scalar conversion. The earlier length-independent touching-support Hilbert bound ||K_t^(-1) C_b||_H<=1/4 therefore does not automatically convert to a Wigner coefficient-l1 bound; nor does a naive intersection or sum norm create a new closed hybrid algebra.

These findings do not disprove a restricted-range endpoint Wigner bound, typed/channel-aware projective polymer construction, support-penalized radius tradeoff, or the physical interacting gap. The fixed-support nonlinear closure, uniform interacting lambda=1 gap and continuum Yang–Mills mass gap remain unproved. Complete report, exact rational verifier, passing log and SHA-256 manifest are archived in Proof Audits Library.