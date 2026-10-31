# R3-IR: exact initial slope of the neighboring Wilson-force autocorrelation

**31 October 2026. Status:** new exact finite-volume Wilson identity; the uniform long-time force-correlation and deleted-face radial-current bounds remain **OPEN**.

## Setting
On a finite original-link SU(2) lattice take the magnetic-deleted Wilson Hamiltonian `H=-sum_k a_k Delta_k + sum_{g != f} b_g(1-p_g)` with `a_k,b_g>0`; the strictly positive normalized ground state is `Omega` and `nu=Omega^2 Haar`. Let `e` be a boundary link of the deleted target `f` that belongs to **one** retained simple face `g`. Each edge occurs once in the oriented face word; inverse occurrences are allowed. Let `X_{e,a}` denote the orthonormal left-invariant SU(2) generators `i sigma_a /2` and `phi_a=X_{e,a}V=-b_g X_{e,a}p_g`. Let `L=sum_k a_k(Delta_k+2 grad_k logOmega · grad_k)` be the ground-state generator and `C_e(t)=sum_a <phi_a,e^{tL}phi_a>_nu`. Define `A_g=sum_{k in boundary g} a_k`.

## Theorem (IC-1): exact SU(2) Hessian contractions
For **every** original-link configuration and for each `k in boundary g`,

`sum_{a,b=1}^3 (X_{k,b} X_{e,a} p_g)^2 = (2+p_g^2)/16`.

For k outside g all such derivatives vanish. In particular `sum_a (X_{e,a}p_g)^2=(1-p_g^2)/4`. Proof: transport each link variation along the cyclic product to the based face holonomy. Each first insertion is an orthogonal adjoint rotation of the Lie-algebra basis. A second insertion on another link yields the 3×3 matrix of mixed character derivatives; by adjoint orthogonality its Frobenius norm is unchanged from the canonical case. At the same link, the ordered second derivatives are `X_b X_a p`. Write `W=p I+i q·sigma`, `p²+|q|²=1`; then the 3×3 second derivative matrix is `-(p delta_ab + epsilon_bac q_c)/4` up to orthogonal rotations and transposes, whose squared Frobenius norm is `(3p²+2|q|²)/16=(p²+2)/16`. The same Frobenius value holds for different links and inverse-oriented occurrences.

## Theorem (IC-2): exact Green–Kubo slope
Reversibility and the Dirichlet form imply

`C_e'(0+) = sum_a <phi_a,L phi_a>_nu = -sum_k a_k sum_{a,b} E_nu[(X_{k,b}phi_a)^2]`.

Substituting IC-1 gives the **exact physical interacting-vacuum identity**

`BOX: C_e'(0+) = -(b_g^2 A_g/16) E_nu[2+p_g²]`.

Together with the previous exact `C_e(0)=(b_g²/4) E_nu[1-p_g²]`, this gives

`-3 b_g² A_g/16 <= C_e'(0+) <= -b_g² A_g/8`.

The negative slope is independent of the unknown score `grad logOmega` **as an explicit formula**, although its expectation of p_g² depends on the vacuum. This is local in the retained face and independent of overall lattice volume given fixed local coefficients. It remains of order b_g² A_g in strong coupling, and supplies **no upper bound on the long-time tail**.

## Why the sign and large initial drop cannot be extended to a decay estimate
The spectral theorem makes `C_e(t)` a positive Laplace mixture. Writing `m= -C_e'(0+)/C_e(0)>0`, Jensen gives the *lower*, not upper, bound `C_e(t)>=C_e(0) exp(-mt)` and hence `S0_e=int_0^infty t C_e(t) dt >= C_e(0)/m²`. This does not control rare slow modes. An arbitrarily small positive spectral atom near zero can preserve the first two derivatives to arbitrary fixed tolerance while making `int t C` arbitrarily large; therefore an initial slope cannot establish the required uniform temporal correlation envelope.

The missing tasks remain a **noncircular long-time force-correlation upper estimate** and an independent passage to center-fiber unweighted positive score variation. No refinement-uniform estimate `sup_f T_(f,h)=o(h^(-1/4))`, connected covariance or continuum mass gap is proved.

## Reproducibility
`verify_wilson_force_slope.py` evaluates all mixed group second derivatives analytically using explicit 2×2 Pauli matrices on 180 random noncommuting words of length 3,4,6 (780 full edge contraction checks) and tests the exact Frobenius and first-gradient identities. Maximum residual `2.220446049250313e-16`. This is algebraic testing, **not vacuum simulation**. Data and SHA-256 manifest accompany this report in Library.