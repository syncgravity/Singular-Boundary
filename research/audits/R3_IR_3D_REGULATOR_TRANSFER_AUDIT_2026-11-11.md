# R3-IR / P0 — 3D regulator transfer audit

**Date:** 2026-11-11. **Status:** conditional degree-eight finite-2-complex reference estimate plus source comparison. No physical 3D regulator is certified; no theorem/claim ID is promoted.

## Result

The illustrative finite 3+2 projected-\(\mathbb Z^5\) cubical skeleton has four-link square faces and maximum link-face incidence \(r=8\). The source screening script reports 903 vertices, 2,620 links, 2,810 square faces and 1,360 cubes; 1,700 square faces are incident to more than two selected cubes, up to six. Reproduction of the source construction at coordinate bounds 4, 5 and 6 gives the same counts.

For its finite **2-skeleton only**, if one assigns independent SU(2) link variables, the product radius-two metric and the isolated reference action \(S_g=\sum_f s_g(p_f)\), the bounded-incidence full-Hessian formulas extend to \(r=8\). With the certified conservative ceilings
\[
S_1=0.000333528,\ S_2=1.94619\times10^{-7},\ T=0.000250292,\ h=0.000166813,\ \rho=6/5,
\]
the r=8 values are
\[
B_8=0.001334112,\quad c_8=0.4935925257152,\quad
C_{3,8}\approx0.199765307,\quad C_{H,8}=0.4387849152,
\]
\[
C_{R,8}\approx0.000943360,\quad C_{G,8}\approx0.200708666,
\quad a_8\approx0.493590776,\quad b_8\approx0.298746188.
\]
An independent rational lower-bound verifier uses \(\pi<22/7\), \(e^{-x}\ge1-x\), \(\sqrt{1728}<42\), and \(\sqrt2<3/2\). Gershgorin then gives
\[
\boxed{\lambda_{\min}(Q_8)>0.1972182881>0.1972.}
\]
Direct floating-point evaluation of the same formula is approximately 0.25630392; the rational 0.1972 bound is the conservative certificate.

This transfers only to a finite product-link reference model on the 2-skeleton. The selected 3-cells are non-manifoldly incident, so this is not an ordinary 3D cellulation. The finite patch supplies no compatible refinement maps or fixed-domain \(h\to0\) family.

## Model identity and transfer boundaries

1. **Historical dissertation coupled-\(\mathbb Z^5\):** Chapter 3 defines \(z_1=\sum m_j\omega^j\), \(z_2=\sum m_j\omega^{2j}\), takes \(\operatorname{Im}z_2=ict\) as time and \(u=\operatorname{Re}z_2\) as a compact spatial direction. This is the Penrose plane plus a compact spatial direction and time. The supplied dissertation does not define an oriented 3D gauge cell complex, independent SU(2) links, Wilson plaquette action, or electric/magnetic coefficients. The later 3+2 split retaining the diagonal axis as an extended physical direction is a distinct candidate, not a source-derived identification.
2. **Extruded prism candidate:** the archived chain construction has exact \(\partial_1\partial_2=\partial_2\partial_3=0\), rooted gauge-covariant electric forms and a chosen magnetic coefficient convention. Its electric metric uses a dense Whitney \(M_1^{-1}\), not the product link metric assumed by the current Hessian theorem. Its six approximants have 95–98 edges and 64–65 faces as nominal \(h\) decreases from 0.2 to 0.0667; no fixed-domain refinement is established.
3. **Voronoi candidate:** it has a genuine refining geometric tiling under scaling, but polygonal faces do not meet the four-link plaquette hypothesis. A perimeter-dependent isolated-rotor and Hessian certificate, plus a physical gauge action, would be needed.
4. **Cubic reference:** it has four-link square faces, product link metric and maximum incidence four, so the r=4 reference estimate applies to the chosen isolated-dressing reference action. It is not the historical Penrose model, and its reference measure is not the true interacting ground-state measure. The separate weak-interaction result is electric-dominated; in the stated convention \(z=4/g_0^4\), asymptotic freedom \(g_0\to0\) is outside that small-z regime.

## Source record

- Main-branch projected-\(\mathbb Z^5\) screening script blob: `bbc629449dfa8f746e9b66a58c3b1e7da711c5ec`.
- Main-branch incidence/Voronoi report blob: `cf6e987ecc7c79ed8e612c80bfe7ab53178e5d8a`.
- Prism chain report blob: `734dcb8e765359cb86ff90ea19a4a69331488841`.
- Prism action report blob: `a596cf5290bb53beeedebd3b645719fd3d7eac14`.
- Prism Gauss-domain report blob: `6f2fc916e955f52306b46f9f4a05b352559518a3`.
- Six-prism continuum audit blob: `d91169e638e19274e6c004073058b9bf714ac28e`.
- Uploaded dissertation archive SHA-256: `c405acd6daa5a0a923429ab659b122b22231787d7a30e97db7f2974f278354d1`.
- Uploaded Stage 26 archive SHA-256: `6cfa12935428533cfeaff40a467705d632b19ede07b7f30e0bb9fb7a0cc68657`. Its metadata identifies a Penrose Monte Carlo run, not a gauge-regulator specification.
- `global_whitney_11face.npz` is a 30×30 matrix with edge IDs/eigenvalues; it does not define the full prism family or gauge action. The sweep NPZ files are direct/multihit geometry/control data, not SU(2) link configurations or Hamiltonian coefficient tables.

## Decision

Keep the r=8 result as a conditional finite-2-complex reference estimate. Do not transfer the product-metric theorem to the dense-Whitney prism or polygonal-face Voronoi model. The next decisive task is P0: source-certify one model identity, then specify its actual 3D cell complex, refinement maps, gauge-covariant electric form, complete magnetic action, Gauss domain and physical normalization. The true interacting-vacuum Poincaré inequality and continuum reconstruction remain separate open obligations.
