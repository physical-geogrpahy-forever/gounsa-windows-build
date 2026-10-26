# 2026-10-26 강우사상 침식량 물리 타당성 검증 인계

## 새 문헌
- papers/2001_Johansen_PostfireRunoffErosionRainSimulation.md
- papers/2008_Kinner_Moody_SteepBurnedHillslopeRainfall.md
- papers/2024_Gangneung_WUI_RUSLE_SEMMA.md
- papers/2026_Samoil_BurnSeverityHillslopeRainSimulator.md

## 이번 확인과 판정
- decisions/2026-10-26_RAINFALL_EROSION_PHYSICAL_VALIDITY_AUDIT.md 생성 및 MASTER/INDEX 갱신.
- 2016_McGuire_SWEHR_Postwildfire_2D.md에 정확한 DOI, 원 논문 검증과 공개 코드 QA를 구분해 추가.
- 원본 공개코드/예제 10–50 mm/h 재현 실험의 출력은 고운사 침식량으로 모두 기각. SWEHR 전체 격자별 gross lowering 0.019m³와 bed rise 0.549m³의 차이는 검증되지 않음. EUROSEM 30mm/h 물수지 오차 12.86%, 40mm/h 28.89%, 50mm/h 실패.
- 한국 강릉 모형 0.07–94.9 t/ha/storm은 모의값이며 실측치로 취급 금지. Johansen(2001), Samoil(2026)은 현장실측이지만 지질/토양/강우 조건이 달라 고운사 10-50mm/h 상한으로 직접 전이 금지.
- 원본 실행/재현성 자료: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/rainfall-sensitivity-original-models-20261025/experiments/rainfall_10_50
- 수치 후처리 독립검증 Actions: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40253018836

## 재검증 시 우선사항
1. SWEHR 초기 토사층 상태 U[1]/SOLID/M과 초기지형 변환의 차이를 확인하는 무강우/무침식 독립 검증.
2. 소스 내부 유출 경계의 water and solid flux 적분, mass closure.
3. EUROSEM 반복 실행 불일치 원인과 경계 연결 오류(현재 2 plane unconnected) 진단.
4. root macropore infiltration, spatial SF & TF source, and rainfall drip KE 와 genuinely 2D erosion coupling 연결; 시험모델/원본 기능 구분.
5. 측정된 고운사 면적, 토심, 지형, 입도, 원식생 우점종별 식생구조를 넣기 전에는 t/ha/event 수치 보고 금지.
