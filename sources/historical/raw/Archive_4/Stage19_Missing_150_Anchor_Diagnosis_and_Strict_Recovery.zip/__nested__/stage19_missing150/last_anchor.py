import sys,json,time
sys.path.insert(0,'/mnt/data/stage19_target_first')
from stage19_full import setup_geometry
from diagnose_missing import screen
sp,_=setup_geometry('penrose',20,3.5)
for n in (12,16,24):
 t=time.time();x=screen(sp,[10550],tuple(range(2,26)),n,(1.5,));print('variants',n,'min_distance',x['min_distance'].tolist(),'size',x['size'].tolist(),'target',x['target'].tolist(),'time',round(time.time()-t,2),flush=True)
 if x['min_distance'][0]<=1.5:break
