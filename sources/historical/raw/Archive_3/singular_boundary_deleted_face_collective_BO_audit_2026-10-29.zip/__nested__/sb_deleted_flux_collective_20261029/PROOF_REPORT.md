# The Singular Boundary — Deleted-face collective-mode and center-flux Born–Oppenheimer audit

**Date:** 2026-10-29. **Evidence classification:** exact finite SU(2) nonlinear **deleted-vacuum** Dirichlet/parity theorem, and size-uniform spectral geometry theorems for the **exact harmonic normal operator of the nonlinear Wilson magnetic Hessian**. The longitudinal Schur-complement statement is a theorem for the gauge-reduced **linear/tangent kinetic matrix** only. None of these establishes a polynomial flat-holonomy small-ball probability in the actual magnetic-deleted vacuum, a uniform physical Yang–Mills mass gap, or the original Stage 7/26 operator correspondence.

## 1. Finite SU(2) deleted Hamiltonian and assumptions

Take a finite face-complete simply connected edge-to-edge Penrose rhombus disk with mesh size `h`, a fixed bounded physical domain of positive inradius, and an interior target plaquette `f` separated by a positive physical distance from the outer boundary. Let each rhombus area be in `[c_- h²,c_+ h²]`, each dual-neighbor face-center displacement be at most `C h`, and the number of faces in each Euclidean annulus `[kh,(k+1)h]` be at most `C(k+1)` (consequences of uniformly shape-regular, nonoverlapping rhombi). For uniform constants `0<a_-<=a_e<=a_+`, and `0<beta_-<=beta_g<=beta_+` on `g != f`, define

`H^-_{f,h}=sum_e a_e (-Delta_e) + h^-2 sum_{g != f} beta_g (1-p_g)` on the all-vertex Gauss-invariant SU(2) link Hilbert space, with `p_g=ReTr(W_g)/2`. The true normalized positive ground state is `Omega^-`, its measure is `nu^-=(Omega^-)² dHaar`, and `K^-=H^- - E0^-`.

The previous proof `R3_IR_DELETED_FACE_ADJOINT_FLUX_DIAMAGNETISM_2026-10-29.md` establishes the exact magnetic Hessian normal matrix at a flat-remaining-face background of deleted-face holonomy `U`:

`L_{U,h}=D_beta^(1/2) B_U diag(a_e) B_U^* D_beta^(1/2)`,

where `B_U` is the SU(2)-adjoint-twisted oriented face-edge differential on *remaining* faces. At central U this is the ordinary 3-color weighted face Gram matrix. It is of dimension `3(F-1)`, positive definite on a planar disk. The harmonic transverse frequencies are `omega_j(U)=sqrt(lambda_j(L_{U,h}))/(sqrt(2) h)`.

## 2. Theorem CG-1: collective transverse frequencies are Theta(1), uniformly in flux

**Statement.** If the physical region contains a fixed-radius subdisk disjoint from `f` and the outer boundary, there exist constants `c,C>0` independent of h, the number of faces, and deleted holonomy `U`, such that

`c h² <= lambda_min(L_{U,h}) <= C h²`, hence `sqrt(c/2) <= omega_min(U) <= sqrt(C/2)`.

**Lower bound.** Expand the real quadratic form of `L_{U,h}` as a sum of shared-edge terms `a_e ||sqrt(beta_g) z_g - O_{gg'}sqrt(beta_{g'}) z_{g'}||²` and boundary/missing-face edge terms `a_e beta_g ||z_g||²`. The pointwise reverse triangle inequality gives the discrete diamagnetic estimate `Q_U(z)>=a_- Q_scalar(y)`, with `y_g=sqrt(beta_g)||z_g||`. Since `||y||²>=beta_-||z||²`, we get `lambda_min(L_U)>=a_- beta_- lambda_min(B^- B^-T)`. The remaining-face scalar gram is a principal submatrix of the complete face gram, hence its bottom eigenvalue is no lower than that of the complete matrix. The previously established planar discrete Cheeger/coarea estimate on a bounded physical rhombus disk gives `lambda_min(B B^T)>=c h²`. This is uniform in U and needs no harmonic spectral gap hypothesis.

**Upper bound.** Select a fixed physical subdisk `D_0` of positive radius disjoint from target face f and the outer boundary. The adjoint connection on D_0 is flat and locally gauge-trivial because all other background holonomies are identity and D_0 is simply connected. Choose a nonzero smooth real test function `phi` compactly supported in D_0 and one covariantly constant 3-vector `v`. Put `z_g=beta_g^(-1/2)phi(x_g) v`, zero elsewhere. The numerator is a weighted sum of squared differences between adjacent face centers; each is `O(h²)` and there are `O(h^-2)` edges, so `z^* L_U z<=C`. Meanwhile `||z||²>=c h^-2` by face-area counting. Its Rayleigh quotient is `O(h²)`, uniformly in U. Therefore the smallest harmonic transverse **excitation** does not scale as h^-1: it remains O(1), even though many microscopic modes have frequencies O(h^-1).

**Consequence.** A Born–Oppenheimer reduction that discards *all* transverse excitations on the assumption of a uniform `h^-1` fast spectral gap is invalid as a model-independent derivation. The positive O(h^-1) flux-dependent difference of sums of normal-mode zero-point energies proved previously is fully compatible with individual collective transverse frequencies O(1). This theorem does **not** say that all BO or multiscale adiabatic approaches fail; a controlled low-mode retained reduction remains possible.

## 3. Theorem CG-2: logarithmic longitudinal Schur softening in the tangent kinetic form

At U=I, let the full (nondeleted) scalar face kinetic Gram matrix be `M=B diag(a_e) B^T` (F-by-F, positive definite). Partition its f-th coordinate from all others:

`M=[[A_f, m^T],[m,M_{--}]]`.

The exact Schur complement is

`mu_f := A_f-m^T M_{--}^-1 m = 1/(M^-1)_{ff}`.

It is the coefficient of the squared f-th face momentum after minimizing the **quadratic tangent kinetic form over all transverse face momenta**, for fixed f-th momentum. It is **not** by itself a physical SU(2) eigenvalue or a complete BO effective Hamiltonian.

**Logarithmic variational inequality:** For each interior f with distance to the physical boundary bounded below, there are `c,C>0` independent of h such that

`(M^-1)_{ff} >= c log(R/h)` and `0<mu_f <= C/log(R/h)`.

Indeed for positive M,

`(M^-1)_{ff}=sup_{v!=0} v_f²/(v^T M v)`.

Take a radial discrete logarithmic cutoff `v_g = 1` at distance `<=h` from f, `v_g=log(R/r_g)/log(R/h)` for h<r_g<R, and zero beyond R. Uniform face geometry implies an O(1) number of faces in the first shell and O(k) face centers in the k-th shell. Neighbor differences in shell k are `O(1/[k log(R/h)])`, so its energy is bounded by

`C/log²(R/h) sum_{k<=R/h} 1/k <= C/log(R/h)`.

Since v_f=1, the inverse diagonal is at least c log(R/h). This is a **size-uniform exact inequality** for the linear face Gram on Penrose-class shape-regular rhombus disks. It shows collective kinetic screening of a single deleted-face coordinate in the tangent form, and identifies another obstruction to a naive independent-plaquette longitudinal kinetic approximation.

## 4. Theorem CG-3: exact SU(2) deleted-vacuum class-marginal Dirichlet form and parity bound

Let `p=p_f=(1/2)ReTr(W_f)` be the deleted face's **gauge-invariant** trace and let `rho^-_f` be its true ground-state pushforward probability distribution on [-1,1]. Each of the four incident electric links satisfies `Delta_e p=-(3/4)p` and `|grad_e p|²=(1-p²)/4`, regardless of neighboring interactions. For **every real C¹** function g on [-1,1], the exact interacting ground-state transform implies

`<g(p)Omega^-, K^- g(p)Omega^-> = (A_f/4) int_{-1}^1 (1-p²)|g'(p)|² rho^-_f(dp)`.

This is a fully nonlinear, all-volume, physical-sector identity. It does **not** require the unknown marginal to be Haar or Gaussian. The previously proved physical center-flux unitary sends `p->-p` and fixes `Omega^-`, so `rho^-_f` is exactly even and `E^- p=0`.

Let `v_f = E^-[p²]` (strictly positive for the smooth positive finite-volume ground state). The centered center-odd trial state `p Omega^- / sqrt(v_f)` is physical and obeys the *exact* Rayleigh upper bound

`Delta^-_{center-odd} <= (A_f/4) (1-v_f)/v_f`.

If the deleted marginal instead satisfies a **hypothetical center-concentration estimate** `E^-[1-|p|]<=epsilon<1/2`, then `1-v_f=E(1-p²)<=2epsilon`, `v_f>=1-2epsilon`, and thus

`Delta^-_{center-odd} <= A_f epsilon / [2(1-2epsilon)]`.

So strong center localization **forces** a soft physical center-odd mode in the *deleted* Hamiltonian. This does not imply a soft mode in the original full Hamiltonian after the magnetic term is restored. It shows that the BO longitudinal problem can contain a low-energy center-flux doublet; projecting it away along with transverse modes is not justified. The exact Haar reference has `v_f=1/4`, `A_f=4a`, and the upper bound is the exact one-plaquette electric gap `3a`.

## 5. Numerical and provenance audit

The deterministic script `verify_collective_modes.py` reconstructs the genuine earlier three-face Penrose **spatial** dual Gram (eigenvalues 4-sqrt2,4,4+sqrt2) and separately evaluates growing **square-grid surrogates**, which are *not Penrose regulators*. For an n-by-n square dual disk with uniform a=beta=1 and `h=1/(n+1)`:

`lambda_min(M)=4-4cos(pi/(n+1))`, so `omega_min=sqrt(lambda_min)/(sqrt2 h) -> pi`.

At n=7,15,31,63, the exact full-frequency numerical values are about 3.12145,3.13655,3.14033,3.14128. The central diagonal Green values `G_ff=(M^-1)_ff` increase 0.48897,0.60009,0.71061,0.82097, and the Schur coefficients decrease 2.04511,1.66641,1.40725,1.21807. For n<=31 the missing-central-face transverse frequencies are 3.91190,3.77631,3.66933, again O(1). Direct sparse positive-matrix solvers and symmetric eigenvalue calculations were used, not Monte Carlo. The authentic Penrose Stage 26 archives were not used as incidence inputs; those NPZ files are observables and checkpoints rather than verified full face/edge incidence catalogues.

## 6. Scope and next obligation

**Proved:** size-uniform collective low normal frequencies O(1) despite magnetic coefficients O(h^-2); logarithmic upper bound on effective deleted-coordinate tangent Schur coefficient; exact true nonlinear deleted-vacuum marginal Dirichlet form and center-odd spectral inequality.

**Not proved:** a polynomial lower bound on the true deleted-vacuum small-ball probability `nu^-(1-p<=c h)`, a full nonlinear BO scalar effective potential approximation, uniform magnetic-deletion O(h^-1), fixed-support Wilson–angle covariance, the all-excitation physical mass gap, quartic resolvent, or full continuum reconstruction.

**Revised next proof obligation:** construct a **multichannel** quantum comparison retaining the O(1) collective transverse modes and center-flux parity, or obtain a direct true-vacuum marginal density lower bound from the exact one-dimensional Dirichlet form plus an independently derived conditional force/Harnack estimate. The harmonic flux barrier controls a sum of normal-mode zero-point energies, not the exact deleted-marginal density.
