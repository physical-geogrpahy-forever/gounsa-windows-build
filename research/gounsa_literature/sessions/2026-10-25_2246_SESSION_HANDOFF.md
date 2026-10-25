# 2026-10-25 고운사 생태수문-유출-침식 문헌조사 인계

## 사용자 요구와 이번 작업의 핵심
수관차단, 직접 수관통과우, 수관적하우, 수간유하우의 식생 수문 분배가 침투, 국지 runoff, 2D 유수침식으로 이어지는 published process-based 연구를 탐색한다. 소프트웨어 빌드 및 임의 유량 실험은 요구한 작업이 아니므로 우선하지 않는다.

## 실제 추가한 논문별 파일
- papers/2007_Xiao_HydrologicProcessesResidentialScale.md
- papers/2008_Apip_DistributedSedimentRunoffLumping.md
- papers/2009_Charlier_BananaStemflowRunoff.md
- papers/2009_Liang_StemflowThreeDimensionalSoilWater.md
- papers/2026_Beven_VanStan_StemflowPreferentialFlowReview.md
- papers/2026_DiPrima_TreesControlHillslopeSubsurfaceFlow.md
- papers/2026_Chen_MaizeInRowInterRowErosion.md
- papers/2026_Li_Tian_UndercanopyKineticEnergy.md

## 핵심 비교
- EUROSEM: 원본식에 SF(초본), DT, LD, NR=DT+LD+SF, Smith-Parlange infiltration, interrill/rill와 DET=k KE exp(-bh). genuine 2D 미충족, 국지 SF 합산 손실.
- Charlier 2009: 2분할 부지 모형에서 국지 SF→runoff 연결/18 사상 검증. Sediment 없음.
- Xiao 2007: canopy storage/배수→Green-Ampt→runoff 본문 식 (4),(7),(8) 확인. erosion 없음.
- Apip 2008: SF+DT+LD→net rainfall→CDRMV3 수문과 DR/DF 유사수송. 250m 셀과 1D flow, 국지화 없음.
- HETEROFOR 2020: 시간별 SF/TF/저류/토양수분, 원 논문 명시적으로 지표유출 없음.
- McGuire 2016: Rutter intercept + Green-Ampt + 2D shallow-water + HR sediment, but no stemflow in original publication; fire-after field tests set interception OFF because vegetation burned.
- Beven & Van Stan + Di Prima 2026: macropore pathways may increase local infiltration instead of overland runoff.
- Chen 2026: 더 많은 줄기주변 강우에도 열간 침식이 지배: 강우량과 뿌리/투수성의 경쟁.
- Li & Tian 2026: throughfall drop KE를 성분별 추정, 침식 detachment forcing의 중요한 별도 변수.

## 새 결정문
decisions/2026-10-25_CANOPY_STEMFLOW_RUNOFF_EROSION_RESEARCH.md

## 추가 검증 필요
1. EUROSEM v3.6 내 줄기수간유하의 토양 요소 간 재분포가 실제 실행에서 가능한지 원본 구성파일까지 점검; 코드의 published functionality와 사용자 변경/새 coupling 분리.
2. Charlier 2009 전문 수식의 유출 구획 입출력/침투 매개변수 단위를 원 PDF로 대조.
3. McGuire 2016 Rutter drainage가 각 격자당 단일 net input이고 stemflow term이 없는지 supporting info 및 코드 대조.
4. 수관적하 KE와 Hairsine-Rose raindrop detachment를 2중계산 없이 연결할 수 있는지 입자에너지-강우박리 매개변수의 차원/원 모형 가정 확인.
5. 초본 억새/참나무 맹아의 구조·뿌리·수관배수 실측/모형 논문을 구분하여 신규 검색.
6. 새 문헌마다 papers/, INDEX, MASTER 및 결정을 갱신한다. 기존 모델 최종 선정은 이 세션에서 변경하지 않음.

## 완료 상태
8개 paper md 추가, 결정문 추가, MASTER 요약 및 INDEX 논문 377편으로 업데이트. GitHub main에 저장됨.
