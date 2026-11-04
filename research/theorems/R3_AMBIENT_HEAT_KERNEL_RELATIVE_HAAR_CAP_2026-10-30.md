# R3-IR-518 — Ambient heat-kernel relative Haar-cap comparison

2026-10-30. Finite connected open SU(2) link graph with normalized product Haar, scalar uniformly elliptic inverse-Whitney divergence-form electric H_E=(g2²/2)D* K D with smooth adjoint transport coefficients, and real bounded Wilson magnetic multiplication V with |V|<=B. Assume unique strictly positive ground state Omega with H Omega=E0 Omega. This is a **finite-volume** comparison, not a refinement-uniform bound.

For any t>0 the smooth electric heat kernel k_E(t;U,W) is positive on the connected compact configuration manifold. Define m_t=inf k_E>0, M_t=sup k_E<infinity and r_t=m_t/M_t>0. Positivity and the Feynman–Kac formula (or semigroup domination for scalar bounded real multiplication potentials) give the pointwise kernel sandwich exp(-t B) k_E <= k_H <= exp(t B) k_E. From Omega(U)=exp(t E0) integral k_H(t;U,W) Omega(W)dW and positivity of Omega, for arbitrary U,U' the ratio Omega(U)/Omega(U') >= exp(-2 t B)r_t. This implies a global density lower bound Omega(U)^2 >= exp(-4tB)r_t², since ||Omega||_L2=1 (compare min/max and use normalized Haar). For ANY gauge-invariant event A, including a selected plaquette double-center cap,

Prob_Omega(A)>=exp(-4tB)r_t² Haar(A).

For the fundamental SU2 plaquette on an open disk, Haar(C_delta)=(2/pi)[arccos(1-delta)-(1-delta)sqrt(2delta-delta²)] >=(8/(3pi))delta^(3/2) for delta∈(0,1]. Hence

Prob_Omega(C_delta)>= (8/(3pi)) exp(-4tB) r_t² delta^(3/2).

This is a genuine **relative** shrinking-cap lower bound (positive for all delta>0 at each fixed finite graph) and avoids a conditional fixed-link PDE and additive Haar approximation. Neither electric heat-kernel min/max contrast nor B is known to be refinement/volume-uniform; indeed B=sum b_j grows with volume and physical magnetic scaling. This theorem must not be cited as refinement-uniform, nor as a Yang–Mills continuum mass gap. Its constants can be astronomically small.

Independent validation: research/scripts/validate_ambient_semigroup_cap.py checks a 2-state positivity-preserving semigroup kernel sandwich and computes SU2 rotor Laplacian heat-kernel contrast for t=1,2,4. The rotor contrast is NOT the heat contrast on the 30-link Penrose graph and not a certified rigorous bound. A full M5 heat-kernel estimate is not supplied.

Technical assumptions: scalar connection-free first-order derivations acting on functions (adjoint-transformed derivative COMPONENTS), elliptic principal symbol controlled by K; the corresponding divergence-form operator is positivity preserving. Matrix-valued nonpositive semigroups would require a separate theory. A positive ground state follows from the strong maximum principle on the connected compact manifold for the specified scalar elliptic operator.
