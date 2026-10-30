# Four adjacent-plaquette support and quantitative finite-volume gap

2026-10-30. The extracted simply connected eleven-face open Penrose disk with deleted face f=0 contains ten active retained plaquettes C=(1,3,2,4,154,150,11,10,7,8). Exact incidence gives four target-face edges and their unique retained neighbors: edge 0 to face 1, edge 1 to face 2, edge 4 to face 4, edge 13 to face 10.

If the coupling of any one of these four neighbors vanishes, the deleted Hamiltonian's magnetic potential is independent of BOTH the target-shared link and an outer free-boundary link belonging only to that neighbor and the boundary. By positivity of the electric kinetic energy, uniqueness of the finite-volume ground state, and averaging those two link variables, the ground state is constant on them. The corresponding two-link deleted-face fiber transformation holds every retained based-face holonomy fixed, so Q_f Omega(b)=0. The outer edges can be chosen as face1:86, face2:88, face4:372, face10:26. This is an exact all-orders selection rule for the finite disk.

On the complex coupling polydisc |b_g|<r=3/320, the intermediate-normalized ground-state section Psi(b) is analytic and bounded in norm by 2. Therefore the vector-valued analytic function Phi(b)=Q_f Psi(b) is divisible by b_1 b_2 b_4 b_10. In particular all Taylor coefficients with any of these four exponents zero vanish, independently of the exponents of the other six plaquettes. Multivariate Cauchy then implies, for |b_g|<r,

||Phi(b)|| <= 2 [product_(g in {1,2,4,10}) (|b_g|/r)] [product_(g in C) (1-|b_g|/r)^(-1)].

For b_g=t uniformly this becomes ||Q_f Psi(t,...,t)|| <= 2(t/r)^4/(1-t/r)^10. This is an UPPER bound, and does not certify that the equal-coupling response is nonzero. The tenth-order squarefree nonzero coefficient is consistent with this four-neighbor divisibility.

An independent finite-system energy statement: for nonnegative b_g with B=sum_g b_g<3/4, the ordered first two eigenvalues of H=T-sum_g b_g p_g satisfy lambda_1 >=3/4-B by the min-max principle and ||sum b_g p_g||<=B, while lambda_0<=0 since the constant state has expectation zero for every elementary p_g. Therefore the physical finite-volume gap lambda_1-lambda_0 >=3/4-B. In particular throughout the real box 0<=b_g<=r, B<=3/32 and gap >=21/32. This is NOT refinement-uniform, since electric coefficients and scaling change under refinement, nor a continuum Yang-Mills mass-gap result.

The equal-coupling nonvanishing problem remains OPEN: a positive squarefree tenth-order coefficient does not rule out cancellation with repeated-index Taylor monomials when b_g=t.
