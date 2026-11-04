# R3-IR — Repository synthesis and exact 3D periodic curl spectrum (2026-11-04)

**Status:** exact finite-dimensional theorem for periodic cubic original-link incidence and the **quadratic tangent** SU(2) magnetic model. NOT a nonlinear interacting spectral-gap proof or continuum Yang–Mills mass gap. Expanded proof, incidence checker and SHA256 manifest: conversation archive R3_REPOSITORY_REVIEW_3D_CURL_SPECTRUM_2026-11-04.zip.

## Earlier repository insights and their scope

Reviewed the theorem directory (537 items) and selected earlier documents: R3_IR_MULTIFACE_STRONG_FIELD_DUAL_LAPLACIAN_2026-10-28.md (planar dual Dirichlet Laplacian and fixed-patch strong magnetic oscillator), R3_IR_GAUGE_REDUCED_FLAT_HESSIAN_CHEEGER_2026-10-28.md (gauge quotient of magnetic Hessian), R3_IR_MANY_FACE_STRONG_FIELD_AND_SIGNED_GAUSSIAN_DYNAMICS_2026-10-28.md and R3_IR_VOLUME_UNIFORM_MAGNETIC_QUARTIC_REMAINDER_2026-10-28.md (Gaussian/nonlinear volume-limit distinction), R3_IR_RENORMALIZED_WILSON_REFERENCE_2026-10-28.md and R3_IR_TWO_SCALE_PHYSICAL_SPECTRAL_BAND_2026-10-28.md (source survival and physical-energy normalization), R3_IR_LINKED_CLUSTER_SUBTRACTION_PHYSICAL_OBSTRUCTION_2026-11-03.md (physical disconnected-channel retention), and R3_IR_3D_QUANTITATIVE_THRESHOLD_AND_CONTINUUM_SCALING_AUDIT_2026-11-04.md (electric perturbation regime mismatch). The survey is targeted, not certification of every repository theorem.

## Exact periodic cubic discrete curl theorem

On an L×L×L periodic lattice, L≥2, orient all edges and face boundaries. There are E=F=3L³ edges/faces and V=L³ vertices. Define B:R^E→R^F by
\[
(BA)_{x,ij}=A_{x,i}+A_{x+e_i,j}-A_{x+e_j,i}-A_{x,j}.
\]
For reciprocal momentum \(k_j=2\pi n_j/L\), the discrete Fourier curl symbol has spectrum
\[
\operatorname{spec}(B(k)^*B(k))=\{0,\lambda(k),\lambda(k)\},\quad
\lambda(k)=4\sum_{j=1}^3\sin^2(k_j/2).
\]
At k=0 all three eigenvalues vanish. Hence
\[
\boxed{\operatorname{rank}B=2(L^3-1),\quad
\dim\ker B=L^3+2,\quad
\dim\ker B^T=L^3+2,}
\]
and
\[
\boxed{\lambda_{\min}^+(BB^T)=4\sin^2(\pi/L).}
\]
Here ker B consists of L³−1 vertex-gauge gradients plus 3 harmonic 1-cochains; ker B^T consists of L³−1 independent Bianchi cube-boundary relations plus 3 harmonic 2-cochains. Contrast planar disk theorem: on 3D periodic full face space BB^T is NOT positive definite.

## Strong-magnetic quadratic consequence, not nonlinear spectrum

For flat-connection tangent expansion of the original-link electric plus magnetic Hamiltonian H=a_e K+b Σ_f(1−p_f), nonzero transverse modes have oscillator frequency \(\omega(k)=\sqrt{a_e b\,\lambda(k)/2}\). The quadratic **global color-singlet two-quantum** excitation scale is \(2\omega_{\min}=\sqrt{2a_e b\,\lambda_{\min}^+}\). In Kogut–Susskind normalization \(a_e=g_0^2/(2a_{\rm lat})\), \(b=2/(g_0^2a_{\rm lat})\), yielding
\[
2\omega_{\min}=(2\sqrt2/a_{\rm lat})\sin(\pi/L)\sim 2\sqrt2\pi/(a_{\rm lat}L).
\]
This is a diagnostic of long-wavelength transverse modes, **not** an interacting massless theorem or upper bound on the nonlinear physical spectral gap. On a periodic 3-torus, noncontractible flat connections (torons) produce further zero-mode geometry; the prior fixed-planar-disk unique-well strong-field theorem cannot simply be applied to the periodic model.

Numerical incidence checker builds the original 3D B directly, verifies B·gradient=0, all nonzero Gram eigenvalues, rank, and nullity for L=2,3,4 (largest Gram dimension 192). Exact theorem is proved by Fourier symbol, not finite checks.

## Next objective

Reconstruct an open-boundary 3D Hodge and Gauss-reduced physical tangent operator without erroneously treating faces as independent coordinates; then seek a nonlinear many-volume strong-magnetic covariance/energy comparison with explicit box-size and lattice-spacing dependence. Need physically nonzero finite-time spectral weight, OS/Wightman nontriviality and a positive physical-unit mass gap separately.