# 서지정보
Hlaváčiková, H., Novák, V., & Šimůnek, J. (2016). The effects of rock fragment shapes and positions on modeled hydraulic conductivities of stony soils. *Geoderma, 281*, 39-48. https://doi.org/10.1016/j.geoderma.2016.06.034

# 이 논문을 찾은 이유
고운사처럼 매립 석력이 많은 산지토양의 effective hydraulic conductivity를 단순 석력비 보정식이 아니라, 실제 rock-fragment geometry를 가진 Richards-equation model로 계산할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- numerical experiment
- HYDRUS-2D 중심, 제한적 3D simulation
- Darcy unit-gradient analogue

# 공간 구조
- explicit embedded rock fragments in 2D/3D soil domain

# 적용 환경
- hypothetical stony mountain soils

# 핵심 과정
- saturated water flow
- rock-fragment obstruction
- shape/orientation/distribution effects
- effective saturated hydraulic conductivity

# 식생 입력
- 없음

# 핵심 식
Richards/Darcy numerical solution으로 heterogeneous stony domain을 직접 계산하고, 계산된 flux에서 bulk effective saturated hydraulic conductivity를 산정한다.

# 파라미터와 단위
- volumetric stoniness: 0.07-0.50 cm3 cm-3
- fine-soil hydraulic properties
- rock-fragment shape
- fragment orientation
- spatial distribution
- Ksat

# 원 논문의 구현 범위
sphere, ellipsoid, pyramid와 다른 orientation/distribution을 explicit geometry로 넣었다.
stoniness 0.07-0.50에서 relative effective Ksat가 크게 감소했으며, 같은 stoniness에서도 fragment orientation과 distribution에 따라 값이 달라졌다.

# 고운사에 직접 사용할 수 있는 부분
- 매립 석력이 많은 토양에서 RF fraction만으로 hydraulic conductivity를 정하는 것은 불충분하다는 근거
- HYDRUS-2D/3D를 이용한 geometry-explicit numerical homogenization이라는 기존 모델 경로
- 고운사 석력 geometry를 대표단면/REV로 만들어 effective K를 계산하는 benchmark 후보

# 새로운 coupling이 필요한 부분
HYDRUS에서 산정한 effective hydraulic properties를 Iber+ 또는 LPJ-GUESS로 전달하는 것은 새로운 coupling이지만 동일 물리량의 전달이다.

# 한계
- rock fragments를 impermeable inclusion으로 가정한 사례
- lacunar pore, root macropore, fragment-soil contact gap 등은 기본 시나리오에 직접 포함되지 않음
- erosion model이 아님

# 최종 판정
- 핵심 채택 후보
- 고석력 조건에서 GEM을 맹목적으로 쓰지 않기 위한 geometry-explicit benchmark

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2016.06.034
