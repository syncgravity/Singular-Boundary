# Penrose interacting gauge Hamiltonian: a local-to-global spectral-gap theorem

26 October 2026. **Status:** exact conditional theorem and proof; unconditional strong-coupling verification on Penrose patches is outstanding.

## Setup
Let G=(V,E,F) be a finite connected face complex, including any face-complete Penrose rhombus patch with free spatial boundary. Set X=SU(2)^E with normalized product Haar measure dU and its gauge-invariant subspace H_phys. Use the scalar, normalized group Laplacian on each edge and the weighted Kogut–Susskind operator

H_G= \sum_{e\in E} a_e(-\Delta_e) + B_G(U), \qquad B_G(U)=\sum_{f\in F} b_f(1-\tfrac12\operatorname{ReTr} U_f),

with a_e >= a_*>0 and 0<=b_f<=b^* and free boundary, and smooth bounded real magnetic potential. Finite-volume elliptic positivity implies a unique strictly positive normalized ground wavefunction \Psi_G, which is gauge invariant since the Hamiltonian commutes with gauge transformations and the ground state is simple. Put d\nu_G=\Psi_G^2 dU. (The ground-state uniqueness applies to the full L^2(X), so also to its invariant subspace.)

For an edge e, write Var_{\nu_G}(f | U_{E\setminus\{e\}}) for the variance in that edge conditional on the others. Define the corresponding conditional measure \nu_{G,e}(dU_e|U_{-e}).

## Theorem LS-1 (ground-state transform: exact)
For every f in the smooth form core, with \psi=\Psi_G f,

\langle \psi,(H_G-E_0)\psi\rangle=\sum_e a_e \int_X \|\nabla_e f\|^2 d\nu_G.

This is exact, with no approximation in the magnetic coupling or system size. The equality follows by expanding the quadratic form of \Psi f, subtracting the ground-state equation (H-E_0)\Psi=0 tested against \Psi |f|^2, and cancelling the cross terms. By form closure it holds on the appropriate domain.

## Theorem LS-2 (conditional volume-uniform interacting gap)
Assume constants c_loc>0 and K>=1 independent of G, such that, for every edge e and almost every fixed external link configuration,

Var_{\nu_{G,e}}(f) <= c_loc \int\|\nabla_e f\|^2 d\nu_{G,e},

and for all smooth f the variance tensorization bound holds:

Var_{\nu_G}(f) <= K\sum_e \int Var_{\nu_{G,e}}(f|U_{-e})d\nu_G(U_{-e}).

Then the physical gauge-invariant Hamiltonian satisfies

H_G-E_0 >= [a_*/(K c_loc)](I-|\Psi_G\rangle\langle\Psi_G|)

as quadratic forms on H_phys. The same bound is valid on all of L²(X).

**Proof.** For \psi perpendicular to \Psi_G, f=\psi/\Psi_G has zero \nu_G-mean and norm² equal to Var_{\nu_G}(f). Apply tensorization, then each edge's conditional Poincaré inequality. By LS-1 the resulting bound is <= (K c_loc/a_*)\langle\psi,(H-E_0)\psi\rangle. Rearranging yields the claim. Extend by density and the min-max principle. QED.

### What this theorem does not yet prove
Its hypotheses on the interacting ground-state measure are NOT verified here for the Penrose Wilson Hamiltonian. They are nontrivial strong-mixing estimates; the theorem is a rigorous local-to-global criterion, not a completed strong-coupling gap proof. It has no assumed C5/J dependence, and it does not give a continuum gap as a->0.

## Local geometry control (unconditional)
For genuine Penrose rhombus face patches, each face has exactly four edges and each spatial edge belongs to at most two faces. Therefore the magnetic interaction support has uniform range/overlap. In particular, changing one link affects at most two plaquette terms. Since 0<=1-(1/2)ReTr U_f <=2, its potential change is bounded by 4 b^*, independently of |V|. This **does not** by itself control the conditional distribution of \Psi_G², which is the ground-state measure, not a Gibbs weight exp(-B_G).

## Why a naive perturbation bound fails
The electric sector has an exactly volume-independent first nonzero eigenvalue >=(3/4)a_* in full tensor-product Hilbert space; gauge projection cannot decrease that spectral infimum. However, ||B_G|| <=2 b^* |F|. Using only global operator norm gives a spectral-gap bound that deteriorates with |F|. Locality alone is insufficient to replace the missing correlation control.

## Strong coupling strategy and literature qualification
The general idea of stability of a gapped product vacuum under sufficiently weak local perturbations goes back to rigorous quantum lattice perturbation theory. D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, Commun. Math. Phys. 261, 799–819 (2006), arXiv:math-ph/0412040, proves a uniform gap under specified smallness hypotheses on translation-invariant Z^nu lattice systems. Its published Theorem 1 cannot simply be cited as a theorem for an irregular Penrose graph. A new bounded-overlap, nontranslation-invariant extension, or a direct proof of the LS-2 hypotheses, is necessary. Kogut and Susskind, Phys. Rev. D 11, 395 (1975), gives the Hamiltonian formulation.

**Concretely outstanding:** prove c_loc and K uniformly when sup_f b_f/inf_e a_e <= eps_*(d_max,4,2), with epsilon independent of patch size and with free boundary conditions. Prove for the exact nonperiodic interaction hypergraph, or supply a published applicable general-graph theorem with all assumptions checked. If established, LS-2 delivers a rigorous strong-coupling volume-uniform physical Hamiltonian gap. To reach continuum Yang–Mills one still needs control along the physical continuum scaling trajectory, where such strong-coupling smallness may fail.

## C5 covariance
For a rotation-related Penrose family with transported a_e,b_f, the link-relabeling unitary U_r satisfies U_r H_G = H_{rG}U_r. The unique positive ground states correspond, as do c_loc and K. This transports an established bound around the C5 orbit but cannot create one or improve its constant merely through symmetry. The complex structure J remains supplementary geometry, with no proven gap enhancement.