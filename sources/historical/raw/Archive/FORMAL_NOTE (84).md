# R3: exact two-step periodic temporal Wilson insertion comparison
Date 2026-10-27. Model: constructed 2×2 quadrilateral spatial disk × a *two-edge* periodic temporal circle. This is NOT a Penrose-extracted patch.

## Incidence certificate
The spatial disk extracted from the previously verified four-prism file has 9 vertices, 12 edges, 4 quadrilateral faces. Taking its cellular product with a two-edge circle gives 18 vertices, 42 edges, 32 faces (8 spatial + 24 temporal), 8 3-cells. The explicit signed incidence matrices in `incidence.npz` obey d1*d2=d2*d3=0, with ranks (17,24,8). The two distinct time-oriented links at each spatial vertex are retained; they should not be collapsed even though the time-circle has two vertices. All 24 temporal faces correspond bijectively to one spatial edge in one of the two time intervals. The verified construction has a central four-prism shared-link loop in both intervals.

## Exact SU(2) transfer kernel
Let X=SU(2)^{12}, H=L²(X), G=SU(2)^9 (spatial vertex gauge group), and P_G its Haar-averaging orthogonal projector. Let f(x)=exp[-sum_{a=1}^4 alpha_a d(W_a(x))], strictly positive and gauge invariant; assume **the same** f at both time slices, with arbitrary nonnegative spatial couplings. Write F for multiplication by f. For each time interval r=1,2 and spatial edge e=1,...,12, with temporal coupling t_{r,e}>=0, define normalized Haar convolution K_{t_{r,e}} on L²(SU2) with kernel w_t(x y^{-1})/q(t), w_t(g)=exp[-t(1-Tr(g)/2)], q(t)=e^{-t}2I_1(t)/t, q(0)=1. Let K_r=tensor_e K_{t_{r,e}}, a positive trace-class operator for any t>=0. SU2 Peter-Weyl yields eigenvalues I_{2j+1}(t)/I_1(t)>=0, including eigenvalue 1 in trivial sector; at t=0 K_0=P_0. Hence K_t>=K_0 in quadratic form sense, and tensor product monotonicity extends to inserting any subset of temporal faces in either step.

Gauge projection P_G commutes with F and all K_r (because each kernel is invariant under common spatial gauge transformation). Integrating temporal links by Haar averaging gives normalized periodic partition function

  Z / (product_{r,e} q(t_{r,e})) = Tr_{H_G}(F K_1 F K_2)

where H_G=P_G H. Equivalently Tr_H(P_G F K_1 F K_2). This expression includes all spatial and temporal Wilson plaquettes and the integration of time-like gauge links. Trace is finite because normalized kernels on compact SU2 are smooth and trace class.

If K_1' >= K_1 and K_2>=0, cyclicity shows

  Tr(F K_1' F K_2)-Tr(F K_1 F K_2)
   = Tr((K_1'-K_1) F K_2 F)>=0.

The same is true for increasing K_2 with K_1 fixed. These arguments hold after gauge restriction. Insert an arbitrary subset Q of 24 temporal faces one by one. Each insertion adds its explicit positive scalar normalization q(gamma_q) and cannot decrease the remaining normalized transfer trace. Therefore

  Z_insert / Z_cavity >= product_{q in Q} q(gamma_q),
  0<= log(Z_cavity/Z_insert) <= sum_{q in Q}[-log q(gamma_q)].

For gamma_q~lambda>=1, -log q(gamma_q)= (3/2)log gamma_q+O(1). Overlaps across time intervals, common spatial links, the four-prism spatial loop, and arbitrary nonnegative pre-existing temporal couplings are all included. For the full inserted Gibbs law nu relative to cavity mu0, E_nu V_Q+D_KL(nu||mu0)= log(Z0/Z1), so both nonnegative terms are bounded by that quantity.

## Sharp scope and obstacle to three or more steps
The proof **requires** two periodic time intervals and identical spatial Boltzmann multiplier F on both slices, no nonpositive or externally imposed gauge-breaking fields, and temporal face insertion only. It does NOT cover open two-interval chains, spatial faces in Q, nonidentical f_0,f_1, or arbitrary Penrose cavities. For periodic n>=3, varying a factor leads to Tr(DeltaK F K_2 F K_3 ... F); the remaining product of positive operators need not itself be positive or Hermitian. Thus the two-step PSD trace argument cannot simply be iterated. More reflection symmetry or a separate correlation inequality would be needed. In particular this construction does not prove the full arbitrary-support R3 estimate or a continuum mass gap.
