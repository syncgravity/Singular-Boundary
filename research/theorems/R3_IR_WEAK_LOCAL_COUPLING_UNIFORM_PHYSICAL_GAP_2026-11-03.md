# R3-IR — Local-density weak-coupling uniform physical SU(2) strip gap
Research dated 2026-11-03. **A corollary of published Yarotsky weak-interaction stability, not a new proof of that imported theorem.** Expanded proof, checker, log and checksums: conversation file R3_IR_WEAK_LOCAL_COUPLING_UNIFORM_PHYSICAL_GAP_2026-11-03.zip.

For a finite open straight N-plaquette strip, the original link set is t_i,b_i (1<=i<=N), and v_0,...,v_N, consisting of 3N+1 links. On the **unconstrained** tensor-product Hilbert space H=⊗_e L²(SU2), the physical electric operator is K=∑_e k_e with k_e=-∑_a X_{ea}². Each link has unique constant ground state and lowest positive eigenvalue 3/4.

Partition the links into disjoint *cell sites* C_0={v_0}, C_i={t_i,b_i,v_i}, 1<=i<=N. Then K=∑_{i=0}^N h_i, where each h_i is a nonnegative on-site rotor Hamiltonian with a unique constant product ground state and gap >=3/4. The magnetic term
\[
V_i=-\frac{z_i}{2}\chi_1(U_{\partial p_i})
\]
acts only on C_{i-1}∪C_i, since ∂p_i={t_i,b_i,v_{i-1},v_i}; it is self-adjoint and bounded in operator norm by |z_i| (as |χ_1|<=2). Thus this is a nearest-neighbor bounded perturbation of a gapped product reference **even though each cell Hilbert space is infinite dimensional**.

**Imported published theorem:** Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, arXiv:math-ph/0412040 (2004), published CMP 261 (2006), Theorem 1, and the finite-volume inhomogeneous on-site formulation discussed in Henheik–Teufel–Wessel, *Local stability of ground states in locally gapped and weakly interacting quantum spin systems*, LMP 112, 9 (2022), §2:
https://arxiv.org/html/math-ph/0412040
https://link.springer.com/article/10.1007/s11005-021-01494-y

Their weak finite-range perturbation theory supplies **existential**, volume-independent numbers z_*>0, gamma_*>0 such that |z_i|<z_* for every i gives the full ungauged H_N a unique ground state and spectral gap >=gamma_* for ALL N. Because H_N commutes with the connected semisimple local gauge group SU(2)^vertices, its unique ground eigenspace carries a trivial one-dimensional representation; the ground state is gauge invariant. Restriction to the Gauss-invariant reducing subspace containing the unique ground vector cannot decrease the spectral gap. Thus
\[
\boxed{\operatorname{gap}(H_N|_{\rm physical})\ge\gamma_*>0,\qquad
\sup_i|z_i|<z_*,\quad\text{uniformly for all }N.}
\]
In particular homogeneous z_i=z≠0 is covered when |z|<z_*; unlike the previous total-bond min-max estimate, no N-dependent sum of local interaction strengths occurs.

**Scope and provenance:** This is an application of externally established stability theory, not a novel, independently proven local-density or dressed-residual stability theorem. No numerical z_* or gamma_* is determined. It does NOT assert z=3/4, z=1, an explicit coupling interval, a full 3D spatial lattice theorem, a nontrivial scaling continuum limit, or a physical-unit 4D Yang–Mills mass gap. The local dressing identities and their exact 3-face regression remain separate from this alternative weak-coupling result.

**Verification:** accompanying Python checked 2,505,500 basic finite link-cell incidence/Casimir assertions for N=1..1000; it does not verify the external theorem. Full audit and log in the conversation ZIP. Next: an explicitly quantitative small-coupling threshold and independently verified mapping of all boundary conventions, then 3D lattice and continuum-scaling obligations.