# 2026-10-27 비-LISEM 신규 공개 원본 비교 검증

## 목적과 판정
고운사에서 이미 탈락시킨 모델을 반복하지 않고 새 공개 코드를 조사하였다. OpenLISEM 수정은 다른 Work가 담당한다. 이번 결과는 **SMODERP2D 원본에서 강우와 세류 유출은 작동하지만 침식 토사량 계산을 찾지 못했고, WaTEM/SEDEM 원본은 토사 침식·퇴적량을 계산하지만 연평균 모델로서 수관차단·6시간 자유 2D 유동은 지원하지 않는다는 것**이다. 둘 다 5~10cm 강우사상 단일 주모델로는 탈락.

## SMODERP2D
- 공식 https://github.com/storm-fsv-cvut/smoderp2d
- 원본 [코드 검증](../models/SMODERP2D_2019_2026_Native_Interception_Rill_Without_Sediment_Source_Audit.md), [직접 결정](2026-10-27_SMODERP2D_ACTUAL_SOURCE_RILL_RUNOFF_NOT_SEDIMENT_NATIVE_NO_GO.md).
- [Landa et al. (2019)](../papers/2019_Landa_Jerabek_Pesek_Kavka_SMODERP2D_OpenSource_Parallel.md), DOI 10.5194/isprs-archives-XLII-4-W14-143-2019. 원문 7쪽 PDF screenshot으로 본문 D8, 침투, interception, sheet/rill Manning, CFL 확인.
- [Kavka et al. (2022)](../papers/2022_Kavka_Jerabek_Landa_SMODERP2D_SheetRill_ThreeScaleValidation.md), DOI10.3390/w14030327. 2×8m/60mmh 실험구, 50m² 유출관측구, 36.6ha 현장세류분포 **5m 계산격자**. 세류 분포 비교는 토사 질량 계산 검증이 아님.
- [Neumann (2022)](../papers/2022_Neumann_SMODERP_Sediment_Transport_PhD_Experimental_Evaluation.md), 공식 박사논문 http://hdl.handle.net/10467/104997: 450회 이상 4°~34°/40~160mmh 실험으로 후속 유사이송식 연구. 공개 작동 바이너리에 완성 유사루틴이 있다는 증거는 아님.
- 코드 `processes/rainfall.py`의 leaf proportion * rain, potential interception cap; `kinematic_diffuse.py` D8/MFDA; `time_step.py` sheet/rill routing만 확인, 활성 sediment detach/transport/deposit 미확인.

## WaTEM/SEDEM
- 공식 개발팀 KU Leuven: https://ees.kuleuven.be/en/geography/modelling/erosion/watem-sedem
- 공식 공개 소스 https://github.com/watem-sedem/watem-sedem (LGPL3, Free Pascal, source+binaries), 보존 2024 Zenodo https://doi.org/10.5281/zenodo.10997288.
- [Van Rompaey et al. (2001)](../papers/2001_VanRompaey_Verstraeten_VanOost_WaTEM_SEDEM_AnnualSediment.md), DOI10.1002/esp.275.
- [원본 Pascal 감사](../models/WaTEM_SEDEM_2024_Pascal_Native_Annual_RUSLE_Sediment_Audit.md): `common/runmodel.pas` routes topographic flow and calculates RUSLE LS; `docs/watem-sedem.rst` annual gross soil erosion R·K·LS·C·P; `docs/routing.rst` downstream 1~2 pixel flux; `docs/formulas-units.rst` TC-limited incoming plus erosion and cell deposition.
- 유사 퇴적 계산은 실제 존재하지만 **연평균 RUSLE + 하류방향 유사분배**이다. 강우 강도에 따른 6시간 수관저류 C(t), LAI/수관낙수 KE, full XY hydrodynamic momentum, 초단위 침식 연속방정식은 원본 확인 안 됨.

## 공통 하드게이트
- 소스 제공: 둘 다 확인.
- 고운사 식생 수관저류 동적 LAI/수관통과/적하: 둘 다 불충족.
- 전방향 자유 2D 흐름: 둘 다 D8/MFD 또는 하류방향 분배, 불충족.
- 강우 및 유수 박리와 국지 퇴적을 한 강우사상 동안 동시 계산: 둘 다 불충족.
- 원본 5~10cm 선행연구: 둘 다 확인 못함.

**결론: 새로운 논문 4건(2019, 2022 peer-reviewed, 2022 doctoral, 2001 peer-reviewed)과 두 별도 공개계열 실제 코드 검증 완료, 고운사 all-PASS 신규 주모델은 미확보.**
