# Source-level reconciliation: Paper 2 real structure and Paper 3 helical observer

**2026-11-11 · source audit of dissertation v10.7 and Papers 2–4**  
**Disposition:** preserve the geometric and sampling investigations; do not treat the current Lorentzian or dynamical interpretations as established.

## 1. Paper 2: the (C_5) representation is correct; the claimed real Lorentz action is not

Paper 2 correctly decomposes the real permutation representation as
[
\mathbb R^5=\mathbb R_{\rm triv}\oplus V_{72^\circ}\oplus V_{144^\circ},
\qquad
\mathbb R^4_{\rm eff}=V_{72^\circ}\oplus V_{144^\circ}.
]
This is the ordinary real representation-theoretic statement about the two nontrivial conjugate eigenvalue pairs.

The next identification (z_2=u+iv), (v=ict), changes the real slice: if (u,ct\in\mathbb R), then (z_2=u+i(ict)=u-ct) is real, so this is not a real-linear identification of the original real (z_2)-plane with a real ((u,ct))-plane. If instead one retains the original real coordinates (z_2=u+iv), the real (144^\circ) rotation acts by
[
\begin{pmatrix}u'\\v'\end{pmatrix}
=
\begin{pmatrix}\cos144^\circ&-\sin144^\circ\\
\sin144^\circ&\cos144^\circ\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
]
After substituting (v=i ct), the induced matrix on ((u,ct)) has imaginary off-diagonal entries; it is not a real Lorentz boost.

More generally, the full four-dimensional real (C_5) representation has no nonzero fixed vector. A finite odd-order subgroup of a real Lorentz group preserves the future timelike cone; averaging any future timelike vector over the finite group gives a fixed future timelike vector. Hence this same four-dimensional representation cannot be made into a real Lorentz ((3,1))-isometry representation with (C_5) acting as claimed. This is a no-go for the asserted real (C_5)-Lorentz symmetry on (\mathbb R^4_{\rm eff}), not a disproof of the finite Penrose graph, projection, or scalar spectral calculations.

The Paper 2 assertion that a (144^\circ) Euclidean rotation becomes a real discrete boost with (\tanh\beta=\tan144^\circ) also fails the finite-order test: a nonzero real boost has eigenvalues (e^{\pm\beta}), and its fifth power cannot be the identity. The (C_5) generator is order five. The complexified quadratic-form identity does not repair the failure to preserve the proposed real slice.

**Required correction:** retain the real (C_5) decomposition and the complexified algebraic structure; withdraw the claim that this (C_5) action is itself a real Lorentz boost on the same four real coordinates. A viable physical time direction would need a separately defined real structure / external time extension and a new action-level derivation. The dissertation's uniqueness proposition for (operatorname{Im}(z_2)) as time is not established by the stated finite representation.

## 2. Paper 3: what the helical construction actually defines

Paper 3 §7 defines
[
z_2(\tau)=A e^{2\pi i p\tau}
]
with constant (A), and lists (p=3/13,5/13,8/13). The text itself later says in Remark 6 that the observer effect is algebraic/kinematic, not field dynamics: a static field is sampled at successive angular positions; no field equation or dynamical evolution is asserted. This is the soundest interpretation to retain.

There are two mathematical qualifications:

1. In the stated (z_2)-plane this is a circle of fixed radius, not a three-dimensional helix. No longitudinal coordinate, Lorentzian metric, monotone physical clock, or embedding into a physical 3-space is specified.
2. The equation is a uniform angular parametrization. Its velocity components satisfy (dot u/dot v=-\tan(2\pi p\tau)) (up to the phase convention), which is not constant. Thus the prose definition “constant ratio (dot u/dot v)” does not follow from the displayed circular path. The parameter (p) sets angular frequency / winding rate, not a constant component-velocity pitch in the displayed coordinates.

The tabulated “pitch angles” should also be audited against the listed ratios before use: (arctan(3/13)), (arctan(5/13)), and (arctan(8/13)) are not the printed (16.99^\circ,26.99^\circ,39.18^\circ). The source does not state a separate conversion formula reconciling them.

Paper 3 also calls the three ratios the three lightest Kaluza–Klein excitations and assigns mass ratios (3:5:8). That is a physical interpretation, not derived by the displayed kinematic sampling equation. No Hamiltonian, KK eigenvalue problem, or dynamical compactification calculation is supplied in §7 to turn the three angular sampling rates into a mass spectrum. Retain the (3:5:8) as a proposed sampling-frequency / symbolic correspondence; do not report it as a proved mass spectrum.

## 3. The 34:55 Conway-worm / spiral statement

The dissertation states that the double Fibonacci spiral has 34 clockwise and 55 counterclockwise arms and that the directional asymmetry should propagate into the angular decomposition of the mode spectrum. It does not specify a reproducible mapping from the 34 and 55 arm families to the five accepted (\mathbb Z^5) direction families, accepted rhombi, or a directed observer path. The 34:55 ratio is therefore a source claim / research hypothesis, not yet a derived observer trajectory or spectral theorem.

Do not substitute the Paper 3 (3:5:8) pitch list for a derivation of 34:55. They are different numerical structures. A synthetic golden-angle annulus or rational 13-step orbit may be useful as a control, but it is not source authentication of the 34:55 Conway-worm mapping.

## 4. Paper 4 and the acceptance-window geometry

Paper 4 supplies the five failure-band / overlap construction and a proposed relation to five Conway-worm families. It does not supply the missing directed 3D observer path or a physical clock. The Paper 3 and Paper 4 band-width conventions and shift-vector normalizations are not transparently reconciled in the source texts. In particular, Paper 3's reported width near (0.062R_W) and Paper 4's expression (2R_W(1-\cos18^\circ)\approx0.0978869R_W) must remain distinct until a common geometric definition is shown. The complementary-overlap area ratio should not be promoted from a proof sketch without deriving the projection and area factors from the same acceptance-window convention.

## 5. Proof-program consequence

The helical observer remains a legitimate **kinematic sampling proposal** on the perpendicular acceptance window. Its useful role is as an observer-marked, gauge-invariant probe once the relevant observables are defined. It does not currently provide:

- a real Lorentzian (C_5) symmetry;
- a source-authenticated 3D helix;
- a physical time/clock or kinetic normalization;
- a KK mass spectrum;
- a derivation of the 34:55 arm-to-worm mapping;
- an interacting-vacuum covariance or spectral-gap estimate.

These are separate obligations in the canonical S0/S1 and interacting-vacuum gates. The finite Z5 geometry, acceptance-window combinatorics, scalar graph spectra, and kinematic sampling experiments remain independently reviewable and should not be discarded because the physical-time interpretation fails.

## 6. Source locations

- Supplied dissertation v10.7, Chapter 3 §§3.1–3.6 and observer discussion.
- Supplied Paper 2, §§2.2–3.4, especially the (C_5) real decomposition and (144^\circ) rotation / boost claim.
- Supplied Paper 3, §7.1–7.2 and Remark 5–6.
- Supplied Paper 4, §§4–5 and §12.

This is a source reconciliation and no-go audit, not a replacement theory. The real-structure / clock question remains open under any alternative formulation.
