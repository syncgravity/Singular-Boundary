# R3-IR-417 — Exact two-channel Ward cancellation for every incomplete Wilson cage

2026-10-30. Proven on the genuine finite original-link SU(2) Wilson rhombus disk with free boundary, target plaquette f magnetically deleted. This is an exact cancellation theorem, not a completed-cage sign estimate.

Take a last-neighbor coupling family H(t)=H0+t b_g(1-p_g), with other three neighbors at arbitrary nonnegative couplings. Assume at least one of those other three neighboring couplings vanishes. For a planar rhombus disk with ordinary interior edge incidence, that omitted neighbor h shares an interior edge z with f which is magnetically private for every t. The operator splits H(t)=a_z(-Delta_z)+H_rest(t). The unique positive normalized ground state is independent of z; since W_f traverses z exactly once, W_f is exactly Haar in the vacuum for every real t for which the Hamiltonian family is defined.

Therefore, for every nontrivial SU(2) character chi_j, and in particular spin one, c_1(t)=<chi_1(W_f)>_t=0 IDENTICALLY. Consequently c_1''(0)=0.

Apply the verified R3-IR-416 exact environmental tensor formula at the other private edge x shared by f and g at t=0. Let q be the x quaternion, H0=a_x(-Delta_q)+H_y, omega normalized environment vacuum, D=H_y-E0, S=(D+3a_x/4)^-1 and T=(D+2a_x)^-1. Let p_g=q dot m, chi_1(W_f)=4(q dot n)^2-1, v_i=S(m_i omega), and Z_ij=(m_i v_j+m_j v_i)/2-delta_ij(m dot v)/4.

Because c_1''(0)=0 for b_g!=0, the two *signed, generally nonzero* environmental terms cancel EXACTLY:

boxed:
8 sum_ij <omega,n_i n_j T Z_ij>_y
+
int dy [4(n dot v)^2-|v|^2]
=0.  (WC-1)

Proof: multiply the R3-IR-416 formula
c1''(0)=(4b_g²/3)sum_ij<omega,n_i n_j T Z_ij>+(b_g²/6)int[4(n dot v)^2-|v|²]
by 6/b_g², using c1''(0)=0 from the second independently magnetically private target link z.

No property of the environmental interacting spectral gap is required. The identity holds for arbitrary nonnegative couplings of the other retained faces and all physical finite graph sizes where the stated two private links exist. It supplies an exact unit test for any calculation of the two-channel curvature: separately retaining only one channel, or perturbing a magnetically incomplete cage and obtaining nonzero target spin-one curvature, violates the original-link Wilson constraints.

This is not a positivity proof for a completed four-neighbor cage. When all four neighbor couplings are positive, no second target-private link remains, so the cancellation need not hold. The sign of the complete curvature and its full-coupling cap survival remain OPEN. Nor does the identity establish a continuum mass gap.
