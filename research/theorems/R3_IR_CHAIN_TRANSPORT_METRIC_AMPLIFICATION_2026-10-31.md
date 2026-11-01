# R3-IR — Exact multi-link rooted SU(2) transport shear and path-length amplification

**2026-10-31.** Exact path-level original-link metric calculation. Not a general tree–cotree cage Jacobian estimate, interacting-vacuum calculation, or mass-gap result.

## Transport and full Jacobian

Let `(x,y_1,...,y_n)∈SU(2)^(n+1)` and `P=y_n ... y_1`, with electric coefficients `a_x,a_1,...,a_n>0`. Fix `g∈SU(2)` and define `T_g(x,y_1,...,y_n)=(P^(-1)g P x,y_1,...,y_n)`. This Haar-preserving diffeomorphism sends `W=P x` to `g W` and leaves every `y_i` unchanged. The electric quadratic form is `Σ a_i|∇_i F|²` in the standard bi-invariant SU(2) metric.

Use left-trivialized Lie coordinates at each link. The full differential is block-triangular `J=[[R,K_1,...,K_n],[0,I_(3n)]]`, where `R∈SO(3)` and the `K_i` are nonzero in general, despite every `y_i` being fixed by T. Write `g=cos θ I+i sin θ n·σ`, `σ=2|sin θ|`. Each `K_i K_i^T=σ² Π` for the **same rank-two orthogonal projector** Π (the plane perpendicular to the adjoint axis of `P^(-1)gP` in the output x tangent frame). Hence the off-diagonal block K has

`K diag(a_1 I_3,...,a_n I_3) K^T=σ² (Σ_i a_i) Π`.

Let `r=(Σ_i a_i)/a_x`. For `A=diag(a_x I_3,a_1 I_3,...,a_n I_3)`, define the electric-normalized metric defect `N=A^(-1/2)(JAJ^T−A)A^(-1/2)`. The nonzero eigenvalues of N consist of **two copies** of

`λ_±=(rσ² ± sqrt(r²σ⁴+4rσ²))/2`.

All remaining eigenvalues are zero. In particular its largest positive eigenvalue is

**`d_g=(rσ²+sqrt(r²σ⁴+4rσ²))/2`,**

with maximum at an SU(2) adjoint half-turn `σ=2`, namely

**`d_max=2r+2sqrt(r²+r)`**.

With equal electric coefficients, `r=n`, hence `d_max=2n+2sqrt(n²+n)=4n+1+O(1/n)` as n grows. A rooted transport along an arbitrarily long unchanged-link path therefore has unbounded **kinematic** electric-normalized distortion. This disproves a path-length-independent metric *operator-norm* bound for this explicit transport family; it does **not** disprove signed cancellations in the vacuum expectation, nor rule out a better transport choice on the completed cage.

## Proof sketch

In the left Lie frame, variation of any `y_i` induces a left variation `δP P^(-1)=Ad_(y_n...y_(i+1)) ξ_i`, an orthogonal transformation of the input vector. For `z=P^(-1)gP`, variation of `P` gives `δz z^(-1)=Ad_(P^(-1))(Ad_g−I)(δP P^(-1))`, up to a conventional overall sign. Every K_i is thus `(Ad_z−I)` composed with orthogonal rotations, modulo fixed conjugations. Its output range is the same plane Π and `K_iK_i^T=σ²Π`. The defect has upper-left block `Σ_i a_i K_iK_i^T`, off-diagonal blocks `a_i K_i`, and vanishing lower-right block. Weighting by `A^(-1/2)`, orthogonally rotating the `3n` spectator directions and using the rank-two singular value decomposition reduces N to two identical 2×2 blocks `[[rσ², σ sqrt(r)],[σ sqrt(r),0]]`. This gives λ_± exactly.

## Verification and limits

`verify.py` constructs the complete `(3n+3)×(3n+3)` Jacobian by centered-in-group forward finite differences on SU(2) quaternions for `n=1,2,3,5,8`, twelve seeded random configurations per path length, with random positive coefficients. The maximum observed discrepancy between measured and exact positive eigenvalue is below `1e−5`, consistent with step-size `1e−6`; the same common-plane matrix identity and lower diagonal blocks are independently checked. These are geometric checks, **not** Wilson ground-state calculations. No gauge-invariant, completed-cage transport optimization has been carried out.

**OPEN:** cancellation or geometric choice giving small true `⟨Ω,(P_g* H P_g−H)Ω⟩`, unweighted deleted-face signed current, connected covariance and continuum Yang–Mills mass gap.