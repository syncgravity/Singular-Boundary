# Audit of two uploaded sources: compact Haar benchmarks and a uniform Gaussian rank-update proposal

Date: 27 October 2026. Scope: direct-Z5 Penrose **rhombus disks crossed with three periodic time intervals**, not an icosahedral three-dimensional Penrose complex. This note independently reruns exact group-word and Gaussian diagnostics; it **does not** prove a volume-uniform finite-coupling SU(2) Wilson estimate.

## Source provenance

- `uploaded_exact_compact_certificate.json`, copied from the user's `certificate (15).json`, documents a planar nine-rhombus factorization, a six-face SU(2) prism-sphere character expansion and a separate eight-face example where a linear tangent null vector is not an exact nonlinear retained-action symmetry. The prism character-series rows were re-evaluated independently in `verify_uploaded_benchmarks.py`, giving maximum absolute error `5.56e-17`. Those successes do **not** establish interacting three-dimensional Penrose concentration.
- `original_uploaded_gaussian.py`, copied from the user's `uniform_gaussian.py`, constructs exterior Schur forms for an `eta`-regularized **linear Gaussian** model. It references missing files `/mnt/data/R3_local_conditional_2026_10_27/incidence.npz`, `effective_forms.npz`, and `bianchi_operator.npz`; consequently the uploaded script could not be run as-is. Its mathematical rank-update conclusion is correct in its Gaussian scope, but the exterior-Schur penalty does not include the determinant from integrating the local Gaussian link variables. We independently reconstructed a fully normalized Gaussian calculation using the genuine Penrose incidence in `audit_penrose_gaussian.py`, plus the local Schur comparison in `audit_local_schur.py`.

## A. Rigorous general eta-regularized *Gaussian* rank-update theorem

Let D_R and D_Q be the signed link-by-face boundary-incidence matrices, with Q the inserted faces and |Q|=q. For the three-component **linearized** Gaussian gauge model with quadratic action `(lambda/2)||D_R^T x||^2+(eta/2)||x||^2` on every real link component, eta>0, the exact Gaussian insertion free energy is

\[
 \mathcal G_\eta(\lambda)=\tfrac32\log\det\left[I_q+\lambda D_Q^T(\eta I+\lambda D_RD_R^T)^{-1}D_Q\right].
\]

By the matrix determinant lemma, and `0 <= lambda D_Q^T(eta I+lambda D_RD_R^T)^-1 D_Q <= (lambda/eta)D_Q^T D_Q`, each eigenvalue is at most `lambda||D||^2/eta`. If each face has at most p links and each link meets at most nu faces, `||D||^2 <= p nu`, so

\[
 \boxed{0\le\mathcal G_\eta(\lambda)\le\tfrac32 q\log(1+\lambda p\nu/\eta).}
\]

This is uniform in ambient *Gaussian* volume and valid for arbitrary, overlapping Q, even if the face-incidence rank changes. The `eta I` is an independent artificial mass/regulator, **not** normalized compact SU(2) Haar measure. The estimate may diverge as eta→0 in rank-changing examples. There is no legitimate inference to a finite-lambda compact SU(2) bound from this Gaussian theorem alone.

## B. Stronger local Schur theorem for *Bianchi-fillable* Penrose Q14

Let L denote the 36 links of the original fixed 14 temporal face insertion. Let M be the retained faces touching L together with the 54 retained Bianchi-support faces. For the verified patches, |M|=72 and only 89 exterior links enter M. Write the retained **linear** face map as `Au+Bv` in local variables u and exterior variables v, and the inserted map as `Fu`, since every inserted face uses only links of L. Define exterior quadratic Schur forms by

\[
 v^T C_0 v=\inf_u\|Au+Bv\|^2,
 \qquad v^T C_1 v=\inf_u(\|Au+Bv\|^2+\|Fu\|^2).
\]

The exact nonabelian Bianchi certificate establishes `S_Q(U) <= 44 S_{Afill}(U)` for **all** compact SU(2) link configurations. Differentiating at the identity and recalling `M` contains `Afill` gives the linear inequality

\[
 \|Fu\|^2\le44\|Au+Bv\|^2\quad\text{for all }u,v.
\]

It follows from minimization that

\[
 \boxed{0\preceq C_0\preceq C_1\preceq45 C_0.}
\]

Moreover `rank(C1-C0)<=q=14`. To prove the rank statement, choose a linear minimizer `u0(v)=-A^+ Bv` of the first quadratic. The increment of the second minimum depends on v only through the q-vector `F u0(v)`, since all other terms are optimized over the displacement `u-u0(v)`. Therefore its quadratic form factors through R^q.

For every eta>0 and lambda>=0 the **exterior Schur penalty** in the uploaded script consequently obeys the stronger bound

\[
 \boxed{0\le\tfrac32\log\frac{\det(\eta I+\lambda C_1)}{\det(\eta I+\lambda C_0)}
 \le \tfrac32q\log45=21\log45\approx79.9399.}
\]

The proof uses the eigenvalues of `lambda(eta I+lambda C0)^(-1/2)(C1-C0)(eta I+lambda C0)^(-1/2)`, at most 44, of rank at most q. Unlike the arbitrary-Q Gaussian estimate, this result has **no dependence on eta, lambda, or ambient volume**. In the singular eta→0 limit it has a well-defined relative *pseudodeterminant* interpretation because C0 and C1 share their kernel.

This remains a statement about a **linear Schur exterior energy**, not a compact-Haar exterior Gibbs marginal. It also does not include the Gaussian local-integration determinant factor if one instead defines a fully integrated local partition ratio.

### Exact nested Penrose numerical audit

All four nested direct-Z5 Penrose patches give identical 72-face local retained problem (36 local links and 89 relevant exterior links). The independently computed Schur rank increment is 14 and the Schur free-energy penalty at eta=1 and lambda=300 is `7.35123522969684`, identical at all four radii. The full-link regularized Gaussian determinant penalty is volume-dependent but bounded and modest: `28.61354`, `28.54148`, `28.49803`, `28.47118` for radii 5, 6.5, 8 and 10, respectively. These are **different** Gaussian quantities and must not be conflated.

## C. Exact *compact SU(2)* local coupling interpolation: what would close R3

For any retained compact-Haar Wilson action `S_R(U)=sum_{p in R}d(Wp)` and insertion `S_Q`, the finite-dimensional partition functions satisfy the exact identity

\[
 -\log\frac{Z_{R+Q}(\lambda)}{Z_R(\lambda)}
 =\lambda\int_0^1\mathbb E_{\mu_{R+\tau Q,\lambda}}S_Q\,d\tau
 \le\lambda\mathbb E_{\mu_{R,\lambda}}S_Q.
\]

The inequality holds because `d/dtau E_{R+tau Q} S_Q = -lambda Var_{R+tau Q}(S_Q) <=0`. For the fixed Penrose Q14, the *nonabelian* Bianchi bound therefore implies

\[
 \boxed{0\le-\log(Z_{R+Q}/Z_R)\le44\lambda\mathbb E_{\mu_{R,\lambda}} S_{Afill},\qquad |Afill|=54.}
\]

Consequently, a genuinely volume-uniform **local coupling interpolation estimate**

\[
 \sup_{\Lambda}\lambda\,\mathbb E_{\mu_{R,\lambda}}S_{Afill}
 \le C|Q|(1+\log\lambda)
\]

would indeed imply the original finite-coupling, ambient-uniform R3 insertion bound for this Bianchi-fillable support. The proof of that *last* inequality is **not** contained in the two uploaded sources or established by the Gaussian determinants. In particular, `eta I` must not be silently identified with Haar curvature control, and no global Morse-Bott limit is used in the local comparison above.

## D. What the two files actually contribute

- `certificate (15).json` is sound as a set of finite planar/prism compact-Haar benchmarks; its eight-face tangent example explicitly warns against treating a Gaussian null direction as a nonlinear symmetry.
- `uniform_gaussian.py` proposes a valid **regulated Gaussian exterior-rank theorem**. The upload alone is not executable because three referenced inputs are missing. Its Schur quantity is not the total normalized Gaussian partition ratio and is not a compact Wilson ratio.
- The accompanying independent work strengthens the Gaussian result **for the fixed 14-face Bianchi-fillable Penrose support** to a regulator-free rank-14 exterior Schur bound, and computes both the local and normalized Gaussian rank penalties across four ambient volumes.
- None of the above proves a uniform compact-SU(2) plaquette-moment estimate or justifies commuting the infinite-volume and weak-coupling limits.

## Reproduction

Run `python audit_penrose_gaussian.py`, `python audit_local_schur.py`, `python verify_bianchi.py`, `python verify_uploaded_benchmarks.py` in this directory. All dependencies for those four scripts (including the direct-Z5 geometry generator) are bundled. Numerical scripts check theorems but do not replace their algebraic proofs.
