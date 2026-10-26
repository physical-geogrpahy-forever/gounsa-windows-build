#!/usr/bin/env python3
"""Summarize the actual source C run artifacts (22 baseline +16 controls).
Every number comes from native QA_JSON/QA_LAYER. Never report as Gounsa field estimate.
"""
from pathlib import Path
import json,csv,math,statistics
ROOT=Path(__file__).resolve().parent/"spatial_patch_experiments"
BASE=ROOT/"archive"/"base"
CONTROLS=ROOT/"archive"/"controls"
OUT=ROOT/"consolidated"
OUT.mkdir(parents=True,exist_ok=True)
records={}
paths=list(BASE.glob("**/qa_result.json"))+list(CONTROLS.glob("**/qa_result.json"))
for p in paths:
    v=json.loads(p.read_text())
    key=(v["scenario"],v["intensity_mm_h"],v["stemflow"],v.get("mechanism","all"))
    assert key not in records,("duplicated native output",key)
    assert v.get("qa_pass"),("native QA failure",key)
    assert v["water_relative_residual"]<.001 and v["original_soil_relative_residual"]<.01
    assert v["bed_geometry_relative_residual"]<.01
    records[key]=(v,p)
assert len(records)==38,("expected 38 native runs",len(records),list(records))
def get(s,r,sf="off",mechanism="all"):return records[s,r,sf,mechanism][0]
short=["grass_dense","oak_sparse","barrier_equal","island_equal"]
shorthand={"grass_dense":"밀생 억새 가상배치",
           "oak_sparse":"산발 참나무 가상배치",
           "barrier_equal":"40% 횡방향 연결",
           "island_equal":"40% 고립 패치"}
lines=[
"# 실제 2차원 SWEHR 원본 엔진의 공간배치 민감도",
"",
"**상태: 원본 C 방정식 + 명시적으로 새로 작성한 공간강우/침투/거칠기/박리 입력 결합. 고운사 현장 지형 또는 실측 식생 예측이 아님.**",
"",
"모든 실행은 13×25격자, dx=0.5m, 81.25m²이며 1시간 강우사상이다.",
"원본 SWEHR source commit = "+get("oak_sparse",30)["native_source_sha"]+".",
"",
"## 사상별 토사유출량 t/ha/event",
"| 입력 강우 (mm/h) | 밀생 억새 | 산발 참나무 | 40% 횡방향 연결 | 40% 고립 패치 |",
"|---:|---:|---:|---:|---:|"]
for rain in [10,20,30,40,50]:
    z=[get(s,rain)["sediment_export_t_ha"] for s in short]
    lines.append("| "+str(rain)+" | "+" | ".join(f"{x:.8g}" for x in z)+" |")
lines+=["","## 사상별 경계 유출수심 mm/event",
"| 강우 (mm/h) | 밀생 억새 | 산발 참나무 | 40% 횡방향 연결 | 40% 고립 패치 |",
"|---:|---:|---:|---:|---:|"]
for rain in [10,20,30,40,50]:
    z=[get(s,rain)["outflow_mm"] for s in short]
    lines.append("| "+str(rain)+" | "+" | ".join(f"{x:.6g}" for x in z)+" |")
lines+=["","## 동일 식생 면적의 공간배치 효과"]
for r in [20,30,40,50]:
    e1=get("barrier_equal",r)["sediment_export_t_ha"]
    e2=get("island_equal",r)["sediment_export_t_ha"]
    lines.append(f"- P={r}mm/h: 40% 고립형/횡방향 연결형 토사배출량 = {e2/e1:.4f}배; 모델 격자 식생 면적 양쪽 정확히 40%.")
lines+=["","## 30mm/h 과정별 분리 (모형과 가상 공간특성의 sensitivity, 종별 empirical coefficient 아님)",
"| 물리과정 변형 | 억새 유출 mm | 참나무 유출 mm | 억새 배출 t/ha | 참나무 배출 t/ha |",
"|---|---:|---:|---:|---:|"]
for mode in ["canopy_only","hydraulic_only","detachment_only","all"]:
    g=get("grass_dense",30,mechanism=mode);o=get("oak_sparse",30,mechanism=mode)
    lines.append(f"| {mode} | {g['outflow_mm']:.6g} | {o['outflow_mm']:.6g} | {g['sediment_export_t_ha']:.8g} | {o['sediment_export_t_ha']:.8g} |")
lines+=["","## 줄기 기부에 유하우의 총량보존적 공간 재배치 (수관 적하 KE는 미구현)",
"| P (mm/h) | 식생 | SF 이동수량 m³ | SF 없음 유출 mm | SF 있음 유출 mm | SF 없음 토사 t/ha | SF 있음 토사 t/ha |",
"|---:|---|---:|---:|---:|---:|---:|"]
for rain in [10,20,30,40,50]:
    for s in ["grass_dense","oak_sparse"]:
        a=get(s,rain);b=get(s,rain,"on")
        lines.append(f"| {rain} | {shorthand[s]} | {b['stemflow_relocated_m3']:.7g} | {a['outflow_mm']:.6g} | {b['outflow_mm']:.6g} | {a['sediment_export_t_ha']:.7g} | {b['sediment_export_t_ha']:.7g} |")
lines+=["","## 공간입력 측정단위와 결합의 경계",
"- 구조: 숲의 피복이 아닌, 2D cell polygon mask. 밀생 억새 94.77%, 산발 참나무 9.23%, 연결형/고립형 각 40%. 전부 **가상 배치**.",
"- 가상 지표 매개변수: 노출지 Ks=1e-6m/s, n=.08, rainsplash a=.25, ad=.25, cohesive entrainment J=30; 식생격자 Ks=4e-6m/s, n=.18, a=.07, ad=.10, J=90. **실측 수종별 값 아님**.",
"- 모든 격자의 사건 차단저류는 식생격자에서 최대 .8mm; stemflow spatial-on일 때 차단 후 수관격자 공급량의 P 총량 중 10%를 가까운 포기/그루터기 중앙격자로 재배분. 도달 수량+차단량=전체 강우량. 이는 과거 EUROSEM 형상 계수로 계산한 현장 SF 비율이 아님.",
"- 토사 박리항에서는 줄기를 따라 흐르는 SF를 빗방울 충격으로 취급하지 않으나, **수관적하우의 추가 낙하운동에너지는 아직 구현하지 않음**.",
"- 입력된 침투능과 유수박리 저항의 식생공간 차이는 모형 자체의 물리식을 바꾼 것이 아니라 제어조건이다. 같은 토양에서 실측으로 캘리브레이션하지 못하면 종별 정량 순위를 고정할 수 없음.",
"- 관측 bare flowlength를 모델-격자 경사방향 j열로 간략 계산하며, 이는 수치적으로 계산된 실제 흐름선/입경별 유사 연속성과 동일하지 않음.",
"- 모든 수치 사례는 원래 3×51 시험과 달리 새 13×25 2D 가상 경사표면을 생성한 후 사용함; 기존 original-published SWEHR 코드는 원래의 비지형물리학적인 외부 강제 물/유사경계를 비활성화하는 선행 QA 수정이 포함됨.",
"- SWEHR native 기계론적 2D finite-volume 물/유사수지는 모든 사례에서 통과했지만, 실제 고운사 DEM과 식생 공간분포, 뿌리량, 암편, 계절별 수관, 시작 토양수분, 낙엽층, 검증 관측유출량 및 TLS 사면변화 미입력.",
"",
"## 검증",
f"- 아카이브에서 읽은 38개 QA 기록 모두 QA_PASS. 최대 상대 물수지 오차 {max(x[0]['water_relative_residual'] for x in records.values()):.2e}.",
f"- 최대 원토양 박리-지표퇴적층-부유사-유출구 유사량 상대오차 {max(x[0]['original_soil_relative_residual'] for x in records.values()):.2e}.",
f"- 최대 지형-퇴적층 질량 상대오차 {max(x[0]['bed_geometry_relative_residual'] for x in records.values()):.2e}.",
"",
"원본 코드 GitHub Actions: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264048008",
"과정별 대조: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40264354578",
]
outrows=[]
for k,(v,p) in sorted(records.items(),key=lambda x:(x[0][1],x[0][0],x[0][2],x[0][3])):
    outrows.append({k:v.get(k) for k in ["scenario","mechanism","intensity_mm_h","stemflow","vegetation_fraction","bare_fraction","max_uninterrupted_bare_column_length_m","interception_volume_m3","stemflow_relocated_m3","effective_rain_volume_m3","rain_m3","outflow_mm","infil_m3","gross_detachment_t_ha","sediment_export_t_ha","original_soil_relative_residual","bed_geometry_relative_residual","water_relative_residual","qa_pass"]})
keys=sorted(set().union(*(x.keys() for x in outrows)))
with (OUT/"summary.csv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader();writer.writerows(outrows)
(OUT/"summary.md").write_text("\n".join(lines)+"\n")
(OUT/"full_qa.json").write_text(json.dumps([x[0] for x in records.values()],indent=2,ensure_ascii=False))
for scenario in ["grass_dense","oak_sparse","barrier_equal","island_equal"]:
    # Pull a 30mm OFF base map, csv stored in the same source run directory.
    q=get(scenario,30)
    p=records[(scenario,30,"off","all")][1].parent/"vegetation_map.csv"
    raw=list(csv.DictReader(p.open()))
    indices={(int(row["i"]),int(row["j"])):int(row["veg"]) for row in raw}
    pic="\n".join("".join("██" if indices[(i,j)] else "  " for i in range(13)) for j in reversed(range(25)))
    (OUT/(scenario+"_mask.txt")).write_text("██=vegetation, blank=bare soil, upstream/top at top; illustrative raster\n"+pic+"\n")
print("\n".join(lines),flush=True)
