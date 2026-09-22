# 서지정보
Cohen, S., Willgoose, G., & Hancock, G. (2015). The effects of sediment transport, weathering, and aeolian mechanisms on soil evolution. *Journal of Geophysical Research: Earth Surface*. https://doi.org/10.1002/2014JF003186

# 이 논문을 찾은 이유
mARM3D 이후 sediment transport와 soil evolution을 실제 landscape scale로 더 확장한 기존 모델 및 공개 소스 여부를 확인하기 위해 검토했다.

# 연구 유형
- spatial soil-landscape evolution model
- mARM5D

# 공간 구조
- raster landscape
- multilayer soil profile
- multiple particle-size classes

# 적용 환경
- long-term soil/regolith evolution

# 핵심 과정
- physical weathering
- surface armouring
- fluvial sediment transport
- diffusive/creep transport
- aeolian deposition
- soil-profile evolution

# 식생 입력
- 없음

# 핵심 식
mARM state-space grading/weathering framework에 lateral sediment processes를 확장한다.

# 파라미터와 단위
- particle grading
- layer depth
- armour depth
- weathering rate
- erosion/transport parameters
- creep/aeolian terms

# 원 논문의 구현 범위
soil profile grading, transport and weathering의 장기 공간진화를 계산한다.

# 공개 구현
CSDMS GitHub `csdms-contrib/marm5d`에 Fortran 90 source `5D_mARM5.6.F90`가 공개되어 있다.
소스에는 `SurfaceGrad`, `ProfileGrading`, `WeatheringTrans`, `ErosionGrad`, soil-depth 계산 등이 명시적으로 구현되어 있다.

# 고운사에 직접 사용할 수 있는 부분
- paper formula만 재구성할 필요 없이 실제 공개 코드를 참고/이식 가능
- surface/subsurface PSD와 physical weathering을 mass-conserving하게 갱신
- 100년 장기 상태 updater 후보

# 새로운 coupling이 필요한 부분
modern 2D hydrology/erosion solver와의 연결은 new software coupling.

# 한계
자체 hydrology와 erosion transport는 현대 2D postfire runoff engine보다 단순하며, 원 site calibration을 고운사에 그대로 이식하면 안 됨.

# 최종 판정
- **공개 구현이 있는 armour/weathering/profile 핵심 후보**
- hydrology/erosion 전체 엔진으로는 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1002/2014JF003186
https://github.com/csdms-contrib/marm5d
