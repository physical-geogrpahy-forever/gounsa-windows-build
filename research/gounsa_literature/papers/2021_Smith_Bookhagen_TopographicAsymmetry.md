# 서지정보
Smith, T., & Bookhagen, B. (2021). Climatic and Biotic Controls on Topographic Asymmetry at the Global Scale. *Journal of Geophysical Research: Earth Surface, 126*(1), e2020JF005692. DOI: 10.1029/2020JF005692.

# 이 논문을 찾은 이유
aspect에 따른 식생 차이가 사면형과 전지구적으로 일관된 연관성을 갖는지 확인하여 고운사 aspect sensitivity의 일반성을 평가하기 위해 검토했다.

# 연구 유형
- global empirical topographic analysis
- remote sensing + DEM analysis

# 공간 구조
- global 0.25° analysis windows
- terrain aspect and slope distributions
- vegetation/aspect asymmetry

# 적용 환경
- global terrestrial landscapes
- broad climate, lithology, tectonic settings

# 핵심 과정
- insolation asymmetry
- microclimate
- vegetation-cover asymmetry
- topographic asymmetry
- drainage-network form

# 식생 입력
세 global vegetation datasets:
- Landsat vegetation continuous fields
- MODIS NDVI
- TanDEM-X forest fraction

# 핵심 결과
global scale에서:
- pole-facing terrain이 평균적으로 더 steep
- 이 경향은 mid-latitude, tectonically quiescent, vegetated landscapes에서 특히 강함
- opposing aspects는 vegetation cover, climate and insolation에 체계적인 차이를 보임

논문은:
```
insolation
 -> microclimate
 -> vegetation
 -> geomorphic process balance
 -> topographic asymmetry
```
의 broad consistency를 지지한다.

# 고운사에 직접 사용할 수 있는 부분
- aspect를 단순 geometric covariate가 아니라 ecohydrologic-weathering forcing으로 취급할 근거
- LPJ-GUESS가 aspect별 vegetation recovery를 다르게 만들 경우 지형과정도 달라질 수 있다는 broad-scale consistency check

# 새로운 coupling이 필요한 부분
이 논문으로:
```
vegetation cover -> P_sand
```
또는
```
vegetation cover -> q_hill
```
계수를 만들 수 없다.

# 한계
- modern vegetation data vs long-term topography의 timescale mismatch
- empirical global association
- chemical weathering 직접 측정 아님
- root biomass/process model 아님

# 최종 판정
- **보조 채택: global aspect-vegetation-topography constraint**
- process equation source로 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1029/2020JF005692
