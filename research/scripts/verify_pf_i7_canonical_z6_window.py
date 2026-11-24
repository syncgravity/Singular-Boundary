#!/usr/bin/env python3
"""Independent certificate for the canonical Z^6 -> R^3_perp acceptance window.

The six rows of E_PERP are the projected coordinate generators.  The
canonical window for the centred unit 6-cube is their zonotope
    W = sum_j [-1/2, 1/2] g_j.
Its facets are perpendicular to cross products g_i x g_j, not to the
six generators themselves.  This script does not modify or import the
historical source generator; it independently reconstructs its basis.

Dependencies: numpy, scipy.
"""
from __future__ import annotations

from itertools import combinations, product
import json
import math

import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection

PHI = (1.0 + math.sqrt(5.0)) / 2.0
SOURCE_PATH = (
    "syncgravity/Tau:public/science/mathematical-physics/dissertation/"
    "supplementary/Paper6-7_final/Finiteness/"
    "paper67_icosahedral_finiteness_v2.py"
)
SOURCE_SHA256 = "e3fdae681c2288534a0629db64907eb8f8a86a0c"


def perpendicular_generators() -> np.ndarray:
    """Return the six normalized Galois-conjugate rows used by the source."""
    raw = np.array(
        [
            [1, -1 / PHI, 0],
            [1, 1 / PHI, 0],
            [0, 1, -1 / PHI],
            [0, 1, 1 / PHI],
            [-1 / PHI, 0, 1],
            [1 / PHI, 0, 1],
        ],
        dtype=float,
    )
    return raw / np.linalg.norm(raw, axis=1)[:, None]


def canonical_facet_system(g: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return 15 unoriented unit facet normals and their zonotope supports."""
    normals: list[np.ndarray] = []
    for i, j in combinations(range(6), 2):
        n = np.cross(g[i], g[j])
        norm = np.linalg.norm(n)
        if norm < 1e-12:
            raise AssertionError(f"parallel generators at pair {(i, j)}")
        n /= norm
        # Fix the sign to identify n and -n as the same facet-normal axis.
        nz = np.flatnonzero(np.abs(n) > 1e-12)
        if n[nz[0]] < 0:
            n = -n
        if not any(np.linalg.norm(n - old) < 1e-10 for old in normals):
            normals.append(n)
    normals.sort(key=lambda x: tuple(np.round(x, 12)))
    if len(normals) != 15:
        raise AssertionError(f"expected 15 normal axes, found {len(normals)}")
    supports = np.array([0.5 * np.abs(g @ n).sum() for n in normals])
    return np.asarray(normals), supports


def inside_canonical_window(
    r_perp: np.ndarray, normals: np.ndarray, supports: np.ndarray,
    tolerance: float = 1e-10,
) -> bool:
    """Strict interior membership in the projected centred unit 6-cube."""
    return bool(np.all(np.abs(normals @ np.asarray(r_perp)) < supports - tolerance))


def unique_hull_planes(hull: ConvexHull, tolerance: float = 1e-9):
    """Group Qhull's triangulated simplices into geometric polygon facets."""
    planes: list[tuple[np.ndarray, float]] = []
    for eq in hull.equations:
        n = eq[:3] / np.linalg.norm(eq[:3])
        d = eq[3] / np.linalg.norm(eq[:3])
        if not any(
            np.linalg.norm(n - old_n) < tolerance and abs(d - old_d) < tolerance
            for old_n, old_d in planes
        ):
            planes.append((n, float(d)))
    return planes


def main() -> None:
    g = perpendicular_generators()
    gram = g.T @ g
    if not np.allclose(gram, 2 * np.eye(3), atol=1e-12):
        raise AssertionError(f"perpendicular frame Gram matrix changed: {gram}")

    cube_coefficients = np.asarray(list(product((-0.5, 0.5), repeat=6)))
    projected_cube_vertices = cube_coefficients @ g
    hull = ConvexHull(projected_cube_vertices)
    planes = unique_hull_planes(hull)

    facet_vertex_counts = []
    rhombus_side_spread = []
    for n, d in planes:
        face_points = projected_cube_vertices[
            np.abs(projected_cube_vertices @ n + d) < 1e-8
        ]
        if len(face_points) != 4:
            raise AssertionError(f"expected rhombic quadrilateral, got {len(face_points)}")
        # Order the four coplanar points in a 2D affine coordinate system.
        center = face_points.mean(axis=0)
        _, _, vt = np.linalg.svd(face_points - center, full_matrices=False)
        planar = (face_points - center) @ vt[:2].T
        polygon = ConvexHull(planar)
        ordered = face_points[polygon.vertices]
        side_lengths = np.linalg.norm(
            np.roll(ordered, -1, axis=0) - ordered, axis=1
        )
        rhombus_side_spread.append(float(side_lengths.max() - side_lengths.min()))
        facet_vertex_counts.append(len(face_points))

    normals, supports = canonical_facet_system(g)
    expected_support = math.sqrt(1.0 + 2.0 / math.sqrt(5.0))
    if not np.allclose(supports, expected_support, atol=1e-12):
        raise AssertionError("canonical support values do not match the icosahedral frame")

    # Every facet plane found from the projected cube must be represented by
    # one of the 15 normal axes and the computed support value.
    for n, d in planes:
        if not any(
            min(np.linalg.norm(n - a), np.linalg.norm(n + a)) < 1e-8
            and abs(abs(d) - h) < 1e-8
            for a, h in zip(normals, supports)
        ):
            raise AssertionError("convex-hull facet missing from analytic H-representation")

    # Reproduce the historical six-slab polytope exactly as implemented.
    old_radius = math.sqrt(2.0 / (PHI + 2.0)) * 1.15
    old_halfspaces = np.vstack(
        [
            np.column_stack([g, np.full(6, -old_radius)]),
            np.column_stack([-g, np.full(6, -old_radius)]),
        ]
    )
    old_poly = HalfspaceIntersection(old_halfspaces, np.zeros(3))

    unique_projected_points = np.unique(np.round(projected_cube_vertices, 12), axis=0)
    result = {
        "scope": "finite-dimensional exact-shape audit of the canonical projected-cube window",
        "source": {"path": SOURCE_PATH, "sha256": SOURCE_SHA256},
        "construction": "W = E_perp^T([-1/2,1/2]^6), a zonotope generated by the six source rows",
        "canonical_window": {
            "projected_cube_corners": 64,
            "distinct_projected_corners": int(len(unique_projected_points)),
            "convex_hull_vertices": int(len(hull.vertices)),
            "facets": int(len(planes)),
            "edges_by_euler": int(len(hull.vertices) + len(planes) - 2),
            "facet_vertex_counts": sorted(facet_vertex_counts),
            "all_facets_are_rhombi": max(rhombus_side_spread) < 1e-8,
            "maximum_rhombus_side_spread": max(rhombus_side_spread),
            "facet_normal_axes": int(len(normals)),
            "facet_supports": sorted(set(np.round(supports, 12).tolist())),
            "exact_common_support_expression": "sqrt(1 + 2/sqrt(5))",
            "common_support_numeric": float(expected_support),
            "h_representation": (
                "|r_perp dot n_ij| <= (1/2) sum_k |g_k dot n_ij|, "
                "n_ij = normalize(g_i cross g_j), 0 <= i < j <= 5"
            ),
        },
        "historical_six_slab_window": {
            "radius": old_radius,
            "halfspace_boundaries": int(len(old_halfspaces)),
            "vertices": int(len(old_poly.intersections)),
            "facets": 12,
            "facet_type": "pentagons",
            "matches_canonical_rhombic_triacontahedron": False,
        },
        "basis_checks": {
            "perpendicular_gram_matrix": gram.tolist(),
            "all_generator_norms_one": bool(np.allclose(np.linalg.norm(g, axis=1), 1.0)),
        },
        "scope_limit": (
            "This certifies the shape and membership inequalities for the standard "
            "centred-unit-cube cut-and-project window. It does not regenerate the "
            "historical accepted vertex set, graph, spectra, or thermodynamic limit."
        ),
    }
    assert len(hull.vertices) == 32
    assert len(planes) == 30
    assert sorted(facet_vertex_counts) == [4] * 30
    assert len(old_poly.intersections) == 20
    assert result["canonical_window"]["edges_by_euler"] == 60
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
