# The Singular Boundary — Exact shared-edge SU(2) Wilson covariance and weak-magnetic two-rhombus theorem

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Status:** exact, finite-volume, gauge-invariant nonlinear SU(2) Wilson identities at arbitrary magnetic coupling; additionally an analytic and strictly positive connected plaquette covariance coefficient **near zero magnetic coupling** for two edge-sharing rhombi. This is not a result at the physical Penrose strong-magnetic scaling `b_f≈h^-2`, nor a continuum mass-gap, finite-energy survival, or transfer-clustering theorem. No Monte Carlo or historical source edits.

## A. Why this is the right next test

The previous regional exponential-tilt theorem and independent nonlinear rotor comparator show that local spectral moments alone do not decide fixed-physical-time survival. To test what shared edges introduce *exactly*, take two rhombi sharing a full oriented edge, not two factorized plaquette rotors. The connected open two-face disk has 6 vertices, 7 edges, 2 faces and hence 2 independent face holonomies after maximal-tree gauge fixing. Its magnetic terms are nonnegative Wilson plaquette deficits; the shared edge carries a strictly positive electric coefficient. All physical states and observations below satisfy vertex Gauss invariance.

The available data include the original 3-face Penrose Z^5 **spatial** seed, which contains two such adjacent-face pairs and has 8 vertices, 10 edges, 3 faces. This geometry check is not the original temporal Q14 or an authentication of Stage7/26 action coefficients.

## B. The exact shared-edge carré-du-champ Fierz identity (all magnetic couplings)

Let `U` be the shared oriented link (electric coefficient `t=a_s>0`), with the two face boundaries traversing U oppositely. Write their based holonomies as `W_1=U A` and `W_2=U^-1 B`, where A and B are the respective complementary three-edge transports. Let

`p_1=(1/2)ReTr(UA)`, `p_2=(1/2)ReTr(U^-1B)`, and `m=(1/2)ReTr(AB)`.

The trace m is precisely the perimeter-six merged Wilson loop (the internal shared edge is cancelled). On the SU(2) metric normalized by `-Delta chi_(1/2)=3 chi_(1/2)/4`, the quaternion/Pauli completeness relation gives, **pointwise**,

`sum_{alpha=1}^3 (D_e^alpha p_1)(D_e^alpha p_2) = (m-p_1 p_2)/4`. **(SE-1)**

Proof: because trace is cyclic, the second factor may be written `p(BU^-1)`; under `U -> exp(tX)U` the two trace derivatives are respectively `D_X p(UA)` and `-D_X p(BU^-1)`. The two SU(2) elements `UA` and `BU^-1` have product `UABU^-1`, whose scalar quaternion component is m. The S^3 tangent gradient completeness formula is `sum_alpha D_alpha p(Q) D_alpha p(R)= [p(QR^-1)-p(Q)p(R)]/4`. Applying the opposite-orientation sign and the SU(2) trace symmetry gives SE-1. More directly, in quaternion coordinates at a point transformed to U=1, the gradients are opposite imaginary vector parts of A and B divided by two, so their dot product equals `(p(AB)-p(A)p(B))/4`. Bi-invariance proves the general case.

For the physical Wilson Hamiltonian `H=T+V`, `T=sum_e a_e(-Delta_e)`, `V=sum_f b_f(1-p_f)`, the exact ground-state transform gives

`< (p_1-<p_1>) Omega, (H-E_0)(p_2-<p_2>) Omega >`
`    = E_nu Gamma(p_1,p_2) = (a_s/4)(<m>_nu-<p_1p_2>_nu).` **(SE-2)**

This holds at **all** positive magnetic couplings, for any containing graph where the selected faces share exactly one edge. The magnetic potential does not enter the operator identity, but its actual interacting vacuum measure appears on the right. If the faces have disjoint edge support the corresponding off-diagonal first spectral moment is exactly zero, whether or not their equal-time covariance vanishes. Thus SE-2 rigorously distinguishes the shared-edge kinetic coupling from the independent-plaquette comparator without claiming a sign for general coupling.

## C. Exact free-electric two-face physical eigenchannels

For this two-face disk, set magnetic couplings to zero in this section only. Product Haar measure on links pushes to **independent SU(2) Haar face holonomies A,B** under maximal-tree gauge fixing. The unique normalized physical ground state is the constant `1`. Define

`E_1=(3/4)sum_{e in boundary f1}a_e`, `E_2=(3/4)sum_{e in boundary f2}a_e`, `S=E_1+E_2`, `t=a_s`.

The one-face Wilson traces `p_1,p_2` are orthogonal physical electric eigenfunctions with energies E1,E2 and norms squared 1/4. The merged loop `m` is an eigenfunction with energy

`E_M=S-(3/2)t`,

because its six-link perimeter excludes the shared edge. The Leibniz formula `T(fg)=(Tf)g+f(Tg)-2 Gamma(f,g)` and SE-1 give

`T(p_1p_2)=(S+t/2)p_1p_2-(t/2)m`. **(SE-3)**

Exact quaternion Haar moments give

`||p_1p_2||²=1/16`, `||m||²=1/4`, `<p_1p_2,m>=1/16`.

Hence the orthogonal physical combination `Q=p_1p_2-m/4` has norm `||Q||²=3/64` and is another *exact electric eigenstate* with energy

`E_Q=S+t/2`. **(SE-4)**

Both energies are strictly positive since all seven electric coefficients are positive. The physical two-face mixed resolvent matrix element is thus **exact**:

`R_12=<p_1p_2,T_perp^-1 p_1p_2>`
`    =(1/64)(1/E_M+3/E_Q).` **(SE-5)**

The two channels M and Q are indispensable: replacing them with a single Gaussian or independent-rotor energy misses the actual shared-edge response.

## D. Strictly positive nonlinear connected covariance at weak magnetic coupling

Restore genuine Wilson magnetic couplings `b_1,b_2>0` and use the physical Hamiltonian

`H(b_1,b_2)=T+b_1(1-p_1)+b_2(1-p_2)`.

Its unique physical ground state is analytic in `(b_1,b_2)` near `(0,0)` by finite-volume elliptic perturbation theory. The scalar constants b1+b2 do not affect its eigenvector. Choose the intermediate normalization `<1,Omega>=1`. The first and mixed second orders are

`Omega=1+(b_1/E_1)p_1+(b_2/E_2)p_2`
`      +b_1 b_2 (1/E_1+1/E_2)T_perp^-1(p_1p_2) + O(b_1²,b_2²,degree>=3)`. **(SE-6)**

The notation suppresses the individual b1²,b2² second-order terms, which do not enter the mixed coefficient of the connected two-face covariance. The mixed ground-energy derivative vanishes at b=0 because `<p_1,p_2>_Haar=0`.

Using the exact Haar moments and SE-5, the coefficient of b1 b2 in the full **normalized** expectation `<p_1p_2>` is

`2(1/E_1+1/E_2)R_12 + 2/(16 E_1 E_2)`.

The first moments are `<p_1>=b_1/(2E_1)+...`, `<p_2>=b_2/(2E_2)+...`. Subtracting their product therefore yields

`[b_1 b_2] Cov(p_1,p_2)`
` = 2(1/E_1+1/E_2) R_12 - 1/(8 E_1E_2)`
` = (1/(32 E_1E_2)) {S(1/E_M+3/E_Q)-4}`
` = 3t²/[8 E_1E_2 (2S-3t)(2S+t)] > 0.` **(SE-7)**

In the penultimate equality use S=E1+E2 exactly. The final coefficient is strictly positive for t>0 and positive electric coefficients. Its vanishing at t=0 is a direct consistency check for independent face kinetic energies.

Each of the two plaquettes has an exterior link not belonging to the other. Multiplying such a link by the SU(2) center `-I` changes the sign of just one p_f while leaving the electric Casimirs and other plaquette trace unchanged; hence the covariance is *odd separately in b1 and b2*. The analytic expansion consequently has the stronger remainder

`Cov_{Omega_{b1,b2}}(p_1,p_2)`
` = b_1b_2 * 3t²/[8E_1E_2(2S-3t)(2S+t)]`
`   + O(|b_1b_2|(b_1²+b_2²))`. **(SE-8)**

The big-O constant can depend on the fixed seven electric coefficients and the finite physical graph. In particular **for all sufficiently small positive b1,b2 the actual, positive, gauge-invariant nonlinear ground state has positive nonzero connected shared-edge covariance**. This is a finite-model theorem, not a perturbative claim about h→0 at the strong-magnetic coupling.

For seven equal link coefficients a>0, E1=E2=3a, S=6a, t=a, E_M=9a/2 and E_Q=13a/2. The coefficient is exactly

`Cov(p_1,p_2)=b_1b_2/(2808 a²)+O(|b_1b_2|(b_1²+b_2²)/a^4)`. **(SE-9)**

The deficits `d_f=1-p_f` have the **same** connected covariance as the traces, because Cov(1-p1,1-p2)=Cov(p1,p2).

## E. New mixed physical first-spectral-moment response

SE-2 is valid at arbitrary couplings. In the weak-coupling expansion, the merged-loop expectation has the mixed coefficient

`[b1 b2]<m>= (1/(8E1E2))(S/E_M+1)`.

Together with the product expectation in Section D this gives

`E_nu Gamma(p1,p2) = b1 b2 * (S/2) * 3t²/[8E1E2(2S-3t)(2S+t)]`
`                          + O(|b1 b2|(b1²+b2²))`. **(SE-10)**

Thus the off-diagonal **physical energy-weighted** source covariance is strictly positive for sufficiently small positive b1,b2. For uniform a, it begins as `b1 b2/(936 a)`. This is a second analytic signature of shared-link interaction. No assertion about the sign of the full nonperturbative covariance at arbitrary b or strong field is made.

## F. Proof boundaries and next genuine connected-Penrose problem

**Independently proved:** SE-1/SE-2 exact SU(2) merged Wilson-loop carré-du-champ and physical off-diagonal f-sum at all couplings; SE-3–SE-5 exact free-electric physical eigenchannel decomposition; SE-7–SE-10 positive weak-magnetic connected covariance and mixed first spectral moment in the true *interacting* two-face SU(2) vacuum. Symbolic identities and the canonical three-face/ten-edge Penrose **spatial** incidence are checked by `verify_shared_edge_weak_coupling.py`.

**Not proved:** a nonzero covariance at b_f=β_f h^-2 for genuine refining Penrose patches; any macroscopic sum covariance lower bound or upper bound; fixed-time source spectral survival, regulator-uniform all-excitation physical gap, quartic resolvent, or quantum continuum. Small-b Kato radii are regulator- and graph-dependent; there is no justification for analytically continuing SE-8 to b≈h^-2 or summing a finite two-face coefficient over O(h^-2) faces. The signs of remote connected correlations and possible cancellations remain unresolved.

**Next proof gate:** develop a controlled *strong-magnetic*, *shared-edge*, Gauss-invariant covariance comparison with a uniform physical-support scale, using SE-1 as a diagnostic. Necessary ingredients include a quantitative nonlinear vacuum comparison in mixed face directions and bounds on remote covariances; a positive local weak-field coefficient alone is insufficient. Separately authenticate historical Stage7/26 source coefficients and temporal normalization.

## Reproducibility

`verify_shared_edge_weak_coupling.py` performs exact rational SymPy checks of Haar moments, mixed eigenchannel energies, the positive coefficient for arbitrary electric data, the universal equal-a coefficient 1/2808, and mixed physical f-sum 1/936; it also checks the canonical three-rhombus ten-edge Penrose spatial seed. It is an algebraic verifier, not Monte Carlo, and does not simulate the original Stage26 action or establish nonzero continuum covariance. Original archives have not been modified.
