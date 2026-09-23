# 서지정보
Haga, C., Hotta, W., Inoue, T., Matsui, T., Aiba, M., Owari, T., Suzuki, S. N., Shibata, H., & Morimoto, J. (2022). Modeling Tree Recovery in Wind-Disturbed Forests with Dense Understory Species under Climate Change. Ecological Modelling, 472, 110072. https://doi.org/10.1016/j.ecolmodel.2022.110072

# 이 논문을 찾은 이유
고운사 후보가 실제 fine geographic grid에서 tree cohort와 명시적 understory cohort를 동시에 추적하고, roots/litter/C/N 및 succession까지 계산한 동아시아 온대림 선례가 있는지 확인하기 위해 검토했다.

# 연구 유형
- forest landscape numerical simulation
- LANDIS-II + NECN v6.3 확장
- 공개 project repository가 존재

# 공간 구조
- spatially explicit LANDIS-II raster landscape
- 연구 전체 분석에 10 m x 10 m fine landscape representation이 사용됨
- southern Hokkaido, Oshima-Hiyama National Forest의 wind-disturbed forest

# 하층식생 구현
- Sasa kurilensis를 별도 understory species로 모델에 넣음
- 공개 입력파일에서 `sasa_spp`는 단순 cover parameter가 아니라 정상 LANDIS species-age/biomass cohort로 설정됨
- longevity, maturity, shade tolerance, fire tolerance, seed dispersal, vegetative reproduction, sprout age, post-fire resprout을 갖음
- initial community에서도 `sasa_spp age (biomass)` 형태의 실제 cohort로 존재

# NECN 생체량/뿌리/litter 경로
공개 `NECN-succession_donan_v3.1.0.txt`에서 `sasa_spp`가 교목과 동일하게 다음 parameter를 가짐.
- Leaf lignin
- FRoot lignin
- Wood lignin
- CRoot lignin
- Leaf C:N
- FRoot C:N
- Wood C:N
- CRoot C:N
- litter C:N
- coarse-root fraction
- fine-root fraction
- monthly max NPP
- biomass limit
따라서 Sasa는 실제 NECN plant biomass, root, litter, C/N pathway를 이용한다.

# 천이와 경쟁
- tree cohorts와 Sasa cohort가 establishment and growth conditions를 공유
- Sasa density/biomass가 tree establishment를 제한
- snowpack and climate response가 Sasa mortality를 바꾸고, 그 결과 tree recovery와 species composition이 변화
- post-disturbance tree recovery를 2100까지 모의

# 토양/수문
공개 NECN config에 실제 raster inputs:
- SoilDepthMap
- SoilDrain
- BaseFlow
- StormFlow
- FieldCapacity
- WiltingPoint
- sand/clay
- surface/soil SOM C/N
- dead surface wood and dead coarse roots
따라서 criterion 3은 매우 강함.

# 시간 구조
- NECN ecosystem calculations are monthly-scale internally
- LANDIS succession timestep은 설정에 따라 annual/multi-year이며 Haga config는 Timestep 1을 사용
- 따라서 고운사 고정 criterion 5, 즉 physiology/hydrology <=1 day에는 부합하지 않음

# 적용 환경
- 실제 wind-disturbed temperate/hemiboreal mountain forest in northern Japan
- climate, snow, understory, tree regeneration interactions를 landscape scale에서 평가

# 고운사에 직접 사용할 수 있는 부분
- 동아시아 온대림에서 understory species 자체를 age/biomass cohort로 처리하는 명확한 precedent
- 10 m geographic raster에서 woody + understory succession이 가능함을 보여주는 사례
- root/litter/C/N을 understory에도 동일한 species parameter pathway로 부여하는 방식

# 새로운 coupling이 필요한 부분
- daily/hourly event ecohydrology
- storm-time soil depth/state updates
- geomorphic erosion/deposition and root exposure

# 한계
- temporal resolution이 고운사 criterion 5를 통과하지 못함
- understory가 Sasa 한 계열에 집중되어 있어 다종 herb community보다 단순

# 최종 판정
- 공간과 하층식생 구조의 매우 강한 보조근거
- 5조건 전체 후보로는 시간해상도 때문에 탈락
- 그러나 "fine-grid geographic cohort + explicit understory cohort + roots/litter + succession"의 가장 직접적인 published precedent 중 하나
