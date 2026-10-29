# R3-IR — Deleted-face collective-mode and Born–Oppenheimer audit (2026-10-29)

**Status:** finite SU(2) *nonlinear deleted-vacuum* marginal Dirichlet/parity theorem, plus exact geometric spectral theorem for the magnetic Hessian normal modes and gauge-reduced tangent kinetic matrix. Not a proof of polynomial flat-holonomy small-ball mass, uniform physical gap, or nonlinear continuum construction. Full report and deterministic sparse-matrix verifier are in the local companion archive singular_boundary_deleted_face_collective_BO_audit_2026-10-29.zip.

## Assumptions and operator

Let a bounded physical, edge-to-edge, shape-regular Penrose rhombus disk have mesh h, full open boundary, all-vertex Gauss invariance, at most two faces per edge, and an interior face f. The remaining-face magnetic coefficient is beta_g/h², beta_g in [beta_-,beta_+], and all link electric coefficients a_e in [a_-,a_+]. The fixed domain has a nonempty physical-radius subdisk away from f and the boundary. Put H^- = sum_e a_e (-Delta_e) + h^-2 sum_{g != f} beta_g (1-p_g), with p_g=ReTr(W_g)/2. Its unique normalized positive physical ground state is Omega^-.

The *exact* nonlinear magnetic Hessian evaluated on configurations with all other plaquettes flat is the 3-color, adjoint-twisted normal matrix L_U = D_beta^(1/2) B_U diag(a_e) B_U^* D_beta^(1/2), indexed by remaining faces and parameterized by deleted-face holonomy U. Its harmonic frequencies are omega_j(U)=sqrt(lambda_j(L_U))/(sqrt(2)h).

## CG-1. A collective transverse harmonic frequency stays O(1), uniformly in flux

Under the above assumptions,
  c h² <= lambda_min(L_U) <= C h²
for constants independent of h, face count, and U. Therefore c'<=omega_min(U)<=C'. In particular the complete transverse system does **not** have a uniform fast gap of order 1/h.

**Lower:** Express the L_U quadratic form as weighted squares of z_g-O_gg' z_g' on shared edges and z_g on boundary/missing-face edges. The reverse triangle inequality gives a discrete diamagnetic comparison with the scalar remaining-face incidence form: Q_U(z)>=a_- Q_scalar(sqrt(beta_g)|z_g|). The scalar form is the principal submatrix of the full positive face Gram, whose lowest eigenvalue is at least c h² by the previously established planar coarea/Cheeger bound. With beta_g>=beta_-, this proves the lower bound.

**Upper:** Choose a fixed-radius disk away from f and the outer boundary. The adjoint transport is gauge-trivial in that simply connected disk. Take an interior smooth nonzero test phi and one covariantly constant color v; put z_g=beta_g^-1/2 phi(x_g)v, zero outside. The numerator is O(1) because neighboring face-center differences are O(h) over O(h^-2) edges, and the denominator is Theta(h^-2). The quotient is <=C h². No Gaussian replacement of the nonlinear ground state is asserted.

This is compatible with the previously proved O(h^-1) flux-dependent *sum of zero-point energies*. A scalar BO projection that discards all transverse excitations as h^-1-fast is unjustified; a controlled multichannel low-mode treatment remains possible.

## CG-2. A deleted-face tangent longitudinal kinetic coefficient softens at least logarithmically

At central U, let M=B diag(a_e)B^T be the full positive scalar face Gram. Separate target f from all remaining faces and define mu_f=M_ff-M_f,-f M_-f,-f^-1 M_-f,f = 1/(M^-1)_ff. This is exactly the Schur-complement coefficient of target face momentum after optimizing the other **quadratic tangent** face momenta. It is not an interacting SU(2) excitation eigenvalue.

The variational formula (M^-1)_ff = sup_{v!=0} v_f²/(v^T Mv) combined with a radial logarithmic cutoff in a fixed physical disk centered at f proves
  (M^-1)_ff >= c log(R/h), hence mu_f<=C/log(R/h).
On the kth annulus, the cutoff differs by O(1/[k log(R/h)]) across each shared edge; O(k) faces occur in that annulus. Summing its squared differences for k<=R/h gives total quadratic energy O(1/log(R/h)). This proof uses only shape regularity, bounded edge weights, face-area bounds and the planar disk topology, so it applies to the Penrose-class spatial regulators. A square-grid surrogate confirms the scaling but is not Penrose simulation evidence.

## CG-3. Exact nonlinear SU(2) deleted-vacuum one-face marginal and center-odd soft-mode criterion

For p=p_f, each incident electric link obeys Delta_e p=-(3/4)p and |grad_e p|²=(1-p²)/4. Let rho_f^- be the **actual nonlinear deleted-vacuum** pushforward distribution of p, and A_f=sum_{e in boundary f}a_e. The exact ground-state transform yields for every real C1 class test g:
  <g(p)Omega^-, (H^--E0^-)g(p)Omega^-> = (A_f/4) int (1-p²)|g'(p)|² rho_f^-(dp).
The exact deleted-face center-flux unitary sends p->-p and fixes the unique positive Omega^-. Thus rho_f^- is even and E^- p=0.

Let v_f=E^-(p²)>0. The physical center-odd trial state p Omega^-/sqrt(v_f) gives
  Delta_center_odd^- <= (A_f/4)(1-v_f)/v_f.
If E^-(1-|p|)<=epsilon<1/2, then v_f>=1-2epsilon and
  Delta_center_odd^- <= A_f epsilon/[2(1-2epsilon)].
Hence **if** the deleted vacuum strongly localizes near the two SU(2) center holonomies, then its lowest center-odd physical excitation softens. This is a conditional statement about the *deleted* Hamiltonian, not a gap assertion for the original full Hamiltonian. The Haar one-face benchmark has v=1/4 and saturates the upper bound at the exact electric gap 3a for equal electric links a.

## Verification and explicit limitations

The deterministic verifier checks the genuine earlier 3-face, 10-edge spatial Penrose dual Gram eigenvalues 4-sqrt(2),4,4+sqrt(2), plus separate n-by-n square-grid surrogates for n=7,15,31,63. There omega_min for the complete scalar matrix approaches pi while the central inverse Green diagonal grows and its Schur coefficient decreases; missing-central-face normal frequencies remain O(1). The square grids are not Penrose regulator simulations and historical Stage 7/26 files were not modified.

**OPEN:** a polynomial near-center small-ball bound for the actual nonlinear deleted vacuum, volume-uniform quantum fiber comparison, fixed-support nonlinear connected covariance, restored-Hamiltonian physical mass gap, nonlinear quartic resolvent, and continuum reconstruction. Next proof task: retain the slow collective modes and center parity in a multichannel comparison or derive a true marginal Harnack/density lower bound independently from the exact class Dirichlet form.