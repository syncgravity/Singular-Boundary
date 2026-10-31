# R3-IR-563 — Gauge covariance and Gauss-law domain for the six Penrose-prism candidate operators (2026-10-31)

## Scope

Constructed and executed a six-approximant (M=5,7,9,11,13,15) numerical audit of finite vertex gauge transformations on the complete oriented 3D graph, matching the R3-IR-560 edge mass and R3-IR-561 plaquettes. THIS DOES NOT COMPUTE AN INTERACTING SPECTRUM OR PROVE A CONTINUUM GAP.

For oriented edge e=(s(e),t(e)), let U'_e=g_s U_e g_t^-1. For the rooted spanning tree based at r, define path holonomy V_s from r to source s. Its exact transformation is V'_s=g_r V_s g_s^-1. The left electric Lie generator X_e transforms as X'_e=Ad(g_s)X_e under pushforward of the configuration. Hence the rooted field Y_e=Ad(V_s)X_e transforms by a COMMON Ad(g_r) for every link. Consequently with any *fixed symmetric scalar* K=M1^-1,

 sum_e,e' K_ee' Y_e·Y_e'

is gauge invariant, even with dense off-diagonal K. Each plaquette holonomy transforms by conjugation at its starting vertex, so p_f=Tr(U_f)/2 is gauge invariant. This is exact algebra, independently of the Monte Carlo numerical check.

The quantum gauge group action is (T_g ψ)(U)=ψ(g^-1·U). A correctly defined self-adjoint electric quadratic operator from the rooted *first-order derivations* with respect to product Haar measure, e.g. the Friedrichs operator associated to the manifestly invariant positive form

 Q_E[ψ]=(g²/2)∫ Σ_ee' K_ee' (D_e ψ)·overline{D_e' ψ} dμ,

commutes with each T_g (assumes the D_e derivations are gauge-covariant and the induced Haar change of variables is used). The Wilson multiplication operator similarly commutes. Therefore the gauge-invariant subspace H_phys={ψ:T_gψ=ψ for all g∈SU2^V}, equivalently the joint kernel of the corresponding vertex Gauss generators on smooth vectors, is reducing/invariant under the closed form and Hamiltonian. This is a formal functional-analytic construction; **the physical projector or constrained eigenspectrum has NOT yet been explicitly built or solved**.

The exact infinitesimal vertex Gauss constraint is G_v^a=Σ_{e:s(e)=v} L_e^a−Σ_{e:t(e)=v} R_e^a (up to a consistent conventional sign for Lie algebra generators). For a gauge invariant smooth wavefunction, G_v^a ψ=0. The left/right electric fields commute on distinct Lie algebra actions as required; edge-frame parallel transport must be handled in cross terms. The gauge-covariant *quadratic form* is the safe operator definition; naive untransported mixed derivatives K_ee' X_e·X_e' would NOT generally be gauge invariant and are not interchangeable with the audited form. An operator defined by a nondivergence sum without the appropriate adjoint/ordering is also not automatically self-adjoint.

## Executed numerical checks

Random deterministic seed 20261031: independently sampled SU2 link holonomies, vertex transformations, and Lie-algebra electric vectors for each model. Tested all Wilson plaquettes, the tree-transport equivariance for all link sources, and the full positive inverse of archived candidate mass M1. All passed tolerance 1e-11:

|M|vertices|links|plaquettes|
|---:|---:|---:|---:|
|5|48|98|65|
|7|46|95|64|
|9|48|98|65|
|11|46|95|64|
|13|46|95|64|
|15|46|95|64|

Maximum observed Wilson trace discrepancy ~1.34e-15, rooted adjoint field discrepancy ~5.38e-15, relative electric quadratic discrepancy ~2.89e-15. A finite random check supports implementation integrity but is not a proof of all functional-analytic operator assertions; those follow from the stated exact transformation laws.

## Remaining obligations

1. Explicit finite-dimensional *gauge-invariant* spin-network truncation with a controlled cut-off, respecting link representation tensor-product and vertex intertwiners, then test the strong Wilson regime.
2. Show convergence in truncation of the gauge-constrained low spectrum at each fixed finite graph.
3. Derive the physical normalization/renormalization of the candidate action. No continuum spectral gap follows from covariance.
4. Revisit whether the original historical 11-face Whitney operator is related to this candidate family.

Executable audit: research/scripts/audit_prism_gauge_covariance.py; also preserved in ChatGPT Library /The Singular Boundary/Source. The original binary candidate matrices are Library-only.
