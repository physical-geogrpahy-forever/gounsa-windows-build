# 2026-10-27 Work의 OpenLISEM 수정보고와 독립된 새로운 문헌 4편 확인

## 조사 범위
사용자는 Classic OpenLISEM 7.5.2 원본 수정/수치 재검증을 Work에 맡겼다. 본 세션은 **그 코드의 수정이나 실행을 수행하지 않고**, 이미 검토/기각 모델 계보를 제외한 별도의 논문과 소스 공개를 검증. 시작 전 `SYSTEM.md`, `MASTER.md`, `INDEX.md` 읽고 2026 Long & He/Gash/SWE 선례가 **이미 등록된 것**을 확인하여 새 성과로 재포장하지 않았다.

## 신규 논문과 판정

| 새 연구 | 실제 공간/방법 | 수관 저류/낙수 | runoff/rill/interrill/deposition 2D | 원본 코드 | 고운사 |
|---|---|---|---|---|---|
| [Abrantes et al. 2021](../papers/2021_Abrantes_Simoes_2D_TwoDirectional_Slope_Erosion.md), DOI 10.2478/johh-2021-0003 | 2×2m x1%/y10% 토양 flume 강우모사; 논문 초록이 genuine unsteady 2D flow/2D sediment eq. 명시 | LAI / canopy 구현 미확인 | rill + interrill + deposition 발표 및 유출/유사 관측 비교 | 공개 리포지터리/동일 실행판 미발견 | 주모델 NO-GO, 다방향 물리 2D 비교근거 |
| [Li & Tian 2025](../papers/2025_Li_Tian_Microphysical_Canopy_Interception_Python.md), DOI 10.1029/2024WR038296 | 다층 canopy microphysical droplet collision model; 20/80mm/h 실험 | LAI, leaf projection, FVC, beta,p; 시간별 multilayer store, 직접통과 | 없음 | **YES 소스/데이터 Zenodo v2 10.5281/zenodo.15045577 Python basic/simplified 파일 목록 확인**, 파일 내용 직접 실행 미실시 | 수관 물리 비교 선례, 단일 erosion engine 아님 |
| [Senn et al. 2025](../papers/2025_Senn_Schaefer_Hosseini_Seitz_VSF_ULS_Energy.md), DOI 10.1002/esp.70150 | UAV lidar 약800–1200point/m², 0.5m xy /0.25m vertical voxel VSF, splash cups 현장 검증 | **수관 아래 rainfall impact kinetic energy** 증감 예측, 저류 물수지 아님 | 없음 | independent executable/source 미발견 | 드론수관→빗방울 KE hotspot 관측 보조근거 |
| [Katayama et al. 2023](../papers/2023_Katayama_Nanko_Jeong_Canopy_Drip_Kinetic_Hotspots.md), DOI 10.5194/esurf-11-1275-2023 | 일본 일본너도밤나무 야외 splash cup, 한 집중 가지 낙수점 | throughfall/canopy drip flux+TKE 집중 관측 | 없음, 현장 실측 논문 | 데이터 supplementary 공개, numerical engine 아님 | 임의 cover factor 아닌 국지 drip hotspot 물리 근거 |

## 각 논문의 가장 중요한 실제 결과 및 방법
1. Abrantes 2021: 2.00 × 2.00m flume, x방향 경사1%, y방향10%, 현장 runoff와 sediment time series 비교. 낮은 x방향 flux를 모델이 과소추정하지만 y와 방향 합계에서 좋은 재현. 실측 자유XY 2D 출력과 연구용 경사 대조의 이점, **산지 canopy 모델과 구분**. 원논문 PDF 직접 호스팅은 content-type octet-stream으로 web.open 차단; 첫 장/공식 초록 확인까지만 확인한 세부근거에 한정.
2. Li & Tian 2025: Eq5–7 `I1=gamma I0`, `dw_i/dt=I_i beta p max(0,1-w_i/Y_i)`, `I_(i+1)=I_i-dw_i/dt`; 강우강도 20/80mm/h의 basic vs simplified 정확도 비교; basic 80mm/h R² .972, RMSE .046 / simplified R² .943 RMSE .066. 수관 구조 LAI*G/gamma와 beta/p를 명시적으로 구분. 공개 Python 기본형과 단순형 코드 각 5–6kB **공식 Zenodo 파일 목록 확인**, 실제 실행 PASS 아님. 기존 OpenLISEM 수정 포크에 본 식을 새로 넣는 것은 새로운 coupling.
3. Senn 2025: forest canopy vertical gap fraction from high density ULS, VSF predict throughfall KE relative to open rainfall. 0.5m horizontal 0.25m vertical으로 lidar geometry voxelize. field measured relation significant but predicted KE systematic underestimate. **식생이 rainfall kinetic energy 증폭할 수 있어 canopy ON이 splash detachment를 꼭 감소시키는 것은 아님.** 5cm exact simulation 아님.
4. Katayama 2023: 한 집중 나무가지 drip location의 TKE general undercanopy의 15.2배, freefall의 49.7배; throughfall 양 general 11.4배/freefall 8.1배. unit TKE hotspot 39.2±23.7 vs general22.0±12.7 vs freefall4.5±3.5 J m^-2 mm^-1. **1개 woody hotspot 파일럿**, 이를 전체 참나무수관/고운사 조건 정량 계수로 전용 금지. 원자료 논문 supplement 공개.

## 기존 연구와 겹치는 것
- [Long & He 2009/2010 2D SWE + modified Gash interception + Green-Ampt + erosion/rill paper model](2026-10-27_2100_NEW_LONG_HE_2009_2010_2D_GASH_EROSION_SOURCE_VERDICT.md)은 다른 세션에서 이미 등록된 것으로 확인했으므로 본 조사 신규에 넣지 않는다. 비공개 executable/unknown mesh이므로 주모델 선정을 뒤집지 않는다.
- Classic openLISEM 7.5.2, new LISEM 0.2.3/0.2.5, SWEHR CSDMS 1.0, SHETRAN cm extrapolation, Wflow D8 sediment, FeST routing, Iber+ source 등 기존 GO/NO-GO 전부 유지.

## 결론 및 결정
**논문 네 편은 고운사의 2D 물리구조 또는 수관 충돌/강우충격 원리 이해에 각각 실질적으로 도움**. 특히 Li 2025는 **실제로 Python 원본 코드가 공식적으로 공개된** 새로운 canopy-only source example. 그러나 5–10cm + genuine 2D water&sediment + canopy-on + direct/drop splash + local deposition + same publicly executable **single published model all-PASS = 여전히 없음**.

다음 모델 탐색은 반드시 article method+mesh+published original code+canopy mass + sediment mass/time stability을 한 구현체에서 확인해야 하며, 이미 탈락한 기존 공개 엔진을 새 후보로 다시 거론하지 않는다. 본 세션은 **OpenLISEM 수정 작업/실험 수행 X**.

## 외부 링크
- https://doi.org/10.2478/johh-2021-0003
- https://doi.org/10.1029/2024WR038296 ; https://zenodo.org/records/15045577
- https://doi.org/10.1002/esp.70150 ; https://publikationen.bibliothek.kit.edu/1000184451
- https://doi.org/10.5194/esurf-11-1275-2023
