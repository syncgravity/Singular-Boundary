# R3-IR — Balanced-tree analytic-radius majorant obstruction (2026-11-01)

**Status:** theorem about the numerical constant in the published PW upper estimate, NOT about divergence of physical SU(2) coefficients.

For touching intervals with union length t, the established inverse/bilinear estimate has constant
`M_t(δ)=16t sqrt[(D²F_t)(z)(D²G_t)(z)]`, where `z=exp(-2δ)`, `D=z∂_z`, `F_t=((1+z)/(1-z)^3)^t`, `G_t=(1-z)^(-t)`.

Direct differentiation yields `D log F_t=t[z/(1+z)+3z/(1-z)]` and `D log G_t=tz/(1-z)`. As their second logarithmic derivatives are nonnegative,
`M_t(δ) >= 48t^3 z^2 (1+z)^(t/2)(1-z)^(-2t-2) >=48t^3 exp(-4δ)(2δ)^(-2t-2)`.

Consider a balanced binary tree of n=2^L touching singleton face leaves. At level k there are n/2^k unions of length t=2^k. If the same unrefined estimate is applied at each node with loss δ_k>0 and total fixed root-to-leaf radius budget Σδ_k≤σ₀≤1/2, the product of its numerical constants is
`P_n=∏_{k=1}^L M_{2^k}(δ_k)^(n/2^k)`.
Dropping nonnegative terms in the displayed lower bound and using AM-GM,
`log P_n >=2n Σ_k log(1/(2δ_k))-4nσ₀ >=2nL log[L/(2σ₀)]-4nσ₀`.
This grows at least as n log n log log n, and hence this *particular fully expanded scalar majorant* cannot be bounded by C^n(n!)^s for any fixed s as n→∞.

**Scope and limits.** Lower bounding a previously proved **upper-bound constant** does NOT lower bound the bilinear operator or actual score coefficients. This obstruction neither proves physical-series divergence nor negates the independent connected L² Gevrey-8 theorem. It specifically rules out obtaining a fixed-Gevrey estimate from naive repeated use of this full-union PW constant along all nodes of balanced touching-support trees. It does not rule out improvements through cancellations, alternative tree reorganizations, or refined boundary-local estimates.

**Next obligation:** Derive a shared-link/boundary-localized PW gradient estimate without full-union factor (1-z)^(-2t), and prove compatible rooted aggregation. Independently audit the shared-link Γ sign in earlier low-order recursions before trusting numerical coefficients.

A complete exposition and executable 30-case numerical consistency checker are preserved in the companion downloadable proof audit produced in the research conversation.
