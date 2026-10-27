# HydroSed2D: 원본 Fortran 공개 코드 감사 (2026-10-27)

## 모델 식별 및 탐색 이유
Xiaofeng Liu, Penn State University, HydroSed2D v1.0. 홈페이지 https://water.engr.psu.edu/liu/hydrosed2d.html
공식 GPLv3 소스 https://github.com/psu-efd/HydroSed2D .
고운사 사용자의 5–10cm, LAI 기반 canopy hydrology, 2D 천수방정식, 강우 및 유수박리와 퇴적을 **동일 공개 원본**에서 구현하는지 검사.

## 실제 확인한 소스
- `src/swe.f90` Git blob `e2b4e3741f72514f33cd4e3dcfc5c4e478ccd96b`
- `src/sediment.f90` Git blob `7e6be5983c8f8eee32a5ba919a6347acf425d615`
- `src/module.f90` Git blob `45fc895e14b7f4b0e6711628018540c58762e2d1`
- `src/initialization.f90` Git blob `a32e07cebebbe3f7faef7e47b99fcf852be9c9c3`
- 예제 디렉터리 `cases/1DTranscriticalFlow`, `dambreak_over_hump`, `sediment_hump`, 기타.

## 확인된 실제 과정
- unstructured-mesh X/Y 2D SWE `swe.f90` ; 독립 `sediment.f90::sediment` 본문 L23–54는 `calc_shear → calc_steepestSlope → calc_criticalShieldsNumber → calc_ShieldsNumber → calc_sedimentFlux → calc_divSedimentFlux → calc_faceElevChange → calc_nodeNewElevation → updateMeshData` 순서.
- `calc_sedimentFlux` L174–200에서 `sedTransRate=1`이면 Meyer–Peter–Müller(MPM) bedload, `=2`이면 Grass 속도 기반 bedload 식. `faceBedLoadFlux(i,1:2)` x/y 벡터이고 Exner 지표고도 업데이트 있음.
- **강우-수관차단-강우타격박리 없음.** `swe.f90`, `sediment.f90`, `initialization.f90`, `module.f90`에서 rain, interception, canopy, LAI, throughfall, splash, infiltration에 해당하는 구현 또는 배포 예제 없음. 검색 결과 0은 전체 가능한 숨은 코드 부재의 절대증명이 아니라 **검사된 배포 원본의 과정 연결 부재**에 대한 코드감사 판정.

## 해상도와 물리적 부합성
공개 예제는 주로 수로/붕괴류/이동상 시험. 0.05–0.1m 산림사면 강우+수관차단 실증 미확인. solver가 유동 및 유사이송을 풀 수 있다는 사실만으로 빗방울 박리와 정량 식생저류가 있는 산림 강우 침식모델로 해석 금지.

## 새로운 coupling이 필요한 부분
외부 수관차단, 강우, 침투, rainfall splash를 신규 구현해야 하므로 사용자 조건의 원본 단일모델에 부적합.

## 최종 판정
**탈락**. 유사 플럭스의 전방위 2D bedload 및 Exner 실제 코드만 통과. 강우 유수침식의 중요한 강우박리 및 canopy가 없음. 컴파일 및 네이티브 실행까지 한 것은 아님.

## 원본 링크
https://github.com/psu-efd/HydroSed2D/blob/master/src/sediment.f90
https://github.com/psu-efd/HydroSed2D/blob/master/src/swe.f90
