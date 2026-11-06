# R3 · Fixed-physical-radius smoothing in the linearized cubic SU(2) Wilson flow, and an exact nonlinear plaquette warning

**Audit date:** 2026-11-05 (America/Denver); source comparison: draft PR #70, `R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md` (historical source filename retained).  
**Scope:** exact **flat-field linearization** of 3D spatial SU(2) Wilson gradient flow on oriented finite cubic complexes; periodic cubic Fourier reference; exact **isolated four-link plaquette under free Haar/electric reference**, not the full interacting Wilson vacuum.  
**Status:** finite/linearized theorem and an exact nonlinear countercheck. P0–P5, T0–T5, nontrivial 4D OS construction, physical mass gap and a gravitational UV theory remain **OPEN**. No source archive or historical claim promoted.

## 1. Why this addresses the next target—but does not close it

The prior cubic spatial Wilson-flow result proves `||Hess S_W|| <= 4` and a Jacobian bound `||D Phi_s|| <= exp(4s)` uniform in the total number of links at **fixed lattice flow time** `s`. At a fixed positive physical smoothing scale `tau`, the conventional dimensionless scaling is `s=tau/h^2`, which makes that worst-case nonlinear estimate useless as `h -> 0`. It is not a proof that the actual nonlinear flow or physical continuum observable diverges.

Here we isolate the **flat-field linearization of exactly that finite gradient-flow ODE**. In this sector we prove **mesh-independent bounds at fixed physical flow time**, and we show explicitly how fixed Fourier modes converge at rate `O(h^2)`. We then give a separate, exact **nonlinear isolated-plaquette reference** demonstrating why a linearized bound cannot be extended to the interacting theory without a nonlinear and true-vacuum argument.

The physically used four-dimensional gradient flow of lattice gauge theory is a separate construction; see M. Lüscher, *Properties and uses of the Wilson flow in lattice QCD*, JHEP 08 (2010) 071, DOI `10.1007/JHEP08(2010)071`, and M. Lüscher/P. Weisz, *Perturbative analysis of the gradient flow in non-abelian gauge theories*, JHEP 02 (2011) 051, DOI `10.1007/JHEP02(2011)051`. Their renormalization/flow statements are **not** being adopted as a proof for the present nonperturbative 3D cubic/4D continuum construction. We use only their standard dimensional motivation for positive flow time.

## 2. Exact SU(2) flat-field linearization and cubic cochain geometry

Consider a finite **open** `n x n x n` spatial cubic cell complex of side length one, `h=1/n`. Let `C^0_h`, `C^1_h`, `C^2_h` be real vertex, oriented edge and oriented plaquette cochains; tensor each with the three-dimensional `su(2)` Lie algebra. Let `d0:C^0->C^1`, `d1:C^1->C^2` be oriented incidence matrices satisfying `d1 d0=0`. With the canonical product metric on link Lie algebras, they have the usual transpose adjoints. The exact counts are

```
V=(n+1)^3,
E=3n(n+1)^2,
F=3n^2(n+1),
C=n^3,
V-E+F-C=1.
```

Parametrize a neighborhood of the flat link connection by `U_e=exp(a_e)`, where `a_e` are **dimensionless** Lie-algebra link angles with bi-invariant generator convention `T_j=i sigma_j/2` and `Casimir(j)=j(j+1)`. For `a` sufficiently small,

```
S_W(U) = sum_p [1 - (1/2) tr_fund(U_p)]
       = (1/8) ||d1 a||_ell2^2 + O(||a||^3),
```

where the error is local and the equality of quadratic terms is the only statement used here. Thus the **exact derivative of the full nonlinear Wilson-gradient vector field at the flat connection** is

```
(da/ds)_lin = -(1/4) d1* d1 a .                                  (L1)
```

This is three independent color copies of a positive semidefinite discrete edge operator. Infinitesimal gauge transformations are `a -> a+d0 phi`; since `d1 d0=0`, they are fixed by (L1), and the linearized curvature `d1 a` is unchanged. This uses the same open cubical geometry and plaquette convention as PR #70; it is **not** a new interacting Hamiltonian or a gauge-fixed operator claim for all nonflat connections.

Define a physical curvature cochain `F_h=d1 a/h^2`, a positive *physical* flow time `tau=h^2 s`, and `L_h=d1 d1*/h^2` on plaquette cochains. From the exact singular-value intertwining `d1 exp[-t d1*d1]=exp[-t d1 d1*]d1`,

```
F_h(tau) = exp[-(tau/4)L_h] F_h(0),                              (L2)
```

for every finite open cubic complex, all three Lie-algebra colors, and any real initial **linearized** one-form. No spectral positivity bound or interacting vacuum hypothesis is assumed.

### Theorem 1 (uniform physical-radius smoothing, linearized curvature)

For any `tau>0`, `k>=0`, and each finite open cubical complex, in its natural `h^3`-weighted spatial `ell^2` norm,

```
|| L_h^(k/2) F_h(tau) || <= [2k/(e tau)]^(k/2) ||F_h(0)||,       (L3)
```

where the `k=0` factor is one. In particular,

```
|| F_h(tau) || <= ||F_h(0)||,
|| L_h^(1/2) F_h(tau) || <= sqrt(2/(e tau)) ||F_h(0)||,
|| L_h F_h(tau) || <= 4/(e tau) ||F_h(0)||.                      (L4)
```

**Proof.** `L_h` is a finite-dimensional self-adjoint positive semidefinite operator. Its spectral values `lambda` are nonnegative. The multiplier `lambda^(k/2) exp(-tau lambda/4)` has maximum `[2k/(e tau)]^(k/2)` at `lambda=2k/tau` for `k>0`. The spectral theorem gives (L3) exactly, including zero modes. Multiplying the inner product by the common physical cell factor `h^3` does not change the operator norm. The bound contains **no lattice size, box volume, or bare SU(2) coupling**. It holds because this is a *linearized deterministic spatial gradient flow*; it does not bind the true interacting-vacuum measure. QED.

**Meaning:** The quadratic quantity `h^3||F_h(tau)||_ell2^2` is invariant under infinitesimal lattice gauge transformations and cannot increase with physical flow time. At the **linearized curvature level**, fixed positive physical flow time **does** have the required smoothing normalization. The previous `exp(4 tau/h^2)` estimate is a worst-case nonlinear Lipschitz bound, not a sharp bound on this linearized sector. The theorem neither proves a continuum vacuum nor describes the full nonlinear SU(2) flow.

## 3. Exact periodic cubic Fourier benchmark and an O(h^2) comparison

On a **separate periodic cubic reference**, for integer momentum `k` with `|k_j| <= n/2`, a nonzero transverse edge/curvature Fourier mode has eigenvalue

```
lambda_h(k) = 4 h^(-2) sum_j sin^2(pi k_j h),
```

and its continuum reference is `lambda_0(k)=4 pi^2 |k|^2`. The formula is the exact periodic forward-difference (discrete curl/Hodge) symbol on the **nonzero transverse curvature sector**; longitudinal gauge modes and the zero Fourier curvature modes must not be mistaken for this physical branch.

### Theorem 2 (fixed-mode convergence in physical flow time)

For every `|k_j| <= n/2`,

```
0 <= lambda_0(k)-lambda_h(k)
   <= (4 pi^4/3) h^2 sum_j k_j^4,                              (F1)

|exp[-tau lambda_h(k)/4]-exp[-tau lambda_0(k)/4]|
   <= (tau pi^4/3) h^2 sum_j k_j^4 .                           (F2)
```

Thus each fixed transverse Fourier mode has an actual **nonzero finite physical-time smoothing limit**, with explicit `O(h^2)` control.

**Proof.** The standard inequality `0 <= x^2-sin^2 x <= x^4/3` for `|x|<=pi/2` applied to `x=pi k_j h` gives (F1). The map `u->exp(-tau u/4)` on `u>=0` has Lipschitz constant `tau/4`; combine with (F1) to get (F2). QED.

The periodic Fourier identity is an **independent regulator control**, not an identification of a periodic cube with Penrose geometry, and not a universality theorem for the nonlinear interacting cubic action. For multiple simultaneous Fourier modes or rough fields, additional uniform summability/regularity hypotheses are needed; modewise `O(h^2)` alone does not prove a full interacting quantum continuum.

## 4. Exact nonlinear isolated plaquette: fixed physical flow time can over-concentrate a normalized observable

To audit what Theorem 1 does **not** say, take one isolated open square with four SU(2) links, spatial Wilson action `S=1-(1/2)tr U_p`, and the **actual nonlinear spatial gradient flow** from PR #70. In the product-Haar/free-electric reference state the loop holonomy is exactly Haar. Let `x=(1/2)tr U_p` with Haar density `p(x)=2 sqrt(1-x^2)/pi` and put

```
x_s = [x+tanh(s)]/[1+x tanh(s)],
epsilon = 1-tanh(s) -> 0,
D_epsilon = 1-x_s = epsilon(1-x)/[1+(1-epsilon)x].              (N1)
```

The flat connection `x=+1` attracts every `x>-1` under this isolated nonlinear flow. The exceptional stationary `x=-1` has zero Haar mass. At fixed dimensionless flow time `s`, this construction is gauge invariant and nonlinear; it is **not** the actual interacting 3D Wilson ground state and is **not** a physical fixed-size loop along h-refinement.

### Theorem 3 (exact nonlinear rare-event normalization, isolated Haar control)

As `epsilon -> 0+`,

```
E_Haar[D_epsilon] ~ 3 epsilon,
Var_Haar(x_s) ~ 4 sqrt(2) epsilon^(3/2),
E_Haar[ |grad_SU2 x_s|^2 ] ~ (sqrt(2)/4) epsilon^(1/2),
E_Haar[ |grad_SU2 x_s|^2 ] / Var_Haar(x_s) ~ 1/(16 epsilon).    (N2)
```

Consequently the *variance-normalized* and centered flowed fundamental character `f_s=(x_s-E x_s)/sqrt Var(x_s)` has norm one but converges **to zero in Haar probability and weakly in L^2(Haar)**. For the four-link free-electric Hamiltonian `K=4 alpha C_SU2`, its first spectral moment diverges as

```
-C'_s(0) ~ alpha/(4 epsilon)
         ~ (alpha/8) exp(2s).                                  (N3)
```

For every **fixed** `alpha>0` and fixed **positive** physical quantum time `t>0`, its normalized connected correlation obeys

```
C_s(t) = <f_s, exp(-4 alpha t C_SU2) f_s>_Haar -> 0.           (N4)
```

**Proof.** Set `r=1+x` and note `p(r)=2 sqrt[r(2-r)]/pi` on `[0,2]`. The first integral in (N2) follows by dominated convergence from the integrable function `(1-x)/(1+x)`, whose Haar mean is three. For the second and third, rescale `r=epsilon u` in their exact Haar integrals; the endpoint density is `(2 sqrt2/pi)r^(1/2)[1+o(1)]`. One obtains respectively

```
E D^2 ~ (8 sqrt2/pi) epsilon^(3/2) B(3/2,1/2)
      = 4 sqrt2 epsilon^(3/2),
E |grad x_s|^2 ~ (4 sqrt2/pi) epsilon^(1/2) B(5/2,3/2)
                 = (sqrt2/4) epsilon^(1/2).
```

The squared first moment `(E D)^2=O(epsilon^2)` is lower order than `epsilon^(3/2)`. The SU(2) gradient convention is `|grad x|^2=(1-x^2)/4`; for the four distinct plaquette links, the free electric form is `4 alpha` times the single-holonomy Dirichlet form. This gives (N3). For each `x>-1`, `D_epsilon=O(epsilon)` whereas the standard deviation is `Theta(epsilon^(3/4))`, so `f_s ->0` almost everywhere and in probability; its L² norms are one, hence it converges weakly to zero in L². The positive-time SU(2) heat semigroup `exp(-4 alpha t C_SU2)` is compact on L² for any fixed `t>0`, giving (N4). QED.

**Important:** Theorem 3 is a **nonlinear one-plaquette Haar/free-electric control**: it shows that naive long deterministic flow can collapse an observable while variance normalization merely shifts its spectral mass to very high energies. It is **not** a counterexample to existence of finite positive-flow observables in an interacting 4D continuum, because the spatial model, support and vacuum differ. Nor does it show that SU(2) Yang–Mills lacks a mass gap.

## 5. Nonperturbative work now isolated by these results

Theorem 1 and Theorem 2 are useful **linearized** positive results. They establish physical-radius scaling and a modewise continuum control without either of the two false shortcuts: (a) assuming a generic nonlinear Lipschitz bound remains uniform, or (b) mistaking arbitrarily smoothed readout distributions for physical interacting observables.

To advance the actual cubic weak-coupling program, the next mathematical certificate must address **all** of the following:

1. **Nonlinear physical-radius estimate:** upgrade the linearized `d1 d1*` heat bound to a local, gauge-covariant, *nonlinear* finite 3D/4D flowed-field estimate with constants that do not grow as `s=tau/h²`, under **source-derived** hypotheses compatible with a genuine weak-coupling vacuum. Control unstable/gauge directions, nonlinear curvature recoupling, singular configurations and boundary terms; the spectral theorem alone does not supply this.
2. **Interacting variance and normalized field:** for fixed **physical** support and positive physical flow radius `tau`, prove a lower bound or physically sensible renormalization of the **true interacting** covariance of a gauge-invariant flowed Wilson observable, rather than using the product-Haar reference. The normalized isolated-plaquette counterexample demonstrates why nonzero variance at every finite mesh does not imply a nontrivial limiting state.
3. **Physical time and full Schur form:** construct comparable physical-time centered correlations or energy-dependent variational shorted forms across actual cubic refinements; require a common observable dictionary and summably controlled scale/volume errors. A UV first-moment bound yields spectral tightness only and **cannot exclude small positive energies**.
4. **Full 4D OS existence and gap:** establish reflection positivity, locality/covariance, nontriviality, unique vacuum, dense physical probes, and positive spectral exclusion in common physical units before claiming a 4D YM mass gap.
5. **Quasicrystalline transfer/gravity separately:** no 3D Penrose/coupled-Z5 regulator identification, same-action gauge comparison or physically justified quantum-gravity fluctuation operator is supplied by these cubic controls.

A useful **conditional observable acceptance test** is to define, on matched physical supports, a renormalized family `O_{h,R}(tau)` with (i) `inf Var_nu O_{h,R}>0` (or a common explicitly renormalized normalization), (ii) true interacting covariance and original-link Dirichlet matrix with suitable volume/mesh control, and (iii) a complete long-physical-time/Schur comparison beyond initial moments. None is established here.

## 6. Executable verification and provenance

The companion `research/scripts/verify_physical_radius_linearized_flow.py` constructs actual oriented open 3D cube incidence matrices `d0,d1`, checks `d1 d0=0`, Euler and V/E/F counts, and independently verifies the two commuting heat semigroups and gauge shifts for four spatial meshes `n=2,3,4,6` and two physical times `tau=.025,.1`. It tests the scale-independent gradient and Laplacian bounds against exact sparse matrix exponentials.

For the distinct periodic cubic control, it checks **ten Fourier modes/refinements** against the analytical `O(h^2)` eigenvalue and multiplier bounds. For the nonlinear isolated plaquette, high-accuracy SU(2) Weyl integrals at seven `epsilon` values verify the asymptotic exponents/constants; nine independent finite-character Haar/heat-correlation evaluations check positive-time decay of the variance-normalized observable. These numerical checks do not prove the general theorems; their proofs are the incidence, spectral calculus, exact Fourier symbol and Haar endpoint-integral arguments above.

All source paths and SHA-256 values are in the reproducibility package. Previous PRs #63–#70 remain stacked drafts; this checkpoint will likewise be proposed as a draft against #70. **All six YM continuum gates and the separate gravitational objective remain OPEN.**
