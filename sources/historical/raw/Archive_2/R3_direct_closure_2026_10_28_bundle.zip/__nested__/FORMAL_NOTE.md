# Direct R3 closure attempt: exact Haar elimination and the remaining 54-face geometry

Date: 2026-10-28. Status: an unconditional, volume-uniform SU(2) energy theorem for **peelable** local face sets, with an executable certificate checker; **no unconditional theorem for the specific 54 Penrose fill faces** has been obtained. This note does not claim a continuum Yang–Mills mass gap.

## 1. The target and what is actually available

The requested estimate is `sup_Λ λ E_{R,λ} S_F <= a log(1+λ)+C` for the 54 retained fill faces F, where R is an arbitrary nonstationary retained mask. Prior work proves the exact local one-link Ward estimate `λ E(S_e-m_e) <= 3/2` and the Bianchi comparison `S_Q <= 44 S_F` under its reported Penrose certificate. The gap is control of the *Gibbs-averaged* `m_e`. A pointwise link-star argument cannot bound it: two opposite staples give `m_e=2` for every λ. The global exterior Gibbs measure might suppress such staples, but this is not a consequence of the one-link Ward identity.

The uploaded `penrose_complete_catalogue.npz` has arrays `idx`, `sign`, `length`, `roots`, `distance`, `target`, `faces`, `cidx`, `csign`, `clength`, `ckind`, `F`, `graph_hash`, `threshold`, `coverage_version`. These are not a labelled retained-face-to-prism-link incidence map for the 54 fill faces. The other uploaded Stage 26 and Phase III archives are numerical simulation and 2D geometry files, not an identified 54-face R3 fill certificate. Thus the exact local peeling/cover tests cannot responsibly be asserted for the specific 54 faces from these materials alone.

## 2. A new unconditional theorem: private-edge elimination

**Theorem (exact local face peeling).** Let R be any finite collection of ordinary oriented Wilson plaquettes on an arbitrary finite SU(2) gauge complex. Let `F⊂R`. Suppose there exists an ordering `p_1,...,p_m` of all faces in F and an edge `e_i` on `p_i` such that `e_i` occurs exactly once in `p_i` and in no other face of `R\{p_1,...,p_{i-1}}`. The same link may not appear twice in any plaquette. All retained couplings equal λ, and Haar measure is normalized. Then

`Z_R(λ) = z(λ)^m Z_{R\F}(λ)`

where `z(λ)=∫_{SU(2)}exp[-λ d(g)]dg = 2e^{-λ}I_1(λ)/λ`.

Moreover, for every `p_i∈F`, under the *original* full Gibbs measure,

`E_{R,λ} d(W_{p_i}) = -∂_λ log z(λ)`

when varying that plaquette's coupling independently, and

`0 <= λ E_{R,λ} S_F <= (3/2)|F|`.

The constants are independent of the total number of edges and faces, boundary geometry, and all nonstationarity elsewhere.

**Proof.** Since `e_1` appears only once in `p_1` and nowhere else in the retained action, write its holonomy as `u`, and the plaquette holonomy as `A u B` or `A u^{-1} B`, with A,B depending on other edges. Haar invariance under inversion and left/right translation gives

`∫_{SU(2)} exp[-λ d(Au^{±1}B)]du = z(λ)`

independently of A,B. Integrating `e_1` removes the face `p_1` and multiplies the remaining partition function by z. Repeat with `e_2,...,e_m`. To compute the marginal of any peeled face, allow independent couplings `λ_i`, obtaining `Z_R=(∏ z(λ_i)) Z_{R\F}`; differentiating gives the exact single-face marginal mean. Finally `λ(-d/dλ log z(λ))<=3/2` follows from the SU(2) one-link heat-bath integration-by-parts identity, or by the `S^3` integral in the Ward audit. QED.

**Partial peeling corollary.** If only a subset `P⊂F` can be peeled from R, then

`Z_R=z(λ)^{|P|} Z_{R\P}`,

`λ E_R S_F = |P| λ(-d/dλ log z) + λ E_{R\P} S_{F\P}`.

Thus an exact combinatorial elimination reduces the unresolved energy estimate to a strictly smaller face set whenever `P` is nonempty. The identity does not assume positivity of mixed SU(2) spin-network coefficients.

## 3. Why the certificate matters

A numerical rank of the linearized face-edge incidence matrix is **not** a private-edge peeling certificate. In a nonabelian theory, invertibility of a linearized Jacobian does not imply a global Haar-preserving factorization of the Wilson integral. The certificate checker `peeling_certificate.py` therefore uses exact discrete incidence and explicitly checks each private edge against *every currently retained face*, including those outside F.

A failed peeling test does not disprove the 54-face energy estimate. It shows only that this exact factorization mechanism does not cover the whole set. The generic one-link Ward and interpolation identities then remain, and their frustration/partition-ratio terms still require genuine Gibbs control.

## 4. Exact alternative identity (does not close the estimate)

For `Z(s)=∫exp[-λ S_{R\F}-sλS_F]dU`, let `μ_s` denote the Gibbs law. Then

`λ E_1 S_F = log[Z(0)/Z(1)] - D_KL(μ_1 || μ_0)`.

Proof: `log(dμ_1/dμ_0)=-λS_F+log[Z(0)/Z(1)]`, integrate under μ_1. Since KL≥0, this recovers the coupling interpolation upper bound. This exact identity shows why interpolation alone cannot establish the needed polynomial ratio: the KL term can be extensive and does not supply a bound on the ratio.

## 5. Data and verification

`peeling_certificate.py` reads JSON `{"faces":{"p1":["e1",...]},"fill":["p1",...]}`. Every retained face must be listed, not just the 54 fill faces. The checker returns a full or partial peeling certificate, with the ordered private-edge witnesses. `test_peeling.py` covers a peelable disk, a closed two-face shell, an external-face obstruction, a partial certificate, and a full-rank incidence system without any private edge; all five tests passed. This is an exact combinatorial check, not an SU(2) Monte Carlo estimate.

## 6. Closure status

**Proved here:** exact volume-uniform `3|F|/2` energy estimate for any fully peelable F in an arbitrary nonstationary SU(2) Wilson background; exact partial-peeling reduction; KL identity.

**Not established here:** peelability or an alternative nonabelian Haar-elimination certificate for the particular 54 Penrose fill faces; suppression of the remaining staple-frustration term if the 54 faces are not peelable; the unrestricted three-slab R3 bound; a continuum mass gap.

**One concrete missing input for applying this new theorem:** the *labelled* retained-face-to-link incidence for the actual R3 54-face fill support and its surrounding retained faces. The files inspected in this session contain geometry/simulation catalogs but not an identified mapping for that exact support. A fresh geometry reconstruction would need the original 14 Q face labels or coordinates to avoid selecting a different cavity.
