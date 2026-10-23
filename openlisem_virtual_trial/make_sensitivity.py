"""Diagnose timestep/algorithm sensitivity using ORIGINAL OpenLISEM executable and SAME maps.
Overrides run-file flags only; source code remains unchanged.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
RUNS=ROOT/"runs"
RESULTS=ROOT/"results"
variants={
 "Oak_dt2":("Oak_sprouts_sparse",20,{"Timestep":"2"}),
 "Oak_dt5":("Oak_sprouts_sparse",20,{"Timestep":"5"}),
 "Oak_dt20":("Oak_sprouts_sparse",20,{"Timestep":"20"}),
 "Oak_dt30":("Oak_sprouts_sparse",20,{"Timestep":"30"}),
 "Oak_HR":("Oak_sprouts_sparse",20,{"Flooding SS method":"2"}),
 "Oak_noncontinuous":("Oak_sprouts_sparse",20,{"Advanced Options":"1","Deposition continuous":"0"}),
 "Oak_exponential":("Oak_sprouts_sparse",20,{"Advanced Options":"1","Deposition continuous":"1","Deposition exponential":"1"}),
 "Oak_HR_exponential":("Oak_sprouts_sparse",20,{"Advanced Options":"1","Deposition continuous":"1","Deposition exponential":"1","Flooding SS method":"2"}),
 "Miscanthus_dt5":("Miscanthus_dense",20,{"Timestep":"5"}),
 "Miscanthus_dt20":("Miscanthus_dense",20,{"Timestep":"20"}),
 "Miscanthus_HR":("Miscanthus_dense",20,{"Flooding SS method":"2"}),
 "Miscanthus_noncontinuous":("Miscanthus_dense",20,{"Advanced Options":"1","Deposition continuous":"0"}),
}
for label,(case,rain,changes) in variants.items():
    p=RUNS/f"{case}_P{rain:02d}.run"
    s=p.read_text(encoding="utf8")
    for k,v in changes.items():
        patt=re.compile(rf"(?m)^{re.escape(k)}=.*$")
        assert len(patt.findall(s))==1,(p,k)
        s=patt.sub(f"{k}={v}",s)
    initial=(ROOT/"results"/f"{case}_P{rain:02d}").resolve()
    replacement=(RESULTS/label).resolve()
    RESULTS.joinpath(label).mkdir(exist_ok=True)
    assert str(initial).lower() in s.lower(),(p,initial)
    s=re.sub(re.escape(str(initial)),lambda m:str(replacement),s,flags=re.I)
    (RUNS/f"{label}.run").write_text(s,encoding="utf8")
print("Extra diagnostic variants:",len(variants))
