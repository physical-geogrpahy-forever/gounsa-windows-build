# SHETRAN 20 mm/h 침식량 6.77 mm의 원인 분해: native 원본 Fortran 6회 실행

날짜: 2026-10-26
원본 upstream `nclwater/Shetran` commit `cf9cd540add78ad3accbaf62b4199d2032887f6b`, model v4.7.2.0. 원본 Fortran 미변경.
재현: [GitHub Actions run 40289105946](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40289105946), [Native input-only mechanism program](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/blob/main/experiments/shetran_native_mechanism_probes.py).

## 질문과 왜 실험했는가
원본 Cobres(2km 격자) 강우 20 mm/h 3시간 조건에서 최대 순간 원토양 박리율 `s_v_er=67.2599 mm/day`, 시간별 출력 우측적산 최대 `6.7699 mm`의 크기가 과도하다는 지적. `s_v_er`는 **순유역토양유실이나 하루 누적 침식이 아니라 순간 mm/day 단위의 원토양 박리율**이다. 비교할 사건 3h 최대 적산 박리량은 약 6.77 mm (0.677 cm)다. 67.26 mm/day는 그 속도를 24h 유지할 경우 6.726cm/day의 차원으로 환산한 것일 뿐.

원본 토양 bulk density `RHOSO=1537kg/m3`, 6.7699mm 최대 격자에 해당하는 in-place soil mass `0.0067699 ×1537 × 10000/1000 ≈104.05 t/ha` (**총박리 환산, 출구 유사유출이나 연간 순손실 아님**). 현장 연평균 순토양유실 3t/ha 참고치와 직접 동질 비교 불가. 그래도 고운사 산림 연구에서는 원인과 교정 필요.

## 실제 실행 조건
- 원본 `examples/Cobres/model/`을 6개 폴더로 복사, native SHETRAN `gfortran -ffree-line-length-none`의 실제 Fortran 실행파일로 각각 실행. 원래 저장소의 Fortran 코드는 한 줄도 바꾸지 않았음.
- 강우 `input_wet_prd.txt` 5관측소에 20 mm/h 3시간 후 0, FR6 사상종료 48h, FR7a sediment 시작 0. 다섯 다른 예제 설정은 고정하고 `input_cob_syd.txt`의 1개 지정항목만 변경한 통제실험.
- 원본 `SY22`은 `GKR=2.5`, `GKF=1.0e-5`, `RHOSO=1537 kg/m3`, `FPCLAY=0.26`. `SY41c FCG=0.3`, `SY42c FCROCK=0`, `SY24 XDRIP=3m, DRDRIP=0.005m, FDRIP=0.5`. `SY12 DLSMAX=0.05m`, `SY51c DLS_initial=0.03m`.
- HDF5 `s_v_er=GNU×86400000` mm/day, 49 기록시점 / 육상 유효격자 176개. 우측끝 적산은 **native timestep 정확 적산은 아니며** Run 종료시간 48.544h도 FR6 48.0h를 초과함.

## 실제 분리 결과

| 입력사본 조건 | 최대 `s_v_er`(mm/day) | 최대 시계열 누적 원지반 박리(mm, 근사) | 176개 육상격자 평균 박리(mm, 근사) |
|---|---:|---:|---:|
| 원본 Cobres | 67.259918 | 6.769896 | 1.866657 |
| GKR=0, 강우박리 없음 | 67.237823 | 6.732517 | 1.831384 |
| GKF=0, 유수박리 없음 | 0.723569 | 0.037378 | 0.035273 |
| GKR=0 및 GKF=0 | 0 | 0 | 0 |
| FDRIP=0, 수관적하 충격 제거 | 67.239601 | 6.735519 | 1.834222 |
| FCG=0.9, 지표피복 90% | 67.240974 | 6.737857 | 1.836423 |

**핵심: 원본 max 박리량 6.76989569mm 중 6.73251747mm가 `GKR=0`인 유수박리 단독에서, 0.03737823mm가 `GKF=0`인 강우박리 단독에서 발생. 둘의 합은 원본 최대 박리와 수치적으로 일치(소스 nonlinearity가 없는 이 특정 실험). 최대박리 기준 `6.732517/6.769896=99.45%` 유수박리, `0.55%` 강우박리. 176개 평균기준 유수단독 `1.831384/1.866657=98.11%`, 강우단독 `1.89%`.** 최대 격자가 동일한지는 원본 좌표별 검증 전까지 단정 금지하나 일치하는 최대값 관계가 확인됨.

## 정확한 원본 계산식과 과도한 침식 후보
원본 `src/sediment/SYmod.f90`, `SYOVER`:
```fortran
DR = GKR(ISOIL)*EXP(-MAX(ZERO, (DWAT1(IEL)/DRDROP(IEL)) - ONE))* &
     (ONE - FCG(IEL) - FCROCE)*(GMR + GMD)
CALL SYCRIT(ISTEC, DRSO50(ISOIL), TAUKE, FPCLAY(ISOIL), TAUEC)
DF = GKF(ISOIL)*(ONE - FCROCE)*MAX(ZERO, TAUKE - TAUEC)/TAUEC
IF (DLS(IEL) < DLSMAX) THEN
  GNU(IEL) = (DR + DF)/RHOSO(ISOIL)
ELSE
  GNU(IEL) = ZERO
END IF
```
- `FCG`(지표피복률)은 **강우박리 DR에만 직접 작용**. 유수박리 DF에는 `FCROCK`과 `GKF`, `τ/τc` 등이 포함되고 식생/뿌리량 자체의 억제항은 없다. 이 실험에서 피복률 30%→90%의 효과는 max gross 6.769896→6.737857 mm, 감소율 약 0.47%.
- `DLS_initial=30mm`에서 `DLSMAX=50mm`까지 원토양 `GNU`에 **퇴적층 두께 비례 억제는 없고 임계값 기반 on/off**. 20mm/h 실험에서는 최대 `DLS` 증가 5.416mm 정도로, 초기 30mm에서 시작하므로 보호 임계 50mm에 도달하지 않는다.
- Cobres 원본 `ISTEC=0`은 `SYCRIT`의 Shields-based critical stress를 사용하며 `FPCLAY=0.26`은 임계전단응력 계산에 사용되지 않는다. `ISTEC=1`은 `τc=0.493 exp(1.83 ln(10)×FPCLAY)` 식을 사용. 두 옵션 간의 정확한 native 수치 비교는 별도 실행해야 확정할 수 있다.
- **1단계 결론**: 과대한 총 원지반 박리는 빗방울 충격이 아니라 **유수전단응력 기반 DF 항**이 거의 전부를 생산. `GKF`, `τ/τc`, `ISTEC`, `DLSMAX`, 초기 토층 상태와 가짜 고빈도 event forcing 여부를 검증해야 함. 근거 없는 `GKF` 0 강제나 임의 calibration으로 논문 교정 결론 금지.

## 코드 및 분리 원칙
모든 조건은 실제 native `shetran` compiled exe, original Fortran source 유지. `GKR=0` 및 `GKF=0`은 실험용 **과정 분리 통제변수**이지 고운사 최종 물성값이 아님. 2km Cobres 예제의 176 토양격자 3시간 강우 결과를 고운사 사암 산림 0.5m TLS의 현장 침식량으로 제시 금지.

## 다음 단계
1. 20mm/h `ISTEC=1` vs native `ISTEC=0`의 임계전단응력 및 gross sediment 비교. Shields `D50` 0.1mm와 점토 26%의 물리적 의미 구분.
2. `GKF` 10배/100배 변화는 **민감도**이지 교정값이 아님. native `TAUK`, `TAUEC`, `DF/DR`의 공간별 값을 직접 출력하는 진단 실험이 필요.
3. 정확한 원본 substep `ΣGNU Δt` 적산과 유사/물 수지 검증 후 연속강우사상 DEM 상태 전달.
