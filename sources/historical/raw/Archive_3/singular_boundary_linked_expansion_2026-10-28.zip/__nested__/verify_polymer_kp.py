#!/usr/bin/env python3
"""Exact rational verification of bounded-degree KP inequality.
No Gibbs or Monte Carlo sampling. Primary KP theorem is external.
"""
from fractions import Fraction as F
import json
out=[]
for degree in (4,6,9,17):
    critical=F(1,degree*degree+degree+1)  # x=e^(1+theta) u
    assert degree*degree*critical<1
    lhs=F(degree+1)*critical/(1-degree*degree*critical)
    assert lhs==1
    half=critical/2
    assert F(degree+1)*half/(1-degree*degree*half)<1
    out.append({'dependency_degree':degree,
        'critical_x_exp_1_plus_theta_times_activity':str(critical),
        'exact_KP_lhs_at_critical':str(lhs)})
assert out[0]['critical_x_exp_1_plus_theta_times_activity']=='1/21'
assert out[2]['critical_x_exp_1_plus_theta_times_activity']=='1/91'
print(json.dumps({'KP_application_algebra':out,'external_KP_theorem_reproved':False,'simulations':False},indent=2))
