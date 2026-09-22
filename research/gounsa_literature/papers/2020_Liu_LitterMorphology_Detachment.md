# 서지정보
Liu, J., Zhang, G.-H., et al. (2020). Effects of soil-incorporated plant litter morphological characteristics on the soil detachment process in grassland on the Loess Plateau of China. *Science of the Total Environment, 705*, 134651. https://doi.org/10.1016/j.scitotenv.2019.134651

# 이 논문을 찾은 이유
같은 litter mass라도 형태와 soil-contact area가 erosion resistance를 다르게 만드는지 확인하고, LPJ SurfaceLitC를 단순 mass-only coefficient로 쓰는 자의성을 피하기 위해 검토했다.

# 연구 유형
- flume experiment
- litter morphology experiment

# 공간 구조
- soil core / concentrated flow

# 적용 환경
- Loess Plateau grassland soils

# 핵심 과정
- litter length density
- litter surface area density
- litter volume ratio
- soil detachment capacity
- rill erodibility

# 식생 입력
- litter mass rate 0.7 kg m^-2
- litter length classes <0.5 to 8 cm
- litter morphology

# 핵심 결과
- same litter mass에서도 species/fragment length에 따라 erosion resistance가 달라짐
- litter surface area density(LSAD)가 rill erodibility effect를 가장 잘 대표
- soil-contact area가 핵심 control

# 고운사에 직접 사용할 수 있는 부분
- SurfaceLitC mass만으로 K_d modifier를 정하면 안 된다는 근거
- 최소한 litter mass + morphology/contact-area state가 필요
- 독립 flume measurement가 가장 안전한 parameter source

# 새로운 coupling이 필요한 부분
LPJ SurfaceLitC -> LSAD 변환은 litter specific leaf/fragment area information이 필요하며 new coupling이다.

# 최종 판정
- **litter effect는 mass-only가 아니라 LSAD/contact-area를 우선 고려**
- generic litter multiplier 금지

# 참고 링크 / DOI
https://doi.org/10.1016/j.scitotenv.2019.134651
