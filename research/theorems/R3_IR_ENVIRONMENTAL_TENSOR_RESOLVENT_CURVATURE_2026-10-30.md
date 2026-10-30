# R3-IR-416 — Exact interacting-environment tensor-resolvent formula

2026-10-30. Finite-volume SU(2) original-link Wilson result at last-neighbor coupling zero. This is a reduction of the signed problem, not its solution.

Write the shared private SU(2) link as unit quaternion q in S^3. All other links form environment y, with H0=a(-Delta_q)+H_y, vacuum Omega=omega(y), and D=H_y-E0>=0. Let p_g(q,y)=q dot m(y), with m(y) a unit real four-vector determined by the neighboring Wilson word. The target character equals chi_1(W_f)=4(q dot n(y))^2-1, where n(y) is another unit vector determined by the target Wilson word. Normalized Haar integration is uniform measure on S^3.

Use the SU(2) Laplacian convention giving eigenvalues 3/4 for fundamental link coefficients and 2 for spin-one coefficients. Define S=(D+3a/4)^-1, T=(D+2a)^-1, and v_i=S[m_i omega] for i=0,...,3. Then Rp_g Omega=q dot v.

Let Z_ij=(m_i v_j+m_j v_i)/2 -delta_ij(m dot v)/4. It is symmetric and traceless, and Q_1[p_g Rp_g Omega]=sum_ij (q_i q_j-delta_ij/4)Z_ij. The second resolvent acts as T on each coefficient Z_ij.

Normalized S^3 moments give
E[q_i q_j]=delta_ij/4 and
E[q_i q_j q_k q_l]=(delta_ij delta_kl+delta_ik delta_jl+delta_il delta_jk)/24.
In particular,
int chi_1(q dot n)(q dot v)^2 dq = [4(n dot v)^2-|v|^2]/12,
and
int chi_1(q dot n) sum_ij(q_i q_j-delta_ij/4)T Z_ij dq
=(1/3)sum_ij n_i n_j T Z_ij.

Insert these into the exact two-channel curvature identity R3-IR-412, noting that the link-spin-zero normalization term vanishes against chi_1. The full physical Wilson spin-one vacuum curvature is

c1''(0)
= (4 b^2/3) sum_ij <omega, n_i n_j T Z_ij>_y
 + (b^2/6) int dy [4(n dot v)^2-|v|^2].   (ET-1)

Both channels are included. The actual interacting H_y appears unchanged in the resolvents S and T; no environment-freezing or independent-plaquette kinetic approximation is made.

The second term has either sign depending on the alignment of n and v. Although S and T are positive operators, positivity alone does not fix the sign of the first tensor contraction. Therefore ET-1 is an exact environmental reduction but supplies no favorable signed estimate, uniform full-coupling cap survival, or continuum Yang-Mills mass gap.
