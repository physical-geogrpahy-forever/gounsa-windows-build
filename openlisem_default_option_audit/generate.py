"""Controlled OpenLISEM 7.5.2 audit on identical synthetic inputs.
This is NOT an upstream official dataset. Does not implement a custom physical model.
Only varies source-code routing modes, D50, and timestep in native executable.
"""
import csv, re, shutil, sys
from pathlib import Path
import numpy as np
import rasterio

ROOT=Path(__file__).resolve().parent
REF=ROOT.parent/'openlisem_reference_trial'
ROOT.mkdir(parents=True,exist_ok=True)
for name in ('maps','runs','results','rain','logs'):
    (ROOT/name).mkdir(exist_ok=True)

def replace1(text, key, val):
    pattern=rf"(?m)^{re.escape(key)}=.*$"
    text,count=re.subn(pattern,lambda m:key+"="+str(val),text)
    if count!=1: raise ValueError((key,count))
    return text

def generate():
    for grain in (99,100):
        directory=ROOT/'maps'/f'd50_{grain}'
        shutil.copytree(REF/'maps'/'Oak',directory,dirs_exist_ok=True)
        p=directory/'d50.map'
        with rasterio.open(p) as ds:
            a=ds.read(1)
            profile=ds.profile.copy()
            profile['driver']='PCRaster'
            profile['PCRASTER_VALUESCALE']=ds.tags()['PCRASTER_VALUESCALE']
        with rasterio.open(p,'w',**profile) as ds:
            ds.write(np.full_like(a,grain),1)
        with rasterio.open(p) as ds:
            assert np.allclose(ds.read(1),grain)
    base=(REF/'runs'/'Oak_dt10_exponential_eff1.run').read_text(encoding='utf8')
    assert 'Routing Kin Wave 2D=0' in base
    rows=[]
    for grain in (99,100):
        for mode in ('factory','advanced','altSV'):
            for dt in (2,10):
                tag=f'g{grain}_{mode}_dt{dt}'
                dest=ROOT/'results'/tag
                dest.mkdir(exist_ok=True)
                s=base
                mods={
                    'Timestep':dt,
                    'Deposition continuous':int(mode!='factory'),
                    'Deposition exponential':int(mode!='factory'),
                    'Settling Velocity':3 if mode=='altSV' else 1,
                    'Detachment efficiency':1,
                    'Map Directory':str((ROOT/'maps'/f'd50_{grain}').resolve())+'\\',
                    'Result Directory':str(dest.resolve())+'\\',
                    'Rainfall Directory':str((ROOT/'rain').resolve())+'\\',
                    'Rainfall file':f'rain_dt{dt}.txt',
                    'Rainfall Bias Correction':3600/(3600+dt),
                }
                for k,v in mods.items(): s=replace1(s,k,v)
                if mode=='altSV':
                    # The v7.5.2 backend mistakenly expects this unspaced variant.
                    s+='\nSettlingVelocity=3\n'
                (ROOT/'runs'/(tag+'.run')).write_text(s,encoding='utf8')
                rows.append((tag,grain,mode,dt))
    for dt in (2,10):
        (ROOT/'rain'/f'rain_dt{dt}.txt').write_text(
            '# Constant 20 mm/h for 60 minutes\n2\ntime\ngauge 1\n001:0000 20.0\n001:0060 0\n001:0120 0\n',
            encoding='ascii')
    with (ROOT/'design.csv').open('w',newline='',encoding='utf8') as file:
        w=csv.writer(file);w.writerow(('run','grain_um','options','dt_seconds'));w.writerows(rows)
    print('AUDIT_GENERATED',len(rows),'full native OpenLISEM runs')

def summarize():
    rows=[]
    for r in csv.DictReader((ROOT/'design.csv').open(encoding='utf8')):
        p=ROOT/'results'/r['run']/'totals.csv'
        status=dict(r,totals_found=p.exists())
        if p.exists():
            vals={}
            for line in p.read_text(encoding='utf-8-sig',errors='replace').splitlines():
                rr=next(csv.reader([line]))
                if len(rr)<2:continue
                try: vals[rr[0].strip()]=float(rr[1].strip())
                except ValueError: pass
            for metric,key in (
                ('rain_mm','Total Precipitation (mm):'),
                ('runoff_mm','Total outflow (overland+channel) (mm):'),
                ('export_kg_ha','Average soil loss (kg/ha):'),
                ('detachment_t','Flow detachment (land) (ton):'),
                ('deposition_t','Deposition (land) (ton):'),
                ('sediment_t','Total soil loss (ton):'),
            ):status[metric]=vals.get(key,'')
        rows.append(status)
        print('AUDIT_RESULT',','.join(f'{k}={v}' for k,v in status.items()))
    keys=('run','grain_um','options','dt_seconds','totals_found','rain_mm','runoff_mm','export_kg_ha','detachment_t','deposition_t','sediment_t')
    with (ROOT/'audit_table.csv').open('w',newline='',encoding='utf8') as file:
        w=csv.DictWriter(file,keys);w.writeheader();w.writerows(rows)

if __name__=='__main__':
    {'generate':generate,'summarize':summarize}[sys.argv[1]]()
