# 2026-10-27 고운사 5–10cm 모델선정 정책 정정: 선행연구가 적용한 모델 우선

## 기존 결정과 충돌하는 부분의 정정
사용자는 **다른 연구자가 실제로 5~10cm에서 사용한 수관차단+강우침식 단일모델**을 원한다. 2026-10-27에 SHETRAN 4.7.2를 20×20m 테스트베드에 5cm까지 별도 확장하자는 [이전 계획](2026-10-27_SUB10CM_SHETRAN_CONCRETE_GO_NOGO_EXECUTION_DECISION.md)은 사용자 우선순위인 **published precedent 우선**과 충돌하므로 **추진계획을 철회하고 보류**한다. 4m 원본 35개 가상사면 계산이 이미 완료되었다는 사실과 별개이다.

## 실제로 사용된 5~10cm 모델 확인
1. **Maggioli et al. (2022)**, https://doi.org/10.3389/fevo.2022.765148 : spatial distributed LISEM 0.05m grid, 1s output/routing, 375m² 실험사면에 다수 강우사상, vegetation cover → LAI → canopy storage. **kinematic wave routing**, freely spreading genuine 2D SWE 미입증. 해당 정확 소스 버전 및 재현 입력자료 미확보. OpenLISEM 7.5.2 GitHub Actions QA 불합격을 부정할 수 없다.
2. **Cuomo (2018)**, https://doi.org/10.19199/2018.3.0557-1405.31 : LISEM 0.1m grid, bare vs vegetated 35% test slope, LAI=6 (model input), Green-Ampt, rainfall/runoff erosion. 원본 exact binary/code 미식별, 자유로운 2D SWE 입증 아님.
3. **Epple et al.(2025)**, https://doi.org/10.1002/esp.70127 : **신형 Bastian van den Bout LISEM 계열**, 0.01m grid/DoD/PTV erosion, vegetation canopy ON 시나리오 미확인, exact version 및 공개 2022 git branch 일치 불명.
4. **Nord & Esteves (2005) PSEM_2D**, https://doi.org/10.1029/2004WR003690 : true 0.05m 2D SWE erosion/sedimentation, 저자가 직접 interception/vegetation effects를 제외했다고 기술, 공개 전체 source 미확보.

## 실제 시도 가능한 방법과 한계
- **가장 직접적인 published 5~10cm vegetation canopy+erosion 계보는 LISEM**이지만, **OpenLISEM Classic 7.5.2의 실제 native 12개 2D sediment 시간간격 비수렴 + finite soil stock 위반은 확인된 NO-GO**: [검증 보고](2026-10-26_OPENLISEM_752_NATIVE_2D_STABILITY_FAILED.md). 절대 재채택 불가.
- Maggioli 2022 및 Cuomo 2018 **실제로 사용된 classic LISEM 정확 버전/모델 설정/입력자료/원본(실행빌드)을 먼저 동정**, 동일 모델의 공개 가용성과 기존 코드 QA 결함 유무를 확인한다. 버전 미확인인 경우 재현 완료/선정 주장 금지. 이 단계에서 수관저류계산이 실제 5~10cm인 것은 입증돼도 **2D free-flow 조건은 여전히 불충족**.
- **사용자가 요구한 자유 X/Y 2D 유동, LAI canopy, rainfall + overland detachment, deposition, ≤10cm published run, matching complete publicly available source 전부 동시 만족**하는 검증된 원본은 이번까지 발견되지 않았다. LISEM 논문으로 부정확하게 all-PASS 승인할 수 없다.
- 만약 자유 2D가 절대 요건이라면 Maggioli 운동파 버전으로 대체하는 것은 **요구사항 위반**. 따라서 이를 완성된 추천으로 제시할 수 없으며 원래 실행판+2D SWE+수관을 동시 사용한 실제 published 사례를 확보할 때까지 **주모델 선정은 보류**.
- 사용자 우선순위가 "선행연구로 실증된 5cm에서 LAI+침식"을 더 높게 두고, kinematic wave를 허용한다면 published LISEM 설정 재현이 합리적인 대안이나 본인 승인 없이 2D 요건을 변경하지 않는다.

## 새 작업 규율
(a) 이미 제외한 TREX/SHETRAN/SMODERP2D/GSSHA/기타를 신규후보로 반복하지 않는다.
(b) 5~10cm 실행선례 없는 모델에 cm-level 임의 확대를 최선책으로 내세우지 않는다.
(c) 논문 모델 소개와 실제 동일 원본 실행판 일치 및 timestep sediment convergence를 구분한다.
(d) "모델 탐색"이 "모델 임의 개발"로 바뀌는 일을 차단한다.

## 남은 지점
Maggioli 2022/ Cuomo 2018 exact LISEM versions and source/input provenance, dynamic SWE vegetation storm at 5cm different published example, prior OpenLISEM native numerical stability conflicts resolved independently. 해결 전까지 물리적으로 완성된 재현가능 단일모델은 없음.
