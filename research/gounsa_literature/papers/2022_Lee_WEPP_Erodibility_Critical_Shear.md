# 서지정보
Lee, S., Chu, M. L., Guzman, J. A., & Flanagan, D. C. (2022). *Modeling soil erodibility and critical shear stress parameters for soil loss estimation*. Soil & Tillage Research, 218, 105292. DOI: 10.1016/j.still.2021.105292.

# 이 논문을 찾은 이유
WEPP 내부에서 `Ki`, `Kr`, `τc`가 vegetation/root 상태에 의해 실제로 어떻게 조정되는지 확인하기 위해 검토했다.

# 연구 유형
- 모델 분석/parameterization
- WEPP 내부구조 검증

# 공간 구조
- WEPP 기반
- 기본 hillslope profile은 1D 계열

# 적용 환경
- 농경/토양침식 중심

# 핵심 과정
- interrill erodibility
- rill erodibility
- critical shear stress

# 식생 입력
- canopy
- ground cover
- live root biomass
- dead root biomass
- soil consolidation
- freeze-thaw

# 핵심 식
채팅에서 확인된 WEPP 구조상 root biomass는 `Ki`와 `Kr` 조정에 직접 들어간다.
Cropland 계열의 확인식:
```
CKidr = exp(-0.56 * dr)
CKilr = exp(-0.56 * lr)

CKrdr = exp(-2.2 * dr)
CKrlr = exp(-3.5 * lr)
```
`dr`: dead root mass, `lr`: live root mass.

# 파라미터와 단위
root mass의 정확한 단위와 WEPP 내부 normalization은 Chapter 7과 함께 사용해야 하며 원문 표 기준으로 구현한다.

# 원 논문의 구현 범위
WEPP daily erodibility/critical-shear parameter behavior를 설명하고 surrogate regression도 제시한다.

# 고운사에 직접 사용할 수 있는 부분
WEPP에 root biomass effect가 실제 존재함을 확인하는 핵심 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS FineRootC를 WEPP root-mass 변수로 변환하는 절차는 별도 정의가 필요하며, Wu/Iber 같은 2D 엔진에 넘기면 **새로운 coupling**이다.

# 한계
논문 자체의 LAI/DAYS/GC surrogate regression은 고운사에서 사용하지 않는 방향으로 판정했다.

# 최종 판정
**채택: WEPP biomass-erodibility 근거문헌.**

## 2026-09-21 현재 채팅 최종 보정
- **현재 유수침식 모델 계보에서 매우 중요한 모델 연구.** WEPP는 interrill erodibility Ki, rill erodibility Kr, critical shear stress를 분리하고 live/dead root biomass, residue, cover 등의 시간변화를 이용해 이들을 갱신한다.
- 특히 root biomass가 Ki와 Kr에 서로 다른 강도로 작용하는 구조는 `FineRootC -> Ki/Kr` coupling의 직접적인 published precedent이다.
- 단, WEPP의 hillslope routing은 고운사에서 요구하는 genuine 2D 산지 지표유출 엔진이 아니다. WEPP 자체를 최종 erosion engine으로 채택하지 않는다.
- WEPP의 biomass-dependent Ki/Kr를 Wu 2D 또는 HighLand 유동장에 연결하는 것은 **새로운 coupling**이다.
