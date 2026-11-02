# R3-IR — Boundary-weight internal-insertion obstruction (2026-11-02)

**Scope:** A theorem about the explicitly defined positive scalar interval insertion operator. It is **not** an assertion that the actual SU(2) dressed resolvent diverges.

For a finite straight square strip let E(I) be the original-link union of interval I. Define
(Tc)(J) = sum over intervals I and faces f with E(I)∩E(f) nonempty and I∪{f}=J of |E(I)∩E(f)| c(I).

For interval I=[a,b] with ℓ=b−a+1, a face f in I shares four links, an existing immediate external neighbor shares one, and all other faces share zero. Thus T_{I,I}=4ℓ; total outgoing positive overlap weight equals 4ℓ+1_{a>0}+1_{b<N−1}.

For any positive weights w(I), the weighted ℓ¹ operator norm satisfies ||T_N||≥4N, by testing the full interval I of N faces. Repeated diagonal insertion gives (T_N^k)_{I,I}≥(4|I|)^k, so this unrenormalized positive scalar model has no volume-uniform positive Neumann radius. Support-length weighting cannot help because its input and output weights cancel on diagonal internal insertions.

Splitting T into internal insertion and genuine interval extension identifies a possible alternative: the *scalar extension part* has at most two outgoing terms per interval and weighted ℓ¹ bound ≤2e^α for w(I)=e^{α|I|}. This does not prove a corresponding bound for the actual Fourier-valued operator. Block dressing / internal resummation and dressed centering remain open.

Exact-integer checks verify all interval-link overlaps for strips N=1,...,30 and repeated diagonal examples. Full proof, verifier, log and SHA256 manifest are in Library /The Singular Boundary/Proof Audits.

The nonlinear connected expansion, interacting λ=1 gap and continuum mass gap remain open.