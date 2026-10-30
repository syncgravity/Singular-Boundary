# Three-face small-coupling deleted-vacuum mixed response
Date: 2026-10-30
Status: rigorously identified mixed perturbative coefficient; NONVANISHING NOT YET ESTABLISHED for a concrete Penrose three-rhombus patch.

Finite simply connected three-face SU(2) disk, deleted f, retained g,k, H_-(b_g,b_k)=T+b_g(1-p_g)+b_k(1-p_k), all positive edge coefficients a_e. Physical normalized constant vacuum at b=0, with T>=0, simple zero ground state and spectral gap at fixed regulator. p_g,p_k are real trace half-holonomies. They are mean zero and eigenfunctions of T with eigenvalues lambda_g=(3/4) sum_{boundary g} a_e, lambda_k similarly. Let Q_f be Haar-conditional deleted face projection, which kills p_g,p_k. By analytic nondegenerate perturbation theory in b_g,b_k, the normalized ground state has first-order terms +(b_g/lambda_g)p_g+(b_k/lambda_k)p_k.

At mixed second order, after projection Q_f all scalar energy-correction terms and single-face retained terms vanish, leaving
Q_f Omega_-(b_g,b_k)=b_g b_k(1/lambda_g+1/lambda_k) Q_f T_perp^-1(p_g p_k) + [terms of total order >=3 that involve both b_g and b_k].
This equality should be read as coefficient of b_g*b_k, not as a uniform error for arbitrary disparate b_g,b_k. T_perp^-1 is the inverse on the orthogonal complement of constants; p_g p_k has zero mean in independent based face Haar coordinates, or else subtract its mean before inversion, which Q eliminates. The overall normalization of Omega affects only higher orders after Q because first-order projected terms vanish.

The exact diffusion formula
T(p_g p_k)=(lambda_g+lambda_k)p_gp_k-2 Gamma_T(p_g,p_k)
shows that Q_f T(p_gp_k)=-2 Q_f Gamma_T(p_g,p_k). This produces a concrete geometric diagnostic: compute the shared-link cross gradient in the actual rooted three-face patch, including the transported conjugation factors. HOWEVER, Q_f Gamma_T(p_g,p_k) nonzero is not by itself a proof that Q_f T_perp^-1(p_gp_k) is nonzero; these are different operators. The resolvent coefficient (or a separately proven invariance property) must be evaluated.

For a three-square chain whose retained faces form a tree in dual adjacency, nonzero response is not assumed. A three-rhombus planar patch with a three-cycle in the dual graph around a degree-3 primal vertex is a stronger candidate, but its actual admissibility in the Penrose matching rules and the source must be verified from an embedded patch. Do not assert that an arbitrary three-face connected patch exhibits non-Haar ground state.

No numerical contraction or explicit nonzero three-face coefficient was verified. Hence NO claim of a demonstrated nontrivial three-face deleted vacuum, Penrose cap bound or continuum mass gap.
