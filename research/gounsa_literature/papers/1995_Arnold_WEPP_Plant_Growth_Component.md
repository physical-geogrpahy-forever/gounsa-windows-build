# 서지정보
Arnold, J. G., Weltz, M. A., Alberts, E. E., & Flanagan, D. C. (1995). *Plant Growth Component*. In D. C. Flanagan & M. A. Nearing (Eds.), USDA-Water Erosion Prediction Project: Hillslope Profile and Watershed Model Documentation. NSERL Report No. 10, Chapter 8.

# 이 문서를 찾은 이유
WEPP가 vegetation state를 단순 cover가 아니라 biomass/root pools로 동적으로 계산하는지 확인하기 위해 검토했다.

# 연구 유형
- official technical model documentation

# 공간 구조
WEPP plant-growth module coupled to hillslope erosion.

# 적용 환경
- cropland
- rangeland vegetation

# 핵심 과정
- plant growth
- aboveground biomass
- root biomass
- root depth
- LAI
- canopy height/cover

# 식생 입력/상태
- above-ground biomass
- live root biomass
- root depth
- LAI
- canopy cover
- canopy height
- root-to-shoot relations in cropland

# 핵심 식
Detailed crop/rangeland growth equations are retained in Chapter 8; this archive records the state-variable structure rather than reproducing every equation.

# 파라미터와 단위
Original WEPP units must be preserved.

# 고운사에 직접 사용할 수 있는 부분
Shows that WEPP root effects can be driven by dynamic vegetation pools, not only static cover.

# 새로운 coupling이 필요한 부분
Replacing WEPP plant growth with LPJ-GUESS is **new coupling**.

# 한계
WEPP vegetation model itself is not intended to replace LPJ-GUESS in Gounsa.

# 최종 판정
**core supporting technical source.**
