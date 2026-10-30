# The Singular Boundary — Exact eight-face joint-color Ritz spectrum and strong-field truncation obstruction

**Research date:** 2026-10-29. **Status:** independently constructed, finite-dimensional **exact Galerkin compression of the continuous SU(2) Gauss-invariant Wilson Hamiltonian** on the minimal connected eight-face square-rhombus test complex; precise analytical strong-field no-go for this truncated basis. **It is not a complete eight-face spectral certificate or a Penrose continuum result.**

## 1. Physical geometry and Hilbert space

Take the 3×3 square-rhombus face complex with corner `(0,0)` removed, leaving eight faces, 15 vertices, and 22 links. Let the central face `f=(1,1)` have **zero magnetic coefficient** and retain all seven other positive Wilson plaquette potentials. Impose Gauss invariance at every vertex, with independent SU(2) Haar on links, electric operator `T=sum_e a_e(-Delta_e)`, normalization `-Delta chi_j=j(j+1)chi_j`, and `V=sum_{q!=f}b_q(1-p_q)`, `p_q=(1/2)Tr(W_q)`. There are precisely six shared-edge adjacencies among the seven retained faces, even though their magnetic-link graph is connected and touches all four target edges. Assign unequal positive coefficients `a_e`, `b_q` for a genuinely asymmetric fixture.

By the planar face-coordinate Haar isomorphism, the full physical invariant space contains orthonormal vectors built from products of fundamental SU(2) plaquette characters, together with relative-color spin-network contractions. Kinematic independence of the face holonomies means **Haar orthogonality of the basis**, not independence in the true interacting vacuum.

## 2. A 35-dimensional exact joint-color Galerkin space

For each subset `S` of retained faces with `|S|<=2`, define

`psi_S = product_{q in S} chi_(1/2)(W_q) = product_{q in S} 2p_q`.

They are kinematically orthonormal, giving `1+7+21=29` vectors. For each of the six retained adjacent face pairs `q,r`, form

`D_qr=p_(boundary(q union r))-p_q p_r`,

with orientations so the shared-edge identity is `Gamma_e(p_q,p_r)=a_e D_qr/4`; set `zeta_qr=4D_qr/sqrt(3)`. Conditional SU(2) Haar axes have `E[D_qr|p_q,p_r]=0` and `E[D_qr²]=3/16`. The six `zeta_qr` are orthonormal to every `psi_S` and to each other. Thus `P` projects onto a **physical gauge-invariant 35-dimensional** space including every first pairwise nonclass SU(2) relative-color sector. It is **not** the full electric spectral projector `P_M` of the preceding certification theorem.

For each `S`, the exact compressed electric diagonal is `(3/4)*sum_{q in S}A_q` with `A_q=sum_{e in boundary q}a_e`. For a retained adjacent pair `q,r` sharing edge `e`, the two-face electric sector is closed under the full `T` and has exact matrix

```
         psi_{qr}                   zeta_{qr}
psi_{qr}   lambda               -(sqrt(3)/2)*a_e
zeta_{qr} -(sqrt(3)/2)*a_e       lambda-a_e
```

where `lambda=3(A_q+A_r)/4`, eigenvalues `lambda-3a_e/2` and `lambda+a_e/2`. No other electric compressed off-diagonal terms occur between these 35 states. This follows from SU(2) Clebsch–Gordan `1/2 tensor 1/2 = 0 plus 1` and exact link-gradient integration, not a finite-group approximation.

The compressed potential is particularly simple. Write `B=sum_q b_q`. On the trace-product subspace it is `B*I` minus half the weighted adjacency of the `0,1,2` occupation levels of the seven-cube, where a single plaquette insertion toggles an occupancy. On every relative-color `zeta_qr`, the compressed potential is precisely `B*I`, with no color-to-class matrix element: the required Haar conditional color mean vanishes. These rules specify the **complete exact 35×35 matrix** `PHP` used by the accompanying script.

## 3. Quantitative genuinely asymmetric eight-face Ritz spectrum

For 22 links indexed in a fixed sorted order, set `a_e=0.8+0.07*(i mod 6)+0.013*(i mod 3)`; for seven retained faces in sorted order, set `b_q=b*(0.78+0.09*i)`. This breaks coefficient reflection pairing. The script constructs the exact matrix from the analytical SU(2) rules and diagonalizes it in double precision. Values below are **numerical Ritz diagnostics**, not interval-certified eigenvalues.

| `b` | Ritz `e0` | Ritz `e1` | Ritz gap | Nonclass ground-state weight | Proved upper bound `S_H` for true `E0` |
|---:|---:|---:|---:|---:|---:|
| 1 | 6.707378 | 9.555144 | 2.847766 | 0.00011672 | 15.042168 |
| 4 | 23.021663 | 28.236625 | 5.214961 | 0.00034652 | 30.084336 |
| 16 | 83.871643 | 101.138220 | 17.266578 | 0.00004946 | 60.168672 |
| 64 | 325.880735 | 392.074213 | 66.193478 | 0.00000370 | 120.337345 |
| 256 | 1293.579790 | 1555.632604 | 262.052814 | 0.00000024 | 240.674690 |

The nonzero relative-color weight confirms that the Galerkin matrix is **not** the invalid, fully separable character-only truncation. Nevertheless it is far too small at strong coupling.

## 4. Exact analytic energy-scale no-go, independent of numerical diagonalization

Set `n=7`. Let `A_{<=2}` be the adjacency of the 7-dimensional Boolean hypercube restricted to subset sizes 0,1,2. Permutation symmetry and Perron–Frobenius give its exact top eigenvalue

`lambda_max(A_{<=2})=sqrt(n+2(n-1))=sqrt(19)`.

The three-layer symmetric compression has off-diagonals `sqrt(n)` and `sqrt(2(n-1))`, proving the formula; positivity of adjacency ensures this is the global Perron eigenvalue. Since each nonnegative weighted magnetic adjacency is dominated entrywise by `b_max*A_{<=2}`, while the color block has zero compressed `p_q`, the compressed Hamiltonian obeys the rigorous **form bound**

`e0(PHP) >= B-(sqrt(19)/2)*b_max`, because `T>=0`.

The preceding simultaneous positive **gauge-invariant Wilson trial state** proves for the **actual** nonlinear full physical Hamiltonian

`E0(H) <= S_H=(3/(2sqrt(2)))*sum_q sqrt(A_q*b_q)`.

Write `b_q=b*c_q`, with `c_q=0.78+0.09*i`. For this asymmetric fixture, direct finite sums yield

`B-(sqrt(19)/2)b_max = L*b`, `L=4.473126697263...>0`;

`S_H=C*sqrt(b)`, `C=15.042168124831...`.

Therefore, without using a numerical Ritz eigenvalue,

`e0(PHP)-E0(H) >= L*b-C*sqrt(b) > 0` whenever `b>(C/L)^2=11.3083301194...`.

At `b=16`, the exact inequalities force an energy bias greater than **11.40135**; at `b=64`, greater than **165.94276**; at `b=256`, greater than **904.44574**. These are **rigorously signed bounds derived from exact SU(2) operator inequalities**; the printed decimals are approximations to explicit finite algebraic expressions. Hence this first joint-color subspace **provably fails** to approximate the full strongly coupled ground energy as `h->0` with `b~h^-2`.

## 5. Why this space cannot detect the target cap at any coupling

Every `psi_S` and `zeta_qr` is built from at most two retained plaquette loops. Any product of two such basis functions contains at most four retained plaquette-loop factors. For a nontrivial SU(2) target character `chi_j(W_f)` with integer `j>=1`, integrating any of the four target edges against product Haar is zero unless the adjacent cardinal plaquette loop occurs at least `2j` times, by SU(2) representation orthogonality. That would require at least `8j>=8` retained loop factors; only four are available. Half-integer target characters integrate to zero by the independent target-center flux involution, which leaves every retained-loop basis function invariant. Therefore, for **every** state `xi` in the entire 35-dimensional space,

`<xi,chi_j(W_f)xi>=0` for all nonzero `j`, and the **target group-valued holonomy is exactly Haar under `|xi|²`**.

This is a **basis-selection artifact**, not a physical full-coupling deleted-vacuum Haar theorem. The Galerkin ground state has Haar-order center-cap expectation by construction and could not falsify that conclusion regardless of the actual full-state marginal. A future meaningful test must include joint, connected spin networks with enough support to wind around all four target boundary edges and the three corner connectors.

## 6. Exact necessary class spin-resolution scale

For the **separate product-class subspace only** with each face character index `n=2j` restricted to `0<=n<=N`, SU(2) character fusion gives `p*chi_(n/2)=(chi_((n+1)/2)+chi_((n-1)/2))/2`. The compressed one-face multiplication operator is the `(N+1)` tridiagonal Jacobi matrix with off-diagonals `1/2`, whose largest eigenvalue is exactly

`cos(pi/(N+2))`.

Consequently, with each retained face subject to this class cutoff, the **magnetic** energy is at least

`sum_q b_q*[1-cos(pi/(N+2))]`.

For `b_q=b*c_q` and the full physical gauge-invariant trial `E0<=C*sqrt(b)`, avoiding an energy-scale contradiction requires

`(N+2)^2 >= c*b^(1/2)`, or `N=Omega(b^(1/4))=Omega(h^(-1/2))`.

This necessity is proved for the *individual-plaquette class-character product cutoff*; it is **not** asserted as a sharp theorem for an arbitrary general joint spin-network truncation. Raising this local cutoff alone still misses relative-color and globally connected Wilson sectors, so both local spin resolution and nonlocal color completeness are required.

## 7. Explicit noncertification and exact next gate

The ground Ritz vectors have **strictly nonzero** off-block Hamiltonian residual. The script computes a rigorous **lower-bound formula** for its squared norm from orthonormal omitted trace states (`chi_1(q)`, `chi_1(q)*chi_(1/2)(r)`, and triple fundamental-character products). For `b=16,64,256` the numerically evaluated lower bound on residual norm is respectively approximately `19.2707`, `80.7601`, `326.6455`; already larger than the *Ritz gap*. This is a noncertification diagnostic, not an a posteriori certificate of the true ground state.

Crucially, `P` is a **hand-selected Galerkin subspace, not the full low-electric-energy spectral projection** `P_M` needed for the previously proved Schur-complement enclosure. It would be mathematically invalid to insert this 35×35 Ritz gap into the prior full-operator gap/cap certificate. The actual low-energy eight-face joint spin-network eigenvalue, off-block residual with a complete electric shell, and center-cap lower bound **remain uncomputed**.

**Next gate:** enumerate the full physical joint spin-network space through a growing electric cutoff (including the center-even target-flux sector and all minimal connected color contractions); compute recoupling Hamiltonian and actual off-block shell; produce interval-certified Ritz eigenvalues, center-sector gap, residual and cap observable, then test against refining asymmetric Penrose patches. No continuum mass-gap claim follows from this finite eight-face result.
