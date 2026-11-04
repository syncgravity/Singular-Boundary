# Multi-Wilson source chain rule and rooted support geometry
Date: 2026-10-30
Status: exact finite-volume operator identities on smooth retained invariant cylinder algebra; uniform interacting vacuum source bounds remain OPEN.

In the simply connected finite SU(2) disk fix a primal maximal tree and complementary face variables. P_f averages the deleted based face holonomy while retaining other based holonomies; Q_f=1-P_f. Let T=sum_e a_e(-Delta_e) in physical generator convention; Gamma_T(F,G)=sum_e a_e <grad_e F,grad_e G>. Let B_1,...,B_N be smooth real residual-conjugation invariant functions of only retained based-face holonomies, and Phi a smooth real function. With F=Phi(B_1,...,B_N), Q_f B_i=0 and Q_f partial_i Phi=0. The diffusion chain rule for positive T and conditional Haar projection imply exactly
-Q_f T F= -sum_i partial_i Phi Q_f(T B_i) + sum_(i,j) partial_ij Phi Q_f Gamma_T(B_i,B_j).
The order-2 sum uses ALL ordered i,j, so off-diagonal pairs count twice. This reduces to the separate retained trace formula when each B_i=p_g because T p_g=(3A_g/4)p_g and Gamma_T(p_g,p_g)=(A_g/4)(1-p_g²), both retained.

For any smooth B_i, B_j with original primal-link supports S_i,S_j, Gamma_T(B_i,B_j)=sum_(e in S_i intersect S_j) a_e <grad_e B_i,grad_e B_j>, hence absolute value at most sum_(intersection) a_e |grad_e B_i||grad_e B_j| and identically zero for disjoint support. This is ORIGINAL LINK support, not intrinsic face-coordinate support. Root-based holonomies may traverse long common maximal-tree paths, so separated plaquettes can have correlated link supports. Conversely tree gauge fixing changes the electric metric, so applying a naive product-face Laplacian is invalid.

More explicit length estimate: for a normalized SU(2) trace of a word B=(1/2)ReTr(U_e1^(sigma1)...U_em^(sigmam)), a derivative with respect to one occurrence has pointwise norm <=sqrt(3)/2 in physical SU(2) generator convention (orthonormal su2 basis with -Delta chi_half=3/4). If edge e occurs n_e times, |grad_e B|<=sqrt(3)n_e/2, leading to
|Gamma_T(B_i,B_j)|<= (3/4) sum_e a_e n_ie n_je.
This count-based estimate is generally conservative and no path-length independence follows when based words revisit many links. For a simple one-face plaquette each incident edge appears once, and the exact sharper p_g formula applies. Gauge-invariant products B_i may be normalized to sup norm 1 but their gradients still depend on word lengths.

The actual projected vacuum P_f Omega may require arbitrarily many joint Wilson invariants, so the finite cylinder chain rule alone does not bound Q_f T P_f Omega, its localized inverse response, polynomial cap probability, or continuum mass gap. Any extension to the full vacuum requires a controlled approximation in the electric graph norm, not just L2 convergence.

NOTE: The earlier trace-only nearest-edge theorem remains correct for its explicitly restricted variables; no assertion of universal nearest-face support is made.
