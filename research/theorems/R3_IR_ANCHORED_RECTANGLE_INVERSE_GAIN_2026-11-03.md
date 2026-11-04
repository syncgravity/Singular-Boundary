# R3-IR — Anchored rectangle electric-inverse gain (2026-11-03)

**Research status:** Rigorous special-family estimate for the original-link free-electric SU(2) operator on finite open straight square strips. It is not a general anchored-polymer theorem or a physical interacting/continuum Yang–Mills mass-gap proof. The expanded proof, exact verifier, log and SHA256 manifest are in the conversation file R3_IR_ANCHORED_RECTANGLE_INVERSE_GAIN_2026-11-03.zip.

## Setup
Let N>=2 squares form one straight row; let C_N be the outer rectangular loop of L=2N+2 original links, W_N=Tr(U_{C_N}) its fundamental Wilson trace, and v_f=-(1/2)Tr(U_{partial f}) the fundamental face observable. The original-link free-electric operator and carré du champ are
\[
K=-\sum_e a_e\sum_{j=1}^3 X_{ej}^2,\qquad
\Gamma_K(F,G)=\sum_ea_e\sum_{j=1}^3(X_{ej}F)(X_{ej}G),\qquad 0<a_0\le a_e\le a_*.
\]
Let Q remove constants, \(\mathcal B=K^{-1}Q\Gamma_K\), and use the dimension-weighted nuclear projective Fourier norm P_0 from the prior same-radius audit.

Each face shares r_f links with C_N: r_f=3 for the two endpoints and r_f=2 for the N-2 interior faces. Hence \(\sum_f r_f=L\).

## Proposition (uniform size control in this specific family)

\[
\boxed{\left\|\sum_{f=1}^N\mathcal B(W_N,v_f)\right\|_{P_0}\le
\frac{a_*}{a_0}\left(\sum_f\frac{r_f}{L-r_f}\right)
\|W_N\|_{P_0}\max_f\|v_f\|_{P_0}
\le\frac{2a_*}{a_0}\|W_N\|_{P_0}\max_f\|v_f\|_{P_0}.}
\]
The exact coefficient is
\[
\sum_f\frac{r_f}{L-r_f}
=\frac6{L-3}+\frac{2(N-2)}{L-2}\longrightarrow1.
\]

### Proof
For a fundamental spin-1 SU(2) link the generator operator norm is <=1/2. Fourier projective P_0 is an algebra; therefore
\[
\|\Gamma_K(W_N,v_f)\|_{P_0}\le(3a_*/4)\,r_f\|W_N\|_{P_0}\|v_f\|_{P_0}.
\]
The CG decomposition can change output spin only on links common to the two inputs. Thus every nonzero Fourier output sector retains spin-1 on at least L-r_f outer-loop links. Each contributes Casimir 3/4, so the eigenvalue of physical K on that output is \(\Lambda_{\rm out}\ge(3a_0/4)(L-r_f)\). This excludes constant outputs, and yields \(K^{-1}\) norm <=4/[3a_0(L-r_f)] on the entire output subspace. Multiply the two estimates, sum over f, and use \(\sum_fr_f/(L-r_f)\le L/(L-3)\le2\) for L>=6. This proves the claim.

## Anchored history corollary
For \(\|F\|_{\mathrm{anch},\kappa}=\sup_x\sum_{I\ni x}e^{\kappa|I|}\|f_I\|_{P_0}\), label W_N with the full N-face history I and each v_f with singleton history {f}. Their fused outputs all carry history I. Therefore this concrete pair obeys
\[
\|\mathcal B_{\rm hist}([I]\otimes W_N,\sum_f[\{f\}]\otimes v_f)\|_{\rm anch,\kappa}
\le(2a_*/a_0)e^{-\kappa}\|[I]\otimes W_N\|_{\rm anch,\kappa}\|\sum_f[\{f\}]\otimes v_f\|_{\rm anch,\kappa}.
\]

## Interpretation, limitation and next obligation
The naive positive overlap-counting bound would charge O(N) insertions. The physical inverse instead sees O(N) **surviving occupied original-link spins**, giving O(1/N) per insertion. However, arbitrary long history hulls may reconstruct into short-support spin networks, so their free-electric eigenvalue need not scale with history length. Do NOT extrapolate this example into a general anchored Banach algebra theorem.

Next: resolve low-energy channels in general recoupling, track both interaction-history extent and surviving spin energy, and prove a volume-uniform anchored nonlinear fixed point. Then address interacting physical coupling, 3D spatial geometry, OS reconstruction, and physical-unit continuum mass gap.

## Verification
Exact rational test of link-counting and summed coefficients for N=2..512,1024,10000: 2565 assertions passed. General operator estimate relies on the proof above, not exhaustive tests. No historical simulation archive was changed.