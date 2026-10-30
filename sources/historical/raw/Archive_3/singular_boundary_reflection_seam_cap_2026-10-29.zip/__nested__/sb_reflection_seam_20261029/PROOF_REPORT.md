# The Singular Boundary — Reflection-seam positive-cone theorem for fully connected SU(2) Wilson deletions

**Date:** 2026-10-29. **Research line:** R3 independent reconstruction, finite positive SU(2) electric–magnetic Wilson Hamiltonians. **Classification:** exact finite-volume, full-coupling, Gauss-invariant theorem **under a global reflection symmetry of the finite graph and its coefficients**. It resolves the deleted-face polynomial cap bound on the reflection-symmetric 3×3 nine-face square-rhombus disk and on its four symmetric eight-face, corner-deleted connected patches. **It does not establish the bound for generic asymmetric or Penrose bulk faces, nor a Yang–Mills continuum mass gap.**

## 1. The finite reflection-seam hypotheses

Let a finite planar face-complete, edge-to-edge rhombus complex with free boundary links carry a spatial reflection `r` with these properties:

1. The reflected graph has a **site seam** through vertices but through **no primal links**. The oriented links split into two disjoint sets `E_+` and `E_- = r(E_+)`, exchanged by reflection. Reflection reverses directions where necessary, so their independent product-Haar spaces are naturally identified with the same probability space `X=SU(2)^{E_+}`.
2. Each magnetic face is either paired with a distinct reflected face wholly on the opposite side, or is **cut into two open boundary paths with the same endpoints at seam vertices**, one in each half. The target face `f` is a cut face. Its magnetic coefficient is deleted, `b_f=0`.
3. Electric weights pair exactly across the seam: `a_{r(e)}=a_e>0`; paired magnetic face weights also match, `b_{r(g)}=b_g>=0`. Every seam-cut retained magnetic plaquette has nonnegative weight. There is no extra non-Wilson cross-seam term.

The spatial Wilson Hamiltonian on the full product-link Hilbert space is

`H_f^- = sum_e a_e(-Delta_e) + sum_{g != f} b_g [1 - p_g]`, with `p_g=(1/2) Re Tr W_g`, the positive SU(2) Laplacian normalized by `-Delta chi_(1/2)=3 chi_(1/2)/4`.

The finite-volume ground state `Omega_f^-` is unique, smooth, real and strictly positive by the positivity-improving compact elliptic semigroup; gauge invariance then places it automatically in the physical Gauss-invariant sector.

After identifying both half-link product spaces with `X` by reflection and suitable orientation inversions, the Hamiltonian acts on kernels `Psi(x,y) in L²(X × X)` as

`H_f^- = A_x + A_y + sum_{q in F_cross} b_q [1 - p(P_q(x) P_q(y)^(-1))]`,  (RS-1)

where `A` is the identical self-adjoint local electric-plus-magnetic operator on one half; `P_q(x)` is a **half-plaquette open-path holonomy**, based at two seam vertices; `p(V)=Tr(V)/2`. For `q=f`, the b_f=0 term vanishes. For the target itself, `W_f=P_f(x) P_f(y)^(-1)` in trace up to conjugation/inversion. No approximation is involved.

## 2. RS-1: SU(2) crossing Wilson weight is a positive kernel

For any SU(2) representation `j`, the character kernel

`K_j(x,y)=chi_j(P(x) P(y)^(-1))`

is positive semidefinite in the integral-kernel sense. Indeed, for unitary representation matrices,

`chi_j(P(x)P(y)^(-1))=sum_(a,b) D^j_ab(P(x)) conjugate[D^j_ab(P(y))]`.

In particular, `p(P(x)P(y)^(-1)) = K_(1/2)(x,y)/2` is positive-definite. The pointwise product of positive-definite kernels is positive-definite (Schur product); therefore, for every `s>=0`,

`q_s(x,y)=exp[-s b(1-p(P(x)P(y)^(-1)))]`

is a positive-definite kernel. To see this without Bessel expansions, expand `exp[s b p]=sum_(n>=0) (s b)^n p^n/n!`, whose terms are positive-definite kernels with nonnegative coefficients. Uniform convergence follows from `|p|<=1`. The product over arbitrarily many crossing faces remains positive-definite.

## 3. RS-2: exact positive-Hilbert-Schmidt cone preservation

Identify `L²(X × X)` with Hilbert–Schmidt operators on `L²(X)`, using reflection to identify the negative-half space with the conjugate positive-half space. Let `C` be the closed cone of self-adjoint nonnegative Hilbert–Schmidt kernels.

* The half-side operator `A_x+A_y` generates `K -> S_t K S_t`, with `S_t=exp(-tA)`, preserving `C` for every `t>=0`. Because `A` is electric Laplacian plus bounded local magnetic multiplication, `S_t` additionally has a nonnegative integral kernel (Feynman–Kac), though the latter is not required for cone preservation.
* Every cross-seam magnetic Trotter factor acts by **pointwise multiplication by `q_s(x,y)`**, which preserves `C` by the Schur-product theorem, since `q_s` is a continuous positive-definite kernel.

Trotter product convergence on compact link space establishes

`exp(-t H_f^-) C subset C` for every `t>=0`.  (RS-2)

The constant wavefunction `1(x,y)` is a rank-one positive kernel, and it has nonzero overlap with the unique strictly positive ground state. Therefore, after rescaling, `exp(-t H_f^-) 1` converges in Hilbert–Schmidt norm to a positive multiple of `Omega_f^-`. Closedness of `C` proves:

`Omega_f^- in C`.  (RS-3)

This is a **ground-state** result for the Hamiltonian, not merely a Euclidean equilibrium-measure assertion. It requires the global reflection pairing of couplings and the link-free vertex seam stated in Section 1.

## 4. RS-3: all target Wilson-character expectations are nonnegative

The ground state is also a smooth real nonnegative function of the original link configuration. The **pointwise square** `rho(x,y)=Omega_f^-(x,y)^2` is positive-definite as a kernel because it is the Schur product of the two positive-definite kernels `Omega_f^-` with itself. The target character kernel `K_{j,f}(x,y)=chi_j(P_f(x)P_f(y)^(-1))` is positive-definite by RS-1, so the triple Schur product `rho * K_{j,f}` is again positive-definite. Taking its positive quadratic form on the constant function gives

`c_j(f)=integral_{X×X} Omega_f^-(x,y)^2 chi_j(W_f(x,y)) dxdy >= 0`  (RS-4)

**for every half-integer or integer spin j** and all nonnegative retained magnetic couplings obeying reflection pairing. Independent target-center parity also makes half-odd-integer `c_j=0`, but is not needed to prove the sign. Nonnegative character coefficients are not assumed: they follow from the exact nonlinear, reflection-paired Wilson dynamics.

## 5. RS-4: full-coupling polynomial cap lower bound and deletion-energy corollary

Let `B_a={U: angle(U)<a}`, `0<a<pi/2`, and `H(a)=Haar_SU2(B_a)=(a-sin(2a)/2)/pi`. The prior SU(2) character-convolution minorization is self-contained: let `q=1_{B_(a/2)}`, `k=q*q^vee`, so `0<=k<=H(a/2) 1_{B_a}` and `int k=H(a/2)^2`. By SU(2) Peter–Weyl,

`k=sum_j (int q chi_j)^2/(2j+1) chi_j`, with all nonnegative coefficients. Using RS-4,

`H(a/2) Pr_(Omega_f^-)(W_f in B_a) >= int Omega_f^-² k >= H(a/2)^2`.

Hence the **unconditional full-coupling conclusion within the reflection class** is

`Pr_(Omega_f^-)(W_f in B_a) >= H(a/2)`.  (RS-5)

At the physical deficit `d_f=1-p_f<=h`, let `a_h=arccos(1-h)`. Then

`m_(f,h)^-(d_f<=h) >= H(a_h/2) = [sqrt(2)/(6 pi)+O(h)] h^(3/2)`.  (RS-6)

The bound is independent of the number or strengths of **reflection-paired** retained plaquettes, and is not perturbative. If `a_e in [a_-,a_+]` and `b_f~h^-2`, the previous exact positive-ground-state exponential trial / tilted-cap argument gives

`Delta_f=E_0(H_f^-+b_fd_f)-E_0(H_f^-) <= C h^-1 (1+log(1/h))`.  (RS-7)

This corollary is a deletion-energy estimate for the reflection class, not a continuum mass gap or a generic connected-bulk Penrose bound.

## 6. RS-5: geometries closed by this theorem

On the complete 3×3 square-rhombus disk, reflect `(x,y)->(y,x)` through the main diagonal. The seam crosses **no primal edges**, bisects three faces, including the deleted central face `(1,1)`, and pairs the remaining link/face coefficients. This gives the result for the nine-face fully connected patch at arbitrarily strong Wilson coupling.

Removing exactly one of the four corners still gives a reflection-symmetric **eight-face connected** patch:

- Missing `(0,0)` or `(2,2)`: reflect across the main diagonal.
- Missing `(0,2)` or `(2,0)`: reflect across the anti-diagonal `(x,y)->(3-y,3-x)`.

For each, the theorem holds when the **remaining** electric and magnetic coefficients respect the indicated reflection. These four patches are precisely the four minimal connected activation supports in the preceding 3×3 corner-sewing theorem. The fifth case is the full nine-face patch. Thus all five minimal connected patterns possess a rigorous full-coupling polynomial cap lower bound **in their reflection-symmetric parameter subfamilies**.

The proof does not assert that generic asymmetric coefficients, a Penrose rhombus with a nonsymmetric environment, or a complete refining Penrose disk enjoys such a reflection. The connection to existing Osterwalder–Seiler / Menotti–Pelissetto lattice-gauge reflection positivity is conceptual; RS-2 is a standalone Hamiltonian positive-cone argument under the exact site-seam hypotheses, not a claim that those works establish the present continuum mass gap.

## 7. Verification and open obligations

The executable audit `verify_reflection_seam.py` checks: (i) SU(2) character kernels `chi_j(U_x U_y^-1)` have nonnegative Gram eigenvalues for spins 1/2,1,3/2,2,3,5 at 12 noncommuting SU(2) group points; (ii) the positive-definite crossing Wilson multiplier; (iii) a finite non-Gaussian positive-kernel Trotter iteration with a positivity-preserving half-side kinetic semigroup, and nonnegative response in every tested spin; (iv) 3×3 link/face reflection incidence and no links on the seam for all five connected eight-/nine-face supports; (v) correct SU(2) Haar center-cap prefactor. These are deterministic checks of the algebra and incidence, **not diagonalization of the full many-link physical SU(2) Hamiltonian**. The theorem rests on the exact positive-cone proof above, not on finite sampling.

**PROVED:** RS-1–RS-5 for the stated reflection class; physically full-coupling polynomial cap and `O(h^-1 log(1/h))` magnetic-deletion upper bound in that class.

**OPEN:** extend to asymmetrically weighted or non-reflection-invariant cycle-rich connected Penrose interiors, establish a uniform all-bulk deletion estimate, fixed-support Wilson-angle covariance, full interacting physical mass gap, quartic resolvent, and continuum reconstruction.
