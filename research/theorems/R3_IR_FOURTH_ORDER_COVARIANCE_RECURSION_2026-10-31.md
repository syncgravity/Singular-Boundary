# R3-IR — Fourth-order Wilson covariance recursion and parity gate (2026-10-31)

This is an exact finite-volume coupling-expansion identity, not a solved fourth-order SU(2) contraction. Full derivation and verifier are retained in the corresponding Library Proof Audits ZIP.

For K=-sum_e a_e Delta_e, P=sum_(k!=f) b_k p_k, H_lambda=K+lambda(B-P), normalize the positive eigenfunction of K-lambda P by Haar mean 1. Write psi_lambda=sum_n lambda^n u_n, u_0=1, <u_n>=0 (n>0), and eigenvalue e(lambda)=sum_n lambda^n e_n. With R=K_perp^-1, the exact finite-volume recurrence is

e_n=-<P u_(n-1)>, u_n=R[P u_(n-1)+sum_(j=1)^n e_j u_(n-j)].

Define w_n=sum_(j=0)^n u_j u_(n-j), z_2=<w_2>, and m_(i,2)=<r_i w_2>. The exact fourth connected covariance derivative for domino traces r_i,r_j is

N_ij = 24{ <(r_i r_j - delta_ij/4)(w_4-z_2 w_2)> - m_(i,2) m_(j,2) }.

This includes both the normalization correction and connected mean subtraction. Center-parity restricts order-n contributions to symmetric differences of <=n plaquette face boundaries. For two disjoint dominoes with symmetric difference four faces, parity excludes second-order terms but does **not** exclude fourth-order terms. No nonzero fourth-order connected coefficient or spatial range is inferred; a linked-cluster cancellation calculation is still required.

Independent 8-state three-spin reversible Z2 comparator (not SU2 Wilson): c2=0.27450980392156954, c4=-0.2966707619338621, N=-7.12009828641269; finite-coupling residual scales as lambda^6, evenness error under 4.59e-16, recursion residual 1.54e-14. Full reproducible audit in Library /The Singular Boundary/Proof Audits/R3_IR_FOURTH_ORDER_COVARIANCE_RECURSION_2026-10-31.zip.

SU2 fourth-order contractions, physical lambda=1, regulator-uniform connected covariance, signed center current, and continuum mass gap remain open.