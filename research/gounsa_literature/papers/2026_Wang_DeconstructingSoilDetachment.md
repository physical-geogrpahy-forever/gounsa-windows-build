# 서지정보
Wang, J., Li, J., Liu, G., Ma, W., & Wang, B. (2026). Deconstructing soil detachment: Integrated assessment of soil properties, root characteristics, and hydraulics under diverse land uses on the Chinese Loess Plateau. *CATENA, 274*, 110515.

# 이 논문을 찾은 이유
cropland, grassland, shrubland, woodland를 포괄하는 최신 detachment prediction framework를 확인하기 위해 검토했다.

# 연구 유형
- 실험 + 통합 예측모델

# 공간 구조
- plot/flume

# 적용 환경
- cropland
- grassland
- shrubland
- woodland

# 핵심 과정
- soil detachment

# 식생 입력
- specific root length
- root characteristics
- soil structure

# 핵심 식
flow velocity, water-stable aggregates, specific root length를 결합한 detachment framework로 정리됨.

# 파라미터와 단위
flow velocity, aggregate stability, SRL.

# 원 논문의 구현 범위
8개 식물종 및 다양한 land use의 detachment controls를 통합.

# 고운사에 직접 사용할 수 있는 부분
Hydraulics + SoilStructure + PFT-specific root traits를 동시에 써야 한다는 최신 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root traits와 고운사 hydraulic variables를 이 식에 연결하면 새로운 coupling.

# 한계
2D landscape evolution model이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2026.110515
