# WaNuLCAS: LAI 수관차단+식생 침식 공개 문헌과 공간구조 원본 대조

## 모델/근거
- van Noordwijk, M., Lusiana, B., & Khasanah, N. (2004). *WaNuLCAS 3.01: Background on a model of Water, Nutrient and Light Capture in Agroforestry Systems*. ICRAF technical manual. https://www.cifor-icraf.org/publications/region/sea/publications/softcopy/BK0060-04.pdf
- Onsamrarn, W., Chittamart, N., & Tawornpruek, S. (2020). Performances of the WEPP and WaNuLCAS models on soil erosion simulation in a tropical hillslope, Thailand. *PLOS ONE*, 15(11), e0241689. https://doi.org/10.1371/journal.pone.0241689
- 현재 GitHub `https://github.com/degi/wanulcas`의 WaNuLCAS 5.0 Shiny UI는 **원래 2004 v3.01 STELLA 전체모델과 동일 SHA 및 동일 erosion solver임을 검증하지 않음**.

## 탐색 목적
식생의 구조적 상태(LAI, tree-crop canopy, root traits)를 입력받아 수관차단과 유수침식/퇴적을 함께 계산하는 기존 단일모델이므로 고운사 강우사상 5–10cm 수치모델 요건과 비교.

## 확인된 과정과 핵심 식
- 2004 manual Chapter 3.2.5: tree+crop canopy 최대저류용량은 water film thickness × LAI, 증발산 이전에 수관수분 증발 우선.
- Chapter 3.2.6–3.2.7: 원토양 입자의 박리/이동/퇴적과 Rose equation/USLE 선택 가능. 최신 기초인 2020 PLOS 논문은 강우 유출과 유사량을 실측 비교.
- Rose 형태 일별 토양손실 `E_loss [kg m^-2] = Q * E / 10` (정확 단위/관측 구획 문맥은 2020 paper 확인); 표토 피복 및 경사 기여가 있음.

## 공간과 시간, 소스 한계
- WaNuLCAS는 **tree/crop/soil vertical layers + 수평 구획(zones) 기반의 농림복합시스템**임. 2D SWE의 (q_x,q_y)와 동적 유사농도 연립 수송 격자가 아니다. 일부 문헌의 'simplified 2D erosion'은 사면 단면/구획 재배분이며 freely spreading 2D hydrodynamics와 동의어가 아니다.
- 전반적으로 일별 기상 구동; published 5cm 또는 10cm full 2D erodible hillslope storm solver와 동일하지 않다.
- PLOS 2020 식생 복합재배에서 성능을 보였으나 5cm 침식/퇴적 지형지도와 물리적/수치적 안정성 입증 아님.
- modern Shiny source가 original STELLA equation-native erosion 코드라고 입증할 수 없음.

## 고운사 적용 부분과 새로운 coupling
LAI storage 계보와 tree-crop erosion comparison은 보조문헌 근거. 자유 XY 유동을 넣거나 모델을 연결하려면 새로운 결합으로 표시하고, 사용자 단일 원본 조건을 충족하지 않음.

## 최종 판정
**탈락(주 유수침식 엔진), 보조근거(LAI 차단과 식생 침식).**

## 참고
https://www.cifor-icraf.org/publications/region/sea/publications/softcopy/BK0060-04.pdf
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241689
