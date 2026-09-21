# 서지정보
Shouse, M. L., & Phillips, J. D. (2016). Soil deepening by trees and the effects of parent material. Geomorphology, 269, 1-7.
DOI: 10.1016/j.geomorph.2016.06.031

# 이 논문을 찾은 이유
고운사와 같이 얕은 산림토양에서 tree-root/bedrock interaction이 실제로 soil-regolith thickness를 국소적으로 증가시키는지, 그리고 그 효과가 특수한 steep bedding에서만 가능한지 확인하기 위해 검토했다.

# 연구 유형
- 현장 비교 연구
- stump site와 인접 non-tree site의 depth-to-bedrock paired comparison
- 수치모델 아님

# 공간 구조
- Ouachita Mountains, Arkansas
- Cumberland Plateau, Kentucky
- 각 tree/stump microsite와 1 m 이내 인접 지점의 soil depth를 비교
- hillslope 전체 2D 모델이 아니라 국소 paired field design

# 적용 환경
- 산림
- Paleozoic sedimentary rocks dominated by sandstone and shale
- strongly dipping/contorted strata와 flat-bedded strata를 비교

# 핵심 과정
- root penetration of joints, fractures, bedding planes
- biomechanical widening / regolith deepening
- root-channel preferential water flow 가능성
- local soil-thickness heterogeneity

# 식생 입력
- 과거 큰 나무가 점유했던 stump microsite
- biomass, RLD, FineRootC의 연속 정량입력은 없음

# 핵심 식
직접적인 soil-production rate equation은 제시하지 않는다.
핵심은 stump와 adjacent site 사이 depth-to-bedrock 차이의 paired 통계 비교이다.

# 파라미터와 단위
- soil depth / depth to lithic or paralithic contact: 길이
- adjacent comparison radius: 1.0 m 이내
- 기존 Ouachita 연구에서는 tree-occupied site가 adjacent site보다 깊었던 경우가 91%였다고 배경에서 보고

# 원 논문의 구현 범위
- Ouachita의 strongly dipping sedimentary rocks와 Cumberland Plateau의 flat-bedded sedimentary rocks를 비교
- 두 지역 모두 stump 아래 토양이 인접지보다 유의하게 깊었음
- 두 지역의 stump-adjacent difference 자체는 통계적으로 유의하게 다르지 않았음
- 즉 tree-induced local deepening이 steeply dipping geology에만 한정되지 않음을 지지

# 고운사에 직접 사용할 수 있는 부분
1. 얕은 soil-regolith에서 root-rock contact가 soil depth heterogeneity를 만들 수 있다는 현장근거.
2. `root effect`를 단순히 slope/bedding orientation의 대리변수로 만들면 안 된다.
3. fracture/joint accessibility와 root access가 local production/deepening sensitivity에 들어갈 수 있다는 근거.

# 새로운 coupling이 필요한 부분
`LPJ-GUESS root state + inherited fracture accessibility -> local biomechanical soil-production sensitivity`는 published equation이 아니며 NEW COUPLING이다.
Mode C sensitivity의 구조적 근거로만 사용하고 coefficient는 만들지 않는다.

# 한계
- stump-adjacent depth difference는 누적된 tree legacy를 반영하며 연간 생산률이 아니다.
- sedimentary parent material에 sandstone과 shale이 함께 포함되어 sandstone-only rate를 제공하지 않는다.
- chemical weathering과 biomechanical deepening을 분리한 flux가 없다.
- tree effect라는 해석에는 microsite 차이를 tree history로 귀속하는 가정이 포함된다.

# 최종 판정
- 보조근거
- 역할: vegetation-sensitive local soil deepening과 root-rock contact feedback의 field support
- `P_sand` calibration에는 사용하지 않음

# 참고 링크 / DOI
- https://doi.org/10.1016/j.geomorph.2016.06.031