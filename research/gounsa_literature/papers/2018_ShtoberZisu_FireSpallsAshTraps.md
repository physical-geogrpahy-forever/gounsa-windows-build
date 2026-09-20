# 서지정보
Shtober-Zisu, N., Brook, A., Kopel, D., Roberts, D., Ichoku, C., & Wittenberg, L. (2018). Fire induced rock spalls as long-term traps for ash. *Catena, 162*, 88–99. https://doi.org/10.1016/j.catena.2017.11.021

# 이 논문을 찾은 이유
fire spall이 생성된 뒤 단순히 이동 가능한 조립질 퇴적물로만 작동하는지, 아니면 표면에 잔류하면서 재와 세립질 퇴적물을 포획하는 armour 또는 trap 역할도 하는지 확인하기 위해 검토했다.

# 연구 유형
- 현장조사
- 산불연대 비교
- 퇴적물과 화재지표 분석

# 공간 구조
- 이스라엘 Mt. Carmel과 Judean Hills의 지중해성 탄산염암 사면
- 1989, 2005, 2010, 2015년 산불지와 비산불 대조지 비교
- 수치 지형모델 아님

# 적용 환경
- 탄산염암 노두
- 얕은 토양
- 지중해성 산불환경

# 핵심 과정
- fire-induced spalling
- exfoliation
- ash trapping
- fine sediment trapping
- spall residence

# 식생 입력
- 직접적인 biomass 입력 없음
- 산불과 주변 식생은 배경조건

# 핵심 식
범용 fire-spall 수치식은 제시하지 않는다. 박리암편 위, 박리암편 아래, 노두 하부사면의 퇴적물을 비교하고 pH, EC, 색상, DRIFTS 기반 지표를 분석한다.

분석에는 hydroxylapatite, charcoal, 유기물 등이 포함되지만, 이 연구의 핵심 geomorphic 결과는 spall 아래에 재와 세립질 물질이 장기간 포획된다는 점이다.

# 파라미터와 단위
- pH
- EC
- 화재지표 분석값
- 시간경과: 화재 후 수년에서 수십 년

# 원 논문의 구현 범위
강한 산불이 암석표면의 spalling과 flaking을 촉진하고, 생성된 spall 일부가 장기간 현장에 남아 재, 유기물, 세립질 퇴적물을 포획하는 과정을 현장자료로 제시한다.

# 고운사에 직접 사용할 수 있는 부분
fire spall을 단순한 즉시 유출 sediment source로만 취급하지 않고, 일부를 stable/resident reservoir로 두어 surface armour과 fine-sediment trapping을 표현해야 한다는 근거.

# 새로운 coupling이 필요한 부분
```text
M_spall -> mobile fraction + stable fraction
stable spall -> CF_surface increase -> fine erosion protection
```
은 원 논문에 없는 새로운 coupling이다.

# 한계
- 탄산염암 환경
- spall cover에서 soil erodibility 또는 Manning n으로 가는 정량식을 제시하지 않음
- 고운사 암질과 직접 동일하지 않음

# 최종 판정
- fire spall의 residence와 armour 효과에 채택
- 정량 erosion coefficient는 별도 보정 필요

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2017.11.021
