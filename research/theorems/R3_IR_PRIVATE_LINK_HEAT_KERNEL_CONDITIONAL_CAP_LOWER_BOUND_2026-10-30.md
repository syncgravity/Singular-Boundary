# R3-IR-427 — Genuine Wilson private-link heat-kernel conditional cap lower bound

2026-10-30. FINITE-VOLUME FULL-COUPLING THEOREM. Establishes a strictly positive Haar-relative conditional cap estimate for the actual original-link SU(2) Wilson vacuum. Its constant is NOT uniform under physical refinement, so no continuum gap follows.

## Model
Let f be a magnetically deleted target face of a planar SU(2) Wilson rhombus disk with original links and free dynamical boundary. Choose an edge x incident to f and only one other magnetic face g. Set H=a_x(-Delta_x)+H_y-b_g p_g(x,y), up to constants, with a_x>0, b_g>=0, |p_g|<=1, H_y the exact interacting Hamiltonian on all other links (including all their magnetic interactions), and Delta_x normalized to eigenvalues -j(j+1). The normalized positive unrestricted ground state Omega(x,y)>0 is unique and Gauss invariant.

Let k_s(x,z) be the strictly positive central SU(2) heat kernel for generator a_x Delta_x at time s>0. Define
m_s= min_{x,x',z in SU(2)} k_s(x,z)/k_s(x',z)>0,
and r_s=e^(-2 b_g s) m_s.

## Theorem (HK-1): conditional density domination
For almost all y and all x,x' (with the smooth positive representative),
Omega(x,y)>=r_s Omega(x',y). (HK-1)

Proof. Let H_free=a_x(-Delta_x)+H_y. The original-link Feynman–Kac formula with bounded scalar potential -b_g p_g yields the pointwise positive semigroup kernel comparison
e^(-b_g s) K_free(s; (x,y),(z,w))
<= K_H(s;(x,y),(z,w))
<= e^(b_g s) K_free(s;(x,y),(z,w)).
The free kernel is k_s(x,z) K_y(s;y,w) because the two operators act on disjoint sets of links. For all x,x',z,w, the lower H kernel starting at (x,y) is at least e^(-2b_g s)m_s times its upper bound starting at (x',y). Integrating both against the positive Omega(z,w) in the eigenfunction identity Omega=e^(sE0)e^(-sH)Omega gives HK-1. This is a comparison of positive unprojected kernels; gauge invariance is retained because the unique unrestricted positive vacuum is gauge invariant. No unsupported factorization of a *Gauss-projected finite-temperature trace* is used.

Fix y. Set N(y)=int_SU2 Omega(x,y)^2 dx. Since min_x Omega>=r_s max_x Omega, the normalized conditional x-density obeys
Omega(x,y)^2/N(y) >=r_s² for every x.

Thus for every measurable central target cap B on W_f=xL(y),
P_vac(W_f in B | y)>=r_s² Haar(B).
After integrating y,

boxed: P_vac(W_f in B)>=r_s² Haar(B)
= e^(-4b_g s) m_s² Haar(B). (HK-2)

For any bounded nonnegative central cap multiplier k, the same proof gives
<k(W_f)>_vac >= e^(-4b_g s)m_s² int k(W)dW. (HK-3)

This is a TRUE full-coupling bound, valid with the other three neighboring Wilson plaquettes active, no interacting spectral-gap assumption, and independent of environmental volume.

## Heat-kernel constant and limitation
By scaling, m_s depends only on a_x s. For s=1/a_x, define the universal number m_*=min_{u,v,w} k_1(u,w)/k_1(v,w)>0, where k_1 is the normalized SU(2) heat kernel at time 1. Then
P_vac(B)>=m_*² exp(-4 b_g/a_x) Haar(B). (HK-4)

A half-Haar bound would follow from the explicit additional condition m_*² exp(-4 b_g/a_x)>=1/2; that condition is not established at physical Penrose refinements, and the simple heat-kernel ratio bound may be extremely conservative. Other s can be optimized, but no regulator-uniform positive infimum is obtained when b_g/a_x diverges.

The inequality cannot be promoted to a continuum mass-gap theorem. It is a genuine conditional Harnack-type positive density bound at every finite volume, not the desired uniform half-Haar cap-survival estimate.

Scope: scalar bounded Wilson magnetic potential, compact SU(2) link, unconstrained original-link configuration space, real positive ground state, and a selected edge magnetically incident to exactly one retained face. Other boundary conditions/topologies require separate checks.
