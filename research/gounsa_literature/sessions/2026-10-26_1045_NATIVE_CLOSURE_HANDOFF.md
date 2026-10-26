# 2026-10-26 SWEHR/EUROSEM source closure handoff

## 이번에 한 일
- SWEHR 원본의 j=ny forced external water+sediment inflow(경계 설정 이후 무조건 적용됨) 제거, 수심 U[1], loose layer M, SOLID 및 sed states 초기조건 명시.
- 원본 SWEHR C 9개 시험 실행 통과. 강우 10,20,30,40,50mm/h, 1h. Ks=2e-6m/s, a=ad=0.25, F=0.004, 원래 3×51 dx=0.25m test DEM. water volume and two independent sediment ledgers pass; measured observed field validation은 아님.
- EUROSEM 원본 F77 gfortran 디버그/배열 범위 점검. 테스트 2 independent plane→1 plane, hyetograph declared point count2→actual3 및 unused gauge/order line 제거. 강우 5조건 모두 물수지 <0.034% pass, 30mm/h 반복값 일치. 원본 출력 폭 F9.3→E14.6로 수정해서 sediment mass 판독 가능. 독립 유사수지는 NOT PASS / NOT AUDITED.
- 지배 침식 방정식은 변경하지 않았으나 초기, 외부 공급, 시험 매개변수, 출력 포맷, 검증용 장치만 구분해 수정.
- main decision: decisions/2026-10-26_SWEHR_EUROSEM_SOURCE_CLOSURE_VERIFICATION.md. MASTER / INDEX 갱신.

## 코드와 실행
- branch: swehr-water-sediment-closure-20261026
- experiments/rainfall_10_50/verify_swehr_closure.py
- experiments/rainfall_10_50/verify_eurosem_native.py
- experiments/rainfall_10_50/CLOSURE_VERIFICATION_2026-10-26.md
- .github/workflows/swehr_mass_budget.yml
- .github/workflows/eurosem_native_qa.yml
- SWEHR actions https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40254743506
- EUROSEM actions https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40255588717

## 중요 잔여
- EUROSEM sediment budget 독립방정식/관측량 계측. 50mm/h net soil erosion 237937kg/14500m²(164t/ha/event)는 모델 출력이며 현장 적용 금지.
- SWEHR 5 case numerical mass closure complete; root and canopy SF/TF not coupled; high-resolution field topography, soil hydraulics and grain classes needed.
- 2026-09-22 Iber+ selected primary event hydro-erosion in MASTER, do not silently replace with SWEHR.
