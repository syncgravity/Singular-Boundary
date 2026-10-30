# R3-IR-429 — Explicit weak-coupling stability of full Wilson target cap

2026-10-30. Exact finite-volume original-link SU(2) Wilson estimate conditional on a small magnetic/electric ratio. It is NOT the physically required strong-coupling, regulator-uniform theorem.

Use R3-IR-427: for R=b_g/a_x and any t>0, the true full-environment Wilson vacuum satisfies P(W_f in B)/Haar(B)>=e^(-4Rt)m(t)^2, where m(t)=min_{x,x',z} k_t(x,z)/k_t(x',z).

The normalized SU(2) heat kernel with Casimir j(j+1) has character expansion
k_t(U)=1+sum_{n>=1}(n+1)e^(-n(n+2)t/4)chi_{n/2}(U).
Since |chi_{n/2}(U)|<=n+1, for t>=1,
sup_U |k_t(U)-1| <= A e^(-3t/4),
A=sum_{n>=1}(n+1)^2 exp[-(n(n+2)-3)/4] < infinity.
Consequently for epsilon_t=A e^(-3t/4)<1,
m(t)>=(1-epsilon_t)/(1+epsilon_t).

For 0<R<=R0:=min(1/2,A e^(-3/4)), choose t=(4/3)log(A/R)>=1. Then epsilon_t=R and
P(W_f in B)/Haar(B)
>= exp[-(16/3)R log(A/R)] [(1-R)/(1+R)]^2
>= exp[-(16/3)R log(A/R)-8R]. (WS-1)
The final inequality uses log((1-R)/(1+R))>=-4R for R<=1/2. At R=0, the private link is exactly Haar and the ratio equals 1.

Thus the full-environment positive Wilson vacuum is **quantitatively Haar-stable from below** as R->0, uniformly in the number and strength of all other retained plaquettes. In particular the explicit sufficient inequality
(16/3)R log(A/R)+8R <= log 2
implies half-Haar cap survival, for 0<R<=R0.

This is a true nonperturbative small-ratio theorem, not a perturbative truncation in the other couplings. It is ineffective if the physical Penrose refinement has R=b_g/a_x large. No uniform strong-coupling completed-cage cap bound, infrared spectral gap or continuum mass-gap theorem follows.
