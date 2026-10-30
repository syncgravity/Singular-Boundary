# R3-IR-513 — Zero-local-coupling parity and insufficiency for exponential trial

2026-10-30. Conditional on the previously specified finite gauge-covariant inverse-Whitney kinetic operator and a *unique* strictly positive ground state, with a free boundary edge e of f absent from every other magnetic plaquette.

Center flip Z_e:U_e↦-U_e leaves H(0) invariant because each parallel transporter occurs in adjoint form and Ad(-U)=Ad U. It sends p_f↦-p_f. Ground-state uniqueness and positivity imply Z_e Omega0=Omega0. Therefore the marginal law of p_f under |Omega0|² Haar is symmetric: μ0(dp)=μ0(d(-p)). In particular all odd moments vanish. Its exponential trial partition function and response obey exactly

Z0(t)=<cosh(2t p_f)>_0,
E_(0,t)[p_f]=<p_f sinh(2t p_f)>_0 / <cosh(2t p_f)>_0,
E_(0,t)[1-p_f²]=<(1-p_f²)cosh(2t p_f)>_0 / <cosh(2t p_f)>_0.

But parity and smooth strictly positive density do not imply uniform double-center mass. On SU2 take a normalized positive conjugation-invariant probability density ρ_N(U)∝exp(-N p(U)²) relative to Haar for any N>0. The Haar p law has density (2/π) sqrt(1-p²) dp on [-1,1]. The marginal ρ_N is even and smooth, yet for every fixed δ∈(0,1), its double-center probability μ_N(|p|≥1-δ)→0 as N→∞. Indeed the cap numerator <= exp[-N(1-δ)²] Haar(Cδ) while the normalization denominator is bounded below by a positive multiple of 1/sqrt(N) (integrate |p|<=1/sqrt(N)); hence its cap mass is O(sqrt(N) exp[-N(1-δ)²]).

For δ=.1, numerical quadrature gives cap masses approximately 0.0192829814 (N=1), 1.73422278e-5 (N=10), and 1.75918765e-37 (N=100). These are explicit probability densities, NOT demonstrated ground states of the physical Penrose Hamiltonian. The result refutes only the attempted inference from center parity and smooth positivity to environment-uniform near-center mass, not the desired Penrose center-cap statement.

The exact next requirement is a dynamical estimate on μ0, e.g. lower bounds on μ0(|p|>1-δ), or a different variational/conditional method not relying on them. Gauge invariance alone and the Whitney matrix spectral sandwich do not provide such an estimate. Shrinking center cap and continuum mass gap remain OPEN.
