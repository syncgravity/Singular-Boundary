# PF-I16: guarded mutual-survival diamond lemma

Date: 2026-11-18

Status: **proved for the target-side guarded reverse relation, for every finite port tree.** Canonical source/fiber compatibility and mixed-fiber Hall remain separate open obligations.

## 1. Definitions

Let T be a tree on an ordered finite port set V. A two-port set J={a,b} is a valid guarded reverse mark if there is a unique pair e_J={u,v} disjoint from J such that, on X_J=J union {u,v}:

1. T[X_J] is exactly one of the three ordered local trees
   [
   S_0={x_1x_2,x_2x_3,x_2x_4},quad
   S_1={x_1x_2,x_2x_3,x_3x_4},quad
   S_2={x_1x_3,x_2x_3,x_3x_4};
   ]
2. every edge of T incident to J is in this local tree, with exact incidence equality;
3. e_J is not an edge of the local target tree (no reinsertion);
4. the open intervals e_J and J have positive-length overlap.

The inverse target is
[
P_J(T)=T[Vsetminus J]cup{e_J}.
]
For any valid mark, all three edges of its local tree are incident to J. In particular,
[
|delta_T(J)|=3,
	ag{1}
]
where (delta_T(J)) denotes the set of T-edges incident to at least one vertex of J.

The rank census in `PF_I16_MUTUAL_REVERSE_MARK_SURVIVAL_CENSUS_2026_11_18.md` verifies directly that the only possible mark ranks are (1,3), (2,3), and (2,4), with the corresponding local patterns listed there. This makes (1) immediate from the three displayed patterns.

## 2. Lemma

**Theorem (guarded mutual-survival diamond).** Let J,K be disjoint valid guarded reverse marks of T. Suppose K is still a valid guarded reverse mark of P_J(T), and J is still a valid guarded reverse mark of P_K(T). The second inverse witnesses may differ from the original witnesses. Then the two double inverses agree:
[
P_K^{,J}(P_J(T))=P_J^{,K}(P_K(T)).
	ag{2}
]
Here the superscript indicates that the second mark's witness is recomputed in the first parent tree.

### Proof

Let
[
h=|E_T(J,K)|
]
be the number of T-edges joining J to K. Since J and K are disjoint, the incident edges of K after reversing J are exactly
[
delta_{P_J(T)}(K)
=
igl(delta_T(K)setminus E_T(J,K)igr)
cup
egin{cases}
{e_J},&e_Jcap K
earnothing,\
arnothing,&e_Jcap K=arnothing.
end{cases}
	ag{3}
]
The added edge e_J is not an edge of T by the no-reinsertion guard, so the union in (3) adds one new edge precisely when e_J meets K. Because K is valid both before and after the projection, (1) gives
[
3=|delta_{P_J(T)}(K)|
 =3-h+mathbf 1_{{e_Jcap K
earnothing}}.
]
Thus
[
h=mathbf 1_{{e_Jcap K
earnothing}}.
	ag{4}
]
Applying the same argument with J and K interchanged gives
[
h=mathbf 1_{{e_Kcap J
earnothing}}.
	ag{5}
]
There are two cases.

**Case I: h=0.** Equations (4)–(5) show that e_J is disjoint from K and e_K is disjoint from J. No edge joining J to K is removed in either projection. Hence the K-incidence pattern and its external endpoints are unchanged by P_J, and conversely. By fixed-mark inverse uniqueness, the second inverse witnesses remain e_K and e_J respectively.

These two old edges must be distinct: if e_J=e_K, then after the J inverse that edge lies inside K's four-port support, contradicting the K no-reinsertion guard and exact induced local pattern. Therefore both orders produce
[
T[Vsetminus(Jcup K)]cup{e_J,e_K}.
	ag{6}
]

**Case II: h=1.** Equations (4)–(5) show that e_J meets K and e_K meets J. Each meets the opposite mark in exactly one endpoint. For example, if both endpoints of e_J lay in K, then all three edges incident to J in its local four-port tree would lie within J union K. At most one of those three edges can be internal to J, so at least two would join J to K, contradicting h=1. The same argument applies to e_K.

Consequently write
[
e_J={k,a},quad kin K, a
otin Jcup K,
qquad
e_K={j,b},quad jin J, b
otin Jcup K.
	ag{7}
]
There is exactly one T-edge between J and K. In P_J(T), that edge is deleted, j is deleted, b remains as one external endpoint of K, and the restored edge e_J supplies the other external endpoint a. Since K is valid in P_J(T), these are distinct, and its unique inverse edge is {a,b}. Thus the J-then-K double inverse is
[
T[Vsetminus(Jcup K)]cup{a b}.
	ag{8}
]
Symmetrically, in P_K(T), the unique inverse edge for J is also {a,b}; the K-then-J double inverse is exactly (8).

The two cases exhaust (4)–(5), proving (2). (square)

## 3. Exact content and limits

The theorem proves a target-side diamond whenever the two disjoint marks are mutually valid after the opposite inverse. It does not say that every pair of disjoint marks is mutually surviving. Equations (4)–(5) give the useful dichotomy:

- **No-cross case:** h=0, neither restored edge meets the opposite mark, and the two original inverse edges are distinct; both are restored in either order.
- **One-cross case:** h=1, each original restored edge meets the opposite mark in exactly one endpoint; both orders replace the unique J-K edge by the same edge {a,b} between the two surviving external endpoints.

The theorem does not require disjoint four-port supports. The finite census found both the one-shared-old-endpoint no-cross geometry and the two-cross-endpoint one-cross geometry, but the proof above does not depend on those finite observations.

## 4. Consequence for the proof program

The target-side reverse-mark relation is locally confluent on every mutually surviving pair. This supplies a rigorous diamond for organizing two-step target inverses and removes the need to assume disjoint supports in that local argument.

It does **not** imply a canonical diamond for source fibers. For fibers F=(p,J) and G=(q,K), one must still establish independently that the common twice-reversed target belongs to the relevant canonical leaf-last neighborhoods of the appropriate parent sources. Nor does pairwise local confluence provide an arbitrary-family target-capacity estimate or mixed-fiber Hall.

The next obligation is therefore canonical compatibility: characterize exactly when the second reverse mark selected by the target-side diamond is the canonical leaf of the corresponding parent overlap-tree source, in both orders. Only after that source-level condition is established should the diamond be used in a weighted fiber expansion argument.

No all-orders mixed-fiber Hall theorem or unconditional weighted one-link inequality is claimed.
