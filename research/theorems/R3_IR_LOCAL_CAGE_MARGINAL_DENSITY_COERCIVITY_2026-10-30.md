# R3-IR-439 — Local cage density comparison independent of distant Wilson volume

2026-10-30. Finite original-link SU(2) Wilson disk, deleted target magnetic term, strictly positive unrestricted ground state (automatically Gauss invariant). This is a local marginal theorem, NOT global susceptibility coercivity.

Choose any nonempty fixed subset S of original links, with complement Y. Partition the retained magnetic faces into those incident to at least one link in S (touching) and those disjoint from S. Set B_S=sum_{g touching S} b_g, and a_e>0 for e in S. The exact Hamiltonian, up to irrelevant constants, is H=K_S+H_Y+V_touch, where K_S=sum_{e in S}a_e(-Delta_e), H_Y contains ALL environmental electric and disjoint magnetic interactions, and 0<=V_touch<=2B_S. This partition does not require neighboring plaquettes to be independent.

For t>0 define the SU(2) link heat-kernel ratio m_e(t)=min_{x,x',z} k_{a_e t}(x,z)/k_{a_e t}(x',z)>0, M_S(t)=prod_{e in S}m_e(t), r_S(t)=exp(-2 B_S t) M_S(t). Positive Feynman–Kac kernel comparison of H against K_S+H_Y and the ground-state eigenfunction equation give, for fixed y and every s,s' in SU(2)^S,

Omega(s,y)>=r_S(t) Omega(s',y). (LC-1)

The estimate is independent of all couplings on faces disjoint from S and the number of links in Y. It DOES depend on B_S, a_e for e in S and |S|.

Disintegrate mu=Omega²ds dy=rho_y(s)ds nu(dy). By LC-1, rho_y,max/rho_y,min<=r_S^-2. Since int rho_y ds=1, r_S²<=rho_y(s)<=r_S^-2 for every y and s. Integrating over y shows the genuine S-link marginal density q_S(s) also obeys

r_S²<=q_S(s)<=r_S^-2. (LC-2)

The product Haar weighted SU(2)^S Poincare constant is lambda_S^0=(3/4)min_{e in S}a_e. Density comparison proves for any smooth S-cylinder observable phi(s),

Var_mu(phi)=Var_{q_S}(phi) <=r_S^-2 (lambda_S^0)^-1 sum_{e in S}a_e int|grad_e phi|² dmu. (LC-3)

This is an explicit local marginal coercivity certificate independent of distant Wilson volume. In particular any target-cap multiplier whose holonomy uses solely the selected S links has a local marginal distribution dominated below by r_S² product Haar; since any fixed face holonomy from independent Haar links is Haar, its full physical vacuum cap expectation obeys

<k(W_f)> >=r_S² int_SU2 k(W)dW. (LC-4)

Unlike R3-IR-427's one-link estimate, LC-4 can be applied to any selected local cage; it is not automatically stronger, because B_S and the heat-kernel product may increase as S grows.

CRITICAL LIMITATION. LC-3 holds ONLY for cylinder functions depending on S. It is not a global Poincare inequality for functions of all original links, does not imply control of the full cap source inverse L^(-1), and does not prove an energy bound for the environmental marginal flux of R3-IR-434/438. If local magnetic-to-electric coefficients or the local number of links diverge under refinement, even r_S may vanish. No regulator-uniform half-Haar survival, infrared spectral gap or continuum Yang–Mills mass gap follows.
