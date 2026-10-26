# 2026-10-26 억새 및 참나무 맹아 생태수문형질 재검증 인계

## 완료
원본 코드 SWEHR 30계절형-강우 조건 water/independent sediment ledger 30/30 통과. EUROSEM 30/30 수문 물수지 통과, sediment mass 독립수지 미검증.
EUROSEM v3.6 manual PLANTH 입력 cm 발견: 기존 2.5m를 2.5cm로 실행한 예전 실험을 정정. 수정 native height case에서 DRIPKE 0→1.980338로 변하나 gross erosion 45986.5kg이 동일함을 확인; 에너지항→계산된 침식량 연결 검증 필요.
6개 가상 계절/재생 수관 endpoint ×5강우(10~50mm/h 1h) ×2 native engines 새 실행. 30mm/h EUROSEM oak early/dense runoff 4.098/3.392mm, grass early/dense 4.135/3.491mm. SWEHR exported sediment (t/ha/event) oak early .0044737/dense .00367994, grass early .00451832/dense .00378437. 순위변경은 실물 species ranking이 아닌 가상 상태 비교.
문헌 7편 새 papers 파일로 생성; INDEX 389편 갱신 및 MASTER 최신 링크/erratum 저장.
최종 결정 decisions/2026-10-26_OAK_MISCANTHUS_REAUDIT.md. 2026년 9월 Iber+ production 선택 유지.

## 원본코드 및 Actions
branch swehr-water-sediment-closure-20261026
experiments/rainfall_10_50/run_postfire_phenology_20261026.py
experiments/rainfall_10_50/verify_eurosem_native.py
experiments/rainfall_10_50/verify_swehr_closure.py
60-run corrected native: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40261338013
height kinetic original C F77 experiment: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40261969796

## 연구상 함정
EUROSEM stemflow and drip remerge as area-averaged surface forcing; per-stem base infiltration/excess runoff not evaluated. SWEHR receives homogeneous net rain only. Real oak stump bark/branch structure and M.sinensis culm position, rhizome RD/RLD, litter, hydrophobicity, fragments, rainfall drop kinetic energy need field quantification.
Annual measured TF/SF percentages from mature Quercus or M.×giganteus must not be repurposed into hourly postfire event parameters. PBASE definition and standard guide values have inconsistent physical interpretation; measure basal fraction locally. EUROSEM DERO=5m original demo exceeds shallow soil supply of Gounsa.
Important: recent manuscript Jo & Oh 2026 assesses Gounsa temple forestry but specific plot colocation unverified.

## Next step
Recheck native EUROSEM raindrop detachment and drip KE coupling by outputting actual integrated RDETIN/DRDTIN vs summed sediment on same one-plane test. Build mass-conservative 2D spatial source for SF with measured stem/rhizome distribution; repeat numerical stability and sensitivity against actual measured topo and soil hydraulic depth.
