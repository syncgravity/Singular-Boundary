# Penrose 54-face contraction audit: what can be certified from current data

Date 2026-10-27. The currently mounted `R3_contraction_certificate_2026_10_27` contains `FORMAL_NOTE.md`, `certify_B.py`, and an illustrative 2x2 input matrix. It does **not** contain the canonical 14-face insertion Q, the explicit 54-face list, the 36 original link names, or exact nonabelian pair-staple loop identities. The Phase III zip contains a verified direct-Z5 *spatial* generator, but does not uniquely specify Q. The earlier reported Q counts cannot be used to reconstruct a unique historical Q. Consequently **there is no certified 54x54 Penrose matrix B** in this response.

## 1. Valid finite theorem

For a fixed list G of retained plaquettes and each p in G an incident edge e(p), set x_p=lambda E[d(W_p)]. SU(2) link heat-bath integration implies x_p <= 3/2 + lambda E[m_{e(p)}]. If, for every SU(2) link assignment, m_{e(p)} <= sum_{r in G} B_{pr}d(W_r), with B nonnegative and *independently justified by exact group-word identities*, then x <= (3/2)1 + Bx. If a vector h>0 obeys Bh <= theta h with theta<1, then x <= (3/2)(I-B)^(-1)1 and the desired finite-face bound follows uniformly in the exterior volume. The required statement about the pointwise SU(2) inequality is mathematically distinct from the spectral test.

## 2. A genuine local no-go: naive self-feedback

The trivial bound m_e<=S_e cannot be promoted to a uniform strict contraction m_e<=c S_e, c<1. For an SU(2) two-plaquette star with opposite staples a and -a, one has S_e(u)=2 and m_e=2 for **every** link u. Thus necessarily c>=1. Any nonnegative B with a self-loop coefficient B_pp>=1 has rho(B)>=1 (because rho(B)>=B_pp). Therefore matrix construction by merely distributing the inequality m_e<=S_e among the same plaquettes cannot guarantee rho<1; genuine Bianchi-word cancellation or Gibbs-probabilistic suppression is necessary. This is a local algebraic obstruction, **not** a proof that all candidate Penrose matrices must fail.

## 3. Leakage and the missing certificate

A valid candidate must identify G, p->e(p), and for each row a finite word identity and a proved bound including all exterior faces it mentions. If m <= B d_G + C d_ext, spectral contraction of B still leaves (I-B)^(-1)C E[d_ext]. The exterior term needs its own argument. A complete audit requires the *actual* face words for Q14, the 54 retained Bianchi-fill words, the 36-link H indexing, and all stars against the full retained R. Current mounted files do not supply this relative certificate.

## 4. The next executable certification path

- Obtain the canonical Q14 index/vertex-word list and its retained Bianchi decomposition (not merely its sizes).
- Generate the 54x36 incidence, link-star closures, and all pair-staple loop words, preserving noncommutative order.
- Establish rowwise inequalities by explicit SU(2) group identities (or precise interval bounds) before filling B.
- Compute rho(B) and rational supersolution Bh<=theta h with theta<1, and independently audit all boundary leakage. Do not call a numerical eigenvalue alone a proof.
- If unavoidable self-feedback or leakage defeats finite closure, revert to a joint Gibbs transport or a multi-scale estimate rather than asserting local contraction.

**Status:** conditional matrix theorem proved; naive-star strict contraction ruled out; original Penrose 54-face spectral test **not executable from the currently supplied historical incidence data**; unrestricted R3 and volume-uniform 54-face Gibbs bound remain open.
