# 2026-10-26 고운사 SHETRAN 원본 native 구동 및 강우 5강도 검증 인계

## 판정의 최우선 출처
- [실제 원본 native Cobres 5강도 상세 결과](../decisions/2026-10-26_SHETRAN_472_NATIVE_COBRES_RAIN_QA.md)
- [원본 전체 호출경로 정적 감사](../decisions/2026-10-26_SHETRAN_472_FULL_PATH_SOURCE_AUDIT.md)
- [원본 강우/침식 빌드 및 분석 성공 CI](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40287116566)
- 원본 소스 SHA cf9cd540add78ad3accbaf62b4199d2032887f6b, SHETRAN 4.7.2.0, 코드를 고치지 않고 build flags만 GNU Fortran용 -ffree-line-length-none 추가.

## 이번 세션에서 실제 실행 성공한 것
1. 원본 upstream 전체 Fortran/C 의존성을 설치하여 Debug 빌드. 첫 시도 ZQmod.f90 287행 긴 소스줄에서 gfortran 오류, 이후 컴파일 플래그 보정으로 성공.
2. Cobres 17×29=493 지도칸, HDF5 육상 유효격자 176개, 원본 원자료 복제 후 FRD 종료시간 48 h 및 sediment 시작시각 0, 강우는 5관측소에 3h 10/20/30/40/50 mm/h를 각각 부여하고 이후 0; 강우없는 시험 포함 여섯 사상 모두 종료코드 0.
3. HDF5 s_v_er/s_t_dp 원자료 29×17×49시간기록, 입경 7개 s_dis 실제 생성 및 분석.
4. Native time-series **근사 적산** (원본 timestep exact 적산 아님):

| 강우(mm/h) | 순간 s_v_er 최대(mm/day) | 49시점 오른쪽 끝 적산 원토양 최대(mm) | 초기 DLS 대비 증가 최대(mm) | 근사 Δz 최소/최대(mm) | 하강/상승 격자 |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 / 0 | 0 / 0 |
| 10 | 2.7084 | 0.1431 | 0.0662 | -0.07687 / -0.00431 | 176 / 0 |
| 20 | 67.2599 | 6.7699 | 5.4159 | -1.35400 / +0.02479 | 174 / 2 |
| 30 | 105.3299 | 15.7236 | 12.6998 | -3.02378 / +0.01421 | 175 / 1 |
| 40 | 133.2840 | 23.5062 | 20.0784 | -4.82008 / +4.04589 | 173 / 3 |
| 50 | 430.5913 | 29.7016 | 20.3374 | -9.36421 / -0.01797 | 176 / 0 |

## 발견된 실제 문제
- 원본 SY51 초기 DLS=30mm, 하지만 원본 HDF5 첫 t=0 s_t_dp=0mm; 이는 초기 SYMAIN/SYINIT 전의 출력을 읽은 것이므로 30mm 퇴적으로 계산하면 오류.
- FR6 48h 원래 종료시각에도 실제 마지막 HDF5 시간은 48.315~48.862h (18.90~51.73분 초과); `run_sim.f90`의 최종 step이 종료시각보다 길어지는 구조.
- `SYMAIN`은 첫 호출에서 initialize-only: 첫 hydrologic timestep sediment computation missing 가능성; 아직 정밀 native test로 시간별 민감도 보정 못 함.
- BALSED 빈 함수, 정확한 입경별 전체 유사 수지 불명, native sediment state restart 누락, VS08 토심 재생성, bank/link elevation 별도 처리, 실제 DEM feedback 미구현.

## 생성한 코드
- `.github/workflows/shetran_native_cobres_smoke.yml`: full original native CI, 실제 rain tests, output artifact.
- `experiments/analyze_shetran_native_cobres.py`: native HDF5 및 SY51 baseline 진단; coarse temporal integration 정확 적산으로 혼동 금지.
- 기존 `experiments/shetran_original_event_bridge.py`는 DEM 재작성 외부 후처리만 수행. Restart_ready false.

## 다음 연구 단계
1. 원본 Fortran 진단 추가로 각 내부 timestep `GNU*DTUZ`를 정확 누적하고 `SYMAIN` 첫 호출 누락 native 수치 비교.
2. 모형 사건 종료시각 `UZNEXT <= TTH-TIH-UZNOW` 제한을 **명시적으로 수정한 실험용 fork**에서 원본과 A/B 비교해 강우총량 및 수지 검증; 원본 공개 SHETRAN을 자동 변경했다고 주장하지 않는다.
3. `BALSED` 대체하는 외부 입경별 고체체적 수지, 물수지 점검, `DLS/FBETA/FDEL` 정확 재시작과 수문 hotstart, 압밀 및 지반기준 고도 정합성.
4. 사상 1 후 FR37/OC35/VS08/SY51–53 모두 새 입력으로 재조립하고 **사상 2 native 실행**의 수문 경로/침식 변화 검증.
5. 잔존 토심 상한 및 기반암 노출, 억새/참나무 맹아 정량 입력, 암편 spall/armoring으로 확장. Cobres 2km 지형을 고운사 0.5m TLS 결과와 혼동하지 않는다.

## 결정
원본 SHETRAN의 native 수문, 강우, 침식, 입경별 유사수송 모듈은 실제 실행됨을 실증. **강우사상 사이 모형 전체 물질수지와 지형 연동은 미검증**. 고운사 최종모형으로 자동 확정하지 않는다.
