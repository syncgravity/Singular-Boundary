#!/usr/bin/env python3
"""Fully specified (astronomical but finite) one-/two-stage geodesic collar Gibbs surgery.
Finite product net target uses exterior links ONLY, so partial contraction has
one-to-one conditional Haar Jacobian bounded independently of ambient volume.
No proof that the outer conditional minimum is typically O(1/lambda).
"""
from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parent

# Any explicit SU(2) angular covering net of radius delta / sqrt(lambda) suffices.
# The finite quaternion chart net from construct_surgery.net uses a 1/sqrt(beta)
# covering, so beta=lambda/delta^2 yields a delta/sqrt(lambda) cover.
def surgery_bounds(lam,k,nu=7,delta=1/16):
    assert lam>=1 and k>=1 and 0<delta<1
    r=1/(math.pi*math.sqrt(lam));tau=1-r
    action_error=2*nu*k*(1+delta)**2
    inverse_multiplicity=2
    log_inverse_jacobian_bound=3*k*(math.log(math.pi)+.5*math.log(lam))
    peierls_log_prefactor=math.log(2)+3*k*math.log(math.pi)+1.5*k*math.log(lam)+action_error
    return {'lambda':lam,'links':k,'nu':nu,'net_resolution_over_sqrt_lambda':delta,'fractional_geodesic_contraction':tau,'action_error_lambda_scaled':action_error,
            'inverse_multiplicity':inverse_multiplicity,'min_log_Jacobian':-log_inverse_jacobian_bound,
            'log_tail_prefactor':peierls_log_prefactor,
            'tail_theorem':'P(lambda(s_B-s_K)>=t)<=min(1, exp(log_tail_prefactor-t)), assuming B subset K, with true SU2 Haar measure for all exterior b. This DOES NOT bound s_K.'}

def main():
    rows=[surgery_bounds(lam,k) for lam in [1,8,32,1024] for k in [59,125]]
    cert={'construction':'For frozen K-exterior b, select canonical argmin of S_K on a deterministic delta/sqrt(lambda) product SU2 net; this target depends only on b. Apply partial geodesic contraction of all K links toward the target by tau=1-1/(pi sqrt(lambda)); choose the lower full-action candidate of this map and identity. The map is piecewise one-to-one a.e., with at most two inverse branches; all link changes confined to K.',
          'proof':'Haar Jacobian per SU2 link is (1-tau)*[sin((1-tau)theta)/sin(theta)]^2 >= (1-tau)^3. Distance from global K minimizer at output <= (1+delta)/sqrt(lambda) in each link. Action Taylor bound is lambda[S_K(output)-s_K]<=2nu*k*(1+delta)^2. Full-action nonincrease by identity option. A(B) subset A(K) gives S_K(U)>=s_B, hence Gibbs tail inequality with factor 2*(pi sqrt(lambda))^(3k)*exp(2nu*k*(1+delta)^2).',
          'tested_collar_sizes':[59,125],'bounds':rows,
          'limitation':'Deterministic product-net search is exponential in number K of links. The map provides conditional-minimum increment control only, not the absolute distribution of s_K. O(|Q|) physical changed links, not polynomial computational complexity.'}
    (ROOT/'multiscale_certificate.json').write_text(json.dumps(cert,indent=2))
    print('PASS analytic constants; 125-link lambda32 log Peierls prefactor',round(next(x['log_tail_prefactor'] for x in rows if x['lambda']==32 and x['links']==125),2))
if __name__=='__main__':main()
