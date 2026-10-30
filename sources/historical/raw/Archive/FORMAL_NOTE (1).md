# An exact Wilson small-field / large-field split: established bounds and remaining RG obligations

Date: 2026-10-26. Scope: arbitrary finite bounded-incidence 3D spacetime lattice with SU(2) links; includes spatial Penrose rhombi times a temporal discretization subject to bounded local incidence. The results here are not a proof of mass gap.

## 1. Physical fixed-anisotropy trajectory

Write the full Wilson Gibbs measure
\[d\mu_\lambda(U)=Z_\lambda^{-1}\exp[-\lambda X(U)]\prod_{e\in E}dU_e,\qquad X(U)=\sum_{p\in P}c_p(1-\tfrac12\operatorname{Tr}W_p),\]
where \(c_-\le c_p\le c_+\), \(\lambda=(g_3^2h)^{-1}\), \(a_t=\kappa h\) with fixed \(0<\kappa_-\le\kappa\le\kappa_+\). Assume bounded plaquette perimeter \(L\), \(|E|\le\rho |P|\), and for convenience all plaquettes contractible with fixed length <= L. No translation invariance is used.

## 2. Uniform mean defect from a small-link partition-function bound

There exist constants \(A,B\), depending only on \(c_+,L\), group metric and bounded incidence, such that for \(\lambda\ge 2\),
\[-\log Z_\lambda\le |E|\bigl(A+B\log\lambda\bigr).\]
Proof: restrict each link to a ball of group radius \(r_0\lambda^{-1/2}\) around identity. Haar mass of this ball is at least \(c\lambda^{-3/2}\), and plaquette defect is at most \(C L^2r_0^2/\lambda\). Therefore \(Z_\lambda\ge (c\lambda^{-3/2})^{|E|}\exp[-C'|P|]\). Since bounded incidence gives \(|P|\le d|E|\), the claim follows. A mild nonempty-complex ratio is assumed. The estimate can equivalently be written \(F\le C(|E|+|P|)(1+\log\lambda)\).

Concavity of \(F(\lambda)=-\log Z_\lambda\), with \(F(0)=0\), gives \(F'(\lambda)=\mathbb E_\lambda X\le F(\lambda)/\lambda\). Thus
\[\frac1{|P|}\sum_p\mathbb E_\lambda(1-p_p)\le\frac{C\rho}{c_-}\frac{1+\log\lambda}{\lambda}.\tag{1}\]
This concerns the complete spatial and temporal Wilson measure.

## 3. An exact gauge-invariant sector decomposition

Fix \(0<\alpha<1\), \(\delta_\lambda=\lambda^{-\alpha}\). Mark each plaquette bad if \(1-p_p>\delta_\lambda\). Then the identity
\[1=\prod_{p\in P}\left[\mathbf 1_{1-p_p\le\delta_\lambda}+\mathbf 1_{1-p_p>\delta_\lambda}\right]\]
partitions the full integral into sector weights indexed by bad-plaquette sets. Gauge invariance is exact, since each indicator is conjugation invariant.

Let \(N_{\rm bad}\) be the number of bad plaquettes. Markov and (1) imply
\[\boxed{\frac{\mathbb E N_{\rm bad}}{|P|}\le C\rho\frac{1+\log\lambda}{\lambda\delta_\lambda}=C\rho(1+\log\lambda)\lambda^{\alpha-1}.}\tag{2}\]
In particular, \(\alpha=1/2\) gives \(O(\lambda^{-1/2}\log\lambda)\), independent of volume. For any \(\epsilon>0\), \(\mu(N_{\rm bad}/|P|>\epsilon)\le C\rho (1+\log\lambda)\lambda^{\alpha-1}/\epsilon\).

IMPORTANT: this is a density bound, not a bound on the probability of any bad plaquette, nor an exponentially decaying connected polymer activity. At fixed physical volume the number of cells diverges, and \(\mathbb E N_{\rm bad}\) need not vanish.

## 4. Local Gaussian approximation on the good sector

For each good face, write \(W_p=\exp(i\theta_p n_p\cdot\sigma)\), \(0\le\theta_p\le\pi\). If \(\delta_\lambda<1\), \(\theta_p\le\arccos(1-\delta_\lambda)\). The Taylor bound
\[0\le\frac{\theta^2}{2}-(1-\cos\theta)\le\frac{\theta^4}{24}\]
yields \(\bigl|\lambda c_p(1-p_p)-\lambda c_p\theta_p^2/2\bigr|\le\lambda c_p\theta_p^4/24\). Since \(\theta_p^2\le C\delta_\lambda\) on the good face,
\[\boxed{\bigl|\lambda c_p(1-p_p)-\lambda c_p\theta_p^2/2\bigr|\le C\delta_\lambda\,[\lambda c_p\theta_p^2/2].}\tag{3}\]
The relative nonlinear correction per good plaquette vanishes, for \(\alpha=1/2\), like \(O(\lambda^{-1/2})\). The sum over all plaquettes is extensive; this alone is NOT a bound on renormalized connected polymers.

The logarithm of each plaquette holonomy need not be representable by a globally small link potential on a topologically nontrivial spacetime torus, or without gauge fixing. Flat holonomies and gauge zero modes must be handled separately.

## 5. Finite-block exact renormalized coefficients

Choose a gauge-covariant block map \(Y=\mathcal B(U)\) preserving retained boundary parallel transports. The exact blocked density is \(e^{-S_{\rm eff}(Y)}=\int \delta(\mathcal B(U)-Y)e^{-S(U)}dU\), understood via disintegration of Haar measure. The split in Sec. 3 can be inserted inside the integral, yielding exact good/bad sector integrals.

Let \(S_{\rm loc}(Y)\) denote *defined* extracted local action terms. The residual is \(\Psi(Y)=S_{\rm eff}(Y)-S_{\rm loc}(Y)\). Without a specified gauge-fixing, fluctuation covariance, localization operator and block extraction, \(\Psi\) does not yet have proved polymer decay. Source derivative coefficients are exact conditional cumulants only when differentiating the *full* conditional logarithmic integral including the cutoff indicators' coupling dependence, if any.

A sufficient next theorem would be \(\sup_z\sum_{\Gamma\ni z}e^{m\operatorname{diam}(\Gamma)+\alpha|\Gamma|}\|\Psi(\Gamma)\|\le\varepsilon\) uniformly at each scale, together with explicit control of large-field region activities. Neither follows from (2)–(3).

## 6. Relation to known results

Balaban, *Ultraviolet stability of three-dimensional lattice pure gauge field theories*, Commun. Math. Phys. 102 (1985) 255–275, establishes ultraviolet stability for regular 3D Wilson lattices. Its use on Penrose-derived nonperiodic spacetime complexes needs independent geometric and covariance estimates. Ultraviolet stability is not a physical mass-gap proof.

## Verdict

Proved: a gauge-invariant split, uniform mean density of bad plaquettes, and uniformly small *relative local action error* on good plaquettes. Not proved: exponential large-field region suppression, a localized Penrose background-field propagator, small connected residual polymer norm, repeated RG stability, Hamiltonian gap, and continuum R2.
