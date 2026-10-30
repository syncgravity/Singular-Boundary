# Temporal plaquettes and cutoff-uniform Penrose Wilson block comparison

**Date:** 2026-10-26. **Scope:** SU(2) finite Wilson-action spacetime rhombus complexes. Distinguish exterior-*conditioned* block laws from unconditioned spatial-slice/quantum-vacuum laws. No full R3/R2 theorem is claimed.

## A. Exact temporal external-field representation (the seven-link block)

Let B contain seven spatial links of two adjacent rhombi in a fixed time slice n. Condition on all spacetime links outside B (including links at n+1 and n-1 and all temporal links). The conditional probability on U_B is

 dλ(U_B|ext)= Z_ext^{-1} exp[t p_f(U_B)+s p_g(U_B)+Σ_{j∈B} (τ_{j,-} p(U_j C_{j,-})+τ_{j,+}p(U_j C_{j,+})) + X_spatial(U_B)]∏_{j∈B}dU_j.

Here the C matrices are exterior-determined SU(2) staples, orientation adjusted; all coefficients nonnegative. On SU(2), p(U)=Re Tr(U)/2 is a real 4D quaternion linear functional. For a single edge the two temporal terms combine *exactly* into h_j p(U_j W_j), with h_j=|τ_{j,-}q_{j,-}+τ_{j,+}q_{j,+}| where q's are unit quaternion staple vectors. They can reinforce to h_j=τ_{j,-}+τ_{j,+}, or cancel to h_j=0. The exterior can choose different preferred edge elements even at the same bare temporal coupling. Thus temporal coupling alone gives no uniform conditional covariance mixing.

## B. Theorem: no cutoff-uniform, exterior-uniform RN comparison for general anisotropic Wilson trajectories

Fix any two-face rhombus disk and a tuple g=(g_j)_{j∈B}∈SU(2)^7 with fused boundary V(g)=-I, possible by choosing a single outer edge g_j=-I and the other edges I. Let the two interior spatial face coefficients both equal T. Choose the exterior time-adjacent spatial links and temporal links so that *both* temporal staples at each j are maximized uniquely by U_j=g_j, at equal coefficient τ=R T. This exterior choice is allowed by the original positive fundamental-plaquette Wilson action: take temporal links I and the corresponding spatial links at adjacent times g_j, with the orientations absorbed in the staple.

The conditional block law becomes exactly

 dλ_{T,R}(U_B)∝exp[T(p_f(U_B)+p_g(U_B))+2RT Σ_{j∈B}p(U_jg_j^{-1})]∏_{j∈B}dU_j.

Let λ_iso,T be the isolated two-face block law proportional to exp[T(p_f+p_g)]∏dU_j, and let μ_{T,R}, μ_iso,T be their *fused boundary holonomy* push-forwards. Choose an open neighborhood N of g small enough that its image under V is contained in F_δ={V∈SU(2): d(V,-I)<δ}, for some fixed δ∈(0,π). For each neighborhood N, compactness and uniqueness of the maximum of L(U)=Σ_jp(U_jg_j^{-1}) at g give κ_N=L(g)-max_{U∉N}L(U)>0. Since the entire spatial-face sum takes values in [-2,2], its variation is at most 4. For R>2/κ_N, the total exponent evaluated at g exceeds the exponent on the complement of N by a positive multiple of T. Standard compact-space Laplace concentration implies λ_{T,R}(N)→1, hence μ_{T,R}(F_δ)→1.

On the other hand the isolated law has p_f,p_g independent and both converge in probability to I at T→∞; therefore V→I, and μ_iso,T(F_δ)→0. Accordingly,

 lim_{T→∞} ||dμ_{T,R}/dμ_iso,T||_{L∞(μ_iso,T)}=∞.

In fact the ratio grows at least exp(cT) for fixed small disjoint neighborhoods, by elementary Laplace bounds (the isolated probability of a neighborhood of -I decays exponentially, and the conditional probability tends to one). This counterexample uses **positive original temporal plaquette interactions only**, not an artificially inserted negative effective fused-loop coupling.

**Scope:** proves no exterior-*uniform* RN comparison for the unrestricted anisotropic family with a sufficiently large fixed ratio τ/t=R. It does **not** prove divergence at the precisely tuned isotropic τ/t ratio or the *unconditioned* full Penrose time-slice law. It refutes attempting to derive such uniformity merely from positivity of temporal Wilson plaquettes, bounded incidence, or two-dimensional face independence.

## C. Exact local source response must include exterior fields

Write the block partition Z_ext(t,s)=∫ exp[t p_f+s p_g+X_ext(U_B)]dU_B. At fixed exterior,

 ∂_t∂_s log Z_ext(t,s)=Cov_{λ(·|ext)}(p_f,p_g),

provided X_ext is independent of t,s in the partial differentiation. The previously derived isolated response ∂_t∂_s log z(√(t²+s²+2ts p(V))) is NOT this covariance if any frozen exterior term touches the integrated link. A sufficient actual-covariance bound, valid for every external environment, is

 |Cov(p_f,p_g|ext)| ≤ [Var(p_f|ext)Var(p_g|ext)]^(1/2),

but there is no volume- or cutoff-uniform decay derived here for those true conditional variances. In fact the example's temporal external field can pin the block around a *frustrated* outer holonomy; its conditional covariance may still decay because strong pinning constrains each edge, which shows RN domination is stronger than needed. The correct source test is a uniform conditional covariance estimate averaged in the complete external Wilson measure, not a worst-case density ratio.

## D. Temporal scaling and noncommuting limits

The anisotropic (2+1) Wilson coefficients depend separately on spatial spacing h and temporal spacing a_t. In a common tree-level normalization, spatial plaquettes scale as β_s∝a_t/(g_3²h²), and temporal plaquettes as β_t∝1/(g_3² a_t), giving β_t/β_s∝(h/a_t)² for regular spacing; geometric face/edge weights alter factors but not the need to specify anisotropy. In the Hamiltonian limit a_t/h→0 the ratio diverges, and exterior-conditioned single-time link alignment is strong. In the isotropic refinement a_t≈h the ratio is of order one and the above counterexample with R≫1 need not apply. Uniformity should be formulated only after specifying the trajectory and (when applicable) nonperturbative anisotropy matching.

The earlier Stage 26 runs use finite time step and fixed beta_ref; they do not produce a simultaneous h→0, a_t→0 quantum continuum family nor certify the desired boundary conditional covariance.

## E. Decision and next acceptable theorem

- **Proved:** exact temporal-staple SU(2) fusion; original-positive-temporal-action exterior counterexample to a universal cutoff-uniform conditional boundary RN constant; exact full conditional covariance-response derivative.
- **Not proved:** failure of *unconditioned* Penrose quantum boundary domination on a fixed isotropic continuum trajectory; cutoff-uniform conditional covariance after exterior averaging; reflected/transfer-matrix Hamiltonian spectral contraction; continuum R3/R2 gap.
- **Next gate:** bound the full exterior-averaged conditional **variance** of physically smeared Wilson operators, with anisotropic scale and boundary observability, potentially via reflection positivity and multilevel/cumulant techniques. This is distinct from a scalar spatial 2D block result and remains unproved.