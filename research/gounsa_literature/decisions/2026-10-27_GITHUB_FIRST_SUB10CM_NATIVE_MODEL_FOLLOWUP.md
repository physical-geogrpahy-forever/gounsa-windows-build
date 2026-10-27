# 2026-10-27 GitHub 우선 대조 후 5–10cm 단일 수관침식 원본 추가 모델 판정

## 결정 내용
2026-10-27 17:20 이전까지 완료된 467편 논문, 93개 모델 인덱스, LISEM 3개 브랜치 감사, SHETRAN 4m 35회 실험, 10cm 전역 배열제약, OpenLISEM Classic 7.5.2 침식유사수지 Δt 비수렴 결론을 최우선 기준으로 확인하고 검색함. **고운사 완전 조건 PASS인 신규 공개 실행원본 미확정**. 조건 누락 후보는 신규 채택 금지.

## 기존 기록 중복 대조
- `SYSTEM.md` 규정 읽음. `MASTER.md`, `INDEX.md`, `decisions/2026-10-27_5CM_10CM_CANOPY_2D_EROSION_NATIVE_MODEL_SCREEN.md`, `...SHETRAN_SUB10CM...`, `...LISEM_ALL_PUBLIC_BRANCHES_CODE_AUDIT.md`, 최근 `sessions/2026-10-27_1720_SUB10CM_CANOPY_EROSION_FOLLOWUP_HANDOFF.md` 확인.
- TREX, CASC2D, SHETRAN, LISEM Classic, van den Bout LISEM, PSEM_2D, GSSHA, SWEHR, tRIBS-FEaST, MAHLERAN, SERGHEI-SE, SMODERP2D 등 이미 심사된 이름을 신규 모델로 재추천하지 않음.

## 새 실제 10cm 연구: Cuomo (2018)
Sabatino Cuomo, `Modelling of rainfall-induced runoff and superficial erosion in unsaturated air-fall soil deposits`, DOI 10.19199/2018.3.0557-1405.31.
- LISEM **0.1m 실제 계산격자**의 나지, 35% 피복 초본 사면 실험 재현. LAI=6 및 clumped grass canopy LAI storage; runoff 및 sediment concentration 관측과 비교.
- 저자 논문 §4.2 명시: small flume 0.1m, dt=0.2×dx (즉 0.02s); 별개의 남부 이탈리아 산지 유역에는 5m 격자이므로 합치지 말 것.
- 논문에서 same run genuinely 2D freely spreading flow (full SWE) 또는 파일 단위 LISEM version checksum, grid DoD 퇴적고 검증 근거 없음.
- 이것은 Maggioli (2022) 5cm 외 추가 **published 10cm canopy+erosion 연구**, 그러나 OpenLISEM7.5.2 안정화나 고운사 native 모델 재채택 근거 아님.
- 상세: ../papers/2018_Cuomo_LISEM_10cm_LAI_Vegetated_Erosion.md.

## 신규 공개 코드 심사: LUCIA SustainSahel
- 기관 공식 https://lucia.uni-hohenheim.de/en/materials GitHub https://github.com/gcadisch/LUCIA_SustainSahel .
- `src/erodep/erodepModule.py` blob SHA `60d894f05504be50217c634f8d77bb5a05813292` 직접 검사.
- `interception` 상태, `E_detach_throughfall_1/2`로 direct/canopy throughfall rainfall splash, 입경별 이동/퇴적 존재.
- **LDD and `accufractionflux(self.LDD,...)` 로 유출 및 유사량 계산**. shallow-water X/Y 자유유동 아님. 모델 공식 예시 6,30,100m이며 published 5–10cm 유사수렴 확인 안 됨. strict **탈락**.
- 상세: ../models/LUCIA_SustainSahel_Code_Audit_2026.md

## 새 이름이었으나 엄격 조건에서 즉시 제외한 후보
- **CCHE2D / Jia et al. (2023)** DOI 10.1016/j.jhydrol.2023.129419 : 2D SWE 기반 UAS/photogrammetry 실험과 강우박리 및 침식, 지형변형. NCCHE https://www.ncche.olemiss.edu/downloads/ 모델 바이너리와 테스트판 공개, 하지만 최신 정식 모델은 상용 제공, 동일 원본 오픈소스 미확인. 논문은 경운 농경지이며 동적 LAI canopy interception 검증 없음. 원본 공개조건 충족 못함.
- **Feng et al. (2026)** DOI 10.1029/2025WR042040 : ELMv3-Erosion + TELEMAC-GAIA **두 모델 coupling**, 약 30m; 새 결합 모델/코드 존재하더라도 사용자 단일모델/5–10cm 미충족.
- **MEFIDIS**: 이벤트 수관/침식 연구이나 기본 흐름 경로는 1D kinematic 계열, 실험 최소 0.3m 보고. strict 탈락.
- **Ajayi et al. (2008)** vegetation-aware 2D SWE runoff, 공개 full sediment erosion/deposition solver 미확인. 단순 full 2D runoff ≠ sediment process.
- **LUCIA**는 제대로 공개된 원본에서 식생/강우타격/퇴적을 확인하였으나 LDD 때문에 제외함.

## 남은 해결되지 않은 핵심
1. **한 공개 실행판에서** cm급 실제 computational grid, dynamic canopy storage/drainage/throughfall, free 2D XY overland momentum, rainfall/flow detachment, deposition/mass balance가 동시에 작동했음을 재현하거나 published로 직접 확인하지 못함.
2. 기존 LISEM 7.5.2 침식출력의 큰 Δt 민감도와 sediment availability ledger 문제 원인 해결 전에는 LISEM 신뢰 판정 금지.
3. 기존 SHETRAN native 4m 사례를 10cm 논문 실증으로 제시하지 않음. 배열 규모 확장 자체만으로 물리적·수치적 유효성 주장을 하지 않음.
4. 새 DOI가 있어도 논문 초록의 capability listing만으로 published whole-path benchmark를 충족했다고 주장하지 않음.

## 다음 조사
정량 수관차단+침식 10cm 연구인 Cuomo(2018)의 실제 classic LISEM 버전과 매개변수 및 재현자료, Maggioli (2022) version 간 차이. 새 코드 후보의 경우 GitHub SHA를 통한 canopy/flow/sediment 실행경로부터 확인 후 5–10cm 연구 검색.

## 참고
- https://doi.org/10.19199/2018.3.0557-1405.31
- https://doi.org/10.1016/j.jhydrol.2023.129419
- https://doi.org/10.1029/2025WR042040
- https://github.com/gcadisch/LUCIA_SustainSahel/blob/main/src/erodep/erodepModule.py
