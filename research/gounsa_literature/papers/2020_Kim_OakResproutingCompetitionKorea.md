# 서지정보
Kim, J., Lim, J.-H., Shin, M., Han, S.-H., & Kang, W. (2020). Oak Resprouting Survival and Competition for 19 Years after Wildfire in the Republic of Korea. *Forests, 11*(5), 515. https://doi.org/10.3390/f11050515

# 이 논문을 찾은 이유
산불 후 참나무 맹아가 장기적으로 얼마나 생존하고 경쟁우위를 유지하는지, 그리고 지형/토양조건과 우점이 어떻게 연결되는지 확인하기 위해 검토했다.

# 연구 유형
- 19-year postfire field monitoring
- competition/survival analysis

# 공간 구조
- forest stand/plots

# 적용 환경
- Republic of Korea
- wildfire-affected eastern mountain forest

# 핵심 과정
- stump resprouting
- survival
- self-thinning
- interspecific competition
- topographic filtering

# 식생 입력
- oak species
- stump sprouts
- species density/growth
- topographic setting

# 핵심 식
단일 geomorphic equation보다 장기 regeneration trajectory가 핵심이다.
초기 resprouts는 기존 stump/root resources를 이용하여 seedlings보다 빠르게 높이 성장하는 경쟁상 이점이 있다.
Q. mongolica 우점지는 ridge/upper mountain과 같은 지형조건과 연관되며, 토양/입지조건이 불리해 생장은 낮아도 높은 밀도가 지속될 수 있다.

# 파라미터와 단위
sprout survival, density, height/DBH, topographic position. 세부 회귀식은 원문 재검증 필요.

# 원 논문의 구현 범위
한국 산불 이후 oak resprouting의 19년 생존과 경쟁과정을 추적한다.

# 고운사에 직접 사용할 수 있는 부분
- oak dominance를 establishment suitability 하나로 결정하지 않을 근거
- `disturbance legacy -> resprout advantage -> long-term dominance` 경로
- ridge/poor-site conditions에서도 oak density가 유지될 수 있어 soil depth만으로 배제하면 안 됨

# 새로운 coupling이 필요한 부분
고운사 topography/soil-water state와 species-specific resprout survival/growth를 결합하는 것은 **새로운 coupling**이다.

# 한계
석력피복률을 직접 측정한 armour 연구가 아니다.

# 최종 판정
- 핵심 채택
- postfire oak competitive legacy의 핵심 국내근거

# 참고 링크 / DOI
https://doi.org/10.3390/f11050515
