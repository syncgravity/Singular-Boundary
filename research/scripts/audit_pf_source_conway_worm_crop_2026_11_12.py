#!/usr/bin/env python3
"""Audit source Conway-worm extraction and a common physical-window correction.

The authenticated predecessor archive is read but never modified. Only the
source PenroseTiling class, worm extraction/analysis functions, and substitution
invariant are AST-compiled; run_full_pipeline and all file/plot side effects are
excluded.
"""
import argparse
import ast
import collections
import hashlib
import json
import math
import time
import zipfile
from pathlib import Path
import numpy as np

ARCHIVE_SHA256 = "bdc3792b2f2be40736c20c4574ef72a6f1eded226fe28415a5f1c33392af2f9b"
PAPER2_SHA256 = "a8e73bb783471bed28dc062856c69101a26945ad516a8c9c06af755adcea5510"

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def load_source_namespace(archive_path):
    archive_bytes = Path(archive_path).read_bytes()
    archive_hash = sha256_bytes(archive_bytes)
    if archive_hash != ARCHIVE_SHA256:
        raise ValueError(f"Archive SHA-256 mismatch: {archive_hash}")
    with zipfile.ZipFile(archive_path) as zf:
        source = zf.read("paper2_compute.py")
    source_hash = sha256_bytes(source)
    if source_hash != PAPER2_SHA256:
        raise ValueError(f"paper2_compute.py SHA-256 mismatch: {source_hash}")
    tree = ast.parse(source.decode("utf-8"), filename="paper2_compute.py")
    wanted_assignments = {"PHI", "GRID_ANGLES", "E_NORMALS", "ZETA", "GAMMA_GENERIC"}
    wanted_functions = {"make_generic_gamma", "extract_conway_worms",
                        "analyze_worm_fibonacci", "verify_substitution_invariant"}
    body = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = {t.id for t in node.targets if isinstance(t, ast.Name)}
            if names & wanted_assignments:
                body.append(node)
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if node.name == "PenroseTiling" or node.name in wanted_functions:
                body.append(node)
    ns = {"np": np, "defaultdict": collections.defaultdict, "time": time}
    exec(compile(ast.Module(body=body, type_ignores=[]),
                 "paper2_compute.py:selected", "exec"), ns)
    run_pipeline = next(n for n in tree.body
                        if isinstance(n, ast.FunctionDef) and n.name == "run_full_pipeline")
    grid_sizes = None
    selected_large = None
    for node in ast.walk(run_pipeline):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "grid_sizes":
                    grid_sizes = ast.literal_eval(node.value)
                if isinstance(target, ast.Name) and target.id == "tiling_large":
                    if isinstance(node.value, ast.Subscript):
                        selected_large = ast.literal_eval(node.value.slice)
    return ns, archive_hash, source_hash, grid_sizes, selected_large

def original_worm_summary(tiling, ns):
    worms = ns["extract_conway_worms"](tiling)
    analysis = ns["analyze_worm_fibonacci"](worms)
    family_counts = [len(analysis["by_family"].get(f, [])) for f in range(5)]
    lengths = collections.Counter(w["n_tiles"] for w in worms)
    return {
        "n_worms": len(worms),
        "family_counts": family_counts,
        "length_histogram": {str(k): v for k, v in sorted(lengths.items())},
        "mean_L_over_S": float(analysis["mean_ratio"]),
        "source_fibonacci_matches": int(analysis["fibonacci_matches"]),
    }

def tile_edge_set(tile):
    v = tile["vertices"]
    return {tuple(sorted((v[i], v[(i + 1) % 4]))) for i in range(4)}

def physical_disk_worms(tiling, radius, ns):
    E_NORMALS = ns["E_NORMALS"]
    groups = {}
    tile_edges = [tile_edge_set(t) for t in tiling.tiles]
    omega = np.exp(2j * math.pi / 5)
    for family in range(5):
        direction = np.array([-E_NORMALS[family, 1], E_NORMALS[family, 0]])
        by_line = collections.defaultdict(list)
        for tile_index, tile in enumerate(tiling.tiles):
            j, k = tile["families"]
            n_j, n_k = tile["grid_indices"]
            if family == j:
                line = n_j
            elif family == k:
                line = n_k
            else:
                continue
            centroid = np.mean(tile["positions"], axis=0)
            if np.linalg.norm(centroid) > radius:
                continue
            coordinate = float(np.dot(centroid, direction))
            m_center = np.mean(np.asarray(tile["mi_vertices"], dtype=float), axis=0)
            z2_center = sum(m_center[q] * omega ** (2 * q) for q in range(5))
            by_line[line].append((coordinate, tile_index, tile["type"], z2_center))
        for line, items in by_line.items():
            if len(items) < 3:
                continue
            items.sort(key=lambda x: x[0])
            sequence = "".join("L" if x[2] == "thick" else "S" for x in items)
            bad_adjacencies = 0
            for left, right in zip(items, items[1:]):
                if len(tile_edges[left[1]] & tile_edges[right[1]]) != 1:
                    bad_adjacencies += 1
            groups[family, line] = {
                "items": items,
                "sequence": sequence,
                "n_tiles": len(sequence),
                "L_count": sequence.count("L"),
                "S_count": sequence.count("S"),
                "bad_adjacencies": bad_adjacencies,
            }
    return groups

def max_run(sequence, symbol):
    separator = "S" if symbol == "L" else "L"
    return max((len(part) for part in sequence.split(separator)), default=0)

def crop_summary(groups, phi):
    worms = list(groups.values())
    long = [w for w in worms if w["n_tiles"] >= 10]
    ratios = [w["L_count"] / max(w["S_count"], 1) for w in long]
    matches = [abs(r - phi) / phi < 0.15 for r in ratios]
    ss = sum(w["sequence"].count("SS") for w in long)
    adjacent_symbols = sum(max(0, len(w["sequence"]) - 1) for w in long)
    strict_word = [
        "SS" not in w["sequence"]
        and max_run(w["sequence"], "L") <= 3
        and max_run(w["sequence"], "S") <= 2
        for w in long
    ]
    target = 2 * math.pi * phi ** -2
    phase_errors = []
    for w in long:
        z2_values = [item[3] for item in w["items"] if abs(item[3]) > 1e-12]
        phases = np.unwrap(np.asarray([np.angle(z) for z in z2_values]))
        for increment in np.diff(phases):
            phase_errors.append((
                abs(np.angle(np.exp(1j * (increment - target)))),
                abs(np.angle(np.exp(1j * (increment + target)))),
            ))
    target_errors = np.asarray([e[0] for e in phase_errors])
    opposite_errors = np.asarray([e[1] for e in phase_errors])
    return {
        "n_worms": len(worms),
        "family_counts": [sum(1 for (f, _), _w in groups.items() if f == j) for j in range(5)],
        "length_min": min(w["n_tiles"] for w in worms),
        "length_max": max(w["n_tiles"] for w in worms),
        "long_worms_n_ge_10": len(long),
        "mean_L_over_S_long": float(np.mean(ratios)),
        "within_15_percent_of_phi": int(sum(matches)),
        "within_15_percent_fraction": float(np.mean(matches)),
        "consecutive_tile_pairs": int(sum(max(0, w["n_tiles"] - 1) for w in worms)),
        "bad_shared_edge_adjacencies": int(sum(w["bad_adjacencies"] for w in worms)),
        "SS_bigrams_long": int(ss),
        "symbol_adjacencies_long": int(adjacent_symbols),
        "SS_bigram_fraction_long": float(ss / adjacent_symbols),
        "max_thick_L_run_long": int(max(max_run(w["sequence"], "L") for w in long)),
        "max_thin_S_run_long": int(max(max_run(w["sequence"], "S") for w in long)),
        "strict_fibonacci_word_proxy_passes": int(sum(strict_word)),
        "internal_z2_phase_increments": int(len(phase_errors)),
        "internal_z2_phase_mean_abs_error_to_phi_minus2_deg": float(np.mean(target_errors) * 180 / math.pi),
        "internal_z2_phase_median_abs_error_to_phi_minus2_deg": float(np.median(target_errors) * 180 / math.pi),
        "internal_z2_phase_within_10deg_fraction": float(np.mean(target_errors < math.radians(10))),
        "internal_z2_phase_within_20deg_fraction": float(np.mean(target_errors < math.radians(20))),
        "internal_z2_phase_mean_abs_error_to_opposite_deg": float(np.mean(opposite_errors) * 180 / math.pi),
        "internal_z2_phase_within_10deg_opposite_fraction": float(np.mean(opposite_errors < math.radians(10))),
    }

def disk_tile_signatures(tiling, radius):
    return {
        (tile["families"], tile["grid_indices"])
        for tile in tiling.tiles
        if np.linalg.norm(np.mean(tile["positions"], axis=0)) <= radius
    }

def run(archive_path, radius=20.0, crop_grid=25, comparison_grid=21):
    ns, archive_hash, source_hash, grid_sizes, selected_large = load_source_namespace(archive_path)
    phi = float(ns["PHI"])
    original_at_pipeline = ns["PenroseTiling"](N_grid=selected_large, verbose=False)
    original15 = original_worm_summary(original_at_pipeline, ns)
    original_at_paper_claim = ns["PenroseTiling"](N_grid=25, verbose=False)
    original25 = original_worm_summary(original_at_paper_claim, ns)
    comparison = ns["PenroseTiling"](N_grid=comparison_grid, verbose=False)
    crop_tiling = ns["PenroseTiling"](N_grid=crop_grid, verbose=False)
    sig_a = disk_tile_signatures(comparison, radius)
    sig_b = disk_tile_signatures(crop_tiling, radius)
    if sig_a != sig_b:
        raise AssertionError("Physical disk tile crop changes with the comparison grid")
    groups = physical_disk_worms(crop_tiling, radius, ns)
    cropped = crop_summary(groups, phi)
    cropped.update({
        "radius": radius, "crop_grid": crop_grid,
        "comparison_grid": comparison_grid, "disk_tile_count": len(sig_b),
        "disk_tile_crop_stable": True,
    })
    substitution = ns["verify_substitution_invariant"]()
    eig = substitution["eigenvalues_M1"]
    rho = abs(float(eig[1]) / float(eig[0]))
    phase_link = {
        "M1": substitution["M1"],
        "M2_equals_M1_squared": bool(substitution["M2_equals_M1_sq"]),
        "M1_eigenvalues": [float(x) for x in eig],
        "stable_to_unstable_magnitude_ratio": rho,
        "golden_angle_fraction_phi_minus_2": phi ** -2,
        "ratio_equals_phi_minus_2": abs(rho - phi ** -2) < 1e-12,
        "interpretation": "Source matrix fixes the contraction magnitude; interpreting it as a turn fraction Δθ/(2π) is an additional observer phase-lift rule, not stated by the source script.",
    }
    return {
        "status": "PASS_SOURCE_REPLAY_AND_CROP_AUDIT",
        "archive_sha256": archive_hash,
        "paper2_compute_sha256": source_hash,
        "source_pipeline_grid_sizes": grid_sizes,
        "source_pipeline_tiling_large_grid": selected_large,
        "paper_text_claimed_worm_grid": 25,
        "original_extractor_at_pipeline_grid": original15,
        "original_extractor_at_paper_claim_grid": original25,
        "corrected_common_physical_disk_crop": cropped,
        "source_fibonacci_phase_link": phase_link,
        "scope": "The disk crop is a new explicit physical-interior convention. It reproduces a near-phi frequency ratio and connected tile chains, but does not establish exact Fibonacci substitution words or the 34:55 observer-to-worm map.",
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="Authenticated Archive(1).zip")
    parser.add_argument("--radius", type=float, default=20.0)
    parser.add_argument("--crop-grid", type=int, default=25)
    parser.add_argument("--comparison-grid", type=int, default=21)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.archive, args.radius, args.crop_grid, args.comparison_grid)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
