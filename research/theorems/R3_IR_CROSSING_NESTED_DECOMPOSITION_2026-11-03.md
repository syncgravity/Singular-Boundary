# R3-IR — Same-weight crossing closure and nested scalar obstruction
Research audit: 2026-11-03. The **crossing/end-joining** portion of the history-labelled physical SU(2) original-link free-electric Poisson bilinear operation is bounded at the **same spatial-history weight**, assuming the previously reported matrix Peter–Weyl local estimate. The **nested** portion remains open. This is **not** a full interacting or continuum mass-gap theorem.

## Setup
On a finite open straight row of square faces, let I,J be face intervals, E(I) their incident original-link supports, \(K\) the corrected original-link electric operator, \(\Gamma_K\) the corresponding carré du champ and \(\mathcal B=K^{-1}Q\Gamma_K\). Assume the prior finite-original-link estimate
\[
\|\mathcal B(f_I,g_J)\|_{P_\sigma}\le C_0 |E(I)\cap E(J)|\|f_I\|_{P_\sigma}\|g_J\|_{P_\sigma},\quad C_0=24(1+a_*/a_0).
\]
For history-labelled inputs \(F=\sum_I[I]\otimes f_I\), let
\[
\|F\|_{\mathrm{anch},\kappa,\sigma}=\sup_x\sum_{I\ni x}e^{\kappa|I|}\|f_I\|_{P_\sigma},\quad \kappa>0,\;\sigma\ge0.
\]
Crossing pairs are I=[a,b], J=[c,d] with a<c<=b<d or the reverse, plus adjacent end-joining pairs b+1=c or d+1=a. The history-aware operation retains all physical output channels and labels each output by I∪J.

## Theorem: crossing pairs bounded without weight loss
\[
\boxed{\|\mathcal B_{\mathrm{cross}}(F,G)\|_{\mathrm{anch},\kappa,\sigma}
\le 4C_0 S(e^{-\kappa})\|F\|_{\mathrm{anch},\kappa,\sigma}\|G\|_{\mathrm{anch},\kappa,\sigma}}
\]
where \(S(q)=1/(1-q)+3q/(1-q)^2\). The constant is uniform in strip length, representation degree and connected-history lengths.

### Proof
For a crossing pair set t=|I∩J|>=0. The output history weight factor is e^{-κt} and |E(I)∩E(J)|<=3t+1 (t=0 for adjacent pair). Fix an output anchor x. In the case x∈I, every J crossing I on the right with intersection length t has start c=b-t+1 and necessarily contains exterior endpoint b+1. For each t, its total input weighted norm is at most ||G||_anch, regardless of I length. The left side has the analogous endpoint a-1. Thus x∈I contributes <=2C0 ∑_{t>=0}(3t+1)e^{-κt} ||F||_anch||G||_anch. The symmetric case x∈J doubles this. Completion yields the bound.

## Exact obstruction to the scalar nested majorant
Let I_N=[1,N]. Define the positive **auxiliary scalar** history kernel by replacing each pair's physical fusion with |E(I)∩E(J)| and retaining union history. For F carrying only I_N with coefficient e^{-κN}, and G carrying all N singleton histories with coefficient e^{-κ}, both anchored norms equal one. Each singleton shares four links with E(I_N), and union history remains I_N. Hence
\[
\boxed{\|\mathcal B_{\mathrm{nested}}^+(F,G)\|_{\mathrm{anch},\kappa}=4Ne^{-\kappa}\to\infty.}
\]
No uniform same-κ theorem follows from **bare positive overlap-counting** in the nested sector. This is not a counterexample to the physical SU(2) bilinear operation; the previously derived Casimir-energy splitting controls the physically relevant fundamental-singleton insertion case.

## Verification and precise next task
The exact-rational Python checker in the full conversation archive verifies crossing/end-joining interval geometry for widths 2..59 and 195 exact-rational seeded scalar anchored tests across widths 2..14: **12,942,199 checks passed**. It does not re-prove the inherited matrix Peter–Weyl input or the infinite-dimensional operator estimate.

The next required theorem is same-weight **nested-history** closure using physical electric-energy denominators and actual SU(2) recoupling, or a convergent renormalized nested recurrence. Physical λ=1 gap, three-dimensional spatial extension, continuum construction and positive physical Yang–Mills mass gap all remain open. The full mathematical report, executable verifier, execution log, and SHA-256 manifest are preserved in R3_IR_CROSSING_NESTED_DECOMPOSITION_2026-11-03.zip.