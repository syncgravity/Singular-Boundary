# P2 — Exact full corrected SU(2) two-face electric inverse and second-frequency thermodynamic curvature

**Private audit, 2026-11-04.** Restricted corrected original-link SU(2) open straight-strip model in its unchanged independent-face PW nuclear norm; continuation of P-67/P-68. Full expanded proof, three executed scripts, logs and SHA-256/ZIP verification: \`p2_exact_inverse_fourth_moment_2026-11-04.zip\` preserved in Library \`/The Singular Boundary/Proof Audits/\`. **No high-spin N≈m² complete physical response asymptotic, interacting infinite-volume automorphism, gap, signed Borel reconstruction or four-dimensional continuum YM mass-gap theorem is proved.**

## P-69 — Genuine corrected N=2,m=3 Poisson source: exact complete electric inverse and weighted nuclear response

Use the balanced residual-SU(2)-twirled two-face outer intertwiner, a separately invariant inner \(\chi_3\) inserted at a face, actual original-link electric \(K(X)=D X-2\sum_a (J_1^a\otimes I)X(I\otimes J_2^a)\), and the exact CG output \(\ell=m\pm1=2,4\). The true Poisson-polarized source is
\[
Y_\ell=\tfrac12[(KF)\chi_m+m(m+2)F\chi_m-K(F\chi_m)]_\ell.
\]
The residual Gauss-twirled output is a linear combination of two total-spin projectors \(P_L\), \(L=\ell\pm1\), with coefficient coordinates the **sector traces** \(v_L=\operatorname{tr}(P_LY_\ell)\) (thus \(X=\sum_L v_L P_L/(L+1)\)). Since K is SU(2)-equivariant, its matrix in this two-dimensional invariant trace basis is exact:
\[
K_{\ell=2}^{\rm trace}=
\begin{pmatrix}35/3&2/3\\4/3&28/3\end{pmatrix},
\quad
v_{\ell=2}=\binom{5/4}{-5/2},
\quad
(K_{\ell=2}^{\rm trace})^{-1}v=\binom{10/81}{-185/648};
\]
\[
K_{\ell=4}^{\rm trace}=
\begin{pmatrix}144/5&4/5\\6/5&121/5\end{pmatrix},
\quad
v_{\ell=4}=\binom{7/2}{-9/4},
\quad
(K_{\ell=4}^{\rm trace})^{-1}v=\binom{173/1392}{-23/232}.
\]
The trace-coordinate matrices are not necessarily Euclidean symmetric because spin-sector dimensions differ; the actual corrected K remains HS self-adjoint. For a twirled matrix \(\sum_L t_L P_L/(L+1)\), the **exact nuclear norm** is \(\sum_L|t_L|\). Therefore full-inverse S1 norms are \(265/648\) for \(\ell=2\) and \(311/1392\) for \(\ell=4\). Use the *same* P-44/P-67 first-moment PW weights \(w_\ell=(\ell+1)^2/[4(m+1)^3]\) and the two insertion sites to obtain
\[
\boxed{R_{2,3}=2\Bigl[\frac9{256}\frac{265}{648}
+\frac{25}{256}\frac{311}{1392}\Bigr]
=\frac{38695}{534528}\approx0.07239096922892721.}
\]
This matches the earlier independently computed dense full-original-link physical inverse to numerical precision and now establishes its **exact rational value**. Exact q-Neumann S1 truncation errors:

| q | \(\ell=2\) | \(\ell=4\) |
|---:|---:|---:|
|0|485/7128|265/12528|
|1|1015/78408|251/112752|
|2|1985/862488|595/3044304|
|3|365/862488|673/27398736|
|4|7985/104361048|1699/739765872|
|5|16015/1147971528|5737/19973678544|

The entire proof uses exact rational/radical SymPy generators, CG compression and projector traces: first construct the **genuine** source, then its **full** invariant electric operator (not a scalar comparison), solve and calculate q-errors. This is a complete exact physical source→electric inverse→Schatten response chain **only for N=2,m=3**. At joint N≈m² the spin multiplicities grow and the physical problem remains open.

## P-70 — A uniform *fourth* frequency moment on finite Casimir projection core identifies the limiting second derivative

P-68 established \(C_\infty^{F,G}\in C^2\) and \(|C_\infty''|\le L_FL_G\), but **a uniform second-moment bound does not imply convergence of second moments under weak convergence of spectral measures**. The new theorem closes this *moment passage* for a **dense finite-Casimir-spectral core**, using extra fourth-moment control.

Let \(\mathcal C_{\rm fin}\) be the algebraic span of finite products of individual face Casimir finite-spin spectral projections and identities (each element has finite spatial support W and finite cutoff in all nontrivial factors). Its norm closure is the separable unital protected Casimir-projection algebra from P-64. Fix real \(\lambda\); set
\[
\delta_F=\lambda[V_W,F],\quad V_W=-\tfrac12\sum_{i\in W}\chi_1(U_i).
\]
Because F commutes with all corrected original-link spin generators, \([H_N,F]=\delta_F\) whenever its support is inside the anchor strip. It is bounded and local. For anchored finite-strip ground vector \(\Psi\) and excitation \(h=H-E\ge0\), \(h\Psi=0\), so
\[
hF\Psi=\delta_F\Psi,\qquad h^2F\Psi=[H,\delta_F]\Psi.
\]
For finite-spectral F the local \([C_i,\delta_F]\) is **bounded** (fundamental-character multiplication changes face spin by at most one; F has finite spectral cutoff). The first generator commutators \([R_i^a,\delta_F]\), \([L_i^a,\delta_F]\) are bounded by the Jacobi identity, \([J_i^a,F]=0\), and bounded smooth first derivatives \([J_i^a,V_W]\). Expand each corrected nearest-neighbor electric cross term; the remainder is a finite sum of bounded coefficients times **one** neighboring first-order generator. Hence for a finite constant \(A_{F,\lambda}\) independent of ambient width,
\[
\|[H,\delta_F]\Psi\|^2\le A_{F,\lambda}\Bigl(1+\sum_{i\in W^+}\langle\Psi,C_i\Psi\rangle\Bigr).
\]
Finite anchor patterns intersecting a boundary can be bounded with a maximum over finitely many restricted local factors; the exterior constant Haar vector has zero Casimir energy. The P-55 averaged local kinetic estimate implies
\[
\boxed{\sup_N\int_0^\infty E^4\,d\mu_N^{F,F}(E)<\infty,\quad F\in\mathcal C_{\rm fin}.}
\]
For two core elements, positivity/Cauchy–Schwarz and \(1_{E>M}E^2\le E^4/M^2\) yield a uniform **second-moment tail** \(O_{F,G,\lambda}(M^{-2})\). Therefore the second cross moments are uniformly integrable, unlike what P-68's second-moment estimate alone would ensure.

At finite N, using \(h\Psi=0\):
\[
\int E^2\,d\mu_N^{F,G}
=\frac1N\sum_{\rm anchors}
\langle[H,F]\Psi,[H,G]\Psi\rangle.
\]
Only O(|W_F|+|W_G|) anchor positions meet strip endpoints. Their commutators are uniformly bounded, so the above equals \(\omega_N(\delta_F^*\delta_G)+O_{F,G,\lambda}(N^{-1})\). P-55 local density matrices converge **in trace norm**, so the bounded local expectation tends to \(\omega_\infty(\delta_F^*\delta_G)\). The new fourth-moment tightness lets us pass \(E^2\) to P-64's weak limit, proving
\[
\boxed{\int_0^\infty E^2\,d\mu_\infty^{F,G}(E)
=\omega_\infty(\delta_F^*\delta_G),\qquad
C_\infty^{F,G\,\prime\prime}(0)=-\omega_\infty(\delta_F^*\delta_G).}
\]
For fixed finite support W, both sides are continuous in the Casimir algebra norm by P-68's spectral second-moment bound and bounded local \(\delta_F\); extend by density to the norm-closed separable unital protected algebra. The result identifies the *time curvature* with a positive semidefinite local interacting commutator quadratic form. It **does not** assert \(\delta_{\rm loc}^2G\) is bounded or identify the curvature with \(-\omega(F^*\delta_{\rm loc}^2G)\), nor construct a common interacting infinite-volume automorphism or gap.

**Independent regression:** Actual one-face SU(2) character Jacobi Hamiltonians at real \(\lambda=0.25,1,2,4\) and cutoffs 16,32,64,128 verify the finite spectral second moment equals the *first commutator* quadratic form, the fourth moment equals the squared **double** commutator acting on the finite ground vector, and the high-frequency second-moment tail and numerical second-time derivative bounds. This is verification of the spectral algebra, **not** a substitute for the all-width kinetic-energy proof.

## Mathematical gates still open

**Physical:** assemble true corrected-original-link sources and their spin-projected electric matrices beyond two faces in the joint N≈m² regime; certify normalized nuclear-norm asymptotics.

**Dynamics:** construct a consistent gauge-compatible **interacting infinite-volume automorphism** with an invariant generator core and determine whether the protected spectral kernels extend to it. Uniform gap, clustering, Borel/OS and 4D continuum YM mass gap **OPEN**.