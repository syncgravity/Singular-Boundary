import math,json
from pathlib import Path
p=Path(__file__).resolve().parent
r=json.load(open(p/'exact_rational_no_go.json'))
b=json.load(open(p/'bianchi_certificate.json'))
f=json.load(open(p/'flat_adjoint_rank_certificate.json'))
n=json.load(open(p/'nonlinear_no_go_probe.json'))
assert b['pointwise_nonabelian_Wilson_energy_coefficient']==44 and b['Q_count']==14 and b['maximum_noncommuting_factor_count']==17
assert all(x['rank_H_35_pivots']==105 and x['rank_joint_59_pivots']==177 for x in f['data'])
assert all(x['selected_adaptive_tau']==0 and x['original_H_conditional_min']>0 for x in n['results'])
assert r['rigorous_lower_bound_float']>0
s={'model':'Penrose rhombus spatial disk x 3-periodic Euclidean time; Q14 fixed interior','rigorous_no_go':'59-pivot-only globally action-decreasing surgery cannot uniformly dominate positive original s_H; exact rational exterior perturbation witness link 438',
   'rational_positive_witness_lower_coefficient':r['rigorous_lower_bound_float'],
   'local_relative_real_normal_mode_rank':177-105,'24_SU2_components':24,
   'compact_SU2_sequential_mgf':'for each finite Lambda and theta in [0,1): limsup_lambda E exp(theta lambda s_H) <= (1-theta)^-36',
   'compact_SU2_sequential_tail':'limsup_lambda P(lambda s_H>=t) <= min(1,2^36 exp(-t/2))',
   'fixed_volume_nonasymptotic_tail':'for each Lambda there exists lambda0(Lambda) such that for lambda>=lambda0(Lambda): P(lambda s_H>=t)<=min(1,2^37 exp(-t/2))',
   'sequential_local_mean':'limsup_lambda lambda E s_H <=36 and limsup_lambda lambda E S_A <=88.5',
   'Bianchi_curvature_coefficient':44,'inserted_face_count':14,
   'sequential_compact_Haar_insertion_ratio_lower':45**(-21),
   'sequential_compact_Haar_free_energy_upper':21*math.log(45),
   'UNPROVED':'uniform volume-independent lambda threshold; joint finite-lambda absolute concentration; arbitrary-support nonlinear R3; continuum mass gap'}
(p/'theorem_certificate.json').write_text(json.dumps(s,indent=2));print(json.dumps(s,indent=2))
