# Interval-hull Möbius projection and conditional electric Poisson compatibility

**The Singular Boundary | 2026-11-01 | Finite open SU(2) face chains.**

Let P_J denote conditional product-Haar averaging outside face set J, with P_A P_B=P_{A∩B}. For I=[a,b], a<b, set

H_I=P_[a,b]-P_[a+1,b]-P_[a,b-1]+P_[a+1,b-1],

and H_{a}=P_{a}-P_empty. With E_i=P_{all faces except i} and Q_S=∏_{i∈S}(1-E_i)∏_{i∉S}E_i, one has H_I=∑_{nonempty S:hull(S)=I}Q_S. Thus H_I are mutually orthogonal projections, and ∑_I H_I=1-P_empty. The proof is direct inclusion–exclusion, using commuting Haar conditional expectations.

**Conditional Poisson-commutation theorem.** If the nonnegative self-adjoint electric operator K with constants as kernel commutes with every E_i (sufficient: preserves all tensor Peter–Weyl multi-degree blocks), then [K,H_I]=0. On the centered subspace its reduced inverse also commutes: [K^{-1},H_I]=0. Accordingly the corrected-sign formal score recurrence can be projected as H_I S_1=-K^{-1}H_I V and H_I S_n=K^{-1}H_I ∑_{j=1}^{n-1}Γ(S_j,S_{n-j}) for n≥2. This conditional statement requires a separate audit of the original-link electric operator's exact block invariance under the target weights and boundary conditions.

**Adjacent check.** With a=Re A, b=Re B, r=Re(AB), the previously checked identities K(ab)=11ab/2+r/2, K(r)=15r/2, Γ(a,b)=(ab-r)/4 yield

K^{-1} H_[A,B] Γ(a,b)=ab/22-2r/55.

Both ab and r are individually Haar-centered on A and B. Exact rational verification passes.

**Limitation.** Hull-connected is NOT graph-connected or cumulant-connected. A product of separate Haar-centered observables on distant A,C can live in hull [A,C] even if no Γ link connects them. Thus this decomposition alone does not prove a tree majorant or analytic convergence. The physical original-link commutation audit, true connected-cumulant expansion, all-orders hull decay, interacting λ=1 gap, Penrose signed-current bound, and continuum Yang–Mills mass gap remain open.

**Verification:** Exhaustive finite support enumeration through seven faces and rational adjacent inversion checked in the Library proof package R3_IR_INTERVAL_HULL_PROJECTION_2026-11-01.zip.
