# PF-I16 — Authenticated three-face witness, original eight-size replay, sharp incidence, and conditional non-HS bilinear estimate

**November 9, 2026. Research audit, not a Yang–Mills mass-gap proof.** Full reimplementation of indexed original source selection, executable checker, eight-size log, analytical derivation and SHA-256 manifest: Library \`/The Singular Boundary/Proof Audits/PF_I16_AUTHENTICATED_MOTIF_2026_11_09.zip\`.

## Essential provenance

The original unpublished \`paper6_extend_local.py\` was located in Library and its indexed algorithm read. Raw-byte materialization was unavailable. The source's generic gamma, five-direction pentagrid intersection/ceiling enumeration and original 35%-of-max-tile-center interior selection were independently reimplemented. Actual accepted faces additionally require **PF-I11's lower-height perpendicular 3-coordinate triangle test**, not just four original vertices. The original script was **not executed byte-identically** in this turn; independently reproducing all eight PF-I11 V/E/F counts and the face witness is substantial consistency evidence but not a substitute for source-SHA execution.

|Ngrid|V|E|F|max genuine faces/edge|trivalent witness|
|---:|---:|---:|---:|---:|---|
|7|1550|3017|1468|2|yes|
|10|3042|5927|2886|2|yes|
|12|4324|8468|4145|2|yes|
|15|6980|13779|6800|2|yes|
|18|9950|19593|9646|2|yes|
|20|12207|24091|11879|2|yes|
|23|16435|32582|16138|2|yes|
|25|19260|38139|18874|2|yes|

Every count equals PF-I11's original source-population record. No square/cubic/Voronoi replacement. The *full-window core* remains a separate control, not the population replayed here.

## Corrected authentic three-face trivalent witness

All eight source-selected complexes contain the genuine accepted faces (lower five-integer label, family):
- \`((0,1,0,0,0), (2,3))\`
- \`((0,1,0,0,0), (3,4))\`
- \`((0,1,0,0,1), (0,3))\`.

The respective maximal perpendicular-face triangle halfspace residuals are \`-0.0348977077231, -0.0236953850391, -0.0236953850391\` (negative => strict acceptance). The union has 8 vertices, 10 original links, three loops, four degree-two and four degree-three vertices. After suppressing degree-two vertices **only for SU(2) spin labeling**, six strand lengths are **3,3,1,1,1,1**. Its trivalent multi-graph and weighted electric spectrum are precisely those used by the preceding PF-I16 theorem \`K^-1 P0 in Schatten S_p iff p>3\`. Therefore that **abstract spectral threshold applies to an authenticated source-local motif**; this does *not* establish an interacting mass gap.

At Ngrid=7, 6,156 accepted three-face chains (8V,10E) were found, split into 2,786 four-trivalent motifs (six-label theorem applies) and 3,370 motifs with one degree-four, two degree-three vertices (requires separate four-valent intertwiner analysis).

## ERRATUM to preceding three-face example

The *specific* three-squares-of-a-3-cube witness \`ij@m\`, \`ik@m\`, \`ij@(m+e_k)\` described in \`PF_I16_THREE_FACE_SCHATTEN_THRESHOLD_2026_11_09.md\` is **not an accepted PF source motif**. Indeed the opposite \`ij\` faces cannot simultaneously pass the strict perpendicular-triangle test: writing \`q_r=P_perp(e_r)\` and letting \`l,r\` be the complement of \`i,j,k\`, the lower face requires \`P_perp(m+gamma)\` in the interior of \`conv(q_k,q_l,q_r)\`; the opposite upper \`ij\` face (after subtracting q_k) requires it in the interior of \`conv(q_l,q_r,q_l+q_r-q_k)\`. The third vertices are reflections through the midpoint of \`[q_l,q_r]\`; the interiors are in opposite halfplanes and disjoint. This is an **exact structural exclusion**, independent of gamma. The earlier geometric illustration is invalid; the abstract six-spin theorem is *rescued* by the explicit accepted witness above, which has the same weighted six-strand graph. Do not cite the prior cube as authenticated source geometry.

## Improved PF-I16 source-incidence constants

In these authentic accepted complexes, every original edge meets at most **two** genuine rhombi (not the crude at-most-eight five-coordinate-square count). Thus at fixed auxiliary coefficients \`a_e>=a0>0, 0<=b_f<=b0\`:
\[
T_e=\int|\nabla_e\Omega|^2d\mu\le 4b_0/a_0,\quad
\mathbb E_{\nu}|s_e|^2\le16b_0/a_0,\quad
I_\nu(U_e;U_{-e})\le16b_0/a_0.
\]
Each face has at most 4 edge-overlap neighbors, not 28. The rooted connected face-set count improves to \`A_k(f)<=16^(k-1)\`; the anchored fixed-order pair-history norm bound improves to \`(7/351)a_*b0²/a0³\` plus same-face \`b0²/(288a0²)\`. The first nonzero one-link mutual-information perturbative coefficient is bounded by \`c0²/(9a0²)\`.

For unit coefficients, replacing \`T_*=16\` with \`T_*=4\` sharpens the earlier positive-frequency Wilson spectral-weight theorem: \`q_-(4)=0.1141101056459326\`, threshold \`c/2=0.0570550528229663\`, weight lower bound \`c²/(4B²)=2.69031326663758e-5\`. This is **not** a low-energy exclusion or physical mass.

## Direct non-Hilbert–Schmidt bound on the combined nonlinear operator

Let \`K=sum_e a_e C_e\`, reduced electric gap \`Delta_el>=3a0\`, and \`Gamma_K(F,G)=sum_e a_e <grad_eF,grad_eG>\`. Define \`D4(F)^2=sum_e a_e||grad_e F||_(L4(product Haar))²\`. Hölder and weighted Cauchy–Schwarz yield \`||Gamma_K(F,G)||_2<=D4(F)D4(G)\`. The source-volume-independent resolvent gap then proves **on every finite authenticated original-source graph**
\[
\boxed{\|K^{-1}P_0\Gamma_K(F,G)\|_2\le\frac{D_4(F)D_4(G)}{3a_0},}
\qquad
\boxed{\mathcal E_K(K^{-1}P_0\Gamma_K(F,G))^{1/2}
\le\frac{D_4(F)D_4(G)}{\sqrt{3a_0}}.}
\]
This genuine all-finite-source *conditional regularity* result does not need Hilbert–Schmidt inverse. It is not an iterable score bound because \`D4\` of the **output** is not controlled. No such uniform score-regularity estimate has been proved.

**Gates remain OPEN:** uniform all-orders nonlinear convergence; interacting Poincaré gap; source-selected kinetic/time normalization, physical continuum/OS reconstruction; four-dimensional Yang–Mills mass gap. Canonical main and historic source archives are unchanged.
