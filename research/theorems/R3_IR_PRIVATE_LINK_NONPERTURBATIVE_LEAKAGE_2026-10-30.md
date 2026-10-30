# R3-IR-395: Nonperturbative single-edge Wilson leakage

Date: 2026-10-30. Finite-volume theorem, NOT a regulator-uniform cap bound.

For a deleted target face f, pick a neighboring face g sharing edge e, with all other Wilson couplings held fixed. On original link coordinates x=U_e and environment y, the genuine SU(2) Hamiltonian at neighbor coupling t is

H(t)=a_e(-Delta_x)+H_y+t b_g(1-p_g(x,y)).

At t=0 the edge x is absent from the magnetic potential. Let E_y be the lowest energy of H_y and omega_y its strictly positive normalized ground state. For each t>=0, the full positive, physical Gauss-invariant vacuum Omega_t minimizes H(t). Let P_e be x-Haar averaging, and eta_t=||(1-P_e)Omega_t||_2^2.

**Theorem.** For all t>=0,

0 <= E(t)-E_y <= t b_g,
a_e ||grad_x Omega_t||_2^2 <= t b_g,
eta_t <= min(1, 4t b_g/(3a_e)).

Proof. H_y-E_y and -Delta_x are nonnegative, as is t b_g(1-p_g). The physical trial state 1_x omega_y has magnetic expectation t b_g because Haar integral of p_g over x vanishes. Therefore E(t)<=E_y+t b_g, while E(t)>=E_y+a_e||grad_x Omega_t||^2. SU(2) link Poincare has its first nonconstant eigenvalue 3/4; apply it fiberwise.

For any positive target cap observable O=k_a(W_f) with 0<=O<=nu_a and x-Haar average alpha_a^2, write Omega_t=phi+xi with phi=P_e Omega_t. Then the exact Haar baseline and Cauchy-Schwarz yield

F_a(t)=<Omega_t,O Omega_t> >= alpha_a^2(1-eta_t)-2 nu_a sqrt(eta_t(1-eta_t)).

Consequently eta_t<=min(1/4,alpha_a^4/(256 nu_a^2)) guarantees F_a(t)>=alpha_a^2/2 (with slack). This is a rigorously gap-free, all-coupling estimate; it is ineffective at b_g proportional to h^-2, a_e order one, target cap radius proportional to sqrt(h), because it requires eta=O(h^3).

This uses only original-link Wilson geometry, trial-state variational comparison, and kinematical link Poincare. It DOES NOT show sign of the cap-neighbor cross-source susceptibility, nor full-coupling cap survival, nor a Yang-Mills continuum gap. It extends archived R3-IR-394 at the private-link coupling hyperplane.