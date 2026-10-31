# R3-IR: Three-moment Wilson-force tail obstruction

**31 October 2026. Status:** exact sharp abstract positive-spectral-measure obstruction preserving three Wilson-derived local constraints; **not** a counterexample realized by a completed-cage Wilson ground state and **not** a proof of a continuum mass gap.

## Wilson source constraints

For a boundary link e of a deleted face with one retained neighboring simple face g, the archived force correlation is
\(C_e(t)=\sum_a\langle F_a,e^{-t(H_f^--E_0)}F_a\rangle\ge0\). The earlier exact identities prescribe:

\[
C_e(0)=\frac{b_g^2}{4}(1-\mathbb E p_g^2)=:c,\quad
-C'_e(0)=\frac{b_g^2 A_g}{16}(2+\mathbb E p_g^2)=:d,\quad
\int_0^\infty C_e(t)dt=\frac{3b_g}{8}\mathbb E p_g=:s.
\]

The desired full link-score norm is \(S_0=\int_0^\infty t C_e(t)dt\). Its upper control does **not** follow from the preceding three scalar constraints, even if their precise Wilson moment relationships and the plaquette inequalities \(-1\le p_g\le1\) are imposed.

## Exact two-point counterfamily

Normalize \(m=d/c>0\), \(r=s/c>0\), and suppose \(mr>1\). For every \(0<\epsilon<\min(m,1/r)\), set

\[
\lambda_\epsilon=\frac{m-\epsilon}{1-r\epsilon}>m,\qquad
q_\epsilon=\frac{\lambda_\epsilon-m}{\lambda_\epsilon-\epsilon}\in(0,1),
\]

\[
C_\epsilon(t)=c\big(q_\epsilon e^{-\epsilon t}+(1-q_\epsilon)e^{-\lambda_\epsilon t}\big).
\]

Algebra gives, **for every epsilon exactly**,

\[
C_\epsilon(0)=c,\qquad -C'_\epsilon(0)=cm=d,\qquad
\int_0^\infty C_\epsilon(t)dt=cr=s.
\]

But \(q_\epsilon\sim (mr-1)\epsilon/m\), so

\[
\int_0^\infty t C_\epsilon(t)dt
=c\left(\frac{q_\epsilon}{\epsilon^2}+\frac{1-q_\epsilon}{\lambda_\epsilon^2}\right)
\sim \frac{c(mr-1)}{m\epsilon}\longrightarrow\infty.
\]

This is a positive Laplace mixture and is realized by a two-dimensional strictly positive diagonal operator and a force vector with the corresponding squared spectral amplitudes. It is an **abstract spectral response**, not a construction of a Wilson lattice ground state.

## Values compatible with local Wilson moment constraints

Choose \(b_g=2\), \(A_g=2\), \(\mathbb E p_g=1/2\), \(\mathbb E p_g^2=1/2\). These moment values are feasible for a random variable in [-1,1] (e.g. p=0 or 1 with equal weights). They give \(c=1/2\), \(d=5/4\), \(s=3/8\), hence \(m=5/2\), \(r=3/4\), \(mr=15/8>1\). Thus the counterfamily satisfies all three numerical local Wilson sum rules exactly, along with their elementary trace inequalities. We **do not** assert those moments are realized by any actual deleted-face vacuum, nor that arbitrary measures matching them obey further Wilson correlation identities.

## Consequence

Even knowing the **exact** local Wilson force variance, Dirichlet initial slope and local f-sum cannot imply a uniform upper bound on low-energy score strength. A fourth, genuinely dynamical constraint is necessary: a low-energy spectral weight suppression strong enough to integrate \(\lambda^{-2}\), a long-time correlation bound, or a physical collar comparison not relying on these moments alone. The unweighted radial current requires still more anti-depletion information.

**Unproved gates:** uniform long-time Wilson force tail; \(\sup_f\mathfrak T_{f,h}=o(h^{-1/4})\); connected covariance and continuum Yang–Mills mass gap.

## Reproduction

Run `python verify.py`. Its five exact two-atom constructions retain c=0.5, d=1.25, s=0.375 to numerical precision while the time-weighted integral increases from 1.967 to 17500.22 as epsilon decreases from 0.1 to 1e-5. This is deterministic algebra, not Monte Carlo.