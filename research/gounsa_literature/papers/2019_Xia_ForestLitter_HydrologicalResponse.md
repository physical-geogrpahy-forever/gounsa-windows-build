# 서지정보
Xia, L., Song, X., Fu, N., Cui, S., Li, L., Li, H., & Li, Y. (2019). *Effects of forest litter cover on hydrological response of hillslopes in the Loess Plateau of China*. CATENA, 181, 104076. DOI: 10.1016/j.catena.2019.104076.

# 이 논문을 찾은 이유
forest litter mass를 직접 조절하면서 interception, runoff, infiltration, soil erosion을 측정하고 WEPP로 분석한 연구가 surface-litter quantitative coupling을 제공하는지 확인하기 위해 검토했다.

# 연구 유형
- field rainfall-simulation experiment
- modified Merriam interception analysis
- WEPP hillslope model application

# 공간 구조
- 10 m x 1.5 m hillslope plots
- 5 degree slope

# 적용 환경
- Loess Plateau forest hillslope
- needle-leaf litter
- broad-leaf litter

# 핵심 과정
- rainfall interception
- runoff
- infiltration
- soil loss

# 식생 입력
Three direct litter masses:
- 300 g m^-2
- 500 g m^-2
- 800 g m^-2

Two rainfall intensities:
- 30 mm h^-1
- 60 mm h^-1

# 핵심 식
A modified Merriam interception model was used for litter rainfall interception.
WEPP was used to analyze runoff and soil erosion.

Key measured results:
- litter interception storage: approximately 0.55-2.10 mm
- about 1.8-9.2% of rainfall intercepted
- runoff reduction approximately 18.6% for needle litter and 25.9% for broadleaf litter relative to bare plots
- soil loss was strongly controlled once litter mass reached roughly 500 g m^-2

# 파라미터와 단위
- litter mass: g m^-2
- interception storage: mm
- rainfall intensity: mm h^-1
- runoff and soil loss

# 원 논문의 구현 범위
Links direct litter mass to interception and observed erosion, but the WEPP erosion application itself retains WEPP surface-cover/residue conventions.

# 고운사에 직접 사용할 수 있는 부분
1. forest litter mass has a measurable threshold/nonlinear erosion response
2. litter mass can separately control rainfall interception before considering soil detachment
3. needle and broadleaf litter differ, supporting PFT/litter-trait distinctions

# 새로운 coupling이 필요한 부분
Directly mapping LPJ-GUESS litter mass to a 2D rainfall-detachability coefficient remains a **new coupling**.

# 한계
- WEPP analysis does not solve the user requirement by itself because the erosion component ultimately uses WEPP surface residue/cover concepts
- Loess soil and gentle 5-degree slope
- not postfire

# 최종 판정
- **채택: forest exposed-litter mass/interception benchmark**
- not final surface-litter erosion equation

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2019.104076
