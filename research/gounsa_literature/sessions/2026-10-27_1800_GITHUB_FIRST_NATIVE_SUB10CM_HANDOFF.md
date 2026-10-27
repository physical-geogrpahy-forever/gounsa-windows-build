# 2026-10-27 18:00 GitHub 선대조 5–10cm 단일모델 인계

## 이번 세션에서 새로 찾은 문헌
- **Cuomo (2018)** `Modelling of rainfall-induced runoff and superficial erosion in unsaturated air-fall soil deposits`. https://doi.org/10.19199/2018.3.0557-1405.31 . Classic LISEM을 실제 0.1m computational DTM, 나지와 35% 초본 피복에 적용; LAI 6 clumped grass canopy interception, 런오프/유사농도 실험 비교. 시간간격 논문 규칙 0.2×dx→0.02s. 단 원본 LISEM 소스버전 및 full 2D hydrodynamic 확인 못함. 5m 실제 산지유역 실험은 10cm 실험과 구별. [논문별 저장](../papers/2018_Cuomo_LISEM_10cm_LAI_Vegetated_Erosion.md).
- CCHE2D / Jia et al. (2023) https://doi.org/10.1016/j.jhydrol.2023.129419: photogrammetry + flow/erosion/deposition, 하지만 forest LAI canopy / 정식 공개 소스 요건 불통과; 발표 원문과 공식 NCCHE 공개/상용 배포 페이지 교차 확인.
- Feng et al.(2026) https://doi.org/10.1029/2025WR042040: 30m ELM-Erosion + TELEMAC-GAIA 모델 결합, 사용자 단일모델 조건 불통과.
- Ajayi et al.(2008): vegetation dynamic intercepted overland 2D runoff 강점 있지만 sediment transport+deposition 코드 미확인.
- MEFIDIS 및 LUCIA 등의 소개를 추가 검색했으나 strict 2D SWE 조건 통과 없음.

## 새로 확인한 코드 사실
- **LUCIA 공개 원본** https://github.com/gcadisch/LUCIA_SustainSahel `src/erodep/erodepModule.py` blob 60d894f05504be50217c634f8d77bb5a05813292. `E_detach_throughfall_1/2` 및 모래/실트/점토 퇴적 있지만 `self.LDD`, `accufractionflux(self.LDD,...)` 사용, 자유 XY 지표수 방정식이 아님. [코드감사 기록](../models/LUCIA_SustainSahel_Code_Audit_2026.md).

## 기존 판정 및 변화
- 이전 `decisions/2026-10-27_5CM_10CM_CANOPY_2D_EROSION_NATIVE_MODEL_SCREEN.md` 및 SHETRAN, LISEM code SHA audits부터 읽음.
- **독립적인 LISEM 10cm canopy+erosion 실험 논문 1편 추가**는 새로운 사실. 이미 확인된 Maggioli2022 5cm, PSEM_2D 나지 5cm, Epple2025 1cm 등은 중복 신규발견이라고 제시하지 않음.
- **고운사 요구조건 전체 PASS 모델 여전히 발견 못함.** LUCIA source-backed 탈락.
- 상세 결정 [2026-10-27_GITHUB_FIRST_SUB10CM_NATIVE_MODEL_FOLLOWUP.md](../decisions/2026-10-27_GITHUB_FIRST_SUB10CM_NATIVE_MODEL_FOLLOWUP.md).

## 이번 세션 GitHub 신규파일
- `papers/2018_Cuomo_LISEM_10cm_LAI_Vegetated_Erosion.md`
- `models/LUCIA_SustainSahel_Code_Audit_2026.md`
- `decisions/2026-10-27_GITHUB_FIRST_SUB10CM_NATIVE_MODEL_FOLLOWUP.md`
- `sessions/2026-10-27_1800_GITHUB_FIRST_NATIVE_SUB10CM_HANDOFF.md`

## 미확인 사항
원본 7.5.2 유사수렴 문제 해결 없음. 신규 LISEM 10cm 논문의 exact executable version와 독립 2D SWE 사용 여부, 공개 재현용 설정/데이터 미확인. 5–10cm 동일 실행원본 물수지/유사수지 및 지면고도 검증 아직 없음. 이번 검색과 코드 읽기는 네이티브 컴파일/시뮬레이션 성공에 해당하지 않음.

## 다음 작업
`MASTER.md`와 `INDEX.md`, 위 결정문을 먼저 읽고, **현재 탈락 모델 재추천 금지**. Cuomo LISEM exact version/input provenance와 기존 2022 Maggioli 차이를 먼저 추적. 동시에 원본 native canopy+2D sediment가 기능 수준 아닌 실행경로 수준에서 일치하는 공개 모델만 선별.
