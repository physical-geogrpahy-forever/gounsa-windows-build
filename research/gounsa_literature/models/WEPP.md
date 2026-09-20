# WEPP 계보

## 고운사에서 조사한 이유
interrill과 rill을 분리하면서 식생과 뿌리 상태가 erodibility에 실제로 들어가는 published numerical model 계보를 찾기 위해 검토했다.

## 모델 구조
- hillslope profile 기반 process model
- interrill erodibility Ki
- rill erodibility Kr
- critical shear stress tau_c
- plant growth, residue, live/dead root state가 일별로 변함

## 식생 입력
- canopy/ground cover
- residue
- live root biomass
- dead root biomass

## 이번 채팅에서 확인한 핵심
Lee et al. (2022) 분석을 통해 WEPP 내부에서 root biomass가 Ki와 Kr의 시간변화 조정에 직접 들어가는 구조를 확인했다. cropland 계열에서 live/dead root mass에 대한 exponential adjustment가 사용된다.

## 고운사에 사용할 수 있는 부분
- interrill와 rill을 서로 다른 erodibility로 처리하는 구조
- FineRootC를 Ki/Kr 조정에 사용하는 published precedent
- live/dead root를 분리할 수 있다는 점

## 사용할 수 없는 부분
- WEPP 자체의 1D hillslope routing을 고운사 최종 2D 엔진으로 사용하지 않는다.
- 농경지용 cover-management 구조를 그대로 산림에 이식하지 않는다.

## 새로운 coupling
`LPJ-GUESS FineRootC/LitterC -> WEPP형 Ki/Kr modifiers -> Wu 2D 또는 HighLand 2D flow field`는 단일 published model이 아니라 **새로운 coupling**이다.

## 관련 논문
- `../papers/2022_Lee_WEPP_Erodibility_Critical_Shear.md`

## 최종 판정
- **기능 채택**: biomass-dependent Ki/Kr의 근거
- **엔진 탈락**: 고운사 genuine 2D 최종 수문-침식 엔진으로는 사용하지 않음
