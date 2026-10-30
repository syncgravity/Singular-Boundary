import math,json
from pathlib import Path
p=Path(__file__).resolve().parent
q=14;k=125;a=175;nu=7;eps=.25;delta=.05
r={'lambda_min':1,'penrose_incidence_max':nu,'Q14':{'Q':q,'H_links':36,'K_links':k,'A_K_faces':a,'halo_links':133,'epsilon':eps,'eta_over_Q':8*eps*eps*a/q,'alpha':1,
    'joint_tail_constant_additive':8*eps*eps*a+k*(math.log(4097)+2*nu),'joint_tail_loglambda_coefficient':1.5*k,
    'defect_event_delta':delta,'defect_sH_lower':2-6*delta,'defect_gibbs_exp_rate':8*math.cos(4*delta)},
    'general_Penrose':{'per_Q_H_bound':4,'per_Q_K_bound':88,'per_Q_A_K_bound':616,'epsilon':eps,'eta_per_Q':8*eps*eps*616,
    'joint_tail_additive_per_Q':8*eps*eps*616+88*(math.log(4097)+2*nu),'joint_tail_loglambda_coefficient_per_Q':1.5*88},
    'warning':'The stated tails control either large frustration AND the near-pure-gauge exterior event, or a special 13-link center defect. They do not bound the unconditional entire s_H tail.'}
(p/'full_analytic_constants.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
