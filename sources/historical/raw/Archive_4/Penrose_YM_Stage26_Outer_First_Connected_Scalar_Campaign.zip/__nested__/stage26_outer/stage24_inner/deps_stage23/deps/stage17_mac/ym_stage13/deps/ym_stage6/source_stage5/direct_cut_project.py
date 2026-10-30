"""Explicit 2D Z^5 cut-and-project Penrose rhombus complex.

The graph is generated from *acceptance-window membership* and Z^5 basis
neighbor squares. It does not call the old dual-pentagrid face generator.
This is a finite open disk patch, not a 3D construction.

Coordinates: e_j=(cos(2*pi*j/5),sin(2*pi*j/5)), e'_j=(cos(4*pi*j/5),sin(4*pi*j/5)).
Canonical regular pentagrid offsets sum to 1; internal windows are the four
hypersimplex slices conv{sum_{j in A} e'_j: |A|=h}, h in {1,2,3,4}.
"""
from __future__ import annotations
from collections import Counter, deque
from dataclasses import dataclass
from itertools import combinations, product
from typing import Sequence
import numpy as np
from scipy.spatial import ConvexHull

THETA = 2 * np.pi * np.arange(5) / 5
PAR = np.column_stack([np.cos(THETA), np.sin(THETA)])
PERP = np.column_stack([np.cos(2 * THETA), np.sin(2 * THETA)])
HULLS = {h: ConvexHull(np.array([PERP[list(idx)].sum(axis=0)
                               for idx in combinations(range(5), h)]))
         for h in range(1, 5)}
DEFAULT_GAMMA = np.array([.07, .19, .31, .43, .61])
OFFSET_STEP = np.array([.119, .241, .347, .063, .173])

@dataclass
class Complex:
    labels: list[tuple[int, ...]]
    xy: np.ndarray
    faces: list[tuple[int, int, int, int]]
    edges: list[tuple[int, int]]


def gamma_for_offset(offset: int = 0) -> np.ndarray:
    g = (DEFAULT_GAMMA + OFFSET_STEP * offset) % 1
    return g + (1 - g.sum()) / 5


def internal_window(k: Sequence[int], gamma: np.ndarray, eps: float = 1e-9) -> bool:
    k = np.asarray(k, dtype=int)
    h = -int(k.sum()) - 1
    if h not in HULLS:
        return False
    y = -(k + gamma) @ PERP
    eq = HULLS[h].equations
    return bool(np.max(eq[:, :2] @ y + eq[:, 2]) <= -eps)


def build(radius: float = 7.0, offset: int = 0) -> tuple[Complex, np.ndarray]:
    """Open patch made of entire rhombi with all vertices in |x|<=radius.

    A margin is explored to avoid inferring membership from the finite face crop.
    Every accepted vertex found is reached by Z^5 basis-step BFS; the finite
    construction is checked separately against the dual pentagrid enumeration.
    """
    if radius < 2.5: raise ValueError('radius should be >= 2.5')
    gamma = gamma_for_offset(offset)
    def xy(k): return np.asarray(k, dtype=float) @ PAR
    seeds = {tuple(k) for k in product(range(-2, 2), repeat=5)
             if np.linalg.norm(xy(k)) <= 1.4 and internal_window(k, gamma)}
    if not seeds: raise RuntimeError('no interior seed')
    explored = set(seeds)
    queue = deque(sorted(seeds))
    extent = radius + 2
    while queue:
        k = queue.popleft()
        for i in range(5):
            for delta in (-1, 1):
                m = list(k); m[i] += delta; m = tuple(m)
                if m in explored or np.linalg.norm(xy(m)) > extent: continue
                if internal_window(m, gamma):
                    explored.add(m); queue.append(m)
    kept = {k for k in explored if np.linalg.norm(xy(k)) <= radius}
    face_labels = []
    for k in sorted(kept):
        b = np.asarray(k, dtype=int)
        for i, j in combinations(range(5), 2):
            p = b.copy(); p[i] += 1
            q = p.copy(); q[j] += 1
            r = b.copy(); r[j] += 1
            face = (tuple(b), tuple(p), tuple(q), tuple(r))
            if all(v in kept for v in face):
                # Consistent counterclockwise face orientation.
                cross = np.linalg.det(PAR[[i, j]])
                if cross < 0: face = (face[0], face[3], face[2], face[1])
                face_labels.append(face)
    verts = sorted({tuple(int(x) for x in k) for f in face_labels for k in f})
    ids = {k: i for i, k in enumerate(verts)}
    faces = [tuple(ids[v] for v in f) for f in face_labels]
    edges = sorted({tuple(sorted((f[i], f[(i + 1) % 4])))
                    for f in faces for i in range(4)})
    return Complex(verts, np.asarray(verts, dtype=float) @ PAR, faces, edges), gamma


def face_label_sets(g: Complex):
    return {frozenset(g.labels[i] for i in f) for f in g.faces}


def validate(g: Complex, gamma: np.ndarray) -> dict:
    n = len(g.labels)
    if n == 0: raise AssertionError('empty graph')
    degree = np.zeros(n, dtype=int)
    edge_use = Counter()
    edges = set(g.edges)
    for a, b in edges:
        degree[a] += 1; degree[b] += 1
        assert np.abs(np.asarray(g.labels[a]) - g.labels[b]).sum() == 1
    for f in g.faces:
        assert len(f) == 4 and len(set(f)) == 4
        pts = g.xy[list(f)]
        signed_double_area = sum(np.linalg.det(np.array([pts[i], pts[(i+1)%4]])) for i in range(4))
        assert signed_double_area > 0.00001
        for i in range(4):
            e = tuple(sorted((f[i], f[(i+1)%4])))
            assert e in edges
            edge_use[e] += 1
    assert set(edge_use) == edges
    assert all(v in (1, 2) for v in edge_use.values())
    assert all(internal_window(k, gamma) for k in g.labels)
    assert int(max(degree)) <= 7
    assert n - len(g.edges) + len(g.faces) == 1
    adjacency = [set() for _ in g.labels]
    for u, v in g.edges:
        adjacency[u].add(v);adjacency[v].add(u)
    seen = {0}; todo = deque([0])
    while todo:
        for j in adjacency[todo.popleft()]:
            if j not in seen:seen.add(j);todo.append(j)
    assert len(seen) == n
    counts = Counter(degree)
    return {
        'vertices': n, 'edges': len(g.edges), 'faces':len(g.faces),
        'euler':n-len(g.edges)+len(g.faces), 'boundary_edges':sum(v == 1 for v in edge_use.values()),
        'max_degree':int(max(degree)), 'degree_histogram':{str(k):int(v) for k,v in sorted(counts.items())},
        'height_classes':sorted({int(-sum(k)-1) for k in g.labels}),
        'exact_normalized_m2':float(np.mean(degree**2 + degree)),
        'mean_degree':float(np.mean(degree)),
        'gamma_sum':float(gamma.sum()),
    }
