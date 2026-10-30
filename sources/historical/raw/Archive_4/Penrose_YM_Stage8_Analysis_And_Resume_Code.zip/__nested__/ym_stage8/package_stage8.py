from pathlib import Path
import hashlib,json,zipfile,shutil
root=Path(__file__).resolve().parent
out=root.parent
exclude={'.partial.npz','SHA256_MANIFEST.json','__pycache__'}
files=sorted(p for p in root.rglob('*') if p.is_file()
        and '__pycache__' not in p.parts and not p.name.endswith('.partial.npz')
        and p.name!='SHA256_MANIFEST.json')
manifest={}
for p in files:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    manifest[str(p.relative_to(root))]={'sha256':h.hexdigest(),'bytes':p.stat().st_size}
(root/'SHA256_MANIFEST.json').write_text(json.dumps(manifest,indent=2))

for small,name in [(True,'Penrose_YM_Stage8_Analysis_And_Resume_Code.zip'),
                    (False,'Penrose_YM_Stage8_All_8_Checkpoints.zip')]:
    zpath=out/name
    with zipfile.ZipFile(zpath,'w',allowZip64=True) as z:
        for p in files+[root/'SHA256_MANIFEST.json']:
            if small and p.parent.name=='checkpoints' and p.suffix=='.npz':continue
            compression=zipfile.ZIP_STORED if p.suffix=='.npz' else zipfile.ZIP_DEFLATED
            z.write(p,arcname=str(Path('ym_stage8')/p.relative_to(root)),compress_type=compression)
    with zipfile.ZipFile(zpath) as z:
        bad=z.testzip()
        assert bad is None, bad
        raw=json.loads(z.read('ym_stage8/SHA256_MANIFEST.json'))
        for inner in z.namelist():
            if inner.endswith('SHA256_MANIFEST.json'):continue
            rr=inner.split('ym_stage8/',1)[1]
            assert hashlib.sha256(z.read(inner)).hexdigest()==raw[rr]['sha256'], rr
    print(name, zpath.stat().st_size, 'bytes; ZIP and file SHA256 verified',flush=True)
shutil.copy2(root/'STAGE_8_REPORT.md',out/'Penrose_YM_Stage8_Report.md')
print('report', (out/'Penrose_YM_Stage8_Report.md').stat().st_size)
