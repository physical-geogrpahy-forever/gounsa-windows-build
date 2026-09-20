# Root reinforcement model lineage

## 범위
고운사 문헌검토에서 root biomass, root mechanics, root cohesion, shallow landslide 연결을 통합한다.

## 역사적 계보
- Waldron (1977): root-permeated soil shear resistance
- Wu, McKinnell & Swanston (1979): tree roots and landslide stability
- Ziemer (1981): forested-slope root strength
- Sidle (1991): vegetation management 후 root cohesion change
- Hales (2018): biome-scale root biomass -> root area -> tensile force -> root cohesion

## 핵심 물리경로
`root biomass -> root cross-sectional area -> tensile failure force -> root cohesion`

Hales (2018)에서 modified Wu/Waldron 형태 `Cr = r * F / Ds`를 사용한다.

## 고운사 적용
유수침식의 root protection coefficient와 shallow-landslide root cohesion은 같은 변수가 아니다. FineRootC가 두 경로에 들어가더라도 서로 다른 transfer function을 사용해야 한다.

## 새로운 coupling
LPJ-GUESS FineRootC를 root dry mass, depth profile, root area distribution, tensile strength parameter로 바꾸는 과정은 새로운 coupling이다.

## 관련 논문
- ../papers/2018_Hales_RootReinforcementSlopeStability.md

## 판정
- shallow landslide 모듈을 활성화할 때 핵심 계보
- 현재 기본 유수침식 모델과는 분리
