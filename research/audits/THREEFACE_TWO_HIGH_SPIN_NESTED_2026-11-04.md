# Two independently high-spin degrees: nested original-link SU(2) three-face family

**2026-11-04.** Exact *family-level* trace-class estimate in the corrected finite open three-plaquette Gauss-invariant model, using the trace-expansion Peter–Weyl norm. This does **not** prove arbitrary-history nonlinear closure or a mass gap. Independent full Python verifiers and exact-quaternion regressions are preserved in the conversation research ZIP.

Let A,B,C be face holonomies and K=4(C_A+C_B+C_C)+2(D_12+D_23) with D_12=ΣR_A L_B and D_23=ΣR_B L_C. Degree n means SU(2) spin n/2. For independent integers p,q≥1 choose F_pq=χ_p(A)χ_q(B)χ_1(C), G=χ_1(B), with connected histories [1,3] and [2]. With W_l=χ_p(A)χ_l(B)χ_1(C), the exact original-link source is

Γ_K(F_pq,G) = −q W_(q+1)+(q+2) W_(q−1) − (D_12+D_23)(W_(q+1)−W_(q−1))/(q+1).  (1)

This follows from χ_q χ_1 fusion and d[U_(q+1)(x)−U_(q−1)(x)]/dx=2(q+1)U_q(x). The q=1 lower block χ_p(A)χ_1(C) is nonconstant, physically gauge-invariant, disconnected in minimal edge support and **retained** in the connected history.

For each l=q±1, define P=p(p+2), L=l(l+2), b=P+L+3, d=2(p+1)(l+1), and S=(√(PL)+√(3L))/4. The Fourier coefficient matrix M_l obeys the exact physical *superoperator* equation

(b I+2𝒟_12+2𝒟_23) M_l = α_l I_d + β_l(𝒟_12+𝒟_23) I_d,

with (α_+,β_+)=(-q,-1/(q+1)), (α_−,β_−)=(q+2,1/(q+1)). On trace-expansion matrices 𝒟_12(X)=−Σ J_p^a X J_l^a and 𝒟_23(X)=−Σ J_l^a X J_1^a, with tensor factors understood. These are **superoperators**, not arbitrary commuting output matrices. Schatten row-column Cauchy yields ∥𝒟_12X∥_1≤√(PL)∥X∥_1/4 and ∥𝒟_23X∥_1≤√(3L)∥X∥_1/4. Since S≤(P+2L+3)/8≤b/4, the Neumann inverse exists in trace norm and

∥M_l∥_1 ≤ d [|α_l|+S/(q+1)]/(b−2S).  (2)

For local-first L^(1) of F and L^(2) of G, the exact input norms are d_in²(1+max(p,q))e^(3κ+σ(p+q+1)) and 16e^(κ+σ), d_in=2(p+1)(q+1). The normalized response R_pq has the following direct bound:

R_pq ≤ e^(−κ)/16 Σ_(l=q±1) [(l+1)/(q+1)]² [(1+max(p,l))/(1+max(p,q))] e^[σ(l−q−1)] [|α_l|+S_l/(q+1)]/(b_l−2S_l).  (3)

**Theorem:** for all p,q≥1, κ>0, σ≥0,

**0 < R_pq(σ,κ) ≤ (105/32) e^(−κ)/(p+q).**  (4)

**Proof:** L≥q²−1 gives b≥(p+q)²/2; b−2S≥b/2≥(p+q)²/4. Also |α_l|≤3q, S_l/(q+1)≤(q+2)(p+3)/[4(q+1)]≤3p/2. Hence the last quotient of (3) is at most 12/(p+q). Dimension-squared and max-spin-moment ratios have product at most 27/8 in upper channel and 1 in lower channel. Both e^[σ(l−q−1)]≤1. Sum: R≤e^(−κ)(27/8+1)*12/[16(p+q)]=105 e^(−κ)/[32(p+q)]. No finite-degree extrapolation enters this argument.

**Reproducibility and scope:** Direct quaternion source identities were checked at (p,q)=(2,1),(2,2),(3,2),(3,3) with both original shared links; exact Chebyshev derivative tests in 14 degrees; 50 finite Fourier inverse residual/trace checks and 25 ratio checks for p,q=1,..,5. The portable scripts and logs are in the conversation research ZIP named threeface_two_highspin_audit_2026-11-04.zip, including SHA256. The finite checks are regressions; equation (4) is algebraic.

**Remaining:** G is still a *fundamental* singleton. Independent arbitrary spin in G, simultaneous high-spin *inputs*, all nested histories and supports, physical interacting coupling, 3D regulator and continuum are unproved. This family does not establish the general coefficientwise tame theorem or the conditional Borel-disk hypothesis. Next target: G=χ_r(B) with r independently unbounded and all low-energy fusion channels retained.

Related prior [one-high-spin three-face family](THREEFACE_ALL_SPIN_NESTED_2026-11-04.md).