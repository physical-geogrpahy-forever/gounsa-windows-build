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

## 2026-10-27 후속 메인 호출경로 및 건조격자 안정성 위험 검증
이번 세션에서 GitHub HEAD Fortran 전체 컴파일 경로 `Makefile`/ `Makefile.gfortran`(11 source .f90)와 `src/swefvm.f90` 85줄, `src/sediment.f90` 360줄, `src/swe.f90` 1,520줄, `src/module.f90`310줄, `src/initialization.f90`520줄을 직접 열어 코드 참조 확인했다. `src/auxsubs.f90`, `src/auxfuncs.f90`, `buildMeshData.f90`, `results_output.f90`, `restart_output.f90`, `readGMSHMesh.f90`, `readGambitMesh.f90`도 rain/LAI/canopy/splash/suspended 등의 키워드와 실행 변수 탐색. **해당 전체 메인 소스 경로에서 기상 강우와 수관저류/낙수 빗방울박리 루틴은 확인되지 않았다.**
- `src/swefvm.f90` L50–74 메인 `do while(t<=tstop)` 내부 `call swe`, 다음 `if(sedimentctl.eq.1.and.scalc.eq.1)call sediment`, `t=t+dt`와 `sedInterval` flag. 수문 강우차단과 유효강우를 계산하는 호출 없음. `src/initialization.f90` L47–90 input control contains `inletH/inletUB/inletVB/inletQ`, `outlet...`, sediment switch, mesh type, terrain, not rainfall/LAI file mappings.
- `src/sediment.f90::sediment()` L23–55 full call `calc_shear`, `calc_steepestSlope`, `calc_criticalShieldsNumber`, `calc_ShieldsNumber`, `calc_sedimentFlux`, `calc_divSedimentFlux`, `calc_faceElevChange`, `calc_nodeNewElevation`, `updateMeshData`. **No detachable rainfall-induced source and no advected size-class suspended concentration state; one representative diameter and bed-load motion**. `readSedimentProperties()` L75–89 input `diam,porosity,Shields thresholds,sedTransRate,GrassConst...` not canopy.
- `src/sediment.f90` L174–200 bedload vector MPM `qflat=8 sqrt(g*Rs*diam^3)*(Shields-Shields_cr)^(3/2)`, or Grass empirical `q_b=A(U,V)|V|^(m-1)`. L247–299 edge boundary vector flux integrates each face and Exner change `Δzb= -(sedInterval*dt)/(1-porosity) div(q_b)/faceArea`. This is genuinely X/Y transported bedload + changing terrain, **not Hairsine-Rose active subsoil/raindrop transport despite sediment in name**.
- **Numerical caveat needing independent runtime test**: `src/sediment.f90::calc_shear()` lines~102–116 loops every `nFaces` and calculates `.../Q1(i)**(4.0/3.0)` for both stress components **without a local wet/dry guard**. If `Q1(i)=0` at a truly dry element this expression can be indeterminate (0/0) or divide by zero. `swe()` may clamp depth elsewhere; **do not assert proven NaN failure** without native running. A separate gfortran/ifort build and dry/wet-bed sediment-on test would be necessary to make that claim.
- Native gfortran was locally installed in this investigator runtime but external GitHub codeload access via container refused DNS, so full release was **not downloaded or built**. GitHub source connector verifies code/file blob; compiler availability != compile success. Model remains NO-GO due missing essential canopy and rain splash, not due this unproven numerical hazard.
