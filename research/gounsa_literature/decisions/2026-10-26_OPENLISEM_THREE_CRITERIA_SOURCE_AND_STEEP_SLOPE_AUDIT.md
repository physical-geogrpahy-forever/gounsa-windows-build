# 2026-10-26 OpenLISEM 3조건 재평가: 원본 코드 + 실제 급경사지 2D 적용

## 판단 대상
요구 1: LAI 등 정량 식생 요소를 사용한 canopy storage, interception, direct throughfall, leaf drainage. Stemflow은 우선순위가 낮지만 존재 여부는 정직하게 표기.
요구 2: 직접 유출에 의한 토양박리와 유사수송.
요구 3: 산지/급경사지 적용 경험.

## 원본 소스 고정
`vjetten/openlisem` `main_C`, SHA `d894c72428947247ce49eb88353dadf49b3123e8`.
- `hydro/lisInterception.cpp::cell_Interception`: canopen=1-exp(-0.45 LAI), CS=Smax*(1-exp(-canopen RainCumInt/Smax)), LeafDrain=max(0,Rainc-ΔCS), RainNet=Cv*LeafDrain+(1-Cv)*Rainc. 저장량은 식생부분, RainNet은 셀 전체를 고려.
- `model/lisDataInit.cpp` 대략 499~523: Smax 유형별 초기화, Broadleaf 0.2856 LAI, Clumped Grass 0.59 LAI^0.88, 0.001 곱해서 mm→m. `smax.map` 사용자 지정 가능. LAI는 별도로 계속 필요.
- `erosion/lisErosionSplash.cpp::SplashDetachment`: direct rain and leaf drainage KE separated; KE_LD=max(15.3 sqrt(PlantHeight [m])-5.87,0); leafdrip fraction = (1-Lc)*Cv*LeafDrain; stone cover and optional grass strip shielding.
- `erosion/lisSWOF2DSediment.cpp`: `SWOFSediment`, `SedimentDetachmentSS`, 2D transport.
- `flow/lisOverlandflow.cpp` uses `fullSWOF2openMUSCL(...DEM)` in 2D mode.

## 중요한 소스 부정 결과
- `StemflowFraction`은 `include/model.h`에 선언됐지만 `model/lisDataInit.cpp`의 입력 읽기와 `ui_full/LisUIrunfile.cpp`의 매핑이 **주석처리**되어 있다. 원본이 개별 나무 SF를 직접 계산한다고 주장 금지.
- `PlantHeight`, LAI, Cover는 각각 별도 변수. 덮개 비율 하나로 식생을 환원해서 해석 금지.
- 2D flow에서 `DEM`을 사용한다고 해서 **침식량으로 DEM이 시간내 자동 갱신**된다고 주장 금지. 외부 사건간 DEM 갱신은 신규 coupling.
- 7.5.2 Windows 설치 파일은 2026-10-15 SourceForge에 게시, GitHub `main_C` SHA와 binary source-identical build proven 상태는 **아님**.
- 지금 환경은 Windows 실행파일을 실행한 게 아니며 원본 실행과 water/sediment closure도 **미검증**.

## 세 조건 판정
| 조건 | 자료 | 결론 |
|---|---|---|
| LAI canopy storage / throughfall / drip | source `lisInterception.cpp` + `lisErosionSplash.cpp` | 네이티브 원본 YES |
| runoff erosion 2D | source `lisSWOF2DSediment.cpp`, `lisOverlandflow.cpp` | 네이티브 원본 YES |
| mountain steep slope | Opedes et al. 2025 DOI 10.1002/esp.70074 | 실제 2D Dynamic Wave 적용 YES (erosion 검증은 NO) |

## 산지 선례 Opedes et al. (2025)
- Mount Elgon의 Ukha 유역 44.5km², 공간 12.5m, 계산 15초, 2D Dynamic Wave, 토양침식 시나리오.
- 설치도랑 조사 지점의 82%가 10–30°, 3%가 >=31°; 이것은 전체 유역 경사 분포가 아님.
- LAI, 식생 높이, litter, PER, COHr, stone fraction 각각 입력.
- 2022-04-28 5시간 18.6mm, 최고 25mm/h 강우로 관측 discharge NSE 0.72 KGE 0.61.
- 관측 유사자료는 확보하지 못했으므로 **침식 검증 미확인**.
- https://onlinelibrary.wiley.com/doi/full/10.1002/esp.70074

## 연구 결론
OpenLISEM은 세 필수 조건을 *기능 및 적용 선례 수준에서* 전부 뒷받침할 수 있는 강력한 유수침식 후보. 그러나 표면적 rock armoring 변화, 사건간 DEM 갱신, 개별 SF, LPJ-GUESS root biomass 변환, 그리고 현재 바이너리 실행의 유사수지는 고운사 독립 검증/새로운 연결이 필요.

## 최단 실행 경로
사용자가 이미 Windows 7.5.2 setup exe를 보유하고 있다는 선행 작업 맥락을 활용한다.
1. Windows에서 **설치형 원본 실행파일**로 공식 예제 데이터 먼저 구동. Linux Qt6/QWT 재빌드 우선 금지.
2. 원본 공식 예제로 rainfall, net rainfall, interception, 2D runoff, splash, flow detachment, deposition, sediment outlet mass closure를 순서대로 확인.
3. 10/20/30/40/50 mm/h 1시간 사상과 동일 토양/경계로 억새 및 맹아 식생 구조만 변환. 신호가 실제로 침식 출력까지 전파되는지 LAI/CH/Smax/stone/root/litter 단독 perturbation으로 확인.
4. 고운사 자료가 없을 땐 실제 생태관측 결과라고 주장하지 않고 가상 민감도 실험으로 명시.

## 관련 기록
- ../papers/2025_Opedes_OpenLISEM_MountElgon_Trenches.md
- ../models/OpenLISEM.md
- 2026-10-26_FULL_OPEN_SOURCE_NATIVE_2D_VEGETATION_EROSION_MODELS.md
