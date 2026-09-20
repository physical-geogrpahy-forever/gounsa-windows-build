# 서지정보
Ma, J., Li, Z., Ma, B., Wang, C., Sun, B., & Shang, Y. (2022). Response mechanism of the soil detachment capacity of root-soil composites across different land uses. *Soil and Tillage Research, 224*, 105501.

# 이 논문을 찾은 이유
cropland, orchard, grassland, woodland에서 root-soil composite의 detachment response를 비교한 최신 parameterization 연구로 검토했다.

# 연구 유형
- 실험 + 예측모델

# 공간 구조
- plot/flume

# 적용 환경
- cropland
- orchard
- grassland
- woodland

# 핵심 과정
- soil detachment

# 식생 입력
- RLD
- RMD
- 토양 clay/organic matter

# 핵심 식
stream power, RLD, RMD, clay content, organic matter를 결합한 예측모델을 제시했으며 이 채팅 정리에는 `NSE=0.92`로 기록됨.

# 파라미터와 단위
stream power, RLD, RMD, clay, OM.

# 원 논문의 구현 범위
land-use별 hydrodynamic/root/soil controls를 비교.

# 고운사에 직접 사용할 수 있는 부분
root effect가 식생상태와 토양상태에 따라 saturating/piecewise할 수 있다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root state와 고운사 soil state를 prediction model에 연결하면 새로운 coupling.

# 한계
landscape evolution model이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.still.2022.105501
