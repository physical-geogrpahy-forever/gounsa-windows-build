# 2026-10-27 SHETRAN 원본 검증의 중대한 정정: "시간간격 수렴 불합격"은 **TMAX가 아닌 PMAX** 실험이었다

## 원본코드 확인 (source SHA cf9cd540add78ad3accbaf62b4199d2032887f6b)

원본 `src/frame/FRmod.f90:5453–5456`:

```fortran
READ (FRD, '(4F7.0,L7)', IOSTAT=ios, IOMSG=emsg) PMAX, PALFA, QMAX, TMAX, BSOFT
```

원본 `src/driver/rest.f90:1330–1345`:

```fortran
IF (PTOT(I) > PMAX) THEN
  UZNEXT = MIN(UZNEXT, PMAX/PINP(I))
END IF
```

따라서 `PMAX`는 강우사상 중 timestep마다 허용할 최대 강우량(mm), `TMAX`는 원래 지정된 기본 최대 timestep (h), `BSOFT`는 처음 102 step의 timestep 축소 여부다. 원본 Cobres `input_cob_frd.txt`의 `BASIC TIMESTEP DATA` 레코드는 **`1.00 0.05 9999. 1.00 T`**라는 fixed-width 7-char 필드 5개.

### 확인한 기존 연구 스크립트 결함

`experiments/shetran_timestep_refinement_20261027.py`과 `experiments/shetran_timestep_forcing_probe_20261027.py`가 이전에

```python
lines[i] = f"{tmax:7.5f}" + lines[i][7:]
```

를 사용하여 `BASIC TIMESTEP DATA` 첫 7글자 `PMAX`만 변경하고 네 번째 필드 `TMAX`는 원본의 **1시간**으로 남겼다. 결과적으로 [Actions 40441585117](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40441585117), [40443456084](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40443456084), [40444641155](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40444641155) 등은 **PMAX 제한강우량 변화 실험**이었다. 종전 `TMAX 0.03125h vs 0.015625h 침식차 4.89%` 및 이전 분할 차이 5.8%를 *TMAX 수렴 실패 증거*라고 서술한 내용은 사실과 다르다.

고운사 연구 도중 이 검증오류를 원본 SHETRAN 자체의 수치 불안정이라고 해석한 것은 **부당하며, 종전 '시간간격 수렴성 불합격' 판정은 철회한다**. 단, 기존 결과는 `PMAX`에 따른 다른 동적 timestep 및 수문과 유사 결과의 민감도를 보여 주므로 재해석할 가치가 있다. 원본의 정량적 신뢰성 자체도 여전히 미검증.

### 확인된 다른 timestep 관련 사항

원본 `src/driver/rest.f90:1105–1131`는 `IF (BSOFT .AND. NSTEP <= 102) TSOFT = TMAX*0.05*1.03**NSTEP` 로, **초기 102 calculation steps 기반** softstart를 적용한다. 따라서 TMAX만 변경하더라도 softstart ON은 실제 경과시간과 초기사건 이력을 서로 다르게 만들 가능성이 있다. 이를 분리해 원본 `BSOFT=F`로 통일한 별도 시험이 타당하다.

원본 `src/sediment/SYmod.f90::SYMAIN:3469–3485`는 `SYWAT→SYOVER`을 상위 수문 timestep마다 한 번 계산하고, `DTSY=DTUZ/NEPS`로 내부 유사 timestep을 나눈다. 그러므로 실제 TMAX 변화는 SYOVER의 원토양 박리율 평가시각, 수심/전단응력 입력, 내부 DLS 재투입 모두에 영향을 줄 수 있다. **원인 결함으로 판정하기 전에 올바른 TMAX sweep 결과를 보아야 한다.**

## 수정한 실험 코드와 재현성

- 수정 `experiments/shetran_timestep_refinement_20261027.py`: `FRD` 원본 네 번째 `[21:28]` 필드만 `TMAX`로 기록, 첫 `[0:7]` `PMAX=1.0` 불변 확인, 보조실험 `BSOFT=F`. 0.015625h 등을 7자리 내 `.015625`로 정확 입력한다. 
- 수정 `experiments/shetran_timestep_forcing_probe_20261027.py`도 같은 규약 적용.
- [실제 원본 TMAX 재시험 workflow](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40445638896) — status/결과 확인 전까지 **TMAX 수렴성 최종 판정 없음**.
- [원본 기상 적산 통제](https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40445644339) — 똑같은 90mm forcing 적산 여부 다시 확인.
- 실제 사면은 여전히 합성 4m, 활성176 cells, PET0, 혼재 NVC 2종, closed boundary; 개방 경계와 0.5/1/2m 공간수렴, finite soil available stock, 실제 고운사 데이터 미검증은 변함없음.

## 판정 수정

| 확인 항목 | 이전 주장 | 올바른 현재 판정 |
|---|---|---|
| 원본 4m 합성사면 2D canopy+박리+입경별 유사 4방향 이동, 퇴적 | 통과 | 코드/원본 native 기능 통과 유지 |
| native 이동가능 유사 closed-domain budget | 통과 | 통과 유지 |
| original canopy interception conservation PET0 | 통과 | 통과 유지 |
| TMAX 시간간격 수렴성 | **불합격** | **이전 시험이 PMAX sweep였으므로 아직 미검증** |
| PMAX 강우제어 시간분할 민감도 | TMAX 민감도라고 오명명 | 실제 PMAX에서 상당한 반응차 발생 (수치 원인 추가 분석 필요) |
| 고운사 소사면 실제 관측 검증, 공간수렴, open boundary | 미완 | 미완 그대로 |

**연구자의 요청에 응하는 원칙:** 잘못된 시험 설정을 그대로 두고 SHETRAN 탈락 선언 금지. 원본 `TMAX`로 실제 시간간격 수렴부터 재실행하며 이후 canopy/flow/erosion component별 원인 분해. 단일모델 유지. 
