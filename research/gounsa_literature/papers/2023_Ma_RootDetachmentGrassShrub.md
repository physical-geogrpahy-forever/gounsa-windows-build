# 서지정보
Ma, J., Ma, B., Li, Z., et al. (2023). Effect of roots on the soil detachment process in grassland and shrubland. *Land Degradation & Development, 34*, 3017-3032.

# 이 논문을 찾은 이유
grassland와 shrubland의 root effect를 직접 비교해 PFT별 차이를 확인하기 위해 검토했다.

# 연구 유형
- 현장/실험

# 공간 구조
- flume / plot

# 적용 환경
- grassland
- shrubland

# 핵심 과정
- soil detachment

# 식생 입력
- fine roots
- coarse roots
- root-soil properties

# 핵심 식
root effect는 주로 rill erodibility 변화로 나타났으며 fine fibrous roots가 중요하다고 정리됨.

# 파라미터와 단위
root-size classes와 soil parameters.

# 원 논문의 구현 범위
grass와 shrub root-system 차이를 실험적으로 비교.

# 고운사에 직접 사용할 수 있는 부분
FineRootC를 PFT별로 보존하고 root diameter/architecture를 써야 할 근거.

# 새로운 coupling이 필요한 부분
실험결과를 erosion model coefficient로 이식하면 새로운 coupling.

# 한계
수치 유역모델이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1002/ldr.4664
