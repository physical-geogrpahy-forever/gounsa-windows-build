# 서지정보
Tang, J., Miller, P. A., Persson, A., Olefeldt, D., Pilesjö, P., Heliasz, M., Jackowicz-Korczynski, M., Yang, Z., Smith, B., Callaghan, T. V., & Christensen, T. R. (2015). Carbon budget estimation of a subarctic catchment using a dynamic ecosystem model at high spatial resolution. Biogeosciences, 12, 2791–2808. https://doi.org/10.5194/bg-12-2791-2015

# 이 논문을 찾은 이유
LPJ-DH 계열이 2014년 단기 runoff 시험을 넘어 실제 장기 catchment vegetation dynamics와 탄소수지 연구에 사용됐는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델 장기 유역 적용 및 관측 비교
- Arctic-enabled LPJ-GUESS, LPJG-WHyMe-TFM

# 공간 구조
- Stordalen subarctic catchment
- 50 m 실제 geographic grid
- topographic flow routing을 포함하는 TFM 계보

# 적용 환경
- 산지, tundra, birch forest, peatland가 공존하는 subarctic catchment
- terrestrial과 aquatic carbon flux를 함께 평가

# 핵심 과정
- LPJ-GUESS dynamic vegetation
- topography-driven spatial hydrology
- peatland/permafrost 계보의 수문 및 biogeochemistry
- 장기 biomass, carbon flux, methane response

# 식생과 천이
- 미래에 birch forest densification과 tundra heath로의 encroachment가 emergent vegetation response로 모의됨
- LPJ-GUESS의 establishment, growth, competition, mortality 계보를 유지
- 50 m 공간에서 장기 vegetation composition/biomass 변화를 계산한 직접 선례

# 시간 구조
- LPJ-GUESS 생리 및 soil-water calculations는 daily 계보
- demography/allocation의 일부는 annual

# 토양/수문
- LPJG-WHyMe 및 TFM을 통해 peatland/permafrost hydrology와 topographic routing을 반영
- 고운사처럼 지형에 따른 공간 수분재분배가 vegetation state에 장기 feedback하는 precedent

# 고운사에 직접 사용할 수 있는 부분
- 50 m actual catchment grid에서 dynamic vegetation을 장기간 돌릴 수 있음을 입증
- terrain-controlled water redistribution이 vegetation biomass/composition에 누적 영향을 주는 구조

# 새로운 coupling이 필요한 부분
- 산불 직후 hourly geomorphic erosion/deposition
- dynamic soil depth, root exposure/burial
- 현대 LPJ-GUESS-RE 또는 PF-LPJG soil physics를 이 old 50 m routing 계보와 결합하는 작업

# 한계
- subarctic 특화 parameterization
- 고운사 온대 산림 PFT/종 parameterization 필요
- 현대 공개 source branch가 명확하지 않음

# 최종 판정
- 보조근거이자 LPJ-DH 계보 강화 자료
- LPJ-DH가 단발성 routing prototype이 아니라 장기 고해상도 catchment ecosystem model로 실제 사용되었음을 보여주는 중요한 선례
