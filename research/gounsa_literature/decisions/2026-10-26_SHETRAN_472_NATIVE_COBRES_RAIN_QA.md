# SHETRAN 4.7.2 원본 native Cobres 강우 및 침식 실행 검증 (2026-10-26)

## 판정 및 출처
- **실제 공개된 원본 Fortran 본체를 컴파일하고 실행했다.** upstream nclwater/Shetran SHA `cf9cd540add78ad3accbaf62b4199d2032887f6b`, CMake `SHETRAN 4.7.2.0`. SHETRAN 원본 방정식과 소스 코드는 변경하지 않음.
- OS: GitHub-hosted Ubuntu 24.04, GNU Fortran Debug, `FFLAGS=-ffree-line-length-none`. 외부 원본 종속 tarball (HDF5, zlib-ng, Fortran stdlib)로 CMake 빌드.
- 첫 시도 [40285351729](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40285351729)는 `src/overland_channel/ZQmod.f90:287`이 gfortran free-form 기본 행 길이 132열을 초과해 실패. **원본 코드 수정 없이** free-form 길이 컴파일 옵션 적용 후 [40285558709](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40285558709)에서 빌드, native Cobres 48시간 실행, HDF5 생성/열기 성공.
- [최종 native 6사상 실행 40287116566](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40287116566): 강우 없음, 10, 20, 30, 40, 50 mm/h 각각 3시간 강우 후 건조. 모두 원본 SHETRAN native .exe에서 실제 수행, 모든 단계 성공. 앞선 0/10/30/50 시험 40286452968도 성공.
- 실행 및 데이터 파일: [native QA workflow](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/.github/workflows/shetran_native_cobres_smoke.yml), [native diagnostics script](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/analyze_shetran_native_cobres.py). 출력 HDF5/CSV/log를 Actions artifact `native-cobres-48h-forensic-logs`로 저장(14일 보존).

## 원본과 시험용 입력의 구분
원본 `examples/Cobres/model/` 전체를 시험 임시 디렉터리로 복사. 물리과정 Fortran 변경 없음.
원본 FRD: 17 x 29 = 493 지도 칸(이 중 HDF5에서 유효한 육상 격자 176개), 2 km 격자, 시뮬레이션 1977-10-01~12-01, sediment 원래 시작 10-02.
시험용 **복사 입력만**: 종료시각을 1977-10-03 00:00으로 변경, sediment를 10-01 00:00부터 활성화. 폭우 시험용 `input_wet_prd.txt`의 처음 3시간을 5개 강우관측소 공통 강우 10, 20, 30, 40, 50 mm/h로 변경, 나머지 45시간 0으로 설정. 0 강우 native run도 별도로 실시. 수관, 지형, 초기 토양, 침식계수 등은 Cobres 예제 그대로 사용했으며 **고운사 파라미터가 아님**.

## 실제 HDF5와 수치 결과
- HDF5 `s_v_er`, `s_t_dp`는 각각 **29 x 17 x 49 시점** 기록. `s_dis` 7개 입경도 출력. 유효 육상 격자 176개.
- `s_v_er` 순간 mm/day; `s_t_dp` 현재 느슨한 표층퇴적물 깊이 mm; `s_dis` face별 kg/s. `s_v_er`의 원토양 박리두께 적산은 실제 내부 timestep `GNU*DTUZ`가 아직 아니라 **HDF5 시계열 오른쪽 끝값 × 관측 간격**의 근사임.

| 강우강도 (3시간) | `s_v_er` 최대 순간값 mm/day | HDF5 오른쪽 끝 적산 최대 원토양 박리 mm(근사) | 초기 SY51 대비 `DLS` 최대 증가 mm | 유효 육상격자 중 근사 침식 >0 |
|---|---:|---:|---:|---:|
| 0 mm/h | 0 | 0 | 0 | 0/176 |
| 10 mm/h | 2.708354 | 0.143090 | 0.066216 | 176/176 |
| 20 mm/h | 67.259918 | 6.769896 | 5.415897 | 176/176 |
| 30 mm/h | 105.329895 | 15.723558 | 12.699776 | 176/176 |
| 40 mm/h | 133.283951 | 23.506236 | 20.078381 | 176/176 |
| 50 mm/h | 430.591309 | 29.701565 | 20.337357 | 176/176 |

**주의**: 박리량 최대와 DLS 증가 최대가 동일 격자라는 뜻이 아님. 누적값을 `real native GNU-integral`이라고 명명하지 말 것. 3시간 50 mm/h를 고운사 실제 3 t/ha/year와 그대로 비교하는 것은 부당함(공간격자, 토양, 강우 시간척도, 예제 매개변수 불일치).

## 검증 중 확인된 실제 의미상의 함정

### 1) HDF5 시각 0 퇴적층은 초기 SY51과 불일치
원본 `input_cob_syd.txt` `SY51c`는 모든 대상 격자의 초기 `DLS=0.03 m` (30 mm), `SY12`은 `DLSMAX=0.05 m` (50 mm).
그러나 native HDF5 `s_t_dp`의 **t=0 값은 0 mm**, 첫 이후 저장부터 30 mm 또는 강우로 변한 값.
코드상 `run_sim`에서 시각 0 `RECORD_VISUALISATION_DATA`가 `SYMAIN` 초기화보다 앞서 호출됨.
**가짜 30 mm 퇴적**을 만들지 않도록 기준상태는 HDF5 t=0이 아니라 **원본 SY51 초기상태**와 비교해야 함. 현재 `analyze_shetran_native_cobres.py`에서 이 문제를 수정함.

### 2) 기대 종료시각을 native 계산이 넘김
`FRD:FR6`가 지정한 48.000 h에 반해 실제 마지막 HDF5 시간:
| 강우 | 마지막 HDF5 시각 h | 초과분 분 |
|---|---:|---:|
| 0 | 48.315079 | 18.90 |
| 10 | 48.632286 | 37.94 |
| 20 | 48.543804 | 32.63 |
| 30 | 48.584282 | 35.06 |
| 40 | 48.862160 | 51.73 |
| 50 | 48.375805 | 22.55 |

`run_sim.f90`에서 `TMSTEP` 후 `UZNOW+=UZNEXT`, 계산 및 기록 뒤에 `IF(UZNOW >= TTH-TIH) EXIT`를 검사. 즉 종료시각을 넘어선 적응적 마지막 timestep을 허용함. *강우사상 간 외부 연결에 중요한 확정적 시간 경계 결함*. 복제 원본에 `TMSTEP` 내부 `UZNEXT <= TTH-TIH-UZNOW` 상한을 넣는 것은 후속 **명시적 새 코드 수정**으로서 A/B 검증할 것. 이번 원본실행은 수정하지 않음.

### 3) 강우가 없는 smoke test는 erosion regression이 아니다
0 mm/h 시나리오에서 `s_v_er=0`, 하지만 `s_dis` 2번 입경의 미약한 face flux는 존재. 최초에 dry 48h만 성공했다고 해서 erosion 기능이 물리적으로 검증되었다고 할 수 없음. 이후 폭우 시험으로 `GNU>0`과 `DLS` 변화가 실제로 발생함을 확인함.
`DLS>0.05m`까지 성장하는 50 mm/h 사례에서는 `SYOVER`이 물수문 timestep마다 한 번, `SYCOLM`이 하위 sediment substeps를 반복하는 보호 지연 가능성 별도 테스트 필요.


## 6사상 최종 추가결과: 근사 순지표고 변화 (2026-10-26, run 40287116566)
실제 native HDF5 유효육상격자 176개에 대해 시계열 오른쪽 끝 누적 박리와 **SY51 초기퇴적층 30 mm 대비** 최종 `DLS` 차이를 계산하여 `Δz_approx=ΔDLS-SUM_right(GNU*dt)`로 구한 참고값. 이는 native exact-integral 및 native DEM 갱신이 아니며, 고운사 예측치도 아니다.

| 강우 mm/h | 최소 Δz_approx mm | 최대 Δz_approx mm | 하강 격자/176 | 상승 격자/176 |
|---|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 10 | -0.07687 | -0.00431 | 176 | 0 |
| 20 | -1.35400 | +0.02479 | 174 | 2 |
| 30 | -3.02378 | +0.01421 | 175 | 1 |
| 40 | -4.82008 | +4.04589 | 173 | 3 |
| 50 | -9.36421 | -0.01797 | 176 | 0 |

40mm/h 사례의 최대 상승이 50mm/h보다 큰 이유는 별도 수지, 공간별 flux, `DLSMAX`, time-integral과 입경분포를 검사해야 확정할 수 있음. 단순히 전체적으로 퇴적이 많아졌다고 결론 내리지 않는다.

**매우 중요**: 40 mm/h 종료 시각 초과는 51.73분으로, 이 보고서의 종료시간 표도 6사상 전체 기준으로 판정한다.

## 여전히 미검증
1. 각 내부 timestep `GNU*DTUZ` 정확 적산값과 시계열 근사의 차이 및 `FRRESP` 출력44 초기화 경고.
2. 원본 `BALSED`가 빈 함수이므로 **독립적인 solids mass balance**, 특히 `FETA=(1-THSAT)/(1-PLS)`로 변환된 원토양 solid volume, suspended/loose/channel/outlet 총수지.
3. `SY51,DLS`, `SY52,FBETA`, `SY53,FDEL`, bed states 및 수문 hotstart까지 연동한 native event2 재시작.
4. `FR37/OC35/VS08`의 깊이/토심/고도/수두를 동시에 새 초기상태에 반영하는 진정한 장기 morphodynamic feedback.
5. 잔존토심 초과 침식의 bedrock clamp, 억새 vs 참나무 뿌리량과 litter의 정량 연결 및 산불 후 암편 과정.
6. 10–50 mm/h의 **5강도 native 실행은 성공**. 다만 정확한 GNU 내부 적산, 측정규모 적합성, 시나리오 교정은 별개 과제.

## 최종 판정
**원본 SHETRAN 실제 Fortran 빌드 및 강우/침식/퇴적 native 실행: 확인됨.**
**사상간 morphodynamic DEM 및 상태의 완전한 연동, 질량보존, 고운사 현장 적용: 미완료.**
임의 외부 코드를 원본 published 기능이라고 주장 금지.
