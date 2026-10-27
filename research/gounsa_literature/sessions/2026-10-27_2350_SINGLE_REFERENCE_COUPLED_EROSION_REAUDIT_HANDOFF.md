# 2026-10-27 23:50 단일 레퍼런스 결합모델 재분류 인계서

## 이번 세션의 판정 변화
- '단일 모델'은 하나의 계산 엔진이 아니라 하나의 **원논문에서 제시하고 실제 결합한 완성된 수치모델**을 의미한다. 2~3엔진 결합을 이유로 제외한 이전 판단을 철회했다.
- 원논문상의 물리 성숙도와 **실제로 공개된 동일 판본의 통합 소스**, published native 5~10cm 해상도, canopy ON 상태의 sediment mass/bed numerical convergence를 엄격히 분리한다.
- 고운사 필수: 단일 강우사상 10~50mm/h, 억새·참나무 맹아·나지·혼재, LAI/canopy water interception ON/OFF, rainfall/sheet/rill detachment, freely XY sediment transport and local erosion/deposition/DEM update.

## 오늘 선별한 7개
1. Kim, Ivanov & Katopodes (2013), tRIBS–OFM–Hairsine–Rose, DOI 10.1002/wrcr.20373. 완성된 단일논문 통합 2D SWE 강우/유수 침식퇴적+수관 수문. 현 GitHub tRIBS에는 FEaST Hairsine–Rose 침식 엔진 없음. **0.005m2 요소는 1D 사실상 실험에서 hydrology OFF**, 초고해상도 canopy+2D 실행선례 아님.
2. Maggioli et al.(2022), LISEM, DOI10.3389/fevo.2022.765148: 실제5cm canopy LAI water storage + erosion 연구는 최강 선례이나 사용 유동은 kinematic; exact research source 없고 공개7.5.2 native sediment stability 실패. Work에서 별도 복구 시도 중.
3. Long & He (2009/2010), modified-Gash interception+2D SWE+Green-Ampt+erosion/deposition+bed change. Exact source, Δx, drip KE 증거 미확보.
4. Wei et al.(2017) forest TREX, DOI10.1016/j.jher.2017.09.003: 산림수관+2D diffusive+rain/flow erosion/transport 논문 있으나 실제90m, exact improved code 비공개/미확보.
5. Jiang et al.(2025) AHMS-SED, DOI10.1029/2024MS004593: open canopy/drip source & coupled sediment model; actual20km, dedicated sed2d file not linked, free SWE 부족.
6. Feng et al.(2026) ELM–TELEMAC–GAIA, DOI10.1029/2025WR042040: one-reference coupled 3-engine model, Zenodo source DOI10.5281/zenodo.18331808, actual30m; upland hill erosion not changing land bed, GAIA does channel/floodplain morphology.
7. Cea et al.(2024) Iber+, DOI10.1016/j.envsoft.2024.106098: excellent 2D rainfall+flow multiclass Exner, author research binary DOI10.57745/UFEK4L; native canopy interception lacking, source collaborators only, 5cm laboratory element is 5cm x 2m quasi1D.

## 이미 반증된 부분을 반복하지 말 것
- Single-reference model rejection based only on count of engines.
- Kim2013 0.005m2 plot size ≠ active canopy+XY 2D all coupled at 7cm.
- ELM-TELEMAC-GAIA Exner river/floodplain ≠ hillslope rain-driven bed erosion updates.
- Maggioli exact code and native 7.5.2 same edition.
- T1 Iber+ 5cm along slope ≠ genuine 5cm x5cm 2D field.
- SHETRAN sub10cm code extension without published precedent, Wflow sediment LDD vs genuine XY.

## 결과 저장
- New decision: decisions/2026-10-27_SINGLE_REFERENCE_MULTI_ENGINE_FULL_RECLASSIFICATION.md
- MASTER.md top-level corrected verdict and references.
- No new paper DOI found: existing canonical records reused; no duplicate paper files.

## 다음 채팅 최우선
- First: exact published Kim2013/2014 integrated FEaST executable source and availability; if not, mark source gap and focus Long–He research version.
- Second: official Long & He publication code/data and mesh dimensions.
- Third: Wei 2017 improved forest TREX (do not substitute generic TREX).
- Keep LISEM numerical fix delegated Work, demand native mass closure and canopy-ON/OFF from same version before selection.
