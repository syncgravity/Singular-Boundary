# R3-IR — Volume-uniform dressed reference spectral gap
Research continuation dated 2026-11-03. **A theorem on the locally dressed reference diffusion on finite open straight square SU(2) strips, NOT on the full interacting Hamiltonian or continuum Yang–Mills mass gap.** Complete mathematical report and verification script: conversation artifact R3_IR_DRESSED_REFERENCE_UNIFORM_GAP_2026-11-03.zip.

## Theorem
Let N>=1 finite open straight square faces, with corrected original-link unit electric operator K=-sum_{e,a}X_{ea}² and Γ_K(f,g)=sum_{e,a}(X_{ea}f)(X_{ea}g). For each real |z_i|<=3/4, let psi_i(P_i) be the positive, Haar-mean-one ground state of the actual original-link one-plaquette Hamiltonian K_face-z_i chi_1(P_i)/2, as established in the previous single-face dressing theorem. Its character Wiener estimate supplies 1/2<=psi_i<=3/2. Define Phi=product_i psi_i(P_i), L_0=K-2Γ_K(log Phi,·), and dressed probability measure mu=Phi² dHaar/Z on gauge-invariant configurations.

Then L_0 is nonnegative/self-adjoint in L²(mu), has constants as its ground space, and satisfies
\[
\boxed{\operatorname{gap}(L_0)\ge 1/12}
\]
**uniformly in N** and in all real individual couplings |z_i|<=3/4. Equivalently, its inverse on mu-mean-zero functions has L² operator norm <=12.

## Proof
Fix a maximal tree that contains all original links except the N top links. The independent top-edge variables identify the gauge-reduced open strip with N independent SU(2) plaquette holonomies P_i modulo one global simultaneous conjugation. Original-link Haar measure becomes independent Haar in P_i; the dressed mu becomes the product of normalized one-site measures nu_i=psi_i(P_i)²dHaar(P_i)/Z_i, restricted to conjugation-invariant functions.

For every f(P_1,...,P_N), the original-link K Dirichlet form contains the N independent top-edge terms and is bounded below by \(\sum_{i,a}\int|L_{i,a}f|² d\mu\), where L_{i,a} differentiates only P_i. Other original-link derivatives give nonnegative squares. Full SU(2) Haar has one-site -sum_aL_a² spectral gap 3/4. One-site density comparison, using 1/2<=psi_i<=3/2, gives
\[
\operatorname{Var}_{\nu_i}(h)\le (4/3)\,9\int\sum_a|L_a h|²d\nu_i
=12\int\sum_a|L_a h|²d\nu_i.
\]
Product Poincaré tensorization yields Var_mu(f)<=12 E_mu Γ_K(f,f). Integration by parts identifies E_mu Γ_K(f,f)=⟨f,L_0 f⟩_mu, proving the bound. Restricting to the simultaneous-conjugation-invariant physical subspace preserves the inequality. Crucially, the constant is independent of N.

## Dressed residual and open obligation
The exact original-link conjugation is
\[
\Phi^{-1}\left(H-\sum_iE_i\right)\Phi=L_0+W,\qquad
W=-2\sum_{i<j}\Gamma_K(s_i,s_j),\quad s_i=\log\psi_i.
\]
For a straight row, W consists only of neighboring face interactions; it is an extensive multiplication operator. **The gap of L_0 does not by itself bound the gap of L_0+W uniformly in N.** A local residual stability or convergent connected expansion remains necessary.

For \(\Psi=\Phi e^T\), the exact logarithmic residual equation is
\[
L_0T=(E_{\rm full}-\sum_iE_i)-W+\Gamma_K(T,T).
\]
At adjacent-face source degree (1,1), \(W_{ij}=-(1/18)\Gamma_K(\chi_1(P_i),\chi_1(P_j))\), so
\[
T_{ij}=(1/18)K^{-1}Q\Gamma_K(\chi_1(P_i),\chi_1(P_j))
=-\chi_1(P_i)\chi_1(P_j)/468+2\operatorname{Tr}(P_iP_j)/351.
\]
This matches the independently computed original-link physical score coefficient. The harder three-face (1,2,1) disconnected end-loop coefficient \(-1381/1261578240\) has **not** yet been independently reconstructed from dressed perturbation; preserve that open regression test.

Next: control the full dressed residual \(L_0+W\) in a spatially local manner uniformly in N, then verify the fourth-order regression, before attempting λ=1, three-dimensional spatial lattices or the nontrivial four-dimensional continuum Yang–Mills mass gap.

Arithmetic verifier: 5,050 density-ratio comparisons and rational one-face/second-order regression checks passed; the Poincaré proof is an analytic argument, not a machine proof or independent peer review.