# Recovered theorem: stationary completed temporal SU(2) Wilson insertion

**2026-10-28 recovery audit of 2026-10-27 historical proof.** Original source: \`R3_SU2_transfer_barrier_2026_10_27_bundle.zip/FORMAL_NOTE.md\`, archive SHA-256 \`d3c62eaed9b4c65b5b3dc75ab31abf86c97241795d0df9ff36cc3ea4d81cfc94\`. Core Peter–Weyl / Schatten–Hölder argument independently checked; every other archived certificate has not been re-proved.

**Theorem.** Let a finite spatial graph be extruded through N periodic Euclidean-time slabs. Assume that the **completed** Wilson action has a time-independent positive spatial Wilson potential and time-independent nonnegative temporal couplings \(\beta_e\), all links (including temporal vertex links) integrated with normalized Haar. Remove any set \(Q\) of *temporal* faces to form the cavity, leaving all spatial terms unchanged. Then, for arbitrary overlapping Q and deletion times,
\[
\frac{Z_+}{Z_-}\ge\prod_{(t,e)\in Q}z(\beta_e),\qquad z(\beta)=2e^{-\beta}I_1(\beta)/\beta,\quad z(0)=1.
\]
Moreover \(-\log(Z_+/Z_-)\le\sum_{q\in Q}[(3/2)\log(1+\beta_q)+\log(6\pi)+1/2]\), independent of ambient volume.

**Proof audit.** One-link central Wilson convolution on \(L^2(SU(2))\) has eigenvalue \(2e^{-\beta}I_{2j+1}(\beta)/\beta\ge0\) on spin-j coefficients; its trivial eigenvalue equals \(z(\beta)\). With \(P_0=C_0\), \(C_{\beta}\succeq z(\beta)P_0\). Tensoring gives \(C\succeq z_t C_t\). Gauge projection and common positive spatial multipliers give positive trace-class \(T\succeq z_t T_t\). Periodicity and time-stationarity give \(Z_+=\mathrm{Tr}(T^N)\), \(Z_-=\mathrm{Tr}(\prod_t T_t)>0\). Schatten–Hölder and eigenvalue monotonicity imply \(Z_-\le\prod_t\|T_t\|_N\le(\prod_t z_t^{-1})\mathrm{Tr}(T^N)\). A small SU(2) Haar ball proves the stated uniform polynomial lower bound on z. This proof DOES NOT use invalid monotonicity of traces of three arbitrary positive operators.

**Original Penrose Q14 specialization.** The original \`cavity_audit.py\` inside \`R3_recovered_original_2026_10_27_bundle.zip\` (SHA-256 \`86a598a5f13d672289ad0f7742562ffaeadcb98e79c155c17df3c900fabab71c\`) creates temporal-only Q in slabs 0 and 1, then sets \`R=set(range(len(faces)))-Q\`. Its \`construct_surgery.py\` generates **all** spatial faces each t and temporal ribbons with \`(t+1)%3\`; this verifies that its completed homogeneous Wilson mask is stationary. With \(|Q|=14\) and \(\beta_q=\lambda\),
\[
-\log\frac{Z_{\mathrm{all\ faces}}}{Z_{\mathrm{all\ faces}\setminus Q14}}
\le 21\log(1+\lambda)+14[\log(6\pi)+1/2].
\]
**Status: proved for the unconditioned, all-links-integrated finite-volume Q14 stationary-completion setting, uniformly in ambient volume.** It is a HISTORICAL theorem recovered, not a new simulation or proof of continuum mass gap.

**Important restrictions.** Not a pointwise frozen-exterior boundary comparison. Not a comparison when the *completed* spatial/temporal mask is nonstationary or when spatial plaquettes are inserted/deleted. Not source-identification of the older twelve-prism/four-rhombus/37-independent-link fixed-boundary object. Not interacting Hamiltonian spectral contraction or R2 quantum continuum construction.

**Nonstationary follow-up.** The original \`R3_nonstationary_extension_2026_10_27_bundle.zip\` (SHA-256 \`8146f70688515bdce3204cc53616795ab1bc9f2dc8331c57875f0a0a45eec81b\`) proves arbitrary N=2 completed masks and an N-slab exact extra overlap penalty \(\log\Omega\). \`R3_three_slab_local_bridge_2026_10_27_bundle.zip\` (SHA-256 \`f4ea369e058f926cc2e2dd06ba0ca596578a0faf5d97e55598f9aab341797855\`) localizes the extra N=3 penalty to the negative spectral part of a q-link reduced Jordan bridge. Uniform control of \(\mathfrak E_Q/Z_+\) remains **OPEN**.

See \`docs/evidence/R3_FOURTEEN_ARCHIVE_RECONCILIATION_2026-10-28.md\` and the original archive hashes therein.