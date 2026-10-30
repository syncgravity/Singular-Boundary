# R3-IR-510 — Quantitative susceptibility: conditional lower bound and unavoidable missing variance control

Date: 2026-10-30. Finite inverse-Whitney gauge-covariant SU(2) open disk; positive ground state assumed simple. This repairs the proof strategy without claiming a uniform Penrose center-cap theorem.

For a boundary plaquette p=Tr(U_f)/2, with coupling b and a unique free boundary link, the center flip shows m(0)=0. Let m(b)=<p>_b, v(b)=<p²>_b-m(b)², q(b)=<1-p²>_b, and chi(b)=m'(b)>0. The spectral representation of the centered multiplication phi=(p-m)Omega gives the positive first spectral moment s=<phi,(H-E0)phi> and susceptibility chi=2<phi,(H-E0)_perp^{-1}phi>. Spectral Cauchy-Schwarz:

v² <= (chi/2) s.

The exact ground-state carré-du-champ gives s<=(g2²/2)lambda_max(K_ff) q = C_f q. Consequently,

**chi(b)>= 2 v(b)²/[C_f q(b)] >= 2 v(b)²/C_f,**

whenever q>0 (as for a smooth strictly positive finite-link ground state); K=M^-1. This is a quantitative nonperturbative local lower bound on susceptibility for the *full* interacting environment. The coefficient C_f depends on the local inverse-metric block, not explicitly on the sum of magnetic couplings.

If a separately proven bound v(t)>=nu>0 holds on 0<=t<=b, and C_f<=C uniformly, then m(b)=integral_0^b chi(t)dt >= (2 nu²/C)b. More generally m(b)>= (2/C_f)integral_0^b v(t)² dt. Since 0<=m<=1, a constant positive variance bound CANNOT persist over an unbounded b interval; the bound must be used in a finite response window. This exposes the precise missing input: lower control of the conditional local variance or an alternative method as magnetic coupling/refinement grows. It does not follow from Whitney ellipticity.

At zero coupling for the *standalone* Haar SU(2) rotor H=a(-Delta) (no other magnetic terms), p is an eigenfunction with Casimir 3/4, m=0, v=<p²>_Haar=1/4, s=(3a/4)v=3a/16 and chi=2v/(3a/4)=2/(3a). The spectral Cauchy-Schwarz inequality is an equality. The single-link carré-du-champ coefficient C=a/4, q=3/4, so Cq=3a/16 exactly. This standalone check is NOT a statement about the Penrose interacting environment at b=0: center-flip invariance forces m(0)=0 but does not force v(0)=1/4.

For the archived M5 11-face matrix, the earlier face-local coefficient bound max C_f about 3.4922466 at g2²=1 was obtained by floating point; its precision is not certified. Under an admissible patchwise lower SPD face bound, C_f is uniformly bounded as a geometric coefficient before any physical g2² scaling, but v(t) remains uncontrolled.

A simple scaling obstruction: any hypothetical environment-independent chi(b)>=chi0>0 for all b>=0 would imply m(b)>=b chi0>1 eventually, impossible. Thus a valid uniform susceptibility theorem must be restricted to a bounded b window, or scale/decay appropriately. Lower-bound susceptibility is not equivalent to center concentration. Even m close to 1 would imply q<=2(1-m), but the present theorem gives no such bound.

No refinement-uniform center cap or continuum Yang–Mills mass gap has been proved.
