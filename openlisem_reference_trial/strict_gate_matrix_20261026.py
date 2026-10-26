"""Create matched unmodified-native OpenLISEM 7.5.2 2D numerical gates.
No erosion equation is simulated here. Only adds original .run configurations.
Invoked by generate.py AFTER baseline input/output directories and maps exist.
"""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
cases=("Oak","Miscanthus")
schemes={"default":1,"alt_native":3}
steps=(2,5,10,20)
runs=ROOT/"runs"
rain=ROOT/"rain"
results=ROOT/"results"
created=[]
def replace_key(txt,key,val):
    pat=r"(?m)^"+re.escape(key)+r"=.*$"
    txt,count=re.subn(pat,lambda m:key+"="+str(val),txt)
    if count !=1: raise RuntimeError((key,count))
    return txt

for vegetation in cases:
    source=runs/f"{vegetation}_dt10_exponential_eff1.run"
    txt0=source.read_text(encoding="utf-8")
    for scheme,settling_opt in schemes.items():
        for dt in steps:
            label=f"GATE_{vegetation}_{scheme}_dt{dt}"
            out=results/label
            out.mkdir(exist_ok=True)
            txt=txt0
            mods={
                "Timestep":dt,
                "Advanced Options":1,
                "Deposition continuous":1,
                "Deposition exponential":1,
                "Detachment efficiency":1,
                "Routing Kin Wave 2D":2,
                "Flow Boundary 2D":1,
                "Rainfall Bias Correction":3600/(3600+dt),
                "Map Directory":str((ROOT/"maps"/vegetation).resolve())+"\\",
                "Result Directory":str(out.resolve())+"\\",
                "Rainfall Directory":str(rain.resolve())+"\\",
                "Rainfall file":f"GATE_P20_dt{dt}.txt",
                "Settling Velocity":settling_opt,
            }
            for k,v in mods.items():txt=replace_key(txt,k,v)
            # Current native parser uses 'SettlingVelocity' without whitespace.
            # Explicit source-parser key alongside UI value avoids silent mismatches.
            txt += f"\nSettlingVelocity={settling_opt}\n"
            (runs/(label+".run")).write_text(txt,encoding="utf-8")
            created.append(label)
for dt in steps:
    (rain/f"GATE_P20_dt{dt}.txt").write_text(
        "# constant storm; total rainfall corrected by runfile bias\n"
        "2\ntime\ngauge 1\n001:0000 20.0\n001:0060 0\n001:0120 0\n",
        encoding="ascii")
print("STRICT_GATE_MATRIX",len(created),"cases",created)
