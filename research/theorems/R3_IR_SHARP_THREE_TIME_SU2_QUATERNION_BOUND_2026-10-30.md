# R3-IR-410 — Sharp SU(2) quaternion correction to R3-IR-409

2026-10-30. An exact constant improvement of the three-time Wilson cap bridge bound. The formula TT-1 in R3-IR-409 is unchanged. Its conservative constant 5 can be replaced by the **optimal pointwise constant 3**.

For SU(2) matrices A and B write their unit-quaternion coordinates as A=(a0,a), B=(b0,b) in the unit sphere of R4. Set p(A)=Tr(A)/2=a0. The standard quaternion identity gives
p(A^-1 B)=a0 b0+a dot b.

Therefore the environmental kernel from TT-1 is
K(A,B)=4p(A)p(B)-p(A^-1 B)=3a0 b0-a dot b.

This is the real bilinear form with diagonal matrix diag(3,-1,-1,-1). Its operator norm is exactly 3, and hence |K(A,B)|<=3 for all A,B in SU(2). Equality is attained at A=B=I. The former triangle estimate |K|<=5 was valid but nonoptimal.

For the zero-neighbor-coupling genuine Wilson vacuum with magnetic-private shared link electric coefficient a_e, cap character coefficients a0=int k>0, a1=int k chi_1, and X_beta=b_g integral_0^beta p_g(s)ds, the exact TT-1 gives

|E_0^O X_beta²-E_0 X_beta²|
<= (|a1| b_g²/(4a0)) int_[0,beta]^2 exp[-2a_e min(s,t)-(3a_e/4)|s-t|] ds dt
<= |a1| b_g²/(3 a0 a_e²).

The second inequality uses the exact full quadrant integral 4/(3 a_e²). This is stronger by a factor 3/5 than R3-IR-409's archived upper bound.

The pointwise constant 3 is sharp; the final integrated constant need not be jointly saturated by an admissible evolving Wilson environment. This proves no sign. At a1/a0 approaching 3, the estimate remains order (b_g/a_e)^2 and does not yield the full-coupling cap-biased cosh comparison or a regulator-uniform mass gap.

This corrects only the numerical sharpness of the bound, not the three-time identity or its finite-volume scope.