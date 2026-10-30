# R3 — A volume-uniform strong-electric perturbation gate

Date: 2026-10-26

## Model

On a bounded-geometry planar rhombus complex (square or Penrose) let

\[H_G=\sum_{e\in E}a_e(-\Delta_e)+\sum_{f\in F}b_f(1-p_f),\quad p_f=\tfrac12\operatorname{Tr}_{1/2}W_f,\quad a_e>0,\ b_f\ge0.\]

Full link Hilbert space is the product \(\bigotimes_{e}L^2(SU(2))\). Gauge-invariant Hilbert space is the invariant closed subspace. \(-\Delta\) has first nonzero eigenvalue \(3/4\). On the full Hilbert space, the unperturbed vacuum is \(1\), unique, and its gap is \(\delta=3a_{\min}/4\). Each plaquette magnetic perturbation has operator norm \(\le2b_f\) and edge support four links; each link meets at most two faces.

## Verified local estimates

\[\|V_f/\delta\|\le\frac{2b_{\max}}{\delta}=\frac{8b_{\max}}{3a_{\min}}=:\epsilon_{\rm loc}.\]

The support-overlap graph degree is at most \(4(2-1)=4\), possibly less at the boundary (other faces sharing a vertex but no edge act on disjoint link tensor factors). There is no factor \(|F|\) in the per-interaction bound.

The full Hamiltonian is gauge invariant. The perturbatively unique full-space ground state is gauge invariant, since it must transform according to a one-dimensional representation of the connected product gauge group, and such a continuous nontrivial character does not exist. A full-space spectral gap implies at least the same lower bound on the spectrum restricted to the gauge-invariant sector, provided the latter has excited states.

## The standard perturbation-theorem gate

Yarotsky (J. Math. Phys. 45 (2004) 2134–2152; Commun. Math. Phys. 261 (2006) 799–819) establishes nondegenerate gapped ground states, uniform spectral gaps and exponential clustering for sufficiently weak bounded finite-range interactions around a product vacuum with uniformly gapped local terms. Local Hilbert spaces may be infinite dimensional in the latter treatment. The theorem's coupling threshold is existential and depends on the coarse-dimensionality, interaction range, and local incidence.

**Application caveat:** Many formulations of the theorem assume an interaction family indexed by translations of one finite motif on \(\mathbb Z^d\). To apply it to arbitrary finite Penrose complexes requires either (i) a verified bounded-multiplicity, bounded-range embedding of edge degrees of freedom into an augmented \(\mathbb Z^2\) lattice, together with a check that the exact selected theorem allows position-dependent local terms and inert auxiliary factors, or (ii) explicit verification of the polymer proof for the bounded-degree overlap graph. This note does not assert that such an extension has been proved just from the standard reference's abstract.

Under that verified uniform bounded-geometry extension, there is \(\epsilon_*(R,D)>0\) and \(\gamma_*>0\), independent of volume, such that \(\epsilon_{\rm loc}<\epsilon_*\) implies

\[\operatorname{gap}(H_G)\ge\gamma_*\delta.\]

For any complete centered interacting Wilson frame with synthesis operator a unitary \(B:\ell^2\to \mathscr H_{\rm phys}\ominus\mathbb C\Omega\), its physical-time correlation operator satisfies

\[\|B^*e^{-t(H_G-E_0)}B\|=e^{-t\operatorname{gap}_{\rm phys}(H_G)}\le e^{-\gamma_*\delta t}.\]

This gives an independent *dynamical* way to certify the correlation decay, once the perturbation-theory gate has been checked. It does not solve physical source complexity and locality.

## Continuum scaling obstruction

For the previously specified Penrose Hamiltonian prescription \(a_e=g_3^2/(2w_e)\), \(b_f=4/(g_3^2 h^2\sigma_f)\), with \(w_e\) and \(\sigma_f\) uniformly bounded above/below, \(b_{\max}/a_{\min}=\Theta((g_3^2 h)^{-2})\). Consequently \(\epsilon_{\rm loc}\to\infty\) as \(h\to0\) at fixed \(g_3^2>0\). The weak-magnetic perturbation domain is therefore not preserved along the quantum spatial continuum trajectory. No physical R2 continuum gap follows.

## Important distinction

Ordinary Weyl/Kato norm perturbation gives only \(\operatorname{gap}(H_G)\ge\delta-2\|V\|\ge \delta-4\sum_fb_f\), which is extensive and useless in the thermodynamic limit. The uniformly local cluster/polymer theorem is qualitatively stronger. No numerical value of \(\epsilon_*\) or \(\gamma_*\) was derived here. A purported all-coupling bound, or proof that physical refinement enters the cluster radius, would be unfounded.

## Sources

- D. A. Yarotsky, *Perturbations of ground states in weakly interacting quantum spin systems*, J. Math. Phys. 45 (2004), 2134–2152. DOI:10.1063/1.1705718.
- D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, Commun. Math. Phys. 261 (2006), 799–819. DOI:10.1007/s00220-005-1456-9.
- J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Phys. Rev. D 11, 395 (1975). DOI:10.1103/PhysRevD.11.395.
