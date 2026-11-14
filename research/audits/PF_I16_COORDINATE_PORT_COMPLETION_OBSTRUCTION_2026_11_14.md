# PF-I16 — Obstruction to naive coordinate-preserving port completion

**Date:** 2026-11-14  
**Status:** naive extension of the global port-completion injection is REFUTED; a different support-labelled cancellation encoding remains OPEN  
**Scope:** finite incidence systems with row support size at most eight. No P0–P5 gate is promoted.

## 1. The exact issue

The global interval-forest completion inserts a connector row \(c\) into an edge \((a,b)\) of another component whenever \(a<c<b\). This preserves the temporal cut-crossing profile, but it does not preserve support: from \(c\in(a,b)\) one cannot infer that \(X_a\cap X_c\ne\varnothing\) or \(X_b\cap X_c\ne\varnothing\).

The failure occurs even when every row uses at most two links and the original link-labelled union is already a support tree.

## 2. Four-row exact incidence witness

Take four rows with supports
\[
X_1=\{e\},\quad X_2=\{f\},\quad
X_3=\{e,g\},\quad X_4=\{f,g\}.
\tag{2.1}
\]
Thus the support-overlap graph is exactly the path
\[
1\;-\;3\;-\;4\;-\;2,
\tag{2.2}
\]
with edge witnesses \(e,g,f\), respectively.

Choose one non-singleton block for each link:
\[
B_e=\{1,3\},\qquad B_f=\{2,4\},\qquad B_g=\{3,4\}.
\tag{2.3}
\]
The associated increasing link paths are
\[
C_e:1-3,\qquad C_f:2-4,\qquad C_g:3-4.
\tag{2.4}
\]
Their union \(H\) is the connected support tree \(1-3-4-2\). In particular, no support-tree completion is needed: \(H\) itself is a valid spanning tree.

But the two disjoint component hulls
\[
I_e=[1,3],\qquad I_f=[2,4]
\]
overlap. Applying the old port operation with connector \(c=2\) from \(C_f\) to the edge \((1,3)\) of \(C_e\) replaces that edge by
\[
(1,2),\ (2,3).
\]
The first new edge is not a support edge, because
\[
X_1\cap X_2=\varnothing.
\]
Likewise, inserting \(c=3\) into \((2,4)\) would create \((2,3)\), also unsupported. The port operation preserves the temporal cut profile but violates coordinate preservation.

This is a concrete obstruction to the proposed *unmodified* coordinate-preserving port-completion map. It is not a counterexample to the desired support-tree-sum cumulant inequality: the original union \(H\) already contains a support spanning tree.

## 3. Why this does not invalidate coordinate localization

For a fixed link \(e\), expand each ordered semigroup gap in that coordinate as either \(\Pi_e\) or \(Q_t^e\). At a row not incident to \(e\), the row multiplication is the identity in that coordinate. Therefore, if the two adjacent gap choices differ, the coordinate word contains either
\[
Q_s^e\Pi_e=0\quad\hbox{or}\quad \Pi_eQ_t^e=0.
\]
If both choices are \(Q\), they compose by the semigroup law; if both are \(\Pi\), they compose by idempotence. At the stationary endpoints, an unanchored \(Q\)-run vanishes because \(Q_t^e\mathbf1=(Q_t^e)^*\mathbf1=0\).

It follows that every surviving maximal \(Q^e\)-run is anchored at rows incident to \(e\), and its temporal interval can be contracted across intervening nonincident rows. At an incident row the multiplication need not commute with \(Q^e\), so the run is cut there. The resulting interval endpoints share \(e\).

This spells out the zero-product step in the coordinate-localization audit: a \(\Pi/Q\) switch across a row outside the support is annihilated; only a \(Q/Q\) run telescopes.

## 4. Corrected combinatorial target

For each signed link-partition term, let \(H\) be its connected link-labelled support multigraph. Two distinct operations must not be conflated:

1. **Termwise temporal domination:** choose any spanning tree \(T\subseteq H\). Since every discarded exponential factor lies in \([0,1]\),
   \[
   \prod_{a\in E(H)}e^{-\Delta_0|t_{i(a)}-t_{j(a)}|}
   \le
   \prod_{\{i,j\}\in E(T)}e^{-\Delta_0|t_i-t_j|}.
   \]
   This retains support and requires only edge deletion, not vertex insertion. It does not preserve the full cut profile, and it does not control how many signed terms map to the same tree.

2. **Cancellation-preserving coefficient control:** group the signed link-partition expansion before absolute values and prove that the grouped coefficient mass assigned to each support tree (or to a controlled family of support trees) is at most exponential in \(r+\sum_e|I_e|\). This is the real unresolved issue. The global port-completion injection proves an analogous estimate only after forgetting coordinate labels.

Thus exact cut-profile preservation is sufficient for the global temporal theorem but is not necessary for termwise upper bounds. A support proof may use tree deletion, provided it solves the coefficient/fiber problem independently.

## 5. Revised status and next lemma

- Coordinate \(Q/\Pi\) switch annihilation at nonincident rows: **ESTABLISHED**.
- Localization of surviving coordinate \(Q\)-runs to shared-link endpoints: **ESTABLISHED**, with the zero-product qualification in Section 3.
- Connected link-labelled support multigraph for each connected-join term: **ESTABLISHED**.
- Termwise support-tree domination by deleting edges from that multigraph: **ESTABLISHED**.
- Naive use of global port completion with support labels: **REFUTED** by (2.1)–(2.4).
- Exponential bound on the *signed grouped coefficient mass* after support-tree deletion: **OPEN**.
- Support-tree-sum cumulant inequality, smooth face/pair specialization, marked-root sum, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

The next useful calculation is not to force cut-profile-preserving subdivision. It is to derive an exact signed grouping indexed by support spanning trees (or support-tree edge sets) and bound its coefficient mass. The four-row witness shows why coordinate labels must be retained through that grouping.

No P0–P5 acceptance status is promoted.
