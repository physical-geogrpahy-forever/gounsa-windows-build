"""Native OpenLISEM 1ha, 5m-grid root cohesion sensitivity. No model code modifications."""
from pathlib import Path
import re,shutil
import numpy as np
import rasterio
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/"openlisem_reference_trial"
for d in ("maps","runs","rain","results","logs"):
    (ROOT/d).mkdir(parents=True,exist_ok=True)
conditions=[(4,0,1,10),(4,0,2,10),(8,0,2,10),(12,0,2,10),(4,8,2,10),(4,8,2,5),(4,8,2,20),(4,8,1,10),(4,8,2,1),(4,8,2,2),(12,0,2,1),(12,0,2,2)]
for species in ("Oak","Miscanthus"):
    for soil,root,eff,dt in conditions:
        label=f"{species}_S{soil}_R{root}_E{eff}_dt{dt}"
        source=SRC/"maps"/species
        dest=ROOT/"maps"/label
        assert source.exists(),source
        shutil.copytree(source,dest,dirs_exist_ok=True)
        for fn,value in (("coh.map",soil),("cohadd.map",root)):
            path=dest/fn
            with rasterio.open(path) as ds:
                profile=ds.profile.copy()
                profile["PCRASTER_VALUESCALE"]=ds.tags()["PCRASTER_VALUESCALE"]
                original=ds.read(1)
            for k in ("blockxsize","blockysize","tiled"):profile.pop(k,None)
            with rasterio.open(path,"w",**profile) as out:
                out.write(np.full_like(original,value),1)
            with rasterio.open(path) as ds:
                assert ds.tags()["PCRASTER_VALUESCALE"]=="VS_SCALAR"
        original=(SRC/"runs"/f"{species}_dt10_exponential_eff1.run").read_text(encoding="utf8")
        assert "Routing Kin Wave 2D=0" in original
        updates={
          "Map Directory":str(dest.resolve())+"\\",
          "Result Directory":str((ROOT/"results"/label).resolve())+"\\",
          "Rainfall Directory":str((ROOT/"rain").resolve())+"\\",
          "Timestep":str(dt),
          "Detachment efficiency":str(eff),
          "Rainfall file":f"P20_dt{dt}.txt",
          "Rainfall Bias Correction":str(3600/(3600+dt))
        }
        for key,value in updates.items():
            pattern=rf"(?m)^{re.escape(key)}=.*$"
            assert len(re.findall(pattern,original))==1,(label,key)
            original=re.sub(pattern,lambda m:key+"="+value,original)
        (ROOT/"runs"/f"{label}.run").write_text(original,encoding="utf8")
        (ROOT/"results"/label).mkdir(exist_ok=True)
for dt in (1,2,5,10,20):
    (ROOT/"rain"/f"P20_dt{dt}.txt").write_text(
        "# 20mm/h for one hour, then one hour no rain\n2\ntime\ngauge 1\n001:0000 20.0\n001:0060 0\n001:0120 0\n",encoding="ascii")
print("Native input variants:",len(list((ROOT/"runs").glob("*.run"))))
