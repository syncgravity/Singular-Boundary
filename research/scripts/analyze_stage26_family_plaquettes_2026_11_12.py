#!/usr/bin/env python3
"""Reconstruct Stage26 M55 incidence, verify links->plaquettes, and form C5 family operator."""
import argparse, hashlib, io, json, math, tempfile, zipfile
from pathlib import Path
import numpy as np

def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def qmul_vec(a, b):
    a0 = a[:, 0]; av = a[:, 1:]
    b0 = b[:, 0]; bv = b[:, 1:]
    return np.column_stack((a0*b0 - np.sum(av*bv, axis=1),
                            a0[:, None]*bv + b0[:, None]*av + np.cross(av, bv)))

def qconj_vec(a):
    out = a.copy()
    out[:, 1:] *= -1
    return out

def run(stage26_zip, geometry_zip, phase_max=1000):
    stage26_hash = file_sha256(stage26_zip)
    geometry_hash = file_sha256(geometry_zip)
    if stage26_hash != "6cfa12935428533cfeaff40a467705d632b19ede07b7f30e0bb9fb7a0cc68657":
        raise ValueError(f"Stage26 archive hash mismatch: {stage26_hash}")
    if geometry_hash != "d7a3fa153e69dae0129a6f0771d8241b78a0145cbc4939ea16b0a02ea74e7d60":
        raise ValueError(f"M55 geometry archive hash mismatch: {geometry_hash}")

    with tempfile.TemporaryDirectory(prefix="stage26_family_") as td:
        td = Path(td)
        with zipfile.ZipFile(geometry_zip) as gz:
            source = gz.read("rebuild_stage26_geometry.py").decode("utf-8")
            incidence_bytes = gz.read("stage26_penrose_m55_reconstructed_incidence.npz")
        source = source.replace("/mnt/data/stage26_penrose_m55_reconstructed_incidence.npz",
                                str(td / "rebuilt.npz"))
        source = source.replace("/mnt/data/stage26_penrose_m55_geometry_summary.json",
                                str(td / "summary.json"))
        src_path = td / "rebuild.py"
        src_path.write_text(source, encoding="utf-8")
        ns = {"__file__": str(src_path)}
        exec(compile(source, str(src_path), "exec"), ns)

        faces = ns["faces"]
        fidx = np.asarray(ns["fidx"])
        fi = np.asarray(ns["fi"])
        sg = np.asarray(ns["sg"])
        F = len(faces); E = len(ns["edges"]); V = len(ns["nodes"]); nt = int(ns["nt"])
        with np.load(io.BytesIO(incidence_bytes), allow_pickle=False) as inc:
            assert np.array_equal(inc["spatial_face_idx"], fidx)
            assert np.array_equal(inc["fi"], fi)
            assert np.array_equal(inc["sg"], sg)
            assert np.array_equal(inc["spatial_edges"], ns["edges"])
        if ns["h"] != "f67fc4455b37bf18f16c0a5ae90c7c3c5ccd49ca8b739fa1f5e43562b4581c21":
            raise AssertionError("M55 graph hash differs from archived Stage7 graph")
        if ns["arrayhash"] != "fee7afad5b4b464537782b508402401502984947ac5caf5163a87dad8ae33e2e":
            raise AssertionError("M55 incidence array hash mismatch")

        with zipfile.ZipFile(stage26_zip) as sz:
            restart_name = next(n for n in sz.namelist() if n.endswith("/restart.npz"))
            restart_bytes = sz.read(restart_name)
        with np.load(io.BytesIO(restart_bytes), allow_pickle=False) as restart:
            links = restart["links"]
            stored = restart["plaquette_trace"]
            source_sha = str(restart["source_sha256"])
        if source_sha != "275243c7da74941db5bdd882dbb7f44ce02c915503033f040841b75f80409638":
            raise AssertionError(f"Stage26 restart source hash mismatch: {source_sha}")
        assert links.shape == (nt * (E + V), 4)
        assert stored.shape == (nt * (F + E),)
        assert fi.shape == (nt * (F + E), 4) and sg.shape == fi.shape

        # Exact full reconstruction of every stored normalized SU(2) plaquette trace.
        q = np.zeros((len(fi), 4), dtype=np.float64); q[:, 0] = 1.0
        for k in range(4):
            u = links[fi[:, k]].copy()
            neg = sg[:, k] < 0
            u[neg] = qconj_vec(u[neg])
            q = qmul_vec(q, u)
        predicted = q[:, 0]
        error = np.abs(predicted - stored)
        max_error = float(error.max())
        if max_error > 1e-12:
            raise AssertionError(f"plaquette trace reconstruction mismatch: {max_error}")

        face_family = np.asarray([[a, b] for (u, ua, uab, ub, a, b) in faces], dtype=np.int8)
        if np.any(face_family[:, 0] == face_family[:, 1]) or np.any(face_family < 0) or np.any(face_family > 4):
            raise AssertionError("invalid face family pair")
        face_type = np.asarray(["thick" if min((b-a) % 5, (a-b) % 5) == 1 else "thin"
                                for (u, ua, uab, ub, a, b) in faces])
        family_masks = np.stack([np.any(face_family == j, axis=1) for j in range(5)])
        # Source ordering is per timeslice: F spatial faces followed by E temporal faces.
        spatial_by_time = stored.reshape(nt, F + E)[:, :F]
        defect = 1.0 - spatial_by_time
        family_defects = np.stack([defect[:, mask].mean(axis=1) for mask in family_masks], axis=1)

        phi = (1 + math.sqrt(5)) / 2
        rho = phi ** -2
        omega = np.exp(2j * math.pi / 5)
        phase_indices = np.arange(phase_max + 1)
        theta = 2 * math.pi * rho * phase_indices
        weights = math.sqrt(2/5) * np.cos(4*math.pi*np.arange(5)[None, :]/5 - theta[:, None])
        observer = family_defects @ weights.T
        full = family_defects.mean(axis=1)
        anisotropy = family_defects @ (omega ** (2*np.arange(5)))
        harmonic_prediction = math.sqrt(2/5) * np.real(anisotropy[:, None] * np.exp(-1j*theta[None, :]))
        harmonic_error = float(np.max(np.abs(observer - harmonic_prediction)))
        if harmonic_error > 1e-11:
            raise AssertionError("family operator Fourier identity failed")

        amplitude = math.sqrt(2/5) * np.abs(anisotropy)
        return {
            "status": "PASS_STAGE26_FULL_PLAQUETTE_RECONSTRUCTION_AND_FAMILY_OPERATOR",
            "stage26_zip_sha256": stage26_hash,
            "geometry_reconstruction_zip_sha256": geometry_hash,
            "stage26_restart": restart_name,
            "restart_source_sha256": source_sha,
            "restart_sweeps": restart_sweeps,
            "graph_hash": ns["h"],
            "source_array_sha256": ns["arrayhash"],
            "geometry": {"vertices": V, "spatial_edges": E, "spatial_faces": F, "nt": nt,
                         "spacetime_links": int(len(links)), "spacetime_faces": int(len(fi))},
            "exact_incidence_validation": {
                "reconstructed_faces": int(len(fi)),
                "max_abs_normalized_trace_error": max_error,
                "count_error_over_1e_12": int(np.count_nonzero(error > 1e-12)),
                "link_face_index_shapes_match": True
            },
            "family_labels": {
                "definition": "Each spatial rhombus face carries the two basis-direction indices (a,b) from the M55 source generator.",
                "face_type_counts": {"thick": int(np.count_nonzero(face_type == "thick")),
                                     "thin": int(np.count_nonzero(face_type == "thin"))},
                "faces_per_family": [int(x) for x in family_masks.sum(axis=1)]
            },
            "single_restart_spatial_plaquette_diagnostic": {
                "timeslices": nt,
                "family_defect_mean_over_slices": [float(x) for x in family_defects.mean(axis=0)],
                "family_defect_std_over_slices": [float(x) for x in family_defects.std(axis=0)],
                "full_family_control_mean": float(full.mean()),
                "full_family_control_std": float(full.std()),
                "second_harmonic_amplitude_mean": float(amplitude.mean()),
                "second_harmonic_amplitude_std": float(amplitude.std()),
                "second_harmonic_amplitude_min": float(amplitude.min()),
                "second_harmonic_amplitude_max": float(amplitude.max()),
                "second_harmonic_phase_circular_mean_rad": float(np.angle(np.mean(np.exp(1j*np.angle(anisotropy))))),
                "second_harmonic_phase_circular_spread_rad": float(np.sqrt(-2*np.log(abs(np.mean(np.exp(1j*np.angle(anisotropy))))))),
                "relative_second_harmonic_amplitude_to_full_control": float(amplitude.mean()/full.mean()),
                "observer_phase_indices_tested": [0, phase_max],
                "O_n_global_min": float(observer.min()),
                "O_n_global_max": float(observer.max()),
                "O_n_first_13_slice_means": [float(observer[:, k].mean()) for k in range(min(13, phase_max+1))],
                "family_operator_harmonic_identity_max_error": harmonic_error,
                "family_defect_by_timeslice": [[float(x) for x in row] for row in family_defects],
                "observer_O_by_timeslice_first_13_phases": [
                    [float(x) for x in row] for row in observer[:, :min(13, phase_max+1)]
                ]
            },
            "scope": "One restart configuration and its 20 spatial slices; this is a family-labelled plaquette diagnostic, not an ensemble correlator, not a long-worm Wilson-loop measurement, and not a mass-gap estimate. The reconstructed graph hash matches the archived Stage7 graph hash; byte identity with the separate complete measurement catalogue remains unverified."
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage26_zip")
    parser.add_argument("geometry_zip")
    parser.add_argument("--phase-max", type=int, default=1000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.stage26_zip, args.geometry_zip, args.phase_max)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
