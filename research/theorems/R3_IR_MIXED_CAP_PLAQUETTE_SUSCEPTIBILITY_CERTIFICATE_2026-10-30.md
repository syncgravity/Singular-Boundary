# R3-IR-431 — Mixed cap–plaquette susceptibility inequality

2026-10-30. Exact original-link SU(2) Wilson finite-volume response estimate. This is a conditional control of cap transport, not a favorable sign theorem.

Fix a deleted target face f, a neighboring face g and the coupling family H(t)=H0+t b_g(1-p_g), with all other Wilson interactions retained. Let Omega_t be its unique real normalized positive ground state, Q_t=1-|Omega_t><Omega_t| and R_t=Q_t(H(t)-E(t))^(-1)Q_t. For the bounded positive cap multiplier O=k_a(W_f), put F(t)=<O>_t and P(t)=<p_g>_t.

Analytic eigenvector perturbation gives
F'(t)=2 b_g <Q_t O Omega_t,R_t Q_t p_g Omega_t>.
The ordinary neighboring source response (R3-IR-430) is
P'(t)=2b_g <Q_t p_g Omega_t,R_t Q_t p_g Omega_t> >=0.

Define cap susceptibility A(t)=<Q_t O Omega_t,R_t Q_t O Omega_t> >=0. Cauchy–Schwarz in the positive reduced-resolvent seminorm proves the full-coupling mixed response bound

|F'(t)|² <= 2b_g A(t) P'(t). (MS-1)

Integrating t from 0 to 1 gives the signed-agnostic transport certificate

F(1)>=F(0)-sqrt(2b_g [int_0^1 A(t)dt] [P(1)-P(0)]). (MS-2)

At the last-neighbor-zero boundary the target is Haar by a private link, so F(0)=a0=int_SU2 k_a. Also P(0)=0 by center-flux symmetry. Since 0<=P(1)<=1, a sufficient quantitative condition for the desired half-Haar survival F(1)>=a0/2 is

2b_g int_0^1 A(t)dt * P(1) <= a0²/4. (MS-3)

No bound on the cap susceptibility integral that makes MS-3 hold under physical Penrose refinement has been proved. Positivity and monotonicity of P(t) alone do not determine the sign of the mixed response F'(t), and (MS-1) is not a positive association or cap-biased cosh ordering theorem.

The result uses genuine normalized physical ground states at all t, and no assumed interacting mass gap. It is a precise sufficient control criterion, not a completed proof of uniform cap survival, infrared spectral mass gap, or continuum Yang–Mills reconstruction.
